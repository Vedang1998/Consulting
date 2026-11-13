"""Resource pages (v5): one hub, the guides, one recordings page, one questions page and the glossary.
Plus the legal pages and the 404. Text lives in content.py; shared parts in kit.py.
"""

import re

from kit import (C, moved, NAME, ERRORS, RELEASE, SITE, SVC_COLOR, SVC_SPOT, anchor, clip, clip_info, crumbs, e,  # noqa: F401
                 faq_schema, fill, first_sentence, icon, inline, md, nice_date, primary_cta, hero_art, qa_list,
                 sec_head, spot, svc_href, svc_name, svc_price)
import content as R
from pages import hero

PLATFORMS = {"shopify": "Shopify", "odoo": "Odoo", "both": "Shopify and Odoo"}
GUIDE_BY = {g["slug"]: g for g in R.GUIDES}
HUB_PATHS = ("/resources", "/guides", "/videos", "/faq", "/glossary")
VIDEO_GROUPS = [("Orders and payments", ["sale", "pricelist", "pos", "invoice", "return"]),
                ("Stock and purchasing", ["purchase", "landed", "lots", "locations", "count", "reports"])]


def guides_live():
    return [g for g in R.GUIDES if not RELEASE or g["status"] == "approved"]


def live_href(href):
    """None for a link to a page this build leaves out (draft guides on a release build, retired pages)."""
    if not href:
        return None
    if href.startswith("/guides/") and GUIDE_BY.get(href.split("/")[2]) not in guides_live():
        return None
    return moved(href)


def ptag(platform):
    return f'<span class="ptag p-{platform}">{e(PLATFORMS[platform])}</span>'


def guide_card(g):
    text = first_sentence(fill(g["short"]))
    if len(text.split()) < 8:
        text = ". ".join(fill(g["short"]).split(". ")[:2]).rstrip(".") + "."
    return (f'<!--reuse--><li data-platform="{g["platform"]}"><a class="gcard" href="/guides/{g["slug"]}">'
            f'<span class="gc-top">{ptag(g["platform"])}<span class="gc-date">Checked {nice_date(g["checked"])}</span></span>'
            f'<b>{e(g["title"])}</b><span class="gc-text">{e(text)}</span>'
            f'<em>Read the guide{icon("arrow-right")}</em></a></li><!--/reuse-->')


def chips(target):
    opts = [("all", "Everything"), ("shopify", "Shopify"), ("odoo", "Odoo"), ("both", "Both together")]
    btns = "".join(f'<button type="button" class="chip-btn" data-filter="{v}" '
                   f'aria-pressed="{"true" if v == "all" else "false"}">{e(t)}</button>' for v, t in opts)
    return (f'<div class="chips" role="group" aria-label="Show guides for" data-chips="{target}" hidden>'
            f'<span class="chips-l">Show</span>{btns}</div>')


def page_resources():
    _, crs = crumbs([("Resources", "/resources")])
    cards = "".join(guide_card(g) for g in guides_live())
    n_faq = sum(len(x[5]) for x in R.FAQ_PAGES)
    n_clip = sum(1 for k in C.CLIPS if clip_info(k))
    doors = [("/videos", "videos", "Recordings", f"{n_clip} short recordings of real screens with sample data."),
             ("/faq", "questions", "Questions", f"{n_faq} short answers on Shopify, Odoo and working with us."),
             ("/glossary", "glossary", "Glossary", f"{len(R.GLOSSARY)} Shopify and Odoo terms in plain words.")]
    door_html = "".join(f'<a class="door" href="{h}"><span class="ic-block">{spot(ic)}</span><span><b>{e(t)}</b>'
                        f'<span>{e(x)}</span></span>{icon("arrow-right")}</a>' for h, ic, t, x in doors)
    body = hero("Guides and answers on Shopify, Odoo and running both",
                "Long answers to the questions owners ask before they buy a plan, a connector or a setup. Vendor "
                "prices and limits carry the date we checked them on the vendor's own page.", eyebrow="Resources") + f"""
<section class="sec" aria-labelledby="g-h"><div class="wrap">
  {sec_head("Guides", "", "g-h")}
  {chips("guides")}
  <ul class="gcards" data-filter-list="guides">{cards}</ul>
</div></section>
<section class="sec tint"><div class="wrap"><!--reuse--><div class="doors">{door_html}</div><!--/reuse--></div></section>"""
    return {"path": "/resources", "file": "resources.html", "h": "Resources",
            "title": f"Shopify and Odoo guides and answers | {NAME}",
            "desc": (f"Guides, screen recordings and short answers about Shopify, Odoo and connecting them, from "
                     f"{NAME}. Vendor prices carry the date they were checked."),
            "body": body, "schema": [crs]}


def guide_side(g):
    svc = "".join(f'<a class="svc-mini {SVC_COLOR[s]}" href="{svc_href(s)}"><span class="ic-block">{spot(SVC_SPOT[s])}</span>'
                  f'<span><b>{e(svc_name(s))}</b><em class="price">{svc_price(s)}</em></span>{icon("arrow-right")}</a>'
                  for s in g["services"])
    toc = "".join(f'<li><a href="#{anchor(h)}">{e(h)}</a></li>' for h in re.findall(r"^## (.+)$", g["body"], re.M))
    return f"""<!--reuse-->
<aside class="g-side">
  <div class="g-box"><p class="g-label">In this guide</p><ol class="g-toc">{toc}<li><a href="#questions">Questions</a></li>
  <li><a href="#sources">Sources</a></li></ol></div>
  <div class="g-box"><p class="g-label">Where we can help</p><div class="svc-minis">{svc}</div>
  <div class="g-cta">{primary_cta("guide")}</div></div>
</aside><!--/reuse-->"""


def page_guide(g):
    path = f"/guides/{g['slug']}"
    trail, crs = crumbs([("Resources", "/resources"), (g["seo_title"], path)])
    if not re.search(r"^## When the other option wins", g["body"], re.M):
        ERRORS.append(f"guide {g['slug']} has no 'When the other option wins' section")
    words = len(fill(g["short"]).split())
    if not 40 <= words <= 60:
        ERRORS.append(f"guide {g['slug']}: summary is {words} words, needs 40 to 60")
    if re.search(r"\$\d", g["body"] + g["short"]) and not (g.get("checked") and all(len(s) == 3 and s[2] for s in g["sources"])):
        ERRORS.append(f"guide {g['slug']} shows prices without a checked date on it and every source")
    draft = ""
    if g["status"] != "approved":
        draft = (f'<p class="note-box">{icon("triangle-alert")}<span>Draft for review. Draft guides are left out of the '
                 f'launch build until they are approved.</span></p>')
    srcs = "".join(f'<li><a href="{e(u)}" rel="noopener">{e(t)}</a><span>checked {nice_date(d)}</span></li>'
                   for t, u, d in g["sources"])
    related = "".join(guide_card(GUIDE_BY[s]) for s in g["related"] if GUIDE_BY[s] in guides_live())
    faqs = [(q, fill(a)) for q, a in g["faqs"]]
    body = f"""
<section class="ghero"><div class="wrap"><div class="g-head">
  {trail}
  <p class="eyebrow">{ptag(g['platform'])}Guide</p>
  <h1>{e(g['title'])}</h1>
  <!--reuse--><p class="byline">Written by {e(C.FOUNDER)}, {e(NAME)}.
  <span>Checked <time datetime="{g['checked']}">{nice_date(g['checked'])}</time></span></p>
  {draft}<!--/reuse-->
  <p class="summary">{inline(g['short'])}</p>
</div></div></section>
<div class="wrap g-grid">
  <article class="prose g-body">
    {md(g["body"])}
    <h2 id="questions">Questions</h2>
    {qa_list(faqs)}
    <h2 id="sources">Sources</h2>
    <!--reuse--><ul class="sources">{srcs}</ul>
    <p class="small">{e(C.REFERRAL_DISCLOSURE.format(name=NAME))}</p><!--/reuse-->
  </article>
  {guide_side(g)}
</div>
{f'''<section class="sec tint"><div class="wrap">
  {sec_head("Related guides")}
  <ul class="gcards">{related}</ul>
</div></section>''' if related else ''}"""
    art = {"@context": "https://schema.org", "@type": "Article", "@id": SITE + path + "#article",
           "headline": g["title"], "description": g["desc"], "dateModified": g["checked"],
           "author": {"@type": "Person", "name": C.FOUNDER}, "publisher": {"@id": SITE + "/#org"},
           "mainEntityOfPage": SITE + path, "inLanguage": "en-US"}
    return {"path": path, "file": f"guides/{g['slug']}.html", "h": g["seo_title"], "lastmod": g["checked"],
            "title": f"{g['seo_title']} | {NAME}", "desc": g["desc"], "body": body,
            "schema": [art, crs, faq_schema(faqs)], "kind": "guide", "band": "Ask about your setup on a call"}


def page_videos():
    _, crs = crumbs([("Resources", "/resources"), ("Recordings", "/videos")])
    secs, objs = [], []
    groups = list(VIDEO_GROUPS)
    shop = [k for k in C.CLIPS if C.CLIPS[k][0] == "shopify"]
    if shop:
        groups.insert(0, ("Shopify", shop))
    for n, (h2, keys) in enumerate(groups):
        keys = [k for k in keys if clip_info(k)]
        if not keys:
            continue
        secs.append(f"""
<section class="sec{' tint' if n % 2 else ''}" aria-labelledby="v-{anchor(h2)}"><div class="wrap">
  {sec_head(h2, "", "v-" + anchor(h2))}
  <!--reuse--><div class="clips2">{''.join(clip(k) for k in keys)}</div><!--/reuse-->
</div></section>""")
        for k in keys:
            c = clip_info(k)
            objs.append({"@context": "https://schema.org", "@type": "VideoObject", "@id": f"{SITE}/videos#{k}",
                         "name": c["title"], "description": c["desc"] + (" Real Shopify admin screens shown step by step, with sample data."
                                                          if c["platform"] == "shopify" else
                                                          " Silent recording with sample data."),
                         "thumbnailUrl": [f"{SITE}/{c['stem']}-poster.jpg"], "uploadDate": c["recorded"],
                         "duration": f"PT{max(1, round(c['seconds']))}S", "contentUrl": f"{SITE}/{c['stem']}.mp4",
                         "publisher": {"@id": SITE + "/#org"}})
    body = hero("Short clips of real Shopify and Odoo screens",
                "Each clip starts on the task it names and stops when the task is done. The Odoo clips are screen "
                "recordings. The Shopify clips are real admin screens shown one step at a time, with a drawn pointer "
                "on each click. All are silent and made in our own demo systems with sample data, never a client's.",
                eyebrow="Recordings") + "".join(secs)
    return {"path": "/videos", "file": "videos.html", "h": "Recordings",
            "title": f"Shopify and Odoo screen recordings | {NAME}",
            "desc": ("Short, silent clips of real Shopify and Odoo screens with sample data. Orders, returns, stock "
                     "counts, purchase orders, a register sale, a paid invoice and reports."),
            "body": body, "schema": [crs] + objs}


def page_faq():
    _, crs = crumbs([("Resources", "/resources"), ("Questions", "/faq")])
    jump, groups, allq = [], [], []
    for slug, label_, platform, h1, lead, lst in R.FAQ_PAGES:
        jump.append(f'<a href="#{slug}">{e(label_)}</a>')
        more = {q: (live_href(href), fill(txt)) for q, a, href, txt in lst if href and txt}
        items = [(q, fill(a)) for q, a, _, _ in lst]
        allq += items
        groups.append(f'<section class="faq-group" id="{slug}" aria-labelledby="fg-{slug}">'
                      f'<h2 id="fg-{slug}">{e(h1)}</h2><p class="lead">{e(lead)}</p>{qa_list(items, more)}</section>')
    body = hero("Short answers about Shopify, Odoo and working with us",
                "A few sentences each, with a link to the guide or service page that goes further.",
                eyebrow="Questions", extra=f'<nav class="jump" aria-label="Jump to a group">{"".join(jump)}</nav>') + f"""
<section class="sec"><div class="wrap narrow">{''.join(groups)}</div></section>"""
    return {"path": "/faq", "file": "faq.html", "h": "Questions",
            "title": f"Shopify and Odoo questions answered | {NAME}",
            "desc": (f"Short answers about Shopify plans and POS, Odoo hosting and plans, connecting the two, and how "
                     f"{NAME} works with clients."),
            "body": body, "schema": [crs, faq_schema(allq)]}


def page_glossary():
    path = "/glossary"
    trail, crs = crumbs([("Resources", "/resources"), ("Glossary", path)])
    terms = sorted(R.GLOSSARY, key=lambda t: t[0].lower())
    letters = sorted({t[0][0].upper() for t in terms})
    jump = "".join(f'<a href="#letter-{c}">{c}</a>' for c in letters)
    rows, cur = [], ""
    for term, text, href, ltxt in terms:
        c = term[0].upper()
        if c != cur:
            if cur:
                rows.append("</dl></div>")
            rows.append(f'<div class="gl-group" id="letter-{c}"><h2 class="gl-letter">{c}</h2><dl class="gl-list">')
            cur = c
        link = live_href(href)
        mo = f' <a class="more" href="{link}">{e(ltxt)}{icon("arrow-right")}</a>' if link else ""
        rows.append(f'<div class="gl-item" id="{anchor(term)}"><dt>{e(term)}</dt><dd>{e(fill(text))}{mo}</dd></div>')
    rows.append("</dl></div>")
    schema = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Shopify and Odoo glossary",
              "url": SITE + path, "hasDefinedTerm": [
                  {"@type": "DefinedTerm", "name": t, "description": fill(x), "url": f"{SITE}{path}#{anchor(t)}"}
                  for t, x, _, _ in terms]}
    body = hero("Shopify and Odoo terms in plain words",
                f"{len(terms)} terms that come up in our guides and on calls, each with a link to the page that uses it.",
                trail=trail, eyebrow="Glossary") + f"""
<section class="sec"><div class="wrap narrow">
  <nav class="gl-jump" aria-label="Jump to a letter">{jump}</nav>
  {''.join(rows)}
</div></section>"""
    return {"path": path, "file": "glossary.html", "h": "Glossary",
            "title": f"Shopify and Odoo glossary in plain words | {NAME}",
            "desc": ("Plain definitions of Shopify and Odoo terms: SKU, on hand, landed cost, Odoo.sh, the Custom "
                     "plan, POS Pro, cutover, reconciliation and more."),
            "body": body, "schema": [crs, schema]}


def page_404():
    body = hero("This page doesn't exist",
                'The link may be old or mistyped. Try the <a href="/services">services</a>, the '
                '<a href="/industries">industry pages</a> or the <a href="/resources">guides</a>.',
                eyebrow="Page not found", art=hero_art("notfound"))
    return {"path": "/404", "file": "404.html", "title": f"Page not found | {NAME}",
            "desc": "The page you asked for does not exist on this site.", "body": body,
            "index": False, "no_band": True}


def legal_head(eyebrow, h1):
    return (f'<section class="hero slim"><div class="wrap"><p class="eyebrow">{e(eyebrow)}</p><h1>{e(h1)}</h1>'
            f'<p class="small">{e(C.LEGAL_LINE)}.</p></div></section>')


def res_pages():
    pages = [page_resources()] + [page_guide(g) for g in guides_live()]
    pages += [page_videos(), page_faq(), page_glossary()]
    return pages


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
{legal_head("Privacy", "Privacy policy")}
<div class="wrap prose legal">
<h2>What this site collects</h2>
<h3>Our visit counter</h3>
<p>This site has its own visit counter, run on Cloudflare, our web host. It records the page viewed,
the page you landed on, the website that sent you (its domain only), any campaign tags in the link,
whether you have visited before, your country and region as Cloudflare estimates them, the name of the
network you connect through (for example your internet provider), your device type and browser, how far
down a page you scrolled and which sections came into view, clicks on the interactive
tools on our service pages (including which result a tool showed, never your answers), and taps on our
booking, email or phone links.</p>
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
<p><button type="button" class="btn-ghost" id="optout">Stop counting my visits</button>
<span class="small" id="optout-status" role="status"></span></p>

<h2>How long we keep it</h2>
<p>Visit counter data is kept for up to three months by Cloudflare and then deleted. Messages and project
records are kept for as long as we need them for the work and for tax and legal records.</p>

<h2>Your choices</h2>
<p>You can ask what we hold about you, ask us to correct it, or ask us to delete it, by writing to
{contact}. We reply within 30 days.</p>
</div>"""
    return {
        "path": "/privacy", "file": "privacy.html", "no_band": True,
        "title": f"Privacy policy | {NAME}", "h": "Privacy policy",
        "desc": ("What this site records, the one first-party cookie it sets, how to turn the visit "
                 "counter off, and how we handle messages you send us."),
        "body": body,
    }


def page_terms():
    body = f"""
{legal_head("Terms", "Website terms of use")}
<div class="wrap prose legal">
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
        "path": "/terms", "file": "terms.html", "no_band": True,
        "title": f"Website terms of use | {NAME}", "h": "Website terms of use",
        "desc": ("Terms for using this website. Prices shown are typical ranges; projects are governed "
                 "by a signed services agreement and statement of work."),
        "body": body,
    }


def legal_pages():
    return [page_privacy(), page_terms()]
