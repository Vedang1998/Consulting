"""Hero art drawn for this site in SVG: one diagram per page, built from that page's own content.

Nov 13, 2026: Vee turned down people illustrations of every kind. These replace them: no people, no stock art, no AI.
Each diagram sits on a dark dot-grid canvas inside the navy hero, with white cards, the custom spot icons (spot.py)
and the brand colors. Numbers come from the sample data in our demo systems (the same records the page's real
screens and clips show) or from the page's copy, never from a client.

Inline SVG, so text uses the site's fonts and stays sharp. CSP is style-src 'self': presentation attributes and the
.art classes in site.css only, no style attributes. Each diagram has role="img" and an aria-label that says what
it shows.
"""
import html
import math

import spot as S

INK = "#0e1a2e"; MUTED = "#5b6577"; EDGE = "#dbe0e8"; TINT = "#f3f5f9"; WHITE = "#ffffff"
CANVAS = "#16243d"; GRID = "#2b3a57"; ON_DARK = "#eef2f8"; ON_DARK_MUTED = "#aeb9cc"
# family: (deep, for text and bars on white; bright, for marks on the dark canvas; soft tint)
FAM = {"blue": ("#2447d8", "#6d8bff", "#e6ecff"), "coral": ("#d9472b", "#ff7a59", "#fde9e4"),
       "mint": ("#0b7d62", "#34c79a", "#def4ec"), "lilac": ("#6a4fd8", "#a08cff", "#ece8ff"),
       "yellow": ("#8a6100", "#ffc53d", "#fff4d6")}
W, H = 600, 480


def esc(s):
    return html.escape(str(s), quote=True)


def n(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def T(x, y, s, size=14, weight=400, fill=INK, font="b", anchor="start", spacing=None, extra=""):
    """Text. font: h = Archivo, b = IBM Plex Sans, m = IBM Plex Mono."""
    ls = f' letter-spacing="{spacing}"' if spacing is not None else ""
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    return (f'<text class="a{font}" x="{n(x)}" y="{n(y)}" font-size="{size}" font-weight="{weight}" fill="{fill}"{a}{ls}'
            f'{extra}>{esc(s)}</text>')


def lines(x, y, rows, size=14, lead=1.4, **kw):
    """Several lines of text, one per row, wrapped by hand so nothing overflows."""
    return "".join(T(x, y + i * size * lead, r, size, **kw) for i, r in enumerate(rows))


def mono(x, y, s, fill=MUTED, size=10, anchor="start", weight=500):
    return T(x, y, s, size, weight, fill, "m", anchor)


def R(x, y, w, h, rx=0, fill=WHITE, stroke=None, sw=1.5, extra=""):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="{n(rx)}" fill="{fill}"{st}{extra}/>'


def card(uid, x, y, w, h, rx=16, fill=WHITE):
    return R(x, y, w, h, rx, fill, extra=f' filter="url(#sh-{uid})"')


def pill(x, y, label, fam, solid=False, anchor="start"):
    """A small status pill. y is the pill's vertical center."""
    deep, bright, soft = FAM[fam]
    w = 14 + len(label) * 6.6
    x0 = x - w if anchor == "end" else x
    bg, fg = (bright, INK) if solid else (soft, deep)
    return R(x0, y - 10, w, 20, 10, bg) + T(x0 + w / 2, y + 3.6, label, 10.5, 600, fg, "b", "middle")


def icon(name, x, y, size=36, ink=INK):
    """A custom spot icon (spot.py) at x, y, with its color block in the icon's own bright color."""
    col, _label, fills, inks = S.ICONS[name]
    block = FAM[col][1]
    body = (f'<g transform="translate(2.5 2.5)" fill="{block}">{"".join(fills)}</g>'
            f'<g fill="none" stroke="{ink}" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round">'
            f'{"".join(inks)}</g>').replace("#141c2b", ink)
    return f'<svg x="{n(x)}" y="{n(y)}" width="{size}" height="{size}" viewBox="0 0 48 48" overflow="visible">{body}</svg>'


def badge(x, y, name, r=22):
    """A spot icon in a white circle, for stations and nodes on the dark canvas."""
    s = r * 1.25
    return (f'<circle cx="{n(x)}" cy="{n(y)}" r="{r}" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>'
            + icon(name, x - s / 2, y - s / 2, s))


def arrow(d, color=FAM["blue"][1], dash=True, head=True, uid="", width=2.5):
    da = ' stroke-dasharray="6 7"' if dash else ""
    mk = f' marker-end="url(#ah-{uid})"' if head else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{da}{mk}/>'


def frame(uid, label, body, accent="blue"):
    """The dark dot-grid canvas every diagram sits on."""
    bright = FAM[accent][1]
    defs = (f'<defs><pattern id="dg-{uid}" width="24" height="24" patternUnits="userSpaceOnUse">'
            f'<circle cx="12" cy="12" r="1.3" fill="{GRID}"/></pattern>'
            f'<filter id="sh-{uid}" x="-20%" y="-20%" width="140%" height="160%">'
            f'<feDropShadow dx="0" dy="12" stdDeviation="14" flood-color="#000" flood-opacity=".38"/></filter>'
            f'<marker id="ah-{uid}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M1 1 L8 5 L1 9" fill="none" stroke="{bright}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></marker>'
            f'</defs>')
    return (f'<svg class="art" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(label)}" focusable="false">{defs}'
            f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="24" fill="{CANVAS}" stroke="{GRID}" stroke-width="1.5"/>'
            f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="24" fill="url(#dg-{uid})"/>{body}</svg>')


# ---------------------------------------------------------------------------
# Industries
# ---------------------------------------------------------------------------

def apparel():
    u = "ap"
    deep, bright, soft = FAM["coral"]
    b = ""
    chans = [("cart", "Online store", "Shopify", 92), ("register", "Shop counter", "Shopify POS", 206),
             ("pallet", "Wholesale", "B2B orders", 320)]
    b += mono(28, 72, "Sold through", ON_DARK_MUTED)
    join = (252, 188)
    for ic, name, sub, y in chans:
        b += arrow(f"M196 {y + 31} C232 {y + 31} 222 {join[1]} {join[0] - 6} {join[1]}", bright, uid=u, head=False)
    for ic, name, sub, y in chans:
        b += card(u, 28, y, 168, 62, 14) + icon(ic, 42, y + 13, 36)
        b += T(88, y + 29, name, 15, 700, INK, "h") + mono(88, y + 46, sub)
    # the stock card
    cx, cy, cw, ch = 252, 40, 320, 400
    b += card(u, cx, cy, cw, ch, 18)
    b += mono(cx + 22, cy + 34, "Stock on hand, all locations") + T(cx + 22, cy + 60, "Crew tee", 21, 750, INK, "h")
    b += pill(cx + cw - 22, cy + 52, "One count", "coral", anchor="end")
    sizes = ["XS", "S", "M", "L", "XL"]
    col0, cwid = cx + 98, 43
    rows = [("Navy", "#1f2f57", [4, 7, 1, 6, 3]), ("White", "#ffffff", [9, 12, 8, 10, 5]), ("Clay", "#c9785b", [2, 5, 4, 0, 2])]
    hy = cy + 104
    for i, s in enumerate(sizes):
        b += T(col0 + i * cwid + cwid / 2, hy, s, 11, 600, MUTED, "m", "middle")
    for r, (name, sw, vals) in enumerate(rows):
        y = cy + 122 + r * 50
        if r == 0:
            b += R(cx + 12, y - 4, cw - 24, 44, 12, FAM["yellow"][2])
        b += f'<circle cx="{n(cx + 30)}" cy="{n(y + 18)}" r="8" fill="{sw}" stroke="{INK}" stroke-width="1.5"/>'
        b += T(cx + 46, y + 23, name, 14, 500, INK)
        for i, v in enumerate(vals):
            x = col0 + i * cwid + 3
            hot = r == 0 and i == 2
            b += R(x, y, cwid - 6, 36, 9, FAM["yellow"][1] if hot else (TINT if v else FAM["coral"][2]),
                   INK if hot else None, 2)
            b += T(x + (cwid - 6) / 2, y + 23, v, 15, 700 if hot else 500, INK if v else deep, "m", "middle")
    b += f'<circle cx="{join[0]}" cy="{join[1]}" r="7" fill="{FAM["yellow"][1]}" stroke="{INK}" stroke-width="2"/>'
    b += R(cx + 22, cy + 286, cw - 44, 1, 0, EDGE)
    b += mono(cx + 22, cy + 314, "Medium, navy")
    b += T(cx + 22, cy + 340, "1 left, the same on every channel", 14, 600, INK)
    b += T(cx + 22, cy + 364, "Sold at the counter, it shows 0 online", 13, 400, MUTED)
    return frame(u, "Diagram: the online store, the shop counter and wholesale orders all read one stock count per "
                    "size and color. The last medium in navy shows 1 left on every channel.", b, "coral")


def furniture():
    u = "hf"
    deep, bright, soft = FAM["lilac"]
    b = ""
    cx, cy, cw, ch = 36, 64, 476, 384
    b += card(u, cx, cy, cw, ch, 18)
    b += icon("sofa", cx + 24, cy + 24, 40)
    b += T(cx + 78, cy + 46, "Large Cabinet", 20, 750, INK, "h") + mono(cx + 78, cy + 64, "10 units received")
    b += mono(cx + 24, cy + 112, "Cost per unit")
    b += T(cx + 24, cy + 156, "$240.00", 28, 700, MUTED, "h")
    b += R(cx + 22, cy + 146, 112, 2.5, 1, MUTED)
    b += arrow(f"M{cx + 146} {cy + 146} H{cx + 184}", bright, dash=False, uid=u, width=2.5)
    b += T(cx + 198, cy + 158, "$356.74", 38, 800, INK, "h")
    b += R(cx + 198, cy + 166, 150, 6, 3, bright)
    # stacked bar: supplier price, freight, duty (sample landed cost LC/2026/0004)
    parts = [("Supplier price", 2400.00, deep), ("Ocean freight", 850.00, FAM["coral"][1]), ("Import duty", 317.42, FAM["yellow"][1])]
    tot = sum(p[1] for p in parts)
    bx, by, bw = cx + 24, cy + 196, cw - 48
    b += f'<clipPath id="bc-{u}"><rect x="{bx}" y="{by}" width="{bw}" height="26" rx="8"/></clipPath><g clip-path="url(#bc-{u})">'
    x = bx
    for _name, v, c in parts:
        w = bw * v / tot
        b += R(x, by, w + .5, 26, 0, c)
        x += w
    b += "</g>"
    for i, (name, v, c) in enumerate(parts):
        y = cy + 256 + i * 28
        b += R(bx, y - 10, 12, 12, 3, c) + T(bx + 22, y, name, 14, 400, INK) + T(bx + bw, y, f"${v:,.2f}", 14, 500, INK, "m", "end")
    b += R(bx, cy + 330, bw, 1, 0, EDGE)
    b += T(bx, cy + 358, "Landed cost, 10 units", 14, 700, INK) + T(bx + bw, cy + 358, f"${tot:,.2f}", 15, 700, INK, "m", "end")
    # the late freight bill
    fx, fy = 356, 22
    b += card(u, fx, fy, 220, 96, 14)
    b += icon("truck", fx + 16, fy + 20, 36)
    b += T(fx + 62, fy + 38, "Freight bill", 15, 700, INK, "h") + mono(fx + 62, fy + 56, "Posted after receipt")
    b += pill(fx + 62, fy + 76, "+$850.00", "coral")
    return frame(u, "Diagram: 10 Large Cabinets cost $2,400.00 from the supplier. Ocean freight of $850.00 and import duty "
                    "of $317.42 bring the landed cost to $3,567.42, so the cost per unit goes from $240.00 to $356.74.",
                 b, "lilac")


def food():
    u = "fb"
    deep, bright, soft = FAM["mint"]
    b = ""
    cx, cy, cw, ch = 28, 40, 544, 400
    b += card(u, cx, cy, cw, ch, 18)
    b += icon("jar", cx + 24, cy + 22, 40)
    b += T(cx + 78, cy + 44, "Cold Brew Concentrate", 19, 750, INK, "h") + mono(cx + 78, cy + 62, "Case of 12 · 3 lots in stock")
    ax0, ax1, ay = cx + 40, cx + cw - 32, cy + 286
    months = ["Nov", "Dec", "Jan", "Feb", "Mar"]
    step = (ax1 - ax0) / 4
    b += R(ax0, ay - 1.5, ax1 - ax0, 3, 1.5, EDGE)
    for i, m in enumerate(months):
        x = ax0 + i * step
        b += R(x - 1, ay - 7, 2, 14, 1, "#b9c1cf") + mono(x, ay + 26, m, anchor="middle")
    today = ax0 + step * 0.42
    b += f'<path d="M{n(today)} {cy + 96} V{ay}" stroke="{FAM["coral"][0]}" stroke-width="2" stroke-dasharray="4 5"/>'
    b += pill(today - 30, cy + 96, "Today", "coral", solid=True)
    lots = [("Lot 2611-A", "Best by Dec 1", 1 + 0 / 30, 142, True), ("Lot 2612-B", "Best by Jan 12", 2 + 11 / 31, 196, False),
            ("Lot 2701-C", "Best by Feb 10", 3 + 9 / 28, 142, False)]
    for code, best, pos, ty, first in lots:
        x = ax0 + step * pos
        tw = 124
        tx = min(max(x - tw / 2, cx + 14), cx + cw - 14 - tw)
        b += f'<path d="M{n(x)} {cy + ty + 58} V{ay}" stroke="{deep if first else "#b9c1cf"}" stroke-width="2"/>'
        b += f'<circle cx="{n(x)}" cy="{ay}" r="6" fill="{bright if first else WHITE}" stroke="{INK}" stroke-width="2"/>'
        b += R(tx, cy + ty, tw, 58, 12, soft if first else WHITE, deep if first else EDGE, 2 if first else 1.5)
        b += mono(tx + 14, cy + ty + 22, code, deep if first else MUTED, 10.5, weight=600)
        b += T(tx + 14, cy + ty + 44, best, 14, 600, INK)
        if first:
            b += pill(tx + 4, cy + ty - 14, "Ships first", "mint", solid=True)
    b += R(cx + 24, cy + 334, cw - 48, 1, 0, EDGE)
    b += T(cx + 24, cy + 364, "The next order takes lot 2611-A, the first to expire.", 14, 600, INK)
    b += T(cx + 24, cy + 386, "Each order records its lot, so a recall is one search.", 13, 400, MUTED)
    return frame(u, "Diagram: three lots of Cold Brew Concentrate on a timeline, best by Dec 1, Jan 12 and Feb 10. "
                    "The next order takes the lot that expires first, and each order records its lot.", b, "mint")


def beauty():
    u = "hb"
    deep, bright, soft = FAM["blue"]
    b = ""
    cx, cy, cw, ch = 40, 36, 520, 408
    b += card(u, cx, cy, cw, ch, 18)
    b += icon("pump", cx + 24, cy + 22, 40)
    b += T(cx + 78, cy + 44, "Face serum, 30 ml", 19, 750, INK, "h") + mono(cx + 78, cy + 62, "Batch 0425 · ready to fill")
    b += mono(cx + 24, cy + 108, "What one unit needs")
    parts = [("Serum, bulk batch", "Ready", "mint"), ("Glass bottle", "In stock", "mint"), ("Pump", "On order", "coral"),
             ("Label", "In stock", "mint")]
    for i, (name, st, fam) in enumerate(parts):
        y = cy + 124 + i * 46
        late = fam == "coral"
        if late:
            b += R(cx + 12, y, cw - 24, 42, 12, FAM["coral"][2])
        ok = FAM["mint"][0]
        if late:
            b += (f'<circle cx="{cx + 38}" cy="{y + 21}" r="11" fill="{WHITE}" stroke="{FAM["coral"][0]}" stroke-width="2"/>'
                  f'<path d="M{cx + 38} {y + 15} V{y + 21} L{cx + 42} {y + 24}" fill="none" stroke="{FAM["coral"][0]}" stroke-width="2" stroke-linecap="round"/>')
        else:
            b += (f'<circle cx="{cx + 38}" cy="{y + 21}" r="11" fill="{FAM["mint"][2]}"/>'
                  f'<path d="M{cx + 33} {y + 21} l3.5 3.5 6.5-7" fill="none" stroke="{ok}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>')
        b += T(cx + 60, y + 26, name, 15, 600 if late else 500, INK)
        b += pill(cx + cw - 28, y + 21, st, fam, anchor="end")
    # arrival timeline for the pumps
    ty = cy + 336
    x0, x1 = cx + 28, cx + cw - 28
    b += mono(x0, ty - 18, "Pumps arrive")
    b += R(x0, ty, x1 - x0, 10, 5, TINT) + R(x0, ty, (x1 - x0) * 0.08, 10, 5, FAM["coral"][1])
    for i in range(4):
        x = x0 + (x1 - x0) * i / 3
        b += R(x - 1, ty - 4, 2, 18, 1, "#b9c1cf")
        b += mono(x, ty + 34, ["Today", "Week 1", "Week 2", "Week 3"][i], anchor="start" if i == 0 else ("end" if i == 3 else "middle"))
    b += f'<circle cx="{n(x1)}" cy="{ty + 5}" r="9" fill="{FAM["coral"][1]}" stroke="{INK}" stroke-width="2"/>'
    return frame(u, "Diagram: a face serum batch is ready to fill. The serum, bottles and labels are in stock, and the "
                    "pumps are on order, arriving in three weeks.", b, "blue")


def wholesale():
    u = "wh"
    deep, bright, soft = FAM["yellow"]
    b = ""
    # three linked records: B2B order, quotation, invoice (sample quotation for The Jackson Group)
    b += arrow("M150 150 C150 180 168 196 192 200", FAM["yellow"][1], uid=u)
    b += arrow("M194 310 C150 310 128 326 128 356", FAM["yellow"][1], uid=u)
    ax, ay, aw, ah = 28, 28, 262, 118
    b += card(u, ax, ay, aw, ah, 16) + icon("cart", ax + 18, ay + 18, 34)
    b += mono(ax + 62, ay + 30, "B2B order · Shopify") + T(ax + 62, ay + 52, "The Jackson Group", 16, 700, INK, "h")
    b += R(ax + 18, ay + 70, aw - 36, 1, 0, EDGE)
    b += T(ax + 18, ay + 98, "10 × Large Cabinet", 14, 500, INK)
    qx, qy, qw, qh = 196, 160, 376, 190
    b += card(u, qx, qy, qw, qh, 18) + icon("tag", qx + 20, qy + 20, 36)
    b += mono(qx + 66, qy + 32, "Quotation · Odoo") + T(qx + 66, qy + 54, "Priced from the account", 16, 700, INK, "h")
    rows = [("Price list", "Wholesale accounts"), ("Payment terms", "30 days")]
    for i, (k, v) in enumerate(rows):
        y = qy + 90 + i * 28
        b += T(qx + 22, y, k, 13, 400, MUTED) + T(qx + 150, y, v, 14, 600, INK)
    b += R(qx + 22, qy + 130, qw - 44, 1, 0, EDGE)
    b += T(qx + 22, qy + 162, "10 × $320.00", 14, 500, INK, "m")
    b += pill(qx + 150, qy + 157, "−15%", "yellow", solid=True)
    b += T(qx + qw - 22, qy + 162, "$2,720.00", 16, 700, INK, "m", "end")
    ix, iy, iw, ih = 28, 364, 300, 92
    b += card(u, ix, iy, iw, ih, 16) + icon("invoice", ix + 16, iy + 18, 34)
    b += mono(ix + 62, iy + 30, "Invoice · Odoo") + T(ix + 62, iy + 52, "Due in 30 days", 15, 700, INK, "h")
    b += T(ix + 62, iy + 74, "$2,720.00 + tax", 13, 500, MUTED, "m")
    b += pill(330, 60, "Typed once", "yellow", solid=True)
    b += T(330, 98, "The order becomes the quotation", 13, 400, ON_DARK_MUTED)
    b += T(330, 118, "and then the invoice.", 13, 400, ON_DARK_MUTED)
    return frame(u, "Diagram: a B2B order for 10 Large Cabinets from The Jackson Group becomes an Odoo quotation priced "
                    "from the Wholesale accounts price list, $320.00 less 15% on 30-day terms, $2,720.00, and then an "
                    "invoice due in 30 days.", b, "yellow")


# ---------------------------------------------------------------------------
# How we work, book, 404
# ---------------------------------------------------------------------------

def how():
    u = "hw"
    b = ""
    xs = [110, 300, 490]
    ys = [112, 254, 396]
    cols = [FAM["blue"][1], FAM["mint"][1], FAM["coral"][1]]
    r_turn = (ys[1] - ys[0]) / 2
    # the line: three rows joined by half-circle turns
    segs = [f"M{xs[0]} {ys[0]} H{xs[2]} A{r_turn} {r_turn} 0 0 1 {xs[2]} {ys[1]}",
            f"M{xs[2]} {ys[1]} H{xs[0]} A{r_turn} {r_turn} 0 0 0 {xs[0]} {ys[2]}",
            f"M{xs[0]} {ys[2]} H{xs[2]}"]
    for d, c in zip(segs, cols):
        b += f'<path d="{d}" fill="none" stroke="{c}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
    stops = [("calendar", "Scoping call", "30-minute call"), ("roadmap", "Systems Roadmap", "2–3 weeks"),
             ("contract", "Agreement", "Before any work"), ("key", "Access", "Week 1"),
             ("staging", "Build in staging", "Most of the project"), ("checklist", "Testing", "1–2 weeks"),
             ("go-live", "Go-live", "A planned date"), ("support", "After go-live", "2–4 weeks"),
             ("lock", "Handover", "Project close")]
    order = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2)]
    for (row, col), (ic, name, meta) in zip(order, stops):
        x, y = xs[col], ys[row]
        b += badge(x, y, ic, 24)
        b += T(x, y + 44, name, 14, 700, ON_DARK, "h", "middle") + mono(x, y + 60, meta, ON_DARK_MUTED, 9.5, "middle")
    for label, fam, x, y in [("Plan", "blue", xs[0], ys[0]), ("Build", "mint", xs[2], ys[1]), ("Launch", "coral", xs[0], ys[2])]:
        w = 14 + len(label) * 6.6
        b += pill(x - w / 2, y - 44, label, fam, solid=True)
    return frame(u, "Diagram: a project as one line with nine stops in three phases. Plan: scoping call, Systems Roadmap, "
                    "agreement. Build: access, build in staging, testing. Launch: go-live, after go-live, handover.", b, "blue")


def book():
    u = "bk"
    b = ""
    cx, cy, ro, ri = 196, 240, 158, 112
    parts = [(0, 5, "blue", "0–5 min", ["What you sell,", "and where"]),
             (5, 20, "coral", "5–20 min", ["What isn't working,", "and what it costs"]),
             (20, 30, "mint", "20–30 min", ["Which service fits,", "and a rough price"])]

    def pt(minute, r):
        a = math.radians(minute / 30 * 360 - 90)
        return cx + r * math.cos(a), cy + r * math.sin(a)

    gap = 0.25
    for m0, m1, fam, *_ in parts:
        a0, a1 = m0 + gap, m1 - gap
        large = 1 if (a1 - a0) > 15 else 0
        p1, p2, p3, p4 = pt(a0, ro), pt(a1, ro), pt(a1, ri), pt(a0, ri)
        d = (f"M{n(p1[0])} {n(p1[1])} A{ro} {ro} 0 {large} 1 {n(p2[0])} {n(p2[1])} L{n(p3[0])} {n(p3[1])} "
             f"A{ri} {ri} 0 {large} 0 {n(p4[0])} {n(p4[1])} Z")
        b += f'<path d="{d}" fill="{FAM[fam][1]}" stroke="{CANVAS}" stroke-width="2"/>'
    for m in range(0, 30, 5):
        a, c = pt(m, ro + 10), pt(m, ro + 18)
        b += f'<path d="M{n(a[0])} {n(a[1])} L{n(c[0])} {n(c[1])}" stroke="{ON_DARK_MUTED}" stroke-width="2" stroke-linecap="round"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{ri - 14}" fill="{WHITE}"/>'
    b += T(cx, cy + 14, "30", 60, 800, INK, "h", "middle") + mono(cx, cy + 40, "minutes", MUTED, 11, "middle")
    b += mono(cx, cy - 38, "Video call", MUTED, 10, "middle")
    lx = 392
    for i, (_m0, _m1, fam, when, rows) in enumerate(parts):
        y = 128 + i * 110
        b += R(lx, y - 6, 6, 62, 3, FAM[fam][1])
        b += mono(lx + 20, y + 8, when, FAM[fam][1], 11, weight=600)
        b += lines(lx + 20, y + 32, rows, 15, 1.35, weight=500, fill=ON_DARK)
    return frame(u, "Diagram: the 30-minute scoping call as a dial. The first 5 minutes cover what you sell and where, the "
                    "next 15 what isn't working and what it costs, the last 10 which service fits and a rough price.",
                 b, "blue")


def notfound():
    u = "nf"
    b = ""
    sx, sy, sw, sh = 120, 72, 360, 300
    post = "#3b4d70"
    b += R(sx - 10, sy - 10, 12, sh + 10, 3, post) + R(sx + sw - 2, sy - 10, 12, sh + 10, 3, post)
    for i in range(2):
        b += R(sx - 10, sy + i * 150 + 132, sw + 20, 10, 2, post)
    bins = [("A-01", 0, 0, "inventory"), ("A-02", 1, 0, "back-office"), ("A-03", 2, 0, "inventory"),
            ("A-04", 0, 1, None), ("A-05", 1, 1, "back-office"), ("A-06", 2, 1, "inventory")]
    for code, c, r, ic in bins:
        x, y = sx + 14 + c * 112, sy + 10 + r * 150
        if ic:
            b += icon(ic, x + 18, y + 26, 72, INK)
            b += R(x + 26, y + 104, 54, 20, 4, WHITE) + T(x + 53, y + 118, code, 10.5, 600, INK, "m", "middle")
        else:
            b += R(x + 4, y + 18, 98, 104, 10, "none", FAM["coral"][1], 2, ' stroke-dasharray="7 7"')
            b += R(x + 18, y + 102, 70, 24, 5, FAM["coral"][1]) + T(x + 53, y + 118, "A-04 · 404", 10.5, 700, INK, "m", "middle")
            b += T(x + 53, y + 74, "?", 34, 700, FAM["coral"][1], "h", "middle")
    b += mono(W / 2, 424, "Bin A-04 is empty: this page isn't here", ON_DARK_MUTED, 11, "middle")
    return frame(u, "Drawing: a stock shelf with six bins. Bin A-04 is empty and tagged 404.", b, "coral")



# ---------------------------------------------------------------------------
# Hubs: industries overview, pricing ranges
# ---------------------------------------------------------------------------

def industries():
    """One card per industry with the number its own page's diagram is about."""
    u = "in"
    tiles = [("shirt", "coral", "Apparel", "1 left", ["Medium navy, the same count", "online, in store and wholesale"]),
             ("sofa", "lilac", "Home and furniture", "+$850.00", ["Freight added to the cabinet's", "cost before it is priced"]),
             ("jar", "mint", "Food and beverage", "Lot 2611-A", ["Best by Dec 1, so this lot", "ships before the newer ones"]),
             ("pump", "blue", "Health and beauty", "Week 3", ["Pumps for batch 0425 are due,", "and the rest is ready to fill"]),
             ("pallet", "yellow", "Wholesale", "−15%", ["Each account's price list", "and terms, on every order"])]
    b = ""
    cw, ch, gx, gy, x0, y0 = 268, 140, 16, 12, 24, 22
    for i, (ic, fam, name, stat, cap) in enumerate(tiles):
        col, row = i % 2, i // 2
        x, y = x0 + col * (cw + gx), y0 + row * (ch + gy)
        deep, bright, soft = FAM[fam]
        if i < 4:
            b += card(u, x, y, cw, ch, 16) + R(x + 16, y + 16, 40, 40, 10, soft) + icon(ic, x + 19, y + 19, 34)
            b += mono(x + 68, y + 41, name)
            b += T(x + 18, y + 90, stat, 24, 800, deep, "h", spacing="-.3")
            b += lines(x + 18, y + 112, cap, 12.5, 1.35, fill=MUTED)
        else:
            w, hh = 2 * cw + gx, 94
            b += card(u, x, y, w, hh, 16) + R(x + 16, y + 27, 40, 40, 10, soft) + icon(ic, x + 19, y + 30, 34)
            b += mono(x + 70, y + 38, name)
            b += T(x + 70, y + 72, stat, 26, 800, INK, "h", spacing="-.3")
            b += pill(x + 164, y + 63, "Price list", "yellow", solid=True)
            b += lines(x + 300, y + 44, cap, 13, 1.4, fill=MUTED)
    return frame(u, "Five industries and the problem each page covers: apparel, one Medium navy left with the same count on "
                    "every channel; furniture, $850.00 of freight added to a cabinet's cost; food, lot 2611-A best by "
                    "December 1 ships first; beauty, the pumps for batch 0425 arrive in week 3; wholesale, each account's "
                    "price list and terms on every order.", b, "blue")


def pricing():
    """What we look at on the call to set a fixed fee, for one sample business, and the proposal it leads to."""
    u = "pr"
    b = mono(28, 46, "What sets the fee, for one sample business", ON_DARK_MUTED)
    lx, ly, lw, lh = 24, 62, 366, 392
    b += card(u, lx, ly, lw, lh, 18)
    factors = [("inventory", "Products and variants", "1,240 variants", 3, "lilac"),
               ("back-office", "Where stock lives", "2 shops and 1 warehouse", 2, "mint"),
               ("invoice", "History to move", "2 years of orders", 2, "coral"),
               ("sync", "Connector", "Shopify and Odoo, both ways", 2, "blue"),
               ("person", "Staff accounts", "8 people", 1, "yellow")]
    for i, (ic, name, val, lvl, fam) in enumerate(factors):
        y = ly + 22 + i * 74
        if i:
            b += R(lx + 18, y - 10, lw - 36, 1, 0, EDGE)
        b += icon(ic, lx + 18, y + 6, 36)
        b += T(lx + 66, y + 22, name, 14.5, 700, INK, "h") + T(lx + 66, y + 42, val, 13, 400, MUTED)
        for k in range(3):
            b += R(lx + 286 + k * 22, y + 20, 18, 10, 3, FAM[fam][1] if k < lvl else "#e3e7ee")
    b += mono(lx + 286, ly + 16, "Effort", MUTED, 10)
    b += arrow(f"M{lx + lw + 6} 258 C{lx + lw + 26} 258 {lx + lw + 22} 258 412 258", FAM["yellow"][1], uid=u)
    px, py, pw, ph = 416, 150, 160, 216
    b += card(u, px, py, pw, ph, 18) + icon("contract", px + 16, py + 16, 36)
    b += mono(px + 16, py + 76, "Proposal") + T(px + 16, py + 104, "One fixed fee", 17, 800, INK, "h")
    b += lines(px + 16, py + 128, ["In writing within", "3 business days"], 12.5, 1.35, fill=MUTED)
    b += R(px + 16, py + 160, pw - 32, 1, 0, EDGE)
    b += lines(px + 16, py + 182, ["Changes only with", "your signature"], 12.5, 1.35, fill=INK, weight=600)
    return frame(u, "Diagram of what sets a fixed fee for one sample business: 1,240 product variants, two shops and a "
                    "warehouse, two years of orders to move, a two-way Shopify and Odoo connector, and eight staff "
                    "accounts. They lead to a proposal with one fixed fee, in writing within 3 business days, that "
                    "changes only with your signature.", b, "yellow")


# ---------------------------------------------------------------------------
# Home: where storefront agencies stop, where ERP resellers start, and where we work
# ---------------------------------------------------------------------------

GAP_STOPS = [("theme", "Product page"), ("cart", "Checkout"), ("sync", "Handoff"), ("inventory", "Stock"),
             ("truck", "Pick and ship"), ("invoice", "Invoice and refunds"), ("books", "Books")]
GAP_LABEL = ("Diagram of an order's path: product page, checkout, the handoff, stock, pick and ship, invoice and "
             "refunds, books. Storefront agencies cover the product page and checkout. ERP resellers cover stock "
             "through the books. Orders, stock and refunds go missing in the handoff between them. We work across "
             "every step, including the handoff.")


def _stop(x, y, name, gap=False, r=27):
    ring = FAM["coral"][0] if gap else "#c9d0dc"
    da = ' stroke-dasharray="5 4"' if gap else ""
    s = r * 1.3
    return (f'<circle cx="{n(x)}" cy="{n(y)}" r="{r}" fill="{WHITE}" stroke="{ring}" stroke-width="2"{da}/>'
            + icon(name, x - s / 2, y - s / 2, s))


def gap_wide():
    w, h = 1144, 220  # drawn on a 1144 x 300 grid, shown from y 40
    xs = [72 + i * (1000 / 6) for i in range(7)]
    y = 150
    grey, coral, blue = "#c9d0dc", FAM["coral"][0], FAM["blue"][0]
    b = (f'<path d="M{n(xs[0])} {y} H{n(xs[1])}" stroke="{grey}" stroke-width="4" stroke-linecap="round"/>'
         f'<path d="M{n(xs[1])} {y} H{n(xs[3])}" stroke="{coral}" stroke-width="3" stroke-dasharray="7 7" stroke-linecap="round"/>'
         f'<path d="M{n(xs[3])} {y} H{n(xs[6])}" stroke="{grey}" stroke-width="4" stroke-linecap="round"/>')
    for i, (ic, name) in enumerate(GAP_STOPS):
        b += _stop(xs[i], y, ic, gap=(i == 2))
        b += T(xs[i], y + 52, name, 14, 650, coral if i == 2 else INK, "h", "middle")
    # who covers what
    def bracket(a, z, label, yb=78):
        return (f'<path d="M{n(a)} {yb + 12} V{yb} H{n(z)} V{yb + 12}" fill="none" stroke="#8b95a7" stroke-width="1.6" '
                f'stroke-linejoin="round"/>' + mono((a + z) / 2, yb - 12, label, MUTED, 11, "middle", 600))
    b += bracket(xs[0] - 44, xs[1] + 44, "Storefront agencies")
    b += bracket(xs[3] - 44, xs[6] + 44, "ERP resellers")
    b += T(xs[2], 64, "Orders, stock and refunds", 13, 600, coral, "b", "middle")
    b += T(xs[2], 82, "go missing here", 13, 600, coral, "b", "middle")
    b += (f'<path d="M{n(xs[0] - 44)} 220 V232 H{n(xs[6] + 44)} V220" fill="none" stroke="{blue}" stroke-width="2.5" '
          f'stroke-linejoin="round"/>')
    tag = "Where we work: both sides and the link between them"
    tw = len(tag) * 7.4 + 36
    b += R(w / 2 - tw / 2, 218, tw, 30, 15, blue) + T(w / 2, 238, tag, 13.5, 650, WHITE, "h", "middle")
    return (f'<svg class="art gap-wide" viewBox="0 40 {w} 220" role="img" aria-label="{esc(GAP_LABEL)}" focusable="false">'
            f'{b}</svg>')


def _tall_bracket(a, z, rows, mid, xb=304):
    out = (f'<path d="M{xb - 10} {n(a)} H{xb} V{n(z)} H{xb - 10}" fill="none" stroke="#8b95a7" stroke-width="1.6" '
           f'stroke-linejoin="round"/>')
    return out + "".join(mono(xb - 18, mid + k * 14, r, MUTED, 10, "end", 600) for k, r in enumerate(rows))


def gap_tall():
    w, h = 360, 660
    ys = [92 + i * 86 for i in range(7)]
    x = 92
    grey, coral, blue = "#c9d0dc", FAM["coral"][0], FAM["blue"][0]
    b = (f'<path d="M{x} {ys[0]} V{ys[1]}" stroke="{grey}" stroke-width="4" stroke-linecap="round"/>'
         f'<path d="M{x} {ys[1]} V{ys[3]}" stroke="{coral}" stroke-width="3" stroke-dasharray="7 7" stroke-linecap="round"/>'
         f'<path d="M{x} {ys[3]} V{ys[6]}" stroke="{grey}" stroke-width="4" stroke-linecap="round"/>')
    for i, (ic, name) in enumerate(GAP_STOPS):
        b += _stop(x, ys[i], ic, gap=(i == 2), r=25)
        rows = ["Invoice and", "refunds"] if name == "Invoice and refunds" else [name]
        b += lines(x + 40, ys[i] + 5 - (len(rows) - 1) * 8, rows, 14, 1.2, weight=650, fill=coral if i == 2 else INK, font="h")
    b += _tall_bracket(ys[0] - 26, ys[1] + 26, ["Storefront", "agencies"], (ys[0] + ys[1]) / 2 - 2)
    b += _tall_bracket(ys[3] - 26, ys[6] + 26, ["ERP", "resellers"], (ys[4] + ys[5]) / 2 - 2)
    b += lines(196, ys[2] - 4, ["Orders, stock and", "refunds go missing"], 12.5, 1.3, weight=600, fill=coral)
    b += (f'<path d="M36 {ys[0] - 26} H26 V{ys[6] + 26} H36" fill="none" stroke="{blue}" stroke-width="2.5" '
          f'stroke-linejoin="round"/>')
    tag = "Where we work: every step"
    tw = len(tag) * 7.2 + 30
    b += R(16, 18, tw, 30, 15, blue) + T(16 + tw / 2, 38, tag, 13.5, 650, WHITE, "h", "middle")
    return (f'<svg class="art gap-tall" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(GAP_LABEL)}" focusable="false">'
            f'{b}</svg>')


def gap_art():
    return f'<figure class="gap-fig">{gap_wide()}{gap_tall()}</figure>'


HERO = {"apparel": apparel, "home-and-furniture": furniture, "food-and-beverage": food, "health-and-beauty": beauty,
        "wholesale": wholesale, "how-it-works": how, "book": book, "notfound": notfound, "industries": industries,
        "pricing": pricing}


# Diagrams whose records are sample data get the same "Sample data" note as the real screens and clips.
SAMPLE = {"apparel", "home-and-furniture", "food-and-beverage", "health-and-beauty", "wholesale", "industries", "pricing"}


def hero_art(name):
    note = '<p class="art-note">Sample data</p>' if name in SAMPLE else ""
    return f'<div class="art-wrap">{HERO[name]()}{note}</div>'
