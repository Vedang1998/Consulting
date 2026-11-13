"""Core pages (v5): home, services, industries, how we work, pricing, about and book.

Every page returns a dict for build.layout(): path, file, title, desc, body, and optional schema, band (the booking
card heading), no_band and index. Shared parts live in kit.py. Resource and legal pages are in pages_res.py.
"""

import json

import industries as I
from kit import (C, M, NAME, NOTES, ORDER, PKG, SVC_COLOR, SVC_SPOT, clip, crumbs, e,  # noqa: F401
                 faq_schema, facts, icon, ind_tile, more_link, price, primary_cta, qa_list,
                 sec_head, secondary_contacts, service_schema, spot, stack, svc_href, svc_name, svc_price, svc_stack,
                 svc_time, ticks)
import content as R

GUIDE_BY = {g["slug"]: g for g in R.GUIDES}


# ---------------------------------------------------------------------------
# Shared copy
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
    ("Do we have to use Odoo?",
     lambda: ("No. Plenty of businesses run well on Shopify and a bookkeeping app, and we will tell you if that is "
              "you. When a back office is needed, we set up Odoo, because it covers stock, purchasing, sales and "
              "accounting in one system at a price a 5 to 50 person business can carry.")),
    ("Who owns the accounts and the data?",
     lambda: ("You do. Your Shopify store, Odoo database and app accounts stay in your name and on your "
              "billing. We work through named staff or collaborator accounts, and we remove our access at "
              "project close and confirm it in writing.")),
    ("What happens on the scoping call?",
     lambda: (f"It is a {C.PROMISES['call_length']} video call at no charge. We go through what you sell, "
              f"your channels, your current systems and your timeline. You get a proposal or a Roadmap quote "
              f"{C.PROMISES['proposal_after_call']}. If we are not the right fit, we say so on the call.")),
]

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

SVC_EXTRA = {
    "systems-roadmap": {
        "h1": "A written plan and a fixed quote before you buy software or start a build",
        "for": ["You know the current setup is not working, but not yet which systems, connector or plan to use",
                "You are moving off spreadsheets or QuickBooks and want the order of work decided first",
                "The project is larger: more than 15 users, manufacturing, several companies or long history"],
        "after": ["An 8 to 15 page roadmap that is yours to keep, with us or without us",
                  "A connector and plan recommendation checked in a trial database",
                  "A draft statement of work with a fixed fee for the next phase"],
        "faqs": [("Is the roadmap fee credited if we go ahead?",
                  "The roadmap is a separate paid piece of work, and its price is set in writing before it starts. "
                  "Any credit toward a later phase is written into your proposal, so you know before you sign."),
                 ("What do you need from us?",
                  "Up to three working sessions of 60 to 90 minutes with the people who run orders, stock and the "
                  "books, plus read-only access or exports of your current systems.")],
    },
    "store-move": {
        "h1": "Move your store to Shopify with products, customers, order history and redirects intact",
        "for": ["You sell on WooCommerce, Wix, Square Online or BigCommerce and the plugins are holding you back",
                "You want Shopify POS in one or two stores alongside the online shop",
                "Search rankings and old links have to survive the move"],
        "after": ["Products, customers and order history in Shopify, checked against counts you sign off",
                  "A redirect from every old URL, tested before the domain moves",
                  "A recorded training session and a short admin guide for your team"],
        "faqs": [("Will our customers get emails during the import?",
                  "No. Customer and order imports run with notifications off, and we test with internal orders "
                  "before launch."),
                 ("What happens to our search rankings?",
                  "Every old URL gets a 301 redirect to its new page, tested before the domain moves. That keeps "
                  "links and bookmarks working and passes them to the new pages."),
                 ("Do customers keep their accounts after a move?",
                  "Their names, addresses and order history come over. Passwords can't be moved between platforms, "
                  "so customers set a new one. We write the invite email with you, so customers know why.")],
    },
    "odoo-launch": {
        "h1": "A back office for stock, purchasing, sales and accounting, set up for a team of 5 to 15",
        "for": ["Stock lives in spreadsheets and nobody trusts the numbers",
                "Purchasing is done from memory, and vendor bills are typed in by hand",
                "You have outgrown QuickBooks for inventory and want one system for the back office"],
        "after": ["Odoo configured in staging first, then moved to live on a planned date",
                  "Your products, customers, vendors, opening stock and balances, loaded twice and reconciled",
                  "Four weeks of fixes after go-live, with daily check-ins in week one"],
        "faqs": [("Odoo Online, Odoo.sh or on-premise?",
                  "Odoo Online or Odoo.sh. The roadmap or scoping call picks the one that fits your apps and any "
                  "connector you need, before you buy a plan."),
                 ("Can we keep QuickBooks for a while?",
                  "Yes. Many teams keep QuickBooks open for lookups after go-live. We move products, customers, "
                  "vendors, opening stock, open invoices and opening balances. Full history stays in QuickBooks."),
                 ("Do you give accounting or tax advice?",
                  "No. Tax and accounting settings follow written instructions from your accountant, and we set "
                  "them up exactly as written.")],
    },
    "connection": {
        "h1": "Connect Shopify and Odoo so orders, stock and refunds stay in step",
        "for": ["You run Shopify and Odoo already, and someone copies orders between them by hand",
                "Stock counts on the website disagree with the shelf and with Odoo",
                "Refunds and POS sales do not reach the books cleanly"],
        "after": ["A connector chosen on paper and checked in a trial database before you buy it",
                  "Sync rules for orders, stock, fulfillments, refunds and taxes, tested with your team",
                  "Two weeks of monitoring after go-live and a one-page guide for your staff"],
        "faqs": [("Which connector do you use?",
                  "The one that fits your Odoo plan and hosting. Third-party connector modules cannot be installed "
                  "on Odoo Online, and connectors that use Odoo's API need its Custom plan. The memo compares the "
                  "options with license cost and limits."),
                 ("Who pays for the connector?",
                  "You buy the license directly from the vendor, in your name. It is listed in your proposal "
                  "separately from our fee.")],
    },
}

PROBLEMS = [  # home: the four problems we're asked to fix, each tied to the service that fixes it
    ("connection", "The website, the shelf and the books disagree",
     "Orders are copied between systems by hand, stock counts drift apart and refunds miss the books."),
    ("odoo-launch", "Stock and purchasing live in spreadsheets",
     "Nobody trusts the count, reorders come from memory and vendor bills are typed in twice."),
    ("store-move", "The store platform is holding you back",
     "Plugins break on update, the registers don't match the website and every change needs a developer."),
    ("systems-roadmap", "Something has to change, but it isn't clear what",
     "Which systems, which connector, which plan and in what order, settled before money goes on software."),
]


def svc_mini(slug, i=0):
    """A compact link card for one service: icon, name, price and timeline."""
    return (f'<a class="svc-mini {SVC_COLOR[slug]}" href="{svc_href(slug)}"><span class="ic-block">{spot(SVC_SPOT[slug])}</span>'
            f'<span><b>{e(svc_name(slug))}</b><em><span class="price">{svc_price(slug)}</span> · {e(svc_time(slug))}</em></span>'
            f'{icon("arrow-right")}</a>')


def hero(h1, lead, *, eyebrow="", trail="", art="", cta="", extra="", cls=""):
    """Inner page hero: copy on the left, a drawn scene or a screen on the right."""
    return f"""
<section class="hero {cls}"><div class="wrap hero-grid{' no-art' if not art else ''}">
  <div class="hero-copy">{trail}{f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ''}
    <h1>{e(h1)}</h1><p class="lead">{lead}</p>{extra}{f'<div class="cta-line">{cta}</div>' if cta else ''}</div>
  {f'<div class="hero-art">{art}</div>' if art else ''}
</div></section>"""


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------

def page_home():
    cta = primary_cta("hero") + more_link("/pricing", "See prices")
    assure = "".join(f"<li>{icon(i)}<span>{e(t)}</span></li>" for i, t in [
        ("file-check-2", "A fixed fee, agreed in writing"), ("key-round", "Your accounts stay in your name"),
        ("clock", f"{C.TIMEZONE_LABEL} business hours")])
    shop_clip = next((k for k in C.CLIPS if C.CLIPS[k][0] == "shopify"), None)
    pair = [shop_clip, "sale"] if shop_clip else ["sale", "locations"]
    gap = [("Storefront agencies", "theme", "Build the theme, the apps and the checkout. Their work usually ends once the "
                                            "order is placed."),
           ("ERP resellers", "back-office", "Sell the licenses and set up the warehouse and accounting. Their work starts "
                                            "once an order reaches them."),
           ("Where we work", "sync", "Both sides and the link between them: what each system owns, how orders, stock, "
                                     "refunds and payouts move, and how your team runs it each day.")]
    gap_html = "".join(f'<div class="gap-col{" us" if n == 2 else ""}"><span class="ic-block">{spot(ic)}</span>'
                       f'<h3>{e(h)}</h3><p>{e(t)}</p></div>' for n, (h, ic, t) in enumerate(gap))
    probs = "".join(f"""
<a class="prob {SVC_COLOR[s]}" href="{svc_href(s)}">
  <span class="ic-block">{spot(SVC_SPOT[s])}</span>
  <h3>{e(h)}</h3><p>{e(t)}</p>
  <span class="prob-fix"><b>{e(svc_name(s))}</b><span class="price">{svc_price(s)}</span><span>{e(svc_time(s))}</span>{icon('arrow-right')}</span>
</a>""" for s, h, t in PROBLEMS)
    inds = "".join(f"""
<a class="ind-tile" href="/industries/{x['slug']}">
  {ind_tile(x)}<b>{e(x['short'])}</b><span>{e(x['card'])}</span>
</a>""" for x in I.INDUSTRIES)
    steps = [("calendar-check", "Scoping call", f"{C.PROMISES['call_length'].capitalize()}, no charge. You get a proposal "
              f"or a Roadmap quote {C.PROMISES['proposal_after_call']}."),
             ("file-check-2", "Written scope", "Scope, exclusions, milestones and a fixed fee, signed before work starts."),
             ("server", "Build in staging", "Set up and loaded in a copy first, then tested by your team against "
              "written cases."),
             ("package-check", "Go-live and handover", "A planned date outside your peak season, fixes after launch, "
              "and our access removed in writing.")]
    step_html = "".join(f'<li><span class="ic-block">{spot(i)}</span><span><b>{e(h)}</b>{e(t)}</span></li>'
                        for i, h, t in steps)
    rows = "".join(f'<tr><th scope="row"><a href="{svc_href(s)}">{e(svc_name(s))}</a></th><td class="price">{svc_price(s)}</td>'
                   f'<td>{e(svc_time(s))}</td></tr>' for s in ORDER + ["support"])
    fit_yes = ["US product businesses with roughly 5 to 50 staff",
               "Selling online, in your own shops, to wholesale accounts, or all three",
               "Running Shopify, or ready to move to it, with stock that has outgrown spreadsheets"]
    fit_no = ["Projects for more than 50 users, or several companies across countries",
              "Custom theme design, ads or marketing work",
              "Tax or accounting advice, which stays with your accountant"]
    faqs = [(q, fn()) for q, fn in HOME_FAQS]
    body = f"""
<section class="hero home"><div class="wrap hero-grid">
  <div class="hero-copy">
    <p class="eyebrow">Ecommerce and ERP consulting</p>
    <h1 class="display">Shopify and Odoo, planned, set up and connected for product businesses</h1>
    <p class="lead">We decide which systems you need, move your store, set up the back office and connect the two, so
    orders, stock and the books agree. Every project has a written scope and a fixed fee, from
    {price('roadmap_min')} for a roadmap.</p>
    <div class="cta-line">{cta}</div>
    <ul class="assure">{assure}</ul>
  </div>
  <div class="hero-art">{stack("shop-order", "delivery-c", "hero-stack", eager=True)}</div>
</div></section>

<section class="sec" aria-labelledby="gap-h"><div class="wrap">
  {sec_head("The work between the storefront and the warehouse", "Most product businesses hire two kinds of help. "
            "Orders, stock and refunds go missing in the handoff between them.", "gap-h")}
  <div class="gap">{gap_html}</div>
</div></section>

<section class="sec tint" aria-labelledby="prob-h"><div class="wrap">
  {sec_head("Four problems we're asked to fix, and what each costs", "Each one maps to a service with a price range "
            "and a typical timeline. Your exact fee is fixed in writing after a call.", "prob-h")}
  <div class="probs">{probs}</div>
  <p class="after-grid">After go-live, a <a href="{svc_href('support')}">{e(C.SUPPORT['name'])}</a> gives you prepaid hours
  for questions and small changes, from {price('support_10h')}.</p>
</div></section>

<section class="sec" aria-labelledby="ind-h"><div class="wrap">
  {sec_head("The problems we fix, by industry", "What costs each kind of product business the most, and how Shopify "
            "and Odoo are set up to stop it.", "ind-h")}
  <div class="inds">{inds}</div>
</div></section>

<section class="sec tint" aria-labelledby="rec-h"><div class="wrap">
  {sec_head("The same work in Shopify and in Odoo", "Real screens from our own demo store and Odoo database, with "
            "sample data. Each clip starts on the task and stops when it is done.", "rec-h")}
  <div class="clips2">{''.join(clip(k) for k in pair)}</div>
  <p class="after-grid">{more_link("/videos", "See all recordings")}</p>
</div></section>

<section class="sec" aria-labelledby="how-h"><div class="wrap split">
  <div>
    {sec_head("How a project runs", "The same path for every project. Each step ends in something written that you "
              "can check.", "how-h")}
    <ol class="steps-v">{step_html}</ol>
    <p>{more_link("/how-it-works", "See every step and document")}</p>
  </div>
  <div class="split-art">{M.sample_roadmap()}</div>
</div></section>

<section class="sec tint" aria-labelledby="price-h"><div class="wrap split">
  <div>
    {sec_head("Prices", "Fixed fees, agreed in writing before work starts. Software is billed to you by each vendor.",
              "price-h")}
    <div class="tbl"><table class="ptable"><thead><tr><th scope="col">Service</th><th scope="col">Fixed fee</th>
    <th scope="col">Typical timeline</th></tr></thead><tbody>{rows}</tbody></table></div>
  </div>
  <div class="fit">
    <h3>A good fit</h3>{ticks([e(x) for x in fit_yes], "yes")}
    <h3>Not a fit</h3>{ticks([e(x) for x in fit_no], "no")}
  </div>
</div></section>

<section class="sec" aria-labelledby="faq-h"><div class="wrap narrow">
  {sec_head("Questions owners ask first", "", "faq-h")}
  {qa_list(faqs)}
  <p class="after-grid">{more_link("/faq", "More questions and answers")}</p>
</div></section>"""
    return {"path": "/", "file": "index.html", "h": "Home",
            "title": f"Shopify and Odoo consulting for product businesses | {NAME}",
            "desc": ("Ecommerce and ERP consulting for US product businesses. Shopify store moves, Odoo back office "
                     "setups and the link between them, each at a fixed fee."),
            "body": body, "schema": [faq_schema(faqs)]}


# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------

def compare_table():
    head = "".join(f'<th scope="col"><a href="{svc_href(s)}">{e(PKG[s]["name"])}</a></th>' for s in ORDER)
    rows = [("Fixed fee", lambda p: f'<span class="price">{price(*p["price"])}</span>'),
            ("Typical timeline", lambda p: e(p["timeline"])),
            ("What it is", lambda p: e(p["kind"])),
            ("Payment", lambda p: e(p["payment"].split(". ")[0].rstrip(".")))]
    body = "".join(f'<tr><th scope="row">{e(lab)}</th>' + "".join(f"<td>{fn(PKG[s])}</td>" for s in ORDER) + "</tr>"
                   for lab, fn in rows)
    return (f'<div class="tbl"><table class="ctable"><thead><tr><td></td>{head}</tr></thead>'
            f'<tbody>{body}</tbody></table></div>')


def page_services():
    rows = []
    for n, s in enumerate(ORDER + ["support"]):
        if s == "support":
            fit, summary = [], C.SUPPORT["summary"]
        else:
            fit, summary = SVC_EXTRA[s]["for"][:2], PKG[s]["summary"]
        rows.append(f"""
<article class="svc-row {SVC_COLOR[s]}{' flip' if n % 2 else ''}">
  <div class="svc-row-art">{svc_stack(s)}</div>
  <div class="svc-row-copy">
    <p class="eyebrow">{e(PKG[s]['kind'] if s != 'support' else 'Prepaid hours')}</p>
    <h2><a href="{svc_href(s)}">{e(svc_name(s))}</a></h2>
    <p>{e(summary)}</p>
    {ticks([e(x) for x in fit]) if fit else ''}
    {facts([("Fixed fee", f'<span class="price">{svc_price(s)}</span>'), ("Typical timeline", e(svc_time(s)))])}
    {more_link(svc_href(s), "What's included")}
  </div>
</article>""")
    body = hero("Ecommerce and ERP services with fixed fees",
                "Five services, each with a written scope. The ranges are what most projects of each kind cost; your "
                "exact fee comes from a scoping call or a Systems Roadmap and goes into your statement of work.",
                eyebrow="Services", cta=primary_cta("hero")) + f"""
<section class="sec"><div class="wrap">{''.join(rows)}</div></section>
<section class="sec tint" aria-labelledby="cmp-h"><div class="wrap">
  {sec_head("The four projects side by side", "", "cmp-h")}
  {compare_table()}
  <p class="small">{e(C.LARGER_PROJECTS.format(larger_odoo_from=price("larger_odoo_from")))}</p>
</div></section>
<section class="sec"><div class="wrap split">
  <div><h2>What you pay Shopify, Odoo and app vendors</h2>
    <p>Your Shopify plan, POS Pro, theme and apps, your Odoo subscription and any Odoo.sh hosting, connector
    licenses, card processing and hardware are billed to you directly by each vendor. None of it is part of our
    fee, and each item is listed in your proposal.</p>
    <p class="small">{e(C.REFERRAL_DISCLOSURE.format(name=NAME))}</p>
    <p class="small">{e(C.SALES_TAX_LINE)}</p></div>
  <div><h2>Questions about scope and fees</h2>{qa_list(SERVICE_FAQS)}</div>
</div></section>"""
    return {"path": "/services", "file": "services.html", "h": "Services",
            "title": f"Shopify and Odoo services and fixed fees | {NAME}",
            "desc": ("Fixed-fee Shopify store moves, Odoo back office setups for 5 to 15 users, Shopify and Odoo "
                     "connections, systems roadmaps and prepaid support. Ranges and scope for each."),
            "body": body, "schema": [faq_schema(SERVICE_FAQS)], "band": "Talk through which service fits"}


def erp_check():
    qs = "".join(
        f'<fieldset class="pk-q" data-eq="{k}"><legend>{i + 1}. {e(q)}</legend><div class="opts">'
        f'<button type="button" class="opt" data-v="1" aria-pressed="false"><span>Yes</span></button>'
        f'<button type="button" class="opt" data-v="0" aria-pressed="false"><span>No</span></button></div></fieldset>'
        for i, (k, q) in enumerate(R.ERP_CHECK))
    results = [
        ("0", "Not yet", "Your setup is coping. Fix the one or two weak spots with Shopify's own tools or a single "
         "app, and run this check again in six months."),
        ("1", "Worth a roadmap", "Several jobs are straining your setup. Before you buy anything, map what an ERP would "
         f"change and what it would cost. That is what a Systems Roadmap does, for {price('roadmap_min', 'roadmap_max')}."),
        ("2", "Ready for an ERP", "Workarounds are likely costing more than one system would. The next step is a "
         "written scope: which apps, which data, and a go-live date outside your busy season."),
    ]
    res = "".join(f'<div data-er="{k}" hidden><p class="eyebrow">Your result</p><h3>{e(t)}</h3><p>{x}</p></div>'
                  for k, t, x in results)
    return f"""
<div class="picker" data-erp hidden>
  <div class="pk-qs">{qs}</div>
  <div class="pk-r" aria-live="polite">
    <div data-er-empty><p class="eyebrow">Your result</p><p>Answer all eight and your result shows here.</p>
    <p class="small" data-er-count></p></div>
    {res}
    <p class="small" data-er-n hidden></p>
  </div>
</div>
<noscript><p>The check needs JavaScript. Without it: 0 to 2 yes answers means not yet, 3 to 5 means a roadmap is
worth it, and 6 to 8 means you are ready for an ERP.</p></noscript>
<p class="small">Your answers stay in your browser. Our visit counter notes only which of the three results came up.
0 to 2 yes answers: not yet. 3 to 5: worth a roadmap. 6 to 8: ready.</p>"""


SHOPIFY_PLANS = {  # research/R-Shopify-plans-checked.md, shopify.com/pricing, checked Nov 11, 2026
    "basic": ("Basic", 29, 39), "grow": ("Grow", 89, 105), "advanced": ("Advanced", 359, 399),
    "plus": ("Plus", 2300, 2300),
}
POS_PRO = 89


def plan_picker():
    def q(key, legend, opts):
        btns = "".join(f'<button type="button" class="opt" data-v="{v}" aria-pressed="false"><span>{e(t)}</span></button>'
                       for v, t in opts)
        return f'<fieldset class="pk-q" data-pq="{key}"><legend>{e(legend)}</legend><div class="opts">{btns}</div></fieldset>'

    qs = (q("loc", "Where do you sell in person?",
            [("0", "Online only"), ("1", "1 shop"), ("2", "2 shops"), ("3", "3 to 10 shops"), ("11", "More than 10")]) +
          q("staff", "How many staff need their own Shopify login?",
            [("0", "Only the owner"), ("5", "Up to 5"), ("15", "6 to 15"), ("16", "More than 15")]) +
          q("perm", "Do staff at the register need different permissions, or in-store stock tools?",
            [("no", "No"), ("yes", "Yes")]) +
          q("b2b", "Do you sell wholesale with more than 3 price lists?", [("no", "No"), ("yes", "Yes")]) +
          q("sync", "Will Shopify connect to a back office such as Odoo?", [("no", "No"), ("yes", "Yes")]))
    plans = json.dumps({k: {"n": n, "y": y, "m": m} for k, (n, y, m) in SHOPIFY_PLANS.items()} | {"pro": POS_PRO})
    rows = "".join(f'<tr><th scope="row">{n}</th><td data-label="Paid yearly">${y:,} a month</td><td data-label="Paid monthly">${m:,} a month</td></tr>'
                   for n, y, m in SHOPIFY_PLANS.values())
    return f"""
<div class="picker" data-picker data-plans="{e(plans)}" hidden>
  <div class="pk-qs">{qs}</div>
  <div class="pk-r" aria-live="polite">
    <div data-pk-empty><p class="eyebrow">Your result</p><p>Answer the questions and the plan that fits shows here.</p></div>
    <div data-pk-out hidden>
      <p class="eyebrow">The plan that fits</p>
      <h3 data-pk-plan>Basic</h3>
      <ul class="pk-why" data-pk-why></ul>
      <dl class="facts"><div><dt>Paid yearly</dt><dd data-pk-y></dd></div><div><dt>Paid monthly</dt><dd data-pk-m></dd></div></dl>
      <p class="small" data-pk-pro></p>
      <p class="small">Plan prices only, before card fees, apps and hardware. Shopify changes plans often, so check
      shopify.com before you buy.</p>
    </div>
  </div>
</div>
<div class="split rules">
  <div><h3>How the picker decides</h3><ul class="plain">
    <li><b>Plus</b> when you sell from more than 10 locations, need more than 15 staff logins, or need more than 3
    wholesale catalogs. Plus is quoted from $2,300 a month.</li>
    <li><b>Advanced</b> when 6 to 15 staff need their own login. It includes 15 staff accounts.</li>
    <li><b>Grow</b> when up to 5 staff need a login, or Shopify will connect to a back office. Grow includes 5 staff
    accounts, and Shopify lists full data access for custom apps from Grow up, which some connectors use.</li>
    <li><b>Basic</b> for an owner-run store. Every plan takes in-person payments and allows up to 10 locations.</li>
    <li><b>POS Pro</b> adds staff roles, in-store inventory tools, and pickup and delivery for $89 a month per location.
    Plus includes it for 20 locations.</li></ul></div>
  <div><h3>Shopify plan prices</h3>
    <div class="tbl"><table class="gtable"><thead><tr><th scope="col">Plan</th><th scope="col">Paid yearly</th>
    <th scope="col">Paid monthly</th></tr></thead><tbody>{rows}</tbody></table></div>
    <p class="small">US prices from <a href="https://www.shopify.com/pricing" rel="noopener">shopify.com/pricing</a>,
    checked Nov 11, 2026.</p></div>
</div>"""


def sync_model():
    return f"""
<div class="sim" data-sim hidden>
  <div class="sim-sides">
    <div class="sim-side"><p class="sim-h">{icon('shopping-cart')}Shopify shows</p>
      <p class="sim-n" data-shop>33</p><p class="small">Cabinet with Doors, available to sell</p></div>
    <div class="sim-mid" aria-hidden="true"><span class="sim-wire" data-wire></span></div>
    <div class="sim-side"><p class="sim-h">{icon('warehouse')}Odoo on hand</p>
      <p class="sim-n" data-odoo>33</p><p class="small">Cabinet with Doors, main warehouse</p></div>
  </div>
  <p class="sim-state" data-state aria-live="polite"><span class="tag ok">In step</span>Both systems show the same count.</p>
  <div class="sim-acts">
    <button type="button" class="opt" data-act="web">{icon('shopping-cart')}<span>Sell 1 online</span></button>
    <button type="button" class="opt" data-act="pos">{icon('store')}<span>Sell 1 at the register</span></button>
    <button type="button" class="opt" data-act="buy">{icon('truck')}<span>Receive 10 in Odoo</span></button>
    <button type="button" class="opt" data-act="off" aria-pressed="false">{icon('plug')}<span>Connector off</span></button>
    <button type="button" class="link-btn" data-act="reset">{icon('rotate-ccw')}Start again</button>
  </div>
  <ol class="sim-log" data-log aria-label="Sync log"><li><b>09:00:00</b>Connector running. Odoo holds the stock count.</li></ol>
</div>
<ul class="plain sim-rules">
  <li><b>Sell 1 online.</b> Shopify takes the order. The connector brings it into Odoo, Odoo lowers its count, and the
  new count goes back to Shopify.</li>
  <li><b>Sell 1 at the register.</b> The same path. To Odoo, a register sale is one more order.</li>
  <li><b>Receive 10 in Odoo.</b> Stock arrives on a purchase order. Shopify can sell those units once the connector
  sends the new count.</li>
  <li><b>Connector off.</b> Orders pile up in Shopify and received stock stays invisible to it, so both counts drift.
  Switching it back on catches up the queue.</li>
</ul>
<p class="small">A simplified model with one product and sample numbers. Real connectors differ in what they sync
and how often; we set and test those rules for your plan.</p>"""


def svc_feature(slug):
    """The working part of each service page: a tool or real recordings, placed where the decision is made."""
    if slug == "systems-roadmap":
        return f"""
<section class="sec tint" id="readiness" aria-labelledby="erp-h"><div class="wrap">
  {sec_head("An eight-question ERP readiness check", "Answer yes or no. Three or more yes answers usually mean a "
            "roadmap will pay for itself.", "erp-h")}
  {erp_check()}
</div></section>
<section class="sec" aria-labelledby="doc-h"><div class="wrap split">
  <div>{sec_head("What the roadmap looks like", "Eight to fifteen pages, written for the people who run the business. "
                  "It is yours to keep whether or not we do the build.", "doc-h")}
  {ticks(["How orders, stock, purchasing and money move today, with the weak spots marked",
          "Which systems, plan and connector fit, checked in a trial database",
          "What data moves, what stays behind, and the risks",
          "A fixed fee and timeline for the next phase"])}</div>
  <div class="split-art">{M.sample_roadmap()}</div>
</div></section>"""
    if slug == "store-move":
        shop = [k for k in C.CLIPS if C.CLIPS[k][0] == "shopify"]
        clips = (f'<div class="clips2">{"".join(clip(k) for k in shop[:4])}</div>' if shop else "")
        return f"""
<section class="sec tint" id="plan-picker" aria-labelledby="pp-h"><div class="wrap">
  {sec_head("Which Shopify plan fits your shops and staff", "Five questions, answered in your browser, with prices "
            "checked on shopify.com on Nov 11, 2026.", "pp-h")}
  {plan_picker()}
</div></section>{f'''
<section class="sec" aria-labelledby="shrec-h"><div class="wrap">
  {sec_head("Everyday Shopify tasks, on real screens", "Admin screens from our own Shopify demo store, with sample "
            "data, shown one step at a time. The pointer is drawn in to mark each click.", "shrec-h")}{clips}
  <p class="after-grid">For selling in person, Shopify shows its point of sale app on
  <a href="https://www.shopify.com/pos" rel="noopener">its own POS page</a>.</p>
</div></section>''' if clips else ''}
<section class="sec" aria-labelledby="mv-h"><div class="wrap split">
  <div>{sec_head("What moves, and how it is checked", "Counts are taken on the old platform before anything moves, "
                  "then matched in Shopify. You sign off the counts before the domain changes.", "mv-h")}
  {ticks(["Products, variants, images and collections", "Customers and their addresses",
          "Order history, imported with notifications off", "Pages, blog posts and a 301 redirect for every old URL"])}</div>
  <div class="split-art">{M.sample_fieldmap()}</div>
</div></section>"""
    if slug == "odoo-launch":
        keys = ["sale", "purchase", "pos", "invoice", "count", "reports"]
        return f"""
<section class="sec tint" id="recordings" aria-labelledby="rec-h"><div class="wrap">
  {sec_head("What your team will do in Odoo each day", "Recorded in our own Odoo 20 database with sample data. Each "
            "recording starts on the task and stops when it is done.", "rec-h")}
  <div class="clips2">{''.join(clip(k) for k in keys)}</div>
</div></section>"""
    if slug == "connection":
        return f"""
<section class="sec tint" id="sync-model" aria-labelledby="sm-h"><div class="wrap">
  {sec_head("How a connector keeps stock counts in step", "One product, sample numbers. Odoo owns the stock count and "
            "Shopify shows what it can sell. Try each button.", "sm-h")}
  {sync_model()}
</div></section>
<section class="sec" aria-labelledby="sr-h"><div class="wrap">
  {sec_head("The Odoo side, recorded", "What happens in Odoo when stock moves or an order comes back. With a "
            "connector in place, Shopify gets the new count after each one.", "sr-h")}
  <div class="clips2">{clip("locations")}{clip("return")}</div>
</div></section>"""
    return ""


def industries_for(slug):
    return [x for x in I.INDUSTRIES if slug in x["start"][:2]]


def page_service(p):
    slug = p["slug"]
    x = SVC_EXTRA[slug]
    trail, crs = crumbs([("Services", "/services"), (p["name"], svc_href(slug))])
    faqs = x["faqs"] + SERVICE_FAQS[:2]
    inds = industries_for(slug)
    ind_html = "".join(f'<a class="chip-link" href="/industries/{i["slug"]}">{e(i["short"])}</a>' for i in inds)
    others = "".join(svc_mini(o) for o in ORDER + ["support"] if o != slug)
    body = hero(x["h1"], e(p["summary"]), trail=trail, eyebrow=e(p["kind"]),
                extra=facts([("Fixed fee", f'<span class="price">{price(*p["price"])}</span>'),
                             ("Typical timeline", e(p["timeline"]))], "hero-facts"),
                cta=primary_cta("service"), art=svc_stack(slug, eager=True), cls=SVC_COLOR[slug]) + f"""
<section class="sec" aria-labelledby="fit-h"><div class="wrap split">
  <div><h2 id="fit-h">A good fit when</h2>{ticks([e(i) for i in x['for']])}</div>
  <div><h2>What you have at the end</h2><ol class="nums">{''.join(f'<li>{e(i)}</li>' for i in x['after'])}</ol></div>
</div></section>
{svc_feature(slug)}
<section class="sec{' tint' if slug in ('store-move', 'systems-roadmap') else ''}" aria-labelledby="inc-h"><div class="wrap split">
  <div><h2 id="inc-h">What's included</h2>{ticks([e(i) for i in p['includes']])}</div>
  <div><h2>Not included</h2><p>{e(p['excludes'])}</p>
  <h3>Payment</h3><p>{e(p['payment'])}</p>
  {f'<h3>Where this comes up most</h3><div class="chips-row">{ind_html}</div>' if inds else ''}</div>
</div></section>
<section class="sec" aria-labelledby="q-h"><div class="wrap split">
  <div><h2 id="q-h">Questions about the {e(p['name'])}</h2>{qa_list(faqs)}</div>
  <div><h2>Other services</h2><div class="svc-minis">{others}</div></div>
</div></section>"""
    return {"path": svc_href(slug), "file": f"services/{svc_href(slug).split('/')[-1]}.html", "h": p["name"],
            "title": f"{p['name']}: {p['kind'].lower()} | {NAME}",
            "desc": f"{x['h1']}. {p['name']}: {price(*p['price'])}, typically {p['timeline']}. Fixed fee in writing.",
            "body": body, "schema": [faq_schema(faqs), service_schema(p, svc_href(slug)), crs],
            "band": f"Ask about a {p['name']}"}


def page_support():
    s = C.SUPPORT
    trail, crs = crumbs([("Services", "/services"), (s["name"], svc_href("support"))])
    opts = "".join(f'<div class="opt-card"><b>{e(h)}</b><span class="price big">{price(k)}</span><em>{e(v)}</em></div>'
                   for h, k, v in s["options"])
    faqs = [("What counts as a support request?",
             "Questions, small changes, report tweaks, adding users, connector troubleshooting and short training. "
             "Anything over 4 hours is quoted separately first."),
            ("Is there emergency or after-hours support?",
             f"No. We reply {C.PROMISES['support_reply']}, {C.PROMISES['business_days']}, {C.TIMEZONE_LABEL} time."),
            ("Can we buy hours if you didn't set up our systems?",
             "Yes, after a short review of your setup so we know what we are supporting. The review is quoted first.")]
    others = "".join(svc_mini(o) for o in ORDER)
    body = hero("Prepaid hours for the questions and small changes after go-live",
                f"{e(s['summary'])} We reply {e(C.PROMISES['support_reply'])}, {e(C.PROMISES['business_days'])}, "
                f"{e(C.TIMEZONE_LABEL)} time.", trail=trail, eyebrow="Prepaid hours",
                extra=f'<div class="opt-cards">{opts}</div>', cta=primary_cta("service"), art=svc_stack("support", eager=True),
                cls="c-yellow") + f"""
<section class="sec" aria-labelledby="hw-h"><div class="wrap split">
  <div><h2 id="hw-h">How the hours work</h2><p>{e(s['terms'])}</p>
  {ticks(["Questions about Shopify, Odoo or the connector between them", "Small changes, new reports and new users",
          "Connector errors looked at and fixed", "Short training sessions for new staff, recorded"])}</div>
  <div><h2>Questions</h2>{qa_list(faqs)}</div>
</div></section>
<section class="sec tint"><div class="wrap"><h2>The projects before support</h2><div class="svc-minis four">{others}</div></div></section>"""
    return {"path": svc_href("support"), "file": "services/support-block.html", "h": s["name"],
            "title": f"Support block: prepaid hours | {NAME}",
            "desc": (f"Prepaid support hours for Shopify and Odoo after go-live: 10 hours {price('support_10h')}, "
                     f"20 hours {price('support_20h')}. Replies {C.PROMISES['support_reply']}."),
            "body": body, "schema": [faq_schema(faqs), crs], "band": "Ask about support hours"}


# ---------------------------------------------------------------------------
# Industries
# ---------------------------------------------------------------------------

def page_industries():
    cards = "".join(f"""
<a class="ind-card {x['color']}" href="/industries/{x['slug']}">
  <span class="ind-art">{ind_tile(x)}</span>
  <span class="ind-body"><b>{e(x['short'])}</b><span>{e(x['lead'])}</span>
  <ul>{''.join(f'<li>{e(p[0])}</li>' for p in x['problems'])}</ul>
  <em>See the fixes{icon('arrow-right')}</em></span>
</a>""" for x in I.INDUSTRIES)
    body = hero("Shopify and Odoo for product businesses, by industry",
                "Each kind of business loses money in its own places: sizes that oversell, freight left out of costs, "
                "lots nobody can trace, price lists kept in a spreadsheet. These pages name the problem, what it "
                "costs and how it gets fixed.", eyebrow="Industries") + f"""
<section class="sec"><div class="wrap"><div class="ind-cards">{cards}</div>
<p class="after-grid">Selling something else? The same problems show up in most product businesses.
{more_link("/services", "See the services")}</p></div></section>"""
    return {"path": "/industries", "file": "industries.html", "h": "Industries",
            "title": f"Shopify and Odoo by industry | {NAME}",
            "desc": ("The problems that cost apparel, furniture, food, beauty and wholesale businesses the most, and "
                     "how Shopify and Odoo are set up to fix them."),
            "body": body, "band": "Talk through your business on a call"}


def page_industry(x):
    path = f"/industries/{x['slug']}"
    trail, crs = crumbs([("Industries", "/industries"), (x["short"], path)])
    rows = []
    for n, (title, cost, fix, media) in enumerate(x["problems"], 1):
        m = clip(media[1]) if media and media[0] == "clip" else ""
        rows.append(f"""
<article class="pr-row{' flip' if n % 2 == 0 else ''}{' no-media' if not m else ''}">
  <div class="pr-copy">
    <span class="pr-n">{n:02d}</span>
    <h3>{e(title)}</h3>
    <p class="pr-cost"><b>What it costs you.</b> {e(cost)}</p>
    <p class="pr-fix"><b>How it gets fixed.</b> {e(fix)}</p>
  </div>
  {f'<div class="pr-media">{m}</div>' if m else ''}
</article>""")
    a, b, text = x["start"]
    guides = [GUIDE_BY[g] for g in x.get("guides", []) if g in GUIDE_BY]
    glinks = "".join(f'<li><a href="/guides/{g["slug"]}">{e(g["title"])}</a></li>' for g in guides)
    srcs = "".join(f'<li><a href="{e(u)}" rel="noopener">{e(t)}</a></li>' for t, u in x.get("sources", []))
    others = "".join(f'<a class="chip-link" href="/industries/{o["slug"]}">{e(o["short"])}</a>'
                     for o in I.INDUSTRIES if o["slug"] != x["slug"])
    body = hero(x["h1"], e(x["lead"]), trail=trail, eyebrow="Industry",
                cta=primary_cta("hero") + more_link("#start", "Where to start"),
                cls=x["color"]) + f"""
<section class="sec" aria-labelledby="pr-h"><div class="wrap">
  {sec_head(f"What costs {x['short'].lower()} businesses the most", "The problems owners in this trade raise most "
            "often, what each one costs, and how it gets fixed. Recordings are from our own demo database with "
            "sample data.", "pr-h")}
  <div class="pr-rows">{''.join(rows)}</div>
</div></section>
<section class="sec tint" id="start" aria-labelledby="st-h"><div class="wrap split">
  <div><h2 id="st-h">Where to start</h2><p>{e(text)}</p>
  <div class="svc-minis">{svc_mini(a)}{svc_mini(b)}</div></div>
  <div><h2>Questions</h2>{qa_list(x['faqs'])}</div>
</div></section>
<section class="sec"><div class="wrap split">
  <div>{f'<h2>Read more</h2><!--reuse--><ul class="plain">{glinks}</ul><!--/reuse-->' if glinks else ''}
  {f'<h3>Sources</h3><ul class="plain small">{srcs}</ul>' if srcs else ''}</div>
  <div><h2>Other industries</h2><div class="chips-row">{others}</div></div>
</div></section>"""
    return {"path": path, "file": f"industries/{x['slug']}.html", "h": x["short"],
            "title": f"{x['title']} | {NAME}" if len(f"{x['title']} | {NAME}") <= 66 else x["title"],
            "desc": x["desc"], "body": body, "schema": [faq_schema(x["faqs"]), crs],
            "band": f"Talk through your {x['short'].lower()} business"}


# ---------------------------------------------------------------------------
# How we work, pricing, about, book
# ---------------------------------------------------------------------------

STEPS = [
    ("calendar-check", "Scoping call", C.PROMISES["call_length"] + " call",
     f"We go through what you sell, your channels, your current systems and your timeline. You get a "
     f"proposal or a Roadmap quote {C.PROMISES['proposal_after_call']}."),
    ("map", "Systems Roadmap", "2–3 weeks",
     "Up to three working sessions, then a written plan: what fits standard Shopify and Odoo, which "
     "connector and plan to use, what data moves, the risks, and a fixed fee for the next phase."),
    ("file-check-2", "Agreement and deposit", "before any work",
     "You sign a services agreement once, then a statement of work for each project with scope, "
     "exclusions, milestones and price. Work starts when the deposit clears."),
    ("key-round", "Access, the safe way", "week 1",
     "We ask for named staff or collaborator accounts with only the permissions the work needs, with "
     "two-factor sign-in. Never shared passwords, and never by email or chat."),
    ("server", "Build in staging", "most of the project",
     "Configuration and data loads happen in a staging copy or trial database first, with two trial "
     "data loads checked against record counts and totals that you sign off."),
    ("list-checks", "Testing with your team", "1–2 weeks",
     "Your staff run real scenarios against written acceptance criteria: an order, a refund, a "
     "partial shipment, a POS sale, a purchase receipt. Training is recorded."),
    ("package-check", "Go-live", "a planned date",
     "A backup first, a short freeze on changes, the cutover, then checks on live orders. Go-live dates "
     "avoid your peak season."),
    ("life-buoy", "After go-live", "2–4 weeks",
     "Fixes for anything that doesn't work as agreed, at no extra cost, for the period in your "
     "package. A support block covers changes after that."),
    ("shield-check", "Handover and access removed", "project close",
     "You get the as-built record, guides and an access register. We remove our access and confirm it "
     "in writing."),
]


def page_how():
    phases = [("Plan", "Agree what gets built and what it costs.", 0, 3),
              ("Build", "Set up and test in a copy of your systems.", 3, 6),
              ("Launch and hand over", "Go live, fix, then hand everything back.", 6, 9)]
    groups = []
    for n, (name, sub, a, b) in enumerate(phases, 1):
        items = "".join(f'<li><span class="ic-block">{spot(ic)}</span><div><span class="meta">Step {i + 1} · {e(t)}</span>'
                        f'<h4>{e(h)}</h4><p>{e(d)}</p></div></li>' for i, (ic, h, t, d) in list(enumerate(STEPS))[a:b])
        groups.append(f'<div class="phase"><div class="phase-h"><span class="phase-n">Phase {n}</span><h3>{e(name)}</h3>'
                      f'<p>{e(sub)}</p></div><ol class="timeline" start="{a + 1}">{items}</ol></div>')
    body = hero("How a Shopify or Odoo project runs, from first call to handover",
                "The same steps for every project, whatever its size. Each one ends with something written that "
                "you can check before the next begins.", eyebrow="How we work") + f"""
<section class="sec"><div class="wrap">{''.join(groups)}</div></section>
<section class="sec tint" aria-labelledby="docs-h"><div class="wrap">
  {sec_head("What each stage produces", "Samples of the documents you get. Every project's are written for it.",
            "docs-h")}
  <div class="paper-grid">
    <div>{M.sample_roadmap()}</div><div>{M.sample_fieldmap()}</div>
    <div>{M.sample_testlog()}</div><div>{M.sample_handover()}</div>
  </div>
</div></section>
<section class="sec"><div class="wrap split">
  <div><h2>Changes to scope</h2>
  <p>If you need something that isn't in your statement of work, we stop that part, send a written
  change order with the price and the effect on dates, and start it once you sign.</p></div>
  <div><h2>Your data and accounts</h2>
  <p>Your Shopify store, Odoo database and app accounts stay in your name and on your billing. We work
  read-only until the statement of work calls for changes. Tax and accounting settings follow written
  instructions from your accountant.</p></div>
</div></section>"""
    return {"path": "/how-it-works", "file": "how-it-works.html", "h": "How we work",
            "title": f"How a Shopify or Odoo project works | {NAME}",
            "desc": ("The steps of every project: a scoping call, a Systems Roadmap, a signed scope, a "
                     "staging build, testing with your team, go-live, support and access removed."),
            "body": body}


PRICING_FAQS = [
    ("Why ranges and not one price?",
     "Because the work depends on things we can only see in your setup, like product count and how clean your data "
     "is. Your exact fee is fixed in writing before work starts, and it doesn't change unless the scope does."),
    ("Can we pay in parts?",
     "Yes. Each project splits payment at milestones: the Systems Roadmap is paid at signing, a Store Move and a Back "
     "Office Launch are paid 40%, 40% and 20%, and a Sync is paid half at signing and half at go-live."),
    ("What if the scope changes mid-project?",
     "We pause that part and send a written change order with the price and the effect on dates. Nothing extra "
     "starts until you sign it."),
    ("Is the first call free?",
     "Yes. The scoping call is 30 minutes at no charge. You leave with a straight answer on whether we can help."),
]


def page_pricing():
    drivers = {
        "systems-roadmap": "How many systems you run today and how many working sessions the plan needs, up to three.",
        "store-move": "How many products you have, how much order history comes over, and how many apps the move replaces.",
        "odoo-launch": "How many users and locations, whether POS is in scope, and how clean your current data is.",
        "connection": "Which connector fits your plan, and how many stores and warehouses it links.",
    }
    cards = "".join(f"""
<div class="pr-card {SVC_COLOR[s]}">
  <span class="ic-block">{spot(SVC_SPOT[s])}</span>
  <h3><a href="{svc_href(s)}">{e(PKG[s]['name'])}</a></h3>
  <p class="price big">{price(*PKG[s]['price'])}</p>
  {facts([("Typical timeline", e(PKG[s]['timeline'])), ("Payment", e(PKG[s]['payment'].split('. ')[0].rstrip('.'))),
          ("What moves the price", e(drivers[s]))], "stack")}
</div>""" for s in ORDER)
    sup = C.SUPPORT
    sup_opts = "".join(f'<div class="opt-card"><b>{e(h)}</b><span class="price big">{price(k)}</span><em>{e(v)}</em></div>'
                       for h, k, v in sup["options"])
    body = hero("What a project costs, before you call us",
                "Every project is a fixed fee written into a statement of work. Under each range you'll see what "
                "moves a project toward the low or the high end.", eyebrow="Pricing") + f"""
<section class="sec"><div class="wrap">
  <h2 class="vh">Fixed fees by service</h2>
  <div class="pr-cards">{cards}</div>
  <p class="small">{e(C.LARGER_PROJECTS.format(larger_odoo_from=price("larger_odoo_from")))}</p>
</div></section>
<section class="sec tint"><div class="wrap split">
  <div><h2>{e(sup['name'])}</h2><p>{e(sup['summary'])}</p><div class="opt-cards">{sup_opts}</div>
  <p class="small">{e(sup['terms'])}</p></div>
  <div><h2>Software you pay for separately</h2>
  <p>Your Shopify plan and apps, your Odoo subscription and any Odoo.sh hosting, connector licenses, card processing
  and hardware are billed to you by each vendor. None of it is part of our fee, and every item is listed in your
  proposal.</p>
  <p>{more_link(svc_href("store-move") + "#plan-picker", "Which Shopify plan fits")}</p>
  <p class="small">{e(C.REFERRAL_DISCLOSURE.format(name=NAME))}</p>
  <p class="small">{e(C.SALES_TAX_LINE)}</p></div>
</div></section>
<section class="sec"><div class="wrap split">
  <div><h2>Pricing questions</h2>{qa_list(PRICING_FAQS)}</div>
  <div><h2>Choosing between services</h2>
  <p>Start with the free 30-minute scoping call. If the answer isn't clear by the end of it, a Systems Roadmap
  gives you a written plan and a fixed quote, and you keep the plan either way.</p>
  <p>{more_link(svc_href("systems-roadmap") + "#readiness", "Take the ERP readiness check")}</p></div>
</div></section>"""
    return {"path": "/pricing", "file": "pricing.html", "h": "Pricing",
            "title": f"Pricing for Shopify and Odoo projects | {NAME}",
            "desc": ("Fixed-fee ranges for a Systems Roadmap, a Shopify store move, an Odoo setup and a Shopify to Odoo "
                     "sync. Plus prepaid support hours and what decides your fee."),
            "body": body, "schema": [faq_schema(PRICING_FAQS)]}


def page_about():
    bio = "".join(f"<p>{e(p)}</p>" for p in C.ABOUT_BIO)
    if not bio:
        NOTES.append("ABOUT_BIO blank: the About page shows only the business facts")
    photo = (f'<img class="portrait" src="/{e(C.PHOTO)}" alt="{e(C.FOUNDER)}" width="320" height="400">'
             if C.PHOTO else "")
    values = [("file-check-2", "Written before it is done",
               "Scope, price, field maps, test cases and handover are all on paper you can check."),
              ("key-round", "Your accounts, your data",
               "Everything stays in your name and on your billing. We leave with nothing."),
              ("people", "One contact from call to handover",
               f"{C.FOUNDER} scopes the project, writes the statement of work and runs it."),
              ("clock", "US business hours",
               f"{C.PROMISES['business_days']}, {C.TIMEZONE_LABEL} time, with a reply {C.PROMISES['first_reply']}.")]
    vals = "".join(f'<li><span class="ic-block">{spot(ic)}</span><b>{e(h)}</b><span>{e(t)}</span></li>'
                   for ic, h, t in values)
    body = hero(f"About {NAME}",
                f"{e(NAME)} is an ecommerce and ERP consultancy based in {e(C.STATE)}. We plan, set up and connect "
                f"Shopify and Odoo for product businesses across the US, remotely, during {e(C.TIMEZONE_LABEL)} "
                f"business hours.", eyebrow="About", art=photo) + f"""
<section class="sec"><div class="wrap split">
  <div class="prose-s">{f'<h2>{e(C.FOUNDER)}</h2>{bio}' if bio else ''}
  <h2>How {e(NAME)} works</h2>
  <p>{e(C.FOUNDER)} scopes every project, writes the statement of work and is your contact from the
  first call to handover.</p>
  <p>We sell services only. Software, apps and hosting are billed to you by each vendor, so your
  accounts stay yours.</p>
  {facts([("Based in", f"{e(C.STATE)}, working remotely across the US"),
          ("Hours", f"{e(C.PROMISES['business_days'])}, {e(C.TIMEZONE_LABEL)} time"),
          ("Replies", e(C.PROMISES['first_reply']).capitalize()),
          ("Services", '<a href="/services">Five services, each with a written scope</a>')], "stack")}</div>
  <ul class="values">{vals}</ul>
</div></section>"""
    return {"path": "/about", "file": "about.html", "h": "About",
            "title": f"About {NAME}",
            "desc": (f"{NAME} is an ecommerce and ERP consultancy run by {C.FOUNDER} from {C.STATE}, setting up "
                     f"Shopify and Odoo for product businesses across the US."),
            "body": body}


def page_book():
    sec = secondary_contacts()
    if not (C.BOOKING_URL or C.EMAIL):
        NOTES.append("Book page: no scheduler or email yet, so the button points back to this page")
        cta = '<p class="note-box">The booking link goes here once the scheduler is set up.</p>'
    else:
        cta = primary_cta("book")
    agenda = [("First 5 minutes", "What you sell, where you sell it, and what runs your stock, orders and books today."),
              ("Next 15 minutes", "What isn't working, what it costs you each week, and what has to be live by when."),
              ("Last 10 minutes", "Which service fits, a rough price range, or whether a Systems Roadmap should come first.")]
    cov = "".join(f'<li><b>{e(h)}.</b> {e(t)}</li>' for h, t in agenda)
    ready = ["Your Shopify plan and the apps you rely on", "Your Odoo plan and hosting, if you have Odoo",
             "Rough counts: products, orders a month, locations", "Who keeps the books, and in what software"]
    body = hero("Book a scoping call about your store and back office",
                f"A {e(C.PROMISES['call_length'])} video call, {e(C.PROMISES['business_days'])}, "
                f"{e(C.TIMEZONE_LABEL)} time. There is no charge for the call.", eyebrow="Book a call",
                extra=f'<div class="cta-line">{cta}</div>{f"<p class=small>{sec}</p>" if sec else ""}') + f"""
<section class="sec"><div class="wrap split">
  <div><h2>How the 30 minutes go</h2><ol class="nums">{cov}</ol>
  <h2>What to have ready</h2>{ticks([e(x) for x in ready])}</div>
  <div><h2>What happens after</h2>
  <ol class="nums">
    <li>You get a proposal or a Roadmap quote {e(C.PROMISES['proposal_after_call'])}.</li>
    <li>If we are not the right fit, we tell you on the call and, where we can, suggest who is.</li>
    <li>Messages get a reply {e(C.PROMISES['first_reply'])}.</li>
  </ol>
  <p class="note-box">{icon('lock-keyhole')}<span>Please don't send passwords, API keys or customer data before or
  during the call. If a project goes ahead, access is set up the safe way in week one.</span></p></div>
</div></section>"""
    return {"path": "/book", "file": "book.html", "h": "Book a call",
            "title": f"Book a Shopify and Odoo scoping call | {NAME}",
            "desc": (f"Book a {C.PROMISES['call_length']} call about your Shopify, Shopify POS or Odoo setup. "
                     f"You get a proposal or Roadmap quote {C.PROMISES['proposal_after_call']}."),
            "body": body, "no_band": True}


def core_pages():
    svc = [page_service(p) for p in C.PACKAGES] + [page_support()]
    return ([page_home(), page_services()] + svc + [page_industries()] +
            [page_industry(x) for x in I.INDUSTRIES] + [page_how(), page_pricing(), page_about(), page_book()])
