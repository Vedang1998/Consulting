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
  "roadmap": ("lilac", "Systems Roadmap",
    ['<path d="M6 12 L17 8 L31 12 L42 8 V36 L31 40 L17 36 L6 40 Z"/>'],
    [P("M6 12 L17 8 L31 12 L42 8 V36 L31 40 L17 36 L6 40 Z"), P("M17 8 V36"), P("M31 12 V40"),
     P("M10 33 C14 27 18 34 23 28 S30 25 32 27", stroke_dasharray="0.01 4.2"),
     P("M35 28 s-5-4.5-5-8.5 a5 5 0 0 1 10 0 c0 4-5 8.5-5 8.5z", fill=PAPER), '<circle cx="35" cy="19.5" r="1.4" fill="#0e1a2e" stroke="none"/>']),
  "store-move": ("coral", "Store Move",
    ['<rect x="10" y="14" width="28" height="26" rx="1"/>'],
    [P("M10 22 V40 H38 V22"), P("M7 16 L10 8 H38 L41 16"),
     P("M7 16 a4.25 4.25 0 0 0 8.5 0 a4.25 4.25 0 0 0 8.5 0 a4.25 4.25 0 0 0 8.5 0 a4.25 4.25 0 0 0 8.5 0", fill=PAPER),
     P("M20 40 V31 a4 4 0 0 1 8 0 V40", fill=PAPER), P("M1.5 27 h4"), P("M0.5 32 h5"), P("M2.5 37 h3")]),
  "back-office": ("mint", "Back Office Launch",
    ['<rect x="6" y="9" width="36" height="31" rx="2"/>'],
    ['<rect x="15.5" y="8" width="17" height="15" rx="1.5" fill="#fff"/>', '<rect x="6" y="24" width="17" height="15" rx="1.5" fill="#fff"/>',
     '<rect x="25" y="24" width="17" height="15" rx="1.5" fill="#fff"/>', P("M24 8 v5"), P("M14.5 24 v5"), P("M33.5 24 v5"),
     P("M19 19 h5"), P("M9.5 35 h5"), P("M28.5 35 h5")]),
  "sync": ("blue", "Store to Back Office Sync",
    ['<circle cx="24" cy="24" r="15"/>'],
    ['<rect x="4" y="16" width="15" height="16" rx="2.5" fill="#fff"/>', '<rect x="29" y="16" width="15" height="16" rx="2.5" fill="#fff"/>',
     P("M4 21.5 h15"), P("M8 26.5 h7"), P("M36.5 16 v5"), P("M33 27 h7"),
     P("M11.5 12.5 C12 5.5 36 5.5 36.5 11.5"), P("M33 9 l3.5 3.5 3.5-3.5"),
     P("M36.5 35.5 C36 42.5 12 42.5 11.5 36.5"), P("M15 39 l-3.5-3.5 -3.5 3.5")]),
  "support": ("yellow", "Support block",
    ['<circle cx="24" cy="24" r="17"/>'],
    ['<circle cx="24" cy="24" r="17"/>', '<circle cx="24" cy="24" r="7.5" fill="#fff"/>', P("M18.7 18.7 12 12"), P("M29.3 18.7 36 12"),
     P("M18.7 29.3 12 36"), P("M29.3 29.3 36 36")]),
  "guides": ("blue", "Guides",
    [P("M5 11 Q15 8 24 13 Q33 8 43 11 V37 Q33 34 24 39 Q15 34 5 37 Z")],
    [P("M24 13 Q15 8 5 11 V37 Q15 34 24 39 Q33 34 43 37 V11 Q33 8 24 13 Z"), P("M24 13 V39"),
     P("M10 18 q5-1.4 10 0"), P("M10 24 q5-1.4 10 0"), P("M10 30 q4-1.2 7 0"), P("M28 24 q5-1.4 10 0"), P("M28 30 q5-1.4 10 0"),
     P("M30 10.6 V19 l2.5-2 2.5 2 V9.8", fill=C["coral"])]),
  "videos": ("mint", "Videos",
    ['<rect x="5" y="8" width="38" height="26" rx="3"/>'],
    ['<rect x="5" y="8" width="38" height="26" rx="3"/>', P("M20.5 14 L30 19.5 L20.5 25 Z", fill=PAPER),
     P("M10 29.5 H38"), '<circle cx="18" cy="29.5" r="1.9" fill="#0e1a2e"/>', P("M24 34 v5"), P("M16 40 h16")]),
  "questions": ("yellow", "Questions",
    ['<rect x="6" y="7" width="36" height="24" rx="6"/>'],
    [P("M12 7 H36 a6 6 0 0 1 6 6 V25 a6 6 0 0 1 -6 6 H22 L13 39 V31 H12 a6 6 0 0 1 -6 -6 V13 a6 6 0 0 1 6 -6 Z"),
     P("M20 15.6 a4 4 0 1 1 5.6 3.7 c-1 .5-1.6 1.3-1.6 2.3 V22.5"), '<circle cx="24" cy="26.6" r="1.5" fill="#0e1a2e" stroke="none"/>']),
  "tools": ("coral", "Tools",
    ['<rect x="7" y="7" width="34" height="34" rx="5"/>'],
    ['<rect x="7" y="7" width="34" height="34" rx="5"/>', P("M12 15 H36"), P("M12 24 H36"), P("M12 33 H36"),
     '<circle cx="29" cy="15" r="3.5" fill="#fff"/>', '<circle cx="18" cy="24" r="3.5" fill="#fff"/>', '<circle cx="26" cy="33" r="3.5" fill="#fff"/>']),
  "inventory": ("lilac", "Stock",
    [P("M8 17 L24 10 L40 17 V33 L24 40 L8 33 Z")],
    [P("M8 17 L24 10 L40 17 V33 L24 40 L8 33 Z"), P("M8 17 L24 24 L40 17"), P("M24 24 V40"), P("M16 13.5 L32 20.5 V26"),
     P("M12 25 v6"), P("M15 26.3 v6"), P("M18 27.6 v6"), P("M20.6 28.8 v6")]),
  "invoice": ("mint", "Invoice paid",
    ['<rect x="10" y="5" width="24" height="35"/>'],
    [P("M10 5 H34 V41 l-4-2.5 -4 2.5 -4-2.5 -4 2.5 -4-2.5 -4 2.5 Z"), P("M15 12 h14"), P("M15 18 h14"), P("M15 24 h8"),
     '<circle cx="35" cy="31" r="7" fill="#ffc53d"/>', P("M31.8 31 l2.2 2.2 4.2-4.4")]),
  "register": ("blue", "Register sale",
    ['<rect x="12" y="4" width="22" height="39" rx="4"/>'],
    ['<rect x="12" y="4" width="22" height="39" rx="4"/>', '<rect x="16" y="8.5" width="14" height="9" rx="1.5" fill="#fff"/>',
     *[f'<circle cx="{x}" cy="{y}" r=".4"/>' for y in (24, 29.5, 35) for x in (18, 23, 28)],
     P("M38 15 a5 5 0 0 1 0 8"), P("M41.5 11.5 a10 10 0 0 1 0 15")]),
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
  "branch": ("mint", "Change control",
    ['<circle cx="14" cy="10" r="5"/>', '<circle cx="14" cy="38" r="5"/>', '<circle cx="34" cy="14" r="5"/>'],
    [P("M14 14 V34"), P("M34 18 C34 28 14 24 14 33"), '<circle cx="14" cy="10" r="4"/>', '<circle cx="14" cy="38" r="4"/>',
     '<circle cx="34" cy="14" r="4"/>']),
  "key": ("yellow", "Your accounts",
    ['<circle cx="16" cy="17" r="10"/>'],
    [P("M23 24 L40 41"), P("M31 32 l4-4"), P("M36 37 l4-4"), '<circle cx="16" cy="17" r="10"/>', '<circle cx="16" cy="17" r="3" fill="#fff"/>']),
  "shield": ("coral", "Access removed",
    [P("M24 5 L39 10 V22 C39 32 32 39 24 43 C16 39 9 32 9 22 V10 Z")],
    [P("M24 5 L39 10 V22 C39 32 32 39 24 43 C16 39 9 32 9 22 V10 Z"), P("M17 24 l5 5 9-10")]),
  "staging": ("mint", "Built in staging",
    ['<rect x="7" y="8" width="34" height="32" rx="3"/>'],
    ['<rect x="7" y="8" width="34" height="14" rx="3"/>', '<rect x="7" y="26" width="34" height="14" rx="3"/>',
     '<circle cx="13.5" cy="15" r="1.4" fill="#0e1a2e" stroke="none"/>', '<circle cx="13.5" cy="33" r="1.4" fill="#0e1a2e" stroke="none"/>',
     P("M25 15 h10"), P("M25 33 h10")]),
  "checklist": ("yellow", "Testing",
    ['<rect x="9" y="8" width="30" height="34" rx="3"/>'],
    ['<rect x="9" y="8" width="30" height="34" rx="3"/>', '<rect x="17" y="4" width="14" height="7" rx="2" fill="#fff"/>',
     P("M14 20 l2.5 2.5 4-4"), P("M24 20.5 h10"), P("M14 31 l2.5 2.5 4-4"), P("M24 31.5 h10")]),
  "go-live": ("coral", "Go-live",
    [P("M6 17 L22 10 L38 17 V33 L22 40 L6 33 Z")],
    [P("M6 17 L22 10 L38 17 V33 L22 40 L6 33 Z"), P("M6 17 L22 24 L38 17"), P("M22 24 V40"),
     '<circle cx="36" cy="34" r="7.5" fill="#fff"/>', P("M32.6 34 l2.3 2.3 4.4-4.6")]),
  "cart": ("coral", "Online store",
    [P("M12 15 H41 L37 30 H15 Z")],
    [P("M12 15 H41 L37 30 H15 Z"), P("M4 8 h6 l5 22"), P("M15 30 l-1.5 5 H38"),
     '<circle cx="18" cy="40" r="3" fill="#fff"/>', '<circle cx="34" cy="40" r="3" fill="#fff"/>']),
  "people": ("lilac", "One person throughout",
    ['<circle cx="19" cy="16" r="6"/>', P("M7 40 c0-7 5-12 12-12 s12 5 12 12 Z")],
    ['<circle cx="33" cy="17" r="5" fill="#fff"/>', P("M32 28 c5 0 9 4 9 11"), '<circle cx="19" cy="16" r="6"/>',
     P("M7 40 c0-7 5-12 12-12 s12 5 12 12 Z")]),
  "bank": ("blue", "Bank and books",
    ['<rect x="8" y="17" width="32" height="22"/>'],
    [P("M5 17 L24 6 L43 17 Z", fill=PAPER), P("M11 21 V34"), P("M19 21 V34"), P("M29 21 V34"), P("M37 21 V34"), P("M8 38 H40"), P("M5 42 H43")]),
  "theme": ("lilac", "Store theme",
    ['<rect x="5" y="8" width="38" height="32" rx="3"/>'],
    ['<rect x="5" y="8" width="38" height="32" rx="3"/>', P("M5 15 H43"), '<circle cx="9.5" cy="11.5" r=".5"/>',
     '<circle cx="13.5" cy="11.5" r=".5"/>', '<rect x="10" y="19" width="28" height="8" rx="1.5" fill="#fff"/>',
     '<rect x="10" y="30.5" width="7.5" height="5" rx="1"/>', '<rect x="20.25" y="30.5" width="7.5" height="5" rx="1"/>',
     '<rect x="30.5" y="30.5" width="7.5" height="5" rx="1"/>']),
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

# Lucide names the site already passes for tiles, mapped to the custom icon that replaces them.
SPOT_FOR = {
    "map": "roadmap", "truck": "truck", "store": "store-move", "boxes": "back-office", "warehouse": "inventory",
    "refresh-cw": "sync", "life-buoy": "support", "book-open": "guides", "monitor-smartphone": "theme",
    "calculator": "tools", "package": "inventory", "receipt": "invoice", "credit-card": "register",
    "calendar-check": "calendar", "clock": "clock", "copy": "copy", "file-check-2": "contract", "git-branch": "branch",
    "key-round": "key", "shield-check": "shield", "server": "staging", "list-checks": "checklist",
    "package-check": "go-live", "shopping-cart": "cart", "users": "people", "landmark": "bank",
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
