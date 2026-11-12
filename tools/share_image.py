"""Share image (src/og.png, 1200x630) from the site's own fonts, spot icons and shapes.

    python3 tools/share_image.py && node tools/shot.js
writes tools/og.html, then renders it to src/og.png with Playwright. Edit the copy below, then rerun.
"""
import sys
from pathlib import Path
SRC = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC))
import spot as S
FONTS = SRC / "fonts"
ill = ""
right = (f'<img class="ill" src="{ill}" alt="">' if ill else
  f'''<div class="chain">
    <div class="tile t1">{S.icon("store-move")}</div>
    <svg class="path p1" viewBox="0 0 100 20"><path d="M2 10 C 30 -4, 70 24, 98 10" fill="none" stroke="#141c2b" stroke-width="3.2" stroke-dasharray="0.1 8" stroke-linecap="round"/></svg>
    <div class="tile t2">{S.icon("inventory")}</div>
    <svg class="path p2" viewBox="0 0 100 20"><path d="M2 10 C 30 24, 70 -4, 98 10" fill="none" stroke="#141c2b" stroke-width="3.2" stroke-dasharray="0.1 8" stroke-linecap="round"/></svg>
    <div class="tile t3">{S.icon("invoice")}</div>
  </div>''')
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: Archivo; src: url({FONTS}/archivo-latin-wght-normal.woff2) format("woff2"); font-weight: 100 900; }}
@font-face {{ font-family: Plex; src: url({FONTS}/ibm-plex-sans-latin-500-normal.woff2) format("woff2"); font-weight: 500; }}
@font-face {{ font-family: PlexMono; src: url({FONTS}/ibm-plex-mono-latin-500-normal.woff2) format("woff2"); font-weight: 500; }}
html, body {{ margin: 0; }}
body {{ width: 1200px; height: 630px; background: #fbf7f0; color: #141c2b; position: relative; overflow: hidden; }}
.copy {{ position: absolute; left: 72px; top: 92px; width: 600px; }}
.eyebrow {{ font: 500 19px/1 PlexMono; letter-spacing: .08em; text-transform: uppercase; display: flex; align-items: center; gap: 14px; margin-bottom: 30px; }}
.eyebrow i {{ width: 34px; height: 12px; background: #ffc53d; border: 2px solid #141c2b; border-radius: 6px; }}
h1 {{ font: 820 66px/1.02 Archivo; letter-spacing: -.035em; margin: 0 0 30px; }}
h1 span {{ background: linear-gradient(transparent 62%, #ffc53d 62%, #ffc53d 92%, transparent 92%); }}
p {{ font: 500 24px/1.4 Plex; color: #4f5868; margin: 0; }}
.ill {{ position: absolute; right: 36px; top: 115px; width: 500px; border-radius: 24px; }}
.chain {{ position: absolute; right: 64px; top: 170px; width: 470px; height: 300px; }}
.tile {{ position: absolute; width: 132px; height: 132px; background: #fff; border: 2.5px solid #141c2b; border-radius: 24px; box-shadow: 7px 7px 0 #141c2b; display: grid; place-items: center; }}
.tile svg {{ width: 92px; height: 92px; overflow: visible; }}
.t1 {{ left: 0; top: 30px; }} .t2 {{ left: 170px; top: 150px; }} .t3 {{ left: 338px; top: 10px; }}
.path {{ position: absolute; width: 110px; height: 30px; }}
.p1 {{ left: 104px; top: 160px; transform: rotate(34deg); }} .p2 {{ left: 272px; top: 150px; transform: rotate(-38deg); }}
.sp-c {{ fill: var(--sp); }}
.sd-blue {{ --sp: #2f55d4; }} .sd-coral {{ --sp: #ff7a59; }} .sd-mint {{ --sp: #3ecf9e; }} .sd-lilac {{ --sp: #a99bff; }} .sd-yellow {{ --sp: #ffc53d; }}
.mshape {{ position: absolute; overflow: visible; }}
.m1 {{ width: 92px; left: 640px; top: 40px; }} .m2 {{ width: 70px; right: 40px; top: 470px; }}
.m3 {{ width: 54px; left: 690px; top: 500px; }} .m4 {{ width: 64px; right: 60px; top: 30px; }}
.foot {{ position: absolute; left: 0; right: 0; bottom: 0; height: 14px; background: #2f55d4; border-top: 2.5px solid #141c2b; }}
</style></head><body>
<div class="copy">
  <div class="eyebrow"><i></i>Shopify and Odoo consulting</div>
  <h1><span>One stock count</span> across your store, your registers and Odoo</h1>
  <p>Fixed fee and written scope before work starts</p>
</div>
{right}
{S.shape("squiggle", "m1")}{S.shape("half-moon", "m2")}{S.shape("dots", "m3")}{S.shape("triangle", "m4")}
<div class="foot"></div>
</body></html>"""
Path(__file__).with_name("og.html").write_text(html)
