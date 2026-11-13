"""Custom spot icons and Memphis shapes, drawn for this site (no third-party license).

Each icon is an ink outline on a 48-unit grid with a color block printed slightly off-register behind it, matching the
cards' offset shadows. The block takes the color of the surrounding tile or card (its --c), or the icon's own color
when it stands alone. Approved by Vee on Nov 12, 2026 (sample sheet v1 in project files, website-previews/icons/).
"""
INK = "#0e1a2e"; PAPER = "#fff"
C = {"blue": "#2f55d4", "coral": "#ff7a59", "mint": "#3ecf9e", "lilac": "#a99bff", "yellow": "#ffc53d"}


def P(d, **kw):
    a = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in kw.items())
    return f'<path d="{d}" {a}/>'


ICONS = {
  "guides": ("blue", "Guides",
    [P("M5 11 Q15 8 24 13 Q33 8 43 11 V37 Q33 34 24 39 Q15 34 5 37 Z")],
    [P("M24 13 Q15 8 5 11 V37 Q15 34 24 39 Q33 34 43 37 V11 Q33 8 24 13 Z"), P("M24 13 V39"),
     P("M10 18 q5-1.4 10 0"), P("M10 24 q5-1.4 10 0"), P("M10 30 q4-1.2 7 0"), P("M28 24 q5-1.4 10 0"), P("M28 30 q5-1.4 10 0"),
     P("M30 10.6 V19 l2.5-2 2.5 2 V9.8", fill=C["coral"])]),
  "questions": ("yellow", "Questions",
    ['<rect x="6" y="7" width="36" height="24" rx="6"/>'],
    [P("M12 7 H36 a6 6 0 0 1 6 6 V25 a6 6 0 0 1 -6 6 H22 L13 39 V31 H12 a6 6 0 0 1 -6 -6 V13 a6 6 0 0 1 6 -6 Z"),
     P("M20 15.6 a4 4 0 1 1 5.6 3.7 c-1 .5-1.6 1.3-1.6 2.3 V22.5"), '<circle cx="24" cy="26.6" r="1.5" fill="#0e1a2e" stroke="none"/>']),
  "inventory": ("lilac", "Stock",
    [P("M8 17 L24 10 L40 17 V33 L24 40 L8 33 Z")],
    [P("M8 17 L24 10 L40 17 V33 L24 40 L8 33 Z"), P("M8 17 L24 24 L40 17"), P("M24 24 V40"), P("M16 13.5 L32 20.5 V26"),
     P("M12 25 v6"), P("M15 26.3 v6"), P("M18 27.6 v6"), P("M20.6 28.8 v6")]),
  "invoice": ("mint", "Invoice paid",
    ['<rect x="10" y="5" width="24" height="35"/>'],
    [P("M10 5 H34 V41 l-4-2.5 -4 2.5 -4-2.5 -4 2.5 -4-2.5 -4 2.5 Z"), P("M15 12 h14"), P("M15 18 h14"), P("M15 24 h8"),
     '<circle cx="35" cy="31" r="7" fill="#ffc53d"/>', P("M31.8 31 l2.2 2.2 4.2-4.4")]),
}


ICONS.update({
  "calendar": ("blue", "Scoping call",
    ['<rect x="6" y="9" width="36" height="32" rx="3"/>'],
    ['<rect x="6" y="9" width="36" height="32" rx="3"/>', P("M6 17 H42"), P("M15 5 v7"), P("M33 5 v7"), P("M17 28.5 l5 5 9-9")]),
  "clock": ("coral", "Business hours",
    ['<circle cx="24" cy="24" r="17"/>'],
    ['<circle cx="24" cy="24" r="17"/>', P("M24 14 V24 L31 28"), P("M24 9 v2"), P("M39 24 h-2"), P("M24 39 v-2"), P("M9 24 h2")]),
  "copy": ("lilac", "A copy to test in",
    ['<rect x="14" y="12" width="26" height="30" rx="2"/>'],
    [P("M8 32 V8 a2 2 0 0 1 2-2 H28"), '<rect x="14" y="12" width="26" height="30" rx="2"/>', P("M19 20 h16"), P("M19 26 h16"), P("M19 32 h10")]),
  "contract": ("blue", "Fixed fee in writing",
    ['<rect x="9" y="5" width="30" height="37" rx="2"/>'],
    ['<rect x="9" y="5" width="30" height="37" rx="2"/>', P("M14 12 h20"), P("M14 18 h20"), P("M14 24 h12"),
     P("M14 34 c2-5 4 2 6-1 s3 2 5 0 2 1 3 0"), P("M13 38 h22")]),
  "key": ("yellow", "Your accounts",
    ['<circle cx="16" cy="17" r="10"/>'],
    [P("M23 24 L40 41"), P("M31 32 l4-4"), P("M36 37 l4-4"), '<circle cx="16" cy="17" r="10"/>', '<circle cx="16" cy="17" r="3" fill="#fff"/>']),
  "checklist": ("yellow", "Testing",
    ['<rect x="9" y="8" width="30" height="34" rx="3"/>'],
    ['<rect x="9" y="8" width="30" height="34" rx="3"/>', '<rect x="17" y="4" width="14" height="7" rx="2" fill="#fff"/>',
     P("M14 20 l2.5 2.5 4-4"), P("M24 20.5 h10"), P("M14 31 l2.5 2.5 4-4"), P("M24 31.5 h10")]),
  "cart": ("coral", "Online store",
    [P("M12 15 H41 L37 30 H15 Z")],
    [P("M12 15 H41 L37 30 H15 Z"), P("M4 8 h6 l5 22"), P("M15 30 l-1.5 5 H38"),
     '<circle cx="18" cy="40" r="3" fill="#fff"/>', '<circle cx="34" cy="40" r="3" fill="#fff"/>']),
  "truck": ("coral", "Purchase and delivery",
    ['<rect x="4" y="12" width="26" height="22" rx="2"/>'],
    ['<rect x="4" y="12" width="26" height="22" rx="2"/>', P("M30 18 H38 L44 25 V34 H30 Z", fill=PAPER),
     P("M33 21 H37 L40 25 H33 Z"), '<circle cx="13" cy="36" r="4" fill="#fff"/>', '<circle cx="36" cy="36" r="4" fill="#fff"/>']),
})

# Industry icons (Nov 13, 2026), drawn in the same style for the industry tiles and pages.
ICONS.update({
  "shirt": ("coral", "Apparel and footwear",
    [P("M17 6 L6 11 L3 21 L11 23 V42 H37 V23 L45 21 L42 11 L31 6 C29.5 10.5 18.5 10.5 17 6 Z")],
    [P("M17 6 L6 11 L3 21 L11 23 V42 H37 V23 L45 21 L42 11 L31 6 C29.5 10.5 18.5 10.5 17 6 Z"),
     P("M11 23 L12 15"), P("M37 23 L36 15"), P("M30 30 h3")]),
  "sofa": ("lilac", "Home and furniture",
    ['<rect x="9" y="11" width="30" height="25" rx="4"/>'],
    ['<rect x="9" y="11" width="30" height="17" rx="4"/>', '<rect x="13" y="26" width="22" height="10" rx="1.5" fill="#fff"/>',
     '<rect x="4" y="21" width="9" height="15" rx="3" fill="#fff"/>', '<rect x="35" y="21" width="9" height="15" rx="3" fill="#fff"/>',
     P("M24 26 v10"), P("M8 36 v4"), P("M40 36 v4")]),
  "jar": ("mint", "Food and beverage",
    [P("M15 14 c-4 1.5 -6 4 -6 8 V37 a5 5 0 0 0 5 5 H34 a5 5 0 0 0 5 -5 V22 c0-4 -2-6.5 -6-8 Z")],
    [P("M15 12 v2 c-4 1.5 -6 4 -6 8 V37 a5 5 0 0 0 5 5 H34 a5 5 0 0 0 5 -5 V22 c0-4 -2-6.5 -6-8 V12"),
     '<rect x="13" y="5" width="22" height="7" rx="2" fill="#fff"/>', '<rect x="13" y="23" width="22" height="11" rx="1.5" fill="#fff"/>',
     P("M17 28.5 h9"), '<circle cx="30.5" cy="28.5" r="1.4" fill="#0e1a2e" stroke="none"/>']),
  "pump": ("blue", "Health and beauty",
    ['<rect x="11" y="20" width="26" height="22" rx="6"/>'],
    ['<rect x="19" y="5" width="11" height="5" rx="1.5" fill="#fff"/>', P("M19 7.5 H12"), P("M24.5 10 V15"),
     '<rect x="18" y="15" width="13" height="5" rx="1.5" fill="#fff"/>', '<rect x="11" y="20" width="26" height="22" rx="6"/>',
     '<rect x="16" y="26" width="16" height="10" rx="1.5" fill="#fff"/>', P("M19.5 31 h9")]),
  "pallet": ("yellow", "Wholesale and distribution",
    ['<rect x="6" y="20" width="36" height="13" rx="1"/>', '<rect x="14" y="7" width="20" height="13" rx="1"/>'],
    ['<rect x="14" y="7" width="20" height="13" rx="1.5"/>', '<rect x="6" y="20" width="17" height="13" rx="1.5" fill="#fff"/>',
     '<rect x="25" y="20" width="17" height="13" rx="1.5"/>', P("M24 7 v4"), P("M14.5 20 v4"), P("M33.5 20 v4"),
     P("M4 36 H44"), P("M4 42 H44"), P("M8 36 v6"), P("M24 36 v6"), P("M40 36 v6")]),
  "tag": ("yellow", "Price",
    [P("M24 5 H40 a3 3 0 0 1 3 3 V24 L24 43 L5 24 Z")],
    [P("M24 5 H40 a3 3 0 0 1 3 3 V24 L24 43 L5 24 Z"), '<circle cx="35" cy="13" r="2.6" fill="#fff"/>', P("M17 25 l8 8"), P("M21 21 l8 8")]),
})


# Clearer icons (Nov 13, 2026, v2). Vee: keep the style, but each icon should show what it stands for at a glance,
# so these use the most familiar picture for each idea: a signpost for a plan, a warehouse for the back office,
# the two-arrow sync mark, a headset for support, a rocket for go-live, a padlock for access removed.
ICONS.update({
  "roadmap": ("lilac", "Systems Roadmap: which way to go",
    [P("M8 9 H33 L39 14.5 L33 20 H8 Z"), P("M40 24 H15 L9 29.5 L15 35 H40 Z")],
    [P("M24 4 V9"), P("M24 20 V24"), P("M24 35 V43"), P("M17 43 H31"),
     P("M8 9 H33 L39 14.5 L33 20 H8 Z"), P("M40 24 H15 L9 29.5 L15 35 H40 Z"), P("M13 14.5 h13"), P("M22 29.5 h13")]),
  "store-move": ("coral", "Store Move: the shop moves to a new platform",
    ['<rect x="8" y="14" width="26" height="26" rx="1"/>'],
    [P("M8 20 V40 H34 V20"), P("M5 14 L8.5 7 H33.5 L37 14"),
     P("M5 14 a4 4 0 0 0 8 0 a4 4 0 0 0 8 0 a4 4 0 0 0 8 0 a4 4 0 0 0 8 0", fill=PAPER),
     P("M15 40 V31 a4 4 0 0 1 8 0 V40", fill=PAPER),
     '<circle cx="37" cy="35" r="8.5" fill="#fff"/>', P("M32.5 35 h9"), P("M38 31.5 l3.5 3.5 -3.5 3.5")]),
  "back-office": ("mint", "Back office: the warehouse and the books",
    [P("M5 19 L24 7 L43 19 V41 H5 Z")],
    [P("M5 19 L24 7 L43 19 V41 H5 Z"), '<rect x="14" y="25" width="20" height="16" rx="1" fill="#fff"/>',
     P("M14 30.5 h20"), P("M14 36 h20"), P("M20 15.5 h8")]),
  "sync": ("blue", "Sync: both systems stay in step",
    ['<circle cx="24" cy="24" r="14.4"/>'],
    [P("M9.6 24 a14.4 14.4 0 0 1 14.4 -14.4 a15.6 15.6 0 0 1 10.8 4.4 L38.4 17.6"), P("M38.4 9.6 v8 h-8"),
     P("M38.4 24 a14.4 14.4 0 0 1 -14.4 14.4 a15.6 15.6 0 0 1 -10.8 -4.4 L9.6 30.4"), P("M17.6 30.4 H9.6 v8")]),
  "support": ("yellow", "Support: someone to ask",
    ['<rect x="6" y="23" width="9" height="14" rx="3.5"/>', '<rect x="33" y="23" width="9" height="14" rx="3.5"/>'],
    [P("M9 26 V22 a15 15 0 0 1 30 0 V26"), '<rect x="6" y="23" width="9" height="14" rx="3.5"/>',
     '<rect x="33" y="23" width="9" height="14" rx="3.5"/>', P("M37.5 37 v1 a5 5 0 0 1 -5 5 H28"),
     '<rect x="20" y="40" width="8" height="6" rx="3" fill="#fff"/>']),
  "videos": ("mint", "Recordings",
    ['<rect x="5" y="9" width="38" height="30" rx="5"/>'],
    ['<rect x="5" y="9" width="38" height="30" rx="5"/>', P("M20 17 L31 24 L20 31 Z", fill=PAPER)]),
  "glossary": ("lilac", "Glossary: terms from A to Z",
    ['<rect x="8" y="5" width="32" height="38" rx="3"/>'],
    ['<rect x="8" y="5" width="32" height="38" rx="3"/>', P("M13 23 L18 11 L23 23"), P("M15 19 h6"),
     P("M27 11 h8 l-8 12 h8"), P("M14 31 h20"), P("M14 37 h13")]),
  "staging": ("mint", "Built in a copy first",
    ['<rect x="5" y="8" width="38" height="31" rx="3"/>'],
    ['<rect x="5" y="8" width="38" height="31" rx="3"/>', P("M5 15 H43"),
     '<circle cx="9.5" cy="11.5" r=".6"/>', '<circle cx="13.5" cy="11.5" r=".6"/>',
     *[P(f"M{24 + 7.2 * c:.1f} {27 + 7.2 * s:.1f} L{24 + 10 * c:.1f} {27 + 10 * s:.1f}", stroke_width="3.2")
       for c, s in [(1, 0), (.707, .707), (0, 1), (-.707, .707), (-1, 0), (-.707, -.707), (0, -1), (.707, -.707)]],
     '<circle cx="24" cy="27" r="7" fill="#fff"/>', '<circle cx="24" cy="27" r="2.6"/>']),
  "go-live": ("coral", "Go-live",
    [P("M24 5 C31 10 33 19 31 30 H17 C15 19 17 10 24 5 Z")],
    [P("M17 22 L11 29 V35 L17 31.5"), P("M31 22 L37 29 V35 L31 31.5"), P("M24 5 C31 10 33 19 31 30 H17 C15 19 17 10 24 5 Z"),
     '<circle cx="24" cy="17" r="3.6" fill="#fff"/>', P("M20 34 C21 39 24 43 24 43 C24 43 27 39 28 34 Z", fill="#ffc53d")]),
  "lock": ("coral", "Access removed",
    ['<rect x="10" y="21" width="28" height="21" rx="4"/>'],
    [P("M16 21 V15 a8 8 0 0 1 16 0 V21"), '<rect x="10" y="21" width="28" height="21" rx="4"/>',
     '<circle cx="24" cy="30" r="2.6" fill="#fff"/>', P("M24 32.6 v4")]),
  "person": ("lilac", "One contact",
    ['<circle cx="24" cy="16" r="8"/>', P("M9 43 c0-9 6.5-14 15-14 s15 5 15 14 Z")],
    ['<circle cx="24" cy="16" r="8"/>', P("M9 43 c0-9 6.5-14 15-14 s15 5 15 14 Z")]),
  "theme": ("lilac", "Online store",
    ['<rect x="5" y="8" width="38" height="32" rx="3"/>'],
    ['<rect x="5" y="8" width="38" height="32" rx="3"/>', P("M5 15 H43"),
     '<circle cx="9.5" cy="11.5" r=".6"/>', '<circle cx="13.5" cy="11.5" r=".6"/>',
     P("M17.5 23 H30.5 L32 35 H16 Z", fill=PAPER), P("M20.5 23 v-1.5 a3.5 3.5 0 0 1 7 0 V23")]),
  "books": ("blue", "The books",
    ['<rect x="10" y="5" width="28" height="38" rx="4"/>'],
    ['<rect x="10" y="5" width="28" height="38" rx="4"/>', '<rect x="15" y="10" width="18" height="8" rx="1.5" fill="#fff"/>',
     *[f'<circle cx="{x}" cy="{y}" r="1.9" fill="#0e1a2e" stroke="none"/>' for y in (25, 31, 37) for x in (18, 24, 30)]]),
  "register": ("blue", "Card reader at the counter",
    ['<rect x="13" y="12" width="22" height="31" rx="4"/>'],
    ['<rect x="16.5" y="4" width="15" height="11" rx="1.5" fill="#fff"/>', '<rect x="13" y="12" width="22" height="31" rx="4"/>',
     '<rect x="17" y="17" width="14" height="8" rx="1.5" fill="#fff"/>',
     *[f'<circle cx="{x}" cy="{y}" r="1.5" fill="#0e1a2e" stroke="none"/>' for y in (30.5, 36.5) for x in (18.5, 24, 29.5)]]),
})

# Lucide names the site already passes for tiles, mapped to the custom icon that replaces them.
SPOT_FOR = {
    "map": "roadmap", "truck": "truck", "store": "store-move", "boxes": "back-office", "warehouse": "inventory",
    "refresh-cw": "sync", "life-buoy": "support", "book-open": "guides", "monitor-smartphone": "theme",
    "package": "inventory", "receipt": "invoice", "credit-card": "register",
    "calendar-check": "calendar", "clock": "clock", "copy": "copy", "file-check-2": "contract",
    "key-round": "key", "shield-check": "lock", "server": "staging", "list-checks": "checklist",
    "package-check": "go-live", "shopping-cart": "cart", "users": "person", "landmark": "books",
}

SHAPES = {
  "squiggle": '<path d="M4 40 q7-14 14 0 t14 0 t14 0 t14 0" fill="none" stroke="#ff7a59" stroke-width="5" stroke-linecap="round"/>',
  "zigzag": '<path d="M5 44 l9-14 9 14 9-14 9 14 9-14 9 14" fill="none" stroke="#2f55d4" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>',
  "triangle": '<path d="M36 12 L58 52 H14 Z" fill="#0e1a2e"/><path d="M32 8 L54 48 H10 Z" fill="#ffc53d" stroke="#0e1a2e" stroke-width="2.5" stroke-linejoin="round"/>',
  "dots": "".join(f'<circle cx="{10 + 11 * i}" cy="{10 + 11 * j}" r="2.6" fill="#a99bff"/>' for i in range(5) for j in range(5)),
  "half-moon": '<path d="M12 44 a22 22 0 0 1 44 0 Z" fill="#0e1a2e" transform="translate(3 3)"/><path d="M10 44 a22 22 0 0 1 44 0 Z" fill="#3ecf9e" stroke="#0e1a2e" stroke-width="2.5" stroke-linejoin="round"/>',
  "ring": '<circle cx="32" cy="32" r="19" fill="none" stroke="#ffc53d" stroke-width="9"/><circle cx="32" cy="32" r="24" fill="none" stroke="#0e1a2e" stroke-width="2"/>',
  "confetti": ('<g stroke-width="5" stroke-linecap="round" fill="none"><path d="M10 14 l8 -6" stroke="#ff7a59"/><path d="M34 10 l3 9" stroke="#2f55d4"/>'
               '<path d="M50 20 l8 2" stroke="#3ecf9e"/><path d="M16 38 l-2 9" stroke="#ffc53d"/><path d="M38 34 l8 6" stroke="#a99bff"/>'
               '<path d="M26 54 l9 -2" stroke="#0e1a2e"/><path d="M52 50 l4 -7" stroke="#ff7a59"/></g>'),
  "stripe-pill": ('<defs><clipPath id="pc"><rect x="6" y="20" width="52" height="24" rx="12"/></clipPath></defs>'
                  '<rect x="9" y="23" width="52" height="24" rx="12" fill="#0e1a2e"/><rect x="6" y="20" width="52" height="24" rx="12" fill="#fff"/>'
                  '<g clip-path="url(#pc)" stroke="#2f55d4" stroke-width="4">' + "".join(f'<path d="M{x} 48 L{x + 28} 16"/>' for x in range(-20, 60, 9)) + '</g>'
                  '<rect x="6" y="20" width="52" height="24" rx="12" fill="none" stroke="#0e1a2e" stroke-width="2.5"/>'),
  "plus": '<path d="M32 12 V52 M12 32 H52" stroke="#2f55d4" stroke-width="9" stroke-linecap="round"/>',
  "blob": '<path d="M34 8 C48 8 58 20 54 34 C50 50 34 58 22 52 C8 46 6 30 12 20 C16 12 24 8 34 8 Z" fill="#eeebff" stroke="#0e1a2e" stroke-width="2.5"/>',
}


def icon(name, cls=""):
    """Inline a spot icon. Its color block follows the nearest --c, else the icon's own color."""
    col, label, fills, inks = ICONS[name]
    c = f"spot sd-{col} {cls}".strip()
    return (f'<svg class="{c}" viewBox="0 0 48 48" aria-hidden="true" focusable="false">'
            f'<g class="sp-c" transform="translate(2.5 2.5)">{"".join(fills)}</g>'
            f'<g fill="none" stroke="{INK}" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round">{"".join(inks)}</g></svg>')


def shape(name, cls=""):
    """Inline a Memphis shape (decoration only)."""
    return f'<svg class="{('mshape ' + cls).strip()}" viewBox="0 0 64 64" aria-hidden="true" focusable="false">{SHAPES[name]}</svg>'


# Brand shapes for the navy heroes: flat brand colors, no outline, used two at a time behind the corners of the hero
# art (kit.deco). Few and small on purpose (Vee, Nov 13: "in limit, to stay professional").
DECO = {
  "ring": '<circle cx="32" cy="32" r="21" fill="none" stroke="#ffc53d" stroke-width="8"/>',
  "squiggle": '<path d="M4 34 q7-14 14 0 t14 0 t14 0 t14 0" fill="none" stroke="#ff7a59" stroke-width="5.5" stroke-linecap="round"/>',
  "dots": "".join(f'<circle cx="{8 + 12 * i}" cy="{8 + 12 * j}" r="2.6" fill="#a08cff"/>' for i in range(5) for j in range(5)),
  "half": '<path d="M8 46 a24 24 0 0 1 48 0 Z" fill="#34c79a"/>',
  "plus": '<path d="M32 10 V54 M10 32 H54" stroke="#6d8bff" stroke-width="9" stroke-linecap="round"/>',
  "tri": '<path d="M32 8 L57 52 H7 Z" fill="#ffc53d"/>',
  "zig": '<path d="M4 40 l10-15 10 15 10-15 10 15 10-15 6 9" fill="none" stroke="#6d8bff" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>',
}


def deco(name, cls=""):
    return f'<svg class="deco {cls}" viewBox="0 0 64 64" aria-hidden="true" focusable="false">{DECO[name]}</svg>'
