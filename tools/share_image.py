"""Share image (src/og.png, 1200x630) in the v6 look: navy ground, the yellow highlight, spot icons, two flat shapes.

    python3 tools/share_image.py && node tools/shot.js
writes tools/og.html, then renders it to src/og.png with Playwright. Edit the copy below, then rerun.
No people, no Memphis scenes, no prices of ours (Vee, Nov 13, 2026).
"""
import sys
from pathlib import Path
SRC = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC))
import spot as S  # noqa: E402
FONTS = SRC / "fonts"

STEPS = [("theme", "lilac", "Online store and registers"), ("sync", "blue", "The link between them"),
         ("back-office", "mint", "Stock and purchasing"), ("books", "blue", "The books")]
TINT = {"lilac": "#eeebff", "blue": "#e6ecff", "mint": "#ddf6ec"}
steps = "".join(f'<li><span class="tile" style="background:{TINT[t]}">{S.icon(i)}</span><b>{label}</b></li>'
                for i, t, label in STEPS)
dots = "".join(f'<circle cx="{8 + 12 * i}" cy="{8 + 12 * j}" r="2.6" fill="#a08cff"/>' for i in range(5) for j in range(5))
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: Archivo; src: url({FONTS}/archivo-latin-wght-normal.woff2) format("woff2"); font-weight: 100 900; }}
@font-face {{ font-family: Plex; src: url({FONTS}/ibm-plex-sans-latin-500-normal.woff2) format("woff2"); font-weight: 500; }}
@font-face {{ font-family: Plex; src: url({FONTS}/ibm-plex-sans-latin-600-normal.woff2) format("woff2"); font-weight: 600; }}
html, body {{ margin: 0; }}
body {{ width: 1200px; height: 630px; position: relative; overflow: hidden; background: #0e1a2e; color: #fff;
  background-image: radial-gradient(#22324f 1.4px, transparent 1.6px); background-size: 26px 26px; background-position: 13px 13px; }}
.copy {{ position: absolute; left: 72px; top: 96px; width: 640px; }}
.kicker {{ font: 600 22px/1 Plex; color: #aeb9cc; margin: 0 0 26px; }}
h1 {{ font: 820 64px/1.04 Archivo; letter-spacing: -.035em; margin: 0 0 30px; }}
mark {{ color: inherit; background: linear-gradient(transparent 84%, #ffc53d 84%, #ffc53d 100%); }}
p {{ font: 500 25px/1.4 Plex; color: #c9d2e1; margin: 0; max-width: 560px; }}
ol {{ position: absolute; right: 70px; top: 92px; width: 330px; margin: 0; padding: 22px 24px; list-style: none; background: #fff;
  border-radius: 20px; display: grid; gap: 14px; color: #0e1a2e; }}
li {{ display: flex; align-items: center; gap: 18px; position: relative; }}
li + li::before {{ content: ""; position: absolute; left: 33px; top: -16px; height: 18px; border-left: 2.5px dashed #8a93a3; }}
.tile {{ width: 68px; height: 68px; border-radius: 16px; display: grid; place-items: center; flex: none; }}
.tile svg {{ width: 50px; height: 50px; overflow: visible; }}
b {{ font: 600 21px/1.25 Plex; }}
.sp-c {{ fill: var(--sp); }}
.sd-blue {{ --sp: #2f55d4; }} .sd-coral {{ --sp: #ff7a59; }} .sd-mint {{ --sp: #3ecf9e; }} .sd-lilac {{ --sp: #a99bff; }} .sd-yellow {{ --sp: #ffc53d; }}
.ring {{ position: absolute; right: 36px; top: 40px; width: 84px; }}
.dots {{ position: absolute; right: 360px; bottom: 44px; width: 74px; }}
</style></head><body>
<svg class="ring" viewBox="0 0 64 64"><circle cx="32" cy="32" r="21" fill="none" stroke="#ffc53d" stroke-width="8"/></svg>
<div class="copy">
  <p class="kicker">Ecommerce and ERP consulting</p>
  <h1>Shopify and Odoo consulting for <mark>retailers and wholesalers</mark></h1>
  <p>A fixed fee and a written scope, quoted after a free call.</p>
</div>
<ol>{steps}</ol>
<svg class="dots" viewBox="0 0 64 64">{dots}</svg>
</body></html>"""
Path(__file__).with_name("og.html").write_text(html)
