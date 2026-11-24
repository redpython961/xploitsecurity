"""XFSA product page: deployment options (SaaS / Desktop), screenshot showcase, free trial."""
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
        ("saas", "SaaS version", "cloud", app_shots("xfsa-saas"), ("saas", "SAAS"), ["wide", "", "half", "half"], ""),
        ("desktop", "Desktop version", "server", app_shots("xfsa-desktop"), ("desk", "DESKTOP"), ["wide", "", "half", "half"], "cyan"),
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
            f'<a class="btn btn-ghost" href="#deployment">SaaS or Desktop?</a>')
    side = f"""<h3>Sample assessment</h3>
<div class="kpi-row" style="margin-top:4px"><div><strong class="text-red">10.0</strong><span>risk score / 10</span></div><div><strong>48</strong><span>findings</span></div><div><strong class="text-red">9 / 8</strong><span>critical / high</span></div></div>
<div style="height:16px"></div>{chips(["NIST SP 800-53 Rev. 5", "PCI DSS 4.0.1", "Xploit Firewall Baseline", "Vendor hardening"], "red")}
<div style="height:10px"></div>{chips(["Available as SaaS", "Available as Desktop"], "cyan")}
<p class="note">Figures from a sample report on a FortiGate edge firewall.</p>"""
    hero = page_hero(d, crumbs, "Xploit Firewall Security Analyzer · XFSA", "Secure your network. Validate your defenses. Stay compliant.",
                     "Automated, evidence-based firewall configuration audits, available as a cloud SaaS or a locally installed desktop application. "
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
                     "Tell us a little about your environment and we'll set up your trial.", "Request a Free Trial",
                     "Thank you, your XFSA free trial request has been received.",
                     [("Preferred version", "version", ["SaaS (cloud)", "Desktop (local install)", "Not sure yet"]),
                      ("Number of firewalls", "fw", ["1–5", "6–20", "21–50", "51–200", "200+"]),
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

<section class="section section-alt" id="deployment"><div class="container">
{section_head("Deployment options", "Two ways to run XFSA. Same engine, same results.", "Choose the cloud for speed and simplicity, or install XFSA locally when your data must stay inside your environment.")}
<div class="deploy">
<div class="opt saas reveal"><span class="tag">Option A · Cloud-based</span><h3>XFSA SaaS</h3>
<p>Run assessments from any modern browser with nothing to install. We host, update and maintain the platform for you.</p>
{checks(["Accessible through a secure web browser", "No local installation required", "Centralized management and easy access for your team", "Regular updates and maintenance handled by Xploit", "Secure cloud-based data storage and processing"])}
<p class="best"><strong>Best for:</strong> teams that want to start quickly, collaborate across sites, and always run the latest rule library.</p></div>
<div class="opt desk reveal"><span class="tag">Option B · Locally installed</span><h3>XFSA Desktop</h3>
<p>An independent application installed and operated on your own infrastructure, so you keep control of the environment, security and data retention.</p>
{checks(["Installed and operated on your own infrastructure", "You control the environment, security and data retention", "Configurations and reports stay within your local environment, subject to your infrastructure and configuration", "Suited to strict security, privacy, regulatory or data-residency requirements", "An independent application, with no dependency on a shared cloud service"], "cyan")}
<p class="best"><strong>Best for:</strong> critical infrastructure, government, finance and OT environments where firewall configurations should not leave the premises.</p></div>
</div>
<div class="table-wrap reveal" style="margin-top:28px"><table class="data compare"><caption class="sr-only">XFSA SaaS and Desktop compared</caption>
<thead><tr><th scope="col">Consideration</th><th scope="col">SaaS</th><th scope="col">Desktop</th></tr></thead><tbody>
<tr><td>Installation</td><td>None, browser-based</td><td>Installed on your infrastructure</td></tr>
<tr><td>Where configurations and reports are kept</td><td>Secure cloud storage</td><td>Your local environment</td></tr>
<tr><td>Updates and maintenance</td><td>Handled by Xploit</td><td>Applied in your environment</td></tr>
<tr><td>Access for distributed teams</td><td class="yes">✓ Anywhere via browser</td><td>Within your environment</td></tr>
<tr><td>Control over data residency and retention</td><td>Hosted service</td><td class="yes">✓ Fully under your control</td></tr>
<tr><td>Strict security, regulatory or residency requirements</td><td class="part">Discuss with us</td><td class="yes">✓ Designed for it</td></tr>
<tr><td>Same rule library, scoring and reports</td><td class="yes">✓</td><td class="yes">✓</td></tr>
</tbody></table></div>
<p class="note">Not sure which fits? Request a free trial and tell us your requirements. We'll recommend the right option.</p>
</div></section>

<section class="section" id="screenshots"><div class="container">
{section_head("Product showcase", "See XFSA in action.", "Real screens from the application and real pages from an XFSA assessment report. Click any image to enlarge.")}
{gallery(d)}
</div></section>

<section class="section section-alt" id="free-trial"><div class="container"><div class="offer">
<div class="reveal"><span class="badge">{icon("zap")} Free trial</span>
<h2>Experience XFSA before you buy.</h2>
<p class="lead">Run XFSA against your own firewall configurations and see the findings, compliance scores and reports for yourself, then decide. No commitment.</p>
<ol class="steps-mini">
<li><span><strong>Request your trial</strong>Choose SaaS or Desktop and tell us about your firewalls.</span></li>
<li><span><strong>Get set up</strong>We provision your SaaS workspace or provide the desktop installer, with a guided walkthrough.</span></li>
<li><span><strong>Assess your firewalls</strong>Upload a configuration export and get an evidence-based report.</span></li>
<li><span><strong>Decide with confidence</strong>Review the results with our team and choose the edition that fits.</span></li>
</ol>
<div class="trust-row"><span>{icon("check")}No commitment</span><span>{icon("check")}SaaS or Desktop</span><span>{icon("check")}Guided onboarding</span></div>
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
<p>Try XFSA on your own configurations, as SaaS or Desktop, and see the results before making a purchasing decision.</p>
<div class="btn-row"><a class="btn btn-primary" href="#free-trial">Request a Free Trial {icon("arrow")}</a><a class="btn btn-ghost" href="{url(d, "contact/?type=trial&interest=firewall-security-analyzer")}">Contact sales</a><a class="btn btn-wa" href="{SITE["wa"]}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a></div>
</div></div></section>"""
    body += sticky_cta("XFSA: try it free on your own firewalls", "Request a Free Trial", "#free-trial")
    desc = ("Xploit Firewall Security Analyzer (XFSA): SaaS or desktop firewall configuration audits with CVE detection, "
            "risky-rule analysis and NIST/PCI DSS compliance scoring. Request a free trial.")
    return path, page(d, path, "Xploit Firewall Security Analyzer (XFSA)", desc, body, "sp",
                      prod_ld("Xploit Firewall Security Analyzer", desc, path, "SecurityApplication", None, "Web, Desktop"), crumbs,
                      keywords="firewall security analyzer, firewall configuration audit, firewall compliance, FortiGate audit, firewall rule review, PCI DSS firewall, NIST 800-53 firewall, free trial")


ALL = [xfsa]
