// [DBA name] site behavior: the first-party visit counter and the privacy opt-out.
// Sends to /api/e on our own domain only. No third-party scripts, no IP logging, no contact details.
(function () {
  "use strict";
  var ENDPOINT = "/api/e";

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
    if (navigator.globalPrivacyControl) return;
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

  // ---- Motion: scroll reveal, illustrations and the sync stages --------------------------------
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.documentElement.classList.add("js");

  function countTo(el, to) {
    var from = parseInt(el.textContent, 10) || 0;
    if (reduce || from === to) { el.textContent = to; return; }
    var t0 = null, dur = 650;
    function f(t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / dur), v = Math.round(from + (to - from) * (1 - Math.pow(1 - k, 3)));
      el.textContent = v;
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
    stage.querySelectorAll("[data-step]").forEach(function (el) {
      el.classList.toggle("on", +el.getAttribute("data-step") <= n);
    });
    stage.querySelectorAll(".flip").forEach(function (el) {
      var target = stepOf(el) <= n ? +el.getAttribute("data-to") : +el.getAttribute("data-from");
      if (n === 0) el.textContent = target; else if (+el.textContent !== target) countTo(el, target);
    });
  }

  function runStage(stage) {
    var times = (stage.getAttribute("data-times") || "").split(",").map(Number);
    var last = times.length;
    if (reduce) { setStep(stage, last); stage.querySelectorAll("tr.hit").forEach(function (r) { r.classList.add("settled"); }); return; }
    var timers = [], visible = false;
    function cycle() {
      timers.forEach(clearTimeout); timers = [];
      stage.classList.remove("run");
      stage.querySelectorAll("tr.hit").forEach(function (r) { r.classList.remove("settled"); });
      setStep(stage, 0);
      void stage.offsetWidth;
      stage.classList.add("run");
      times.forEach(function (t, i) { timers.push(setTimeout(function () { setStep(stage, i + 1); }, t)); });
      timers.push(setTimeout(function () {
        stage.querySelectorAll("tr.hit").forEach(function (r) { r.classList.add("settled"); });
      }, times[last - 1] + 1200));
      timers.push(setTimeout(function () { if (visible) cycle(); else running = false; }, times[last - 1] + 4200));
    }
    var running = false;
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        visible = en.isIntersecting;
        if (visible && !running) { running = true; cycle(); }
      });
    }, { threshold: 0.35 });
    io.observe(stage);
  }

  if ("IntersectionObserver" in window) {
    var rv = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); rv.unobserve(en.target); }
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
    document.querySelectorAll(".reveal, .mini, .steps.draw li, .timeline.draw li").forEach(function (el) { rv.observe(el); });
    document.querySelectorAll("[data-stage]").forEach(runStage);
  } else {
    document.querySelectorAll(".reveal, .mini").forEach(function (el) { el.classList.add("in"); });
    document.querySelectorAll("[data-stage]").forEach(function (s) { setStep(s, 99); });
  }

  if (location.protocol === "https:") send("view");

  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest("[data-track]");
    if (a && location.protocol === "https:") send(a.getAttribute("data-track"), { where: a.getAttribute("data-where") || "" });
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
