// [DBA name] site behavior (v5): the first-party visit counter and its opt-out, the phone menu, recordings that play
// while on screen, scroll reveals, the guide filter, the ERP readiness check, the Shopify plan picker and the sync model.
// Sends to /api/e on our own domain only. No third-party scripts, no IP logging, no contact details,
// and nothing typed or picked on the page except which tool result was shown.
(function () {
  "use strict";
  var ENDPOINT = "/api/e";
  var LIVE = location.protocol === "https:";
  var root = document.documentElement;

  function utm() {
    var out = {}, q = new URLSearchParams(location.search);
    ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"].forEach(function (k) {
      var v = q.get(k);
      if (v) out[k] = v.slice(0, 100);
    });
    return out;
  }

  function landing() {
    try {
      var l = sessionStorage.getItem("landing");
      if (!l) { l = location.pathname; sessionStorage.setItem("landing", l); }
      return l;
    } catch (e) { return location.pathname; }
  }

  function refHost() {
    try {
      if (!document.referrer) return "";
      var h = new URL(document.referrer).hostname;
      return h === location.hostname ? "" : h;
    } catch (e) { return ""; }
  }

  function send(type, extra) {
    if (!LIVE || navigator.globalPrivacyControl) return;
    var body = JSON.stringify(Object.assign({
      t: type, p: location.pathname, l: landing(), r: refHost(), u: utm(),
      w: window.innerWidth
    }, extra || {}));
    try {
      if (navigator.sendBeacon) {
        navigator.sendBeacon(ENDPOINT, new Blob([body], { type: "application/json" }));
      } else {
        fetch(ENDPOINT, { method: "POST", body: body, keepalive: true,
          headers: { "Content-Type": "application/json" } });
      }
    } catch (e) { /* counting must never break the page */ }
  }

  function track(type, where) { send(type, { where: String(where || "").slice(0, 40) }); }
  function all(sel, el) { return Array.prototype.slice.call((el || document).querySelectorAll(sel)); }

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasIO = "IntersectionObserver" in window;
  root.classList.add("js");


  // ---- Phone menu ---------------------------------------------------------------------------------
  var head = document.querySelector(".site-head"), menuBtn = document.querySelector(".menu-btn");
  if (head && menuBtn) {
    menuBtn.hidden = false;
    menuBtn.addEventListener("click", function () {
      var open = !head.classList.contains("open");
      head.classList.toggle("open", open);
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
      menuBtn.textContent = open ? "Close" : "Menu";
    });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && head.classList.contains("open")) { menuBtn.click(); menuBtn.focus(); }
    });
  }

  // ---- Recordings: silent, play while on screen, one pause button each -------------------------
  all("[data-clip]").forEach(function (fig) {
    var v = fig.querySelector("video"), frame = fig.querySelector(".clip-frame");
    if (!v || !frame) return;
    v.controls = false;
    var btn = document.createElement("button"), paused = reduce, seen = false;
    btn.type = "button"; btn.className = "clip-btn";
    function label() { btn.textContent = v.paused ? "Play" : "Pause"; btn.setAttribute("aria-label", (v.paused ? "Play " : "Pause ") + "recording"); }
    btn.addEventListener("click", function () {
      if (v.paused) { paused = false; var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); track("demo", "play"); }
      else { paused = true; v.pause(); }
    });
    v.addEventListener("play", label); v.addEventListener("pause", label);
    frame.appendChild(btn); label();
    if (!hasIO) return;
    new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting && !paused) {
          if (!seen) { seen = true; v.preload = "auto"; }
          var pr = v.play(); if (pr && pr.catch) pr.catch(function () {});
        } else if (!en.isIntersecting && !v.paused) { v.pause(); }
      });
    }, { threshold: 0.45 }).observe(v);
  });

  // ---- Scroll reveals ----------------------------------------------------------------------------
  var revealed = all(".reveal, .mini");
  if (hasIO && !reduce) {
    var rv = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); rv.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    revealed.forEach(function (el) { rv.observe(el); });
  } else {
    revealed.forEach(function (el) { el.classList.add("in"); });
  }


  // ---- Scroll depth -----------------------------------------------------------------------------
  var marks = [25, 50, 75, 100], ticking = false;
  function onScroll() {
    ticking = false;
    var max = root.scrollHeight - window.innerHeight;
    var k = max > 0 ? Math.min(1, window.scrollY / max) : 1;
    while (marks.length && k * 100 >= marks[0] - 0.5) track("depth", marks.shift());
    updateBar();
  }
  window.addEventListener("scroll", function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });

  // ---- Phone bar: shows once no other booking button is on screen --------------------------------
  var ctaBar = document.querySelector("[data-cta-bar]"), onScreen = 0;
  function updateBar() {
    if (ctaBar) ctaBar.classList.toggle("show", window.scrollY > 420 && onScreen === 0);
  }
  if (ctaBar && hasIO) {
    var bo = new IntersectionObserver(function (es) {
      es.forEach(function (en) { onScreen += en.isIntersecting ? 1 : (en.target._seen ? -1 : 0); en.target._seen = en.isIntersecting; });
      updateBar();
    });
    all(".btn").forEach(function (b) { if (!ctaBar.contains(b)) bo.observe(b); });
  }

  // ---- Counter events and the privacy opt-out ----------------------------------------------------
  send("view");

  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest("[data-track]");
    if (a) track(a.getAttribute("data-track"), a.getAttribute("data-where"));
  });


  // ---- Sync model: Odoo holds the count; Shopify sells and gets the count back ---------------------
  all("[data-sim]").forEach(function (sim) {
    var shopEl = sim.querySelector("[data-shop]"), odooEl = sim.querySelector("[data-odoo]");
    var stateEl = sim.querySelector("[data-state]"), log = sim.querySelector("[data-log]");
    var wire = sim.querySelector("[data-wire]"), offBtn = sim.querySelector('[data-act="off"]');
    var START = 33, shop, odoo, on, queue, held, t, used = false;
    function clock() {
      t += 7 + Math.floor(Math.random() * 30);
      var h = 9 + Math.floor(t / 3600), m = Math.floor(t / 60) % 60, s = t % 60;
      return [h, m, s].map(function (v) { return (v < 10 ? "0" : "") + v; }).join(":");
    }
    function line(text) {
      var li = document.createElement("li"), b = document.createElement("b");
      b.textContent = clock(); li.appendChild(b); li.appendChild(document.createTextNode(text));
      log.appendChild(li); log.scrollTop = log.scrollHeight;
    }
    function pulse() { wire.classList.remove("go"); void wire.offsetWidth; wire.classList.add("go"); }
    function paint() {
      shopEl.textContent = shop; odooEl.textContent = odoo;
      var gap = Math.abs(shop - odoo);
      stateEl.textContent = "";
      var tag = document.createElement("span");
      tag.className = "tag " + (gap ? "bad" : "ok");
      tag.textContent = gap ? "Out of step by " + gap : "In step";
      stateEl.appendChild(tag);
      var msg = " Both systems show the same count.";
      var waiting = queue.length + " order" + (queue.length === 1 ? "" : "s") + " waiting in Shopify";
      if (gap && queue.length && held) msg = " " + waiting + ", and " + held + " received units Shopify can't sell yet. Neither count is right.";
      else if (gap && queue.length) msg = " " + waiting + ". Until " + (queue.length === 1 ? "it reaches" : "they reach") + " Odoo, Odoo counts stock that's already sold.";
      else if (gap) msg = " Shopify shows less than you have, so it may stop selling too early.";
      stateEl.appendChild(document.createTextNode(msg));
      wire.classList.toggle("off", !on);
      offBtn.setAttribute("aria-pressed", on ? "false" : "true");
    }
    function reset() {
      shop = START; odoo = START; on = true; queue = []; held = 0; t = 0;
      log.textContent = ""; line("Connector running. Odoo holds the stock count."); paint();
    }
    function sell(where) {
      if (shop <= 0) { line("Shopify shows 0 available, so the item can't be sold."); return; }
      shop -= 1;
      line("Shopify: 1 sold " + (where === "pos" ? "at the register, Store 1" : "online") + ".");
      if (on) {
        odoo -= 1; pulse();
        line("Odoo: order received, delivery created, on hand " + odoo + ".");
      } else {
        queue.push(where);
        line("Connector off: the order waits in Shopify. Odoo still shows " + odoo + ".");
      }
      paint();
    }
    sim.addEventListener("click", function (ev) {
      var b = ev.target.closest("[data-act]");
      if (!b) return;
      var act = b.getAttribute("data-act");
      if (!used) { used = true; track("demo", "sim:start"); }
      if (act === "web" || act === "pos") sell(act);
      if (act === "buy") {
        odoo += 10;
        line("Odoo: 10 received from the vendor, on hand " + odoo + ".");
        if (on) { shop = odoo; pulse(); line("Shopify: available updated to " + shop + "."); }
        else { held += 10; line("Connector off: Shopify still shows " + shop + "."); }
        paint();
      }
      if (act === "off") {
        on = !on;
        if (!on) line("Connector switched off.");
        else {
          line("Connector back on. " + queue.length + " waiting order" + (queue.length === 1 ? "" : "s") + " sent to Odoo.");
          odoo -= queue.length; queue = []; held = 0; shop = odoo; pulse();
          line("Odoo on hand " + odoo + ", pushed to Shopify. Back in step.");
        }
        paint();
      }
      if (act === "reset") reset();
    });
    sim.hidden = false;
    reset();
  });

  // ---- Resource filters: Shopify, Odoo, both together, or everything -----------------------------
  // Shopify shows Shopify and both-together items, Odoo shows Odoo and both, Both shows only both.
  var SHOWS = { all: null, shopify: ["shopify", "both"], odoo: ["odoo", "both"], both: ["both"] };
  all("[data-chips]").forEach(function (box) {
    var list = document.querySelector('[data-filter-list="' + box.getAttribute("data-chips") + '"]');
    if (!list) return;
    var btns = all(".chip-btn", box), none = document.createElement("p");
    none.className = "small chips-none"; none.setAttribute("aria-live", "polite");
    list.parentNode.insertBefore(none, list.nextSibling);
    function pick(f) {
      var keep = SHOWS[f], shown = 0;
      btns.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-filter") === f ? "true" : "false"); });
      all(":scope > li[data-platform]", list).forEach(function (li) {
        var on = !keep || keep.indexOf(li.getAttribute("data-platform")) > -1;
        if (on) { li.removeAttribute("data-hide"); shown += 1; } else li.setAttribute("data-hide", "");
      });
      none.textContent = shown ? "" : "Nothing in this list for that filter yet.";
    }
    btns.forEach(function (b) {
      b.addEventListener("click", function () { pick(b.getAttribute("data-filter")); track("demo", "filter:" + b.getAttribute("data-filter")); });
    });
    box.hidden = false;
  });


  // ---- Shopify plan picker: five answers, one plan, the reason and the monthly cost ---------------
  all("[data-picker]").forEach(function (box) {
    var P;
    try { P = JSON.parse(box.getAttribute("data-plans")); } catch (err) { return; }
    var qs = all("[data-pq]", box), ans = {};
    var out = box.querySelector("[data-pk-out]"), empty = box.querySelector("[data-pk-empty]");
    var nameEl = box.querySelector("[data-pk-plan]"), why = box.querySelector("[data-pk-why]");
    var yEl = box.querySelector("[data-pk-y]"), mEl = box.querySelector("[data-pk-m]"), pro = box.querySelector("[data-pk-pro]");
    var used = false, lastPlan = "";
    function usd(n) { return "$" + n.toLocaleString("en-US"); }
    function decide(a) {
      var loc = +a.loc, reasons = [], k = "basic";
      if (a.loc === "11") reasons.push("You sell from more than 10 locations. Basic, Grow and Advanced allow up to 10.");
      if (a.staff === "16") reasons.push("More than 15 staff need a login. Advanced includes 15 staff accounts.");
      if (a.b2b === "yes") reasons.push("You need more than 3 wholesale catalogs. Plans below Plus allow 3.");
      if (reasons.length) k = "plus";
      else if (a.staff === "15") { k = "advanced"; reasons.push("6 to 15 staff need their own login. Advanced includes 15 staff accounts, Grow includes 5."); }
      else if (a.staff === "5" || a.sync === "yes") {
        k = "grow";
        if (a.staff === "5") reasons.push("Up to 5 staff need a login. Grow includes 5 staff accounts.");
        if (a.sync === "yes") reasons.push("Shopify lists full data access for custom apps from Grow up, which some back office connectors need.");
      } else reasons.push("An owner-run store fits Basic. Every plan takes in-person payments and allows up to 10 locations.");
      var p = { k: k, reasons: reasons, pro: "" };
      if (loc > 0 && a.perm === "yes") {
        if (k === "plus") p.pro = "POS Pro is included on Plus for 20 locations.";
        else if (loc <= 2) p.pro = "POS Pro for staff roles and in-store stock tools adds " + usd(P.pro * loc) + " a month (" +
          usd(P.pro) + " a location, " + loc + " shop" + (loc === 1 ? "" : "s") + ").";
        else p.pro = "POS Pro for staff roles and in-store stock tools adds " + usd(P.pro) + " a month for each location.";
      } else if (loc > 0) p.pro = "Your shops can use the POS app that comes with every plan. POS Pro is not needed for what you described.";
      return p;
    }
    function paint() {
      var done = qs.every(function (q) { return ans[q.getAttribute("data-pq")] !== undefined; });
      empty.hidden = done; out.hidden = !done;
      if (!done) return;
      var r = decide(ans), plan = P[r.k];
      if (!lastPlan && out.getBoundingClientRect().top > window.innerHeight - 80) {
        out.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center" });
      }
      nameEl.textContent = plan.n;
      why.textContent = "";
      r.reasons.forEach(function (t) { var li = document.createElement("li"); li.textContent = t; why.appendChild(li); });
      var from = r.k === "plus" ? "From " : "";
      yEl.textContent = from + usd(plan.y) + " a month";
      mEl.textContent = from + usd(plan.m) + " a month";
      pro.textContent = r.pro; pro.hidden = !r.pro;
      if (r.k !== lastPlan) { lastPlan = r.k; track("demo", "plan:" + r.k); }
    }
    qs.forEach(function (q) {
      var key = q.getAttribute("data-pq"), opts = all(".opt", q);
      opts.forEach(function (o) {
        o.addEventListener("click", function () {
          opts.forEach(function (x) { x.setAttribute("aria-pressed", x === o ? "true" : "false"); });
          ans[key] = o.getAttribute("data-v");
          if (!used) { used = true; track("demo", "plan:start"); }
          paint();
        });
      });
    });
    box.hidden = false;
  });

  // ---- ERP readiness check: eight yes or no answers, three results -------------------------------
  all("[data-erp]").forEach(function (box) {
    var qs = all("[data-eq]", box), ans = {}, used = false, last = "";
    var empty = box.querySelector("[data-er-empty]"), count = box.querySelector("[data-er-count]");
    var nEl = box.querySelector("[data-er-n]"), res = all("[data-er]", box);
    function paint() {
      var keys = Object.keys(ans), yes = 0;
      keys.forEach(function (k) { yes += ans[k]; });
      var done = keys.length === qs.length;
      count.textContent = done || !keys.length ? "" : keys.length + " of " + qs.length + " answered.";
      empty.hidden = done; nEl.hidden = !done;
      var k = yes <= 2 ? "0" : yes <= 5 ? "1" : "2";
      res.forEach(function (r) { r.hidden = !done || r.getAttribute("data-er") !== k; });
      if (!done) return;
      nEl.textContent = yes + " of " + qs.length + " answers were yes.";
      if (!last && box.querySelector(".pk-r").getBoundingClientRect().top > window.innerHeight - 80) {
        box.querySelector(".pk-r").scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center" });
      }
      if (k !== last) { last = k; track("demo", "erp:" + k); }
    }
    qs.forEach(function (q) {
      var key = q.getAttribute("data-eq"), opts = all(".opt", q);
      opts.forEach(function (o) {
        o.addEventListener("click", function () {
          opts.forEach(function (x) { x.setAttribute("aria-pressed", x === o ? "true" : "false"); });
          ans[key] = +o.getAttribute("data-v");
          if (!used) { used = true; track("demo", "erp:start"); }
          paint();
        });
      });
    });
    box.hidden = false;
  });

  // ---- Screens open full size: people try to zoom admin screenshots, so let them ----------------------
  var shots = all("[data-zoom]");
  if (shots.length && typeof HTMLDialogElement === "function") {
    var dlg = document.createElement("dialog");
    dlg.className = "zoom";
    dlg.innerHTML = '<form method="dialog" class="zoom-bar"><span class="zoom-cap"></span>' +
      '<button class="btn-sm" value="close">Close</button></form><div class="zoom-body"><img alt=""></div>';
    document.body.appendChild(dlg);
    var zimg = dlg.querySelector("img"), zcap = dlg.querySelector(".zoom-cap");
    dlg.addEventListener("click", function (ev) { if (ev.target === dlg) dlg.close(); });
    shots.forEach(function (fig) {
      var frame = fig.querySelector(".clip-frame"), img = fig.querySelector("img");
      if (!frame || !img) return;
      frame.setAttribute("role", "button");
      frame.setAttribute("tabindex", "0");
      frame.setAttribute("aria-label", "Open full size: " + img.alt);
      frame.classList.add("zoomable");
      function open() {
        zimg.src = img.currentSrc || img.src;
        zimg.alt = img.alt;
        zcap.textContent = img.alt;
        dlg.showModal();
        track("demo", "zoom");
      }
      frame.addEventListener("click", open);
      frame.addEventListener("keydown", function (ev) {
        if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); open(); }
      });
    });
  }

  // ---- Cost of manual work: the visitor's own figures, worked out in the browser ---------------------
  all("[data-calc]").forEach(function (box) {
    var form = box.querySelector("form"), used = false;
    function n(k) { var v = parseFloat(form.elements[k].value); return isFinite(v) && v > 0 ? v : 0; }
    function paint() {
      var hours = (n("orders") * n("mins") / 60 + n("other")) * 50 + n("counts") * n("count_h") * 12;
      box.querySelector('[data-out="hours"]').textContent = Math.round(hours).toLocaleString("en-US");
      box.querySelector('[data-out="cost"]').textContent = "$" + Math.round(hours * n("rate")).toLocaleString("en-US");
    }
    form.addEventListener("input", function () { if (!used) { used = true; track("demo", "calc:start"); } paint(); });
    form.addEventListener("submit", function (ev) { ev.preventDefault(); });
    paint();
  });

  // ---- Question form: inline checks that keep what was typed, then a JSON post to /api/ask ----------
  all("[data-ask]").forEach(function (form) {
    var status = form.querySelector(".ask-status"), q = new URLSearchParams(location.search), started = false;
    form.elements.t.value = String(Date.now());
    form.elements.src.value = (location.pathname + " " + new URLSearchParams(utm()).toString()).trim().slice(0, 300);
    var pick = q.get("for");
    if (pick && form.elements["for"].querySelector('option[value="' + pick.replace(/[^a-z-]/g, "") + '"]')) {
      form.elements["for"].value = pick;
    }
    if (q.get("sent")) status.textContent = "Thanks. Your question is in, and the reply comes by email.";
    var MSG = {
      name: "Please add your name.",
      email: "Please check the email address. It needs an @ and a domain, like name@yourstore.com.",
      msg: "Please write a line or two about what's going on.",
      offline: "This form couldn't send just now. Please book a call instead, or try again later.",
      unreadable: "This form couldn't send just now. Please try again."
    };
    function mark(field, on) {
      var el = form.elements[field];
      if (!el) return;
      el.setAttribute("aria-invalid", on ? "true" : "false");
      var lab = el.closest(".fld");
      if (lab) lab.classList.toggle("bad", !!on);
    }
    form.addEventListener("input", function () {
      if (!started) { started = true; track("form", "ask:start"); }
    });
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var bad = "";
      ["name", "email", "msg"].forEach(function (f) {
        var el = form.elements[f], v = el.value.trim();
        var off = f === "email" ? !/^[^\s@]+@[^\s@]+\.[A-Za-z]{2,}$/.test(v) : (f === "msg" ? v.length < 10 : !v);
        mark(f, off);
        if (off && !bad) bad = f;
      });
      if (bad) {
        status.textContent = MSG[bad];
        form.elements[bad].focus();
        track("form", "ask:error:" + bad);
        return;
      }
      if (form.hasAttribute("data-preview")) {
        status.textContent = "Preview build: this form isn't connected yet, so nothing was sent.";
        return;
      }
      var data = { runs: [] };
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name || el.type === "submit") return;
        if (el.type === "checkbox") { if (el.checked) data.runs.push(el.value); return; }
        data[el.name] = el.value;
      });
      var send = form.querySelector('[type="submit"]');
      send.disabled = true;
      status.textContent = "Sending...";
      fetch(form.action, { method: "POST", body: JSON.stringify(data),
        headers: { "Content-Type": "application/json", "Accept": "application/json" } })
        .then(function (r) { return r.json(); })
        .then(function (res) {
          if (res.ok) {
            track("form", "ask:submit");
            form.innerHTML = '<p class="ask-done"><b>Thanks, your question is in.</b> The reply comes by email. If you ' +
              'would rather talk it through, you can still <a href="/book">book a call</a>.</p>';
          } else {
            send.disabled = false;
            if (MSG[res.error] && form.elements[res.error]) { mark(res.error, true); form.elements[res.error].focus(); }
            status.textContent = MSG[res.error] || MSG.unreadable;
            track("form", "ask:error:" + res.error);
          }
        })
        .catch(function () { send.disabled = false; status.textContent = MSG.offline; });
    });
  });

  var btn = document.getElementById("optout");
  if (btn) {
    var status = document.getElementById("optout-status");
    if (navigator.globalPrivacyControl) status.textContent = "Your browser's Global Privacy Control signal is on, so this browser is not counted.";
    btn.addEventListener("click", function () {
      fetch(ENDPOINT + "/optout", { method: "POST" }).then(function (r) {
        status.textContent = r.ok ? " Done. This browser will not be counted." : " That didn't work. Please try again.";
      }).catch(function () { status.textContent = " That didn't work. Please try again."; });
    });
  }
})();

