"""Build the ready-to-serve folder for self-hosting: dist/ = index.html + nb/ + sw.js + manifest + icons + SHA256SUMS."""
import os, shutil, hashlib, json, sys
d = os.path.dirname(os.path.abspath(__file__))
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(d, 'dist')
os.makedirs(os.path.join(out, 'nb'), exist_ok=True)
os.makedirs(os.path.join(out, 'icons'), exist_ok=True)
# claude.ai wraps the published page in a document skeleton; a self-hosted copy has to carry its own.
src = open(os.path.join(d, 'space-x-study.html')).read()
cut = src.index('</style>') + len('</style>')
assert src.lstrip().startswith('<title>') and src.count('<style') == 1 and src.count('<script') == 1
open(os.path.join(out, 'index.html'), 'w').write(
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + src[:cut].lstrip() + '\n</head>\n<body>\n' + src[cut:].strip() + '\n</body>\n</html>\n')
shutil.copyfile(os.path.join(d, 'sw.js'), os.path.join(out, 'sw.js'))
# Page images live in dist/nb in the repo; a fresh set in ./nb (from nbpages.py) replaces them.
if os.path.isdir(os.path.join(d, 'nb')):
    for f in sorted(os.listdir(os.path.join(d, 'nb'))):
        if f.endswith('.webp'):
            shutil.copyfile(os.path.join(d, 'nb', f), os.path.join(out, 'nb', f))
assert len([f for f in os.listdir(os.path.join(out, 'nb')) if f.endswith('.webp')]) == 169, 'expected 169 notebook pages'
for f in ('icon-192.png', 'icon-512.png'):
    shutil.copyfile(os.path.join(d, 'icons', f), os.path.join(out, 'icons', f))
manifest = {
    "name": "Space X Study", "short_name": "Space X", "start_url": "./", "scope": "./", "display": "standalone",
    "background_color": "#161118", "theme_color": "#161118",
    "icons": [{"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
              {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}],
}
open(os.path.join(out, 'manifest.webmanifest'), 'w').write(json.dumps(manifest, indent=1) + '\n')
rows = []
for root, _, files in os.walk(out):
    for f in files:
        if f == 'SHA256SUMS':
            continue
        full = os.path.join(root, f)
        rows.append((os.path.relpath(full, out).replace(os.sep, '/'), hashlib.sha256(open(full, 'rb').read()).hexdigest()))
rows.sort()
open(os.path.join(out, 'SHA256SUMS'), 'w').write(''.join('%s  %s\n' % (h, p) for p, h in rows))
total = sum(os.path.getsize(os.path.join(out, p)) for p, _ in rows)
print(len(rows), 'files', round(total / 1e6, 1), 'MB; SHA256SUMS sha256 =', hashlib.sha256(open(os.path.join(out, 'SHA256SUMS'), 'rb').read()).hexdigest())
