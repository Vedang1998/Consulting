// Compose brand-colored Open Peeps scenes (CC0 art by Pablo Stanley; MIT npm port by Emre Cakir) into src/media/people/*.svg.
// Each scene is one or two busts standing on the bottom edge of a soft brand-color panel. See render.js for setup.
const { load } = require('./render');
const fs = require('fs');
const path = require('path');
const OUT = path.join(__dirname, '..', '..', 'src', 'media', 'people');
const E = load('Effigy').Effigy;
const INK = '#0e1a2e';
const SKIN = { a: '#F2C5A4', b: '#E0A779', c: '#D08B5B', d: '#AE6A3C', e: '#7A4A2E' };
const TOP = { blue: '#7b95f4', coral: '#f39274', mint: '#5fcaa7', lilac: '#ad9bf3', yellow: '#ffc53d', white: '#ffffff', ink: INK };
const PANEL = { blue: '#e6ecff', coral: '#fde4dc', mint: '#d9f3ea', lilac: '#ebe6ff', yellow: '#fff1cc' };

function bust(p) {
  const o = { skinColor: SKIN[p.skin || 'c'], outlineColor: INK };
  const body = { type: p.body, options: { ...o, topColor: TOP[p.top || 'blue'], computerColor: '#e8ebf2', paperColor: '#ffffff', ...(p.bodyOpts || {}) } };
  let svg = E({ body, head: { type: p.head, options: { ...o, hairColor: p.hair || INK } }, face: { type: p.face || 'Smile', options: o },
    beard: p.beard ? { type: p.beard, options: o } : undefined, accessory: p.acc ? { type: p.acc, options: o } : undefined });
  const inner = svg.replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, '');
  return inner.replace(/ id="[^"]*"/g, '');
}
// Effigy viewBox: x 184..1124, y 211..1341 (940 x 1130). Busts sit on the panel's bottom edge.
function scene(name, panel, people, W = 1200, H = 900) {
  const VB = [184.2, 210.8, 940.3, 1130.6];
  let g = '';
  for (const p of people) {
    const s = p.scale || 0.64, w = VB[2] * s, h = VB[3] * s;
    const x = p.x - w / 2, y = H - h + (p.drop || 0);
    const flip = p.flip ? ` transform="translate(${(2 * p.x).toFixed(1)} 0) scale(-1 1)"` : '';
    g += `<g${flip}><svg x="${x.toFixed(1)}" y="${y.toFixed(1)}" width="${w.toFixed(1)}" height="${h.toFixed(1)}" viewBox="${VB.join(' ')}" overflow="visible">${bust(p)}</svg></g>`;
  }
  let out = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" role="img"><defs><clipPath id="c"><rect width="${W}" height="${H}" rx="40"/></clipPath></defs>` +
    `<g clip-path="url(#c)"><rect width="${W}" height="${H}" fill="${PANEL[panel]}"/>${g}</g></svg>`;
  out = out.replace(/(\d+\.\d)\d+/g, '$1').replace(/\s+/g, ' ');
  fs.writeFileSync(path.join(OUT, `${name}.svg`), out);
  return out.length;
}
fs.mkdirSync(OUT, { recursive: true });
const S = {
  'how-it-works': ['blue', [{ body: 'Explaining', head: 'MediumBangs', skin: 'b', top: 'yellow', x: 330 }, { body: 'Paper', head: 'ShortOne', skin: 'd', top: 'blue', x: 870, flip: true }]],
  'book': ['yellow', [{ body: 'Computer', head: 'LongCurly', skin: 'c', top: 'blue', x: 600, scale: 0.7 }]],
  'apparel': ['coral', [{ body: 'StripedTee', head: 'Bun', skin: 'a', top: 'coral', x: 330 }, { body: 'Jacket', head: 'FlatTop', skin: 'd', top: 'yellow', x: 870, flip: true }]],
  'home-and-furniture': ['lilac', [{ body: 'ButtonShirt', head: 'GrayShort', skin: 'a', top: 'lilac', x: 330, beard: 'Chin' }, { body: 'Computer', head: 'Hijab', skin: 'c', top: 'mint', x: 870, flip: true }]],
  'food-and-beverage': ['mint', [{ body: 'Coffee', head: 'Afro', skin: 'd', top: 'mint', x: 330 }, { body: 'Hoodie', head: 'Beanie', skin: 'b', top: 'coral', x: 870, flip: true }]],
  'health-and-beauty': ['blue', [{ body: 'PolkadotJacket', head: 'LongHair', skin: 'b', top: 'lilac', x: 330 }, { body: 'Tee', head: 'ShortFour', skin: 'd', top: 'blue', acc: 'GlassesTwo', x: 870, flip: true }]],
  'wholesale': ['yellow', [{ body: 'ShirtCoat', head: 'Pomp', skin: 'c', top: 'blue', x: 330, beard: 'Goatee' }, { body: 'Paper', head: 'Cornrows', skin: 'd', top: 'coral', x: 870, flip: true }]],
  'notfound': ['lilac', [{ body: 'Whatever', head: 'ShortTwo', skin: 'b', top: 'yellow', x: 600, face: 'Calm', scale: 0.7 }]],
};
for (const [k, [panel, people]] of Object.entries(S)) console.log(k, scene(k, panel, people));
