"""Animated product illustrations for the [DBA name] site.

Every screen here is an HTML illustration of a typical setup, drawn by us, with sample data.
None is a screenshot of a client system. Each one carries a visible "Sample data, not a client"
label (03 Imagery). Animation is CSS and a small script in site.js; with reduced motion the final
state shows and nothing moves.
"""

SAMPLE = '<span class="tag">Sample data, not a client</span>'


def win(cls, app, title, body, tabs=None):
    t = ""
    if tabs:
        t = '<div class="w-tabs">' + "".join(
            f'<span{" class=\"on\"" if i == 0 else ""}>{x}</span>' for i, x in enumerate(tabs)) + "</div>"
    return (f'<div class="win {cls}"><div class="w-bar"><i></i><i></i><i></i>'
            f'<span class="w-app">{app}</span><span class="w-title">{title}</span></div>{t}'
            f'<div class="w-body">{body}</div></div>')


def hero_stage():
    pos = win("w-shop", "Shopify POS", "Store 2 · Register 1", """
<ul class="cart">
  <li><span>Linen throw, grey</span><span class="q">×1</span><span class="m">$68.00</span></li>
  <li><span>Stoneware mug set</span><span class="q">×2</span><span class="m">$48.00</span></li>
  <li><span>Beeswax candle</span><span class="q">×1</span><span class="m">$22.00</span></li>
</ul>
<div class="cart-total"><span>Total</span><span class="m">$148.92</span></div>
<div class="paid" data-step="1"><span class="dot"></span>Paid · Order #1042</div>
""")
    odoo = win("w-odoo", "Odoo", "Inventory · Products", """
<table class="stock">
  <thead><tr><th>Product</th><th>On hand</th><th>Forecast</th></tr></thead>
  <tbody>
    <tr class="hit" data-step="3"><td>Linen throw, grey</td><td><span class="flip" data-from="24" data-to="23">24</span></td><td>41</td></tr>
    <tr class="hit" data-step="3"><td>Stoneware mug set</td><td><span class="flip" data-from="57" data-to="55">57</span></td><td>55</td></tr>
    <tr class="hit" data-step="3"><td>Beeswax candle</td><td><span class="flip" data-from="9" data-to="8">9</span></td><td>32</td></tr>
  </tbody>
</table>
<div class="so" data-step="2"><span class="chip">S00187</span> Sale order confirmed, delivery WH/OUT/00412 done</div>
""", tabs=["Inventory", "Sales", "Purchase", "Accounting"])
    log = """
<div class="log" aria-hidden="true">
  <p data-step="1"><b>10:42:07</b> order #1042 created in Shopify POS, Store 2</p>
  <p data-step="2"><b>10:42:09</b> sale order S00187 created and confirmed in Odoo</p>
  <p data-step="3"><b>10:42:10</b> WH/Stock: 3 products updated</p>
  <p data-step="4"><b>10:42:12</b> stock levels pushed to Shopify, 2 locations</p>
  <p data-step="5"><b>10:42:13</b> invoice INV/2026/00412 posted, payment reconciled</p>
</div>"""
    return f"""
<figure class="stage" data-stage data-times="200,1700,2300,3700,4600" aria-labelledby="stage-cap">
  <div class="stage-grid">
    {pos}
    <div class="pipe" aria-hidden="true"><span class="pk"></span><span class="pk back"></span>
      <em class="pipe-l">orders →</em><em class="pipe-r">← stock</em></div>
    {odoo}
  </div>
  {log}
  <figcaption id="stage-cap">{SAMPLE} An in-store sale reaching Odoo, and the new stock count going back to
  Shopify. Illustration of a typical connector setup.</figcaption>
</figure>"""


# --- Small per-service illustrations -------------------------------------------------------------

def mini_roadmap():
    items = ["Systems and data inventory", "Fit against standard features", "Connector and plan choice",
             "Risks and open questions", "Fixed quote for the next phase"]
    lis = "".join(f'<li style="--i:{i}">{x}</li>' for i, x in enumerate(items))
    return f'<div class="mini mini-road" aria-hidden="true"><div class="doc"><b>Systems Roadmap</b><ul>{lis}</ul></div></div>'


def mini_move():
    rows = [("Products", "1,240"), ("Customers", "3,815"), ("Orders", "9,402"), ("Redirects", "312")]
    r = "".join(f'<div class="mv" style="--i:{i}"><span>{a}</span><span class="bar"><i></i></span>'
                f'<span class="n">{b}</span></div>' for i, (a, b) in enumerate(rows))
    return (f'<div class="mini mini-move" aria-hidden="true"><div class="mv-head"><span>WooCommerce</span>'
            f'<span class="arr">→</span><span>Shopify</span></div>{r}</div>')


def mini_launch():
    apps = ["Sales", "Inventory", "Purchase", "Invoicing", "Accounting", "POS"]
    t = "".join(f'<span style="--i:{i}"><i></i>{a}</span>' for i, a in enumerate(apps))
    return f'<div class="mini mini-launch" aria-hidden="true">{t}</div>'


def mini_sync():
    return ('<div class="mini mini-sync" aria-hidden="true"><span class="node">Shopify</span>'
            '<span class="wire"><i></i><i class="b"></i></span><span class="node o">Odoo</span>'
            '<div class="sync-lines"><span>orders, refunds →</span><span>← stock, tracking</span></div></div>')


def mini_support():
    t = [("Add a user for the new store", "Done"), ("Report: margin by vendor", "In progress"),
         ("Barcode printer setup", "Open")]
    r = "".join(f'<li style="--i:{i}"><span>{a}</span><em class="st st{i}">{s}</em></li>' for i, (a, s) in enumerate(t))
    return f'<div class="mini mini-sup" aria-hidden="true"><ul>{r}</ul></div>'


MINIS = {
    "systems-roadmap": mini_roadmap,
    "store-move": mini_move,
    "odoo-launch": mini_launch,
    "connection": mini_sync,
    "support": mini_support,
}


def stock_showcase():
    """Purchase receipt in Odoo raises on-hand stock, and both Shopify locations update."""
    odoo = win("w-odoo", "Odoo", "Linen throw, grey", """
<div class="pf">
  <div class="pf-k"><span>On hand</span><b class="flip" data-at="1" data-from="23" data-to="41">23</b></div>
  <div class="pf-k"><span>Forecasted</span><b>41</b></div>
  <div class="pf-k"><span>Reordering rule</span><b>min 10 · max 40</b></div>
</div>
<div class="receipt" data-step="1"><span class="chip">WH/IN/00031</span> Receipt validated: 18 units from P00031</div>
<div class="bars" aria-hidden="true">
  <div><span>WH/Stock</span><i style="--w:58%" data-step="2"></i></div>
  <div><span>Store 1</span><i style="--w:30%"></i></div>
  <div><span>Store 2</span><i style="--w:27%"></i></div>
</div>""", tabs=["Inventory", "Purchase", "Sales"])
    shop = win("w-shop", "Shopify admin", "Products · Linen throw, grey", """
<table class="stock">
  <thead><tr><th>Location</th><th>Available</th></tr></thead>
  <tbody>
    <tr class="hit" data-step="3"><td>Online store (WH/Stock)</td><td><span class="flip" data-from="0" data-to="18">0</span></td></tr>
    <tr><td>Store 1</td><td>12</td></tr>
    <tr><td>Store 2</td><td>11</td></tr>
  </tbody>
</table>
<div class="paid" data-step="3"><span class="dot"></span>Back in stock online</div>""")
    return f"""
<figure class="stage show2" data-stage data-times="500,1300,2300" aria-labelledby="show-cap">
  <div class="stage-grid two-win">{odoo}<div class="pipe v" aria-hidden="true"><span class="pk back"></span><em class="pipe-r">stock →</em></div>{shop}</div>
  <figcaption id="show-cap">{SAMPLE} A purchase receipt in Odoo puts an out-of-stock product back on sale online.
  Illustration of a typical setup.</figcaption>
</figure>"""
