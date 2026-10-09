import json, re, sys, threading, pathlib, http.server, functools, time
from playwright.sync_api import sync_playwright

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
man = json.loads((REPO / 'asset-manifest.json').read_text())
BLOB = {a['old_blob_id']: REPO / a['repo_path'] for a in man['assets']}


class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def translate_path(self, path):
        m = re.match(r'^/_blob/([0-9a-f]{32})', path)
        if m and m.group(1) in BLOB:
            return str(BLOB[m.group(1)])
        return super().translate_path(path)


srv = http.server.ThreadingHTTPServer(('127.0.0.1', 8765), functools.partial(H, directory=str(REPO)))
threading.Thread(target=srv.serve_forever, daemon=True).start()

only = set(sys.argv[2:])
comps = sorted((REPO / 'project/components').glob('*/preview.html'))
meta = {}
with sync_playwright() as p:
    b = p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
    for f in comps:
        name = f.parent.name
        if only and name not in only:
            continue
        head = f.read_text(errors='ignore')[:300]
        w = int(re.search(r'width=(\d+)', head).group(1)) if re.search(r'width=(\d+)', head) else 960
        h = int(re.search(r'height=(\d+)', head).group(1)) if re.search(r'height=(\d+)', head) else 600
        g = re.search(r'group="([^"]+)"', head)
        ctx = b.new_context(viewport={'width': w, 'height': h}, device_scale_factor=2, reduced_motion='no-preference')
        pg = ctx.new_page()
        errs = []
        pg.on('requestfailed', lambda r: errs.append(r.url))
        pg.goto(f'http://127.0.0.1:8765/project/components/{name}/preview.html', wait_until='networkidle', timeout=60000)
        pg.wait_for_timeout(4500)
        # seek videos to a representative frame
        pg.evaluate("""() => Promise.all([...document.querySelectorAll('video')].map(v => new Promise(r => {
            try { v.muted = true; v.pause(); const t = Math.min(2.5, (v.duration||5) * 0.4);
                  v.addEventListener('seeked', () => r(), {once:true}); v.currentTime = t; setTimeout(r, 1500);} catch(e){ r(); } })))""")
        pg.evaluate("""() => { document.querySelectorAll('video').forEach(v => v.removeAttribute('controls'));
            const s = document.createElement('style');
            s.textContent = 'video::-webkit-media-controls{display:none!important}';
            document.head.appendChild(s); }""")
        pg.wait_for_timeout(500)
        pg.screenshot(path=str(OUT / f'{name}.png'), full_page=True)
        meta[name] = {'group': g.group(1) if g else '', 'w': w, 'h': h,
                      'failed': [u for u in errs if 'fonts.g' not in u]}
        ctx.close()
        print(name, w, h, len(meta[name]['failed']), flush=True)
    b.close()
(OUT / 'meta.json').write_text(json.dumps(meta, indent=1))
srv.shutdown()
