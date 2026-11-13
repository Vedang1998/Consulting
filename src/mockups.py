"""Icons and sample documents for the [DBA name] site.

The sample documents are drawn in HTML by us with sample data and carry a visible "Sample" label.
None is a client document. Real screens and recordings live in src/media and are listed in config.
"""

import re
from pathlib import Path

ICONS = Path(__file__).resolve().parent / "icons"
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
    body = "".join(f'<tr><td data-l="Shopify">{a}</td><td data-l="Odoo">{b}</td><td data-l="Direction">{c}</td></tr>'
                   for a, b, c in rows)
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
