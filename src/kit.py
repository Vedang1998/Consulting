"""Shared helpers and page parts for the site build (v5). Standard library only.

build.py is the engine (assets, layout, checks, site files). pages.py writes every page from the parts here.
Facts come from config.py, industries.py and content.py; nothing here invents a number.
"""

import datetime as _dt
import html
import json
import re
import struct
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
import config as C  # noqa: E402
import mockups as M  # noqa: E402
import spot as S  # noqa: E402
import art as A  # noqa: E402

RELEASE = "--release" in sys.argv
TODAY = _dt.date.today()
NOTES, ERRORS = [], []

NAME = C.BUSINESS_NAME
SITE = f"https://{C.DOMAIN}" if C.DOMAIN else "https://domain-not-set.invalid"


# ---------------------------------------------------------------------------
# Text
# ---------------------------------------------------------------------------

def e(s):
    return html.escape(str(s), quote=True)


def money(n):
    return f"${n:,}"


def price(key_min, key_max=None):
    """A price range from config, with an en dash between the ends."""
    if key_max is None:
        return money(C.PRICES[key_min])
    return f"{money(C.PRICES[key_min])}–{money(C.PRICES[key_max])}"


def meta_desc(text, limit=158):
    """Whole sentences only, never a hard cut."""
    out = ""
    for s in re.split(r"(?<=[.!?])\s+", text.strip()):
        trial = (out + " " + s).strip()
        if len(trial) > limit:
            break
        out = trial
    if not out:
        ERRORS.append(f"meta description has no sentence under {limit} characters: {text[:60]}...")
    return out


def clean_url(path):
    path = "/" + path.strip("/")
    return SITE + ("" if path == "/" else path)


def first_sentence(text):
    return text.split(". ")[0].rstrip(".") + "."


def fill(text):
    """Fill {NAME} and [[price]] tokens in resource text (see content.py)."""
    text = text.replace("{NAME}", NAME)

    def rep(m):
        ERRORS.append(f"price token [[{m.group(1)}]] in resource text: the site shows no prices of ours")
        return ""
    return re.sub(r"\[\[([a-z0-9_|]+)\]\]", rep, text)


# Pages folded into others in v5 (Nov 2026). Old links in content.py point at the new home of each one.
MOVED = {"/guides": "/resources", "/tools": "/resources",
         "/tools/shopify-plan-picker": "/services/store-move#plan-picker",
         "/tools/erp-readiness": "/services/systems-roadmap#readiness",
         "/tools/sync-simulator": "/services/store-to-back-office-sync#sync-model",
         "/tools/odoo-tours": "/services/back-office-launch#recordings",
         "/shopify": "/services/store-move", "/odoo": "/services/back-office-launch"}


def moved(href):
    """Where an old internal link now lives."""
    if not href or not href.startswith("/"):
        return href
    base, _, frag = href.partition("#")
    if base in MOVED:
        return MOVED[base] if "#" in MOVED[base] or not frag else f"{MOVED[base]}#{frag}"
    if base.startswith("/videos/"):
        return "/videos"
    if base.startswith("/faq/"):
        return "/faq#" + base.split("/")[2]
    return href


def inline(text):
    """Escape text, then turn [label](url) into links."""
    out = e(fill(text))

    def link(m):
        ext = m.group(2).startswith("http")
        return f'<a href="{moved(m.group(2))}"{" rel=\"noopener\"" if ext else ""}>{m.group(1)}</a>'
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, out)


def anchor(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60]


def md(text):
    """The small markdown used in content.py: ## headings, - and 1. lists, | tables, paragraphs."""
    out = []
    for b in re.split(r"\n\s*\n", text.strip()):
        lines = [x.strip() for x in b.strip().split("\n")]
        if lines[0].startswith("## "):
            h = lines[0][3:]
            out.append(f'<h2 id="{anchor(h)}">{e(h)}</h2>')
        elif all(x.startswith("- ") for x in lines):
            out.append("<ul>" + "".join(f"<li>{inline(x[2:])}</li>" for x in lines) + "</ul>")
        elif all(re.match(r"\d+\. ", x) for x in lines):
            out.append("<ol>" + "".join(f"<li>{inline(re.sub(r'^\d+\. ', '', x))}</li>" for x in lines) + "</ol>")
        elif all(x.startswith("|") for x in lines):
            rows = [[c.strip() for c in x.strip("|").split("|")] for x in lines]
            th = "".join(f'<th scope="col">{inline(c)}</th>' if c else "<td></td>" for c in rows[0])
            tb = "".join("<tr>" + f'<th scope="row">{inline(r[0])}</th>' +
                         "".join(f'<td data-label="{e(re.sub(r"[\[\]]|\(.*?\)", "", h))}">{inline(c)}</td>'
                                 for h, c in zip(rows[0][1:], r[1:])) + "</tr>" for r in rows[1:])
            out.append(f'<div class="tbl"><table class="gtable"><thead><tr>{th}</tr></thead>'
                       f'<tbody>{tb}</tbody></table></div>')
        else:
            out.append(f"<p>{inline(' '.join(lines))}</p>")
    return "\n".join(out)


def nice_date(iso):
    return _dt.date.fromisoformat(iso).strftime("%b %-d, %Y")


# ---------------------------------------------------------------------------
# Icons and art
# ---------------------------------------------------------------------------

def icon(name):
    """A small line icon (Lucide shapes, mockups.py)."""
    return M.icon(name)


# Icon tiles (Nov 13, 2026, second pass): the custom spot icons (spot.py, the set Vee liked) on a soft tile in the
# icon's color family, in place of the white Lucide glyphs of v6. Pages pass a spot name or the Lucide name it replaces.
IND_SPOT = {"apparel": "shirt", "home-and-furniture": "sofa", "food-and-beverage": "jar", "health-and-beauty": "pump",
            "wholesale": "pallet"}
MISSING_SPOT = set()


def tile(name, color="", cls=""):
    """A custom spot icon on a soft tile. The tile and the icon's color block follow the icon's family unless a color
    is given."""
    n = name if name in S.ICONS else S.SPOT_FOR.get(name, "")
    if not n:
        MISSING_SPOT.add(name)
        c = f"tile t-{color or 'blue'} {cls}".strip()
        return f'<span class="{c}">{M.icon(name)}</span>'
    col = color or S.ICONS[n][0]
    c = f"tile t-{col} {cls}".strip()
    return f'<span class="{c}">{S.icon(n)}</span>'


def spot(name):
    """The icon tile for a spot name, or for a Lucide name the site passes."""
    return tile(name)


def ind_tile(x, cls=""):
    """The industry's icon tile, in the industry's color."""
    return tile(IND_SPOT[x["slug"]], x["color"].replace("c-", ""), cls)


# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------

SVC_URL = {"systems-roadmap": "systems-roadmap", "store-move": "store-move", "odoo-launch": "back-office-launch",
           "connection": "store-to-back-office-sync", "support": "support-block"}
SVC_SPOT = {"systems-roadmap": "roadmap", "store-move": "store-move", "odoo-launch": "back-office",
            "connection": "sync", "support": "support"}
SVC_COLOR = {"systems-roadmap": "c-lilac", "store-move": "c-coral", "odoo-launch": "c-mint",
             "connection": "c-blue", "support": "c-yellow"}
# Hero art for each service: two real screens from config.SCREENS, (behind, in front).
SVC_STACK = {"systems-roadmap": ("shop-products", "inventory-c"), "store-move": ("shop-products", "shop-order"),
             "odoo-launch": ("inventory-c", "hero-m"), "connection": ("shop-order", "delivery-c"),
             "support": ("shop-inventory", "sales-c")}
PKG = {p["slug"]: p for p in C.PACKAGES}
ORDER = ["systems-roadmap", "store-move", "odoo-launch", "connection"]


def svc_href(slug):
    return f"/services/{SVC_URL[slug]}"


def svc_name(slug):
    return C.SUPPORT["name"] if slug == "support" else PKG[slug]["name"]


def svc_price(slug):
    """Kept for old call sites: the site shows no prices of ours (Vee, Nov 13, 2026)."""
    return "Fixed fee, quoted after a call"


def svc_time(slug):
    return "10 or 20 hours" if slug == "support" else PKG[slug]["timeline"]


# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------

def primary_cta(where, label_="Book a scoping call"):
    """The one primary button for a screen: the scheduler, else email, else the Book page."""
    if C.BOOKING_URL:
        return (f'<a class="btn" href="{e(C.BOOKING_URL)}" data-track="booking" data-where="{where}" '
                f'rel="noopener">{e(label_)}</a>')
    if C.EMAIL:
        return (f'<a class="btn" href="mailto:{e(C.EMAIL)}?subject=Scoping%20call" data-track="email" '
                f'data-where="{where}">{e(label_)}</a>')
    return f'<a class="btn" href="/book" data-where="{where}">{e(label_)}</a>'


def secondary_contacts():
    bits = []
    if C.BOOKING_URL and C.EMAIL:
        bits.append(f'Or email <a href="mailto:{e(C.EMAIL)}" data-track="email">{e(C.EMAIL)}</a>')
    if C.PHONE:
        bits.append(f'Call <a href="tel:{e(C.PHONE)}" data-track="phone">{e(C.PHONE_DISPLAY)}</a>')
    return ". ".join(bits) + ("." if bits else "")


def book_block(heading=None):
    """The booking card at the foot of most pages. The heading changes with the page."""
    h = heading or f"Talk it through on a {C.PROMISES['call_length']} call"
    sec = secondary_contacts()
    return f"""
<!--reuse--><section class="book" aria-labelledby="book-h"><div class="wrap"><div class="book-card">
  <div class="book-copy">
    <h2 id="book-h">{e(h)}</h2>
    <div>
    <p>Tell us what you sell, where you sell it and what runs your stock and books today. The call costs nothing,
    and if we aren't the right fit we'll say so. A written proposal follows {e(C.PROMISES['proposal_after_call'])}.</p>
    <div class="cta-line">{primary_cta("band")}{f'<p class="small">{sec}</p>' if sec else ''}</div>
    </div>
  </div>
</div></div></section><!--/reuse-->"""


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
        for q, a in faqs]}


def service_schema(p, path):
    url = SITE + path
    return {"@context": "https://schema.org", "@type": "Service", "@id": url + "#service",
            "name": p["name"], "serviceType": p["kind"], "description": p["summary"], "url": url,
            "provider": {"@id": SITE + "/#org"}, "areaServed": {"@type": "Country", "name": "US"}}


def crumbs(items):
    """items: [(name, path)], the last one is this page. Returns the trail and its BreadcrumbList schema."""
    parts = [f'<a href="{p}">{e(n)}</a><span aria-hidden="true">/</span>' for n, p in items[:-1]]
    parts.append(f'<span aria-current="page">{e(items[-1][0])}</span>')
    schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(items)]}
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>', schema


# ---------------------------------------------------------------------------
# Page parts
# ---------------------------------------------------------------------------

def qa_list(faqs, more=None):
    """Questions as disclosure rows. more: optional {question: (href, link text)}."""
    out = []
    for q, a in faqs:
        link = ""
        if more and q in more and more[q][0]:
            href, txt = more[q]
            link = f'<p class="qa-more"><a class="more" href="{href}">{e(txt)}{icon("arrow-right")}</a></p>'
        out.append(f'<details class="qa" id="q-{anchor(q)}"><summary><span>{e(q)}</span>'
                   f'<i class="qa-ic">{icon("chevron-down")}</i></summary><div class="qa-a"><p>{e(a)}</p>{link}</div></details>')
    return '<div class="qa-list">' + "".join(out) + "</div>"


# The yellow half highlight: one phrase per page heading, drawn in with the reveal (site.css .hl). Kept to the hero
# heading and a few home section heads so it stays a signature, not decoration.
HL = ["retailers and wholesalers", "with fixed fees", "by industry", "how we price them", "from first call to handover",
      "scoping call", "running both", "real Shopify and Odoo screens", "working with us", "plain words", "intact",
      "a fixed quote", "a team of 5 to 15", "stay in step", "after go-live", "apparel and footwear", "wholesalers and distributors",
      "food and beverage", "health and beauty", "furniture and home goods", "doesn't exist"]


def hl(text, phrases=None):
    """Escape a heading and wrap the first listed phrase it contains in the yellow highlight."""
    out = e(text)
    for p in (HL if phrases is None else phrases):
        ep = e(p)
        if ep in out:
            return out.replace(ep, f'<mark class="hl">{ep}</mark>', 1)
    return out


DECO_SETS = [(("dots", "tl"), ("ring", "br")), (("squiggle", "tr"), ("dots", "bl")), (("half", "tr"), ("plus", "bl")),
             (("tri", "tr"), ("dots", "bl")), (("zig", "tl"), ("ring", "br")), (("ring", "tr"), ("squiggle", "bl"))]


def deco_pair(seed):
    """Two brand shapes behind opposite corners of the hero art, picked from the heading so each page differs."""
    pair = DECO_SETS[sum(map(ord, seed)) % len(DECO_SETS)]
    return "".join(S.deco(n, f"d-{pos}") for n, pos in pair)


def deco_cluster():
    """Three shapes for the empty right side of a hero without art (wide screens only)."""
    return f'<div class="hero-shapes" aria-hidden="true">{S.deco("ring", "h1s")}{S.deco("dots", "h2s")}{S.deco("squiggle", "h3s")}</div>'


def sec_head(h2, lead="", hid=None, center=False, mark=""):
    h = hl(h2, [mark]) if mark else e(h2)
    return (f'<div class="sec-head{" center" if center else ""}"><h2{f" id={chr(34)}{hid}{chr(34)}" if hid else ""}>{h}</h2>'
            f'{f"<p class={chr(34)}lead{chr(34)}>{lead}</p>" if lead else ""}</div>')


def facts(rows, cls=""):
    """A row of label and value pairs, such as price, timeline and payment."""
    return (f'<dl class="facts {cls}">' + "".join(f'<div><dt>{e(k)}</dt><dd>{v}</dd></div>' for k, v in rows)
            + "</dl>")


def ticks(items, cls=""):
    return f'<ul class="ticks {cls}">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def more_link(href, text):
    return f'<a class="more" href="{href}">{e(text)}{icon("arrow-right")}</a>'


# ---------------------------------------------------------------------------
# Screens and recordings
# ---------------------------------------------------------------------------

def webp_size(path):
    b = (SRC / path).read_bytes()[:40]
    kind = b[12:16]
    if kind == b"VP8X":
        return int.from_bytes(b[24:27], "little") + 1, int.from_bytes(b[27:30], "little") + 1
    if kind == b"VP8L":
        v = int.from_bytes(b[21:25], "little")
        return (v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1
    return int.from_bytes(b[26:28], "little") & 0x3FFF, int.from_bytes(b[28:30], "little") & 0x3FFF


def jpeg_size(path):
    data = Path(path).read_bytes()
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return w, h
        i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    return 960, 600


def mp4_seconds(path):
    """Length of an MP4 from its mvhd box (stdlib only)."""
    data = Path(path).read_bytes()
    i = data.find(b"mvhd")
    if i < 0:
        return 0.0
    ver = data[i + 4]
    if ver == 1:
        scale, dur = struct.unpack(">IQ", data[i + 24:i + 36])
    else:
        scale, dur = struct.unpack(">II", data[i + 16:i + 24])
    return dur / scale if scale else 0.0


def mmss(sec):
    sec = int(round(sec))
    return f"{sec // 60}:{sec % 60:02d}"


PLATFORM = {"shopify": "Shopify", "odoo": "Odoo 20"}


def clip_info(key):
    """A recording from config.CLIPS, or None when it hasn't been made yet."""
    row = C.CLIPS.get(key)
    if not row:
        return None
    platform, app, title, desc, stem, recorded = row
    mp4 = SRC / f"{stem}.mp4"
    if not mp4.exists():
        ERRORS.append(f"CLIPS[{key!r}]: {stem}.mp4 is not in src/")
        return None
    return {"key": key, "platform": platform, "app": app, "title": title, "desc": desc, "stem": stem,
            "recorded": recorded, "seconds": mp4_seconds(mp4)}


def clip(key, title=True, lazy=True):
    """A silent screen recording in an app window. JS plays it while it is on screen; a button pauses it."""
    c = clip_info(key)
    if not c:
        NOTES.append(f"clip {key!r} not recorded yet; left out")
        return ""
    w, h = jpeg_size(SRC / f"{c['stem']}-poster.jpg")
    head = (f'<figcaption><b>{e(c["title"])}</b><span>{e(c["desc"])}</span></figcaption>' if title else
            f'<figcaption class="vh">{e(c["desc"])}</figcaption>')
    kind = "Real Shopify screens, shown step by step" if c["platform"] == "shopify" else "Silent screen recording"
    return f"""<figure class="clip clip-{c['platform']}" data-clip>
  <div class="win-bar"><i></i><i></i><i></i><span>{e(PLATFORM[c['platform']])} · {e(c['app'])}</span><em class="tag">Sample data</em></div>
  <div class="clip-frame"><video muted playsinline loop preload="{'none' if lazy else 'metadata'}" controls width="{w}" height="{h}"
  poster="/{e(c['stem'])}-poster.jpg" aria-label="{kind}: {e(c['desc'])}">
  <source src="/{e(c['stem'])}.webm" type="video/webm"><source src="/{e(c['stem'])}.mp4" type="video/mp4"></video></div>
  {head}
</figure>"""


def shot(key, cls="", eager=False):
    """A real screenshot from config.SCREENS in an app window."""
    s = C.SCREENS.get(key)
    if not s:
        return ""
    f, alt = s
    w, h = webp_size(f)
    app = "Shopify" if "/shopify/" in f else "Odoo 20"
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<figure class="clip shot {cls}"><div class="win-bar"><i></i><i></i><i></i><span>{app}</span>'
            f'<em class="tag">Sample data</em></div><div class="clip-frame"><img src="/{e(f)}" alt="{e(alt)}" '
            f'{load} decoding="async" width="{w}" height="{h}"></div></figure>')


def stack(back, front, cls="", eager=False):
    """Two real screens from config.SCREENS, layered: one behind, one in front and lower."""
    c = f"stack {cls}".strip()
    return (f'<div class="{c}"><div class="stack-back">{shot(back, eager=eager)}</div>'
            f'<div class="stack-front">{shot(front, eager=eager)}</div></div>')


def svc_stack(slug, cls="", eager=False):
    return stack(*SVC_STACK[slug], cls=cls, eager=eager)


def hero_art(name):
    """A diagram drawn for this page (art.py): inline SVG built from the page's own content."""
    return A.hero_art(name)


def gap_art():
    """The home page map of who covers which step of an order (art.py)."""
    return A.gap_art()


def json_attr(obj):
    return e(json.dumps(obj))
