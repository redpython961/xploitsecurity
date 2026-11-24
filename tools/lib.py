"""Shared layout, components and icons for the Xploit Security static site generator."""
import json, html

SITE = {
    "name": "Xploit Security",
    "domain": "https://xploit-security.com",
    "email": "hello@xploit-security.com",
    "wa": "https://wa.me/14073074965",
    "wa_display": "+1 407 307 4965",
    "academy": "https://www.xploitacademy.com/",
    "range": "https://cyber.xploitacademy.com/",
    "tagline": "Securing IT. Protecting OT. Enabling Trust.",
    "form_endpoint": "https://formsubmit.co/ajax/00a61be3578636a903da694c5b5a7a41",  # FormSubmit alias for hello@xploit-security.com
    "og_image": "/assets/img/brand/og-image.png",
}

# ---------------------------------------------------------------- icons (24x24 stroke)
_P = {
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
 "shield-check": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "server": '<rect x="2" y="3" width="20" height="8" rx="2"/><rect x="2" y="13" width="20" height="8" rx="2"/><path d="M6 7h.01M6 17h.01"/>',
 "factory": '<path d="M2 20V9l6 4V9l6 4V4h4l2 16z"/><path d="M6 17h2M11 17h2M16 17h2"/>',
 "cpu": '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3"/>',
 "cloud": '<path d="M17.5 19H8a6 6 0 1 1 1.7-11.8A5 5 0 0 1 19 9.5a4.75 4.75 0 0 1-1.5 9.5z"/>',
 "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
 "bug": '<rect x="8" y="6" width="8" height="14" rx="4"/><path d="M19 7l-3 2M5 7l3 2M19 19l-3-2M5 19l3-2M20 13h-4M4 13h4M10 4l1 2M14 4l-1 2"/>',
 "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
 "clipboard": '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
 "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h6"/>',
 "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 "user-check": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="m17 11 2 2 4-4"/>',
 "graduation": '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/>',
 "gauge": '<path d="M12 14l4-4"/><path d="M3.3 19a10 10 0 1 1 17.4 0"/>',
 "activity": '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
 "alert": '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
 "zap": '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
 "droplet": '<path d="M12 2.7s7 7.3 7 12.3a7 7 0 0 1-14 0c0-5 7-12.3 7-12.3z"/>',
 "flame": '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.4-.5-2-1-3-1.1-2.1-.2-4 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.2.4-2.3 1-3.2.3 1.5 1.3 2.7 2.5 2.7z"/>',
 "building": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/>',
 "landmark": '<path d="M3 22h18M6 18v-7M10 18v-7M14 18v-7M18 18v-7M12 2l8 5H4z"/>',
 "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
 "layers": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/>',
 "network": '<rect x="9" y="2" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="16" y="16" width="6" height="6" rx="1"/><path d="M12 8v4M5 16v-4h14v4"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "chev": '<path d="m6 9 6 6 6-6"/>',
 "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
 "play": '<polygon points="6 4 20 12 6 20 6 4"/>',
 "eye": '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8S1 12 1 12z"/><circle cx="12" cy="12" r="3"/>',
 "radar": '<path d="M19.1 4.9A10 10 0 1 0 22 12"/><path d="M16.2 7.8A6 6 0 1 0 18 12"/><circle cx="12" cy="12" r="2"/><path d="m13.4 10.6 6-6"/>',
 "scale": '<path d="M12 3v18M5 21h14M3 7h18M6 7l-3 7a4 4 0 0 0 6 0zM18 7l-3 7a4 4 0 0 0 6 0z"/>',
 "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2M2 13h20"/>',
 "health": '<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7z"/><path d="M3.2 12H9l1.5-3 2 6 1.5-3h4.8"/>',
 "truck": '<path d="M1 3h15v13H1zM16 8h4l3 3v5h-7z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>',
 "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.7-4 3-9 3s-9-1.3-9-3M3 5v14c0 1.7 4 3 9 3s9-1.3 9-3V5"/>',
 "settings": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 0 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 0 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 0 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 0 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
 "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5v15zM4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>',
 "award": '<circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/>',
 "pin": '<path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
 "terminal": '<path d="m4 17 6-6-6-6M12 19h8"/>',
 "train": '<rect x="4" y="3" width="16" height="14" rx="3"/><path d="M4 11h16M8 21l-2-4M16 21l2-4M8.5 14h.01M15.5 14h.01"/>',
 "compass": '<circle cx="12" cy="12" r="10"/><path d="m16.2 7.8-2.1 6.3-6.3 2.1 2.1-6.3z"/>',
 "refresh": '<path d="M23 4v6h-6M1 20v-6h6"/><path d="M3.5 9a9 9 0 0 1 14.8-3.4L23 10M1 14l4.7 4.4A9 9 0 0 0 20.5 15"/>',
 "chart": '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 6-6"/>',
 "key": '<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6M15.5 7.5l3 3L22 7l-3-3"/>',
 "wifi": '<path d="M5 12.55a11 11 0 0 1 14 0M1.4 9a16 16 0 0 1 21.2 0M8.5 16.4a6 6 0 0 1 7 0M12 20h.01"/>',
 "message": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "external": '<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14 21 3"/>',
 "home": '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
 "fingerprint": '<path d="M12 10a2 2 0 0 0-2 2c0 1 0 3-1 5M14 13.1c0 2.5 0 5-1 7.9M17.3 21.5c.1-.6.4-2.6.5-3.5M2 12a10 10 0 0 1 18-6M2 16h.01M21.8 16c.2-2 .1-5.4 0-6M5 19.5c.5-1.5 1-3 1-5.5a6 6 0 0 1 .3-1.9M8.6 21.9c.2-.7.4-1.4.5-2.1M9 6.8a6 6 0 0 1 9 5.2v2"/>',
}

def icon(name, cls=""):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_P[name]}</svg>'

WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-1 1.2-.4.2-.7.1a8.1 8.1 0 0 1-4-3.5c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-1-2.3c-.2-.6-.5-.5-.7-.5h-.6a1.1 1.1 0 0 0-.8.4 3.4 3.4 0 0 0-1 2.5 5.9 5.9 0 0 0 1.2 3.1 13.5 13.5 0 0 0 5.2 4.6c1.9.8 2.7.9 3.6.8a3.1 3.1 0 0 0 2-1.4 2.5 2.5 0 0 0 .2-1.4c-.1-.1-.3-.2-.6-.3zM12 21.8a9.8 9.8 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zM12 0a12 12 0 0 0-10.3 18L0 24l6.2-1.6A12 12 0 1 0 12 0z"/></svg>'

def esc(s):
    return html.escape(s, quote=True)

# ---------------------------------------------------------------- navigation model
SERVICES = [
    ("cybersecurity-consulting", "Cybersecurity Consulting", "Advisory, privacy and security programs", "compass"),
    ("vciso", "vCISO Services", "Fractional security leadership", "user-check"),
    ("it-cybersecurity", "IT Cybersecurity", "Pen testing, cloud and application security", "server"),
    ("ot-industrial-cybersecurity", "OT & Industrial Cybersecurity", "ICS/SCADA assessments and IEC 62443", "factory"),
    ("compliance-risk-management", "Compliance & Risk Management", "ISO 27001, SOC 2, CMMC, NCA, NESA and more", "scale"),
    ("security-assessments-audits", "Security Assessments & Audits", "Gap assessments, audits and reviews", "clipboard"),
]
PRODUCTS = [
    ("safemind", "SafeMind", "Security awareness SaaS", "graduation", "SaaS"),
    ("xploit-grc", "Xploit GRC", "GRC platform, SaaS or on-premises", "layers", "SaaS · On-prem"),
    ("firewall-security-analyzer", "Xploit Firewall Security Analyzer", "Firewall configuration audit & compliance", "shield-check", "Audit"),
    ("ot-attack-scenarios", "OT Cyber Attack Scenarios", "Free OT awareness range", "radar", "Free"),
    ("scada-simulator", "SCADA Simulator", "OT awareness & testing platform", "cpu", "OT"),
]

def pfile(path):
    """Map a logical page path to its file inside the folder layout.
    ''->index.html, 'services/'->services/index.html, 'services/vciso/'->services/vciso/index.html,
    'contact/?type=demo'->contact/index.html?type=demo. Asset paths are returned unchanged.
    Linking to index.html explicitly makes pages open both on GitHub Pages and from a local folder."""
    q = ""
    if "?" in path:
        path, q = path.split("?", 1); q = "?" + q
    frag = ""
    if "#" in path:
        path, frag = path.split("#", 1); frag = "#" + frag
    if path.startswith("assets/") or "." in path.rsplit("/", 1)[-1]:
        return path + q + frag
    p = path.strip("/")
    return (p + "/index.html" if p else "index.html") + q + frag

def abs_url(path):
    """Clean public URL (folder style) used for canonical, Open Graph, sitemap and JSON-LD."""
    p = path.split("?")[0]
    if p.endswith(".html") and "/" not in p and p != "index.html":
        return SITE["domain"] + "/" + p
    return SITE["domain"] + "/" + p.strip("/") + ("/" if p.strip("/") else "")

def rel(depth):
    return "../" * depth

def url(depth, path):
    """Relative link from a page at the given folder depth to a page or asset."""
    return rel(depth) + pfile(path)

def header(depth, active):
    r = lambda p: url(depth, p)
    svc = "".join(f'<li><a class="mega-item" href="{r("services/"+s+"/")}"><span class="ico">{icon(ic)}</span><span><strong>{esc(n)}</strong><small>{esc(d)}</small></span></a></li>' for s, n, d, ic in SERVICES)
    prd = "".join(
        f'<li><a class="mega-item" href="{r("products/"+s+"/")}"><span class="ico cyan">{icon(ic)}</span><span><strong>{esc(n)}{"<span class=badge-free>FREE</span>" if tag=="Free" else ""}</strong><small>{esc(d)}</small></span></a></li>'
        for s, n, d, ic, tag in PRODUCTS)
    def cur(k):
        return ' aria-current="page"' if active == k else ""
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="{r("")}" aria-label="Xploit Security home">
      <img src="{r("assets/img/brand/xploit-mark.png")}" alt="" width="40" height="40">
      <span class="brand-text"><strong>XPLOIT</strong><span>SECURITY</span></span>
    </a>
    <button class="menu-toggle" aria-controls="site-nav" aria-expanded="false" aria-label="Open menu">{icon("menu")}</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul>
        <li><a class="nav-link" href="{r("")}"{cur("home")}>Home</a></li>
        <li class="has-mega">
          <button class="nav-link" aria-expanded="false" aria-controls="mega-sp"{' aria-current="page"' if active=="sp" else ""}>Services &amp; Products {icon("chev")}</button>
          <div class="mega" id="mega-sp">
            <div class="container mega-inner">
              <div class="mega-col"><h4><a href="{r("services/")}">Cybersecurity Services →</a></h4><ul>{svc}</ul></div>
              <div class="mega-col"><h4><a href="{r("products/")}">Cybersecurity Products →</a></h4><ul>{prd}</ul></div>
              <div class="mega-feature">
                <div><span class="eyebrow">Try before you buy</span><h3>Free trial &amp; POCs</h3>
                <ul class="check-list" style="margin-top:12px">
                  <li><a href="{r("products/firewall-security-analyzer/")}#free-trial">XFSA: Request a Free Trial</a></li>
                  <li><a href="{r("products/safemind/")}#poc">SafeMind: Request a POC</a></li>
                  <li><a href="{r("products/xploit-grc/")}#poc">Xploit GRC: Request a POC</a></li>
                </ul></div>
                <a class="btn btn-cyan" href="{SITE["range"]}" target="_blank" rel="noopener">Free OT Attack Scenarios {icon("external")}</a>
              </div>
            </div>
          </div>
        </li>
        <li><a class="nav-link" href="{r("about/")}"{cur("about")}>About</a></li>
        <li><a class="nav-link" href="{r("faq/")}"{cur("faq")}>FAQ</a></li>
        <li><a class="nav-link" href="{r("contact/")}"{cur("contact")}>Contact</a></li>
      </ul>
      <a class="nav-academy" href="{SITE["academy"]}" target="_blank" rel="noopener" title="Cybersecurity training at Xploit Academy">Training → Xploit Academy</a>
      <a class="btn btn-primary nav-cta" href="{r("contact/?type=consulting")}">Request a Consultation</a>
    </nav>
  </div>
</header>'''

def footer(depth):
    r = lambda p: url(depth, p)
    svc = "".join(f'<li><a href="{r("services/"+s+"/")}">{esc(n)}</a></li>' for s, n, d, ic in SERVICES)
    prd = "".join(f'<li><a href="{r("products/"+s+"/")}">{esc(n)}</a></li>' for s, n, d, ic, t in PRODUCTS)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="brand" href="{r("")}" aria-label="Xploit Security home"><img src="{r("assets/img/brand/xploit-mark.png")}" alt="" width="40" height="40" loading="lazy"><span class="brand-text"><strong>XPLOIT</strong><span>SECURITY</span></span></a>
        <p>Xploit Security delivers IT and OT cybersecurity consulting, compliance and assessment services, and builds the SafeMind, Xploit GRC, Xploit Firewall Security Analyzer and SCADA Simulator platforms. Headquartered in Dubai, serving clients worldwide.</p>
        <div class="footer-contact">
          <a href="mailto:{SITE["email"]}">{icon("mail")}{SITE["email"]}</a>
          <a href="{SITE["wa"]}" target="_blank" rel="noopener">{icon("message")}WhatsApp {SITE["wa_display"]}</a>
        </div>
        <a class="academy-link" href="{SITE["academy"]}" target="_blank" rel="noopener"><div><span>Training</span><strong>Training → Xploit Academy</strong></div>{icon("external")}</a>
      </div>
      <div><h4>Services</h4><ul><li><a href="{r("services/")}">All services</a></li>{svc}</ul></div>
      <div><h4>Products</h4><ul><li><a href="{r("products/")}">All products</a></li>{prd}</ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="{r("about/")}">About</a></li>
        <li><a href="{r("faq/")}">FAQ</a></li>
        <li><a href="{r("contact/")}">Contact</a></li>
        <li><a href="{r("products/firewall-security-analyzer/")}#free-trial">XFSA free trial</a></li>
        <li><a href="{r("products/safemind/")}#poc">SafeMind POC</a></li>
        <li><a href="{r("products/xploit-grc/")}#poc">Xploit GRC POC</a></li>
        <li><a href="{r("contact/?type=consulting")}">Request a Consultation</a></li>
        <li><a href="{SITE["academy"]}" target="_blank" rel="noopener">Xploit Academy</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Xploit Cyber Security Services. Registered in the United Arab Emirates. All rights reserved.</span>
      <span class="tag">{SITE["tagline"]}</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{SITE["wa"]}" target="_blank" rel="noopener" aria-label="Chat with Xploit Security on WhatsApp">{WA_SVG}</a>'''

ORG_LD = {
    "@context": "https://schema.org", "@type": "Organization", "@id": SITE["domain"] + "/#org",
    "name": "Xploit Security", "legalName": "Xploit Cyber Security Services", "url": SITE["domain"] + "/",
    "logo": SITE["domain"] + "/assets/img/brand/icon-512.png", "email": SITE["email"],
    "slogan": SITE["tagline"],
    "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"},
    "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "email": SITE["email"], "telephone": "+1-407-307-4965", "availableLanguage": ["English", "Arabic"]}],
    "sameAs": [SITE["academy"]],
}

def page(depth, path, title, desc, body, active="", ld=None, crumbs=None, robots="index,follow", keywords=""):
    r = rel(depth)
    canon = abs_url(path)
    lds = [ORG_LD]
    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE["domain"] + "/"}]
        for i, (n, p) in enumerate(crumbs, start=2):
            items.append({"@type": "ListItem", "position": i, "name": n, "item": abs_url(p)})
        lds.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})
    if ld:
        lds.extend(ld if isinstance(ld, list) else [ld])
    ld_html = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    full_title = title if "Xploit Security" in title else f"{title} | Xploit Security"
    kw = f'\n<meta name="keywords" content="{esc(keywords)}">' if keywords else ""
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">{kw}
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#07090d">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Xploit Security">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE["domain"]}{SITE["og_image"]}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(full_title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE["domain"]}{SITE["og_image"]}">
<link rel="icon" href="{r}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{r}assets/img/brand/favicon-32.png">
<link rel="apple-touch-icon" href="{r}assets/img/brand/apple-touch-icon.png">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preload" href="{r}assets/fonts/space-grotesk-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{r}assets/fonts/space-grotesk-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/css/styles.css">
{ld_html}
</head>
<body>
{header(depth, active)}
<main id="main">
{body}
</main>
{footer(depth)}
<script src="{r}assets/js/main.js" defer></script>
</body>
</html>
'''

# ---------------------------------------------------------------- components
def breadcrumb(depth, crumbs):
    items = [f'<li><a href="{url(depth, "")}">Home</a></li>']
    for i, (n, p) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{esc(n)}</li>')
        else:
            items.append(f'<li><a href="{url(depth, p)}">{esc(n)}</a></li>')
    return f'<nav aria-label="Breadcrumb"><ol class="breadcrumb">{"".join(items)}</ol></nav>'

def checks(items, cls=""):
    return f'<ul class="check-list {cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def chips(items, cls=""):
    return '<div class="chips">' + "".join(f'<span class="chip {cls}">{esc(i)}</span>' for i in items) + "</div>"

def card(ic, title, text, href=None, cyan=False, tag=None, tagcls="", link="Learn more", extra=""):
    t = f'<span class="card-tag {tagcls}">{esc(tag)}</span>' if tag else ""
    inner = f'{t}<div class="ico {"cyan" if cyan else ""}">{icon(ic)}</div><h3>{title}</h3><p>{text}</p>{extra}'
    if href:
        return f'<a class="card hover reveal {"cyan" if cyan else ""}" href="{href}">{inner}<span class="link-arrow">{link} {icon("arrow")}</span></a>'
    return f'<div class="card reveal">{inner}</div>'

def cta_band(depth, title, text, primary=("Talk to us", "contact/"), secondary=None, wa=True):
    btns = f'<a class="btn btn-primary" href="{url(depth, primary[1])}">{primary[0]} {icon("arrow")}</a>'
    if secondary:
        btns += f'<a class="btn btn-ghost" href="{url(depth, secondary[1]) if not secondary[1].startswith("http") else secondary[1]}">{secondary[0]}</a>'
    if wa:
        btns += f'<a class="btn btn-wa" href="{SITE["wa"]}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a>'
    return f'''<section class="section"><div class="container"><div class="cta-band reveal">
<span class="eyebrow">Next step</span><h2>{title}</h2><p>{text}</p><div class="btn-row">{btns}</div>
<p class="note">Or email <a href="mailto:{SITE["email"]}">{SITE["email"]}</a></p></div></div></section>'''

def page_hero(depth, crumbs, eyebrow, h1, lead, buttons, side="", ot=False, eyebrow_cyan=False):
    return f'''<section class="page-hero grid-bg {"ot" if ot else ""}"><div class="container">
{breadcrumb(depth, crumbs)}
<div class="page-hero-grid"><div>
<span class="eyebrow {"cyan" if eyebrow_cyan else ""}">{eyebrow}</span>
<h1>{h1}</h1>
<p class="lead">{lead}</p>
<div class="btn-row">{buttons}</div>
</div>{f'<aside class="page-hero-card">{side}</aside>' if side else ""}</div></div></section>'''

def shot(depth, name, alt, caption=None, frame=True, w=None, h=None, eager=False):
    dims = f' width="{w}" height="{h}"' if w else ""
    img = f'<img src="{url(depth, "assets/img/products/"+name+".webp")}" alt="{esc(alt)}"{dims} {"" if eager else "loading=\"lazy\""} decoding="async">'
    cap = f"<figcaption>{esc(caption)}</figcaption>" if caption else ""
    if frame:
        return f'<figure class="reveal"><div class="shot-frame"><div class="bar"><i></i><i></i><i></i></div>{img}</div>{cap}</figure>'
    return f'<figure class="reveal"><div class="shot">{img}</div>{cap}</figure>'

def section_head(eyebrow, title, lead="", center=False, cyan=False):
    return f'<div class="section-head {"center" if center else ""} reveal"><span class="eyebrow {"cyan" if cyan else ""}">{eyebrow}</span><h2>{title}</h2>{f"<p class=lead>{lead}</p>" if lead else ""}</div>'

# ---------------------------------------------------------------- lead generation
COUNTRIES = ["United Arab Emirates", "Saudi Arabia", "Qatar", "Kuwait", "Bahrain", "Oman", "Egypt", "Jordan", "Lebanon", "Iraq", "Morocco", "Türkiye",
             "India", "Pakistan", "United Kingdom", "United States", "Canada", "Australia", "Germany", "France", "Netherlands", "Singapore", "Other"]

def _hidden(subject, inquiry, interest):
    return (f'<input type="hidden" name="_subject" value="{esc(subject)}">'
            '<input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">'
            f'<input type="hidden" name="Inquiry type" value="{esc(inquiry)}">'
            + (f'<input type="hidden" name="Interest" value="{esc(interest)}">' if interest else "")
            + '<div class="hp" aria-hidden="true"><label>Leave this field empty<input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>')

def lead_form(fid, inquiry, interest, title, intro, button, success, extra=None):
    """Compact inline lead form. extra = list of (label, name, [options]) selects or (label, name, None) text inputs."""
    copts = "".join(f"<option>{c}</option>" for c in COUNTRIES)
    ex = ""
    for lab, name, opts in (extra or []):
        if opts:
            o = "".join(f"<option>{esc(x)}</option>" for x in opts)
            ex += f'<div class="field"><label for="{fid}-{name}">{esc(lab)}</label><select id="{fid}-{name}" name="{esc(lab)}"><option value="">Select</option>{o}</select></div>'
        else:
            ex += f'<div class="field"><label for="{fid}-{name}">{esc(lab)}</label><input id="{fid}-{name}" name="{esc(lab)}" type="text"></div>'
    return f'''<div class="lead-card reveal" id="{fid}">
<h3>{title}</h3><p>{intro}</p>
<form class="lead-form" data-endpoint="{SITE["form_endpoint"]}" data-success="{esc(success)}" action="{SITE["form_endpoint"].replace("/ajax/", "/")}" method="POST" novalidate>
{_hidden("New " + inquiry + " — " + interest, inquiry, interest)}
<div class="form-grid">
<div class="field"><label for="{fid}-name">Full name <span class="req">*</span></label><input id="{fid}-name" name="Name" type="text" autocomplete="name" required></div>
<div class="field"><label for="{fid}-email">Business email <span class="req">*</span></label><input id="{fid}-email" name="email" type="email" autocomplete="email" required placeholder="you@company.com"></div>
<div class="field"><label for="{fid}-company">Company <span class="req">*</span></label><input id="{fid}-company" name="Company" type="text" autocomplete="organization" required></div>
<div class="field"><label for="{fid}-country">Country <span class="req">*</span></label><select id="{fid}-country" name="Country" required><option value="">Select country</option>{copts}</select></div>
{ex}
<div class="field full"><label for="{fid}-msg">Anything we should know?</label><textarea id="{fid}-msg" name="Message" placeholder="Goals, timelines, environment…"></textarea></div>
<div class="field full"><label class="consent"><input type="checkbox" name="Consent" value="Yes" required> <span>I agree that Xploit Security may contact me about this request.</span></label></div>
</div>
<div style="margin-top:16px"><button class="btn btn-primary" type="submit">{button} {icon("arrow")}</button></div>
<div class="form-status" role="status" aria-live="polite"></div>
</form></div>'''

def sticky_cta(text, label, href):
    return f'<div class="sticky-cta" aria-hidden="false"><span>{text}</span><a class="btn btn-primary" href="{href}">{label}</a></div>'

def zshot(depth, name, alt, caption, group, w, h, chip=None, frame=True, cls=""):
    """Zoomable screenshot (opens in the lightbox gallery `group`)."""
    chiphtml = f'<span class="ver-chip {chip[0]}">{chip[1]}</span>' if chip else ""
    img = f'<img src="{url(depth, "assets/img/products/"+name+".webp")}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async" data-zoom="{group}">'
    inner = f'<div class="shot-frame"><div class="bar"><i></i><i></i><i></i></div>{img}</div>' if frame else f'<div class="shot">{img}</div>'
    return f'<figure class="reveal {cls}">{inner}<figcaption>{chiphtml}{esc(caption)}</figcaption></figure>'
