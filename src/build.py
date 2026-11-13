#!/usr/bin/env python3
"""Build the [DBA name] static site into dist/ (v5).

Python standard library only. Business facts come from config.py and industries.py; page copy lives in pages.py
and pages_res.py; shared parts in kit.py; styles and behavior in site.css and site.js. This file is the engine:
assets, the page frame, site files and the checks.

    python3 src/build.py            preview build (prints NOTEs for blank fields)
    python3 src/build.py --release  production build: fails while any
                                    launch-critical field is still blank

Workers Builds must run the --release form so an unfinished site can never deploy.
"""

import datetime as _dt
import hashlib
import html
import json
import re
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
SRC = Path(__file__).resolve().parent
ROOT = SRC.parent
DIST = ROOT / "dist"
sys.path.insert(0, str(SRC))
from kit import (C, ERRORS, MISSING_SPOT, NAME, NOTES, RELEASE, SITE, TODAY, book_block, clean_url, e, meta_desc,  # noqa: E402
                 price, svc_href)
import industries as I  # noqa: E402
import pages as P  # noqa: E402
import pages_res as PR  # noqa: E402

HUB_PATHS = PR.HUB_PATHS


# ---------------------------------------------------------------------------
# Assets: fonts, CSS and JS with content-hashed names
# ---------------------------------------------------------------------------

FONT_FILES = [
    # (family, weight, file in src/fonts/) - OFL fonts, self-hosted. Add the
    # woff2 files to src/fonts/; missing files fall back to the system stack.
    ("Archivo", "100 900", "archivo-latin-wght-normal.woff2"),  # variable weight
    ("IBM Plex Sans", 400, "ibm-plex-sans-latin-400-normal.woff2"),
    ("IBM Plex Sans", 500, "ibm-plex-sans-latin-500-normal.woff2"),
    ("IBM Plex Sans", 600, "ibm-plex-sans-latin-600-normal.woff2"),
]
STATIC_FILES = ["og.png", "apple-touch-icon.png"]  # share image (1200x630) and phone home-screen icon
PRELOAD = ["archivo-latin-wght-normal.woff2", "ibm-plex-sans-latin-400-normal.woff2"]


def build_assets():
    (DIST / "assets").mkdir(parents=True, exist_ok=True)
    (DIST / "fonts").mkdir(parents=True, exist_ok=True)
    faces, missing = [], []
    for family, weight, fname in FONT_FILES:
        f = SRC / "fonts" / fname
        if f.exists():
            shutil.copy(f, DIST / "fonts" / fname)
            faces.append(
                f"@font-face{{font-family:\"{family}\";font-style:normal;font-weight:{weight};"
                f"font-display:swap;src:url(/fonts/{fname}) format(\"woff2\")}}"
            )
        else:
            missing.append(fname)
    if missing:
        NOTES.append("fonts not in src/fonts/ yet, system fallback used: " + ", ".join(missing))
    for fname in STATIC_FILES:
        shutil.copy(SRC / fname, DIST / fname)
    if (SRC / "media").exists():
        shutil.copytree(SRC / "media", DIST / "media", dirs_exist_ok=True)
    for key, row in C.CLIPS.items():
        for ext in (".mp4", ".webm", "-poster.jpg"):
            if not (SRC / (row[4] + ext)).exists():
                ERRORS.append(f"CLIPS[{key!r}]: {row[4] + ext} is not in src/")
    for key, (fname, _alt) in C.SCREENS.items():
        if not (SRC / fname).exists():
            ERRORS.append(f"SCREENS[{key!r}]: {fname} is not in src/")
    css = "\n".join(faces) + "\n" + (SRC / "site.css").read_text()
    js = (SRC / "site.js").read_text()
    names = {}
    for kind, body in (("css", css), ("js", js)):
        h = hashlib.sha256(body.encode()).hexdigest()[:10]
        name = f"site.{h}.{kind}"
        (DIST / "assets" / name).write_text(body)
        names[kind] = f"/assets/{name}"
    return names


# ---------------------------------------------------------------------------
# Contact, offer and schema
# ---------------------------------------------------------------------------

def contact_state():
    if C.PHONE and not C.PHONE_DISPLAY:
        ERRORS.append("PHONE is set but PHONE_DISPLAY is blank")
    if C.PHONE and re.search(r"555[-. ]?01\d\d|\(?555\)?", C.PHONE):
        ERRORS.append("PHONE looks like a 555 placeholder. Only a number that rings Vee may ship.")
    if not C.BOOKING_URL:
        NOTES.append("BOOKING_URL blank: booking buttons fall back to email" if C.EMAIL
                     else "BOOKING_URL and EMAIL both blank: booking buttons point at /book (preview only)")


def head_cta():
    """Small header button. Outlined, so the page keeps one primary button per screen."""
    if C.BOOKING_URL:
        return (f'<a class="btn-sm" href="{e(C.BOOKING_URL)}" data-track="booking" data-where="header" '
                f'rel="noopener">Book a call</a>')
    return '<a class="btn-sm" href="/book">Book a call</a>'


def cta_bar(path):
    """Phone-only bar that shows once no other booking button is on screen."""
    if path in ("/book", "/404"):
        return ""
    return (f'<div class="cta-bar" data-cta-bar><span>{e(C.PROMISES["call_length"]).capitalize()} call, no charge</span>'
            f'{P.primary_cta("bar")}</div>')


def offer_bar():
    o = C.OFFER
    if not o:
        return ""
    for k in ("text", "terms", "regular_price", "capacity", "end"):
        if not o.get(k):
            ERRORS.append(f"OFFER.{k} is required for any offer (00, Stay legal and honest)")
            return ""
    end = _dt.date.fromisoformat(o["end"])
    if TODAY > end:
        NOTES.append(f"OFFER ended {end.isoformat()} and is hidden; remove it from config")
        return ""
    return (f'<div class="offer"><div class="wrap"><strong>{e(o["text"])}</strong> '
            f'<span>Regular price {e(o["regular_price"])}. {e(o["capacity"])}. Ends '
            f'{end.strftime("%B %-d, %Y")}. {e(o["terms"])}</span></div></div>')


# ---------------------------------------------------------------------------
# Page frame
# ---------------------------------------------------------------------------

def org_schema():
    data = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": SITE + "/#org",
        "name": NAME,
        "url": SITE + "/",
        "areaServed": {"@type": "Country", "name": "US"},
        "description": ("Ecommerce and ERP consulting for US product businesses: Shopify store moves, Odoo "
                        "back office setups, the connection between them, and support."),
        "founder": {"@type": "Person", "name": C.FOUNDER},
        "logo": SITE + "/favicon.svg",
    }
    if C.EMAIL:
        data["email"] = C.EMAIL
    if C.PHONE:
        data["telephone"] = C.PHONE
    if C.PROFILES:
        data["sameAs"] = [u for _, u in C.PROFILES]
    return data


NAV = [("/services", "Services"), ("/industries", "Industries"), ("/pricing", "Pricing"),
       ("/resources", "Resources"), ("/about", "About")]


def wordmark():
    return (f'<a class="brand" href="/" aria-label="{e(NAME)} home">'
            f'<span class="mark" aria-hidden="true"></span><span>{e(NAME)}</span></a>')


def layout(page, assets):
    path = page["path"]
    title = page["title"]
    if len(title) > 66:
        ERRORS.append(f"title over 66 characters on {path}: {title!r} ({len(title)})")
    desc = meta_desc(page["desc"])
    canonical = clean_url(path) if page.get("index", True) else None
    schemas = [org_schema()] + page.get("schema", [])
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
                   for s in schemas)

    def here(href):
        if href == path:
            return ' aria-current="page"'
        if href == "/resources" and path.startswith(HUB_PATHS):
            return ' aria-current="true"'
        if path.startswith(href + "/"):
            return ' aria-current="true"'
        return ""
    nav = "".join(f'<a href="{href}"{here(href)}>{label_}</a>' for href, label_ in NAV)
    preload = "\n".join(f'<link rel="preload" href="/fonts/{f}" as="font" type="font/woff2" crossorigin>'
                        for f in PRELOAD if (SRC / "fonts" / f).exists())
    robots = '<meta name="robots" content="noindex">' if not page.get("index", True) else ""
    preview = ""
    if not RELEASE:
        preview = ('<div class="preview-flag" role="note">Staging build. Contact details, name and '
                   'domain are not final.</div>')
    cf = ""
    if C.CF_WEB_ANALYTICS_TOKEN:
        cf = (f'<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
              f'data-cf-beacon=\'{{"token":"{e(C.CF_WEB_ANALYTICS_TOKEN)}"}}\'></script>')
    profiles = " ".join(f'<a href="{e(u)}" rel="me noopener">{e(n)}</a>' for n, u in C.PROFILES)
    band = "" if page.get("no_band") else book_block(page.get("band"))
    svc_links = "".join(f'<a href="{svc_href(x["slug"])}">{e(x["name"])}</a>' for x in C.PACKAGES)
    ind_links = "".join(f'<a href="/industries/{x["slug"]}">{e(x["short"])}</a>' for x in I.INDUSTRIES)
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{f'<link rel="canonical" href="{canonical}">' if canonical else ''}
{robots}
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
{f'<meta property="og:url" content="{canonical}">' if canonical else ''}
<meta property="og:site_name" content="{e(NAME)}">
<meta property="og:image" content="{SITE}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="A shop, a box of stock and an invoice joined by one dotted path">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#fbf7f0">
<meta name="color-scheme" content="light">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
{preload}
<link rel="stylesheet" href="{assets['css']}">
<script defer src="{assets['js']}"></script>
{cf}
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{preview}
{offer_bar()}
<header class="site-head">
  <div class="wrap head-grid">
    {wordmark()}
    <button type="button" class="menu-btn" aria-expanded="false" aria-controls="site-nav" hidden>Menu</button>
    <nav id="site-nav" aria-label="Main">{nav}</nav>
    {head_cta()}
  </div>
</header>
<main id="main">
{page['body']}
{band}
</main>
{cta_bar(path)}
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">{wordmark()}<p>{e(C.TAGLINE)}</p>{f'<p>{profiles}</p>' if profiles else ''}</div>
      <nav aria-label="Services" class="foot-links"><b>Services</b>{svc_links}
        <a href="{svc_href('support')}">{e(C.SUPPORT['name'])}</a></nav>
      <nav aria-label="Industries" class="foot-links"><b>Industries</b>{ind_links}</nav>
      <nav aria-label="Resources" class="foot-links"><b>Resources</b>
        <a href="/resources">Guides</a><a href="/videos">Recordings</a><a href="/faq">Questions</a><a href="/glossary">Glossary</a></nav>
      <nav aria-label="Company" class="foot-links"><b>Company</b>
        <a href="/how-it-works">How we work</a><a href="/pricing">Pricing</a><a href="/about">About</a>
        <a href="/book">Book a call</a></nav>
    </div>
    <div class="foot-legal">
      <p>{e(C.REFERRAL_DISCLOSURE.format(name=NAME))}</p>
      <p>Shopify is a trademark of Shopify Inc. Odoo is a trademark of Odoo S.A. We are not affiliated with or endorsed
      by either unless stated.</p>
      <p>&copy; {TODAY.year} {e(NAME)} · <a href="/privacy">Privacy</a> · <a href="/terms">Terms</a></p>
    </div>
  </div>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Checks across pages: near-duplicate text and internal links
# ---------------------------------------------------------------------------

def main_words(html_text):
    m = re.search(r'<main id="main">(.*?)</main>', html_text, re.S)
    s = m.group(1) if m else ""
    s = re.sub(r"<!--reuse-->.*?<!--/reuse-->", " ", s, flags=re.S)
    s = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).lower()
    return re.findall(r"[a-z0-9$][a-z0-9$.,'%-]*", s)


def duplicate_check(built, n=12):
    """Resource pages must not repeat a long run of words from another page (00: original content)."""
    shingles = {}
    for path, words in built.items():
        for i in range(len(words) - n + 1):
            shingles.setdefault(" ".join(words[i:i + n]), set()).add(path)
    pairs = {}
    for sh, paths in shingles.items():
        if len(paths) > 1:
            ps = sorted(paths)
            for a in ps:
                for b in ps:
                    if a < b:
                        pairs.setdefault((a, b), []).append(sh)
    core = 0
    for (a, b), shs in sorted(pairs.items()):
        if any(p.startswith(HUB_PATHS) for p in (a, b)):
            if len(shs) >= 2:
                ERRORS.append(f"near-duplicate text: {len(shs)} repeated {n}-word runs between {a} and {b}, "
                              f"e.g. {shs[0]!r}. Rewrite it, or wrap a reused widget in <!--reuse--> comments.")
        else:
            core += 1
    if core:
        NOTES.append(f"{core} pairs of core pages share widget or price text (only resource pages are checked)")


def link_check(built_paths):
    """Every internal link points at a page or file this build writes."""
    for f in DIST.rglob("*.html"):
        for href in re.findall(r'href="(/[^"#?]*)', f.read_text()):
            if href in built_paths or (DIST / href.lstrip("/")).exists():
                continue
            ERRORS.append(f"broken internal link {href} in {f.relative_to(DIST)}")


HEADERS = """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: DENY
  Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()
  Content-Security-Policy: default-src 'self'; script-src 'self' https://static.cloudflareinsights.com; connect-src 'self' https://cloudflareinsights.com; img-src 'self' data:; style-src 'self'; font-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
  Cache-Control: public, max-age=0, must-revalidate

/assets/*
  ! Cache-Control
  Cache-Control: public, max-age=31536000, immutable

/fonts/*
  ! Cache-Control
  Cache-Control: public, max-age=31536000, immutable

/favicon.svg
  ! Cache-Control
  Cache-Control: public, max-age=86400

/og.png
  ! Cache-Control
  Cache-Control: public, max-age=86400

/media/*
  ! Cache-Control
  Cache-Control: public, max-age=604800
"""

# Staging (any build without --release) must never be indexed, wherever it is hosted.
STAGING_HEADERS = """
/*
  X-Robots-Tag: noindex, nofollow
"""

# 301s for any URL that changes. Format: "/old /new 301"
REDIRECTS = [
    "/index / 301",
    "/home / 301",
    "/contact /book 301",
    "/sitemap / 301",
    "/site-map / 301",
    "/shopify /services/store-move 301",
    "/odoo /services/back-office-launch 301",
    "/guides /resources 301",
    "/tools /resources 301",
    "/tools/shopify-plan-picker /services/store-move 301",
    "/tools/erp-readiness /services/systems-roadmap 301",
    "/tools/sync-simulator /services/store-to-back-office-sync 301",
    "/tools/odoo-tours /services/back-office-launch 301",
    "/videos/* /videos 301",
    "/faq/* /faq 301",
]

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" fill="#141c2b"/><rect x="6" y="20" width="20" height="6" fill="#e0a526"/></svg>"""


def write_site_files(indexable):
    (DIST / "_headers").write_text(HEADERS + ("" if RELEASE else STAGING_HEADERS))
    (DIST / "_redirects").write_text("\n".join(REDIRECTS) + "\n")
    if RELEASE:
        (DIST / "robots.txt").write_text(
            "# All crawlers are welcome, including AI crawlers.\nUser-agent: *\nAllow: /\n\n"
            f"Sitemap: {SITE}/sitemap.xml\n")
    else:
        (DIST / "robots.txt").write_text("# Staging build. Not for indexing.\nUser-agent: *\nDisallow: /\n")
    urls = []
    for p in indexable:
        lm = p.get("lastmod") or C.LAST_CHANGED.get(p["path"])
        urls.append(f"  <url><loc>{clean_url(p['path'])}</loc>" +
                    (f"<lastmod>{lm}</lastmod>" if lm else "") + "</url>")
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    svc = "\n".join(
        f"- [{p['name']}]({SITE}{svc_href(p['slug'])}): typically {p['timeline']}, fixed fee quoted after a free call. "
        f"{p['summary']}" for p in C.PACKAGES)
    sup = "; ".join(f"{h}, {v}" for h, k, v in C.SUPPORT["options"])
    inds = "\n".join(f"- [{x['short']}]({SITE}/industries/{x['slug']}): " +
                     "; ".join(pr[0] for pr in x["problems"]) + "." for x in I.INDUSTRIES)
    contact = []
    if C.EMAIL:
        contact.append(f"- Email: {C.EMAIL}")
    if C.BOOKING_URL:
        contact.append(f"- Book a call: {C.BOOKING_URL}")
    guides = ""
    if PR.guides_live():
        guides = "\n\n## Guides\n" + "\n".join(
            f"- [{g['title']}]({SITE}/guides/{g['slug']}): {PR.fill(g['short'])} (checked {g['checked']})"
            for g in PR.guides_live())
    llms = f"""# {NAME}

> Ecommerce and ERP consulting for US product businesses. {NAME} plans, sets up and connects Shopify and Odoo, works remotely from {C.STATE} for clients across the US, and runs every project on a fixed fee and a written scope.

## Services
{svc}
- [Support block]({SITE}{svc_href('support')}): {sup}.
- Larger Odoo projects: {C.LARGER_PROJECTS}

## Industries
{inds}

## Questions people ask
""" + "\n".join(f"- {q} {fn()}" for q, fn in P.HOME_FAQS) + guides + f"""

## How we work
- [How a project works]({SITE}/how-it-works)
- Clients pay Shopify, Odoo and app vendors directly; our fees are for services only.
- {C.REFERRAL_DISCLOSURE.format(name=NAME)}

## Pages
""" + "\n".join(f"- [{p['h']}]({clean_url(p['path'])})" for p in indexable) + "\n"
    if contact:
        llms += "\n## Contact\n" + "\n".join(contact) + "\n"
    check_fees("llms.txt", llms)
    (DIST / "llms.txt").write_text(llms)
    key = C.INDEXNOW_KEY
    if not re.fullmatch(r"[A-Za-z0-9-]{8,128}", key or ""):
        ERRORS.append("INDEXNOW_KEY must be 8 to 128 letters, digits or dashes")
    else:
        (DIST / f"{key}.txt").write_text(key)
    (DIST / "favicon.svg").write_text(FAVICON)
    (DIST / "site.webmanifest").write_text(json.dumps({
        "name": NAME, "short_name": NAME, "start_url": "/", "display": "browser",
        "background_color": "#fbf7f0", "theme_color": "#fbf7f0",
        "icons": [{"src": "/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=1))


# ---------------------------------------------------------------------------
# Checks: NO AI LOOK tells and leaks in the built output
# ---------------------------------------------------------------------------

BANNED = ["transform", "elevate", "seamless", "unlock", "leverage", "empower", "game-changer",
          "revolutionary", "streamline your operations", "fast-paced", "end-to-end solution",
          "digital transformation", "synergy", "robust", "cutting-edge", "curated", "effortless"]


# Vendor list prices that happen to equal one of our internal numbers. Each is matched in its exact context
# and removed before the fee check, so only that vendor fact passes.
VENDOR_PRICE_OK = [
    r'data-label="Hours">50</td><td data-label="List price">\$7,000',  # Odoo Success Pack Standard, odoo.com/pricing-packs
]


def check_fees(path, text):
    """Our package fees are internal (Vee, Nov 13). Fail if any of them reaches a public file, source included."""
    for ok in VENDOR_PRICE_OK:
        text = re.sub(ok, "", text)
    for k, v in C.PRICES.items():
        if re.search(r"\$\s?" + f"{v:,}".replace(",", ",?") + r"(?!\d)", text):
            ERRORS.append(f"our fee {k} (${v:,}) appears in {path}; fees are quoted after a call only")


def check_output(path, text):
    check_fees(path, text)
    visible = re.sub(r"<script.*?</script>|<style.*?</style>", "", text, flags=re.S)
    visible = re.sub(r"<[^>]+>", " ", visible)
    if "—" in text:
        ERRORS.append(f"em dash in {path}")
    for m in re.finditer("–", visible):
        ctx = visible[max(0, m.start() - 12):m.end() + 12]
        if not re.search(r"[\d$]\s?–\s?[\d$]", ctx):
            ERRORS.append(f"en dash outside a range in {path}: {ctx.strip()!r}")
    low = visible.lower()
    for w in BANNED:
        if re.search(r"\b" + re.escape(w), low):
            ERRORS.append(f"banned word {w!r} in {path}")
    for h in re.findall(r"<h[1-3][^>]*>(.*?)</h[1-3]>", text, flags=re.S):
        if "!" in h:
            ERRORS.append(f"exclamation mark in a heading in {path}")
    if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", visible):
        ERRORS.append(f"emoji in {path}")
    if re.search(r"555[-. ]\d{4}", re.sub(r"<svg.*?</svg>", "", text, flags=re.S)):
        ERRORS.append(f"555 number in {path}")
    if re.search(r"part[- ]time|first clients|new business|hourly rate", low):
        ERRORS.append(f"over-sharing phrase in {path}")


def release_checks():
    if "[" in NAME or not NAME.strip():
        ERRORS.append("BUSINESS_NAME is still a placeholder (thread 03)")
    if not C.DOMAIN:
        ERRORS.append("DOMAIN is blank (thread 03)")
    if not (C.BOOKING_URL or C.EMAIL):
        ERRORS.append("no real contact path: set EMAIL and, ideally, BOOKING_URL (thread 10)")
    if not C.ABOUT_BIO:
        ERRORS.append("ABOUT_BIO is blank: Vee's own words are needed before launch")
    if "[" in C.LEGAL_LINE:
        ERRORS.append("LEGAL_LINE still has a placeholder")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    contact_state()
    if RELEASE:
        release_checks()
    assets = build_assets()
    pages = P.core_pages() + PR.res_pages() + PR.legal_pages()
    for p in pages:
        if not p.get("h"):
            ERRORS.append(f"page {p['path']} has no short name (h)")
    pages.append(PR.page_404())

    built = {}
    for p in pages:
        out = layout(p, assets)
        check_output(p["file"], out)
        (DIST / p["file"]).parent.mkdir(parents=True, exist_ok=True)
        (DIST / p["file"]).write_text(out)
        if p.get("index", True):
            built[p["path"]] = main_words(out)
    duplicate_check(built)

    indexable = [p for p in pages if p.get("index", True)]
    write_site_files(indexable)
    link_check({p["path"] for p in pages})
    for n in sorted(MISSING_SPOT):
        ERRORS.append(f"icon '{n}' has no custom spot icon (add it to spot.ICONS or spot.SPOT_FOR)")

    for n in dict.fromkeys(NOTES):
        print("NOTE:", n)
    if ERRORS:
        for x in ERRORS:
            print("ERROR:", x, file=sys.stderr)
        print(f"Build failed with {len(ERRORS)} error(s).", file=sys.stderr)
        sys.exit(1)
    print(f"Built {len(indexable)} indexable pages{' (release)' if RELEASE else ' (staging: noindex, not for launch)'}")


if __name__ == "__main__":
    main()
