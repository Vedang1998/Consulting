"""Corporate Memphis illustrations for the [DBA name] site, drawn as inline SVG.

Flat figures with long limbs and small heads, built from a few primitives so every scene shares one
style. These are plainly illustrations: no photo, no real person, nothing passed off as real.
Colors come from CSS classes (m-*) so light and dark themes both work.
"""

# Palette classes are defined in site.css (.m-skin1 ... .m-coral). Shapes use them by name.


def _limb(points, cls, w):
    d = "M" + " L".join(f"{x} {y}" for x, y in points)
    return f'<path d="{d}" class="{cls}" fill="none" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def person(x, y, s=1.0, skin="m-skin1", shirt="m-blue", pants="m-ink", hair="m-hair1",
           arm_l=((-30, 20), (-48, 70)), arm_r=((30, 20), (48, 70)),
           leg_l=((-10, 40), (-16, 92)), leg_r=((10, 40), (16, 92)), hair_style=0,
           flip=False, extra=""):
    """A standing figure. Coordinates are relative to the hips (0, 0). Arms start at the shoulders
    (+-16, -72). Each arm is (elbow, hand) offsets from the shoulder; each leg is (knee, foot) from the hip."""
    sl, sr = (-16, -72), (16, -72)
    al = [sl, (sl[0] + arm_l[0][0], sl[1] + arm_l[0][1]), (sl[0] + arm_l[1][0], sl[1] + arm_l[1][1])]
    ar = [sr, (sr[0] + arm_r[0][0], sr[1] + arm_r[0][1]), (sr[0] + arm_r[1][0], sr[1] + arm_r[1][1])]
    ll = [(-9, 0), (leg_l[0][0], leg_l[0][1]), (leg_l[1][0], leg_l[1][1])]
    lr = [(9, 0), (leg_r[0][0], leg_r[0][1]), (leg_r[1][0], leg_r[1][1])]
    hairs = {
        0: '<path d="M-15 -110 q15 -22 30 0 q2 -18 -15 -20 q-17 2 -15 20z" class="{h}"/>',
        1: '<path d="M-16 -106 q-4 -26 16 -26 q22 0 18 30 l-6 -12 q-12 6 -28 8z" class="{h}"/>'
           '<circle cx="14" cy="-126" r="9" class="{h}"/>',
        2: '<path d="M-17 -104 q-2 -28 17 -28 q20 0 17 28 l0 26 q-6 4 -8 0 l0 -24 q-12 -8 -18 -6 l-2 30 q-4 4 -8 0z" class="{h}"/>',
        3: '<path d="M-16 -108 q0 -24 16 -24 q18 0 16 24 q-16 -8 -32 0z" class="{h}"/>',
    }
    hair_svg = hairs[hair_style].format(h=hair)
    body = (
        _limb(ll, pants, 15) + _limb(lr, pants, 15) +
        f'<ellipse cx="{ll[2][0] - 4}" cy="{ll[2][1] + 4}" rx="11" ry="5" class="m-ink"/>'
        f'<ellipse cx="{lr[2][0] + 4}" cy="{lr[2][1] + 4}" rx="11" ry="5" class="m-ink"/>'
        f'<path d="M-24 -74 q24 -12 48 0 l-6 78 q-18 6 -36 0z" class="{shirt}"/>'
        + _limb(al, skin, 11) + _limb(ar, skin, 11) +
        f'<path d="M-24 -74 q-6 2 -8 14 l12 6z M24 -74 q6 2 8 14 l-12 6z" class="{shirt}"/>'
        f'<rect x="-5" y="-86" width="10" height="14" rx="4" class="{skin}"/>'
        f'<circle cx="0" cy="-100" r="15" class="{skin}"/>' + hair_svg + extra
    )
    t = f"translate({x} {y}) scale({-s if flip else s} {s})"
    return f'<g transform="{t}">{body}</g>'


def hand_at(arm, side):
    """Where a person's hand ends, relative to the hips, for placing a held object."""
    sx = -16 if side == "l" else 16
    return sx + arm[1][0], -72 + arm[1][1]


# ---------------------------------------------------------------------------
# Props
# ---------------------------------------------------------------------------

def plant(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            '<path d="M-14 0 h28 l-4 30 h-20z" class="m-coral"/>'
            '<path d="M0 0 q-30 -30 -18 -62 q14 18 18 62z" class="m-mint"/>'
            '<path d="M0 0 q26 -24 22 -56 q-16 14 -22 56z" class="m-teal"/>'
            '<path d="M0 0 q-4 -40 6 -74 q10 34 -6 74z" class="m-mint2"/></g>')


def box(x, y, s=1.0, cls="m-kraft"):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-22" y="-20" width="44" height="40" rx="3" class="{cls}"/>'
            '<path d="M-22 -8 h44" class="m-line" stroke-width="2"/>'
            '<rect x="-6" y="-20" width="12" height="16" class="m-tape"/></g>')


def deco_dots(x, y, cols=4, rows=3, gap=14, cls="m-dot"):
    out = "".join(f'<circle cx="{x + c * gap}" cy="{y + r * gap}" r="3"/>' for r in range(rows) for c in range(cols))
    return f'<g class="{cls}">{out}</g>'


def squiggle(x, y, w=80, cls="m-s-blue"):
    n = max(2, w // 20)
    d = f"M{x} {y}" + "".join(" q5 -10 10 0 t10 0" for _ in range(n))
    return f'<path d="{d}" class="{cls}" fill="none" stroke-width="4" stroke-linecap="round"/>'


def screen_card(x, y, w, h, kind="chart"):
    """A floating app card inside a scene."""
    inner = ""
    if kind == "chart":
        bars = [0.45, 0.7, 0.55, 0.9, 0.65, 0.8]
        bw = (w - 40) / len(bars)
        inner = "".join(
            f'<rect x="{x + 20 + i * bw + 4}" y="{y + h - 16 - b * (h - 56)}" width="{bw - 8}" '
            f'height="{b * (h - 56)}" rx="3" class="{"m-blue" if i == 3 else "m-sky"}"/>' for i, b in enumerate(bars))
        inner += f'<rect x="{x + 18}" y="{y + 16}" width="{w * 0.4}" height="8" rx="4" class="m-line-fill"/>'
    elif kind == "list":
        for i in range(4):
            yy = y + 20 + i * ((h - 30) / 4)
            inner += (f'<rect x="{x + 16}" y="{yy}" width="14" height="14" rx="4" class="{"m-mint" if i < 3 else "m-line-fill"}"/>'
                      f'<rect x="{x + 38}" y="{yy + 3}" width="{w * 0.5}" height="8" rx="4" class="m-line-fill"/>')
    elif kind == "sync":
        inner = (f'<circle cx="{x + w / 2}" cy="{y + h / 2}" r="{min(w, h) / 4}" class="m-yellow"/>'
                 f'<path d="M{x + w / 2 - 12} {y + h / 2} l8 8 l16 -18" class="m-s-ink" fill="none" stroke-width="5" '
                 f'stroke-linecap="round" stroke-linejoin="round"/>')
    return (f'<g class="m-float"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" class="m-card"/>'
            f'{inner}</g>')


# ---------------------------------------------------------------------------
# Scenes
# ---------------------------------------------------------------------------

def scene_hero():
    """Two people keep a store and a back office in step: one at the register, one carrying stock."""
    p1 = person(150, 420 - 97 * 1.25, 1.25, skin="m-skin2", shirt="m-coral", pants="m-navy", hair="m-hair1", hair_style=2,
                arm_l=((-10, 34), (6, 64)), arm_r=((34, -30), (70, -64)))
    arm_c = ((26, 30), (10, 52))
    p2 = person(500, 420 - 97 * 1.2, 1.2, skin="m-skin3", shirt="m-mint", pants="m-ink", hair="m-hair2", hair_style=0,
                arm_l=((-20, 36), (-6, 54)), arm_r=arm_c, leg_l=((-18, 40), (-30, 90)), leg_r=((16, 38), (30, 88)))
    return f"""
<svg class="memphis scene-hero" viewBox="0 0 640 440" role="img" aria-label="Illustration: one person points at a stock chart while another carries a box of stock">
  <circle cx="330" cy="220" r="170" class="m-bg1"/>
  <path d="M470 40 l60 0 l-30 52z" class="m-lilac m-spin"/>
  <circle cx="80" cy="90" r="30" class="m-yellow m-bob"/>
  {deco_dots(540, 120)}
  {squiggle(60, 400, 100, "m-s-coral")}
  {squiggle(500, 30, 80, "m-s-blue")}
  <path d="M30 420 h580" class="m-s-ink" stroke-width="3" stroke-linecap="round"/>
  {screen_card(210, 80, 230, 160, "chart")}
  {screen_card(360, 250, 100, 84, "sync")}
  {screen_card(70, 150, 120, 110, "list")}
  {plant(590, 390, 0.9)}
  {p1}
  {p2}
  {box(500 + 12 + 4, 420 - 97 * 1.2 - 30, 1.15)}
</svg>"""


def scene_chaos():
    """Someone buried in spreadsheets and sticky notes: the problem before the project."""
    p = person(300, 410 - 97 * 1.2, 1.2, skin="m-skin1", shirt="m-lilac", pants="m-navy", hair="m-hair3", hair_style=1,
               arm_l=((-36, -20), (-50, -62)), arm_r=((36, -20), (50, -62)))
    papers = "".join(
        f'<g transform="translate({x} {y}) rotate({r})"><rect x="-26" y="-32" width="52" height="64" rx="4" class="m-card"/>'
        f'<path d="M-16 -18 h32 M-16 -6 h32 M-16 6 h22 M-16 18 h28" class="m-s-line" stroke-width="3"/></g>'
        for x, y, r in [(160, 120, -18), (440, 110, 14), (230, 60, 8), (380, 50, -10), (120, 230, 22), (500, 220, -16)])
    notes = "".join(f'<rect x="{x}" y="{y}" width="34" height="34" rx="3" class="{c}" transform="rotate({r} {x} {y})"/>'
                    for x, y, r, c in [(90, 300, -8, "m-yellow"), (520, 300, 10, "m-coral"), (330, 20, 6, "m-mint")])
    return f"""
<svg class="memphis scene-chaos" viewBox="0 0 600 420" role="img" aria-label="Illustration: a person surrounded by flying spreadsheets and sticky notes">
  <circle cx="300" cy="230" r="150" class="m-bg2"/>
  {deco_dots(40, 40)}{squiggle(470, 380, 90, "m-s-blue")}
  <path d="M40 410 h520" class="m-s-ink" stroke-width="3" stroke-linecap="round"/>
  <g class="m-float">{papers}</g>{notes}
  {p}
</svg>"""


def scene_call():
    """A video call at a desk: the scoping call."""
    p = person(200, 300, 1.15, skin="m-skin3", shirt="m-blue", pants="m-ink", hair="m-hair1", hair_style=3,
               arm_l=((24, 30), (60, 40)), arm_r=((30, 30), (66, 36)), leg_l=((30, 6), (34, 70)), leg_r=((36, 4), (42, 70)))
    other = person(0, 0, 0.62, skin="m-skin2", shirt="m-coral", pants="m-coral", hair="m-hair2", hair_style=2,
                   arm_l=((-18, 30), (-10, 50)), arm_r=((30, -20), (40, -50)))
    return f"""
<svg class="memphis scene-call" viewBox="0 0 600 400" role="img" aria-label="Illustration: a person at a desk on a video call">
  <circle cx="380" cy="190" r="150" class="m-bg1"/>
  <circle cx="90" cy="70" r="26" class="m-yellow m-bob"/>{deco_dots(500, 40)}
  {squiggle(60, 380, 90, "m-s-coral")}
  <rect x="210" y="70" width="320" height="210" rx="14" class="m-ink-fill"/>
  <rect x="222" y="82" width="296" height="186" rx="8" class="m-sky"/>
  <g transform="translate(370 248)">{other}</g>
  <rect x="440" y="96" width="62" height="44" rx="6" class="m-card"/>
  <circle cx="471" cy="114" r="9" class="m-skin3"/><path d="M455 140 q16 -18 32 0z" class="m-blue"/>
  <path d="M340 280 h60 l10 30 h-80z" class="m-ink-fill"/>
  <rect x="120" y="300" width="440" height="14" rx="4" class="m-kraft"/>
  <path d="M150 314 v80 M530 314 v80" class="m-s-ink" stroke-width="8" stroke-linecap="round"/>
  <path d="M150 300 q-30 -10 -40 -40 q-4 -20 20 -26 l40 0 l8 66z" class="m-lilac"/>
  {p}
  <rect x="236" y="276" width="70" height="8" rx="3" class="m-line-fill"/>
  {plant(560, 300, 0.7)}
</svg>"""


def scene_handover():
    """Two people pass a binder across: handover and access removed."""
    a = person(210, 410 - 97 * 1.15, 1.15, skin="m-skin2", shirt="m-blue", pants="m-ink", hair="m-hair1", hair_style=3,
               arm_l=((-14, 36), (0, 66)), arm_r=((34, 14), (70, 6)))
    b = person(410, 410 - 97 * 1.15, 1.15, skin="m-skin1", shirt="m-mint", pants="m-navy", hair="m-hair3", hair_style=2,
               arm_l=((-34, 14), (-70, 6)), arm_r=((14, 36), (0, 66)))
    return f"""
<svg class="memphis scene-handover" viewBox="0 0 620 420" role="img" aria-label="Illustration: two people hand over a binder">
  <circle cx="310" cy="220" r="160" class="m-bg2"/>
  <path d="M500 60 l50 0 l-25 44z" class="m-coral m-spin"/>{deco_dots(60, 60)}
  {squiggle(420, 400, 90, "m-s-blue")}
  <path d="M40 410 h540" class="m-s-ink" stroke-width="3" stroke-linecap="round"/>
  {a}{b}
  <g transform="translate(310 {410 - 97 * 1.15 - 66}) rotate(-6)"><rect x="-34" y="-40" width="68" height="80" rx="6" class="m-yellow"/>
  <rect x="-24" y="-28" width="48" height="10" rx="3" class="m-card"/><path d="M-24 -4 h40 M-24 8 h30" class="m-s-ink" stroke-width="3"/></g>
  <g class="m-bob"><circle cx="310" cy="120" r="24" class="m-card"/>
  <path d="M298 120 l8 8 l16 -18" class="m-s-mint" fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g>
</svg>"""


def scene_build():
    """Someone stacks blocks labeled with the apps: the build phase."""
    p = person(170, 395 - 97 * 1.2, 1.2, skin="m-skin3", shirt="m-yellow", pants="m-navy", hair="m-hair2", hair_style=0,
               arm_l=((-20, 36), (-8, 62)), arm_r=((40, -10), (80, -28)))
    blocks = [(330, 290, "m-blue", "Sales"), (430, 290, "m-mint", "Stock"), (380, 230, "m-coral", "Buy"),
              (480, 230, "m-lilac", "Books"), (430, 170, "m-sky", "POS")]
    bl = "".join(f'<g class="m-drop" data-i="{i}"><rect x="{x - 46}" y="{y - 28}" width="92" height="56" rx="8" class="{c}"/>'
                 f'<text x="{x}" y="{y + 6}" class="m-label" text-anchor="middle">{t}</text></g>' for i, (x, y, c, t) in enumerate(blocks))
    return f"""
<svg class="memphis scene-build" viewBox="0 0 620 400" role="img" aria-label="Illustration: a person stacks blocks named Sales, Stock, Buy, Books and POS">
  <circle cx="380" cy="220" r="150" class="m-bg1"/>{deco_dots(60, 50)}
  <circle cx="560" cy="80" r="24" class="m-yellow m-bob"/>{squiggle(70, 390, 90, "m-s-coral")}
  <path d="M40 395 h540" class="m-s-ink" stroke-width="3" stroke-linecap="round"/>
  <rect x="280" y="318" width="250" height="12" rx="4" class="m-kraft"/>
  {bl}{p}
</svg>"""


SCENES = {"hero": scene_hero, "chaos": scene_chaos, "call": scene_call, "handover": scene_handover,
          "build": scene_build}
