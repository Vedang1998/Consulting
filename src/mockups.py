"""Product demos, sample documents, illustrations and icons for the [DBA name] site.

Every screen here is an HTML illustration of a typical setup, drawn by us, with sample data.
None is a screenshot of a client system, and no platform logo is used. Each demo carries a visible
"Sample data, not a client" label (03 Imagery). Motion is CSS plus a small sequencer in site.js;
with reduced motion the final state shows and nothing moves.

Real recordings: set a file name in config.DEMO_VIDEOS for a workflow and that tab plays the
recording instead of the drawn demo (see 04-Website-Guide, shot list).
"""

import re
from pathlib import Path

ICONS = Path(__file__).resolve().parent / "icons"
SAMPLE = '<span class="tag">Sample data, not a client</span>'
_icon_cache = {}


def icon(name, cls=""):
    """Inline a Lucide icon (ISC licence, src/icons/). 1.5px stroke per the brand guide."""
    if name not in _icon_cache:
        svg = (ICONS / f"{name}.svg").read_text()
        svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
        inner = re.search(r"<svg[^>]*>(.*)</svg>", svg, flags=re.S).group(1)
        _icon_cache[name] = re.sub(r"\s+", " ", inner).strip()
    c = f"ic {cls}".strip()
    return (f'<svg class="{c}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_icon_cache[name]}</svg>')


# ---------------------------------------------------------------------------
# App windows
# ---------------------------------------------------------------------------

def _bar(url):
    return f'<div class="w-bar"><i></i><i></i><i></i><span class="w-url">{icon("lock-keyhole")}{url}</span></div>'


def shop_win(url, title, body, rail_on=1):
    rail = ["home", "inbox", "tag", "users", "chart-column", "settings"]
    r = "".join(f'<span{" class=\"on\"" if i == rail_on else ""}>{icon(n)}</span>' for i, n in enumerate(rail))
    return (f'<div class="win w-shop">{_bar(url)}<div class="w-main"><div class="w-rail">{r}</div>'
            f'<div class="w-body"><div class="w-h"><span class="w-app">Shopify</span><b>{title}</b></div>{body}</div></div></div>')


def odoo_win(url, app, menu, crumb, body):
    m = "".join(f"<span>{x}</span>" for x in menu)
    return (f'<div class="win w-odoo">{_bar(url)}<div class="w-nav"><b>{icon("layers")}{app}</b>{m}</div>'
            f'<div class="w-body"><div class="w-h"><span class="w-app">Odoo</span><b>{crumb}</b></div>{body}</div></div>')


def statusbar(stages, steps):
    """stages: labels; steps: for each stage, the step at which it becomes current (0 = from the start)."""
    out = []
    for lab, st in zip(stages, steps):
        attr = f' data-step="{st}"' if st else ' class="on"'
        out.append(f"<span{attr}>{lab}</span>")
    return f'<div class="sbar">{"".join(out)}</div>'


def thumb(c):
    return f'<i class="th th{c}"></i>'


def _log(lines):
    ps = "".join(f'<p data-step="{i + 1}"><b>{t}</b>{x}</p>' for i, (t, x) in enumerate(lines))
    return f'<div class="log" aria-hidden="true"><div class="log-h">{icon("refresh-cw")}Sync log</div>{ps}</div>'


def _stage(key, times, left, right, pulses, log, caption):
    pk = "".join(f'<span class="pk {d}" data-step="{s}"></span>' for d, s in pulses)
    return f"""
<figure class="stage" data-stage data-times="{times}" aria-labelledby="cap-{key}">
  <div class="stage-grid">{left}
    <div class="pipe" aria-hidden="true">{pk}<em>connector</em></div>
  {right}</div>
  {_log(log)}
  <figcaption id="cap-{key}">{SAMPLE} {caption}</figcaption>
</figure>"""


def demo_pos_sale():
    left = shop_win("pos.demo-store · Store 2 · Register 1", "Point of sale", f"""
<ul class="cart">
  <li>{thumb(1)}<span>Linen throw, grey</span><span class="q">×1</span><span class="m">$68.00</span></li>
  <li>{thumb(2)}<span>Stoneware mug set</span><span class="q">×2</span><span class="m">$48.00</span></li>
  <li>{thumb(3)}<span>Beeswax candle</span><span class="q">×1</span><span class="m">$22.00</span></li>
</ul>
<div class="cart-total"><span>Total with tax</span><span class="m">$148.92</span></div>
<div class="note ok" data-step="1">{icon("circle-check")}Paid by card · Order #1042</div>""", rail_on=2)
    right = odoo_win("demo-company.odoo.com/odoo/inventory", "Inventory", ["Overview", "Operations", "Products", "Reporting"],
                     "Products", f"""
<table class="grid">
  <thead><tr><th>Product</th><th>On hand</th><th>Forecast</th></tr></thead>
  <tbody>
    <tr class="hit" data-step="3"><td>{thumb(1)}Linen throw, grey</td><td><span class="flip" data-from="24" data-to="23">24</span></td><td>41</td></tr>
    <tr class="hit" data-step="3"><td>{thumb(2)}Stoneware mug set</td><td><span class="flip" data-from="57" data-to="55">57</span></td><td>55</td></tr>
    <tr class="hit" data-step="3"><td>{thumb(3)}Beeswax candle</td><td><span class="flip" data-from="9" data-to="8">9</span></td><td>32</td></tr>
  </tbody>
</table>
<div class="note od" data-step="2"><span class="chip">S00187</span>Sale order confirmed, delivery done</div>""")
    log = [("10:42:07", "order #1042 created in Shopify POS, Store 2"),
           ("10:42:09", "sale order S00187 created and confirmed in Odoo"),
           ("10:42:10", "WH/Stock: 3 products updated"),
           ("10:42:12", "stock levels pushed to Shopify, 2 locations"),
           ("10:42:13", "invoice INV/2026/00412 posted, payment reconciled")]
    return _stage("pos", "500,1800,2600,4000,4900", left, right, [("lr", 2), ("rl", 4)], log,
                  "A sale at the counter reaches Odoo, and the new stock count goes back to both Shopify locations.")


def demo_online_order():
    left = shop_win("admin.shopify.com/store/demo-store/orders/1043", "Order #1043", f"""
<div class="badges"><span class="bdg ok">Paid</span>
  <span class="bdg swap"><span class="a">Unfulfilled</span><span class="b ok" data-step="4">Fulfilled</span></span></div>
<ul class="cart">
  <li>{thumb(4)}<span>Oak serving board</span><span class="q">×1</span><span class="m">$54.00</span></li>
  <li>{thumb(2)}<span>Stoneware mug set</span><span class="q">×1</span><span class="m">$24.00</span></li>
</ul>
<dl class="kv"><div><dt>Ship to</dt><dd>Sample customer, Columbus, OH</dd></div>
<div data-step="4"><dt>Tracking</dt><dd class="m">1Z999AA10123456784</dd></div></dl>""")
    right = odoo_win("demo-company.odoo.com/odoo/inventory/delivery", "Inventory", ["Overview", "Operations", "Products"],
                     "Delivery orders / WH/OUT/00413", f"""
{statusbar(["Draft", "Ready", "Done"], [0, 2, 3])}
<table class="grid">
  <thead><tr><th>Product</th><th>Demand</th><th>Done</th></tr></thead>
  <tbody>
    <tr class="hit" data-step="3"><td>{thumb(4)}Oak serving board</td><td>1</td><td><span class="flip" data-from="0" data-to="1">0</span></td></tr>
    <tr class="hit" data-step="3"><td>{thumb(2)}Stoneware mug set</td><td>1</td><td><span class="flip" data-from="0" data-to="1">0</span></td></tr>
  </tbody>
</table>
<div class="note od" data-step="3"><span class="chip">UPS Ground</span>Label printed, tracking number saved</div>""")
    log = [("14:05:31", "order #1043 placed on the online store"),
           ("14:05:33", "sale order S00188 and delivery WH/OUT/00413 created in Odoo"),
           ("15:20:04", "delivery picked, packed and validated in the warehouse"),
           ("15:20:06", "tracking number sent to Shopify, order marked fulfilled"),
           ("15:20:07", "Shopify emails the customer the shipping update")]
    return _stage("web", "500,1700,3000,4300,5200", left, right, [("lr", 2), ("rl", 4)], log,
                  "An online order is picked in Odoo, and the tracking number lands on the Shopify order.")


def demo_receipt():
    left = shop_win("admin.shopify.com/store/demo-store/products", "Linen throw, grey", f"""
<div class="badges"><span class="bdg swap"><span class="a warn">Sold out online</span><span class="b ok" data-step="3">In stock</span></span></div>
<table class="grid">
  <thead><tr><th>Location</th><th>Available</th></tr></thead>
  <tbody>
    <tr class="hit" data-step="3"><td>Warehouse (ships online orders)</td><td><span class="flip" data-from="0" data-to="18">0</span></td></tr>
    <tr><td>Store 1</td><td>12</td></tr>
    <tr><td>Store 2</td><td>11</td></tr>
  </tbody>
</table>""", rail_on=2)
    right = odoo_win("demo-company.odoo.com/odoo/purchase", "Purchase", ["Orders", "Products", "Reporting"],
                     "Purchase orders / P00031", f"""
{statusbar(["RFQ", "Purchase order", "Received"], [0, 0, 1])}
<dl class="kv"><div><dt>Vendor</dt><dd>Northfield Textiles (sample)</dd></div></dl>
<table class="grid">
  <thead><tr><th>Product</th><th>Ordered</th><th>Received</th></tr></thead>
  <tbody><tr class="hit" data-step="1"><td>{thumb(1)}Linen throw, grey</td><td>18</td><td><span class="flip" data-from="0" data-to="18">0</span></td></tr></tbody>
</table>
<div class="note od" data-step="2"><span class="chip">WH/IN/00031</span>Receipt validated, vendor bill drafted</div>""")
    log = [("09:12:40", "receipt WH/IN/00031 validated in Odoo: 18 units"),
           ("09:12:41", "WH/Stock on hand 0 to 18, draft vendor bill created"),
           ("09:12:44", "available quantity pushed to Shopify, Warehouse location"),
           ("09:12:45", "product back on sale on the online store")]
    return _stage("po", "600,1600,2900,3800", left, right, [("rl", 3)], log,
                  "Receiving a purchase order in Odoo puts a sold-out product back on sale online.")


def demo_refund():
    left = shop_win("admin.shopify.com/store/demo-store/orders/1039", "Order #1039 · Refund", f"""
<div class="badges"><span class="bdg swap"><span class="a ok">Paid</span><span class="b warn" data-step="1">Partially refunded</span></span></div>
<ul class="cart">
  <li>{thumb(2)}<span>Stoneware mug set</span><span class="q">×1</span><span class="m">$24.00</span></li>
</ul>
<dl class="kv"><div><dt>Restock at</dt><dd>Store 1</dd></div>
<div><dt>Refund to card</dt><dd class="m">$25.92</dd></div></dl>
<div class="note ok" data-step="1">{icon("undo-2")}Refund issued</div>""")
    right = odoo_win("demo-company.odoo.com/odoo/accounting", "Accounting", ["Customers", "Vendors", "Reporting"],
                     "Credit notes / RINV/2026/00007", f"""
{statusbar(["Draft", "Posted", "Paid"], [0, 2, 3])}
<table class="grid">
  <thead><tr><th>Line</th><th>Qty</th><th>Amount</th></tr></thead>
  <tbody><tr class="hit" data-step="2"><td>{thumb(2)}Stoneware mug set</td><td>1</td><td>$24.00</td></tr></tbody>
</table>
<dl class="kv"><div class="hitrow" data-step="4"><dt>Store 1 on hand</dt><dd class="m"><span class="flip" data-at="4" data-from="12" data-to="13">12</span></dd></div></dl>
<div class="note od" data-step="4"><span class="chip">WH/IN/00032</span>Return received into Store 1</div>""")
    log = [("11:30:15", "refund issued on order #1039 in Shopify, 1 item, restock on"),
           ("11:30:17", "credit note RINV/2026/00007 posted in Odoo"),
           ("11:30:18", "refund payment matched to the credit note"),
           ("11:30:19", "return WH/IN/00032 validated, Store 1 on hand 12 to 13")]
    return _stage("ref", "500,1700,2600,3600", left, right, [("lr", 2)], log,
                  "A refund in Shopify becomes a credit note and a stock return in Odoo, with nothing typed twice.")


DEMOS = [
    ("pos-sale", "In-store sale", "store", demo_pos_sale),
    ("online-order", "Online order shipped", "truck", demo_online_order),
    ("purchase-receipt", "Purchase receipt", "package-check", demo_receipt),
    ("refund", "Refund and return", "undo-2", demo_refund),
]


def demo_tabs(videos=None):
    """The four workflows as a tabbed, auto-advancing demo."""
    videos = videos or {}
    tabs, panels = [], []
    for i, (key, label, ic, fn) in enumerate(DEMOS):
        sel = "true" if i == 0 else "false"
        tabs.append(f'<button type="button" role="tab" id="tab-{key}" aria-controls="panel-{key}" aria-selected="{sel}" '
                    f'data-demo="{key}"{"" if i == 0 else " tabindex=\"-1\""}>{icon(ic)}<span>{label}</span><i class="tab-prog"></i></button>')
        if videos.get(key):
            inner = (f'<figure class="stage"><video class="demo-video" src="/{videos[key]}" muted playsinline loop '
                     f'preload="none" controls></video><figcaption>Recorded in our demo store and demo database. '
                     f'{SAMPLE}</figcaption></figure>')
        else:
            inner = fn()
        panels.append(f'<div role="tabpanel" id="panel-{key}" aria-labelledby="tab-{key}"{"" if i == 0 else " hidden"}>{inner}</div>')
    return (f'<div class="demo" data-demo-root><div class="demo-tabs" role="tablist" aria-label="Workflows">'
            f'{"".join(tabs)}</div><div class="demo-frame">{"".join(panels)}</div></div>')


# ---------------------------------------------------------------------------
# Small per-service illustrations
# ---------------------------------------------------------------------------

def mini_roadmap():
    items = ["Systems and data inventory", "Fit against standard features", "Connector and plan choice",
             "Risks and open questions", "Fixed quote for the next phase"]
    lis = "".join(f'<li data-i="{i}">{x}</li>' for i, x in enumerate(items))
    return f'<div class="mini mini-road" aria-hidden="true"><div class="doc"><b>Systems Roadmap</b><ul>{lis}</ul></div></div>'


def mini_move():
    rows = [("Products", "1,240"), ("Customers", "3,815"), ("Orders", "9,402"), ("Redirects", "312")]
    r = "".join(f'<div class="mv" data-i="{i}"><span>{a}</span><span class="bar"><i></i></span>'
                f'<span class="n">{b}</span></div>' for i, (a, b) in enumerate(rows))
    return (f'<div class="mini mini-move" aria-hidden="true"><div class="mv-head"><span>WooCommerce</span>'
            f'{icon("arrow-right")}<span>Shopify</span></div>{r}</div>')


def mini_launch():
    apps = [("Sales", "badge-dollar-sign"), ("Inventory", "boxes"), ("Purchase", "clipboard-list"),
            ("Invoicing", "receipt"), ("Accounting", "landmark"), ("POS", "scan-barcode")]
    t = "".join(f'<span data-i="{i}"><i>{icon(ic)}</i>{a}</span>' for i, (a, ic) in enumerate(apps))
    return f'<div class="mini mini-launch" aria-hidden="true">{t}</div>'


def mini_sync():
    return ('<div class="mini mini-sync" aria-hidden="true"><span class="node">Shopify</span>'
            '<span class="wire"><i></i><i class="b"></i></span><span class="node o">Odoo</span>'
            '<div class="sync-lines"><span>orders, refunds →</span><span>← stock, tracking</span></div></div>')


def mini_support():
    t = [("Add a user for the new store", "Done"), ("Report: margin by vendor", "In progress"),
         ("Barcode printer setup", "Open")]
    r = "".join(f'<li data-i="{i}"><span>{a}</span><em class="st st{i}">{s}</em></li>' for i, (a, s) in enumerate(t))
    return f'<div class="mini mini-sup" aria-hidden="true"><ul>{r}</ul></div>'


MINIS = {"systems-roadmap": mini_roadmap, "store-move": mini_move, "odoo-launch": mini_launch,
         "connection": mini_sync, "support": mini_support}


# ---------------------------------------------------------------------------
# Sample deliverables (document mockups)
# ---------------------------------------------------------------------------

def _paper(title, sub, body, cls=""):
    return (f'<div class="paper {cls}"><div class="paper-h"><b>{title}</b><span>{sub}</span>'
            f'<span class="tag">Sample</span></div>{body}</div>')


def sample_roadmap():
    toc = [("1", "How orders, stock and money move today", "2"), ("2", "Systems and data inventory", "4"),
           ("3", "Fit against standard Shopify and Odoo", "6"), ("4", "Connector options and plan check", "8"),
           ("5", "Data to move, and data to leave behind", "10"), ("6", "Risks and open questions", "11"),
           ("7", "Phases, fixed fee and timeline", "12")]
    rows = "".join(f"<li><span>{n}</span><span>{t}</span><i></i><span>{p}</span></li>" for n, t, p in toc)
    return _paper("Systems Roadmap", "Contents", f'<ol class="toc">{rows}</ol>')


def sample_fieldmap():
    rows = [("variant.sku", "product.product.default_code", "match key"),
            ("order.line_items", "sale.order.line", "Shopify → Odoo"),
            ("inventory_level.available", "stock.quant (available)", "Odoo → Shopify"),
            ("fulfillment.tracking_number", "stock.picking.carrier_tracking_ref", "Odoo → Shopify"),
            ("refund.refund_line_items", "account.move (credit note)", "Shopify → Odoo")]
    body = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows)
    return _paper("Field map", "Signed before any data moves",
                  f'<table class="fmap"><thead><tr><th>Shopify</th><th>Odoo</th><th>Direction</th></tr></thead><tbody>{body}</tbody></table>',
                  "wide")


def sample_testlog():
    rows = ["New online order", "Partial fulfillment", "Refund with restock", "Out-of-stock item", "POS sale, second location"]
    body = "".join(f'<li><span>{x}</span><em class="st st0">Pass</em></li>' for x in rows)
    return _paper("Test log", "Run with your team before go-live", f'<ul class="tlog">{body}</ul>')


def sample_handover():
    rows = ["As-built configuration record", "Admin runbook", "User guides and recorded training",
            "Access register", "Our access removed, confirmed in writing"]
    body = "".join(f"<li>{icon('check')}<span>{x}</span></li>" for x in rows)
    return _paper("Handover pack", "Yours at project close", f'<ul class="hand">{body}</ul>')


# ---------------------------------------------------------------------------
# Illustrations: flat geometric scenes in the brand colors. Objects only, no people.
# ---------------------------------------------------------------------------

def scene_flow():
    """Storefront, warehouse shelves and a ledger, joined by one dashed path."""
    return """
<svg class="scene" viewBox="0 0 640 300" role="img" aria-label="Illustration: a storefront, warehouse shelves and a ledger joined by one path">
  <g class="deco">
    <circle cx="52" cy="46" r="26" class="f-yellow"/>
    <path d="M118 34 q10 -14 20 0 t20 0 t20 0" class="s-blue" fill="none"/>
    <g class="f-blue"><circle cx="300" cy="28" r="3"/><circle cx="316" cy="28" r="3"/><circle cx="332" cy="28" r="3"/><circle cx="300" cy="44" r="3"/><circle cx="316" cy="44" r="3"/><circle cx="332" cy="44" r="3"/></g>
    <path d="M560 30 l34 0 l-17 30 z" class="f-blue-soft"/>
    <path d="M600 250 a26 26 0 0 1 -52 0" class="f-yellow"/>
    <path d="M34 262 h18 M43 253 v18" class="s-ink"/>
    <path d="M410 266 q10 -14 20 0 t20 0" class="s-yellow" fill="none"/>
  </g>
  <path class="route" d="M150 196 C 210 120, 250 250, 320 190 S 440 110, 500 176" fill="none"/>
  <g class="shop">
    <rect x="58" y="136" width="130" height="110" rx="4" class="f-surface s-ink"/>
    <path d="M50 136 h146 l-12 -34 h-122 z" class="f-ink"/>
    <path d="M62 136 v14 a12 12 0 0 0 24 0 v-14 z M110 136 v14 a12 12 0 0 0 24 0 v-14 z M158 136 v14 a12 12 0 0 0 24 0 v-14 z" class="f-yellow"/>
    <path d="M86 136 v14 a12 12 0 0 0 24 0 v-14 z M134 136 v14 a12 12 0 0 0 24 0 v-14 z" class="f-surface s-ink"/>
    <rect x="72" y="178" width="46" height="40" rx="2" class="f-blue-soft s-ink"/>
    <rect x="134" y="178" width="38" height="68" rx="2" class="f-blue"/>
    <circle cx="142" cy="214" r="3" class="f-yellow"/>
  </g>
  <g class="shelves">
    <rect x="262" y="96" width="120" height="150" rx="4" class="f-surface s-ink"/>
    <path d="M262 146 h120 M262 196 h120" class="s-ink"/>
    <rect x="274" y="112" width="30" height="34" class="f-yellow s-ink"/><rect x="310" y="120" width="26" height="26" class="f-blue"/><rect x="342" y="108" width="30" height="38" class="f-blue-soft s-ink"/>
    <rect x="276" y="166" width="38" height="30" class="f-blue"/><rect x="322" y="160" width="26" height="36" class="f-yellow s-ink"/>
    <rect x="274" y="212" width="28" height="34" class="f-blue-soft s-ink"/><rect x="308" y="218" width="34" height="28" class="f-yellow s-ink"/><rect x="348" y="208" width="24" height="38" class="f-blue"/>
  </g>
  <g class="ledger">
    <rect x="462" y="110" width="118" height="136" rx="6" class="f-surface s-ink"/>
    <rect x="462" y="110" width="118" height="26" rx="6" class="f-ink"/>
    <path d="M478 156 h52 M478 172 h86 M478 188 h70" class="s-muted"/>
    <rect x="478" y="206" width="14" height="26" class="f-blue-soft"/><rect x="498" y="198" width="14" height="34" class="f-blue"/><rect x="518" y="212" width="14" height="20" class="f-blue-soft"/><rect x="538" y="192" width="14" height="40" class="f-yellow"/>
    <circle cx="566" cy="150" r="13" class="f-yellow"/><path d="M560 150 l4 4 l8 -9" class="s-ink" fill="none"/>
  </g>
  <g class="dots"><circle cx="150" cy="196" r="6"/><circle cx="320" cy="190" r="6"/><circle cx="500" cy="176" r="6"/></g>
</svg>"""


def blob(kind):
    """Loose shapes behind a problem-card icon."""
    shapes = {
        0: '<circle cx="40" cy="40" r="30" class="f-yellow"/><path d="M58 14 q8 -10 16 0 t16 0" class="s-blue" fill="none"/>',
        1: '<rect x="12" y="14" width="54" height="54" rx="10" class="f-blue-soft"/><circle cx="76" cy="62" r="9" class="f-yellow"/>',
        2: '<path d="M10 66 l32 -54 l32 54 z" class="f-blue-soft"/><g class="f-blue"><circle cx="72" cy="18" r="3"/><circle cx="84" cy="18" r="3"/><circle cx="72" cy="30" r="3"/><circle cx="84" cy="30" r="3"/></g>',
        3: '<path d="M14 54 a30 30 0 0 1 60 0 z" class="f-yellow"/><path d="M62 66 h18 M71 57 v18" class="s-blue"/>',
    }
    return f'<svg class="blob" viewBox="0 0 96 80" aria-hidden="true">{shapes[kind]}</svg>'


def deco(kind):
    """Loose background shapes for the dark hero."""
    shapes = {
        "hero-l": ('<circle cx="60" cy="70" r="34" class="f-yellow"/>'
                   '<path d="M20 150 q12 -16 24 0 t24 0 t24 0 t24 0" class="s-blue" fill="none"/>'
                   '<g class="f-soft"><circle cx="130" cy="30" r="3"/><circle cx="146" cy="30" r="3"/><circle cx="162" cy="30" r="3"/>'
                   '<circle cx="130" cy="46" r="3"/><circle cx="146" cy="46" r="3"/><circle cx="162" cy="46" r="3"/></g>'),
        "hero-r": ('<path d="M40 30 l70 0 l-35 60 z" class="f-blue"/>'
                   '<path d="M150 160 a34 34 0 0 1 -68 0" class="f-yellow"/>'
                   '<path d="M130 60 h22 M141 49 v22" class="s-soft"/>'
                   '<rect x="20" y="120" width="34" height="34" rx="6" class="s-blue" fill="none"/>'),
    }
    return f'<svg class="deco-svg {kind}" viewBox="0 0 180 200" aria-hidden="true">{shapes[kind]}</svg>'
