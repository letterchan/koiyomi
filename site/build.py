#!/usr/bin/env python3
"""恋よみ 静的サイトビルダー。

content/*.md (front matter 付き) と content/*.html を templates/base.html で包んで
public/ に書き出す。アフィリエイトリンクは links.json で一元管理し、本文中の
{{link:KEY}} / {{cta:KEY}} を置換する。
"""
import json
import os
import re
import shutil
import sys
from datetime import date
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
PUBLIC = ROOT.parent / "public"

SITE = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
LINKS = json.loads((ROOT / "links.json").read_text(encoding="utf-8"))
BASE_URL = os.environ.get("BASE_URL", SITE["base_url"]).rstrip("/")
BASE_PATH = os.environ.get("BASE_PATH", SITE.get("base_path", "")).rstrip("/")

CATEGORIES = SITE["categories"]  # key -> label


def parse_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("front matter がありません")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, m.group(2)


def render_cta(key):
    l = LINKS[key]
    points = "".join(f"<li>{p}</li>" for p in l.get("points", []))
    return f"""
<div class="cta">
  <div class="cta-name">{l['name']}</div>
  <ul class="cta-points">{points}</ul>
  <a class="cta-btn" href="{l['url']}" target="_blank" rel="nofollow noopener sponsored">{l.get('button', '公式サイトで初回特典を確認する')}</a>
  <div class="cta-note">※広告（PR）。特典・料金は変更されることがあります。必ず公式サイトで最新条件を確認してください。</div>
</div>
"""


def replace_links(html):
    html = re.sub(r"\{\{cta:(\w+)\}\}", lambda m: render_cta(m.group(1)), html)
    html = re.sub(r"\{\{link:(\w+)\}\}", lambda m: LINKS[m.group(1)]["url"], html)
    html = re.sub(r"\{\{name:(\w+)\}\}", lambda m: LINKS[m.group(1)]["name"], html)
    html = html.replace("{{base}}", BASE_PATH)
    return html


def url_for(slug):
    if slug == "index":
        return f"{BASE_PATH}/"
    return f"{BASE_PATH}/{slug}/"


def load_pages():
    pages = []
    for p in sorted(CONTENT.iterdir()):
        if p.suffix not in (".md", ".html"):
            continue
        meta, body = parse_front_matter(p.read_text(encoding="utf-8"))
        if meta.get("draft") == "true":
            continue
        meta.setdefault("slug", p.stem)
        meta.setdefault("type", "article")
        meta.setdefault("category", "guide")
        meta.setdefault("date", date.today().isoformat())
        if p.suffix == ".md":
            html = markdown.markdown(body, extensions=["tables", "toc", "sane_lists"])
        else:
            html = body
        meta["html"] = replace_links(html)
        meta["url"] = url_for(meta["slug"])
        pages.append(meta)
    return pages


def render(template, **ctx):
    out = template
    for k, v in ctx.items():
        out = out.replace("{{" + k + "}}", str(v))
    return out


def card(p):
    label = CATEGORIES.get(p["category"], p["category"])
    return f"""<a class="card" href="{p['url']}"><span class="card-cat">{label}</span><span class="card-title">{p['title']}</span><span class="card-desc">{p.get('description','')}</span></a>"""


def main():
    base = (TEMPLATES / "base.html").read_text(encoding="utf-8")
    pages = load_pages()
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir(parents=True)
    shutil.copytree(STATIC, PUBLIC / "static")

    tools = [p for p in pages if p["type"] == "tool"]
    articles = sorted([p for p in pages if p["type"] == "article"], key=lambda x: x["date"], reverse=True)
    for p in pages:
        if p["slug"] == "index":
            continue
        related = [q for q in articles if q["category"] == p["category"] and q["slug"] != p["slug"]][:4]
        related_html = "".join(card(q) for q in related)
        tools_html = "".join(card(q) for q in tools if q["slug"] != p["slug"])[:6]
        out = render(
            base,
            title=p["title"],
            description=p.get("description", ""),
            canonical=f"{BASE_URL}{p['url']}",
            base_path=BASE_PATH,
            site_name=SITE["name"],
            tagline=SITE["tagline"],
            content=p["html"],
            related=related_html,
            tools=tools_html,
            date=p["date"],
            category=CATEGORIES.get(p["category"], p["category"]),
            year=date.today().year,
            body_class=p["type"],
        )
        d = PUBLIC / p["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(out, encoding="utf-8")

    # index
    idx = next((p for p in pages if p["slug"] == "index"), None)
    tools_html = "".join(card(q) for q in tools)
    latest_html = "".join(card(q) for q in articles[:12])
    cats_html = ""
    for key, label in CATEGORIES.items():
        items = [q for q in articles if q["category"] == key][:6]
        if not items:
            continue
        cats_html += f"<h2>{label}</h2><div class=\"cards\">{''.join(card(q) for q in items)}</div>"
    index_body = (idx["html"] if idx else "") + f"""
<h2>無料診断</h2><div class="cards">{tools_html}</div>
<h2>新着記事</h2><div class="cards">{latest_html}</div>
{cats_html}
"""
    out = render(
        base,
        title=f"{SITE['name']}｜{SITE['tagline']}",
        description=SITE["description"],
        canonical=f"{BASE_URL}{BASE_PATH}/",
        base_path=BASE_PATH,
        site_name=SITE["name"],
        tagline=SITE["tagline"],
        content=index_body,
        related="",
        tools="",
        date="",
        category="",
        year=date.today().year,
        body_class="home",
    )
    (PUBLIC / "index.html").write_text(out, encoding="utf-8")

    # sitemap / robots
    urls = [f"{BASE_URL}{BASE_PATH}/"] + [f"{BASE_URL}{p['url']}" for p in pages if p["slug"] != "index"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n"
    (PUBLIC / "sitemap.xml").write_text(sm, encoding="utf-8")
    (PUBLIC / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}{BASE_PATH}/sitemap.xml\n", encoding="utf-8")
    (PUBLIC / ".nojekyll").write_text("", encoding="utf-8")
    print(f"built {len(pages)} pages -> {PUBLIC}")


if __name__ == "__main__":
    sys.exit(main())
