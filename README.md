# [DBA name] website

Static site for [DBA name] (IVYY LLC), a remote Shopify and Odoo consultancy. Python standard library
only, no frameworks. Hosted on Cloudflare Workers with Static Assets, built and deployed by Cloudflare
Workers Builds from this repository.

## Layout

| Path | What it holds |
| --- | --- |
| `src/config.py` | Every business fact: name, domain, contact, booking link, prices, promises, offer, profiles, demo videos. Most changes happen here. `# CONFIRM` marks values Vee must supply. |
| `src/build.py` | Page templates and copy, site files (`_headers`, `_redirects`, `robots.txt`, `sitemap.xml`, `llms.txt`) and the output checks. |
| `src/content.py` | Resources copy: the FAQ answers (`FAQ_SHOPIFY`, `FAQ_ODOO`, `FAQ_US`), the guides (`GUIDES`) and the video chapters and transcripts (`VIDEOS`). Prices and limits carry the date they were checked. |
| `src/spot.py` | Custom spot icons (27, drawn for this site, no third-party license) and Memphis shapes. `SPOT_FOR` maps the Lucide names the pages pass to the custom icon that replaces them in tiles, doors, cards and service links. |
| `src/mockups.py` | The drawn workflow demos, sample documents, small illustrations and the icon helper. |
| `src/art/`, `src/art.py` | People illustrations from unDraw (undraw.co, free for commercial use, no attribution needed under the unDraw license), recoloured to the brand palette at build and set on CSS Memphis backdrops. Don't repackage them as an illustration set. |
| `src/media/odoo/` | Real Odoo 20 Community screen recordings (MP4 and WebM, with posters) and screenshots, made in our own demo database with Odoo's sample data. Listed in `ODOO_REEL` and `SCREENS` in config. `tour/` holds the guided tour steps listed in `ODOO_TOURS`. |
| `src/site.css` | Design system, light only. No inline style attributes anywhere (the CSP is `style-src 'self'`); scripts set positions through `el.style`, which the CSP allows. |
| `src/site.js` | Demo tabs, service finder, guided Odoo tours, the stock sync model, resource filters, video chapters, the Shopify plan picker, scroll reveals, the first-party visit counter and the privacy opt-out. |
| `src/fonts/` | Self-hosted Archivo, IBM Plex Sans and IBM Plex Mono (OFL). |
| `src/icons/` | Lucide icons (ISC), inlined at build. |
| `src/og.png`, `src/apple-touch-icon.png` | Share image (1200x630) and phone home-screen icon. The share image is drawn by `tools/share_image.py` from the site's fonts, spot icons and shapes; run it, then `node tools/shot.js` to render a new `src/og.png`. No AI images. |
| `worker/index.js` | The Worker on `/api/*` and `/media/*`. Media requests get byte ranges (206), which Safari needs to play video; Cloudflare's static assets ignore Range on their own. On `/api/*` it writes visit events to Workers Analytics Engine, sets one HttpOnly cookie, stores no IP or contact details, honors the opt-out cookie and Global Privacy Control. |
| `wrangler.jsonc` | Workers config: assets from `dist/`, Worker first for `/api/*` and `/media/*`, 404 page, Analytics Engine binding. |
| `dist/` | Build output, git-ignored. |

## Commands

```sh
npm run staging   # python3 src/build.py: builds with a "Staging build" strip, noindex header and Disallow robots.txt
npm run build     # python3 src/build.py --release: the launch build, fails while launch blockers remain
npm run preview   # staging build, then the real Workers runtime on http://localhost:8787
```

A good build ends with `Built N indexable pages`. The build fails on: an em dash, an en dash outside a
number range, a banned buzzword from the project instructions, an exclamation mark in a heading, emoji,
a 555 number, over-sharing phrases, a title over 66 characters, or an offer without an end date, regular
price, capacity and terms.

## Publish on Cloudflare

Tested locally on Nov 10, 2026 with the pinned Wrangler: pages, 301 redirects, the 404 page, security
headers, long-cache headers on `/assets/` and `/fonts/`, and the `/api/e` counter all respond as expected.

1. Merge the site into `main` (Vee says "merge" in the project thread).
2. Cloudflare dashboard, Workers & Pages, Create, Import a repository. Pick this repository.
3. Build settings:
   - Build command: `npm run staging` for a first look, `npm run build` for launch
   - Deploy command: `npx wrangler deploy`
   - Root directory: `/`, production branch: `main`
4. Save and deploy. The site appears at `dba-site.<your-subdomain>.workers.dev`. Staging builds tell
   search engines not to index them.
5. Before launch, set the real values in `src/config.py` (see "Launch blockers"), then change the build
   command to `npm run build`.
6. Add the custom domain under the Worker's Settings, Domains & Routes, then apply the zone settings and
   WAF rules in 04-Website-Guide.

Python and Node versions come from `.python-version` and the build image defaults. No secrets or build
variables are needed. The Analytics Engine dataset `site_events` is created on first write.

## Changing things

- Prices: change 08-Service-Catalog first, then 05's math, then `PRICES` in config, in one PR.
- Promises (reply time, call length, proposal time): change `PROMISES` once; every page follows.
- A real screen recording replaces a drawn demo when its file is set in `DEMO_VIDEOS`.
- Real Odoo recordings live in `ODOO_REEL`, real screenshots in `SCREENS`. Record only in a demo database with
  sample data, never in a client system. Real Shopify footage needs a Shopify development store, recorded by Vee.
  Capture screens at 900 CSS px wide (2x pixels) and record videos at 960 by 600, so Odoo's text stays readable
  on the page. The home hero's highlight boxes are measured on `hero-products.webp`; re-measure them in
  `site.css` (`.hero-stage` variables) if that screenshot changes, and keep the card numbers equal to the screen.
- Guided tours (`ODOO_TOURS` on /odoo): each step is a 960 by 600 screenshot at 2x plus the clickable box in
  percent of the image (left, top, width, height) and a caption. The captions double as the text version for
  readers without JavaScript. Re-measure a box whenever its screenshot changes.
- The sync model on /shopify is a teaching model with one product and sample numbers, not a live connector.
  Its wording lives in `site.js`; keep it in step with how real connectors behave.
- Odoo 20 facts on /odoo come from Odoo's release notes, checked Nov 11, 2026
  (`research/R-Odoo-20-checked.md` in project files). Re-check before changing that section.
- Guides start with `status: "draft"`. Staging builds show them with a draft note; the release build leaves them
  out, and links to them drop away, until Vee sets `status: "approved"`. Every guide needs a 40 to 60 word short
  answer, a "When the other option wins" section and a date on every price; the build stops if one is missing.
- Resource pages (/resources, /guides, /faq, /videos, /tools) must stay original. The build stops when one shares
  two or more 12-word runs with any other page. Wrap text that is meant to repeat, such as a shared widget, in
  `<!--reuse-->` and `<!--/reuse-->`. Every internal link must point to a built page or file.
- Shopify plan prices for the plan picker live in `SHOPIFY_PLANS` in build.py, from
  `research/R-Shopify-plans-checked.md`. Connector facts for guide 1 come from
  `research/R-Shopify-Odoo-connectors-checked.md`. Re-check both before changing them.
- Icons: tiles, doors, cards and service links call `ico(name)`, which uses the custom icon from `spot.py` when one
  exists and Lucide otherwise. Small inline icons (arrows, checks, chevrons, 16px labels) stay Lucide. A new concept
  icon gets drawn in `spot.py` in the same style (ink outline, 48-unit grid, offset color block) and added to
  `SPOT_FOR`, so no list mixes the two sets. Hero shapes come from `hero_shapes()` on pages without an illustration.
- A renamed URL gets a 301 line in `REDIRECTS` in build.py.
- Work on a branch, open a PR, and nothing merges to `main` until Vee says "merge" in the thread.

## Launch blockers (the release build checks 1 to 4)

1. `BUSINESS_NAME` and `LEGAL_LINE`: thread 03 (name and DBA filing). Rename the Worker in
   `wrangler.jsonc` and `package.json` at the same time.
2. `DOMAIN`: thread 03.
3. `EMAIL` (MX, SPF, DKIM, DMARC tested) or `BOOKING_URL` (books into the CRM): thread 10. Booking
   buttons stay hidden until one is real.
4. `ABOUT_BIO` in Vee's own words, plus any current certifications.
5. Privacy and terms text reviewed by the attorney (06).
