from lib import *
from hero_svg import HERO_SVG

CLIENTS = [("johnson-johnson", "Johnson & Johnson"), ("arabian-gulf-oil-company", "Arabian Gulf Oil Company"), ("yamama-cement", "Yamama Cement"),
           ("mbanq", "Mbanq"), ("snapdocs", "Snapdocs"), ("mint-mobile", "Mint Mobile"), ("mend-io", "Mend.io"), ("ordr", "Ordr"),
           ("paywise", "Paywise"), ("burjx", "BurjX"), ("keyo", "Keyo"), ("rep-ai", "Rep.ai"), ("sms-gateway", "SMS Gateway"),
           ("wariq", "Wariq"), ("admission-com-au", "Admission.com.au"), ("saryah", "Saryah"), ("attune", "Attune"), ("gourmeal", "Gourmeal"),
           ("medapharm", "Medapharm"), ("mediphar", "Mediphar"), ("premier-staffing-solution", "Premier Staffing Solution"), ("amazenet", "Amazenet")]

def clients_band(depth, title="Trusted across industries"):
    items = "".join(f'<li><img src="{url(depth, "assets/img/clients/"+f+".webp")}" alt="{esc(n)} logo" loading="lazy" decoding="async"></li>' for f, n in CLIENTS)
    return f'<section class="clients-band" aria-labelledby="clients-h"><div class="container"><h2 id="clients-h">{title}: some of our clients</h2><ul class="logo-wall">{items}</ul></div></section>'

INDUSTRIES = [("zap", "Energy & Power"), ("droplet", "Water & Wastewater"), ("flame", "Oil & Gas"), ("factory", "Manufacturing & Industrial"),
              ("landmark", "Financial Services & Fintech"), ("building", "Government & Public Sector"), ("wifi", "Telecom & Cloud Providers"),
              ("health", "Healthcare & Pharma"), ("cpu", "SaaS & Technology"), ("shield", "Defense Supply Chain")]

def home():
    d = 0
    r = lambda p: url(d, p)
    svc_cards = "".join(card(ic, esc(n), txt, r(f"services/{s}/")) for (s, n, _, ic), txt in zip(SERVICES, [
        "Independent advisory, security program design, data privacy and awareness, shaped around your risks and regulators.",
        "Senior, fractional security leadership that sets strategy, owns governance and reports to your board.",
        "Penetration testing of web, mobile and IoT, plus cloud security audits across AWS, Azure and GCP.",
        "ICS/SCADA security assessments, OT penetration testing and IEC 62443-aligned programs for industrial operators.",
        "Implementation and readiness for ISO 27001, SOC 2, CMMC, PCI DSS, GDPR and Gulf frameworks such as NCA ECC and NESA.",
        "Gap assessments, internal audits and security reviews that tell you exactly where you stand and what to fix first.",
    ]))
    prod = [
        ("safemind", "graduation", "SafeMind", "Security awareness SaaS: microlearning, unlimited phishing simulations, AI-driven learning paths and tips in Microsoft Teams and Slack.", "SaaS", "saas"),
        ("xploit-grc", "layers", "Xploit GRC", "Governance, risk and compliance in one platform: 38+ frameworks, risk registers, audits, evidence and IT/OT assets. SaaS or on-premises.", "SaaS · On-prem", "saas"),
        ("firewall-security-analyzer", "shield-check", "Xploit Firewall Security Analyzer", "Automated firewall configuration audits: CVE checks, risky-rule detection, compliance scoring against NIST, PCI DSS and vendor hardening, with evidence-backed remediation.", "Audit", "saas"),
        ("scada-simulator", "cpu", "SCADA Simulator", "A tailor-made OT cyber range with authentic PLCs and a miniature plant replica to train teams and test defenses safely.", "OT", "ot"),
        ("ot-attack-scenarios", "radar", "OT Cyber Attack Scenarios", "Ten free, browser-based OT/ICS incident scenarios with XP, levels and a final certification exam.", "Free", "free"),
    ]
    prod_cards = "".join(card(ic, n, t, r(f"products/{s}/"), cyan=True, tag=tag, tagcls=tc) for s, ic, n, t, tag, tc in prod)
    inds = "".join(f'<div class="industry reveal">{icon(ic)}{esc(n)}</div>' for ic, n in INDUSTRIES)

    body = f'''
<section class="hero grid-bg">
  <div class="container hero-grid">
    <div>
      <a class="hero-offer" href="{r("products/firewall-security-analyzer/")}#free-trial"><b>NEW</b> XFSA firewall analyzer: free trial available →</a><br>
      <span class="eyebrow">IT &amp; OT Cybersecurity · Consulting · SaaS</span>
      <h1><span class="line">Securing IT.</span><span class="line">Protecting OT.</span><span class="line grad-text">Enabling Trust.</span></h1>
      <p class="lead">From enterprise cybersecurity consulting and regulatory compliance to industrial OT security and intelligent SaaS platforms, Xploit Security helps organizations identify risks, strengthen defenses, and build cyber resilience.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="{r("services/")}">Explore Our Services {icon("arrow")}</a>
        <a class="btn btn-ghost" href="{r("products/")}">Discover Our Products</a>
      </div>
      <div class="hero-meta">
        <span>{icon("pin")}Headquartered in Dubai, UAE</span>
        <span>{icon("globe")}USA · UK · India presence</span>
        <span>{icon("layers")}IT + OT converged coverage</span>
      </div>
    </div>
    <div class="hero-visual reveal">{HERO_SVG}</div>
  </div>
</section>

<section class="section-sm section-alt">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Introducing Xploit Security</span>
        <h2>One security partner for the office and the plant floor.</h2>
      </div>
      <div class="reveal">
        <p>Xploit Security is the cybersecurity services and technology arm of the Xploit family. We protect critical infrastructure, enterprise applications and government organizations across the region and beyond, with practitioners who have run real IT and OT security programs.</p>
        <p>We combine hands-on consulting, from penetration testing to vCISO leadership, with software we build ourselves: SafeMind for awareness, Xploit GRC for governance, Xploit Firewall Security Analyzer for firewall audits, and the SCADA Simulator for industrial cyber training and testing.</p>
        <a class="link-arrow" href="{r("about/")}">About Xploit Security {icon("arrow")}</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("Cybersecurity services", "End-to-end coverage. One accountable team.", "Seven disciplines, from penetration testing to vCISO advisory, delivered from assessment to remediation to ongoing support across IT and OT.")}
    <div class="grid grid-3">{svc_cards}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    {section_head("Cybersecurity products", "Platforms built by practitioners.", "Commercial SaaS and industrial training platforms that turn security programs into everyday practice, plus a free OT range for everyone.", cyan=True)}
    <div class="grid grid-3">{prod_cards}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("IT &amp; OT expertise", "Converged coverage across information and operational technology.", "Attackers don't respect the boundary between your corporate network and your control systems. Neither do we.", center=True)}
    <div class="converge">
      <div class="pillar it reveal">
        <div class="ico-box">{icon("server")}</div>
        <h3>Enterprise IT</h3>
        <p>Protect users, data, applications and cloud workloads against today's threat landscape.</p>
        {checks(["Web, mobile, API and IoT penetration testing", "Cloud security audits on AWS, Azure and GCP", "ISO 27001, SOC 2, PCI DSS, CMMC and GDPR programs", "Security awareness and phishing simulation"])}
      </div>
      <div class="join" aria-hidden="true"><span>ONE PROGRAM</span></div>
      <div class="pillar ot reveal">
        <div class="ico-box cyan">{icon("factory")}</div>
        <h3>Industrial OT</h3>
        <p>Keep PLCs, SCADA and safety-critical processes running, and safe, under attack.</p>
        {checks(["ICS/SCADA security assessments and OT penetration testing", "IEC 62443 and NCA OTCC readiness", "Purdue-aligned segmentation and remote-access reviews", "Hands-on training on authentic PLCs with the SCADA Simulator"], "cyan")}
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    {section_head("Why choose Xploit Security", "Practitioners, not just advisors.")}
    <div class="grid grid-4">
      {card("award", "Industry expertise", "Backed by years of cybersecurity leadership experience across IT and OT environments.")}
      {card("scale", "Compliance and standards", "Experts in global frameworks and Gulf regulations, from ISO 27001 and SOC 2 to NCA ECC, SAMA and NESA.")}
      {card("layers", "Comprehensive solutions", "Covering infrastructure, applications, cloud and operations, with our own software to sustain results.")}
      {card("users", "Trusted partnerships", "A proven record with government, enterprise and critical industries.")}
    </div>
    <div class="grid grid-3" style="margin-top:22px">
      {card("search", "Expert teams", "Our penetration testing and GRC teams include professionals from AWS, Mandiant, Motorola and The World Bank.")}
      {card("compass", "Trusted advisors", "vCISO advisory that gives startups and enterprises strategic insight through complex challenges.")}
      {card("check", "Delivery excellence", "A structured planning and collaboration approach for timely, high-quality, tailored results.")}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head("Industries we support", "Built for regulated and critical sectors.", "We work wherever security failures carry real consequences: financial, operational and physical.")}
    <div class="ind-grid">{inds}</div>
  </div>
</section>

{clients_band(d)}

<section class="section">
  <div class="container">
    {section_head("Try before you buy", "Experience our platforms on your own environment.", "Every Xploit platform can be evaluated before you commit: a free trial of XFSA and a guided Proof of Concept for SafeMind and Xploit GRC.")}
    <div class="spot">
      <article class="item reveal"><div class="pic"><img src="{r("assets/img/products/xfsa-executive-summary.webp")}" alt="XFSA firewall assessment report executive summary" width="1000" height="1089" loading="lazy" decoding="async"></div>
        <div class="body"><span class="offer-tag">Free trial · SaaS or Desktop</span><h3>Xploit Firewall Security Analyzer</h3>
        <p>Evidence-based firewall configuration audits with CVE detection, risky-rule analysis and NIST / PCI DSS compliance scoring.</p>
        <div class="btn-row"><a class="btn btn-primary" href="{r("products/firewall-security-analyzer/")}#free-trial">Request a Free Trial</a><a class="btn btn-ghost" href="{r("products/firewall-security-analyzer/")}">Explore</a></div></div></article>
      <article class="item reveal"><div class="pic"><img src="{r("assets/img/products/safemind-learner-dashboard.webp")}" alt="SafeMind learner dashboard" width="770" height="852" loading="lazy" decoding="async"></div>
        <div class="body"><span class="offer-tag">Proof of Concept</span><h3>SafeMind</h3>
        <p>Security awareness SaaS with microlearning, unlimited phishing simulations and tips in Microsoft Teams and Slack.</p>
        <div class="btn-row"><a class="btn btn-primary" href="{r("products/safemind/")}#poc">Request a SafeMind POC</a><a class="btn btn-ghost" href="{r("products/safemind/")}">Explore</a></div></div></article>
      <article class="item reveal"><div class="pic"><img src="{r("assets/img/products/grc-dashboard.webp")}" alt="Xploit GRC CISO dashboard" width="1100" height="687" loading="lazy" decoding="async"></div>
        <div class="body"><span class="offer-tag">Proof of Concept · SaaS or on-premises</span><h3>Xploit GRC</h3>
        <p>Governance, risk and compliance in one platform: 38+ frameworks, risk registers, audits, evidence and IT/OT assets.</p>
        <div class="btn-row"><a class="btn btn-primary" href="{r("products/xploit-grc/")}#poc">Request a GRC POC</a><a class="btn btn-ghost" href="{r("products/xploit-grc/")}">Explore</a></div></div></article>
    </div>
    <div class="divider"></div>
    <div class="split">
      <div class="reveal">
        <span class="chip cyan">SCADA Simulator</span>
        <h3 style="font-size:1.8rem;margin-top:16px">Break a replica, not your plant.</h3>
        <p>A tailor-made simulation with authentic Siemens, ABB, Rockwell or Mitsubishi PLCs connected to a miniature replica of your plant, so teams can rehearse attacks and responses without touching production.</p>
        <div class="btn-row" style="margin-top:24px"><a class="btn btn-cyan" href="{r("products/scada-simulator/")}">Explore the SCADA Simulator {icon("arrow")}</a></div>
      </div>
      {shot(d, "scada-cabinet", "Line drawing of the SCADA Simulator cabinet holding a miniature model of an industrial site", "SCADA Simulator, miniature plant replica", frame=False, w=940, h=690)}
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow cyan">Free OT cybersecurity resource</span>
        <h2>Defend the plant. One decision at a time.</h2>
        <p class="lead">Ten immersive OT/ICS incident scenarios drawn from real attack patterns: USB drops, logic manipulation, default credentials, fake technicians and industrial ransomware. Make the calls, see the consequences, earn your certificate. Free, no sign-up required to start.</p>
        <div class="btn-row"><a class="btn btn-cyan" href="{SITE["range"]}" target="_blank" rel="noopener">Explore Free OT Attack Scenarios {icon("external")}</a><a class="btn btn-ghost" href="{r("products/ot-attack-scenarios/")}">What's inside</a></div>
      </div>
      <div class="grid grid-2 reveal">
        <div class="unit"><div class="meta"><span>UNIT-01 · REMOVABLE MEDIA</span><span>8 MIN</span></div><h3>The USB Stick in the Car Park</h3><p>One curious decision that can reach the PLC network.</p></div>
        <div class="unit"><div class="meta"><span>UNIT-06 · INCIDENT RESPONSE</span><span>10 MIN</span></div><h3>Ransomware at the Plant</h3><p>Thirty minutes decide whether production and safety survive.</p></div>
        <div class="unit"><div class="meta"><span>UNIT-07 · CONTROL INTEGRITY</span><span>9 MIN</span></div><h3>PLC Logic Manipulation</h3><p>The HMI shows normal. The logic no longer matches.</p></div>
        <div class="unit"><div class="meta"><span>FINAL EXAM</span><span>14 Q</span></div><h3>Certified Defender</h3><p>Pass 11 of 14 to earn your certificate.</p></div>
      </div>
    </div>
  </div>
</section>

{cta_band(d, "Let's strengthen your security posture.", "Tell us about your environment, IT, OT or both, and we'll recommend the right mix of services and platforms. Consultations are delivered on-site in Dubai or remotely worldwide.", ("Request a Consultation", "contact/?type=consulting"), ("Contact Xploit", "contact/?type=general"))}
'''
    ld = {"@context": "https://schema.org", "@type": "WebSite", "name": "Xploit Security", "url": SITE["domain"] + "/", "publisher": {"@id": SITE["domain"] + "/#org"}}
    return page(d, "", "Xploit Security | IT & OT Cybersecurity Consulting & SaaS",
                "Xploit Security delivers IT and OT cybersecurity consulting, vCISO, ISO 27001, SOC 2 and CMMC compliance, ICS/SCADA security, and SaaS platforms: SafeMind, Xploit GRC and the SCADA Simulator.",
                body, "home", ld, keywords="Cybersecurity Consulting, IT Cybersecurity Services, OT Cybersecurity, Industrial Cybersecurity, ICS Security, SCADA Security, vCISO Services, ISO 27001 Consulting, SOC 2 Compliance, CMMC Consulting, Cybersecurity GRC Software, Cybersecurity Awareness SaaS, SCADA Simulator")
