// [DBA name] site behavior: the first-party visit counter, the privacy opt-out, the workflow demo,
// the service finder, scroll reveals, resource filters, video chapters, the Shopify plan picker and the ERP readiness check.
// Sends to /api/e on our own domain only. No third-party scripts, no IP logging, no contact details,
// and nothing typed or picked on the page except which demo tab and which finder result were shown.
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

  // ---- Workflow stages: a list of times, and elements that switch on at each step ----------------
  function countTo(el, to) {
    var from = parseInt(el.textContent, 10) || 0;
    if (reduce || from === to) { el.textContent = to; return; }
    var t0 = null, dur = 650;
    function f(t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / dur);
      el.textContent = Math.round(from + (to - from) * (1 - Math.pow(1 - k, 3)));
      if (k < 1) requestAnimationFrame(f);
    }
    requestAnimationFrame(f);
  }

  function stepOf(el) {
    if (el.hasAttribute("data-at")) return +el.getAttribute("data-at");
    var p = el.closest("[data-step]");
    return p ? +p.getAttribute("data-step") : 0;
  }

  function setStep(stage, n) {
    all("[data-step]", stage).forEach(function (el) {
      el.classList.toggle("on", +el.getAttribute("data-step") <= n);
    });
    all(".flip", stage).forEach(function (el) {
      var target = stepOf(el) <= n ? +el.getAttribute("data-to") : +el.getAttribute("data-from");
      if (n === 0) el.textContent = target; else if (+el.textContent !== target) countTo(el, target);
    });
  }

  function settle(stage, on) {
    all("tr.hit, .hitrow", stage).forEach(function (r) { r.classList.toggle("settled", on); });
  }

  function makeStage(stage) {
    var times = (stage.getAttribute("data-times") || "").split(",").map(Number);
    var end = times[times.length - 1], timers = [];
    function clear() { timers.forEach(clearTimeout); timers = []; }
    return {
      total: end + 4200,
      play: function (done) {
        clear();
        stage.classList.remove("run");
        settle(stage, false);
        setStep(stage, 0);
        void stage.offsetWidth;
        stage.classList.add("run");
        times.forEach(function (t, i) { timers.push(setTimeout(function () { setStep(stage, i + 1); }, t)); });
        timers.push(setTimeout(function () { settle(stage, true); stage.classList.remove("run"); }, end + 1200));
        timers.push(setTimeout(done, end + 4200));
      },
      stop: function () { clear(); stage.classList.remove("run"); },
      finish: function () { clear(); setStep(stage, times.length); settle(stage, true); }
    };
  }

  // ---- Tabbed demo: plays each workflow in turn until the visitor picks one ----------------------
  function demo(el) {
    var tabs = all('[role="tab"]', el);
    var panels = tabs.map(function (t) { return document.getElementById(t.getAttribute("aria-controls")); });
    var stages = panels.map(function (p) { var s = p.querySelector("[data-stage]"); return s ? makeStage(s) : null; });
    var cur = 0, visible = false, auto = true, playing = false;
    // The tabs drive playback, so native controls are only kept for reduced-motion visitors.
    if (!reduce) panels.forEach(function (p) { var v = p.querySelector("video"); if (v) v.controls = false; });

    function prog(i, ms) {
      var bar = tabs[i].querySelector(".tab-prog");
      if (!bar) return;
      bar.style.animation = "none";
      if (ms) { void bar.offsetWidth; bar.style.animation = "tabprog " + ms + "ms linear forwards"; }
    }

    function stop() {
      if (stages[cur]) stages[cur].stop();
      var v = panels[cur].querySelector("video");
      if (v) v.pause();
      prog(cur, 0);
      playing = false;
    }

    function play() {
      var st = stages[cur], v = panels[cur].querySelector("video");
      if (v) {
        if (reduce) return;
        playing = true;
        v.currentTime = 0;
        var pr = v.play(); if (pr && pr.catch) pr.catch(function () {});
        var go = function () { if (v.duration) prog(cur, (v.duration - v.currentTime) * 1000); };
        if (v.readyState >= 1) go(); else v.addEventListener("loadedmetadata", go, { once: true });
        v.onended = function () {
          playing = false;
          if (!visible) return;
          if (auto) select((cur + 1) % tabs.length, false); else play();
        };
        return;
      }
      if (!st) return;
      if (reduce) { st.finish(); return; }
      playing = true;
      prog(cur, st.total);
      st.play(function () {
        playing = false;
        if (!visible) return;
        if (auto) select((cur + 1) % tabs.length, false); else play();
      });
    }

    function select(i, byUser) {
      stop();
      cur = i;
      tabs.forEach(function (t, k) {
        t.setAttribute("aria-selected", k === i ? "true" : "false");
        if (k === i) t.removeAttribute("tabindex"); else t.setAttribute("tabindex", "-1");
        panels[k].hidden = k !== i;
      });
      if (byUser) { auto = false; track("demo", tabs[i].getAttribute("data-demo")); }
      if (visible || reduce) play();
    }

    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(i, true); });
      t.addEventListener("keydown", function (ev) {
        var n = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[ev.key];
        if (n === undefined) return;
        ev.preventDefault();
        n = (n + tabs.length) % tabs.length;
        select(n, true);
        tabs[n].focus();
      });
    });

    if (reduce || !hasIO) { stages.forEach(function (s) { if (s) s.finish(); }); return; }
    new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        visible = en.isIntersecting;
        if (visible && !playing) play();
        if (!visible && playing) stop();
      });
    }, { threshold: 0.2 }).observe(el);
  }

  all("[data-demo-root]").forEach(demo);

  // Stages outside a tabbed demo loop on their own while in view.
  all("[data-stage]").forEach(function (el) {
    if (el.closest("[data-demo-root]")) return;
    var st = makeStage(el);
    if (reduce || !hasIO) { st.finish(); return; }
    var vis = false, run = false;
    function loop() { run = true; st.play(function () { if (vis) loop(); else run = false; }); }
    new IntersectionObserver(function (es) {
      es.forEach(function (en) { vis = en.isIntersecting; if (vis && !run) loop(); });
    }, { threshold: 0.35 }).observe(el);
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

  // ---- Service finder ----------------------------------------------------------------------------
  all("[data-finder]").forEach(function (f) {
    var ans = {}, started = false, shown = "";
    var empty = f.querySelector("[data-empty]"), reset = f.querySelector("[data-reset]");
    var fbar = f.querySelector(".fq-bar i");
    f.hidden = false;

    function pick() {
      if (ans[2] === "l") return "nofit";
      if (ans[1] === "explore") return ans[2] === "s" ? "notyet" : "systems-roadmap";
      if (ans[1] === "move") return "store-move";
      if (ans[1] === "odoo") return ans[2] === "m" ? "systems-roadmap" : "odoo-launch";
      if (ans[1] === "connect") return "connection";
      if (ans[1] === "support") return "support";
      return "systems-roadmap";
    }

    function show() {
      var key = pick();
      all("[data-result]", f).forEach(function (r) { r.hidden = r.getAttribute("data-result") !== key; });
      all("[data-when]", f).forEach(function (n) { n.hidden = n.getAttribute("data-when") !== ans[3]; });
      empty.hidden = true;
      reset.hidden = false;
      if (key !== shown) { shown = key; track("finder", "done:" + key); }
    }

    f.addEventListener("click", function (ev) {
      var b = ev.target.closest(".opt");
      if (b) {
        var fs = b.closest("[data-q]"), n = +fs.getAttribute("data-q");
        all(".opt", fs).forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
        ans[n] = b.getAttribute("data-v");
        if (!started) { started = true; track("finder", "start"); }
        if (fbar) fbar.style.transform = "scaleX(" + Object.keys(ans).length / 3 + ")";
        var next = f.querySelector('[data-q="' + (n + 1) + '"]');
        if (next) next.hidden = false;
        if (ans[1] && ans[2] && ans[3]) show();
        return;
      }
      if (ev.target.closest("[data-reset]")) {
        ans = {}; shown = "";
        if (fbar) fbar.style.transform = "scaleX(0)";
        all(".opt", f).forEach(function (o) { o.setAttribute("aria-pressed", "false"); });
        all("[data-q]", f).forEach(function (q) { q.hidden = q.getAttribute("data-q") !== "1"; });
        all("[data-result]", f).forEach(function (r) { r.hidden = true; });
        empty.hidden = false;
        reset.hidden = true;
      }
    });
  });

  // ---- Scroll progress, depth and sections seen --------------------------------------------------
  var bar = document.querySelector(".progress i"), marks = [25, 50, 75, 100], ticking = false;
  function onScroll() {
    ticking = false;
    var max = root.scrollHeight - window.innerHeight;
    var k = max > 0 ? Math.min(1, window.scrollY / max) : 1;
    if (bar) bar.style.transform = "scaleX(" + k + ")";
    while (marks.length && k * 100 >= marks[0] - 0.5) track("depth", marks.shift());
    updateBar();
  }
  window.addEventListener("scroll", function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });

  if (hasIO) {
    var seen = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (!en.isIntersecting) return;
        track("section", en.target.getAttribute("data-sec"));
        seen.unobserve(en.target);
      });
    }, { threshold: 0.3 });
    all("[data-sec]").forEach(function (el) { seen.observe(el); });
  }

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

  // ---- Guided Odoo tours: real screens, one outlined click target per step -----------------------
  all("[data-tour]").forEach(function (tour) {
    tour.classList.add("live");
    all("[data-tour-panel]", tour).forEach(function (panel) {
      var imgs = all("img[data-step]", panel), items = all(".tour-steps li", panel);
      var hot = panel.querySelector("[data-hot]"), nav = panel.querySelector("[data-tour-nav]");
      var count = panel.querySelector("[data-count]"), next = panel.querySelector("[data-next]");
      var prev = panel.querySelector("[data-prev]"), cur = 1, total = imgs.length, key = panel.getAttribute("data-tour-panel");
      function go(n) {
        cur = Math.max(1, Math.min(total, n));
        imgs.forEach(function (im, i) { im.hidden = i !== cur - 1; });
        items.forEach(function (li, i) { li.classList.toggle("on", i === cur - 1); });
        var im = imgs[cur - 1], box = (im.getAttribute("data-box") || "").split(",").map(Number);
        var last = cur === total;
        hot.hidden = last || box.length !== 4;
        if (!hot.hidden) {
          hot.style.left = box[0] + "%"; hot.style.top = box[1] + "%";
          hot.style.width = box[2] + "%"; hot.style.height = box[3] + "%";
          hot.querySelector(".vh").textContent = "Next step: " + im.getAttribute("data-target");
        }
        count.textContent = "Step " + cur + " of " + total;
        next.textContent = last ? "Start again" : "Next step";
        prev.disabled = cur === 1;
        if (last) track("demo", "tour:" + key + ":done");
      }
      nav.hidden = false;
      hot.addEventListener("click", function () { go(cur + 1); });
      next.addEventListener("click", function () { go(cur === total ? 1 : cur + 1); });
      prev.addEventListener("click", function () { go(cur - 1); });
      items.forEach(function (li) {
        li.querySelector("[data-go]").addEventListener("click", function () { go(+li.getAttribute("data-step")); });
      });
      go(1);
    });
    var tabs = all("[data-tour-tab]", tour);
    tabs.forEach(function (t) {
      t.addEventListener("click", function () {
        tabs.forEach(function (o) { o.setAttribute("aria-selected", o === t ? "true" : "false"); });
        all("[data-tour-panel]", tour).forEach(function (p) {
          p.hidden = p.getAttribute("data-tour-panel") !== t.getAttribute("data-tour-tab");
        });
        track("demo", "tour:" + t.getAttribute("data-tour-tab"));
      });
    });
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

  // ---- Video chapters: jump to a chapter, and mark the one playing -------------------------------
  all("video[data-chapter-video]").forEach(function (vid) {
    var btns = all(".ch-btn[data-t]");
    var starts = btns.map(function (b) { return +b.getAttribute("data-t"); });
    function mark() {
      var at = vid.currentTime, on = 0;
      starts.forEach(function (s, i) { if (at + 0.25 >= s) on = i; });
      btns.forEach(function (b, i) {
        b.classList.toggle("on", i === on);
        if (i === on) b.setAttribute("aria-current", "true"); else b.removeAttribute("aria-current");
      });
    }
    function seek(t, play) {
      function go() { vid.currentTime = t; mark(); if (play) { var p = vid.play(); if (p && p.catch) p.catch(function () {}); } }
      if (vid.readyState >= 1) go(); else vid.addEventListener("loadedmetadata", go, { once: true });
    }
    btns.forEach(function (b, i) {
      b.addEventListener("click", function () { seek(starts[i], true); track("demo", "video:chapter" + i); });
    });
    vid.addEventListener("timeupdate", mark);
    vid.addEventListener("seeked", mark);
    vid.addEventListener("play", function () { track("demo", "video:play"); }, { once: true });
    var m = /^#t=(\d+(?:\.\d+)?)$/.exec(location.hash);
    if (m) { if (vid.preload === "none") vid.preload = "metadata"; seek(+m[1], false); }
    mark();
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
