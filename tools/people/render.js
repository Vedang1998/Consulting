// Render Open Peeps to plain SVG strings, without React.
// Art: Open Peeps by Pablo Stanley, CC0 (openpeeps.com). Pieces come from the MIT npm port @opeepsfun/open-peeps@1.0.6.
// Get it outside the repo:  npm pack @opeepsfun/open-peeps@1.0.6 && tar xzf opeepsfun-open-peeps-1.0.6.tgz
// then pass its build folder:  OPEEPS=/path/to/package/build node tools/people/scenes.js
const fs = require('fs'), path = require('path'), vm = require('vm');
const BUILD = path.resolve(process.env.OPEEPS || 'package/build');
const Fragment = Symbol('frag');
const KEEP = new Set(['viewBox', 'preserveAspectRatio', 'gradientTransform', 'gradientUnits', 'patternUnits', 'clipPathUnits', 'maskUnits']);
const kebab = k => k === 'className' ? 'class' : k === 'xlinkHref' ? 'xlink:href' : KEEP.has(k) ? k : k.replace(/[A-Z]/g, m => '-' + m.toLowerCase());
function h(type, props, ...kids) {
  props = props || {};
  kids = kids.flat(Infinity).filter(k => k !== null && k !== undefined && k !== false);
  if (type === Fragment) return kids.join('');
  if (typeof type === 'function') return type({ ...props, children: kids });
  const attrs = Object.entries(props).filter(([k, v]) => k !== 'children' && v !== undefined && v !== null && k !== 'style')
    .map(([k, v]) => ` ${kebab(k)}="${String(v).replace(/"/g, '&quot;')}"`).join('');
  return `<${type}${attrs}>${kids.join('')}</${type}>`;
}
const React = { createElement: h, Fragment };
const cache = {};
function load(rel) {
  const f = path.join(BUILD, rel.endsWith('.js') ? rel : rel + '.js');
  if (cache[f]) return cache[f];
  let src = fs.readFileSync(f, 'utf8');
  src = src.replace(/import React from "react";/, '').replace(/export var (\w+) =/g, 'var $1 = exports.$1 =')
           .replace(/export default (\w+);/, 'exports.default = $1;').replace(/export \{[^}]*\} from [^;]+;/g, '');
  const exports = {};
  const req = p => load(path.join(path.dirname(path.relative(BUILD, f)), p));
  vm.runInNewContext(src, { React, exports, require: req, module: { exports } }, { filename: f });
  return (cache[f] = exports);
}
function piece(dir, type, opts) { const m = load(`${dir}/${type}`); return { svg: h(m.default, opts || {}), cfg: m[type + 'Config'] }; }
module.exports = { piece, load, h, React };
