"""Scenes drawn for this site in the spot-icon style (no third-party art, no license needed).

A 3px ink outline, flat brand fills and one accent block printed slightly off-register behind the main object, on a
480 x 320 grid. Real objects from the work: rails of stock, pallets, registers, invoices, a scoping call. No faces with
detail, nothing floating. Sample sheet approved direction: website-previews/redesign-2026-11-12 (Nov 12, 2026).
"""
import re
from functools import lru_cache
from pathlib import Path
INK = "#141c2b"; W = "#fff"
BLUE, CORAL, MINT, LILAC, YEL = "#2f55d4", "#ff7a59", "#3ecf9e", "#a99bff", "#ffc53d"
SOFT = "#e3e9ff"; TINT = "#f3ede2"; KRAFT = "#f4d9a6"; SKIN = "#f6b89e"


def svg(body, vb="0 0 480 320"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="480" height="320" aria-hidden="true" focusable="false">'
            f'<g fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>')


def rect(x, y, w, h, fill=W, rx=3, off=None, d=8, extra=""):
    s = ""
    if off:
        s += f'<rect x="{x + d}" y="{y + d}" width="{w}" height="{h}" rx="{rx}" fill="{off}" stroke="none"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'
    return s


def path(d, fill="none", **kw):
    a = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in kw.items())
    return f'<path d="{d}" fill="{fill}" {a}/>'


def circ(cx, cy, r, fill=W, **kw):
    a = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in kw.items())
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" {a}/>'


GROUND = path("M24 296 H456")


# 1. Apparel: a rail of shirts in sizes, a folded stack and a bag
def apparel():
    s = GROUND
    # rail
    s += path("M64 296 V92 H316 V296") + path("M48 296 H80 M300 296 H332")
    shirts = [(108, CORAL), (160, MINT), (212, BLUE), (264, YEL)]
    for x, c in shirts:
        s += path(f"M{x} 112 V100 a6 6 0 1 1 6 -6")  # hook
        s += path(f"M{x - 28} 126 L{x} 112 L{x + 28} 126")  # hanger
        body = (f"M{x - 27} 126 L{x - 42} 146 L{x - 31} 156 L{x - 23} 148 V232 H{x + 23} V148 L{x + 31} 156 "
                f"L{x + 42} 146 L{x + 27} 126 Q{x + 12} 128 {x + 9} 126 Q{x} 140 {x - 9} 126 Q{x - 12} 128 {x - 27} 126 Z")
        s += path(body, fill=c)
        # size tag at the hem
        s += rect(x + 6, 214, 13, 18, W, 2) + circ(x + 12.5, 219, 1.6, INK, stroke="none")
    # sleeve cuffs on the front shirt
    s += path("M227 150 l7 -6 M197 150 l-7 -6", stroke_width="2.5")
    # table with folded stack and a bag
    s += rect(340, 236, 120, 12, W, 2, off=LILAC, d=7) + path("M352 248 V296 M448 248 V296")
    for i, c in enumerate([BLUE, CORAL, MINT]):
        y = 222 - i * 15
        s += rect(352 - i * 2, y, 64 + i * 4, 14, c, 4)
        s += path(f"M{372 - i * 2} {y + 7} h24", stroke_width="2.5")
    s += path("M426 236 V190 H458 V236", fill=W) + path("M432 190 c0 -16 20 -16 20 0")
    s += path("M426 236 H458")
    s += rect(433, 204, 18, 12, YEL, 2, extra='stroke-width="2.5"')
    return svg(s)


# 2. Home and furniture: an armchair on a pallet, a carton and a box truck
def furniture():
    s = path("M24 288 H456")
    # truck
    s += rect(240, 132, 172, 128, W, 4, off=BLUE, d=9)
    for y in (160, 188, 216, 244):
        s += path(f"M256 {y} H396", stroke_width="2.5")
    s += path("M412 260 V176 H440 L462 212 V260 Z", fill=YEL)
    s += path("M420 184 H436 L452 210 H420 Z", fill=SOFT)
    s += path("M232 260 H466", stroke_width="3")
    for cx in (280, 432):
        s += circ(cx, 266, 17, INK) + circ(cx, 266, 6.5, W, stroke="none")
    # pallet
    s += rect(36, 262, 160, 10, W, 2) + rect(44, 272, 22, 14, W, 1) + rect(105, 272, 22, 14, W, 1) + rect(166, 272, 22, 14, W, 1)
    # armchair
    s += rect(64, 158, 108, 70, LILAC, 18, off=CORAL, d=8)
    s += path("M74 176 h88 M74 198 h88", stroke_width="2.5")
    s += rect(52, 220, 132, 28, LILAC, 10)
    s += rect(40, 196, 30, 56, W, 12) + rect(166, 196, 30, 56, W, 12)
    s += path("M60 252 V262 M176 252 V262")
    # carton with this-side-up arrows
    s += rect(196, 214, 40, 48, KRAFT, 2) + path("M196 228 H236", stroke_width="2.5")
    s += path("M208 254 v-12 m-4 4 l4 -4 4 4 M222 254 v-12 m-4 4 l4 -4 4 4", stroke_width="2.25")
    return svg(s)


# 3. Food and beverage: a shelf of jars with lot labels, a crate and a dated clipboard
def food():
    s = GROUND
    s += rect(40, 76, 210, 220, W, 3, off=MINT, d=9)
    s += path("M40 152 H250 M40 226 H250")
    for i, x in enumerate((58, 106, 154, 202)):
        lid = [CORAL, YEL, CORAL, BLUE][i]
        s += rect(x, 104, 34, 48, SOFT, 8) + rect(x + 2, 96, 30, 10, lid, 2)
        s += rect(x + 5, 118, 24, 18, W, 2, extra='stroke-width="2.25"') + path(f"M{x + 10} 124 h14 M{x + 10} 130 h9", stroke_width="2")
    for i, x in enumerate((60, 100, 140, 180, 220)):
        c = [MINT, LILAC, YEL, MINT, CORAL][i]
        s += path(f"M{x} 226 V196 q0 -8 6 -12 V172 h8 V184 q6 4 6 12 V226 Z", fill=c)
        s += rect(x + 4, 204, 12, 12, W, 1.5, extra='stroke-width="2.25"')
    for x in (62, 104, 146, 188):
        s += rect(x, 252, 34, 44, W, 4) + path(f"M{x} 262 h34 M{x} 286 h34", stroke_width="2.5")
    # crate with produce
    for cx, cy, c in ((300, 236, CORAL), (326, 232, YEL), (352, 236, CORAL), (378, 233, MINT), (404, 237, YEL)):
        s += circ(cx, cy, 15, c)
    s += rect(282, 244, 140, 52, KRAFT, 3) + path("M282 262 H422 M282 278 H422", stroke_width="2.5")
    # clipboard with a date grid, one day marked
    s += rect(330, 92, 92, 120, W, 6, off=LILAC, d=8)
    s += path("M376 84 L376 70") + circ(376, 66, 4, INK) + rect(358, 84, 36, 14, INK, 4)
    for r in range(3):
        for c in range(4):
            fill = CORAL if (r, c) == (1, 2) else W
            s += rect(342 + c * 18, 118 + r * 22, 14, 16, fill, 2, extra='stroke-width="2.25"')
    s += path("M342 194 h44", stroke_width="2.5")
    return svg(s)


# 4. Health and beauty: bottles with batch labels, a carton and a scanner reading its label
def beauty():
    s = path("M24 272 H456") + rect(24, 272, 432, 24, TINT, 0, extra='stroke="none"') + path("M24 272 H456")
    # pump bottle
    s += rect(56, 160, 62, 112, LILAC, 14, off=BLUE, d=8)
    s += rect(76, 142, 22, 18, W, 3) + path("M80 142 V128 H112 M104 128 v8")
    s += rect(66, 196, 42, 40, W, 3) + path("M74 208 h26 M74 218 h18 M74 228 h22", stroke_width="2.25")
    # dropper bottle
    s += rect(136, 210, 44, 62, YEL, 10) + rect(146, 196, 24, 14, W, 2) + path("M150 196 V178 a8 8 0 0 1 16 0 V196", fill=INK)
    s += rect(143, 228, 30, 24, W, 2) + path("M149 236 h18 M149 244 h12", stroke_width="2.25")
    # jar
    s += rect(196, 236, 64, 36, MINT, 8) + rect(192, 226, 72, 12, W, 4)
    # carton with barcode label
    s += rect(300, 186, 132, 86, KRAFT, 3, off=CORAL, d=8)
    s += path("M300 206 H432", stroke_width="2.5")
    s += rect(338, 222, 68, 36, W, 2)
    for i, w in enumerate((2.5, 1.5, 3, 1.5, 2.5, 1.5, 3, 2, 1.5, 2.5)):
        s += path(f"M{346 + i * 5.5} 228 v20", stroke_width=str(w))
    # scanner and beam
    s += path("M350 120 L404 110 L410 134 L372 142 L378 172 L362 176 L354 144 Z", fill=BLUE)
    s += path("M478 196 Q430 196 392 170", stroke=INK, stroke_width="24") + path("M478 196 Q430 196 392 170", stroke=MINT, stroke_width="18")
    s += circ(378, 160, 11, SKIN)
    s += path("M362 146 L350 222 M376 142 L404 220", stroke=CORAL, stroke_width="2.5", stroke_dasharray="2 7")
    return svg(s)


# 5. Wholesale: a wrapped pallet of cartons on a pallet jack and an invoice marked paid on terms
def wholesale():
    s = GROUND
    s += rect(40, 266, 216, 12, W, 2) + rect(48, 278, 26, 16, W, 1) + rect(135, 278, 26, 16, W, 1) + rect(222, 278, 26, 16, W, 1)
    for r in range(3):
        for c in range(3):
            x, y = 44 + c * 70, 196 - r * 64
            s += rect(x, y + 6, 66, 64, KRAFT, 2)
            s += path(f"M{x + 26} {y + 6} v18 h14 v-18", stroke_width="2.5")
    # pallet jack
    s += path("M256 284 H300 V246 L322 174", stroke_width="3")
    s += path("M312 172 h22", stroke_width="5") + circ(300, 286, 9, INK)
    # invoice standing on a clip stand
    s += rect(352, 96, 100, 142, W, 4, off=YEL, d=8)
    s += rect(352, 96, 100, 24, BLUE, 4) + path("M366 136 h56 M366 150 h40 M366 164 h48 M366 192 h72", stroke_width="2.5")
    s += path("M366 206 h40", stroke_width="2.5")
    s += circ(420, 214, 16, MINT) + path("M412 214 l6 6 l10 -11", stroke_width="3")
    s += rect(340, 238, 124, 10, W, 2) + path("M352 248 V296 M452 248 V296")
    return svg(s)


# 6. The scoping call: a laptop with a calendar, a notebook with the agenda and a mug
def call():
    s = path("M24 262 H456") + rect(24, 262, 432, 34, TINT, 0, extra='stroke="none"') + path("M24 262 H456")
    s += rect(150, 92, 190, 132, W, 8, off=BLUE, d=9)
    s += rect(162, 104, 166, 108, SOFT, 3, extra='stroke-width="2.5"')
    for r in range(3):
        for c in range(5):
            fill = YEL if (r, c) == (1, 3) else W
            s += rect(172 + c * 31, 124 + r * 28, 24, 20, fill, 3, extra='stroke-width="2.25"')
    s += path("M126 262 L150 224 H340 L364 262 Z", fill=W) + path("M222 244 h46", stroke_width="2.5")
    # notebook
    s += path("M52 262 L66 214 H134 L120 262 Z", fill=W)
    for i in range(3):
        y = 228 + i * 11
        s += path(f"M{73 - i * 3} {y} l3 3 l6 -6", stroke=MINT, stroke_width="2.5") + path(f"M{86 - i * 3} {y} h{28 - i * 4}", stroke_width="2.25")
    # mug with steam
    s += path("M384 214 V250 a10 10 0 0 0 10 10 H418 a10 10 0 0 0 10 -10 V214 Z", fill=CORAL)
    s += path("M428 224 h6 a10 10 0 0 1 0 20 h-6")
    s += path("M398 202 c-6 -8 6 -12 0 -22 M414 202 c-6 -8 6 -12 0 -22", stroke_width="2.5")
    # plant
    return svg(s)


# 7. A person packing an order at a bench
def packing():
    s = GROUND
    # bench
    s += rect(240, 206, 200, 14, W, 2, off=MINT, d=8) + path("M256 220 V296 M424 220 V296")
    # box on bench, flaps open
    s += rect(290, 150, 96, 56, KRAFT, 2) + path("M290 150 L272 128 M386 150 L404 128", stroke_width="3")
    s += path("M290 150 L306 124 H370 L386 150", fill=KRAFT)
    s += rect(318, 168, 40, 22, W, 2, extra='stroke-width="2.25"') + path("M324 176 h26 M324 183 h18", stroke_width="2")
    # tape roll
    s += circ(412, 196, 10, BLUE) + circ(412, 196, 4, W)
    # person: legs, shoes, torso, arms, head
    s += path("M184 206 L176 286", stroke=INK, stroke_width="20") + path("M210 206 L222 286", stroke=INK, stroke_width="20")
    s += path("M160 296 q0 -12 14 -12 h12 q8 0 8 12 Z", fill=W) + path("M212 296 q0 -12 14 -12 h12 q8 0 8 12 Z", fill=W)
    s += path("M168 112 Q196 100 224 112 L226 214 H168 Z", fill=CORAL)
    s += path("M220 120 Q262 140 294 170", stroke=INK, stroke_width="17") + path("M220 120 Q262 140 294 170", stroke=CORAL, stroke_width="11")
    s += path("M176 128 Q214 176 304 186", stroke=INK, stroke_width="17") + path("M176 128 Q214 176 304 186", stroke=CORAL, stroke_width="11")
    s += circ(298, 172, 9, SKIN) + circ(308, 186, 9, SKIN)
    s += rect(189, 90, 16, 18, SKIN, 6)
    s += circ(197, 74, 20, SKIN)
    s += path("M178 72 Q176 48 200 50 Q222 52 218 70 Q206 62 190 66 Q186 76 178 72 Z", fill=INK)
    return svg(s)


SCENES = {"apparel": apparel, "furniture": furniture, "food": food, "beauty": beauty,
          "wholesale": wholesale, "call": call, "packing": packing}


# 8. Systems Roadmap: a plan spread on a table, a route with three stops, a notebook and a pencil
def roadmap():
    s = path("M24 262 H456") + rect(24, 262, 432, 34, TINT, 0, extra='stroke="none"') + path("M24 262 H456")
    s += path("M70 246 L96 96 L206 112 L316 96 L346 246 L236 230 L126 246 Z", fill=W)
    s += path("M70 246 L96 96 L206 112 L316 96 L346 246 L236 230 L126 246 Z", fill=LILAC, stroke="none", transform="translate(9 9)")
    s = s.replace(path("M70 246 L96 96 L206 112 L316 96 L346 246 L236 230 L126 246 Z", fill=W), "", 1)
    s += path("M70 246 L96 96 L206 112 L316 96 L346 246 L236 230 L126 246 Z", fill=W)
    s += path("M206 112 L236 230 M126 246 L96 96", stroke_width="2.5")
    s += path("M112 214 C140 170 170 210 200 172 S262 140 292 128", stroke_dasharray="0.1 9", stroke_width="4")
    for cx, cy, c in ((112, 214, MINT), (200, 172, YEL), (292, 128, CORAL)):
        s += path(f"M{cx} {cy} c-9 -10 -14 -16 -14 -24 a14 14 0 0 1 28 0 c0 8 -5 14 -14 24 Z", fill=c) + circ(cx, cy - 24, 4.5, W)
    s += rect(372, 168, 74, 94, W, 4, off=BLUE, d=7)
    for i in range(3):
        y = 192 + i * 20
        s += path(f"M384 {y} l4 4 l8 -8", stroke=MINT, stroke_width="2.5") + path(f"M404 {y} h30", stroke_width="2.25")
    s += path("M360 252 L432 150 L442 157 L370 259 L356 264 Z", fill=YEL) + path("M432 150 L442 157", stroke_width="3")
    return svg(s)


# 9. Store Move: boxes on a hand truck rolling from an old shop to a new one
def storemove():
    s = GROUND
    def shop(x, w, awn, door):
        t = rect(x, 176, w, 120, W, 2)
        t += path(f"M{x - 10} 176 L{x + 4} 146 H{x + w - 4} L{x + w + 10} 176 Z", fill=awn)
        n = 4; step = (w + 20) / n
        for i in range(1, n):
            t += path(f"M{x - 10 + i * step} 176 L{x + 4 + i * (w - 8) / n} 146", stroke_width="2.5")
        t += rect(x + 14, 222, 30, 74, door, 2) + rect(x + 56, 204, w - 70, 44, SOFT, 2)
        return t
    s += shop(40, 120, LILAC, W)
    s += rect(318 + 9, 176 + 9, 130, 120, BLUE, 2, extra='stroke="none"')
    s += shop(318, 130, CORAL, YEL).replace('<rect x="318" y="176"', '<rect x="318" y="176"', 1)
    # hand truck with boxes
    for i, (w, c) in enumerate(((56, KRAFT), (50, KRAFT), (44, KRAFT))):
        y = 248 - i * 36
        s += rect(222 - w / 2 + 14 + i * 2, y, w, 36, c, 2) + path(f"M{236 + i * 2 - 6} {y} v12 h12 v-12", stroke_width="2.25")
    s += path("M204 294 H262 L272 168 l12 -6", stroke_width="4") + circ(262, 286, 10, INK) + circ(262, 286, 3.5, W, stroke="none")
    s += path("M196 214 h-24 M200 232 h-34 M196 250 h-20", stroke_width="2.5")
    return svg(s)


# 10. Back Office Launch: a monitor with a report, a shelf of binders, a printer with an invoice
def backoffice():
    s = path("M24 262 H456") + rect(24, 262, 432, 34, TINT, 0, extra='stroke="none"') + path("M24 262 H456")
    s += rect(150, 92, 180, 122, W, 8, off=MINT, d=9)
    s += rect(162, 104, 156, 98, SOFT, 3, extra='stroke-width="2.5"')
    for i, (hh, c) in enumerate(((30, BLUE), (52, CORAL), (40, YEL), (66, MINT))):
        s += rect(176 + i * 22, 190 - hh, 14, hh, c, 1.5, extra='stroke-width="2.25"')
    s += path("M268 128 h36 M268 142 h28 M268 156 h36 M268 170 h22", stroke_width="2.25")
    s += path("M226 214 L220 246 H260 L254 214") + path("M206 248 H274")
    # binders on a wall shelf
    s += path("M40 120 H128")
    for i, c in enumerate((BLUE, YEL, CORAL, LILAC)):
        s += rect(44 + i * 21, 58, 18, 62, c, 2) + circ(53 + i * 21, 106, 3.5, W)
    # printer and invoice
    s += rect(356, 196, 96, 52, W, 6, off=CORAL, d=7) + rect(372, 236, 64, 12, INK, 2)
    s += path("M372 196 V150 H436 V196", fill=W) + path("M384 164 h40 M384 176 h28", stroke_width="2.25")
    s += circ(436, 214, 4, MINT, stroke="none")
    return svg(s)


# 11. Support block: a laptop with a short chat thread and a toolbox
def support():
    s = path("M24 262 H456") + rect(24, 262, 432, 34, TINT, 0, extra='stroke="none"') + path("M24 262 H456")
    s += rect(110, 92, 196, 132, W, 8, off=YEL, d=9)
    s += rect(122, 104, 172, 108, SOFT, 3, extra='stroke-width="2.5"')
    s += path("M136 118 H226 a6 6 0 0 1 6 6 V146 a6 6 0 0 1 -6 6 H152 L140 162 V152 H136 a6 6 0 0 1 -6 -6 V124 a6 6 0 0 1 6 -6 Z", fill=W, stroke_width="2.5")
    s += path("M144 132 h62 M144 142 h40", stroke_width="2.25")
    s += path("M280 162 H200 a6 6 0 0 0 -6 6 V188 a6 6 0 0 0 6 6 H266 L278 204 V194 H280 a6 6 0 0 0 6 -6 V168 a6 6 0 0 0 -6 -6 Z", fill=BLUE, stroke_width="2.5")
    s += path("M208 176 h52 M208 184 h34", stroke=W, stroke_width="2.25")
    s += path("M86 262 L110 224 H306 L330 262 Z", fill=W) + path("M184 244 h48", stroke_width="2.5")
    # toolbox with a wrench
    s += rect(350, 210, 96, 52, CORAL, 4) + path("M378 210 V196 H418 V210", stroke_width="3") + path("M350 230 H446", stroke_width="2.5")
    s += rect(390, 224, 16, 12, W, 2, extra='stroke-width="2.25"')
    s += path("M372 196 L410 150 m-6 -8 a12 12 0 1 0 16 14 l-8 -2 -2 -8 Z", fill=W)
    return svg(s)


# 12. Not found: a shelf with one box where the page should be
def notfound():
    s = GROUND
    s += rect(110, 70, 260, 226, W, 3, off=YEL, d=9)
    s += path("M110 146 H370 M110 222 H370")
    for x in (126, 186):
        s += rect(x, 102, 48, 44, KRAFT, 2) + path(f"M{x + 18} 102 v12 h12 v-12", stroke_width="2.25")
    s += rect(296, 178, 48, 44, KRAFT, 2) + path("M314 178 v12 h12 v-12", stroke_width="2.25")
    s += path("M226 168 h52 M226 198 h52", stroke_dasharray="6 7", stroke_width="2.5")
    s += path("M240 250 a12 12 0 1 1 18 10 c-4 2 -6 5 -6 9", stroke_width="3.5") + circ(252, 282, 2.5, INK, stroke="none")
    return svg(s)


SCENES.update({"roadmap": roadmap, "storemove": storemove, "backoffice": backoffice, "support": support, "notfound": notfound})


ART = Path(__file__).resolve().parent / "art"


@lru_cache(maxsize=None)
def _sync():
    s = (ART / "shop-sync.svg").read_text()
    s = re.sub(r"<!--.*?-->\s*", "", s, flags=re.S)
    return s.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)


SCENES["sync"] = _sync


def scene(name, label="", cls=""):
    """A scene in its frame. label is the accessible description ('' = decorative)."""
    role = f' role="img" aria-label="{label}"' if label else ' aria-hidden="true"'
    return f'<figure class="scene{(" " + cls) if cls else ""}"{role}>{SCENES[name]()}</figure>'
