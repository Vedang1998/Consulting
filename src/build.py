#!/usr/bin/env python3
"""Build the [DBA name] static site into dist/.

Python standard library only. Business facts come from config.py; templates and
copy live here; styles and behavior live in site.css and site.js.

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
import config as C  # noqa: E402
import mockups as M  # noqa: E402

RELEASE = "--release" in sys.argv
TODAY = _dt.date.today()
NOTES, ERRORS = [], []

NAME = C.BUSINESS_NAME
SITE = f"https://{C.DOMAIN}" if C.DOMAIN else "https://domain-not-set.invalid"


# ---------------------------------------------------------------------------
# Helpers
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
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    out = ""
    for s in sentences:
        trial = (out + " " + s).strip()
        if len(trial) > limit:
            break
        out = trial
    if not out:
        ERRORS.append(f"meta description has no sentence under {limit} characters: {text[:60]}...")
    return out


def clean_url(path):
    """Extensionless canonical URL: '/' or '/services'."""
    path = "/" + path.strip("/")
    return SITE + ("" if path == "/" else path)


def para(*lines):
    return "".join(f"<p>{x}</p>" for x in lines)


def label(text):
    return f'<span class="tag">{e(text)}</span>'


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
    ("IBM Plex Mono", 400, "ibm-plex-mono-latin-400-normal.woff2"),
    ("IBM Plex Mono", 500, "ibm-plex-mono-latin-500-normal.woff2"),
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
    for key, fname in C.DEMO_VIDEOS.items():
        f = SRC / fname
        if not f.exists():
            ERRORS.append(f"DEMO_VIDEOS[{key!r}]: {fname} is not in src/")
            continue
        (DIST / fname).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(f, DIST / fname)
    for fname in STATIC_FILES:
        shutil.copy(SRC / fname, DIST / fname)
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
# Contact and booking
# ---------------------------------------------------------------------------

def contact_state():
    if C.PHONE and not C.PHONE_DISPLAY:
        ERRORS.append("PHONE is set but PHONE_DISPLAY is blank")
    if C.PHONE and re.search(r"555[-. ]?01\d\d|\(?555\)?", C.PHONE):
        ERRORS.append("PHONE looks like a 555 placeholder. Only a number that rings Vee may ship.")
    if not C.BOOKING_URL:
        NOTES.append("BOOKING_URL blank: booking buttons fall back to email" if C.EMAIL
                     else "BOOKING_URL and EMAIL both blank: contact panels are hidden (preview only)")


def primary_cta(where):
    """The one primary button for a screen. Booking first, email second, nothing if neither is real."""
    if C.BOOKING_URL:
        return (f'<a class="btn" href="{e(C.BOOKING_URL)}" data-track="booking" data-where="{where}" '
                f'rel="noopener">Book a scoping call</a>')
    if C.EMAIL:
        return (f'<a class="btn" href="mailto:{e(C.EMAIL)}?subject=Scoping%20call" data-track="email" data-where="{where}">'
                f'Email {e(C.EMAIL)}</a>')
    return ""


def secondary_contacts():
    bits = []
    if C.BOOKING_URL and C.EMAIL:
        bits.append(f'Or email <a href="mailto:{e(C.EMAIL)}" data-track="email">{e(C.EMAIL)}</a>')
    if C.PHONE:
        bits.append(f'Call <a href="tel:{e(C.PHONE)}" data-track="phone">{e(C.PHONE_DISPLAY)}</a>')
    return ". ".join(bits) + ("." if bits else "")


def booking_band():
    cta = primary_cta("band")
    if not cta:
        return ""
    nxt = [("Pick a time" if C.BOOKING_URL else "Send a short email",
            "Tell us what you sell, where you sell it and what runs your stock and books today."),
           (f"A {C.PROMISES['call_length']} video call",
            "We go through your setup and timeline. If we are not the right fit, we say so."),
           ("A written proposal",
            f"A proposal or Roadmap quote reaches you {C.PROMISES['proposal_after_call']}.")]
    steps = "".join(f"<li><b>{e(h)}</b><span>{e(t)}</span></li>" for h, t in nxt)
    return f"""
<section class="band" aria-labelledby="band-h" data-sec="band">
  <div class="wrap band-grid">
    <div class="band-copy">
      <h2 id="band-h">Talk through your setup on a {e(C.PROMISES['call_length'])} call</h2>
      <p>There is no charge for the call. We reply {e(C.PROMISES['first_reply'])},
      {e(C.PROMISES['business_days'])}, {e(C.TIMEZONE_LABEL)} time.</p>
      <ol class="next">{steps}</ol>
      <div class="band-cta">{cta}<p class="small">{secondary_contacts()}</p></div>
    </div>
    <div class="band-art">{M.scene_flow()}</div>
  </div>
</section>"""


def head_cta(path):
    """Small header button. Outlined, so the page keeps one primary button per screen."""
    if path == "/book" or not (C.BOOKING_URL or C.EMAIL):
        return ""
    if C.BOOKING_URL:
        return (f'<a class="btn-sm" href="{e(C.BOOKING_URL)}" data-track="booking" data-where="header" '
                f'rel="noopener">Book a scoping call</a>')
    return '<a class="btn-sm" href="/book">Book a scoping call</a>'


def cta_bar(path):
    """Phone-only bar that shows once the hero button has scrolled away."""
    cta = primary_cta("bar")
    if not cta or path == "/book":
        return ""
    return (f'<div class="cta-bar" data-cta-bar><span>{e(C.PROMISES["call_length"]).capitalize()} call, no charge</span>'
            f'{cta}</div>')


# ---------------------------------------------------------------------------
# Offer (auto-expires from config)
# ---------------------------------------------------------------------------

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
# Schema
# ---------------------------------------------------------------------------

def org_schema():
    data = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": SITE + "/#org",
        "name": NAME,
        "url": SITE + "/",
        "areaServed": {"@type": "Country", "name": "US"},
        "description": ("Remote Shopify and Odoo consulting for small and mid-size US businesses: "
                        "store moves, Odoo rollouts, Shopify and Odoo connections and support."),
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


def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in faqs
        ],
    }


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------

NAV = [("/services", "Services"), ("/how-it-works", "How it works"), ("/about", "About")]


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
    hcta = head_cta(path)
    nav_items = NAV if hcta else NAV + [("/book", "Book a call")]
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == path else ""}>{label_}</a>'
        for href, label_ in nav_items)
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
    band = "" if page.get("no_band") else booking_band()
    year = TODAY.year
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
<meta property="og:image:alt" content="A storefront, warehouse shelves and a ledger joined by one path">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#141c2b">
<meta name="color-scheme" content="light dark">
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
<div class="progress" aria-hidden="true"><i></i></div>
{preview}
{offer_bar()}
<header class="site-head{' on-dark' if page.get('dark_head') else ''}">
  <div class="wrap head-grid">
    {wordmark()}
    <nav aria-label="Main">{nav}</nav>
    {hcta}
  </div>
</header>
<main id="main">
{page['body']}
</main>
{band}
{cta_bar(path)}
<footer class="site-foot">
  <div class="wrap foot-grid">
    <div>
      {wordmark()}
      <p class="small">{e(C.TAGLINE)}</p>
      {f'<p class="small">{profiles}</p>' if profiles else ''}
    </div>
    <nav aria-label="Footer" class="foot-links">
      <a href="/services">Services</a><a href="/how-it-works">How it works</a>
      <a href="/about">About</a><a href="/book">Book a call</a>
      <a href="/privacy">Privacy</a><a href="/terms">Terms</a><a href="/site-map">Site map</a>
    </nav>
    <div class="small foot-legal">
      <p>{e(C.REFERRAL_DISCLOSURE.format(name=NAME))}</p>
      <p>Shopify is a trademark of Shopify Inc. Odoo is a trademark of Odoo S.A.</p>
      <p>&copy; {year} {e(NAME)}</p>
    </div>
  </div>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

HOME_FAQS = [
    ("How much does a Shopify and Odoo project cost?",
     lambda: (f"A Systems Roadmap is {price('roadmap_min', 'roadmap_max')}. A Store Move is "
              f"{price('store_move_min', 'store_move_max')}, a Back Office Launch is "
              f"{price('odoo_launch_min', 'odoo_launch_max')} and a Store to Back Office Sync is "
              f"{price('connection_min', 'connection_max')}. Your exact fee is fixed in writing before work "
              f"starts. Shopify, Odoo and app vendors bill you separately for plans and licenses.")),
    ("How long does a project take?",
     lambda: ("A Systems Roadmap takes 2 to 3 weeks. A Store Move takes 3 to 8 weeks, a Store to Back Office "
              "Sync 3 to 6 weeks and a Back Office Launch 6 to 12 weeks. Go-live dates are planned around "
              "your peak season.")),
    ("Does connecting Shopify to Odoo need a particular Odoo plan?",
     lambda: ("It depends on the connector. Third-party connector modules can't be installed on Odoo Online, "
              "and connectors that use Odoo's API need its Custom plan. We check the fit in a trial database "
              "before you buy anything.")),
    ("Who owns the accounts and the data?",
     lambda: ("You do. Your Shopify store, Odoo database and app accounts stay in your name and on your "
              "billing. We work through named staff or collaborator accounts, and we remove our access at "
              "project close and confirm it in writing.")),
    ("What happens on the scoping call?",
     lambda: (f"It is a {C.PROMISES['call_length']} video call at no charge. We go through what you sell, "
              f"your channels, your current systems and your timeline. You get a proposal or a Roadmap quote "
              f"{C.PROMISES['proposal_after_call']}. If we are not the right fit, we say so on the call.")),
    ("What if the scope changes during the project?",
     lambda: ("We stop that part and send a written change order with the price and the effect on dates. "
              "It starts once you sign.")),
    ("Do you work with businesses outside New York?",
     lambda: (f"Yes. All work is remote, for businesses anywhere in the US, during {C.TIMEZONE_LABEL} "
              f"business hours.")),
]


def first_sentence(text):
    return text.split(". ")[0].rstrip(".") + "."


def svc_card(slug, kind, name, summary, price_html, meta, wide=False):
    return f"""
<a class="svc reveal{' svc-wide' if wide else ''}" href="/services#{slug}">
  {M.MINIS[slug]()}
  <span class="svc-kind">{e(kind)}</span>
  <span class="svc-name">{e(name)}{M.icon('arrow-right')}</span>
  <span class="svc-sum">{e(summary)}</span>
  <span class="svc-foot"><span class="price">{price_html}</span><span>{e(meta)}</span></span>
</a>"""


def finder():
    """Three questions, answers picked in the browser, every result written here from config."""
    def q(n, legend, opts):
        btns = "".join(f'<button type="button" class="opt" data-v="{v}" aria-pressed="false">{e(t)}</button>'
                       for v, t in opts)
        return (f'<fieldset class="fq" data-q="{n}"{"" if n == 1 else " hidden"}><legend><span class="fq-n">{n} of 3</span>'
                f'{e(legend)}</legend><div class="opts">{btns}</div></fieldset>')

    qs = (q(1, "What do you need first?",
            [("move", "Move my store to Shopify"), ("odoo", "Set up Odoo for the back office"),
             ("connect", "Connect Shopify and Odoo"), ("support", "Help with a setup that is already live"),
             ("unsure", "Not sure yet")]) +
          q(2, "How many people will use the system?",
            [("s", "Up to 15"), ("m", "16 to 50"), ("l", "More than 50")]) +
          q(3, "When does it need to be live?",
            [("soon", "Within 2 months"), ("mid", "In 3 to 6 months"), ("open", "No fixed date")]))

    cta = primary_cta("finder")
    results = []
    by_slug = {p["slug"]: p for p in C.PACKAGES}
    why = {
        "systems-roadmap": "A Roadmap comes first when the scope is still open or the project is larger. It ends "
                           "in a written plan and a fixed quote for the build.",
        "store-move": "Your first step is the store itself. A scoping call is usually enough to fix the fee.",
        "odoo-launch": "This is the standard Odoo setup for a team of up to 15 users.",
        "connection": "Both systems are in place, so the work is the connector, the sync rules and the tests.",
    }
    for slug, p in by_slug.items():
        soon = ""
        if slug == "odoo-launch":
            soon = (f'<p class="fr-note" data-when="soon" hidden>A {e(p["name"])} typically takes {e(p["timeline"])}, '
                    f'so a go-live inside two months needs a narrow first phase. Raise it on the call.</p>')
        results.append(f"""
<div class="fr" data-result="{slug}" hidden>
  <p class="eyebrow">Where we would start</p>
  <h3>{e(p['name'])}</h3>
  <dl class="facts"><div><dt>Price</dt><dd class="price">{price(*p['price'])}</dd></div>
  <div><dt>Typical timeline</dt><dd>{e(p['timeline'])}</dd></div></dl>
  <p>{e(why[slug])}</p>{soon}
  <div class="fr-cta">{cta}<a class="more" href="/services#{slug}">See what is included{M.icon('arrow-right')}</a></div>
</div>""")
    s = C.SUPPORT
    results.append(f"""
<div class="fr" data-result="support" hidden>
  <p class="eyebrow">Where we would start</p>
  <h3>{e(s['name'])}</h3>
  <dl class="facts"><div><dt>10 hours</dt><dd class="price">{price('support_10h')}</dd></div>
  <div><dt>20 hours</dt><dd class="price">{price('support_20h')}</dd></div></dl>
  <p>Prepaid hours for questions, small changes, reports and training on a setup that is already running.
  We reply {e(C.PROMISES['support_reply'])}.</p>
  <div class="fr-cta">{cta}<a class="more" href="/services#support">See the terms{M.icon('arrow-right')}</a></div>
</div>""")
    results.append(f"""
<div class="fr" data-result="nofit" hidden>
  <p class="eyebrow">Probably not us</p>
  <h3>A larger agency is the better fit</h3>
  <p>Setups for more than 50 users are outside the work we take on. An Odoo partner with a bigger team,
  or Odoo itself, will serve you better. If part of the work is a Shopify store move, that part we can do.</p>
  <div class="fr-cta"><a class="more" href="/services#store-move">See the Store Move{M.icon('arrow-right')}</a></div>
</div>""")
    return f"""
<div class="finder" data-finder hidden>
  <div class="finder-q">{qs}</div>
  <div class="finder-r" aria-live="polite">
    <div class="fr-empty" data-empty>{M.blob(1)}<p>Answer three questions and the service that fits shows here, with its
    price range and timeline.</p></div>
    {''.join(results)}
    <button type="button" class="link-btn" data-reset hidden>{M.icon('rotate-ccw')}Start again</button>
  </div>
</div>"""


def page_home():
    by_slug = {p["slug"]: p for p in C.PACKAGES}

    def card(slug, wide=False):
        p = by_slug[slug]
        return svc_card(slug, p["kind"], p["name"], first_sentence(p["summary"]), price(*p["price"]),
                        p["timeline"], wide)

    cards = [card("systems-roadmap", True), card("connection", True), card("store-move"), card("odoo-launch"),
             svc_card("support", "After go-live", C.SUPPORT["name"],
                      f"Prepaid hours for questions, small changes, reports and training. We reply "
                      f"{C.PROMISES['support_reply']}.", "From " + price("support_10h"), "10 or 20 hours")]

    cta = primary_cta("hero")
    if cta:
        hero_cta = (f'<div class="hero-cta">{cta}<a class="more" href="/services">See services and prices'
                    f'{M.icon("arrow-right")}</a></div>'
                    f'<p class="assure">{M.icon("clock")}A {e(C.PROMISES["call_length"])} call at no charge. '
                    f'A proposal or Roadmap quote follows {e(C.PROMISES["proposal_after_call"])}.</p>')
    else:
        hero_cta = '<div class="hero-cta"><a class="btn" href="/services">See services and prices</a></div>'

    proof = [
        ("file-check-2", "Fixed fee in writing", "Scope, exclusions and price are signed before work starts."),
        ("clock", "A reply " + C.PROMISES["first_reply"], f"{C.PROMISES['business_days']}, {C.TIMEZONE_LABEL} time."),
        ("server", "Built in staging first", "Two trial data loads, checked against counts you sign off."),
        ("key-round", "Your accounts stay yours", "Store, database and apps stay in your name and on your billing."),
    ]
    proof_html = "".join(f"<li>{M.icon(ic)}<div><b>{e(h)}</b><span>{e(t)}</span></div></li>" for ic, h, t in proof)
    works = ["Shopify", "Shopify POS", "Odoo 19", "Odoo.sh", "Odoo Online", "QuickBooks Online", "WooCommerce", "Square"]
    works_html = "".join(f"<li>{w}</li>" for w in works)

    problems = [
        ("boxes", "Stock counts that disagree",
         "The website says four, the shelf has one and a spreadsheet says six. Oversold orders and recounts follow.",
         "connection"),
        ("copy", "Orders and refunds typed twice",
         "Someone copies Shopify orders into the accounting system by hand, and refunds are easy to miss at month end.",
         "odoo-launch"),
        ("warehouse", "A second location or a wholesale channel",
         "A setup that worked for one store strains with two stock rooms, transfers between them or wholesale price lists.",
         "systems-roadmap"),
        ("git-branch", "A store platform you have outgrown",
         "WooCommerce, Wix, Square Online or BigCommerce, held together by plugins that nobody wants to update.",
         "store-move"),
    ]
    prob_html = "".join(f"""
<li class="prob reveal" data-i="{i}">
  <span class="prob-art">{M.blob(i)}{M.icon(ic)}</span>
  <h3>{e(h)}</h3><p>{e(t)}</p>
  <a class="more" href="/services#{slug}">{e(by_slug[slug]['name'])}{M.icon('arrow-right')}</a>
</li>""" for i, (ic, h, t, slug) in enumerate(problems))

    steps = [
        ("calendar-check", f"A {C.PROMISES['call_length']} call", "No charge",
         "You describe your setup and what isn't working. If we are not the right fit, we say so on the call."),
        ("map", "A Systems Roadmap", "2–3 weeks",
         "A paid review that ends in a written plan and a fixed quote. You keep the plan whether or not you continue with us."),
        ("list-checks", "A signed scope, then the build", "In staging first",
         "Work starts after the agreement, the statement of work and the deposit are in. Scope changes are priced in writing first."),
        ("package-check", "Go-live and support after it", "A planned date",
         "A backup, the cutover and checks on live orders, then fixes for the support period in your package."),
    ]
    steps_html = "".join(f"""
<li class="reveal" data-i="{i}"><span class="st-ic">{M.icon(ic)}</span><span class="st-meta">{e(meta)}</span>
<h3>{e(h)}</h3><p>{e(t)}</p></li>""" for i, (ic, h, meta, t) in enumerate(steps))

    fit_yes = ["Roughly 5 to 50 people", "Selling on Shopify online, in stores or both",
               "Running Odoo, or moving to it from spreadsheets or QuickBooks",
               "Multi-location retailers, and wholesalers who also sell direct"]
    fit_no = ["Custom theme design", "Shopify Plus or headless storefronts",
              "Odoo for more than 50 users or several companies",
              "Regulated products such as cannabis, alcohol and pharmacy"]
    yes_html = "".join(f"<li>{M.icon('check')}<span>{e(x)}</span></li>" for x in fit_yes)
    no_html = "".join(f"<li>{M.icon('x')}<span>{e(x)}</span></li>" for x in fit_no)

    faqs = [(qn, fn()) for qn, fn in HOME_FAQS]
    faq_html = "".join(f'<details class="qa"><summary><span>{e(qn)}</span>{M.icon("chevron-down")}</summary>'
                       f'<p>{e(a)}</p></details>' for qn, a in faqs)
    mid_cta = primary_cta("mid")
    mid = ""
    if mid_cta:
        mid = (f'<div class="cta-row reveal"><p><b>The first step is a short call.</b> A {e(C.PROMISES["call_length"])} call at no charge, '
               f'in {e(C.TIMEZONE_LABEL)} hours.</p>{mid_cta}</div>')

    body = f"""
<section class="hero hero-dark" data-sec="hero">
  {M.deco('hero-l')}{M.deco('hero-r')}
  <div class="wrap hero-center">
    <p class="eyebrow">Shopify and Odoo consulting</p>
    <h1 class="display">One stock count across your Shopify store, your registers and Odoo</h1>
    <p class="lead">{e(NAME)} sets up Shopify, Shopify POS and Odoo for US retailers and wholesalers, then
    connects them so orders, stock and accounting agree. You get a written scope and a fixed fee before
    any work starts.</p>
    {hero_cta}
  </div>
  <div class="wrap hero-demo" data-sec="demo">
    <p class="demo-intro">Four everyday jobs, shown in a typical setup</p>
    {M.demo_tabs(C.DEMO_VIDEOS)}
    <p class="demo-foot">These screens are drawings of a typical setup with sample data. What syncs, and how
    often, depends on your connector and your Odoo plan.</p>
  </div>
</section>

<section class="proof" aria-label="How we work" data-sec="proof">
  <div class="wrap">
    <ul class="proof-list">{proof_html}</ul>
    <div class="works"><p class="small">Platforms we set up, connect and move data between</p><ul>{works_html}</ul></div>
  </div>
</section>

<section class="section" data-sec="problems">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Why people call</p>
      <h2>Problems this work fixes</h2>
      <p class="lead">Most projects start with one of these four.</p>
    </div>
    <ul class="prob-grid">{prob_html}</ul>
  </div>
</section>

<section class="section alt" id="services" data-sec="services">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Services</p>
      <h2>Services and price ranges</h2>
      <p class="lead">Each project has a fixed fee agreed in writing. The ranges are what most projects of
      each kind cost; your exact fee comes from a scoping call or a Systems Roadmap.</p>
    </div>
    <div class="svc-grid">{''.join(cards)}</div>
    <p class="small">{e(C.LARGER_PROJECTS.format(larger_odoo_from=price("larger_odoo_from")))}
    Shopify, Odoo and app vendors bill you directly for plans and licenses.</p>
  </div>
</section>

<section class="section" id="finder" data-sec="finder">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Where to start</p>
      <h2>Three questions to find the service that fits</h2>
      <p class="lead">Nothing you pick here is sent to us. It only chooses which service to show.</p>
    </div>
    {finder()}
    <noscript><p>See the <a href="/services">services page</a> for what each service includes.</p></noscript>
  </div>
</section>

<section class="section alt" data-sec="deliverables">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">In writing</p>
      <h2>Documents you get on every project</h2>
      <p class="lead">Each stage ends with something written that you can check. These are shortened samples.</p>
    </div>
    <div class="paper-grid">
      <div class="reveal">{M.sample_roadmap()}</div>
      <div class="reveal" data-i="1">{M.sample_fieldmap()}</div>
      <div class="reveal" data-i="2">{M.sample_testlog()}</div>
      <div class="reveal" data-i="3">{M.sample_handover()}</div>
    </div>
  </div>
</section>

<section class="section" data-sec="process">
  <div class="wrap">
    <div class="sec-head reveal"><p class="eyebrow">Process</p><h2>How a project starts and runs</h2></div>
    <ol class="flow">{steps_html}</ol>
    <p><a class="more" href="/how-it-works">See every step of a project{M.icon('arrow-right')}</a></p>
    {mid}
  </div>
</section>

<section class="section alt" data-sec="fit">
  <div class="wrap fit">
    <div class="fit-col reveal">
      <h2>Who we work with</h2>
      <ul class="fit-list yes">{yes_html}</ul>
    </div>
    <div class="fit-col reveal" data-i="1">
      <h2>Work we don't take on</h2>
      <ul class="fit-list no">{no_html}</ul>
      <p class="small">For those, a larger agency or Odoo itself is the better fit.</p>
    </div>
  </div>
</section>

<section class="section" data-sec="faq">
  <div class="wrap faq-wrap">
    <div class="sec-head reveal"><p class="eyebrow">Questions</p><h2>Questions people ask before a call</h2>
    <p class="lead">Pricing and scope questions are answered on the <a href="/services">services page</a>.</p></div>
    <div class="qa-list">{faq_html}</div>
  </div>
</section>
"""
    return {
        "path": "/", "file": "index.html",
        "title": f"Shopify, Shopify POS and Odoo setup | {NAME}",
        "desc": (f"{NAME} sets up Shopify, Shopify POS and Odoo as one system for US retailers and "
                 f"wholesalers. Fixed fees, written scope, remote from {C.STATE}."),
        "body": body, "dark_head": True, "schema": [faq_schema(faqs)],
    }


SERVICE_FAQS = [
    ("Who pays for Shopify, Odoo and connector licenses?",
     "You do, directly to each vendor. Plans, apps, connector licenses and hosting are billed to your "
     "own accounts and listed in your proposal as separate from our fee."),
    ("Why a fixed fee instead of hourly billing?",
     "You know the cost before we start. If you ask for something outside the agreed scope, we send a "
     "written change order with the price before doing it."),
    ("Do you work with Odoo Online, Odoo.sh or on-premise Odoo?",
     "Odoo Online and Odoo.sh. Third-party connector modules can't be installed on Odoo Online, and "
     "connectors that use Odoo's API need its Custom plan, so the Systems Roadmap confirms the right plan "
     "and hosting before you commit."),
    ("Can you start without a Systems Roadmap?",
     "For a Store Move or a Store to Back Office Sync with a clear scope, a scoping call is often "
     "enough. Odoo projects over $20,000 always start with a Roadmap."),
]


def page_services():
    blocks = []
    for p in C.PACKAGES:
        inc = "".join(f"<li>{e(x)}</li>" for x in p["includes"])
        blocks.append(f"""
<section class="pkg reveal" id="{p['slug']}" aria-labelledby="{p['slug']}-h">
  <div class="pkg-head">
    <p class="eyebrow">{e(p['kind'])}</p>
    <h2 id="{p['slug']}-h">{e(p['name'])}</h2>
    {M.MINIS[p['slug']]()}
    <dl class="facts"><div><dt>Price</dt><dd class="price">{price(*p['price'])}</dd></div>
    <div><dt>Typical timeline</dt><dd>{e(p['timeline'])}</dd></div></dl>
  </div>
  <div class="pkg-body">
    <p class="lead">{e(p['summary'])}</p>
    <h3>What's included</h3><ul class="ticks">{inc}</ul>
    <h3>Not included</h3><p>{e(p['excludes'])}</p>
    <h3>Payment</h3><p>{e(p['payment'])}</p>
  </div>
</section>""")
    s = C.SUPPORT
    opts = "".join(f'<div><dt>{e(h)}</dt><dd><span class="price">{price(k)}</span> {e(v)}</dd></div>'
                   for h, k, v in s["options"])
    blocks.append(f"""
<section class="pkg reveal" id="support" aria-labelledby="support-h">
  <div class="pkg-head">
    <p class="eyebrow">Prepaid hours</p>
    <h2 id="support-h">{e(s['name'])}</h2>
    {M.MINIS['support']()}
    <dl class="facts">{opts}</dl>
  </div>
  <div class="pkg-body">
    <p class="lead">{e(s['summary'])}</p>
    <p>We reply {e(C.PROMISES['support_reply'])}, {e(C.PROMISES['business_days'])}, {e(C.TIMEZONE_LABEL)} time.</p>
    <p>{e(s['terms'])}</p>
  </div>
</section>""")
    faqs = "".join(f'<details class="qa"><summary><span>{e(q)}</span>{M.icon("chevron-down")}</summary>'
                   f'<p>{e(a)}</p></details>' for q, a in SERVICE_FAQS)
    body = f"""
<section class="hero slim"><div class="wrap">
  <p class="eyebrow">Services</p>
  <h1>Shopify and Odoo services with fixed fees</h1>
  <p class="lead">Five things we sell, each with a written scope. The ranges are what most projects of
  each kind cost; your exact fee comes from a scoping call or a Systems Roadmap and is written into
  your statement of work.</p>
</div></section>
<div class="wrap">{''.join(blocks)}
<section class="section-tight">
  <h2>Larger Odoo projects</h2>
  <p>{e(C.LARGER_PROJECTS.format(larger_odoo_from=price("larger_odoo_from")))}</p>
</section>
<section class="section-tight">
  <h2>What you pay Shopify, Odoo and app vendors</h2>
  <p>Your Shopify plan, POS Pro, theme and apps, your Odoo subscription and any Odoo.sh hosting,
  connector licenses, card processing and hardware are billed to you directly by each vendor. None of
  it is part of our fee, and each item is listed in your proposal.</p>
  <p>{e(C.REFERRAL_DISCLOSURE.format(name=NAME))}</p>
  <p>{e(C.SALES_TAX_LINE)}</p>
</section>
<section class="section-tight faq">
  <h2>Questions about pricing and scope</h2>
  <div class="qa-list">{faqs}</div>
</section>
</div>"""
    return {
        "path": "/services", "file": "services.html",
        "title": f"Shopify and Odoo services and prices | {NAME}",
        "desc": ("Fixed-fee Shopify store moves, Odoo rollouts for 5 to 15 users, Shopify and Odoo "
                 "connections and prepaid support. Price ranges and scope for each."),
        "body": body, "schema": [faq_schema(SERVICE_FAQS)],
    }


STEPS = [
    ("Scoping call", C.PROMISES["call_length"] + " call",
     f"We go through what you sell, your channels, your current systems and your timeline. You get a "
     f"proposal or a Roadmap quote {C.PROMISES['proposal_after_call']}."),
    ("Systems Roadmap", "2–3 weeks",
     "Up to three working sessions, then a written plan: what fits standard Shopify and Odoo, which "
     "connector and plan to use, what data moves, the risks, and a fixed fee for the next phase."),
    ("Agreement and deposit", "before any work",
     "You sign a services agreement once, then a statement of work for each project with scope, "
     "exclusions, milestones and price. Work starts when the deposit clears."),
    ("Access, the safe way", "week 1",
     "We ask for named staff or collaborator accounts with only the permissions the work needs, with "
     "two-factor sign-in. Never shared passwords, and never by email or chat."),
    ("Build in staging", "most of the project",
     "Configuration and data loads happen in a staging copy or trial database first, with two trial "
     "data loads checked against record counts and totals that you sign off."),
    ("Testing with your team", "1–2 weeks",
     "Your staff run real scenarios against written acceptance criteria: an order, a refund, a "
     "partial shipment, a POS sale, a purchase receipt. Training is recorded."),
    ("Go-live", "a planned date",
     "A backup first, a short freeze on changes, the cutover, then checks on live orders. Go-live dates "
     "avoid your peak season."),
    ("After go-live", "2–4 weeks",
     "Fixes for anything that doesn't work as agreed, at no extra cost, for the period in your "
     "package. A support block covers changes after that."),
    ("Handover and access removed", "project close",
     "You get the as-built record, guides and an access register. We remove our access and confirm it "
     "in writing."),
]


def page_how():
    items = "".join(f'<li class="reveal"><div class="step-meta">{e(t)}</div><div><h2 class="h3">{e(h)}</h2>'
                    f'<p>{e(d)}</p></div></li>' for h, t, d in STEPS)
    body = f"""
<section class="hero slim"><div class="wrap">
  <p class="eyebrow">How a project works</p>
  <h1>How a Shopify or Odoo project runs, from first call to handover</h1>
  <p class="lead">The same steps for every project, whatever its size. Each one ends with something you
  can check before the next begins.</p>
</div></section>
<div class="wrap"><ol class="timeline draw">{items}</ol>
<section class="section-tight">
  <h2>Changes to scope</h2>
  <p>If you need something that isn't in your statement of work, we stop that part, send a written
  change order with the price and the effect on dates, and start it once you sign.</p>
</section>
<section class="section-tight">
  <h2>Your data and accounts</h2>
  <p>Your Shopify store, Odoo database and app accounts stay in your name and on your billing. We work
  read-only until the statement of work calls for changes. Tax and accounting settings follow written
  instructions from your accountant.</p>
</section></div>"""
    return {
        "path": "/how-it-works", "file": "how-it-works.html",
        "title": f"How a Shopify or Odoo project works | {NAME}",
        "desc": ("The steps of every project: a scoping call, a Systems Roadmap, a signed scope, a "
                 "staging build, testing with your team, go-live, support and access removed."),
        "body": body,
    }


def page_about():
    bio = "".join(f"<p>{e(p)}</p>" for p in C.ABOUT_BIO)
    if not bio:
        NOTES.append("ABOUT_BIO blank: the About page shows only the business facts")
    creds = ""
    if C.ABOUT_CREDENTIALS:
        creds = ("<h2>Current certifications</h2><ul>" +
                 "".join(f"<li>{e(n)}, {e(y)}</li>" for n, y in C.ABOUT_CREDENTIALS) + "</ul>")
    photo = ""
    if C.PHOTO:
        photo = f'<img class="portrait" src="/{e(C.PHOTO)}" alt="{e(C.FOUNDER)}" width="320" height="400">'
    body = f"""
<section class="hero slim"><div class="wrap">
  <p class="eyebrow">About</p>
  <h1>About {e(NAME)} and {e(C.FOUNDER)}</h1>
</div></section>
<div class="wrap two about">
  <div>
    {f'<h2>{e(C.FOUNDER)}</h2>{bio}' if bio else ''}
    {creds}
    <h2>How {e(NAME)} works</h2>
    <p>{e(NAME)} is a {e(C.STATE)} business. All work is remote, for businesses anywhere in the US,
    during {e(C.TIMEZONE_LABEL)} business hours.</p>
    <p>{e(C.FOUNDER)} scopes every project, writes the statement of work and is your contact from the
    first call to handover.</p>
    <p>We sell services only. Software, apps and hosting are billed to you by each vendor, so your
    accounts stay yours.</p>
  </div>
  {photo}
</div>"""
    return {
        "path": "/about", "file": "about.html",
        "title": f"About {NAME}",
        "desc": (f"{NAME} is a remote Shopify and Odoo consultancy run by {C.FOUNDER} from {C.STATE}, "
                 f"working with businesses across the US."),
        "body": body,
    }


def page_book():
    cta = primary_cta("book")
    contact = ""
    if cta:
        contact = f'<div class="book-cta">{cta}<p class="small">{secondary_contacts()}</p></div>'
    body = f"""
<section class="hero slim"><div class="wrap">
  <p class="eyebrow">Book a call</p>
  <h1>Book a scoping call about your Shopify or Odoo setup</h1>
  <p class="lead">A {e(C.PROMISES['call_length'])} video call, {e(C.PROMISES['business_days'])},
  {e(C.TIMEZONE_LABEL)} time. There is no charge for the call.</p>
  {contact}
</div></section>
<div class="wrap two">
  <section><h2>What we cover on the call</h2>
  <ul class="ticks">
    <li>What you sell and where: online, in stores, wholesale</li>
    <li>What runs your stock, orders and books today</li>
    <li>What isn't working, and what has to be live by when</li>
    <li>Which service fits, or whether a Systems Roadmap should come first</li>
  </ul></section>
  <section><h2>What happens after</h2>
  <p>You get a proposal or a Roadmap quote {e(C.PROMISES['proposal_after_call'])}. If we are not the
  right fit, we tell you on the call and, where we can, suggest who is.</p>
  <p>Messages get a reply {e(C.PROMISES['first_reply'])}.</p>
  <p>Please don't send passwords, API keys or customer data before or during the call. If a project
  goes ahead, access is set up the safe way in week one.</p></section>
</div>"""
    return {
        "path": "/book", "file": "book.html",
        "title": f"Book a Shopify and Odoo scoping call | {NAME}",
        "desc": (f"Book a {C.PROMISES['call_length']} call about your Shopify, Shopify POS or Odoo setup. "
                 f"You get a proposal or Roadmap quote {C.PROMISES['proposal_after_call']}."),
        "body": body, "no_band": True,
    }


def page_privacy():
    contact = (f'<a href="mailto:{e(C.EMAIL)}">{e(C.EMAIL)}</a>' if C.EMAIL
               else "the email address on our Book a call page")
    cf = ""
    if C.CF_WEB_ANALYTICS_TOKEN:
        cf = ("<h3>Cloudflare Web Analytics</h3><p>We also use Cloudflare Web Analytics, which counts "
              "page views without cookies and without storing your IP address.</p>")
    booking = ("<h3>Booking</h3><p>When you book a call, the booking tool records your name, email, "
               "company and the time you chose, and adds them to our customer records.</p>"
               if C.BOOKING_URL else "")
    body = f"""
<section class="hero slim"><div class="wrap">
  <p class="eyebrow">Privacy</p>
  <h1>Privacy policy</h1>
  <p class="small">{e(C.LEGAL_LINE)}.</p>
</div></section>
<div class="wrap prose">
<h2>What this site collects</h2>
<h3>Our visit counter</h3>
<p>This site has its own visit counter, run on Cloudflare, our web host. It records the page viewed,
the page you landed on, the website that sent you (its domain only), any campaign tags in the link,
whether you have visited before, your country and region as Cloudflare estimates them, the name of the
network you connect through (for example your internet provider), your device type and browser, how far
down a page you scrolled and which sections came into view, clicks on the workflow demo and the service
finder, and taps on our booking, email or phone links.</p>
<p>To tell new visits from returning ones it sets one first-party cookie holding a random ID. The cookie
cannot be read by scripts on the page, is not shared with anyone, and expires after one year. The counter
does not store your IP address, name, email address or anything you type.</p>
{cf}
{booking}
<h3>Messages you send</h3>
<p>If you email us or book a call, we keep your message and contact details in our email and customer
records so we can reply and keep a record of the work. We do not sell or rent them, and we do not use
them for advertising.</p>
<h3>What this site does not use</h3>
<p>No advertising pixels, no session recording, no visitor-identification services, and no third-party
fonts or embeds.</p>

<h2 id="opt-out">Turning off the visit counter</h2>
<p>Use the button below to stop this browser from being counted. It replaces the counter cookie with an
opt-out cookie. If your browser sends a Global Privacy Control signal, we treat that as an opt-out too.</p>
<p><button type="button" class="btn-secondary" id="optout">Stop counting my visits</button>
<span class="small" id="optout-status" role="status"></span></p>

<h2>How long we keep it</h2>
<p>Visit counter data is kept for up to three months by Cloudflare and then deleted. Messages and project
records are kept for as long as we need them for the work and for tax and legal records.</p>

<h2>Your choices</h2>
<p>You can ask what we hold about you, ask us to correct it, or ask us to delete it, by writing to
{contact}. We reply within 30 days.</p>
</div>"""
    return {
        "path": "/privacy", "file": "privacy.html",
        "title": f"Privacy policy | {NAME}",
        "desc": ("What this site records, the one first-party cookie it sets, how to turn the visit "
                 "counter off, and how we handle messages you send us."),
        "body": body,
    }


def page_terms():
    body = f"""
<section class="hero slim"><div class="wrap">
  <p class="eyebrow">Terms</p>
  <h1>Website terms of use</h1>
  <p class="small">{e(C.LEGAL_LINE)}.</p>
</div></section>
<div class="wrap prose">
<h2>Information on this site</h2>
<p>The pages on this site describe our services in general terms. Price ranges and timelines are typical
figures, not a quote or an offer. A project is agreed only through a signed services agreement and a
signed statement of work, and those documents govern the work.</p>
<p>Guides and articles are general information about Shopify and Odoo, checked on the date shown. They
are not legal, tax or accounting advice; settings that affect tax or accounts should be confirmed with
your own accountant.</p>
<h2>Trademarks and links</h2>
<p>Shopify is a trademark of Shopify Inc. Odoo is a trademark of Odoo S.A. Other product names belong to
their owners. Links to other sites are provided for convenience; we are not responsible for their content.</p>
<p>{e(C.REFERRAL_DISCLOSURE.format(name=NAME))}</p>
<h2>Using this site</h2>
<p>You may read, link to and share these pages. Please don't copy the site's text or designs for
commercial use, or try to disrupt or probe the site.</p>
<h2>Liability</h2>
<p>This site is provided as it is. To the extent the law allows, {e(C.LEGAL_NAME)} is not liable for loss
arising from use of the general information here.</p>
<h2>Governing law</h2>
<p>These terms are governed by the laws of the State of New York.</p>
</div>"""
    return {
        "path": "/terms", "file": "terms.html",
        "title": f"Website terms of use | {NAME}",
        "desc": ("Terms for using this website. Prices shown are typical ranges; projects are governed "
                 "by a signed services agreement and statement of work."),
        "body": body,
    }


def page_sitemap(pages):
    items = "".join(f'<li><a href="{p["path"]}">{e(p["h"])}</a></li>' for p in pages)
    svc = "".join(f'<li><a href="/services#{p["slug"]}">{e(p["name"])}</a></li>' for p in C.PACKAGES)
    body = f"""
<section class="hero slim"><div class="wrap">
  <p class="eyebrow">Site map</p><h1>Site map</h1>
</div></section>
<div class="wrap prose"><ul>{items}</ul><h2>Services</h2><ul>{svc}
<li><a href="/services#support">Support block</a></li></ul></div>"""
    return {
        "path": "/site-map", "file": "site-map.html",
        "title": f"Site map | {NAME}",
        "desc": f"Every page on the {NAME} website, with links to each service.",
        "body": body,
    }


def page_404():
    body = """
<section class="hero slim"><div class="wrap">
  <p class="eyebrow">Page not found</p>
  <h1>This page doesn't exist</h1>
  <p class="lead">The link may be old or mistyped. Try the <a href="/services">services page</a>,
  <a href="/how-it-works">how a project works</a> or the <a href="/site-map">site map</a>.</p>
</div></section>"""
    return {"path": "/404", "file": "404.html", "title": f"Page not found | {NAME}",
            "desc": "The page you asked for does not exist on this site.", "body": body,
            "index": False, "no_band": True}


# ---------------------------------------------------------------------------
# Site files
# ---------------------------------------------------------------------------

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
"""

# Staging (any build without --release) must never be indexed, wherever it is hosted.
STAGING_HEADERS = """
/*
  X-Robots-Tag: noindex, nofollow
"""

# 301s for any URL that changes. Format: "/old /new 301"
REDIRECTS = [
    "/index /  301",
    "/home / 301",
    "/sitemap /site-map 301",
    "/contact /book 301",
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
        lm = C.LAST_CHANGED.get(p["path"])
        urls.append(f"  <url><loc>{clean_url(p['path'])}</loc>" +
                    (f"<lastmod>{lm}</lastmod>" if lm else "") + "</url>")
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    svc = "\n".join(
        f"- [{p['name']}]({SITE}/services#{p['slug']}): {price(*p['price'])}, typically {p['timeline']}. "
        f"{p['summary']}" for p in C.PACKAGES)
    sup = "; ".join(f"{h} {price(k)}, {v}" for h, k, v in C.SUPPORT["options"])
    contact = []
    if C.EMAIL:
        contact.append(f"- Email: {C.EMAIL}")
    if C.BOOKING_URL:
        contact.append(f"- Book a call: {C.BOOKING_URL}")
    llms = f"""# {NAME}

> Remote Shopify and Odoo consulting for small and mid-size US businesses. {NAME} is run from {C.STATE} and serves clients across the US. Every project has a fixed fee and a written scope.

## Services
{svc}
- [Support block]({SITE}/services#support): {sup}.
- Larger Odoo projects: {C.LARGER_PROJECTS.format(larger_odoo_from=price("larger_odoo_from"))}

## How we work
- [How a project works]({SITE}/how-it-works)
- Clients pay Shopify, Odoo and app vendors directly; our fees are for services only.
- {C.REFERRAL_DISCLOSURE.format(name=NAME)}

## Pages
""" + "\n".join(f"- [{p['h']}]({clean_url(p['path'])})" for p in indexable) + "\n"
    if contact:
        llms += "\n## Contact\n" + "\n".join(contact) + "\n"
    (DIST / "llms.txt").write_text(llms)
    key = C.INDEXNOW_KEY
    if not re.fullmatch(r"[A-Za-z0-9-]{8,128}", key or ""):
        ERRORS.append("INDEXNOW_KEY must be 8 to 128 letters, digits or dashes")
    else:
        (DIST / f"{key}.txt").write_text(key)
    (DIST / "favicon.svg").write_text(FAVICON)
    (DIST / "site.webmanifest").write_text(json.dumps({
        "name": NAME, "short_name": NAME, "start_url": "/", "display": "browser",
        "background_color": "#f5f6f8", "theme_color": "#141c2b",
        "icons": [{"src": "/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=1))


# ---------------------------------------------------------------------------
# Checks: NO AI LOOK tells and leaks in the built output
# ---------------------------------------------------------------------------

BANNED = ["transform", "elevate", "seamless", "unlock", "leverage", "empower", "game-changer",
          "revolutionary", "streamline your operations", "fast-paced", "end-to-end solution",
          "digital transformation", "synergy", "robust", "cutting-edge", "curated", "effortless"]


def check_output(path, text):
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
    if re.search(r"555[-. ]\d{4}", text):
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

    pages = [page_home(), page_services(), page_how(), page_about(), page_book(),
             page_privacy(), page_terms()]
    heads = {"/": "Home", "/services": "Services and prices", "/how-it-works": "How a project works",
             "/about": "About", "/book": "Book a call", "/privacy": "Privacy policy",
             "/terms": "Website terms of use", "/site-map": "Site map"}
    for p in pages:
        p["h"] = heads[p["path"]]
    sm = page_sitemap(pages)
    sm["h"] = heads["/site-map"]
    pages.append(sm)
    pages.append(page_404())

    for p in pages:
        out = layout(p, assets)
        check_output(p["file"], out)
        (DIST / p["file"]).write_text(out)

    indexable = [p for p in pages if p.get("index", True)]
    write_site_files(indexable)

    for n in NOTES:
        print("NOTE:", n)
    if ERRORS:
        for x in ERRORS:
            print("ERROR:", x, file=sys.stderr)
        print(f"Build failed with {len(ERRORS)} error(s).", file=sys.stderr)
        sys.exit(1)
    print(f"Built {len(indexable)} indexable pages{' (release)' if RELEASE else ' (staging: noindex, not for launch)'}")


if __name__ == "__main__":
    main()
