"""XFSA product page: desktop application, licensing & pricing, screenshot showcase, free trial."""
import os, json
from lib import *
from pages_products import prod_ld, other_products

_IMG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img", "products")


def app_shots(folder):
    """Real application screenshots dropped into assets/img/products/<folder>/ (WebP/PNG/JPG).
    Order and captions come from the file name (e.g. 01-main-dashboard.webp) or an optional captions.json
    mapping file name -> caption."""
    path = os.path.join(_IMG, folder)
    if not os.path.isdir(path):
        return []
    caps = {}
    cj = os.path.join(path, "captions.json")
    if os.path.exists(cj):
        caps = json.load(open(cj, encoding="utf-8"))
    out = []
    for f in sorted(os.listdir(path)):
        if not f.lower().endswith((".webp", ".png", ".jpg", ".jpeg")):
            continue
        stem = os.path.splitext(f)[0]
        cap = caps.get(f) or caps.get(stem) or " ".join(w for w in stem.split("-") if not w.isdigit()).strip().capitalize()
        try:
            from PIL import Image
            w, h = Image.open(os.path.join(path, f)).size
        except Exception:
            w, h = 1600, 1000
        out.append((folder + "/" + f, cap, w, h))
    return out


def _fig(d, rel_file, alt, cap, group, w, h, chip, cls):
    img = (f'<img src="{url(d, "assets/img/products/" + rel_file)}" alt="{esc(alt)}" width="{w}" height="{h}" '
           f'loading="lazy" decoding="async" data-zoom="{group}">')
    return (f'<figure class="reveal {cls}"><div class="shot-frame"><div class="bar"><i></i><i></i><i></i></div>{img}</div>'
            f'<figcaption><span class="ver-chip {chip[0]}">{chip[1]}</span>{esc(cap)}</figcaption></figure>')


REPORT_SHOTS = [
    ("xfsa-executive-summary.webp", "Executive summary: risk score, findings by severity and key weaknesses", 1000, 1089),
    ("xfsa-compliance-status.webp", "Compliance results per standard with failed controls", 1000, 806),
    ("xfsa-findings-table.webp", "Detailed findings with severity, score, mapped controls and CVE", 1000, 1273),
    ("xfsa-finding-detail.webp", "Finding detail: configuration evidence, risk, business impact and remediation", 1000, 962),
    ("xfsa-firewall-info.webp", "Firewall information, configuration hash and parser coverage", 1000, 1273),
    ("xfsa-report-cover.webp", "Report cover with overall risk score", 800, 1131),
]


def gallery(d):
    sets = [
        ("desktop", "Desktop application", "server", app_shots("xfsa-desktop"), ("desk", "DESKTOP"), ["wide", "", "half", "half"], "cyan"),
        ("reports", "Assessment reports", "file", REPORT_SHOTS, ("rep", "REPORT"), [""], ""),
    ]
    tabs, panels, first = [], [], True
    for key, label, ic, items, chip, layout, tcls in sets:
        if not items:
            continue
        figs = "".join(_fig(d, f, f"XFSA {chip[1].lower()} screenshot: {cap}", cap, "xfsa-" + key, w, h, chip, layout[k % len(layout)])
                       for k, (f, cap, w, h) in enumerate(items))
        tabs.append(f'<button type="button" role="tab" class="{tcls}" id="tab-{key}" aria-controls="gal-{key}" '
                    f'aria-selected="{"true" if first else "false"}">{icon(ic)}{label}</button>')
        panels.append(f'<div class="gallery" id="gal-{key}" role="tabpanel" aria-labelledby="tab-{key}"{"" if first else " hidden"}>{figs}</div>')
        first = False
    return (f'<div data-gallery-tabs><div class="gallery-tabs" role="tablist" aria-label="Screenshot sets">{"".join(tabs)}</div>'
            f'{"".join(panels)}</div>')


def xfsa():
    d = 2
    path = "products/firewall-security-analyzer/"
    crumbs = [("Products", "products/"), ("Xploit Firewall Security Analyzer", path)]
    btns = (f'<a class="btn btn-primary" href="#free-trial">Request a Free Trial {icon("arrow")}</a>'
            f'<a class="btn btn-ghost" href="#pricing">See licensing &amp; pricing</a>')
    side = f"""<h3>Sample assessment</h3>
<div class="kpi-row" style="margin-top:4px"><div><strong class="text-red">10.0</strong><span>risk score / 10</span></div><div><strong>48</strong><span>findings</span></div><div><strong class="text-red">9 / 8</strong><span>critical / high</span></div></div>
<div style="height:16px"></div>{chips(["NIST SP 800-53 Rev. 5", "PCI DSS 4.0.1", "Xploit Firewall Baseline", "Vendor hardening"], "red")}
<div style="height:10px"></div>{chips(["Desktop application", "Runs on your infrastructure", "Offline license activation"], "cyan")}
<p class="note">Figures from a sample report on a FortiGate edge firewall.</p>"""
    hero = page_hero(d, crumbs, "Xploit Firewall Security Analyzer · XFSA", "Secure your network. Validate your defenses. Stay compliant.",
                     "Automated, evidence-based firewall configuration audits in a desktop application that runs on your own infrastructure, so your configurations never leave your control. "
                     "XFSA finds vulnerable firmware, risky rules and hardening gaps, scores compliance, and tells you exactly how to fix each issue.",
                     btns, side)
    hero = hero.replace('<span class="eyebrow ">Xploit Firewall',
                        '<a class="hero-offer" href="#free-trial"><b>FREE TRIAL</b> Try XFSA before you buy →</a><br><span class="eyebrow ">Xploit Firewall', 1)

    domains = [("key", "Authentication &amp; administration", "Default and excess admin accounts, MFA, password and lockout policy, trusted hosts, banners, LDAP over TLS."),
               ("network", "Network security &amp; firewall policies", "Any-any rules, insecure services, untrusted inbound access, disabled or undocumented rules, unlogged denies."),
               ("lock", "VPN &amp; cryptography", "Weak IPsec ciphers, integrity algorithms and DH groups, IKEv1, legacy TLS on SSL VPN, VPN without MFA."),
               ("activity", "Monitoring &amp; logging", "Remote log forwarding, logging on rules, authenticated NTP, SNMP v1/v2c and default communities."),
               ("eye", "Security inspection", "IPS, anti-malware, web filtering, application control and DNS security on internet-bound and published traffic."),
               ("server", "Infrastructure &amp; resilience", "Exposed management planes, HA, routing protocol authentication and vendor-specific hardening settings."),
               ("bug", "Vulnerabilities", "Running firmware checked against known CVEs with affected ranges, CVSS scores and fixed releases."),
               ("scale", "Compliance mapping", "Every rule mapped to NIST SP 800-53, PCI DSS 4.0.1, the Xploit baseline and vendor hardening controls.")]
    dom_html = "".join(card(ic, t, x) for ic, t, x in domains)

    form = lead_form("xfsa-trial", "Free trial request", "Xploit Firewall Security Analyzer", "Request your free XFSA trial",
                     "14 days, up to 3 firewalls, full features. Tell us about your environment.", "Request a Free Trial",
                     "Thank you, your XFSA free trial request has been received.",
                     [("Number of firewalls", "fw", ["1–5", "6–20", "21–50", "51–200", "200+"]),
                      ("Firewall vendor(s)", "vendor", None)])

    body = hero + f"""
<section class="section"><div class="container">
{section_head("Why XFSA", "Firewalls drift. Attackers notice first.", "Rules pile up, temporary access becomes permanent, firmware falls behind and management interfaces end up on the internet. XFSA turns a configuration export into a clear, prioritized and defensible picture of your firewall's security posture.")}
<div class="grid grid-3">
{card("search", "Full-configuration coverage", "Every rule, object and system setting is evaluated, not a sample. Sections the parser can't read are reported as Not Assessed, never as compliant.")}
{card("bug", "Vulnerability &amp; misconfiguration detection", "Firmware is matched to vendor advisories with CVSS scores and fixed releases; risky rules and weak settings are flagged automatically.")}
{card("scale", "Compliance scoring", "Pass, fail, manual-review and N/A results per control, with compliance percentages for each selected standard.")}
{card("file", "Evidence for every finding", "Each finding quotes the exact configuration lines that triggered it, with the expected secure configuration.")}
{card("terminal", "Remediation you can apply", "Plain-language remediation plus vendor CLI snippets, technical risk and business impact (confidentiality, integrity, availability).")}
{card("shield-check", "Deterministic and repeatable", "Findings come from version-controlled rules, not AI guesses, so results are consistent, explainable and audit-friendly.")}
</div></div></section>

<section class="section section-alt" id="deployment"><div class="container"><div class="split">
<div class="reveal"><span class="eyebrow cyan">Desktop application</span><h2>Your firewall configurations never leave your control.</h2>
<p>XFSA is an independent desktop application, installed and operated on your own infrastructure. You keep control of the environment, the security and the retention of your data.</p>
{checks(["Installed and operated locally on your infrastructure", "Configurations and assessment reports stay in your local environment, subject to your infrastructure and configuration", "Offline license activation for isolated and restricted networks", "Suited to strict security, privacy, regulatory and data-residency requirements", "Regular rule-library and CVE updates with active maintenance"], "cyan")}</div>
<div class="grid grid-2">
{card("lock", "Data stays on-premises", "Firewall configurations hold your network's blueprint. With XFSA they are analyzed where they live.", cyan=True)}
{card("server", "Independent application", "No shared cloud platform to depend on, and no third-party hosting to assess.", cyan=True)}
{card("key", "Offline activation", "Activate licenses in isolated or restricted environments.", cyan=True)}
{card("factory", "Built for regulated sectors", "A good fit for critical infrastructure, government, finance and OT environments.", cyan=True)}
</div></div></div></section>

<section class="section" id="screenshots"><div class="container">
{section_head("Product showcase", "See XFSA in action.", "Real screens from the desktop application and real pages from an XFSA assessment report. Click any image to enlarge.")}
{gallery(d)}
</div></section>

<section class="section section-alt" id="pricing"><div class="container">
{section_head("Licensing &amp; pricing", "Simple per-firewall licensing.", "Annual subscription based on the number of firewalls you audit. Every tier includes the full product.")}
<div class="plans">
<div class="plan reveal"><h3>Starter</h3><span class="users">Up to 5 firewalls</span><div class="price">$1,500<small> / year</small></div><span class="aed">≈ $300 per firewall</span><p>For a first firewall audit program or a single site.</p><a class="btn btn-ghost" href="#free-trial">Start free trial</a></div>
<div class="plan popular reveal"><span class="pop">MOST POPULAR</span><h3>Professional</h3><span class="users">Up to 25 firewalls</span><div class="price">$4,900<small> / year</small></div><span class="aed">≈ $196 per firewall</span><p>For mid-size organizations with several sites.</p><a class="btn btn-primary" href="#free-trial">Start free trial</a></div>
<div class="plan reveal"><h3>Business</h3><span class="users">Up to 100 firewalls</span><div class="price">$12,900<small> / year</small></div><span class="aed">≈ $129 per firewall</span><p>For multi-site estates with IT and OT firewalls.</p><a class="btn btn-ghost" href="#free-trial">Start free trial</a></div>
<div class="plan reveal"><h3>Enterprise</h3><span class="users">Up to 500 firewalls</span><div class="price">$29,900<small> / year</small></div><span class="aed">≈ $60 per firewall · 500+: quote</span><p>For groups, utilities and critical infrastructure.</p><a class="btn btn-ghost" href="{url(d, "contact/?type=sales&interest=firewall-security-analyzer")}">Contact sales</a></div>
</div>
<div class="grid grid-3" style="margin-top:28px">
<div class="card reveal"><h3>Every tier includes</h3>{checks(["All standards: NIST SP 800-53, PCI DSS 4.0.1, Xploit baseline, vendor hardening", "Unlimited re-assessments of licensed firewalls", "PDF reports with evidence and remediation", "Rule-library and CVE updates", "Email support"])}</div>
<div class="card reveal"><h3>How firewalls are counted</h3>{checks(["One license per separately audited configuration", "Each virtual firewall (VDOM / vsys) counts as one", "An HA pair counts as one firewall", "License count resets every 12 months; retired devices free their slot", "Offline license activation available"])}</div>
<div class="card reveal"><h3>Perpetual option</h3><p>Prefer a one-off purchase? Buy a perpetual license at 2.5× the annual tier price, plus 20% per year maintenance.</p><p class="small" style="margin-top:12px">Maintenance includes rule-library and CVE updates and support. It's strongly recommended so vulnerability checks stay current.</p></div>
</div>
<div class="grid grid-3" style="margin-top:22px">
<div class="card reveal"><div class="ico">{icon("briefcase")}</div><h3>Consultants &amp; auditors</h3><p>Assessment packs usable across any client, valid for 12 months:</p>{checks(["10 assessments: $990", "50 assessments: $3,900"])}</div>
<div class="card reveal"><div class="ico">{icon("users")}</div><h3>MSSPs &amp; resellers</h3><p>Monthly per-client-firewall licensing from $8–12 per firewall per month depending on volume, with partner-branded reports. Reseller margins of 20–30%.</p></div>
<div class="card reveal"><div class="ico">{icon("clipboard")}</div><h3>Assessment as a service</h3><p>Prefer us to run it? Our team performs the XFSA assessment and delivers the report, from $250 per firewall.</p></div>
</div>
<div class="card reveal" style="margin-top:22px"><h3>Add-ons &amp; bundles</h3>
<div class="grid grid-3" style="margin-top:6px">
<div>{checks(["Premium support: +15%"])}</div>
<div>{checks(["Onboarding and custom rule packs: on request"])}</div>
<div>{checks(["XFSA + <a class=\"text-red\" href=\"" + url(d, "products/xploit-grc/") + "\">Xploit GRC</a> bundle: 15% off"])}</div>
</div></div>
<p class="note">Prices in USD, billed annually, excluding VAT. Free trial: 14 days, up to 3 firewalls, full features (reports watermarked "TRIAL"), converting to Starter or Professional.</p>
</div></section>

<section class="section" id="free-trial"><div class="container"><div class="offer">
<div class="reveal"><span class="badge">{icon("zap")} Free trial</span>
<h2>Experience XFSA before you buy.</h2>
<p class="lead">Run XFSA against your own firewall configurations and see the findings, compliance scores and reports for yourself, then decide. No commitment.</p>
<ol class="steps-mini">
<li><span><strong>Request your trial</strong>Tell us about your firewalls and environment.</span></li>
<li><span><strong>Get set up</strong>We send the desktop installer and a 14-day trial license, with a guided walkthrough.</span></li>
<li><span><strong>Assess your firewalls</strong>Upload a configuration export and get an evidence-based report.</span></li>
<li><span><strong>Decide with confidence</strong>Review the results with our team and choose the license tier that fits.</span></li>
</ol>
<div class="trust-row"><span>{icon("check")}No commitment</span><span>{icon("check")}14 days · up to 3 firewalls</span><span>{icon("check")}Guided onboarding</span></div>
</div>
{form}
</div></div></section>

<section class="section"><div class="container">
{section_head("What it checks", "Eight security domains, one rule library.", "The Xploit Firewall Security Baseline groups checks into the domains attackers and auditors care about.")}
<div class="grid grid-4">{dom_html}</div>
</div></section>

<section class="section section-alt"><div class="container"><div class="split">
<div class="reveal"><span class="eyebrow">Reporting</span><h2>Risk your leadership understands in one page.</h2>
<p>Every report opens with an overall risk score, a security score, compliance percentage, findings by severity and domain, the key weaknesses and prioritized recommendations, ready for a CISO, auditor or board pack.</p>
{checks(["Risk score from 0 to 10 and security score out of 100", "Findings by severity: Critical, High, Medium, Low, Informational", "Top weaknesses with individual risk scores", "Priority recommendations in order of impact", "Detailed findings with evidence, CLI remediation, CVE and mapped controls"])}
<div class="btn-row" style="margin-top:24px"><a class="btn btn-primary" href="#free-trial">Request a Free Trial</a></div></div>
{zshot(d, "xfsa-executive-summary", "XFSA report executive summary showing risk score, findings by severity and key security weaknesses", "Executive summary (sample report)", "xfsa-feature", 1000, 1089, ("rep", "REPORT"), frame=False)}
</div></div></section>

<section class="section"><div class="container">
{section_head("How it works", "From configuration file to board-ready report.")}
<div class="steps">
<div class="step reveal"><span class="num">01</span><h3>Export</h3><p>Export the firewall configuration and register the device, its criticality and environment.</p></div>
<div class="step reveal"><span class="num">02</span><h3>Parse</h3><p>XFSA parses the configuration, records its SHA-256 hash and shows which sections it could read.</p></div>
<div class="step reveal"><span class="num">03</span><h3>Assess</h3><p>Version-controlled rules evaluate the configuration against the standards you select.</p></div>
<div class="step reveal"><span class="num">04</span><h3>Report &amp; fix</h3><p>Download the report, remediate with the provided steps and re-assess to confirm the fixes.</p></div>
</div></div></section>

<section class="section section-alt"><div class="container"><div class="split">
<div class="reveal"><span class="eyebrow">Methodology</span><h2>Transparent scoring you can defend.</h2>
<p>Risk scores combine each rule's base severity with exposure (reachability from untrusted zones), device criticality and environment. CVSS is used as a floor for known vulnerabilities.</p>
<div class="table-wrap" style="margin-top:20px"><table class="data"><caption class="sr-only">XFSA severity bands</caption><thead><tr><th scope="col">Severity</th><th scope="col">Risk score</th></tr></thead><tbody>
<tr><td>Critical</td><td>≥ 9.0</td></tr><tr><td>High</td><td>≥ 7.0</td></tr><tr><td>Medium</td><td>≥ 4.0</td></tr><tr><td>Low</td><td>&gt; 0</td></tr></tbody></table></div></div>
<div class="reveal"><div class="grid" style="gap:14px">
{card("check", "No AI-generated findings", "No AI service generates findings or evidence. Every result traces back to a specific rule and configuration line.")}
{card("eye", "Honest coverage", "Controls that can't be determined from configuration are marked Manual Review; missing sections are Not Assessed.")}
{card("fingerprint", "Traceable input", "The analyzed file is identified by its SHA-256 hash, so every report is tied to an exact configuration.")}
</div></div>
</div></div></section>

<section class="section"><div class="container">
{section_head("Who it's for", "Built for teams that own or audit firewalls.")}
<div class="grid grid-4">
{card("shield", "Security teams", "Continuously validate perimeter and internal firewalls against your baseline.")}
{card("clipboard", "Auditors &amp; GRC", "Evidence-backed results for PCI DSS, NIST and internal audits.")}
{card("briefcase", "Consultants &amp; MSSPs", "Deliver consistent, branded firewall assessments across clients.")}
{card("factory", "Utilities &amp; industry", "Verify the firewalls that separate corporate IT from OT networks.")}
</div>
<p class="note">Vendor support: Fortinet FortiGate configurations are fully supported today. Contact us about other firewall platforms. Prefer a done-for-you review? Our <a class="text-red" href="{url(d, "services/security-assessments-audits/")}">security assessments</a> team can run XFSA for you.</p>
</div></section>
"""
    body += other_products(d, "firewall-security-analyzer")
    body += f"""<section class="section"><div class="container"><div class="cta-band reveal">
<span class="eyebrow">Free trial</span><h2>Find the gaps in your firewall before attackers do.</h2>
<p>Install XFSA, audit up to three of your own firewalls free for 14 days, and see the results before making a purchasing decision.</p>
<div class="btn-row"><a class="btn btn-primary" href="#free-trial">Request a Free Trial {icon("arrow")}</a><a class="btn btn-ghost" href="{url(d, "contact/?type=trial&interest=firewall-security-analyzer")}">Contact sales</a><a class="btn btn-wa" href="{SITE["wa"]}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a></div>
</div></div></section>"""
    body += sticky_cta("XFSA: try it free on your own firewalls", "Request a Free Trial", "#free-trial")
    desc = ("Xploit Firewall Security Analyzer (XFSA): desktop firewall configuration audits with CVE detection, "
            "risky-rule analysis and NIST/PCI DSS compliance scoring. Per-firewall licensing. Free trial.")
    return path, page(d, path, "Xploit Firewall Security Analyzer (XFSA)", desc, body, "sp",
                      prod_ld("Xploit Firewall Security Analyzer", desc, path, "SecurityApplication", {"@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "1500", "highPrice": "29900", "description": "Annual subscription per firewall tier"}, "Desktop"), crumbs,
                      keywords="firewall security analyzer, firewall configuration audit, firewall compliance, FortiGate audit, firewall rule review, PCI DSS firewall, NIST 800-53 firewall, free trial")


ALL = [xfsa]
