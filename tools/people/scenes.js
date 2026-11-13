// Draw the people for the page scenes from Open Peeps (CC0 art by Pablo Stanley; MIT npm port by Emre Cakir)
// into src/media/people/*.svg. Each file is one person, cut out (transparent background), in brand colors.
// The page puts the person in front of a real screen on a solid brand-color panel (kit.scene, .scene in site.css).
// See render.js for setup.
const { load } = require('./render');
const fs = require('fs');
const path = require('path');
const OUT = path.join(__dirname, '..', '..', 'src', 'media', 'people');
const E = load('Effigy').Effigy;
const INK = '#0e1a2e';
const SKIN = { a: '#F2C5A4', b: '#E0A779', c: '#D08B5B', d: '#AE6A3C' };
// Clothes in full brand colors, picked to stand out from the panel each person stands on.
const TOP = { yellow: '#ffc53d', white: '#ffffff', blue: '#2447d8', coral: '#ef6a4c', mint: '#3fc29a', sky: '#9db4ff' };
const VB = [184.2, 210.8, 940.3, 1130.6]; // Effigy bust bounds

// The Computer body has a small mark on the laptop lid that reads as a logo; drop the subpaths inside this box
// (body coordinates) so the laptop is plain.
const PLAIN = { Computer: [790, 350, 890, 445] };
function plain(svg, box) {
  const at = svg.indexOf('<g id="Body"'), end = svg.indexOf('</g>', at);
  if (at < 0) return svg;
  const body = svg.slice(at, end).replace(/ d="([^"]+)"/g, (m, d) => ' d="' + d.split(/(?=M)/).filter(sp => {
    const n = (sp.match(/-?\d+\.?\d*/g) || []).map(Number), xs = n.filter((_, j) => j % 2 === 0), ys = n.filter((_, j) => j % 2 === 1);
    return !(Math.min(...xs) >= box[0] && Math.max(...xs) <= box[2] && Math.min(...ys) >= box[1] && Math.max(...ys) <= box[3]);
  }).join('') + '"');
  return svg.slice(0, at) + body + svg.slice(end);
}

function person(name, p) {
  const o = { skinColor: SKIN[p.skin || 'c'], outlineColor: INK };
  const body = { type: p.body, options: { ...o, topColor: TOP[p.top || 'yellow'], jacketColor: TOP[p.top || 'yellow'], computerColor: '#e8ebf2', paperColor: '#ffffff', cupColor: '#ef6a4c' } };
  const svg = E({ body, head: { type: p.head, options: { ...o, hairColor: p.hair || INK } }, face: { type: p.face || 'Smile', options: o },
    beard: p.beard ? { type: p.beard, options: o } : undefined, accessory: p.acc ? { type: p.acc, options: o } : undefined });
  let inner = (PLAIN[p.body] ? plain(svg, PLAIN[p.body]) : svg).replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, '').replace(/ id="[^"]*"/g, '');
  if (p.flip) inner = `<g transform="translate(${(2 * VB[0] + VB[2]).toFixed(1)} 0) scale(-1 1)">${inner}</g>`;
  let out = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${VB.join(' ')}">${inner}</svg>`;
  out = out.replace(/(\d+\.\d)\d+/g, '$1').replace(/\s+/g, ' ');
  fs.writeFileSync(path.join(OUT, `${name}.svg`), out);
  return out.length;
}

fs.mkdirSync(OUT, { recursive: true });
const PEOPLE = {
  'apparel': { body: 'PolkadotJacket', head: 'Bun', skin: 'a', top: 'yellow' },
  'home-and-furniture': { body: 'Coffee', head: 'GrayShort', skin: 'a', top: 'yellow', beard: 'Chin' },
  'food-and-beverage': { body: 'Explaining', head: 'Afro', skin: 'd', top: 'yellow' },
  'health-and-beauty': { body: 'PointingUp', head: 'LongHair', skin: 'b', top: 'yellow' },
  'wholesale': { body: 'Paper', head: 'Cornrows', skin: 'd', top: 'white' },
  'how-it-works': { body: 'Explaining', head: 'MediumBangs', skin: 'b', top: 'coral' },
  'book': { body: 'Computer', head: 'LongCurly', skin: 'c', top: 'yellow' },
  'notfound': { body: 'Whatever', head: 'ShortTwo', skin: 'b', top: 'yellow', face: 'Calm' },
};
for (const [k, p] of Object.entries(PEOPLE)) console.log(k, person(k, p));
