// First-party visit counter for the [DBA name] site, the question form, and byte-range video delivery.
// Runs only for /api/* and /media/* (wrangler.jsonc run_worker_first). Everything else is a static asset.
// Writes one row per event to Workers Analytics Engine (binding EVENTS).
// The counter stores no IP address, no name, no email, nothing typed into the page.
// /api/ask emails a question to one verified inbox (send_email binding ASK_MAIL) and stores nothing itself.

import { EmailMessage } from "cloudflare:email";

const COOKIE = "v";
const OPTOUT = "vo";
const YEAR = 60 * 60 * 24 * 365;
// view: page view. booking/email/phone: taps on contact links. depth: 25/50/75/100 percent scrolled.
// section: a page section came into view. demo: a workflow tab was picked. finder: service finder start/result.
// form: question form start, submit or error (field name only, never what was typed).
const TYPES = new Set(["view", "booking", "email", "phone", "depth", "section", "demo", "finder", "form"]);

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

// Static assets answer a Range request with the whole file (200), and Safari needs 206 Partial
// Content to play video. Media files are small (under 25 MiB by the platform limit), so read the
// asset once and return the requested bytes.
async function media(req, env) {
  const range = req.headers.get("Range");
  const plain = new Request(req.url, { method: req.method === "HEAD" ? "HEAD" : "GET" });
  const res = await env.ASSETS.fetch(plain);
  const headers = new Headers(res.headers);
  headers.set("Accept-Ranges", "bytes");
  if (!range || res.status !== 200 || req.method === "HEAD") {
    return new Response(res.body, { status: res.status, headers });
  }
  const m = /^bytes=(\d*)-(\d*)$/.exec(range.trim());
  const body = await res.arrayBuffer();
  const size = body.byteLength;
  let start, end;
  if (m && m[1] !== "") {
    start = Number(m[1]);
    end = m[2] !== "" ? Math.min(Number(m[2]), size - 1) : size - 1;
  } else if (m && m[2] !== "") {
    start = Math.max(0, size - Number(m[2]));
    end = size - 1;
  }
  if (start === undefined || start > end || start >= size) {
    headers.set("Content-Range", `bytes */${size}`);
    headers.delete("Content-Length");
    return new Response(null, { status: 416, headers });
  }
  headers.set("Content-Range", `bytes ${start}-${end}/${size}`);
  headers.set("Content-Length", String(end - start + 1));
  return new Response(body.slice(start, end + 1), { status: 206, headers });
}

// ---- Question form -------------------------------------------------------------------------------
const PACKAGES = new Set(["", "systems-roadmap", "store-move", "odoo-launch", "connection", "support"]);
const SYSTEMS = new Set(["Shopify", "Shopify POS", "Odoo", "QuickBooks", "Spreadsheets", "Something else"]);
const EMAIL_RE = /^[^\s@<>(),;:"\[\]]{1,64}@[A-Za-z0-9.-]{1,190}\.[A-Za-z]{2,24}$/;
const oneLine = (s, n) => String(s || "").replace(/[\r\n\t]+/g, " ").replace(/[^\x20-\x7E\u00A0-\uFFFF]/g, "").trim().slice(0, n);

// Header text outside plain ASCII goes in as an RFC 2047 encoded word.
function hdr(s) {
  if (/^[\x20-\x7E]*$/.test(s)) return s;
  const bytes = new TextEncoder().encode(s);
  let bin = "";
  bytes.forEach((b) => { bin += String.fromCharCode(b); });
  return `=?UTF-8?B?${btoa(bin)}?=`;
}

async function readForm(req) {
  const type = req.headers.get("Content-Type") || "";
  if (type.includes("application/json")) return await req.json();
  const f = await req.formData();
  const out = {};
  for (const [k, v] of f.entries()) {
    if (k === "runs") (out.runs = out.runs || []).push(v);
    else out[k] = v;
  }
  return out;
}

function answer(req, ok, error) {
  const wantsJson = (req.headers.get("Accept") || "").includes("application/json");
  if (wantsJson) {
    return new Response(JSON.stringify({ ok, error: error || "" }), {
      status: ok ? 200 : 400, headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
    });
  }
  // No-JS fallback: back to the form with a plain status.
  const to = new URL("/book", req.url);
  to.searchParams.set(ok ? "sent" : "error", error || "1");
  to.hash = "ask";
  return Response.redirect(to.toString(), 303);
}

async function ask(req, env) {
  let d;
  try { d = await readForm(req); } catch { return answer(req, false, "unreadable"); }
  // Bots fill the hidden field or submit in under three seconds. Say "sent" so they learn nothing.
  const elapsed = Date.now() - Number(d.t || 0);
  if (String(d.website || "") !== "" || (d.t && elapsed < 3000)) return answer(req, true);

  const name = oneLine(d.name, 100);
  const email = oneLine(d.email, 200);
  const pkg = PACKAGES.has(String(d.for || "")) ? String(d.for || "") : "";
  const runs = [].concat(d.runs || []).map(String).filter((s) => SYSTEMS.has(s));
  const msg = String(d.msg || "").replace(/\r\n?/g, "\n").slice(0, 4000).trim();
  const src = oneLine(d.src, 300);
  if (!name) return answer(req, false, "name");
  if (!EMAIL_RE.test(email)) return answer(req, false, "email");
  if (msg.length < 10) return answer(req, false, "msg");
  if (!env.ASK_MAIL || !env.ASK_FROM || !env.ASK_TO) return answer(req, false, "offline");

  const host = new URL(req.url).hostname;
  const subject = `Website question${pkg ? ` (${pkg})` : ""} from ${name}`.slice(0, 150);
  const body = [
    `Name: ${name}`, `Email: ${email}`, `About: ${pkg || "not sure yet"}`, `Runs today: ${runs.join(", ") || "not given"}`,
    `Sent from: ${src || "unknown"}`, "", msg, "",
  ].join("\n");
  const raw = [
    `From: Website form <${env.ASK_FROM}>`, `To: <${env.ASK_TO}>`, `Reply-To: ${hdr(name.replace(/[<>"]/g, ""))} <${email}>`,
    `Subject: ${hdr(subject)}`, `Date: ${new Date().toUTCString()}`, `Message-ID: <${crypto.randomUUID()}@${host}>`,
    "MIME-Version: 1.0", "Content-Type: text/plain; charset=utf-8", "Content-Transfer-Encoding: 8bit", "", body,
  ].join("\r\n");
  try {
    await env.ASK_MAIL.send(new EmailMessage(env.ASK_FROM, env.ASK_TO, raw));
  } catch {
    return answer(req, false, "offline");
  }
  return answer(req, true);
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (url.pathname.startsWith("/media/")) return media(req, env);
    if (!url.pathname.startsWith("/api/")) return env.ASSETS.fetch(req);

    if (url.pathname === "/api/ask") {
      if (req.method !== "POST") return new Response("Not found", { status: 404 });
      return ask(req, env);
    }

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
