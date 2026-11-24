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

  /* ---------- Lead forms (FormSubmit AJAX endpoint — works on GitHub Pages) ----------
     Every <form class="lead-form" data-endpoint="..."> is handled here: the full contact form
     and the inline Free Trial / POC / Consultation forms on product and service pages.        */
  var INQUIRY = {
    trial: "Free trial request", poc: "Proof of Concept (POC) request", demo: "Product demo request",
    consulting: "Consultation request", sales: "Sales inquiry", general: "General inquiry"
  };
  var personal = /@(gmail|yahoo|hotmail|outlook|live|icloud|aol|proton|protonmail|gmx|mail|yandex)\./i;
  var params = new URLSearchParams(window.location.search);

  document.querySelectorAll("form.lead-form").forEach(function (form) {
    var typeInput = form.querySelector("[name='Inquiry type']");
    var subj = form.querySelector("input[name=_subject]");
    var sel = form.querySelector("select[name=Interest]");
    var status = form.querySelector(".form-status");
    var tabs = form.id === "contact-form" ? document.querySelectorAll("[data-inquiry]") : [];

    function refreshSubject() {
      if (!subj) return;
      var what = sel ? sel.value : (form.querySelector("[name=Interest]") || {}).value;
      subj.value = "New " + (typeInput ? typeInput.value : "inquiry") + (what ? " — " + what : "") + " — xploit-security.com";
    }
    function setType(t) {
      if (typeInput) typeInput.value = t;
      tabs.forEach(function (b) { b.setAttribute("aria-selected", b.getAttribute("data-inquiry") === t ? "true" : "false"); });
      refreshSubject();
    }
    tabs.forEach(function (b) { b.addEventListener("click", function () { setType(b.getAttribute("data-inquiry")); }); });
    if (sel) sel.addEventListener("change", refreshSubject);

    // The main contact form reads ?type= and ?interest= from the URL (e.g. /contact/?type=trial&interest=firewall-security-analyzer)
    if (form.id === "contact-form") {
      var interest = params.get("interest");
      if (interest && sel) Array.prototype.forEach.call(sel.options, function (o) { if (o.getAttribute("data-key") === interest) sel.value = o.value; });
      setType(INQUIRY[params.get("type")] || INQUIRY.sales);
    } else {
      refreshSubject();
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      status.className = "form-status"; status.textContent = "";
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var email = form.querySelector("input[type=email]").value;
      if (personal.test(email) && !form.dataset.warned) {
        form.dataset.warned = "1";
        status.className = "form-status err";
        status.textContent = "Please use your business email if you have one. Submit again to continue with this address.";
        return;
      }
      if (window.location.protocol === "file:") {
        status.className = "form-status err";
        status.innerHTML = "The form only sends once the site is online (opened over http/https). You're viewing a local copy. Please test it on the published site.";
        return;
      }
      var btn = form.querySelector("button[type=submit]");
      btn.disabled = true; var label = btn.innerHTML; btn.textContent = "Sending…";
      refreshSubject();
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      data["Page"] = document.title;
      fetch(form.getAttribute("data-endpoint"), {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok && (res.j.success === true || res.j.success === "true")) {
            var keep = typeInput ? typeInput.value : null;
            form.reset(); if (keep) setType(keep);
            status.className = "form-status ok";
            status.innerHTML = (form.getAttribute("data-success") || "Thank you — your request has been sent.") +
              " Our team will reply from <strong>hello@xploit-security.com</strong>, usually within one business day.";
          } else { var err = new Error((res.j && res.j.message) || "Submission failed"); err.fs = true; throw err; }
        })
        .catch(function (err) {
          if (err && err.fs && /activat/i.test(err.message)) {
            status.className = "form-status err";
            status.innerHTML = "This form is awaiting activation by the site owner. Please email <a href=\"mailto:hello@xploit-security.com\">hello@xploit-security.com</a> or message us on <a href=\"https://wa.me/14073074965\" target=\"_blank\" rel=\"noopener\">WhatsApp</a> in the meantime.";
            return;
          }
          var body = Object.keys(data).filter(function (k) { return k.charAt(0) !== "_"; }).map(function (k) { return k + ": " + data[k]; }).join("\n");
          status.className = "form-status err";
          status.innerHTML = "We couldn't send the form just now. Please email us directly at <a href=\"mailto:hello@xploit-security.com?subject=" +
            encodeURIComponent((typeInput ? typeInput.value : "Website inquiry")) + "&body=" + encodeURIComponent(body) + "\">hello@xploit-security.com</a> or message us on <a href=\"https://wa.me/14073074965\" target=\"_blank\" rel=\"noopener\">WhatsApp</a>.";
        })
        .finally(function () { btn.disabled = false; btn.innerHTML = label; });
    });
  });

  /* ---------- Screenshot galleries: tabs + lightbox ---------- */
  document.querySelectorAll("[data-gallery-tabs]").forEach(function (wrap) {
    var btns = wrap.querySelectorAll("[role=tab]");
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        btns.forEach(function (x) {
          var on = x === b; x.setAttribute("aria-selected", on ? "true" : "false");
          var panel = document.getElementById(x.getAttribute("aria-controls"));
          if (panel) panel.hidden = !on;
        });
      });
    });
  });
  var zoomables = Array.prototype.slice.call(document.querySelectorAll("img[data-zoom]"));
  if (zoomables.length) {
    var lb = document.createElement("div");
    lb.className = "lightbox"; lb.setAttribute("role", "dialog"); lb.setAttribute("aria-modal", "true"); lb.setAttribute("aria-label", "Screenshot viewer"); lb.hidden = true;
    lb.innerHTML = '<button class="lb-close" aria-label="Close">×</button><button class="lb-prev" aria-label="Previous">‹</button><figure><img alt=""><figcaption></figcaption></figure><button class="lb-next" aria-label="Next">›</button>';
    document.body.appendChild(lb);
    var lbImg = lb.querySelector("img"), lbCap = lb.querySelector("figcaption"), idx = 0, set = [], lastFocus;
    function show(i) {
      idx = (i + set.length) % set.length; var im = set[idx];
      lbImg.src = im.currentSrc || im.src; lbImg.alt = im.alt;
      var fc = im.closest("figure") && im.closest("figure").querySelector("figcaption");
      if (fc) { var c = fc.cloneNode(true); c.querySelectorAll(".ver-chip").forEach(function (x) { x.remove(); }); lbCap.textContent = c.textContent; } else { lbCap.textContent = im.alt; }
    }
    function open(im) {
      var group = im.getAttribute("data-zoom");
      set = zoomables.filter(function (x) { return x.getAttribute("data-zoom") === group && x.offsetParent !== null; });
      if (!set.length) set = [im];
      lastFocus = document.activeElement; lb.hidden = false; document.body.classList.add("nav-open");
      show(set.indexOf(im)); lb.querySelector(".lb-close").focus();
    }
    function close() { lb.hidden = true; document.body.classList.remove("nav-open"); if (lastFocus) lastFocus.focus(); }
    zoomables.forEach(function (im) {
      im.tabIndex = 0; im.setAttribute("role", "button"); im.setAttribute("aria-label", "Enlarge: " + im.alt);
      im.addEventListener("click", function () { open(im); });
      im.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(im); } });
    });
    lb.querySelector(".lb-close").addEventListener("click", close);
    lb.querySelector(".lb-prev").addEventListener("click", function () { show(idx - 1); });
    lb.querySelector(".lb-next").addEventListener("click", function () { show(idx + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    document.addEventListener("keydown", function (e) {
      if (lb.hidden) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(idx - 1);
      if (e.key === "ArrowRight") show(idx + 1);
    });
  }

  /* ---------- Sticky product CTA bar (shows after the hero scrolls away) ---------- */
  var sticky = document.querySelector(".sticky-cta");
  var heroEl = document.querySelector(".page-hero");
  if (sticky && heroEl && "IntersectionObserver" in window) {
    var targetSel = (sticky.querySelector("a") || {}).getAttribute ? sticky.querySelector("a").getAttribute("href") : null;
    var target = targetSel && targetSel.charAt(0) === "#" ? document.querySelector(targetSel) : null;
    var footerEl = document.querySelector(".site-footer");
    var vis = { hero: true, target: false, footer: false };
    var upd = function () { sticky.classList.toggle("show", !vis.hero && !vis.target && !vis.footer); };
    var watch = function (el, key) { if (el) new IntersectionObserver(function (en) { vis[key] = en[0].isIntersecting; upd(); }).observe(el); };
    watch(heroEl, "hero"); watch(target, "target"); watch(footerEl, "footer");
  }
})();
