/* Xploit Security — site behaviour (no dependencies) */
(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");

  /* ---------- Mobile navigation ---------- */
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      document.body.classList.toggle("nav-open", open);
    });
  }

  /* ---------- Mega menu ---------- */
  var megaItems = document.querySelectorAll(".has-mega");
  var desktop = window.matchMedia("(min-width: 1081px)");
  megaItems.forEach(function (item) {
    var btn = item.querySelector(".nav-link");
    var closeTimer;
    function setOpen(state) {
      item.classList.toggle("open", state);
      btn.setAttribute("aria-expanded", state ? "true" : "false");
    }
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      setOpen(!item.classList.contains("open"));
    });
    item.addEventListener("mouseenter", function () { if (desktop.matches) { clearTimeout(closeTimer); setOpen(true); } });
    item.addEventListener("mouseleave", function () { if (desktop.matches) { closeTimer = setTimeout(function () { setOpen(false); }, 160); } });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && item.classList.contains("open")) { setOpen(false); btn.focus(); } });
    document.addEventListener("click", function (e) { if (desktop.matches && !item.contains(e.target)) setOpen(false); });
  });

  /* ---------- Reveal on scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- SafeMind pricing calculator (rates from the SafeMind price list) ---------- */
  var calc = document.getElementById("sm-calc");
  if (calc) {
    var range = calc.querySelector("input[type=range]");
    var tiers = [[25, 50, 3.4], [51, 100, 3.1], [101, 500, 2.75], [501, 1000, 2.45], [1001, 2000, 2.2], [2001, 3000, 2.0], [3001, 5000, 1.8]];
    var fmt = function (n) { return "$" + n.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); };
    var update = function () {
      var u = parseInt(range.value, 10);
      calc.querySelector(".calc-users").textContent = u.toLocaleString("en-US") + (u >= 5001 ? "+" : "");
      var rate = null;
      tiers.forEach(function (t) { if (u >= t[0] && u <= t[1]) rate = t[2]; });
      var r = calc.querySelector("[data-rate]"), m = calc.querySelector("[data-month]"), y = calc.querySelector("[data-year12]");
      if (rate === null) { r.textContent = "Custom"; m.textContent = "Get a quote"; y.textContent = "Get a quote"; }
      else { r.textContent = fmt(rate); m.textContent = fmt(rate * u); y.textContent = fmt(rate * u * 12); }
    };
    range.addEventListener("input", update);
    update();
  }

  /* ---------- SCADA Simulator configurator -> WhatsApp ---------- */
  var cfg = document.getElementById("scada-config");
  if (cfg) {
    var summary = cfg.querySelector(".config-summary span");
    var waBtn = cfg.querySelector("[data-wa]");
    var mailBtn = cfg.querySelector("[data-mail]");
    var readCfg = function () {
      var get = function (n) { var el = cfg.querySelector("input[name=" + n + "]:checked"); return el ? el.value : ""; };
      var s = get("sector") + ", " + get("plc") + " PLCs, " + get("size") + " size";
      summary.textContent = s;
      var msg = "Hello Xploit Security, I'd like a SCADA Simulator demo. Requested setup: " + s + ".";
      waBtn.href = "https://wa.me/14073074965?text=" + encodeURIComponent(msg);
      mailBtn.href = "mailto:hello@xploit-security.com?subject=" + encodeURIComponent("SCADA Simulator demo request") + "&body=" + encodeURIComponent(msg);
    };
    cfg.addEventListener("change", readCfg);
    readCfg();
  }

  /* ---------- Contact form (FormSubmit AJAX endpoint — works on GitHub Pages) ---------- */
  var form = document.getElementById("contact-form");
  if (form) {
    // Pre-select interest / inquiry type from URL: /contact/?interest=safemind&type=demo
    var params = new URLSearchParams(window.location.search);
    var interest = params.get("interest");
    var sel = form.querySelector("#f-interest");
    if (interest && sel) {
      Array.prototype.forEach.call(sel.options, function (o) { if (o.getAttribute("data-key") === interest) sel.value = o.value; });
    }
    var typeTabs = document.querySelectorAll("[data-inquiry]");
    var typeInput = form.querySelector("#f-type");
    var setType = function (t) {
      typeTabs.forEach(function (b) { b.setAttribute("aria-selected", b.getAttribute("data-inquiry") === t ? "true" : "false"); });
      if (typeInput) typeInput.value = t;
      var subj = form.querySelector("input[name=_subject]");
      if (subj) subj.value = "New " + t + " — xploit-security.com";
    };
    typeTabs.forEach(function (b) { b.addEventListener("click", function () { setType(b.getAttribute("data-inquiry")); }); });
    var t0 = params.get("type");
    var map = { demo: "Product demo request", consulting: "Consulting inquiry", sales: "Sales inquiry", general: "General contact" };
    setType(map[t0] || "Sales inquiry");

    var status = document.getElementById("form-status");
    var personal = /@(gmail|yahoo|hotmail|outlook|live|icloud|aol|proton|protonmail|gmx|mail|yandex)\./i;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      status.className = "form-status"; status.textContent = "";
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var email = form.querySelector("#f-email").value;
      if (personal.test(email) && !form.dataset.warned) {
        form.dataset.warned = "1";
        status.className = "form-status err";
        status.textContent = "Please use your business email if you have one. Submit again to continue with this address.";
        return;
      }
      var btn = form.querySelector("button[type=submit]");
      btn.disabled = true; var label = btn.innerHTML; btn.textContent = "Sending…";
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      fetch(form.getAttribute("data-endpoint"), {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok && (res.j.success === true || res.j.success === "true")) {
            var keep = typeInput.value; form.reset(); setType(keep || "Sales inquiry");
            status.className = "form-status ok";
            status.innerHTML = "Thank you — your inquiry has been sent. Our team will reply from <strong>hello@xploit-security.com</strong>, usually within one business day.";
          } else { throw new Error((res.j && res.j.message) || "Submission failed"); }
        })
        .catch(function () {
          var body = Object.keys(data).filter(function (k) { return k.charAt(0) !== "_"; }).map(function (k) { return k + ": " + data[k]; }).join("\n");
          status.className = "form-status err";
          status.innerHTML = "We couldn't send the form just now. Please email us directly at <a href=\"mailto:hello@xploit-security.com?subject=" +
            encodeURIComponent("Website inquiry") + "&body=" + encodeURIComponent(body) + "\">hello@xploit-security.com</a> or message us on <a href=\"https://wa.me/14073074965\" target=\"_blank\" rel=\"noopener\">WhatsApp</a>.";
        })
        .finally(function () { btn.disabled = false; btn.innerHTML = label; });
    });
  }
})();
