// [DBA name] site behavior: the first-party visit counter, the privacy opt-out, the workflow demo,
// the service finder and scroll reveals.
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
      if (v) { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); return; }
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
    f.hidden = false;

    function pick() {
      if (ans[2] === "l") return "nofit";
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
        var next = f.querySelector('[data-q="' + (n + 1) + '"]');
        if (next) next.hidden = false;
        if (ans[1] && ans[2] && ans[3]) show();
        return;
      }
      if (ev.target.closest("[data-reset]")) {
        ans = {}; shown = "";
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
