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
