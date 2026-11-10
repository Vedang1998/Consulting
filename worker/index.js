// First-party visit counter for the [DBA name] site.
// Runs only for /api/* (wrangler.jsonc run_worker_first). Everything else is a static asset.
// Writes one row per event to Workers Analytics Engine (binding EVENTS).
// Stores no IP address, no name, no email, nothing typed into the page.

const COOKIE = "v";
const OPTOUT = "vo";
const YEAR = 60 * 60 * 24 * 365;
// view: page view. booking/email/phone: taps on contact links. depth: 25/50/75/100 percent scrolled.
// section: a page section came into view. demo: a workflow tab was picked. finder: service finder start/result.
const TYPES = new Set(["view", "booking", "email", "phone", "depth", "section", "demo", "finder"]);

function cookies(req) {
  const out = {};
  (req.headers.get("Cookie") || "").split(";").forEach((c) => {
    const i = c.indexOf("=");
    if (i > 0) out[c.slice(0, i).trim()] = c.slice(i + 1).trim();
  });
  return out;
}

function device(ua, w) {
  if (/bot|crawl|spider|slurp|preview|headless/i.test(ua)) return "bot";
  if (/iPad|Tablet/i.test(ua)) return "tablet";
  if (/Mobi|Android|iPhone/i.test(ua)) return "mobile";
  if (w && w < 768) return "mobile";
  return "desktop";
}

function browser(ua) {
  if (/Edg\//.test(ua)) return "Edge";
  if (/Firefox\//.test(ua)) return "Firefox";
  if (/Chrome\//.test(ua)) return "Chrome";
  if (/Safari\//.test(ua)) return "Safari";
  return "Other";
}

const clip = (s, n = 100) => String(s || "").slice(0, n);

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (!url.pathname.startsWith("/api/")) return env.ASSETS.fetch(req);

    const secure = "; Path=/; Secure; HttpOnly; SameSite=Lax";

    if (url.pathname === "/api/e/optout" && req.method === "POST") {
      const h = new Headers({ "Cache-Control": "no-store" });
      h.append("Set-Cookie", `${OPTOUT}=1; Max-Age=${YEAR}${secure}`);
      h.append("Set-Cookie", `${COOKIE}=; Max-Age=0${secure}`);
      return new Response(null, { status: 204, headers: h });
    }

    if (url.pathname !== "/api/e" || req.method !== "POST") {
      return new Response("Not found", { status: 404 });
    }

    const c = cookies(req);
    if (c[OPTOUT] === "1" || req.headers.get("Sec-GPC") === "1") {
      return new Response(null, { status: 204 });
    }

    let d = {};
    try { d = JSON.parse(await req.text()); } catch { return new Response(null, { status: 400 }); }
    if (!TYPES.has(d.t)) return new Response(null, { status: 400 });

    const returning = Boolean(c[COOKIE]);
    const id = c[COOKIE] || crypto.randomUUID();
    const ua = req.headers.get("User-Agent") || "";
    const cf = req.cf || {};
    const u = d.u || {};

    if (env.EVENTS) {
      env.EVENTS.writeDataPoint({
        indexes: [clip(d.t, 16)],
        blobs: [
          clip(d.p), clip(d.l), clip(d.r), clip(u.utm_source), clip(u.utm_medium), clip(u.utm_campaign),
          returning ? "returning" : "new", clip(cf.country, 8), clip(cf.region, 64),
          device(ua, d.w), browser(ua), clip(id, 40), clip(cf.asOrganization, 100), clip(d.where, 40),
        ],
        doubles: [1],
      });
    }

    const h = new Headers({ "Cache-Control": "no-store" });
    h.append("Set-Cookie", `${COOKIE}=${id}; Max-Age=${YEAR}${secure}`);
    return new Response(null, { status: 204, headers: h });
  },
};
