#!/usr/bin/env python3
"""Build the Connectry brand guidelines PDF from this repository.

  python3 tools/build_brand_pdf.py <component-shots-dir> <out.pdf>

<component-shots-dir> holds <Component>.png renders of project/components/*/preview.html
(tools/render_previews.py makes them). Pages are 1920 x 1080, the brand's slide grid.
Everything is read from project/: the README brand book, the guideline sections, tokens.json,
the asset groups and the component READMEs. Nothing is retyped by hand except section intros.
"""
import html
import json
import pathlib
import re
import sys
import tempfile

import markdown
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
P = ROOT / 'project'
SHOTS = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
WORK = pathlib.Path(tempfile.mkdtemp(prefix='brandpdf-'))
IMG = WORK / 'img'
IMG.mkdir()

tokens = json.loads((P / 'tokens.json').read_text())
RETIRED = {'It acts before you ask.': 'It takes care.'}  # retired 2026-09-23 (10-positioning)

W, H = 1920, 1080


def esc(s):
    return html.escape(str(s))


def md(text):
    text = re.sub(r'(?m)^# .*\n', '', text, count=1)  # page carries the title
    return markdown.markdown(text, extensions=['tables', 'fenced_code'])


def jpg(src, name, maxw=1800, q=84):
    """Re-encode an image for the PDF; returns a file:// path."""
    dst = IMG / (name + '.jpg')
    if not dst.exists():
        im = Image.open(src).convert('RGB')
        if im.width > maxw:
            im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
        im.save(dst, 'JPEG', quality=q, optimize=True, progressive=True)
    return dst.as_uri()


def svg(path):
    s = (P / path).read_text()
    return re.sub(r'<\?xml[^>]*>', '', s)


LOCKUP_INK = svg('assets/Logo/connectry-lockup-horizontal-ink.svg')
LOCKUP_WHITE = svg('assets/Logo/connectry-lockup-horizontal-white.svg')
MARK_INK = svg('assets/Logo/connectry-mark-ink.svg')
MARK_WHITE = svg('assets/Logo/connectry-mark-white.svg')
FAVICON = svg('assets/Logo/connectry-favicon.svg')

pages = []          # (label, body_html, variant)
toc = []            # (title, page_no)


def page(label, body, variant='ground', title=None):
    pages.append((label, body, variant))
    if title:
        toc.append((title, len(pages)))


def head(title, lead=None):
    h = f'<h1 class="h">{esc(title)}</h1>'
    if lead:
        h += f'<p class="lead">{lead}</p>'
    return h


# ---------------------------------------------------------------- content
readme = (P / 'README.md').read_text()
rd_sections = {}
cur = None
for line in readme.splitlines():
    m = re.match(r'^## (.+)', line)
    if m:
        cur = m.group(1)
        rd_sections[cur] = []
    elif cur:
        rd_sections[cur].append(line)
rd = {k: '\n'.join(v).strip() for k, v in rd_sections.items()}
guides = {p.stem: p.read_text() for p in sorted((P / 'guidelines').glob('*.md'))}


def guide_pages(stem, label, title, cols=2, split=None):
    """A guideline section in full, split over pages at its H2s when long."""
    body = guides[stem]
    parts = [body]
    if split:
        chunks = re.split(r'(?m)^(?=## )', re.sub(r'(?m)^# .*\n', '', body, count=1))
        parts, acc = [], ''
        for c in chunks:
            if acc and len(acc) + len(c) > split:
                parts.append(acc)
                acc = ''
            acc += c
        if acc:
            parts.append(acc)
    for i, part in enumerate(parts):
        t = title if i == 0 else f'{title}, continued'
        page(label, head(t) + f'<div class="md cols{cols}">{md(part)}</div>', title=title if i == 0 else None)


# 1 cover
def baked_cover(src):
    """Photo with the brand scrim burned into the pixels (no CSS transparency, so every PDF viewer
    renders it identically): black rising from the bottom, 55% at the foot to 8% at 40% height."""
    dst = IMG / 'cover.jpg'
    im = Image.open(src).convert('RGB')
    im = im.resize((2400, round(im.height * 2400 / im.width)), Image.LANCZOS)
    tw, th = 2400, 1350
    top = max(0, (im.height - th) // 2)
    im = im.crop((0, top, tw, top + th))
    mask = Image.new('L', (1, th))
    for y in range(th):
        f = y / (th - 1)                      # 0 top .. 1 bottom
        a = 0.0 if f < 0.4 else 0.08 + (0.55 - 0.08) * ((f - 0.4) / 0.6)
        if f >= 0.4 and f < 0.4 + 1e-9:
            a = 0.08
        mask.putpixel((0, y), round(255 * a))
    mask = mask.resize((tw, th))
    im = Image.composite(Image.new('RGB', (tw, th), (0, 0, 0)), im, mask)
    im.save(dst, 'JPEG', quality=88, optimize=True, progressive=True)
    return dst.as_uri()


cover_img = baked_cover(P / 'assets/Imagery/03-kitchen-morning.jpg')
page('', f'''
<div class="bleed" style="background-image:url('{cover_img}')"></div>
<div class="cover">
  <div class="cv-lock">{LOCKUP_WHITE}</div>
  <div class="cv-title">Brand guidelines.</div>
  <div class="cv-sub">Version 2.1 · The whole Connectry system: brand, marketing and product UI.</div>
  <div class="cv-chip">{esc(tokens["meta"]["slogan"])}</div>
</div>''', 'bleed')

# 2 contents (filled later)
page('Contents', '__TOC__', title=None)

# 3 what we are
page('Brand', head('What we are.') + f'<div class="md cols2 big">{md(rd["What we are"])}</div>', title='What we are')
guide_pages('10-positioning', 'Brand', 'Positioning', split=1500)
guide_pages('05-how-this-system-works', 'System', 'How this system works')

# logo
mark_path = 'M32 0H47V47H0V32H32ZM53 53H100V68H68V100H53Z'
page('Logo', head('The mark.', 'Two brackets on a 100 unit grid, stroke 15, gap 6. It reads as a crop mark, a frame around what matters. It is never explained.') + f'''
<div class="row3">
  <div class="tile tl-surface"><div class="lk">{LOCKUP_INK}</div><div class="cap">Lockup, ink. The default on light grounds.</div></div>
  <div class="tile tl-film"><div class="lk">{LOCKUP_WHITE}</div><div class="cap w">Lockup, white. Film, photographs and dark.</div></div>
  <div class="tile tl-surface"><div class="lk blue">{LOCKUP_INK.replace('#1a1a1a', '#4a6fa5')}</div><div class="cap">Lockup, blue. A rare accent on surface or ground only.</div></div>
</div>
<div class="row3 mt">
  <div class="tile tl-surface constr">
    <svg viewBox="-20 -20 140 140" width="300" height="300"><defs><pattern id="g" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M10 0H0V10" fill="none" stroke="rgba(0,0,0,.08)" stroke-width=".5"/></pattern></defs>
    <rect x="0" y="0" width="100" height="100" fill="url(#g)" stroke="rgba(0,0,0,.15)" stroke-width=".5"/>
    <path d="{mark_path}" fill="#1a1a1a"/>
    <text x="0" y="-6" font-size="6" fill="#5b5c66">100 unit grid · stroke 15 · gap 6</text></svg>
    <div class="cap mono">{mark_path}</div></div>
  <div class="tile tl-surface"><div class="md small">{md(rd["The mark"])}</div></div>
  <div class="tile tl-surface"><div class="md small">{md(rd["The logo, in one paragraph"])}</div></div>
</div>''', title='The mark and the logo')

logo_readme = (P / 'assets/Logo/README.md').read_text()
icons = ''.join(f'<figure><img src="{jpg(P / "assets/Icons" / n, n, 512, 92)}"><figcaption>{n}</figcaption></figure>'
                for n in ['connectry-app-icon-blue-512.png', 'connectry-app-icon-ink-512.png',
                          'connectry-avatar-blue-512.png', 'connectry-avatar-white-512.png'])
page('Logo', head('Masters, icons and rules.') + f'''
<div class="split">
  <div class="md small">{md(logo_readme)}</div>
  <div>
    <div class="icons">{icons}<figure><div class="fav">{FAVICON}</div><figcaption>connectry-favicon.svg</figcaption></figure></div>
    <div class="donts">
      {''.join(f'<div class="dont"><div class="dz">{d[1]}</div><b>Never</b> {d[0]}</div>' for d in [
        ('stretch', f'<div style="transform:scaleX(1.5);width:150px">{MARK_INK}</div>'),
        ('rotate', f'<div style="transform:rotate(18deg);width:90px">{MARK_INK}</div>'),
        ('outline', f'<div style="width:90px">{MARK_INK.replace("fill=\"#1a1a1a\"", "fill=\"none\" stroke=\"#1a1a1a\" stroke-width=\"3\"")}</div>'),
        ('recolour', f'<div style="width:90px">{MARK_INK.replace("#1a1a1a", "#c0392b")}</div>'),
        ('place inside glass', f'<div class="glassdemo"><div style="width:70px">{MARK_INK}</div></div>'),
      ])}
    </div>
  </div>
</div>''')

# colour
light = [t for t in tokens['color']['tokens'] if isinstance(t['value'], dict)]
flat = [t for t in tokens['color']['tokens'] if not isinstance(t['value'], dict)]


def chip(val, name, usage, theme_bg='#ffffff'):
    v = val if not val.startswith('{') else '#4a6fa5'
    return (f'<div class="sw"><div class="swc" style="background:{theme_bg}"><div style="background:{v}"></div></div>'
            f'<div class="swn">{esc(name)}</div><div class="swv">{esc(val)}</div><div class="swu">{esc(usage)}</div></div>')


core = ['blue', 'ink', 'body', 'muted', 'faint', 'ground', 'surface', 'hairline', 'blue-light', 'blue-hover', 'blue-tint']
tok = {t['name']: t for t in tokens['color']['tokens']}
page('Colour', head('Colour, Light.', 'One accent. <span class="acc">blue</span> for a primary action and one accent word, at most twice per surface. Everything else is the neutral ladder.') +
     '<div class="swg">' + ''.join(chip(t['value']['light'] if isinstance(t['value'], dict) else t['value'], n, t['usage'])
                                    for n in core for t in [tok[n]]) + '</div>', title='Colour')
themes = tokens['color']['themes']
rows = ''.join(
    '<tr><td class="tn">' + esc(t['name']) + '</td>' + ''.join(
        f'<td><span class="dot" style="background:{t["value"][th["id"]]}"></span>{esc(t["value"][th["id"]])}</td>' for th in themes)
    + f'<td class="tu">{esc(t["usage"])}</td></tr>' for t in light)
page('Colour', head('Three themes.', 'Light is every surface a person reads on. Film is the dark register of photography, the product film and the endcard. Site dark is the website\'s graphite edition. None of them is a toggle.') +
     f'<div class="themes">' + ''.join(
         f'<div class="th" style="background:{tok["ground"]["value"][th["id"]]};color:{tok["ink"]["value"][th["id"]]}">'
         f'<div class="thl" style="color:{tok["muted"]["value"][th["id"]]}">{esc(th["name"]).upper()}</div>'
         f'<div class="tht">One memory. For <span style="color:{"#4a6fa5" if th["id"] == "light" else "#7fa3d6"}">all</span> of it.</div>'
         f'<div class="thb" style="color:{tok["body"]["value"][th["id"]]}">Running text in body. It remembers why, not just what.</div>'
         f'<div class="thc" style="background:{tok["surface"]["value"][th["id"]]};border:1px solid {tok["hairline"]["value"][th["id"]]}"><span style="color:{tok["faint"]["value"][th["id"]]}">LABEL</span> surface</div></div>'
         for th in themes) + '</div>' +
     f'<table class="tt"><tr><th>Token</th>' + ''.join(f'<th>{esc(th["name"])}</th>' for th in themes) + f'<th>Usage</th></tr>{rows}</table>')
func = [t for t in flat if t['name'] not in core]
page('Colour', head('Functional colour.', 'Charts, glass, film and the endcard. Never used as decoration.') +
     '<div class="swg small">' + ''.join(chip(t['value'], t['name'], t['usage'], '#ffffff') for t in func) + '</div>')
guide_pages('20-colour-and-type', 'Colour and type', 'Colour and type, the rules', split=1700)

# type
specimens = ''
for g in tokens['type']['groups']:
    for s in g['styles']:
        sample = RETIRED.get(s.get('sample', ''), s.get('sample', ''))
        size = float(str(s['fontSize']).replace('px', ''))
        disp = min(size, 96)
        upper = s['name'] == 'label'
        specimens += (f'<div class="sp"><div class="spm"><b>{esc(s["name"])}</b><br>{esc(s["fontSize"])} · {s["fontWeight"]} · '
                      f'{s["lineHeight"]}{" · " + esc(s["letterSpacing"]) if s.get("letterSpacing") else ""}<br><span>{esc(s.get("usage", ""))}</span></div>'
                      f'<div class="spt" style="font-size:{disp}px;font-weight:{s["fontWeight"]};line-height:{s["lineHeight"]};'
                      f'letter-spacing:{s.get("letterSpacing", "0")};{"text-transform:uppercase;color:#80818d" if upper else ""}">{esc(sample)}</div></div>')
page('Type', head('Inter. Only.', 'Weights 400, 500 and 600, with <code>cv11</code> and <code>ss01</code> on. Nothing is bold except the wordmark. Headlines end with a full stop. <code>label</code> is the only uppercase. Numbers are tabular.') +
     '<div class="glyphs"><div>Aa</div><div class="gl">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>0123456789 · £ % , . : ;</div>'
     '<div class="gw"><span style="font-weight:400">Regular 400</span><span style="font-weight:500">Medium 500</span><span style="font-weight:600">SemiBold 600</span></div></div>', title='Typography')
sp_list = re.findall(r'<div class="sp">.*?</div></div>', specimens, re.S)
for i in range(0, len(sp_list), 6):
    page('Type', head('Type scale.' if i == 0 else 'Type scale, film.') + '<div class="specs">' + ''.join(sp_list[i:i + 6]) + '</div>')

# layout
sp = tokens['spacing']['tokens']
rad = tokens['radius']['tokens']
page('Layout', head('Spacing and radii.', 'A 4px scale. Nothing is placed on a number that is not on it.') +
     '<div class="spx">' + ''.join(
         f'<div class="spr"><span class="tn">{esc(t["name"])}</span><span class="bar" style="width:{int(t["value"][:-2]) * 4}px"></span><span class="sv">{esc(t["value"])}</span><span class="tu">{esc(t["usage"])}</span></div>' for t in sp) +
     '</div><div class="radg">' + ''.join(
         f'<div class="rd"><div class="rdb" style="border-radius:{min(int(t["value"][:-2]), 60)}px"></div><div class="swn">{esc(t["name"])} · {esc(t["value"])}</div><div class="swu">{esc(t["usage"])}</div></div>' for t in rad) + '</div>',
     title='Layout, spacing and radii')
guide_pages('30-layout-and-spacing', 'Layout', 'Layout and spacing, the rules')
page('Layout', head('Shadows and opacity.') + '<div class="shg">' + ''.join(
    f'<div class="shc"><div class="shb" style="box-shadow:{t["value"]}"></div><div class="swn">{esc(t["name"])}</div><div class="swv">{esc(t["value"])}</div><div class="swu">{esc(t["usage"])}</div></div>'
    for t in tokens['shadow']['tokens']) + '</div><table class="tt mt">' + ''.join(
    f'<tr><td class="tn">{esc(t["name"])}</td><td>{esc(t["value"])}</td><td class="tu">{esc(t["usage"])}</td></tr>' for t in tokens['opacity']['tokens']) + '</table>')

# foundations from the brand book
for key, title in [('Foundations', 'Foundations')]:
    pass
guide_pages('40-glass', 'Glass', 'Glass', split=2300)
guide_pages('50-motion', 'Motion', 'Motion')
guide_pages('60-accessibility', 'Accessibility', 'Accessibility')

# imagery
ind = sorted(n for n in (P / 'assets/Imagery').iterdir() if n.suffix == '.jpg' and '-alt' not in n.name)
page('Imagery', head('The individual.', 'Twenty scenes, one shoot, one grade: warm neutral, natural light, subtle grain, 35mm, shallow depth. Subject in the right two thirds, the left rail free for the line.') +
     '<div class="pg5">' + ''.join(f'<figure><img src="{jpg(n, "im-" + n.stem, 600, 82)}"><figcaption>{esc(n.stem)}</figcaption></figure>' for n in ind) + '</div>', title='Imagery and film')
alts = sorted(n for n in (P / 'assets/Imagery').iterdir() if '-alt' in n.name)
page('Imagery', head('Alternate takes.', 'Each individual scene has a second take for crops and variety.') +
     '<div class="pg5">' + ''.join(f'<figure><img src="{jpg(n, "im-" + n.stem, 600, 82)}"><figcaption>{esc(n.stem)}</figcaption></figure>' for n in alts) + '</div>')
circ = sorted(n for n in (P / 'assets/Circles').iterdir() if n.suffix == '.jpg')
page('Imagery', head('The circles.', (P / 'assets/Circles/README.md').read_text().split('\n', 2)[2].strip().split('\n\n')[0]) +
     '<div class="pg5 big">' + ''.join(f'<figure><img src="{jpg(n, "ci-" + n.stem, 700, 82)}"><figcaption>{esc(n.stem)}</figcaption></figure>' for n in circ) + '</div>')
guide_pages('70-imagery-and-film', 'Imagery', 'Imagery and film, the rules', split=2300)
stills = sorted((P / 'assets/Film/stills').glob('*.jpg'))
page('Film', head('The product film.', '75 seconds, 16:9, sound on. Seven frames set its grammar. The film itself is in the Film asset group as connectry-film-v15-720.mp4.') +
     '<div class="pg4">' + ''.join(f'<figure><img src="{jpg(n, "st-" + n.stem, 900, 84)}"><figcaption>{esc(n.stem)}</figcaption></figure>' for n in stills) + '</div>', title='The product film')
guide_pages('75-the-product-film', 'Film', 'The product film grammar', split=2200)

# voice, ask, dashboard
guide_pages('80-voice', 'Voice', 'Voice')
guide_pages('92-the-ask', 'Product', 'The ask', split=2000)
guide_pages('94-the-dashboard', 'Product', 'The dashboard')
guide_pages('90-applications', 'Applications', 'Applications', split=1800)

slides = sorted((P / 'assets/Slides').glob('*.jpg'))
page('Applications', head('Slides. Eighteen layouts.', '16:9 at 1920 by 1080, margin 86, lockup 36px top left, section label beneath it, page number bottom right.') +
     '<div class="pg6">' + ''.join(f'<img src="{jpg(n, "sl-" + n.stem, 640, 84)}">' for n in slides) + '</div>', title='Slides')
soc = sorted((P / 'assets/Social').glob('*.jpg'))
for i in range(0, len(soc), 24):
    page('Applications', head('Social cards.' if i == 0 else 'Social cards, continued.', 'One line top or middle left, the lockup bottom left, the slogan as the one glass chip bottom right.' if i == 0 else None) +
         '<div class="masonry">' + ''.join(f'<img src="{jpg(n, "so-" + n.stem, 520, 82)}">' for n in soc[i:i + 24]) + '</div>',
         title='Social' if i == 0 else None)

# components
meta = json.loads((SHOTS / 'meta.json').read_text())
order = ['Brand', 'Glass', 'Actions', 'Forms', 'Data', 'People', 'Layout', 'Accessibility', 'Motion', 'Product',
         'Website', 'Film', 'Marketing', 'Social', '']
comps = sorted(meta, key=lambda c: (order.index(meta[c]['group']) if meta[c]['group'] in order else 99, c))
comps = [c for c in comps if c != 'Cover']
page('Components', head('Components.', f'{len(comps)} components, each shown as its live preview renders, with its guidelines. Built in layers: tokens, brand, glass, UI, product, website, film, marketing and social.') +
     '<div class="cidx">' + ''.join(f'<div><span>{esc(meta[c]["group"])}</span>{esc(c)}</div>' for c in comps) + '</div>', title='Components')

AREA_W, AREA_H = 1748, 780
for c in comps:
    shot = SHOTS / f'{c}.png'
    im = Image.open(shot)
    rdme = (P / 'components' / c / 'README.md')
    text = md(rdme.read_text()) if rdme.exists() else ''
    raw = rdme.read_text() if rdme.exists() else ''
    dense = ' dense' if len(raw) > 2000 else ''
    box_w, box_h = 1100, 740
    # slice tall renders so nothing is shrunk past legibility
    slice_h = round(im.width * box_h / box_w)
    # allow up to 1.45x downscale before slicing, so short overflows stay on one page
    n = max(1, -(-im.height // round(slice_h * 1.45)))
    if n > 1:
        slice_h = -(-im.height // n)
    for k in range(n):
        part = im.crop((0, k * slice_h, im.width, min(im.height, (k + 1) * slice_h)))
        f = WORK / f'c-{c}-{k}.png'
        part.save(f)
        src = jpg(f, f'c-{c}-{k}', 2200, 86)
        t = c if k == 0 else f'{c}, continued'
        grp = meta[c]['group'] or 'System'
        note = text if k == 0 else f'<p>Part {k + 1} of {n} of the {esc(c)} preview.</p>'
        body = f'<div class="cn"><div class="md small ct{dense}">{note}</div><div class="ci"><img src="{src}"></div></div>'
        page(f'Components · {grp}', f'<h1 class="h">{esc(t)}</h1>' + body)

guide_pages('96-governance', 'Governance', 'Governance', split=2400)
page('Governance', head('Before anything ships.') + f'<div class="md checks">{md(rd["Before anything ships"])}</div>', title='Before anything ships')

# closing
page('', f'<div class="closing">{LOCKUP_INK}</div>', 'ground-plain')

# ---------------------------------------------------------------- render
toc_html = '<div class="toc">' + ''.join(f'<div><span>{esc(t)}</span><b>{n:02d}</b></div>' for t, n in toc) + '</div>'

CSS = (ROOT / 'tools' / 'brand_pdf.css').read_text()
doc = ['<!doctype html><html><head><meta charset="utf-8"><title>Connectry brand guidelines 2.1</title><style>', CSS, '</style></head><body>']
for i, (label, body, variant) in enumerate(pages, 1):
    body = body.replace('__TOC__', head('Contents.') + toc_html)
    chrome = ''
    if variant in ('ground',):
        chrome = (f'<div class="chrome"><div class="clk">{LOCKUP_INK}</div><div class="clb">{esc(label).upper()}</div></div>'
                  f'<div class="pno">{i:02d}</div>')
    doc.append(f'<section class="pg {variant}">{chrome}<div class="content">{body}</div></section>')
doc.append('</body></html>')
html_path = WORK / 'brand.html'
html_path.write_text(''.join(doc))

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': W, 'height': H})
    pg.goto(html_path.as_uri(), wait_until='networkidle')
    pg.wait_for_timeout(800)
    pg.pdf(path=str(OUT), width=f'{W}px', height=f'{H}px', print_background=True, prefer_css_page_size=True)
    b.close()
print(f'{len(pages)} pages -> {OUT}  (html: {html_path})')
