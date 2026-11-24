from lib import *
from pages_home import clients_band

def about():
    d = 1
    path = "about/"
    crumbs = [("About", path)]
    btns = f'<a class="btn btn-primary" href="{url(d, "contact/")}">Contact us {icon("arrow")}</a><a class="btn btn-ghost" href="{url(d, "services/")}">Our services</a>'
    side = f'<h3>Company</h3>{checks(["Xploit Cyber Security Services, registered in the UAE", "Headquartered in Dubai", "Regional presence in the USA, UK and India", "Part of the Xploit family, alongside Xploit Academy"])}'
    hero = page_hero(d, crumbs, "About Xploit Security", "The corporate technology arm of the Xploit family.",
                     "We deliver IT and OT cybersecurity services that protect critical infrastructure, enterprise applications and government organizations, and we build the platforms that keep those programs running.", btns, side)
    body = hero + f'''
<section class="section"><div class="container"><div class="split">
<div class="reveal"><span class="eyebrow">Who we are</span><h2>Practitioners who build what they use.</h2></div>
<div class="reveal">
<p>Xploit Security is the cybersecurity consulting, services and software business of the Xploit family. Our services are innovative, proactive and trusted, designed to strengthen digital resilience and compliance in an evolving threat landscape.</p>
<p>We work across both worlds most providers treat separately: enterprise IT, where data, users and cloud workloads live, and operational technology, where PLCs, SCADA and physical processes keep utilities and industry running. That converged view shapes everything we do, from a penetration test to a board-level risk report.</p>
<p>Alongside consulting, we develop our own software, SafeMind, Xploit GRC, Xploit Firewall Security Analyzer and the SCADA Simulator, because we wanted tools that remove work instead of creating it.</p>
</div></div></div></section>

<section class="section section-alt"><div class="container"><div class="grid grid-2">
<div class="card reveal"><div class="ico">{icon("target")}</div><h3>Our mission</h3><p>To help organizations identify cyber risk early, strengthen their defenses and build lasting cyber resilience across IT and OT, with practical services and platforms that make security part of everyday operations.</p></div>
<div class="card reveal"><div class="ico cyan">{icon("eye")}</div><h3>Our vision</h3><p>A world where enterprises and critical infrastructure operators can innovate with confidence because their people, systems and processes are secure by design, and trust is earned and proven.</p></div>
</div></div></section>

<section class="section"><div class="container">
{section_head("What we do", "Two pillars. One mission.")}
<div class="grid grid-2">
<div class="card reveal"><div class="ico">{icon("briefcase")}</div><h3>Cybersecurity services</h3><p style="margin-bottom:16px">Professional consulting, advisory, assessments, governance, compliance and IT/OT security services.</p>
{checks(["Penetration testing (web, mobile, OT and IoT)", "Cloud security audits and architecture reviews", "IT and OT/ICS security assessments", "Governance, risk and compliance", "Data privacy and protection", "Virtual CISO advisory", "Cybersecurity awareness and training"])}
<a class="link-arrow" href="{url(d, "services/")}" style="margin-top:18px">Explore services {icon("arrow")}</a></div>
<div class="card reveal"><div class="ico cyan">{icon("layers")}</div><h3>Cybersecurity products</h3><p style="margin-bottom:16px">Commercial SaaS platforms and practical industrial cybersecurity solutions.</p>
{checks(["SafeMind: cybersecurity awareness SaaS", "Xploit GRC: GRC platform, SaaS or on-premises", "Xploit Firewall Security Analyzer: firewall audit & compliance", "SCADA Simulator: OT awareness and testing", "OT Cyber Attack Scenarios: free resource"], "cyan")}
<a class="link-arrow" href="{url(d, "products/")}" style="margin-top:18px">Explore products {icon("arrow")}</a></div>
</div></div></section>

<section class="section section-alt"><div class="container"><div class="split" style="align-items:start">
<div class="reveal"><span class="eyebrow">Our team</span><h2>Practitioners, not just advisors.</h2>
<p>Our penetration testing and GRC teams include professionals from AWS, Mandiant, Motorola and The World Bank. A structured planning and collaboration approach ensures timely, high-quality, tailored solutions.</p>
<div class="org" style="margin-top:28px">
<div class="org-col"><h3>GRC</h3><ul><li>Head of GRC</li><li>GRC Manager</li><li>GRC Consultants</li><li>vCISOs</li></ul></div>
<div class="org-col"><h3>Cybersecurity</h3><ul><li>Head of Cybersecurity</li><li>Lead Penetration Tester</li><li>Penetration Testers</li></ul></div>
<div class="org-col"><h3>Delivery</h3><ul><li>Project Manager</li><li>Client Success</li></ul></div>
<div class="org-col"><h3>Leadership</h3><ul><li>CEO / Founder</li></ul></div>
</div></div>
<div class="reveal"><span class="eyebrow">Where we are</span><h2>A global footprint, a local touch.</h2>
<div class="grid" style="gap:12px;margin-top:20px">
<div class="loc hq"><strong>Dubai, UAE</strong><span>Headquarters</span></div>
<div class="loc"><strong>United States</strong><span>Regional presence</span></div>
<div class="loc"><strong>United Kingdom</strong><span>Regional presence</span></div>
<div class="loc"><strong>India</strong><span>Regional presence</span></div>
</div>
<p style="margin-top:20px">We serve enterprise, critical infrastructure and government clients across the Gulf and internationally, on-site or remotely.</p></div>
</div></div></section>

<section class="section"><div class="container">
{section_head("What sets us apart", "Our commitment to your resilience.")}
<div class="grid grid-4">
{card("award", "Industry expertise", "Backed by years of cybersecurity leadership experience.")}
{card("scale", "Compliance and standards", "Experts in global and regional compliance frameworks.")}
{card("layers", "Comprehensive solutions", "Covering infrastructure, applications, cloud and operations.")}
{card("users", "Trusted partnerships", "A proven record with government, enterprise and critical industries.")}
</div></div></section>

{clients_band(d)}

<section class="section"><div class="container"><div class="cta-band reveal">
<span class="eyebrow">The Xploit family</span><h2>Looking for cybersecurity training?</h2>
<p>Xploit Academy is our education business: self-paced and hands-on courses in OT/ICS security, ISO 27001, SOC 2, CMMC, ethical hacking, cloud security and more. Xploit Security focuses on consulting, services and software.</p>
<div class="btn-row"><a class="btn btn-primary" href="{SITE["academy"]}" target="_blank" rel="noopener">Training → Xploit Academy {icon("external")}</a><a class="btn btn-ghost" href="{url(d, "contact/")}">Talk to Xploit Security</a></div>
</div></div></section>'''
    ld = {"@context": "https://schema.org", "@type": "AboutPage", "name": "About Xploit Security", "url": abs_url(path), "about": {"@id": SITE["domain"] + "/#org"}}
    return path, page(d, path, "About Xploit Security: IT & OT Cybersecurity Company in Dubai",
                      "Xploit Security is a Dubai-headquartered cybersecurity services and technology company delivering IT and OT security consulting, compliance and the SafeMind, Xploit GRC and SCADA Simulator platforms.",
                      body, "about", ld, crumbs, keywords="cybersecurity company Dubai, IT and OT cybersecurity, Xploit Security, cybersecurity services UAE")

FAQ = [
    ("General", "globe", "general", [
        ("What is Xploit Security?", "<p>Xploit Security is the cybersecurity services and technology arm of the Xploit family, operated by Xploit Cyber Security Services, a company registered in the United Arab Emirates. We provide IT and OT cybersecurity consulting, compliance and assessment services, and we build commercial platforms: SafeMind (awareness SaaS), Xploit GRC (governance, risk and compliance) and the SCADA Simulator (OT awareness and testing).</p><p>For cybersecurity courses and certifications, see our sister brand <a href=\"https://www.xploitacademy.com/\" target=\"_blank\" rel=\"noopener\">Xploit Academy</a>.</p>"),
        ("What industries do you support?", "<p>We work with critical infrastructure, enterprise and government organizations, including energy and power, water and wastewater, oil and gas, manufacturing, financial services and fintech, telecom and cloud providers, healthcare and pharma, SaaS and technology companies, and defense-industrial-base suppliers.</p>"),
        ("What geographical markets do you serve?", "<p>We're headquartered in Dubai, UAE, with regional presence in the United States, the United Kingdom and India. We have deep experience with UAE and Saudi regulations (NESA, CBUAE, ADGM, DIFC, NCA ECC, NCA CCC, SAMA, Aramco SACS-002) and deliver international standards such as ISO 27001, SOC 2, CMMC, PCI DSS and GDPR for clients worldwide.</p>"),
        ("Do you provide remote consulting?", "<p>Yes. Most advisory, vCISO, compliance and GRC work is delivered remotely, with on-site visits where they add value, such as OT site assessments, workshops or audits. Penetration testing can be performed remotely or on-site depending on scope.</p>"),
    ]),
    ("Cybersecurity services", "briefcase", "services", [
        ("Do you provide vCISO services?", "<p>Yes. Our <a href=\"../services/vciso/\">vCISO services</a> give you a senior security leader who owns strategy, governance, risk, board reporting and compliance programs on a flexible, fractional basis, for startups, scale-ups and enterprises.</p>"),
        ("Can you help organizations achieve ISO 27001 certification?", "<p>Yes. We provide end-to-end ISO/IEC 27001:2022 implementation and certification readiness: scoping, risk assessment, Statement of Applicability, policies and controls, internal audits by certified lead auditors, management review and support during the certification audit. The certificate itself is issued by an accredited certification body.</p>"),
        ("Do you provide SOC 2 and CMMC consulting?", "<p>Yes. We deliver SOC 2 Type 1 and Type 2 readiness, control implementation and auditor coordination, and CMMC Level 1 and Level 2 readiness, including NIST SP 800-171 assessments, SSP and POA&amp;M preparation. See <a href=\"../services/compliance-risk-management/\">Compliance &amp; Risk Management</a>.</p>"),
        ("Do you perform IT and OT cybersecurity assessments?", "<p>Yes. We perform IT security assessments, penetration testing (web, mobile, IoT and networks), cloud security audits for AWS, Azure and GCP, and OT/ICS security assessments aligned with IEC 62443 and NCA OTCC, planned around safety and uptime. See <a href=\"../services/it-cybersecurity/\">IT Cybersecurity</a> and <a href=\"../services/ot-industrial-cybersecurity/\">OT &amp; Industrial Cybersecurity</a>.</p>"),
    ]),
    ("Products", "layers", "products", [
        ("What is SafeMind?", "<p><a href=\"../products/safemind/\">SafeMind</a> is a cybersecurity awareness platform that combines 100+ microlearning lessons, unlimited realistic phishing simulations, AI-powered learning journeys, reporting by individual, department or organization, and awareness tips delivered in Microsoft Teams and Slack.</p>"),
        ("What is Xploit GRC?", "<p><a href=\"../products/xploit-grc/\">Xploit GRC</a> is a cybersecurity governance, risk and compliance platform. It centralizes risk registers, compliance and control assessments, policies, audits, findings and corrective actions, IT and OT assets, third-party risk, evidence and executive dashboards, with a library of 38+ frameworks and the ability to import your own.</p>"),
        ("What is Xploit Firewall Security Analyzer?", "<p><a href=\"../products/firewall-security-analyzer/\">Xploit Firewall Security Analyzer (XFSA)</a> audits firewall configuration exports against a version-controlled rule library. It flags known firmware vulnerabilities (CVEs), over-permissive and risky rules, exposed management, weak VPN cryptography, and logging and inspection gaps. It scores compliance against standards such as NIST SP 800-53, PCI DSS 4.0.1 and vendor hardening guidance, and produces a report with configuration evidence and remediation for every finding. XFSA is available as a cloud SaaS or as a desktop application installed on your own infrastructure. FortiGate is fully supported today; <a href=\"../contact/?type=sales&amp;interest=firewall-security-analyzer\">contact us</a> about other vendors.</p>"),
        ("Can I try your products before buying?", "<p>Yes. You can request a <a href=\"../products/firewall-security-analyzer/#free-trial\">free trial of XFSA</a> (SaaS or Desktop), and a guided Proof of Concept (POC) for <a href=\"../products/safemind/#poc\">SafeMind</a> or <a href=\"../products/xploit-grc/#poc\">Xploit GRC</a>. You can evaluate each platform in your own environment before making a purchasing decision.</p>"),
        ("Can Xploit GRC be hosted on-premises?", "<p>Yes. Xploit GRC is available as a tenant-isolated SaaS platform, with optional KSA or UAE data residency and dedicated hosting, and it can also be deployed on-premises in your own environment. <a href=\"../contact/?type=sales&amp;interest=xploit-grc\">Contact sales</a> to discuss on-premises licensing.</p>"),
        ("Is SafeMind available as SaaS?", "<p>Yes. SafeMind is a cloud-native SaaS platform running on AWS with a multi-tenant architecture. Pricing is per user per month on a 12-month commitment, starting at $3.40 for 25 to 50 users and decreasing with volume.</p>"),
        ("What is the SCADA Simulator?", "<p>The <a href=\"../products/scada-simulator/\">SCADA Simulator</a> is a tailor-made OT cyber range with authentic Siemens, ABB, Rockwell or Mitsubishi PLCs connected to Level 0 devices and a miniature replica of your plant. It's used for OT awareness training, testing system changes and rehearsing cyberattacks, with an optional attack-simulation add-on covering the full attack chain.</p>"),
        ("Are the OT attack scenarios free?", "<p>Yes, completely free. The <a href=\"../products/ot-attack-scenarios/\">OT Cyber Range</a> offers ten browser-based OT/ICS incident scenarios plus a certification exam. <a href=\"https://cyber.xploitacademy.com/\" target=\"_blank\" rel=\"noopener\">Start the free scenarios</a>.</p>"),
    ]),
]

import re as _re
def _fix(a):
    """Rewrite '../section/page/' links in FAQ answers to flat file names."""
    return _re.sub(r'href="\.\./([^"]*)"', lambda m: 'href="../' + pfile(m.group(1).replace("&amp;", "&")).replace("&", "&amp;") + '"', a)

def faq():
    d = 1
    path = "faq/"
    crumbs = [("FAQ", path)]
    nav = "".join(f'<a href="#{k}">{esc(t)}</a>' for t, ic, k, qs in FAQ)
    groups = ""
    for t, ic, k, qs in FAQ:
        items = "".join(f'<details class="faq"><summary>{esc(q)}</summary><div class="ans">{_fix(a)}</div></details>' for q, a in qs)
        groups += f'<div class="faq-group" id="{k}"><h2>{icon(ic)}{esc(t)}</h2>{items}</div>'
    body = f'''<section class="page-hero grid-bg"><div class="container">{breadcrumb(d, crumbs)}
<span class="eyebrow">Frequently asked questions</span><h1>Answers, before you ask.</h1>
<p class="lead">Everything you need to know about Xploit Security, our services and our products. Can't find what you're looking for? <a class="text-red" href="{url(d, "contact/")}">Contact us</a>.</p></div></section>
<section class="section"><div class="container faq-layout"><nav class="faq-nav" aria-label="FAQ sections">{nav}</nav><div>{groups}</div></div></section>''' + cta_band(d, "Still have questions?", "Our team is happy to help. Email us or message us on WhatsApp for a quick answer.", ("Contact us", "contact/"))
    import re
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a).replace("&amp;", "&")}} for t, ic, k, qs in FAQ for q, a in qs]}
    return path, page(d, path, "FAQ: Services, SafeMind, Xploit GRC & SCADA",
                      "Frequently asked questions about Xploit Security: industries and markets served, vCISO, ISO 27001, SOC 2 and CMMC consulting, IT and OT assessments, SafeMind, Xploit GRC, the Firewall Security Analyzer and the SCADA Simulator.",
                      body, "faq", ld, crumbs)

def contact():
    d = 1
    path = "contact/"
    crumbs = [("Contact", path)]
    opts_s = [(s, n) for s, n, _, _ in SERVICES]
    opts_p = [(s, n) for s, n, _, _, _ in PRODUCTS]
    opt = lambda items: "".join(f'<option data-key="{k}" value="{esc(n)}">{esc(n)}</option>' for k, n in items)
    countries = ["United Arab Emirates", "Saudi Arabia", "Qatar", "Kuwait", "Bahrain", "Oman", "Egypt", "Jordan", "Lebanon", "Iraq", "Morocco", "Türkiye",
                 "India", "Pakistan", "United Kingdom", "United States", "Canada", "Australia", "Germany", "France", "Netherlands", "Singapore", "Other"]
    copts = "".join(f"<option>{c}</option>" for c in COUNTRIES)
    body = f'''<section class="page-hero grid-bg"><div class="container">{breadcrumb(d, crumbs)}
<span class="eyebrow">Contact &amp; sales</span><h1>Let's talk security.</h1>
<p class="lead">Request an XFSA free trial, a SafeMind or Xploit GRC proof of concept, or a consultation with our team. Our team replies from <strong>{SITE["email"]}</strong>, usually within one business day.</p></div></section>

<section class="section"><div class="container"><div class="split contact-split">
<div class="form-card reveal">
<div class="tabs" role="tablist" aria-label="Inquiry type">
<button type="button" role="tab" data-inquiry="Free trial request" aria-selected="false">Free trial</button>
<button type="button" role="tab" data-inquiry="Proof of Concept (POC) request" aria-selected="false">POC</button>
<button type="button" role="tab" data-inquiry="Consultation request" aria-selected="false">Consultation</button>
<button type="button" role="tab" data-inquiry="Sales inquiry" aria-selected="true">Sales</button>
<button type="button" role="tab" data-inquiry="General inquiry" aria-selected="false">General</button>
</div>
<form id="contact-form" class="lead-form" data-endpoint="{SITE["form_endpoint"]}" data-success="Thank you, your inquiry has been sent." action="{SITE["form_endpoint"].replace("/ajax/", "/")}" method="POST" novalidate>
<input type="hidden" name="_subject" value="New Sales inquiry — xploit-security.com">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="Inquiry type" id="f-type" value="Sales inquiry">
<div class="hp" aria-hidden="true"><label for="f-hp">Leave this field empty</label><input type="text" name="_honey" id="f-hp" tabindex="-1" autocomplete="off"></div>
<div class="form-grid">
<div class="field"><label for="f-name">Full name <span class="req">*</span></label><input id="f-name" name="Name" type="text" autocomplete="name" required></div>
<div class="field"><label for="f-email">Business email <span class="req">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required placeholder="you@company.com"></div>
<div class="field"><label for="f-company">Company <span class="req">*</span></label><input id="f-company" name="Company" type="text" autocomplete="organization" required></div>
<div class="field"><label for="f-country">Country <span class="req">*</span></label><select id="f-country" name="Country" required><option value="">Select country</option>{copts}</select></div>
<div class="field full"><label for="f-interest">Service or product of interest <span class="req">*</span></label>
<select id="f-interest" name="Interest" required><option value="">Select one</option>
<optgroup label="Cybersecurity services">{opt(opts_s)}</optgroup>
<optgroup label="Cybersecurity products">{opt(opts_p)}</optgroup>
<option data-key="other" value="Other / not sure">Other / not sure</option></select></div>
<div class="field full"><label for="f-msg">Inquiry details <span class="req">*</span></label><textarea id="f-msg" name="Message" required placeholder="Tell us about your environment, goals, timelines or the demo you'd like."></textarea></div>
<div class="field full"><label class="consent"><input type="checkbox" name="Consent" value="Yes" required> <span>I agree that Xploit Security may use these details to respond to my inquiry.</span></label></div>
</div>
<div class="btn-row" style="margin-top:22px"><button class="btn btn-primary" type="submit">Send inquiry {icon("arrow")}</button></div>
<div id="form-status" class="form-status" role="status" aria-live="polite"></div>
</form>
</div>
<div class="grid reveal" style="gap:14px">
<a class="contact-tile" href="mailto:{SITE["email"]}"><span class="ico-box">{icon("mail")}</span><div><strong>Sales email</strong><span>{SITE["email"]}</span></div></a>
<a class="contact-tile" href="{SITE["wa"]}" target="_blank" rel="noopener"><span class="ico-box" style="background:rgba(37,211,102,.1);color:#25d366;border-color:rgba(37,211,102,.3)">{icon("message")}</span><div><strong>WhatsApp</strong><span>{SITE["wa_display"]}, chat with our team</span></div></a>
<a class="contact-tile" href="{url(d, "contact/?type=trial&interest=firewall-security-analyzer")}"><span class="ico-box">{icon("shield-check")}</span><div><strong>XFSA: Request a Free Trial</strong><span>Try the Firewall Security Analyzer, SaaS or desktop</span></div></a>
<a class="contact-tile" href="{url(d, "contact/?type=poc&interest=safemind")}"><span class="ico-box">{icon("graduation")}</span><div><strong>SafeMind: Request a POC</strong><span>Pilot awareness training and phishing simulations</span></div></a>
<a class="contact-tile" href="{url(d, "contact/?type=poc&interest=xploit-grc")}"><span class="ico-box">{icon("layers")}</span><div><strong>Xploit GRC: Request a POC</strong><span>Evaluate risk, compliance and evidence workflows</span></div></a>
<a class="contact-tile" href="{url(d, "contact/?type=consulting")}"><span class="ico-box">{icon("briefcase")}</span><div><strong>Request a Consultation</strong><span>vCISO, compliance, assessments, IT &amp; OT security</span></div></a>
<div class="contact-tile"><span class="ico-box">{icon("pin")}</span><div><strong>Headquarters</strong><span>Dubai, United Arab Emirates</span></div></div>
<a class="contact-tile" href="{SITE["academy"]}" target="_blank" rel="noopener"><span class="ico-box">{icon("graduation")}</span><div><strong>Looking for training?</strong><span>Training → Xploit Academy</span></div></a>
</div>
</div></div></section>
<script>
document.querySelectorAll('.contact-tile[href*="type="]').forEach(function(a){{a.addEventListener('click',function(e){{e.preventDefault();var u=new URL(a.href);var m={{trial:"Free trial request",poc:"Proof of Concept (POC) request",consulting:"Consultation request"}};var t=m[u.searchParams.get('type')];var b=document.querySelector('[data-inquiry="'+t+'"]');if(b)b.click();var k=u.searchParams.get('interest');var s=document.getElementById('f-interest');if(s){{if(k){{Array.prototype.forEach.call(s.options,function(o){{if(o.getAttribute('data-key')===k)s.value=o.value;}});}}else{{s.value='';}}s.dispatchEvent(new Event('change'));}}document.getElementById('contact-form').scrollIntoView({{behavior:'smooth',block:'start'}});document.getElementById('f-name').focus({{preventScroll:true}});}});}});
</script>'''
    ld = {"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact Xploit Security", "url": abs_url(path)}
    return path, page(d, path, "Contact Xploit Security: Sales, Demos & Consulting",
                      "Contact Xploit Security: request an XFSA free trial, a SafeMind or Xploit GRC proof of concept, or a cybersecurity consultation. Email hello@xploit-security.com or WhatsApp.",
                      body, "contact", ld, crumbs)

def notfound():
    body = f'''<section class="notfound grid-bg"><div class="container"><div class="code">404</div><h1 style="font-size:2rem">This page isn't on the network.</h1>
<p class="lead mx-auto">The page you requested doesn't exist or has moved. Try one of these instead.</p>
<div class="btn-row" style="justify-content:center;margin-top:24px"><a class="btn btn-primary" href="/">Go to homepage</a><a class="btn btn-ghost" href="/services/">Services</a><a class="btn btn-ghost" href="/products/">Products</a><a class="btn btn-ghost" href="/contact/">Contact</a></div></div></section>'''
    # 404 is served from any path by GitHub Pages, so it uses root-absolute links (custom domain at root).
    html_ = page(0, "404.html", "Page not found", "The page you requested could not be found. Explore Xploit Security IT and OT cybersecurity services and products.", body, robots="noindex,follow")
    # GitHub Pages serves 404.html for any missing path, so make its links root-absolute.
    html_ = _re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|/)([^"]*)"', r'\1="/\2"', html_)
    return "404.html", html_

ALL = [about, faq, contact]
