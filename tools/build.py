#!/usr/bin/env python3
"""Build the Xploit Security static site.

Usage:  python3 tools/build.py
Writes HTML pages, sitemap.xml, robots.txt and site.webmanifest into the repository root
(the folder GitHub Pages serves). Edit page content in tools/pages_*.py and shared
layout/navigation in tools/lib.py, then re-run this script.
"""
import os, sys, json, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from lib import SITE
import pages_home, pages_services, pages_products, pages_company

def write(rel_path, content):
    out = os.path.join(ROOT, rel_path if rel_path.endswith(".html") else os.path.join(rel_path, "index.html"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(content)
    return out

def main():
    paths = []
    write("index.html", pages_home.home()); paths.append(("", "1.0"))
    for mod in (pages_services, pages_products, pages_company):
        for fn in mod.ALL:
            p, html_ = fn()
            write(p, html_)
            paths.append((p, "0.9" if p.count("/") == 1 else "0.8"))
    p, html_ = pages_company.notfound(); write(p, html_)

    today = datetime.date.today().isoformat()
    urls = "\n".join(f"  <url><loc>{SITE['domain']}/{p}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>" for p, pr in paths)
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {SITE['domain']}/sitemap.xml\n")
    with open(os.path.join(ROOT, "site.webmanifest"), "w") as f:
        json.dump({"name": "Xploit Security", "short_name": "Xploit", "start_url": "/", "display": "standalone",
                   "background_color": "#07090d", "theme_color": "#07090d",
                   "icons": [{"src": "/assets/img/brand/icon-192.png", "sizes": "192x192", "type": "image/png"},
                             {"src": "/assets/img/brand/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, f, indent=2)
    with open(os.path.join(ROOT, "CNAME"), "w") as f:
        f.write(SITE["domain"].replace("https://", "") + "\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print(f"Built {len(paths) + 1} pages into {ROOT}")

if __name__ == "__main__":
    main()
