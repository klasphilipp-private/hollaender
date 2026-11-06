"""Build public website files for IONOS or GitHub Pages."""
from pathlib import Path
from shutil import copytree, copy2
import argparse
import re

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=root.parent/'outputs'/'ionos')
parser.add_argument('--target',choices=['ionos','pages'],default='ionos')
args=parser.parse_args()
out=args.output.resolve()
if out==root or root in out.parents:
    raise SystemExit('Output must be outside the repository.')
out.mkdir(parents=True,exist_ok=True)
html=(root/'index.html').read_text()
if args.target == 'ionos':
    html=html.replace('noindex,follow,max-image-preview:large','index,follow,max-image-preview:large')
    html=html.replace('https://klasphilipp-private.github.io/hollaender/','https://www.nadinehollaender.de/')
(out/'index.html').write_text(html)
for name in ['impressum.html', 'datenschutz.html']:
    page = (root/name).read_text()
    if name == 'datenschutz.html':
        hosting = (root/'content'/('hosting-' + ('ionos' if args.target == 'ionos' else 'github') + '.html')).read_text().strip()
        page, count = re.subn(r'<!--HOSTING_START-->.*?<!--HOSTING_END-->', lambda _: hosting, page, flags=re.S)
        if count != 1:
            raise SystemExit('Expected exactly one hosting section.')
    (out/name).write_text(page)
asset_types = {'.css','.js','.svg','.jpg','.jpeg','.png','.ico','.webp','.woff','.woff2'}
for asset in (root/'assets').rglob('*'):
    if asset.is_symlink():
        raise SystemExit('Symlinks are not public assets.')
    if asset.is_file() and asset.suffix.lower() in asset_types and not any(p.startswith('.') for p in asset.relative_to(root/'assets').parts):
        target = out/'assets'/asset.relative_to(root/'assets')
        target.parent.mkdir(parents=True,exist_ok=True)
        copy2(asset,target)
copy2(root/'favicon.ico',out/'favicon.ico')
(out/'robots.txt').write_text('User-agent: *\nAllow: /\n' + ('Sitemap: https://www.nadinehollaender.de/sitemap.xml\n' if args.target == 'ionos' else ''))
(out/'sitemap.xml').write_text('''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url><loc>https://www.nadinehollaender.de/</loc><image:image><image:loc>https://www.nadinehollaender.de/assets/nadine-hollaender.jpg</image:loc></image:image></url>
</urlset>
''')
print(out)
