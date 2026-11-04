"""Build the static IONOS handoff, without modifying the Pages preview."""
from pathlib import Path
from shutil import copytree, copy2
import argparse

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=root.parent/'outputs'/'ionos')
args=parser.parse_args()
out=args.output.resolve()
if out==root or root in out.parents:
    raise SystemExit('Output must be outside the repository.')
out.mkdir(parents=True,exist_ok=True)
html=(root/'index.html').read_text()
html=html.replace('noindex,follow,max-image-preview:large','index,follow,max-image-preview:large')
html=html.replace('https://klasphilipp-private.github.io/hollaender/','https://www.nadinehollaender.de/')
(out/'index.html').write_text(html)
copytree(root/'assets',out/'assets',dirs_exist_ok=True)
copy2(root/'favicon.ico',out/'favicon.ico')
(out/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://www.nadinehollaender.de/sitemap.xml\n')
(out/'sitemap.xml').write_text('''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url><loc>https://www.nadinehollaender.de/</loc><image:image><image:loc>https://www.nadinehollaender.de/assets/nadine-hollaender.jpg</image:loc></image:image></url>
</urlset>
''')
print(out)
