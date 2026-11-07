# [DBA name] website

Static site for [DBA name] (IVYY LLC), a remote Shopify and Odoo consultancy. Python standard library
only, no frameworks. Hosted on Cloudflare Workers with Static Assets once Vee connects it.

**Nothing here is live.** The release build refuses to run until the business name, domain, a tested
contact path and Vee's About text are real (see "Launch blockers" below).

## Layout

| Path | What it holds |
| --- | --- |
| `src/config.py` | Every business fact: name, domain, contact, booking link, prices, promises, offer, profiles. Most changes happen here. `# CONFIRM` marks values Vee must supply. |
| `src/build.py` | Page templates and copy, helpers (`meta_desc`, `clean_url`, `faq_schema`), site files and output checks. |
| `src/site.css` | Design system from `brand/tokens.json` (03-Brand-Guide), light and dark. |
| `src/site.js` | First-party visit counter beacon and the privacy opt-out button. |
| `src/fonts/` | Self-hosted woff2 files (Archivo 600, IBM Plex Sans 400/600, IBM Plex Mono 400, all OFL). Empty for now; the site falls back to system fonts. |
| `worker/index.js` | The Worker on `/api/*`: writes visit events to Workers Analytics Engine, sets one HttpOnly cookie, stores no IP or contact details, honors the opt-out cookie and Global Privacy Control. |
| `wrangler.jsonc` | Workers config: assets from `dist/`, Worker only for `/api/*`, 404 page, Analytics Engine binding. |
| `dist/` | Build output, git-ignored. |

## Build

```sh
python3 src/build.py            # preview: prints a NOTE for each blank field, shows a "Preview build" strip
python3 src/build.py --release  # production: fails while launch blockers remain
```

A good build ends with `Built N indexable pages`. The build also fails on: an em dash, an en dash outside
a number range, any banned buzzword from the project instructions, an exclamation mark in a heading,
emoji, a 555 number, over-sharing phrases, a title over 66 characters, or an offer without an end date,
regular price, capacity and terms.

Output: the pages, `_headers`, `_redirects`, `robots.txt`, `sitemap.xml` (no fake lastmod), `llms.txt`
(generated from config), the IndexNow key file, `favicon.svg` and `site.webmanifest`.

## Changing things

- Prices: change 08-Service-Catalog first, then 05's math, then `PRICES` in config, in one PR.
- Promises (reply time, call length, proposal time): change `PROMISES` once; every page follows.
- A renamed URL gets a 301 line in `REDIRECTS` in build.py.
- Work on a branch, open a PR, and nothing merges to `main` until Vee says "merge" in the thread.

## Launch blockers

1. `BUSINESS_NAME`, `LEGAL_LINE` and the Worker name: thread 03 (name and DBA filing).
2. `DOMAIN`: thread 03.
3. `EMAIL` (MX, SPF, DKIM, DMARC tested) and `BOOKING_URL` (books into the CRM): thread 10.
4. `ABOUT_BIO` in Vee's own words, plus any current certifications.
5. Privacy and terms text reviewed by the attorney (06).
6. Font files added to `src/fonts/`.
7. Cloudflare: Workers Builds connected with build command `npm run build` (runs `--release`), the
   Analytics Engine dataset, custom domains, zone settings and WAF rules from 04-Website-Guide. Each
   applied only with Vee's yes.
