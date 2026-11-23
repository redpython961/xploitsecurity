from lib import *

def service_ld(name, desc, path, types):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc, "serviceType": types,
            "provider": {"@id": SITE["domain"] + "/#org"}, "areaServed": ["AE", "SA", "Worldwide"], "url": SITE["domain"] + "/" + path}

def related(d, exclude):
    items = [(s, n, ds, ic) for s, n, ds, ic in SERVICES if s != exclude][:3]
    cards = "".join(card(ic, esc(n), esc(ds), url(d, f"services/{s}/")) for s, n, ds, ic in items)
    return f'<section class="section section-alt"><div class="container">{section_head("Related services", "Explore more ways we help.")}<div class="grid grid-3">{cards}</div></div></section>'

def svc_page(slug, name, title, desc, kw, eyebrow, h1, lead, side, body_html, ot=False):
    d = 2
    path = f"services/{slug}/"
    crumbs = [("Services", "services/"), (name, path)]
    btns = f'<a class="btn btn-primary" href="{url(d, "contact/?type=consulting&interest="+slug)}">Request a consultation {icon("arrow")}</a><a class="btn btn-ghost" href="{SITE["wa"]}" target="_blank" rel="noopener">Talk on WhatsApp</a>'
    hero = page_hero(d, crumbs, eyebrow, h1, lead, btns, side, ot=ot, eyebrow_cyan=ot)
    body = hero + body_html + related(d, slug) + cta_band(d, f"Ready to discuss {name.lower()}?", "Share your scope and objectives. We'll come back with a tailored approach, timeline and proposal.", ("Request a consultation", "contact/?type=consulting&interest=" + slug))
    return path, page(d, path, title, desc, body, "sp", service_ld(name, desc, path, name), crumbs, keywords=kw)

# ---------------------------------------------------------------------------
def consulting():
    d = 2
    side = f'<h3>Engagement areas</h3>{checks(["Security strategy and roadmaps", "Security program design", "Policies, procedures and governance", "Data privacy and protection", "Cloud architecture reviews", "Awareness and training programs"])}'
    b = f'''
<section class="section"><div class="container">
{section_head("Cybersecurity consulting &amp; advisory", "Clear advice, grounded in how attacks really happen.", "Whether you're building a security function from scratch or maturing an established one, we help you decide what matters most, and then help you do it.")}
<div class="grid grid-3">
{card("compass", "Strategy &amp; roadmaps", "Current-state assessment, target operating model and a prioritized roadmap tied to business risk, regulation and budget.")}
{card("file", "Policies &amp; governance", "Security policies, procedures and standards written for your organization, with ownership, approval and review cycles that work in practice.")}
{card("lock", "Data privacy &amp; protection", "GDPR, UAE PDPL, Saudi PDPL and DIFC data-protection programs: records of processing, DPIAs, data subject requests and breach handling.")}
{card("cloud", "Cloud architecture reviews", "Design reviews for AWS, Azure and Google Cloud to build secure foundations and catch risky patterns before they reach production.")}
{card("graduation", "Awareness &amp; training", "Role-based awareness programs for staff, executives and OT operators, delivered live or continuously through SafeMind.", url(d, "products/safemind/"), link="See SafeMind")}
{card("activity", "Risk management", "Cybersecurity risk assessments with defensible likelihood × impact scoring, treatment plans and registers your leadership can act on.")}
</div></div></section>

<section class="section section-alt"><div class="container"><div class="split">
<div class="reveal"><span class="eyebrow">How we work</span><h2>Structured delivery, tailored outcomes.</h2>
<p>Every engagement follows a planned, collaborative approach so you always know what's happening, what's next and what you'll get.</p></div>
<div class="steps two">
<div class="step reveal"><span class="num">01 · DISCOVER</span><h3>Understand</h3><p>Stakeholder interviews, document review and scoping against your business and regulatory context.</p></div>
<div class="step reveal"><span class="num">02 · ASSESS</span><h3>Measure</h3><p>Evaluate controls, risks and gaps across people, process and technology, in IT and OT.</p></div>
<div class="step reveal"><span class="num">03 · PLAN</span><h3>Prioritize</h3><p>A practical roadmap with quick wins, owners and realistic timelines.</p></div>
<div class="step reveal"><span class="num">04 · ENABLE</span><h3>Deliver</h3><p>Hands-on implementation support, reporting and handover, or ongoing advisory.</p></div>
</div></div></div></section>'''
    return svc_page("cybersecurity-consulting", "Cybersecurity Consulting", "Cybersecurity Consulting & Advisory Services",
        "Cybersecurity consulting and advisory from Xploit Security: security strategy, policies and governance, data privacy (GDPR, UAE and Saudi PDPL), cloud architecture reviews, risk management and awareness.",
        "Cybersecurity Consulting, cybersecurity advisory, security strategy, security policies, GDPR consulting, PDPL, data privacy, risk management, Dubai",
        "Cybersecurity consulting", "Cybersecurity consulting that turns risk into a plan.",
        "Independent, practitioner-led advice for enterprises, critical infrastructure and government organizations: from security strategy and governance to data privacy and awareness.", side, b)

def vciso():
    d = 2
    side = f'<h3>What you get</h3>{checks(["Named, senior security leader", "Security strategy and roadmap", "Board and executive reporting", "Audit and customer assurance support", "Flexible monthly engagement"])}'
    b = f'''
<section class="section"><div class="container"><div class="split">
<div class="reveal"><span class="eyebrow">Virtual CISO</span><h2>Executive security leadership, without the full-time overhead.</h2>
<p>Our vCISO advisory services offer strategic insight to help startups and enterprises navigate complex challenges. You get an experienced security leader embedded in your team, setting direction, making decisions and representing security to leadership, customers and auditors.</p>
<p>It's ideal when you need to answer customer security questionnaires, prepare for SOC 2, ISO 27001 or CMMC, respond to a regulator, or mature a security function ahead of a full-time hire.</p></div>
<div class="grid grid-2">
{card("compass", "Strategy", "Security vision, priorities and a roadmap aligned to business goals.")}
{card("landmark", "Governance", "Policies, committees, risk appetite and accountability.")}
{card("chart", "Reporting", "Clear metrics and board-ready briefings on posture and risk.")}
{card("shield-check", "Assurance", "Audits, certifications and customer due diligence handled.")}
</div></div></div></section>

<section class="section section-alt"><div class="container">
{section_head("Typical vCISO responsibilities", "Everything a CISO owns, delivered on your terms.")}
<div class="grid grid-2">
<div class="card reveal"><h3>Program leadership</h3>{checks(["Security strategy, roadmap and budget planning", "Information security policies and standards", "Risk register ownership and treatment decisions", "Security committee setup and facilitation", "Vendor and third-party risk oversight"])}</div>
<div class="card reveal"><h3>Compliance &amp; assurance</h3>{checks(["ISO 27001, SOC 2 and CMMC program ownership", "Audit preparation and auditor liaison", "Customer security questionnaires and trust reviews", "Incident response planning and tabletop exercises", "Regulatory alignment: NCA ECC, NESA, SAMA, CBUAE, ADGM, DIFC"])}</div>
</div>
<p class="note">Pair your vCISO with Xploit GRC to run the program from one dashboard. Consultants and vCISOs can manage every client in an isolated workspace.</p>
</div></section>

<section class="section"><div class="container">
{section_head("Who it's for", "Built for organizations at an inflection point.")}
<div class="grid grid-3">
{card("zap", "Scale-ups &amp; SaaS", "Win enterprise deals with a credible security program and SOC 2 or ISO 27001 assurance.")}
{card("factory", "Industrial operators", "Bring IT and OT security under one governance model, aligned with IEC 62443 and NCA OTCC.")}
{card("shield", "Defense suppliers", "Lead CMMC Level 1 and Level 2 readiness and protect controlled unclassified information.")}
</div></div></section>'''
    return svc_page("vciso", "vCISO Services", "Virtual CISO (vCISO) Services",
        "Virtual CISO services from Xploit Security: fractional security leadership, strategy, governance, board reporting and compliance ownership for ISO 27001, SOC 2, CMMC and Gulf regulations.",
        "vCISO Services, virtual CISO, fractional CISO, security leadership, CISO as a service, Dubai, UAE",
        "vCISO services", "A seasoned CISO on your team, on demand.",
        "Fractional, senior security leadership for startups, scale-ups and enterprises that need a credible security program now, without waiting for a full-time hire.", side, b)

def it_sec():
    d = 2
    side = f'<h3>Coverage</h3>{chips(["Web", "Mobile", "IoT", "API", "AWS", "Azure", "GCP"], "red")}<div style="height:16px"></div><h3>Standards supported</h3>{chips(["ISO 27001", "NIST", "PCI DSS", "NCA"])}'
    b = f'''
<section class="section"><div class="container"><div class="split">
<div class="reveal"><span class="eyebrow">Penetration testing</span><h2>Real-world attack simulation that finds what scanners miss.</h2>
<p>Comprehensive testing across web, mobile and IoT systems, finding and fixing security gaps through real-world attack simulation. Every finding comes with business impact, evidence and clear remediation guidance, followed by retesting.</p>
{checks(["Real-world attack simulations that identify and remediate security gaps", "Serving finance, energy, telecom, cloud providers and manufacturing", "Supporting compliance initiatives across major regulatory standards", "Executive summary plus detailed technical report and retest"])}</div>
<div class="grid grid-2">
{card("terminal", "Web applications", "Authentication, authorization, injection, business logic and session flaws.")}
{card("fingerprint", "Mobile apps", "Android and iOS apps, their storage, transport and back-end APIs.")}
{card("wifi", "IoT &amp; devices", "Embedded devices, firmware and the networks they connect to.")}
{card("network", "Networks &amp; APIs", "External and internal infrastructure, services and exposed APIs.")}
</div></div></div></section>

<section class="section section-alt"><div class="container"><div class="split reverse">
<div class="reveal"><span class="eyebrow">Cloud security audits</span><h2>Find the misconfigurations that weaken your cloud.</h2>
<p>Assessments and audits across the major cloud platforms, identifying the misconfigurations and risks that weaken your environment, and architecture reviews that help you build securely from the start.</p>
{checks(["Identify misconfigurations and security risks across cloud environments", "Strengthen compliance and data protection posture in the cloud", "Identity, network, logging, encryption and workload reviews", "Support for organizations of every size securing cloud infrastructure"])}</div>
<div class="grid grid-3 reveal" style="grid-template-columns:1fr">
<div class="industry">{icon("cloud")}Amazon Web Services</div>
<div class="industry">{icon("cloud")}Microsoft Azure</div>
<div class="industry">{icon("cloud")}Google Cloud Platform</div>
</div></div></div></section>

<section class="section"><div class="container">
{section_head("Vulnerability management", "From one-off findings to a repeatable process.", "We help you build a vulnerability management practice that discovers, prioritizes and closes weaknesses continuously, with findings tracked to closure in Xploit GRC if you choose.")}
<div class="steps">
<div class="step reveal"><span class="num">01</span><h3>Discover</h3><p>Asset coverage and authenticated scanning across infrastructure and applications.</p></div>
<div class="step reveal"><span class="num">02</span><h3>Prioritize</h3><p>Risk-based triage using exploitability, exposure and business criticality.</p></div>
<div class="step reveal"><span class="num">03</span><h3>Remediate</h3><p>Owners, deadlines and practical fix guidance for every finding.</p></div>
<div class="step reveal"><span class="num">04</span><h3>Verify</h3><p>Retesting and metrics that show risk going down over time.</p></div>
</div></div></section>'''
    return svc_page("it-cybersecurity", "IT Cybersecurity", "IT Cybersecurity: Pen Testing & Cloud Security",
        "IT cybersecurity services from Xploit Security: penetration testing for web, mobile, IoT and APIs, cloud security audits for AWS, Azure and GCP, and vulnerability management.",
        "IT Cybersecurity Services, penetration testing, pen testing Dubai, cloud security audit, AWS security, Azure security, vulnerability management",
        "IT cybersecurity", "Test, harden and prove your enterprise defenses.",
        "Penetration testing, cloud security audits and vulnerability management for the applications, infrastructure and cloud platforms your business runs on.", side, b)

def ot_sec():
    d = 2
    side = f'<h3>Frameworks</h3>{chips(["IEC 62443", "NCA OTCC", "NIST SP 800-82", "NERC CIP", "Aramco SACS-002"], "cyan")}<div style="height:16px"></div><h3>Environments</h3>{chips(["Power", "Water", "Oil & Gas", "Manufacturing", "Metro & smart city"])}'
    b = f'''
<section class="section"><div class="container">
{section_head("OT &amp; industrial cybersecurity", "Security that respects safety and uptime.", "Industrial environments can't be tested like an office network. Our OT work is planned around safety, availability and engineering reality, from passive assessments to controlled testing on replicas.", cyan=True)}
<div class="grid grid-3">
{card("search", "IT and OT/ICS security assessments", "Architecture, asset and configuration reviews across Purdue levels: PLCs, HMIs, historians, engineering workstations and remote access.", cyan=True)}
{card("target", "OT penetration testing", "Controlled, safety-first testing of OT networks and systems, including industrial protocols, segmentation and IT-to-OT pathways.", cyan=True)}
{card("layers", "IEC 62443 &amp; NCA OTCC readiness", "Zone and conduit models, security levels and gap assessments with a remediation roadmap per site.", cyan=True)}
{card("network", "Segmentation &amp; remote access", "Review of DMZs, firewalls and vendor remote-access paths, the routes most real OT incidents start from.", cyan=True)}
{card("cpu", "Training on authentic PLCs", "Hands-on exercises and attack rehearsals on the SCADA Simulator: a replica of your plant, not your plant.", url(d, "products/scada-simulator/"), cyan=True, link="See the SCADA Simulator")}
{card("graduation", "OT awareness", "Role-based awareness for operators, engineers and management, plus our free OT attack scenarios.", url(d, "products/ot-attack-scenarios/"), cyan=True, link="Try the free scenarios")}
</div></div></section>

<section class="section section-alt"><div class="container"><div class="split">
<div class="reveal"><span class="eyebrow cyan">Example engagement</span><h2>NCA OTCC readiness across desalination and power plants.</h2>
<p>An illustrative program for a water and power utility, delivered with Xploit GRC as the single register for every site:</p>
{checks(["Inventory PLCs, SCADA and HMIs per plant", "Run OT security checklists at each site", "Track NCA OTCC and IEC 62443 gaps in one view", "Report plant-by-plant readiness to the board"], "cyan")}
<p class="note">Illustrative scenario showing how our services and platform fit an OT program.</p></div>
{shot(d, "grc-asset-inventory", "Xploit GRC IT and OT asset inventory with criticality and owners", "Xploit GRC, IT & OT asset inventory", w=860, h=537)}
</div></div></section>

<section class="section"><div class="container">
{section_head("Threats we help you prepare for", "Real attack patterns, real consequences.", cyan=True)}
<div class="grid grid-4">
{card("alert", "Industrial ransomware", "Containment and recovery planning that keeps safety first.", cyan=True)}
{card("cpu", "PLC logic manipulation", "Integrity checks against golden masters and change control.", cyan=True)}
{card("key", "Default credentials", "Hardening of new RTUs, PLCs and HMIs before go-live.", cyan=True)}
{card("users", "Compromised vendor access", "Monitored, time-bound and approved remote sessions.", cyan=True)}
</div></div></section>'''
    return svc_page("ot-industrial-cybersecurity", "OT & Industrial Cybersecurity", "OT & Industrial Cybersecurity: ICS/SCADA",
        "OT and industrial cybersecurity from Xploit Security: ICS/SCADA security assessments, OT penetration testing, IEC 62443 and NCA OTCC readiness, segmentation and remote-access reviews for utilities and industry.",
        "OT Cybersecurity, Industrial Cybersecurity, ICS Security, SCADA Security, IEC 62443, NCA OTCC, OT penetration testing, utilities cybersecurity",
        "OT &amp; industrial cybersecurity", "Protect the processes that keep the lights on.",
        "ICS and SCADA security for power, water, oil and gas, manufacturing and smart-city operators, aligned with IEC 62443 and NCA OTCC and built around safety and uptime.", side, b, ot=True)

def compliance():
    d = 2
    world = [("ISO 27001", "Information security management"), ("PCI DSS", "Payment card data security"), ("NIST", "Risk management framework"),
             ("GDPR", "Data privacy and protection"), ("SOC 2", "Type 1 and Type 2 attestation"), ("CMMC", "Level 1 and Level 2 maturity")]
    ksa = [("NCA ECC", "Assess and implement core cybersecurity controls for governance, defense and resilience"), ("NCA CCC", "Ensure cloud environments meet national security and data protection standards"),
           ("SAMA Framework", "Guide financial institutions on cyber risk management and incident response"), ("Aramco SACS-002", "Support vendors and contractors in meeting Aramco's cybersecurity requirements")]
    uae = [("UAE NESA", "Assess and implement core cybersecurity measures for government and critical sectors"), ("CBUAE Framework", "Guide financial institutions on cyber risk, data protection and incident response"),
           ("ADGM Regulations", "Support financial and fintech entities in meeting Abu Dhabi Global Market requirements"), ("DIFC Standards", "Help DIFC companies comply with data privacy, security and governance obligations")]
    fw = lambda items: "".join(f'<div class="fw-item"><strong>{esc(a)}</strong><span>{esc(b)}</span></div>' for a, b in items)
    side = f'<h3>Frameworks we deliver</h3>{chips(["ISO 27001", "SOC 2", "CMMC L1/L2", "PCI DSS", "NIST", "GDPR", "NCA ECC", "NCA CCC", "SAMA", "SACS-002", "NESA", "CBUAE", "ADGM", "DIFC"], "red")}'
    b = f'''
<section class="section"><div class="container">
{section_head("Compliance, wherever you operate", "Implement controls. Close gaps. Achieve certification.", "We help organizations meet international standards and Gulf regulations with programs that hold up to auditors and actually reduce risk.")}
<div class="grid grid-3">
<div class="fw-group reveal"><h3>Worldwide <small>{len(world)} frameworks</small></h3>{fw(world)}</div>
<div class="fw-group reveal"><h3>Saudi Arabia <small>Vision 2030 aligned</small></h3><p class="small">Aligned with Saudi Vision 2030, national cybersecurity frameworks and regulatory bodies.</p>{fw(ksa)}</div>
<div class="fw-group reveal"><h3>United Arab Emirates <small>Home market</small></h3><p class="small">Rooted in our home market, with deep familiarity across government, finance and free-zone entities.</p>{fw(uae)}</div>
</div></div></section>

<section class="section section-alt"><div class="container">
{section_head("Programs in focus", "Our most requested compliance engagements.")}
<div class="grid grid-3">
<div class="card reveal"><div class="ico">{icon("award")}</div><h3>ISO 27001 implementation</h3><p>End-to-end ISMS implementation and certification readiness: scope, risk assessment, Statement of Applicability, policies, internal audit and management review.</p>{checks(["ISO/IEC 27001:2022 aligned", "Internal audits by certified lead auditors", "Certification audit support"])}</div>
<div class="card reveal"><div class="ico">{icon("shield-check")}</div><h3>SOC 2 readiness</h3><p>Readiness assessment, control design and evidence preparation for SOC 2 Type 1 and Type 2 attestation, including year-over-year renewals.</p>{checks(["Trust Services Criteria mapping", "Policy and control implementation", "Auditor coordination"])}</div>
<div class="card reveal"><div class="ico">{icon("shield")}</div><h3>CMMC Level 1 &amp; 2</h3><p>Scoping of FCI and CUI environments, NIST SP 800-171 assessment, POA&amp;M and SSP preparation for defense-industrial-base suppliers.</p>{checks(["110 NIST SP 800-171 requirements", "SSP and POA&M development", "Readiness reporting"])}</div>
</div></div></section>

<section class="section"><div class="container"><div class="split">
<div class="reveal"><span class="eyebrow">Risk management</span><h2>Risk you can explain to the board.</h2>
<p>Compliance is the floor, not the ceiling. We build cybersecurity risk management that identifies, scores and treats risk transparently, with likelihood × impact scoring, defined appetite, accountable owners and tracked treatment plans.</p>
{checks(["Risk methodology (3×3, 4×4 or 5×5) and appetite statement", "Asset-based IT and OT risk assessments", "Treatment plans, risk acceptance and approvals", "Key risk indicators and executive reporting"])}
<a class="link-arrow" href="{url(d, "products/xploit-grc/")}" style="margin-top:18px">Run it all in Xploit GRC {icon("arrow")}</a></div>
{shot(d, "grc-risk-heatmap", "Xploit GRC risk heatmap showing risks by likelihood and impact", "Xploit GRC, risk heatmap", w=1100, h=687)}
</div></div></section>'''
    return svc_page("compliance-risk-management", "Compliance & Risk Management", "Compliance: ISO 27001, SOC 2, CMMC, NCA, NESA",
        "Compliance and risk management from Xploit Security: ISO 27001 implementation, SOC 2 readiness, CMMC Level 1 and 2, PCI DSS, GDPR, NCA ECC, SAMA, Aramco SACS-002, UAE NESA, CBUAE, ADGM and DIFC.",
        "ISO 27001 Consulting, SOC 2 Compliance, CMMC Consulting, NCA ECC, NESA, SAMA, SACS-002, PCI DSS, GDPR compliance, risk management",
        "Compliance &amp; risk management", "Compliance that stands up to auditors and attackers.",
        "Implementation and certification readiness for ISO 27001, SOC 2, CMMC and PCI DSS, plus deep experience with Saudi and UAE regulators, backed by practical risk management.", side, b)

def assessments():
    d = 2
    side = f'<h3>Assessment types</h3>{checks(["Gap assessments against any framework", "ISO 27001 internal audits", "IT and OT/ICS security assessments", "Cloud security audits", "Penetration tests and security reviews", "Third-party / vendor assessments"])}'
    b = f'''
<section class="section"><div class="container">
{section_head("Know exactly where you stand", "Independent assessments with findings you can act on.", "An assessment is only as good as what happens next. Ours end with prioritized, owner-ready findings, not a report that sits on a shelf.")}
<div class="grid grid-3">
{card("clipboard", "Gap assessments", "Measure your current controls against ISO 27001, SOC 2, CMMC, NCA ECC, NESA, IEC 62443 or your own policy set, and size the work to close each gap.")}
{card("award", "Internal audits", "ISO 27001 internal audits conducted by certified lead auditors, with nonconformities, observations and corrective-action follow-up.")}
{card("eye", "Security reviews", "Focused reviews of architecture, configurations, identity, logging and incident readiness, in IT, cloud or OT environments.")}
</div></div></section>

<section class="section section-alt"><div class="container">
{section_head("Our assessment approach", "Evidence-based. Transparent. Repeatable.")}
<div class="steps five">
<div class="step reveal"><span class="num">01</span><h3>Scope</h3><p>Agree objectives, criteria, sites, systems and stakeholders.</p></div>
<div class="step reveal"><span class="num">02</span><h3>Collect</h3><p>Interviews, document review, technical sampling and site walk-throughs.</p></div>
<div class="step reveal"><span class="num">03</span><h3>Evaluate</h3><p>Test controls against criteria and rate each finding by risk.</p></div>
<div class="step reveal"><span class="num">04</span><h3>Report</h3><p>Executive summary, detailed findings, evidence and recommendations.</p></div>
<div class="step reveal"><span class="num">05</span><h3>Follow up</h3><p>Corrective-action tracking and verification to closure.</p></div>
</div></div></section>

<section class="section"><div class="container"><div class="split reverse">
<div class="reveal"><span class="eyebrow">Findings to closure</span><h2>Turn every finding into an assigned task.</h2>
<p>Clients can receive findings directly into Xploit GRC's findings register and task board, with owners, priorities and deadlines, so remediation is visible to everyone and nothing gets lost after the audit.</p>
{checks(["Central findings register for audit, assessment and vendor findings", "Corrective actions with due dates and approval", "Progress tracking and accountability on the dashboard"])}</div>
{shot(d, "grc-task-board", "Xploit GRC Kanban task board for remediation", "Xploit GRC, remediation task board", w=1100, h=687)}
</div></div></section>'''
    return svc_page("security-assessments-audits", "Security Assessments & Audits", "Cybersecurity Assessments, Audits & Gap Assessments",
        "Security assessments and audits from Xploit Security: gap assessments, ISO 27001 internal audits, IT and OT/ICS security assessments, cloud audits and security reviews with findings tracked to closure.",
        "cybersecurity audit, gap assessment, ISO 27001 internal audit, security assessment, OT security assessment, cloud security audit",
        "Security assessments &amp; audits", "See your gaps before an auditor or attacker does.",
        "Gap assessments, internal audits and security reviews across IT, cloud and OT, delivered by certified auditors with findings tracked through to closure.", side, b)

def services_hub():
    d = 1
    path = "services/"
    crumbs = [("Services", path)]
    disciplines = [("bug", "Penetration testing"), ("cloud", "Cloud security audit and architecture reviews"), ("factory", "IT and OT/ICS security assessments"),
                   ("scale", "Governance, risk and compliance (GRC)"), ("lock", "Data privacy and protection"), ("user-check", "Virtual CISO (vCISO) advisory"),
                   ("graduation", "Cybersecurity awareness and training")]
    cards = "".join(card(ic, esc(n), esc(ds), url(d, f"services/{s}/")) for s, n, ds, ic in SERVICES)
    disc = "".join(f'<div class="industry reveal">{icon(ic)}{esc(n)}</div>' for ic, n in disciplines)
    btns = f'<a class="btn btn-primary" href="{url(d, "contact/?type=consulting")}">Book a Consultation {icon("arrow")}</a><a class="btn btn-ghost" href="{url(d, "products/")}">View products</a>'
    side = f'<h3>Frameworks covered</h3>{chips(["ISO 27001", "NIST", "PCI DSS", "GDPR", "SOC 2", "CMMC", "NCA ECC", "NCA CCC", "SAMA", "SACS-002", "NESA", "CBUAE", "ADGM", "DIFC", "IEC 62443"], "red")}'
    body = page_hero(d, crumbs, "Cybersecurity services", "IT and OT cybersecurity services that strengthen resilience.",
                     "We deliver innovative, proactive and trusted services that protect critical infrastructure, enterprise applications and government organizations, designed to strengthen digital resilience and compliance in an evolving threat landscape.", btns, side)
    body += f'''<section class="section"><div class="container">{section_head("Our services", "Choose where to start.")}<div class="grid grid-3">{cards}</div></div></section>
<section class="section section-alt"><div class="container">{section_head("Seven disciplines, one security partner", "End-to-end coverage, from assessment to remediation to ongoing advisory.")}
<div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(300px,1fr))">{disc}</div></div></section>'''
    body += cta_band(d, "Not sure which service you need?", "Describe your challenge and we'll recommend the right starting point: an assessment, a compliance program or ongoing vCISO support.", ("Talk to an expert", "contact/?type=consulting"))
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": "Xploit Security cybersecurity services",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": SITE["domain"] + f"/services/{s}/"} for i, (s, n, _, _) in enumerate(SERVICES)]}
    return path, page(d, path, "Cybersecurity Services: IT, OT, Compliance & vCISO",
                      "Explore Xploit Security's cybersecurity services: consulting, vCISO, IT cybersecurity and penetration testing, OT and industrial security, compliance and risk management, and security assessments.",
                      body, "sp", ld, crumbs, keywords="Cybersecurity Consulting, IT Cybersecurity Services, OT Cybersecurity, vCISO Services, ISO 27001 Consulting, SOC 2 Compliance, CMMC Consulting")

ALL = [services_hub, consulting, vciso, it_sec, ot_sec, compliance, assessments]
