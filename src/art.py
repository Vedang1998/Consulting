"""People illustrations for the site.

The SVGs in src/art/ are from unDraw (https://undraw.co, by Katerina Limpitsouni), free for
commercial use without attribution under the unDraw license. They are recoloured here at build
time to the brand palette, cleaned for the CSP (no inline style attributes, no ids) and set on a
Memphis backdrop of shapes drawn in CSS.
"""

import re
from functools import lru_cache
from pathlib import Path

ART = Path(__file__).resolve().parent / "art"

# unDraw neutrals and darks -> brand tints and inks. currentColor stays, so CSS sets the accent.
RECOLOR = {
    "#3f3d56": "#24324f", "#3f3d58": "#24324f", "#33323d": "#24324f", "#504f60": "#24324f",
    "#2f2e41": "#141c2b", "#090814": "#141c2b", "#010001": "#141c2b",
    "#65617d": "#8f80f5", "#575a89": "#8f80f5",
    "#e6e6e6": "#e7dfcf", "#e4e4e4": "#e7dfcf", "#f2f2f2": "#f1ebdf", "#f0f0f0": "#f1ebdf",
    "#ccc": "#d6cbb6", "#cacaca": "#d6cbb6", "#d6d6e3": "#d3d9f5", "#e8eaf1": "#e3e8fb",
    "#e6e8ec": "#e3e8fb", "#e3e8f4": "#e3e8fb",
}


@lru_cache(maxsize=None)
def _svg(name):
    s = (ART / f"{name}.svg").read_text()
    s = re.sub(r'\sstyle="[^"]*"', "", s)
    s = re.sub(r'\sid="[^"]*"', "", s)
    s = re.sub(r'#([0-9a-fA-F]{3,6})"', lambda m: RECOLOR.get("#" + m.group(1).lower(), "#" + m.group(1)) + '"', s)
    s = s.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)
    return s


def art(name, color="c-blue", label="", shape="blob", extra=""):
    """An illustration on its backdrop. label is the accessible description ('' = decorative)."""
    role = f' role="img" aria-label="{label}"' if label else ' aria-hidden="true"'
    return (f'<figure class="art {color} art-{shape}"{role}>'
            f'<span class="art-bg"></span><span class="art-s s1"></span><span class="art-s s2"></span>'
            f'<span class="art-s s3"></span><span class="art-dots"></span>'
            f'<span class="art-in">{_svg(name)}</span>{extra}</figure>')
