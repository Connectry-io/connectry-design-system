#!/usr/bin/env python3
"""People of the City house treatment: glass ask bar, two-line answer, logo and url.

Geometry is measured from the published campaign frames (crosswalk, ATL22) so new sets
sit beside the old ones without a visible seam. Supersampled 2x for clean edges.
Needs Pillow, numpy and the Inter / Inter Display OTFs in FD.
"""
import sys, json, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FD = "/usr/share/fonts/opentype/inter/"
INK = (26, 26, 26)
BLUE = (74, 111, 165)
BLUE_LIGHT = (185, 206, 238)

# Per format: canvas, bar box, radius, tile, send, type sizes, answer baselines, footer.
F = {
 "16x9": dict(W=1920, H=1080, bx0=300, bx1=1620, cy=628, bh=112, r=40, tile=44, tr=10, send=80,
              ask=50, ask_x=405, ans=68, b1=790, lh=82, logo=40, lb=983, mx=140),
 "9x16": dict(W=1080, H=1920, bx0=70, bx1=1010, cy=1114, bh=92, r=33, tile=38, tr=9, send=68,
              ask=40, ask_x=160, ans=52, b1=1250, lh=64, logo=32, lb=1754, mx=82),
 "4x5":  dict(W=1080, H=1350, bx0=108, bx1=972, cy=675, bh=72, r=26, tile=30, tr=7, send=52,
              ask=31, ask_x=178, ans=42, b1=785, lh=52, logo=32, lb=1236, mx=82),
}

def font(name, size): return ImageFont.truetype(FD + name, size)

def tlen(d, txt, f, tr=-0.02):
    return d.textlength(txt, font=f) + tr * f.size * max(len(txt) - 1, 0)

def ttext(d, xy, txt, f, fill, tr=-0.02):
    """Draw with tracking while keeping pair kerning: place each glyph at its kerned offset."""
    x, y = xy
    for i, ch in enumerate(txt):
        d.text((x + d.textlength(txt[:i], font=f) + tr * f.size * i, y), ch, font=f, fill=fill)

def film(im, seed=7):
    """Bring a clean generated still toward the campaign's 35mm look: soft blacks, warmth, grain."""
    a = np.asarray(im).astype(np.float32)
    a = a * 0.94 + 10
    a[..., 0] *= 1.015; a[..., 2] *= 0.985
    lum = a.mean(2, keepdims=True); a = lum + (a - lum) * 0.93
    rng = np.random.default_rng(seed)
    g = rng.normal(0, 1, a.shape[:2]).astype(np.float32)
    g = np.asarray(Image.fromarray(((g * 40) + 128).clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))).astype(np.float32) - 128
    a += (g / 40.0 * 5.5)[..., None]
    return Image.fromarray(a.clip(0, 255).astype(np.uint8))

def cover(im, W, H, fx=0.5, fy=0.5, zoom=1.0):
    """Crop to the target aspect around a focal point (optionally zoomed in), then resize."""
    w, h = im.size; t = W / H
    w, h = int(w / zoom), int(h / zoom)
    if w / h > t: cw, ch = int(h * t), h
    else: cw, ch = w, int(w / t)
    fw, fh = im.size
    x0 = int(min(max(fx * fw - cw / 2, 0), fw - cw)); y0 = int(min(max(fy * fh - ch / 2, 0), fh - ch))
    return im.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.LANCZOS)

def rr_mask(size, box, r):
    m = Image.new("L", size, 0); ImageDraw.Draw(m).rounded_rectangle(box, r, fill=255); return m

def mark(d, x, y, s, fill):
    """The bracket mark: two L shapes, from connectry-mark-white.svg (100 unit grid)."""
    k = s / 100.0
    p1 = [(32, 0), (47, 0), (47, 47), (0, 47), (0, 32), (32, 32)]
    p2 = [(53, 53), (100, 53), (100, 68), (68, 68), (68, 100), (53, 100)]
    for p in (p1, p2): d.polygon([(x + u * k, y + v * k) for u, v in p], fill=fill)

def render(src, fmt, ask, a1, a2, out, fx=0.5, fy=0.5, zoom=1.0):
    g = F[fmt]; S = 2
    W, H = g["W"], g["H"]
    base = film(cover(Image.open(src).convert("RGB"), W, H, fx, fy, zoom)).resize((W * S, H * S), Image.LANCZOS)
    s = lambda v: int(round(v * S))
    bx0, bx1, cy, bh, r = s(g["bx0"]), s(g["bx1"]), s(g["cy"]), s(g["bh"]), s(g["r"])
    by0, by1 = cy - bh // 2, cy + bh // 2

    # Glass: blurred plate under a white veil with a soft vertical falloff, plus a bright rim.
    blur = base.filter(ImageFilter.GaussianBlur(s(g["W"] / 1920 * 14)))
    veil = Image.new("RGBA", base.size, (0, 0, 0, 0))
    vg = np.zeros((bh, bx1 - bx0, 4), np.uint8); vg[..., :3] = 255
    vg[..., 3] = np.linspace(0.74 * 255, 0.64 * 255, bh)[:, None].astype(np.uint8)
    veil.paste(Image.fromarray(vg, "RGBA"), (bx0, by0))
    glass = Image.alpha_composite(blur.convert("RGBA"), veil)
    m = rr_mask(base.size, (bx0, by0, bx1, by1), r)
    # Faint shadow so the bar sits on bright plates too.
    sh = Image.new("L", base.size, 0); ImageDraw.Draw(sh).rounded_rectangle((bx0, by0 + s(4), bx1, by1 + s(6)), r, fill=70)
    sh = sh.filter(ImageFilter.GaussianBlur(s(10)))
    img = Image.composite(Image.new("RGB", base.size, (0, 0, 0)), base, sh)
    img.paste(glass.convert("RGB"), (0, 0), m)
    d = ImageDraw.Draw(img, "RGBA")
    d.rounded_rectangle((bx0, by0, bx1, by1), r, outline=(255, 255, 255, 215), width=max(2, s(1.3)))

    # Tile with mark.
    t = s(g["tile"]); tx = bx0 + int(bh * 0.30); ty = cy - t // 2
    d.rounded_rectangle((tx, ty, tx + t, ty + t), s(g["tr"]), fill=BLUE)
    ms = int(t * 0.46); mark(d, tx + (t - ms) / 2, ty + (t - ms) / 2, ms, (255, 255, 255))

    # Ask text and caret.
    fa = font("InterDisplay-Medium.otf", s(g["ask"]))
    ax = s(g["ask_x"]) if fmt == "16x9" else tx + t + int(t * 0.55)
    capH = fa.getbbox("H")[3] - fa.getbbox("H")[1]
    ty_txt = cy - capH / 2 - fa.getbbox("H")[1]
    ttext(d, (ax, ty_txt), ask, fa, INK)
    tw = tlen(d, ask, fa)
    cx = ax + tw + s(3); d.rectangle((cx, cy - capH * 0.72, cx + max(2, s(1.6)), cy + capH * 0.72), fill=INK)

    # Send button.
    sd = s(g["send"]); scx = bx1 - (by1 - by0) // 2 - s(1)
    d.ellipse((scx - sd // 2, cy - sd // 2, scx + sd // 2, cy + sd // 2), fill=BLUE)
    aw = max(3, s(g["send"] * 0.04)); ah = sd * 0.30
    d.line((scx, cy + ah / 2, scx, cy - ah / 2), fill="white", width=aw)
    d.line((scx - ah * 0.45, cy - ah / 2 + ah * 0.45, scx, cy - ah / 2 - aw * 0.15), fill="white", width=aw)
    d.line((scx + ah * 0.45, cy - ah / 2 + ah * 0.45, scx, cy - ah / 2 - aw * 0.15), fill="white", width=aw)

    # Answer: two centred lines, white then blue-light, soft shadow, never boxed.
    fn = font("InterDisplay-Medium.otf", s(g["ans"]))
    lines = [(a1, (255, 255, 255)), (a2, BLUE_LIGHT)]
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0)); sd_ = ImageDraw.Draw(shadow)
    pos = []
    for i, (txt, col) in enumerate(lines):
        w = tlen(d, txt, fn); x = (W * S - w) / 2
        yb = s(g["b1"] + i * g["lh"]); y = yb - fn.getmetrics()[0]
        pos.append((x, y, txt, col)); ttext(sd_, (x, y + s(2)), txt, fn, (0, 0, 0, 120))
    # Bright plates get a deeper, wider shadow so the answer holds without a box.
    xs = [p[0] for p in pos]; x0a = int(min(xs)); x1a = int(W * S - min(xs))
    y0a = int(pos[0][1]); y1a = int(pos[-1][1] + fn.getmetrics()[0] * 1.3)
    lum = np.asarray(base.crop((x0a, y0a, x1a, y1a)).convert("L")).mean()
    k = min(max((lum - 95) / 90.0, 0), 1)
    sh_a = shadow.filter(ImageFilter.GaussianBlur(s(10 + 16 * k)))
    if k > 0:
        a = np.asarray(sh_a).copy(); a[..., 3] = np.clip(a[..., 3].astype(np.float32) * (1 + 1.6 * k), 0, 255).astype(np.uint8)
        sh_a = Image.fromarray(a, "RGBA")
    img = Image.alpha_composite(img.convert("RGBA"), sh_a)
    if k > 0.3:
        img = Image.alpha_composite(img, shadow.filter(ImageFilter.GaussianBlur(s(4))))
    d = ImageDraw.Draw(img)
    for x, y, txt, col in pos: ttext(d, (x, y), txt, fn, col)

    # Footer: mark + wordmark left, url right, one baseline, on a faint shadow for bright plates.
    fl = font("InterDisplay-SemiBold.otf", s(g["logo"])); fu = font("Inter-Regular.otf", s(g["logo"]))
    lb = s(g["lb"]); mx = s(g["mx"])
    capL = fl.getbbox("C")[3] - fl.getbbox("C")[1]
    msz = int(capL * 0.92)
    url = "connectry.io"; uw = tlen(d, url, fu, 0)
    def footer(dd, c1, c2, dy=0):
        mark(dd, mx, lb - capL / 2 - msz / 2 - capL * 0.02 + dy, msz, c1)
        ttext(dd, (mx + msz + int(capL * 0.45), lb - fl.getmetrics()[0] + dy), "Connectry", fl, c1, -0.01)
        dd.text((W * S - int(mx * 0.9) - uw, lb - fu.getmetrics()[0] + dy), url, font=fu, fill=c2)
    fsh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    footer(ImageDraw.Draw(fsh), (0, 0, 0, 110), (0, 0, 0, 110), s(1.5))
    img = Image.alpha_composite(img, fsh.filter(ImageFilter.GaussianBlur(s(6))))
    footer(ImageDraw.Draw(img), (255, 255, 255), (255, 255, 255, 235))
    img.convert("RGB").resize((W, H), Image.LANCZOS).save(out, quality=90, optimize=True, progressive=True)

if __name__ == "__main__":
    # comp.py jobs.json  (list of {src, fmt, ask, a1, a2, out, fx, fy, zoom})
    for j in json.load(open(sys.argv[1])):
        render(j["src"], j["fmt"], j["ask"], j["a1"], j["a2"], j["out"], j.get("fx", 0.5), j.get("fy", 0.5), j.get("zoom", 1.0))
        print(j["out"])
