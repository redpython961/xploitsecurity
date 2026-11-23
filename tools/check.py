#!/usr/bin/env python3
"""QA: broken internal links/assets, missing alt text, duplicate titles/descriptions, metadata presence."""
import os, re, sys, glob, json
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class P(HTMLParser):
    def __init__(s): super().__init__(); s.links=[]; s.imgs=[]; s.ids=set(); s.meta={}; s.title=""; s._t=False; s.ld=[]; s._ld=False
    def handle_starttag(s,t,a):
        a=dict(a)
        if "id" in a: s.ids.add(a["id"])
        if t=="a" and "href" in a: s.links.append(a["href"])
        if t in ("link","script") and (a.get("href") or a.get("src")): s.links.append(a.get("href") or a.get("src"))
        if t=="img": s.imgs.append(a); s.links.append(a.get("src",""))
        if t=="iframe": s.links.append(a.get("src",""))
        if t=="meta": s.meta[a.get("name") or a.get("property")]=a.get("content")
        if t=="title" and not s.title: s._t=True
        if t=="script" and a.get("type")=="application/ld+json": s._ld=True
    def handle_endtag(s,t):
        if t=="title": s._t=False
        if t=="script": s._ld=False
    def handle_data(s,d):
        if s._t: s.title+=d
        if s._ld: s.ld.append(d)
errors=[]; titles={}; descs={}; ext=set()
files=sorted(glob.glob(ROOT+"/**/*.html",recursive=True))
for f in files:
    relf=os.path.relpath(f,ROOT)
    if relf.startswith("tools"): continue
    p=P(); p.feed(open(f,encoding="utf-8").read())
    for k in ("description","og:title","og:description","og:image","twitter:card"):
        if not p.meta.get(k): errors.append(f"{relf}: missing meta {k}")
    titles.setdefault(p.title,[]).append(relf); descs.setdefault(p.meta.get("description"),[]).append(relf)
    if not (10 <= len(p.title) <= 75): errors.append(f"{relf}: title length {len(p.title)}")
    d=p.meta.get("description") or ""
    if not (70 <= len(d) <= 230): errors.append(f"{relf}: description length {len(d)}")
    for blob in p.ld:
        try: json.loads(blob)
        except Exception as e: errors.append(f"{relf}: invalid JSON-LD {e}")
    for im in p.imgs:
        if "alt" not in im: errors.append(f"{relf}: img without alt {im.get('src')}")
    for l in p.links:
        if not l or l.startswith(("mailto:","tel:","javascript:")): continue
        if l.startswith(("http://","https://")): ext.add(l.split("?")[0]); continue
        u=urlparse(l); path=unquote(u.path)
        if path=="" and u.fragment:
            if u.fragment not in p.ids: errors.append(f"{relf}: missing anchor #{u.fragment}")
            continue
        if relf=="404.html" and path.startswith("/"): target=os.path.join(ROOT,path.lstrip("/"))
        else: target=os.path.normpath(os.path.join(os.path.dirname(f),path))
        if os.path.isdir(target): target=os.path.join(target,"index.html")
        if not os.path.exists(target): errors.append(f"{relf}: broken link {l}")
for t,fs in titles.items():
    if len(fs)>1: errors.append(f"duplicate title '{t}': {fs}")
for t,fs in descs.items():
    if len(fs)>1: errors.append(f"duplicate description: {fs}")
print(f"Checked {len(files)} HTML files.")
print("External URLs:", *sorted(ext), sep="\n  ")
print("\nERRORS:" if errors else "\nNo errors found.", *errors, sep="\n  ")
sys.exit(1 if errors else 0)
