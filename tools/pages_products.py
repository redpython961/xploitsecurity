from lib import *

def prod_ld(name, desc, path, category, offers=None, os="Web"):
    ld = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": name, "description": desc, "applicationCategory": category,
          "operatingSystem": os, "url": abs_url(path), "publisher": {"@id": SITE["domain"] + "/#org"}}
    if offers:
        ld["offers"] = offers
    return ld

def other_products(d, exclude):
    cards = "".join(card(ic, esc(n), esc(ds), url(d, f"products/{s}/"), cyan=True, tag=t, tagcls={"Free": "free", "OT": "ot"}.get(t, "saas"))
                    for s, n, ds, ic, t in PRODUCTS if s != exclude)
    return f'<section class="section section-alt"><div class="container">{section_head("More from Xploit Security", "Explore our other platforms.", cyan=True)}<div class="grid grid-4">{cards}</div></div></section>'

# ---------------------------------------------------------------------------
def safemind():
    d = 2
    path = "products/safemind/"
    crumbs = [("Products", "products/"), ("SafeMind", path)]
    btns = f'<a class="btn btn-primary" href="#poc">Request a SafeMind POC {icon("arrow")}</a><a class="btn btn-ghost" href="#pricing">See pricing</a>'
    side = '''<h3>Demo inbox</h3>
<div style="border:1px solid var(--line-2);border-radius:12px;padding:16px;background:var(--bg-2)">
<div style="display:flex;justify-content:space-between;font-family:var(--mono);font-size:.72rem;color:var(--text-3)"><span>IT Helpdesk</span><span>09:41</span></div>
<div style="font-family:var(--mono);font-size:.72rem;color:#ff8a80;margin:4px 0 10px">it-helpdesk@c0mpany-secure.example</div>
<strong style="display:block;margin-bottom:6px">Action required: your password expires today</strong>
<p class="small" style="margin-bottom:14px">Dear user, verify your account now to keep your access.</p>
<div style="display:flex;gap:8px"><span class="chip red">Verify now</span><span class="chip" style="border-color:rgba(34,197,94,.4);color:#86efac">Report phishing ✓</span></div>
</div><p class="note">This email landed in your inbox. What do you do?</p>'''
    hero = page_hero(d, crumbs, "SafeMind · Security awareness SaaS", "Your firewall can't stop a click.",
                     "Build real defensive reflexes across your workforce with microlearning, realistic phishing simulations and tips delivered in Microsoft Teams and Slack.", btns, side)
    hero = hero.replace('<span class="eyebrow ">SafeMind', '<a class="hero-offer" href="#poc"><b>POC</b> Pilot SafeMind with your own team →</a><br><span class="eyebrow ">SafeMind', 1)
    sm_form = lead_form("safemind-poc", "Proof of Concept (POC) request", "SafeMind", "Request a SafeMind POC",
                        "Tell us about your organization and we'll scope a proof of concept.", "Request a SafeMind POC",
                        "Thank you, your SafeMind POC request has been received.",
                        [("Number of employees", "emp", ["25–100", "101–500", "501–1,000", "1,001–5,000", "5,000+"]),
                         ("Collaboration platform", "collab", ["Microsoft Teams", "Slack", "Both", "Neither"])])
    sm_poc = f"""<section class="section" id="poc"><div class="container"><div class="offer">
<div class="reveal"><span class="badge">{icon("graduation")} Proof of Concept</span>
<h2>See SafeMind work with your own people.</h2>
<p class="lead">Arrange a SafeMind Proof of Concept (POC) and evaluate the platform in your environment before you commit.</p>
<ol class="steps-mini">
<li><span><strong>Experience the platform</strong>Explore the learner and administrator experience first-hand.</span></li>
<li><span><strong>Explore awareness capabilities</strong>Try microlearning, phishing simulations and Teams/Slack tips.</span></li>
<li><span><strong>Evaluate fit</strong>Assess features, reporting and suitability for your organization.</span></li>
<li><span><strong>Build security culture</strong>Understand how SafeMind supports employee awareness and a stronger security culture.</span></li>
</ol>
<div class="trust-row"><span>{icon("check")}Guided by our team</span><span>{icon("check")}Your users, your scenarios</span><span>{icon("check")}No long-term commitment</span></div>
</div>
{sm_form}
</div></div></section>"""
    stats = '''<div class="stats reveal">
<div class="stat"><strong class="text-red">74%</strong><span>of breaches involved a human element, including phishing clicks, weak or stolen passwords and misconfigured systems.</span><cite>Verizon DBIR 2023</cite></div>
<div class="stat"><strong class="text-red">41%</strong><span>of cybersecurity incidents originated from phishing, the most common attack method.</span><cite>IBM Security X-Force 2023</cite></div>
<div class="stat"><strong class="text-red">41%</strong><span>of organizations say lack of time and resources is the biggest barrier to effective awareness training.</span><cite>SANS Security Awareness 2024</cite></div>
<div class="stat"><strong class="text-red">89%</strong><span>of respondents rank social engineering as the top human-related cyber risk.</span><cite>SANS Security Awareness 2024</cite></div>
</div>'''
    tiers = [("A", "25 to 50", "$3.40"), ("B", "51 to 100", "$3.10"), ("C", "101 to 500", "$2.75"), ("D", "501 to 1,000", "$2.45"),
             ("E", "1,001 to 2,000", "$2.20"), ("F", "2,001 to 3,000", "$2.00"), ("G", "3,001 to 5,000", "$1.80"), ("H", "5,001 and above", "Get a quote")]
    rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in tiers)
    body = hero + f'''
<section class="section"><div class="container">
{section_head("Why awareness matters", "Attackers target people first.", "Humans remain the most vulnerable link in an organization's defense. Email phishing continues to be the most effective attack method, and the root cause is a lack of knowledge and defensive skills, not a technology flaw.")}
{stats}
</div></section>

<section class="section section-alt"><div class="container">
{section_head("How SafeMind works", "One program that keeps people sharp.", "SafeMind combines concise lessons with hands-on practice in a continuous cycle, so awareness turns into everyday habit, at work and at home.")}
<div class="cycle reveal">
<div><strong data-n="01">Phish</strong><p>Send realistic attacks in a safe, controlled environment.</p></div>
<div><strong data-n="02">Train</strong><p>Deliver short lessons that build recognition skills.</p></div>
<div><strong data-n="03">Test</strong><p>Measure what changed with assessments and new campaigns.</p></div>
<div><strong data-n="04">Repeat</strong><p>Track progress and keep improving over time.</p></div>
</div></div></section>

{sm_poc}
<section class="section"><div class="container">
{section_head("Platform capabilities", "Everything you need to run an awareness program.")}
<div class="grid grid-3">
<div class="card reveal"><div class="ico">{icon("cloud")}</div><h3>Cloud-native platform</h3><p>Modern and easy to deploy.</p><div style="height:14px"></div>{checks(["Runs on AWS with a multi-tenant architecture, optimized for businesses of all sizes", "Fast deployment and seamless integration with your existing internal systems", "Flexible scalability that grows with your organization"])}</div>
<div class="card reveal"><div class="ico">{icon("mail")}</div><h3>Phishing simulations</h3><p>Realistic, technically diverse and flexible.</p><div style="height:14px"></div>{checks(["Content and attack strategies refined by leading offensive security experts", "Unlimited phishing campaigns throughout your subscription", "Customizable campaigns for specific departments or groups", "Direct links, short links, QR codes, attachments and more"])}</div>
<div class="card reveal"><div class="ico">{icon("zap")}</div><h3>AI-powered phishing &amp; training</h3><p>Smarter and more effective.</p><div style="height:14px"></div>{checks(["AI-generated simulation content that taps into human psychology", "Behavioral and learning analysis with personalized recommendations", "Orchestrated learning journeys that reduce human vulnerabilities"])}</div>
</div></div></section>

<section class="section section-alt"><div class="container"><div class="split">
<div class="reveal"><span class="eyebrow">Microlearning</span><h2>Bite-sized lessons for busy schedules.</h2>
<p>100+ practical lessons, updated to reflect the latest threats. Organizations can also add their own awareness content tailored to internal policies, industry requirements or compliance regulations.</p>
{checks(["Information system security", "Social engineering and deception techniques", "Identifying phishing, scams and malware", "Passwords and account protection", "Safe use of computers and the internet", "Secure remote and in-office working", "Device (USB, mobile) and public Wi-Fi security", "Online safety for children and families", "Real-world incident response strategies"], "cols-2")}</div>
{shot(d, "safemind-learner-dashboard", "SafeMind learner dashboard showing courses in progress, new enrollments and phishing results, including a 42.9 percent phish-prone rate", "Learner dashboard, with sample data", w=770, h=852)}
</div></div></section>

<section class="section"><div class="container"><div class="split reverse">
<div class="reveal"><span class="eyebrow">Reporting &amp; tracking</span><h2>Measure security behavior over time.</h2>
<p>Role-based, tiered access to reports gives administrators, managers and executives the view they need.</p>
{checks(["Lesson completion and assessment pass rates", "Phishing susceptibility per campaign: emails sent, content opened, links clicked, information submitted", "Learner engagement by individual or group", "Risk overview by individual, department or the entire organization"])}</div>
{shot(d, "safemind-admin-overview", "SafeMind administrator overview with ring charts of training status and results", "Administrator overview, with sample data", w=938, h=406)}
</div></div></section>

<section class="section section-alt"><div class="container">
{section_head("Microsoft Teams &amp; Slack integration", "Awareness reaches people where they already work.", "The SafeMind bot sends visual awareness tips straight to employees in Microsoft Teams and Slack, with regular reminders that keep security top of mind between training sessions.")}
<div class="grid grid-2">
{shot(d, "safemind-teams", "Illustration: the SafeMind bot in Microsoft Teams sending a weekly tip on spotting a lookalike email domain", "SafeMind tips in Microsoft Teams (illustration)", frame=False, w=1200, h=820)}
{shot(d, "safemind-slack", "Illustration: the SafeMind bot in a Slack channel sharing image tips on passphrases and QR code phishing", "SafeMind tips in Slack (illustration)", frame=False, w=1200, h=820)}
</div></div></section>

<section class="section"><div class="container">
{section_head("Business outcomes", "What your organization gains.", "You get a clear view of your security awareness posture from the very first step, then a structured way to improve it.")}
<div class="grid grid-3">
{card("shield-check", "Less human vulnerability", "Continuous, practical, up-to-date training prepares employees for the latest attack techniques, so they recognize and stop threats early.")}
{card("chart", "Lower costs, fewer incidents", "Aware employees prevent many incidents outright. When one does happen, an informed team responds faster and limits the damage.")}
{card("gauge", "Effective management", "Visual insights show each person's and department's progress, helping managers make timely decisions.")}
</div></div></section>

<section class="section section-alt"><div class="container">
{section_head("Rollout", "Five steps to full rollout.")}
<div class="steps five">
<div class="step reveal"><span class="num">01</span><h3>Assessment &amp; planning</h3><p>Analyze your current state and develop a tailored implementation plan.</p><span class="dur">1 week</span></div>
<div class="step reveal"><span class="num">02</span><h3>Setup &amp; integration</h3><p>Install, configure and integrate with your existing infrastructure.</p><span class="dur">1 day</span></div>
<div class="step reveal"><span class="num">03</span><h3>Pilot testing</h3><p>Test the system and adjust based on real user feedback.</p><span class="dur">1 week</span></div>
<div class="step reveal"><span class="num">04</span><h3>Operational training</h3><p>Train admins and end users on using and managing the platform.</p><span class="dur">1 week</span></div>
<div class="step reveal"><span class="num">05</span><h3>Official rollout</h3><p>Launch into full operation with ongoing technical support.</p><span class="dur">Ongoing</span></div>
</div><p class="note">Timelines are estimates.</p></div></section>

<section class="section"><div class="container">
{section_head("Customer story", "From easy target to prepared workforce.")}
<div class="split">
<div class="reveal">
<p>A large enterprise in a highly sensitive industry, with over 5,000 employees, had invested heavily in firewalls and intrusion prevention. A third-party penetration test found a different reality: using public information such as job postings and customer service data, testers crafted targeted phishing emails, and the greatest risk lay in the habits and awareness of people.</p>
<div class="kpi-row"><div><strong class="text-red">78%</strong><span>failed to recognize the attack in the first campaigns</span></div><div><strong class="text-cyan">&lt;5%</strong><span>phishing-prone rate after two years</span></div></div>
<div class="kpi-row"><div><strong>325</strong><span>phishing campaigns</span></div><div><strong>75,000+</strong><span>simulated emails sent</span></div><div><strong>100+</strong><span>learning videos</span></div></div>
</div>
<div class="reveal"><blockquote class="quote">“We deployed multiple sophisticated and compelling scenarios using a variety of techniques, but detected no signs of compromise. The entire phishing campaign had to be redesigned from scratch.”<footer>The returning red team</footer></blockquote>
<p class="note">Results reported by SafeMind for one client. Your results may differ.</p></div>
</div></div></section>

<section class="section section-alt" id="pricing"><div class="container">
{section_head("Pricing", "Simple per-user pricing.", "Prices are per user per month, based on a 12-month commitment. The more people you protect, the lower your rate.")}
<div class="split" style="align-items:start">
<div class="table-wrap reveal"><table class="data"><caption class="sr-only">SafeMind pricing tiers</caption><thead><tr><th scope="col">Level</th><th scope="col">Users</th><th scope="col">USD / user / month</th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="reveal">
<div class="calc" id="sm-calc">
<label for="sm-users">How many users do you have? <span class="calc-users">250</span></label>
<input id="sm-users" type="range" min="25" max="5001" step="1" value="250">
<div class="calc-out"><div><span>Rate / user / mo</span><strong data-rate>$2.75</strong></div><div><span>Monthly</span><strong data-month>$687.50</strong></div><div><span>12 months</span><strong data-year12>$8,250.00</strong></div></div>
<p class="note">Estimate only, before any discount. Assumes one rate for all users in your level.</p>
</div>
<div style="height:20px"></div>
{checks(["Organizations with over 5,000 users receive a customized quotation", "10% discount for 3-year contracts", "Onboarding support included", "Add your own awareness content, tailored to your policies and regulations"])}
</div></div></div></section>
''' + other_products(d, "safemind") + cta_band(d, "Find out who would click before an attacker does.", "Arrange a SafeMind Proof of Concept and see how your workforce responds, before you commit.", ("Request a SafeMind POC", "contact/?type=poc&interest=safemind"), ("See pricing", "products/safemind/#pricing")) + sticky_cta("SafeMind: pilot it with your own team", "Request a SafeMind POC", "#poc")
    desc = "SafeMind is a cybersecurity awareness SaaS platform: 100+ microlearning lessons, unlimited realistic phishing simulations, AI-powered learning journeys, reporting, and tips in Microsoft Teams and Slack."
    offers = {"@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "1.80", "highPrice": "3.40", "description": "Per user per month, 12-month commitment"}
    return path, page(d, path, "SafeMind: Security Awareness Training SaaS", desc, body, "sp",
                      prod_ld("SafeMind", desc, path, "SecurityApplication", offers), crumbs,
                      keywords="Cybersecurity Awareness SaaS, security awareness training, phishing simulation, SafeMind, Microsoft Teams security awareness, microlearning")

# ---------------------------------------------------------------------------
def grc():
    d = 2
    path = "products/xploit-grc/"
    crumbs = [("Products", "products/"), ("Xploit GRC", path)]
    btns = f'<a class="btn btn-primary" href="#poc">Request a GRC POC {icon("arrow")}</a><a class="btn btn-ghost" href="#features">Discover features</a>'
    side = f'''<h3>At a glance</h3>
<div class="kpi-row" style="margin-top:6px"><div><strong>38+</strong><span>frameworks &amp; regulations</span></div><div><strong>80</strong><span>security checklists</span></div></div>
<div class="kpi-row" style="margin-top:18px"><div><strong>IT + OT</strong><span>one connected register</span></div><div><strong>0</strong><span>code to add a framework</span></div></div>
<div style="height:18px"></div>{chips(["SaaS", "On-premises", "Tenant-isolated", "SSO & audit trail"], "red")}'''
    hero = page_hero(d, crumbs, "Xploit GRC · Governance, risk &amp; compliance", "Govern risk. Ensure compliance. Stay secure.",
                     "A smarter, simpler way to manage cybersecurity governance, risk, compliance and security frameworks from one centralized platform, available as SaaS or deployed on-premises.", btns, side)
    hero = hero.replace('<span class="eyebrow ">Xploit GRC', '<a class="hero-offer" href="#poc"><b>POC</b> Evaluate Xploit GRC on your own program →</a><br><span class="eyebrow ">Xploit GRC', 1)
    grc_form = lead_form("grc-poc", "Proof of Concept (POC) request", "Xploit GRC", "Request a GRC POC",
                         "Tell us about your program and we'll prepare a proof of concept.", "Request a GRC POC",
                         "Thank you, your Xploit GRC POC request has been received.",
                         [("Preferred deployment", "dep", ["SaaS", "On-premises", "Not sure yet"]),
                          ("Frameworks of interest", "fw", None)])
    grc_poc = f"""<section class="section" id="poc"><div class="container"><div class="offer">
<div class="reveal"><span class="badge">{icon("layers")} Proof of Concept</span>
<h2>Evaluate Xploit GRC on your own program.</h2>
<p class="lead">Arrange a Proof of Concept (POC) and assess how Xploit GRC supports your governance, risk and compliance requirements, with your frameworks and your data.</p>
<ol class="steps-mini">
<li><span><strong>Explore the dashboard</strong>Walk through the CISO dashboard, registers and day-to-day functionality.</span></li>
<li><span><strong>Evaluate risk &amp; compliance</strong>Score risks, run compliance assessments and review gaps.</span></li>
<li><span><strong>Review frameworks</strong>Browse the 38+ standards in the library, or import your own.</span></li>
<li><span><strong>Try evidence &amp; remediation</strong>Attach evidence once, reuse it, and track remediation to closure.</span></li>
</ol>
<div class="trust-row"><span>{icon("check")}SaaS or on-premises</span><span>{icon("check")}Your frameworks</span><span>{icon("check")}Guided by GRC practitioners</span></div>
</div>
{grc_form}
</div></div></section>"""
    tour = [
        ("grc-compliance-assessments", "Compliance assessments", "Assess every requirement in one workspace.", "Inline status buttons, evidence reuse, owners and gaps, with live compliance scoring, focus mode and one-click tasks from gaps.", ["Readiness score per framework", "Evidence linked once, reused everywhere", "PDF & Excel reports"]),
        ("grc-risk-scoring", "Risk scoring", "Scoring your board can actually read.", "Click the matrix to set inherent, residual and target risk. Every result reads like L 4 × I 5 = 20 → Critical, mapped to your appetite.", ["3×3, 4×4 or 5×5 methodologies", "Risk acceptance with approvals", "Linked assets, controls and vendors"]),
        ("grc-risk-heatmap", "Risk heatmap", "Your whole risk portfolio on one grid.", "Every cell shows its score and how many risks sit there. Filter IT or OT, switch between inherent, residual and target, and click a cell to drill in.", ["Scale values and labels on both axes", "Colour bands tied to your risk appetite", "One click from cell to risk record"]),
        ("grc-checklist-focus", "Checklist focus mode", "Run a checklist in minutes, not hours.", "Pick any of 80 checklists, run it against a PLC, server, vendor or process, and answer one item at a time with Pass, Fail or N/A, keyboard shortcuts included.", ["Run against assets, vendors or processes", "Evidence notes on every answer", "Failures become assigned tasks"]),
        ("grc-task-board", "Task board", "Remediation everyone can see.", "Create, assign and drag tasks across a Kanban board. Findings, risk treatments and audit actions all land in one place.", ["Assign to anyone with due dates", "Closure notes & approval", "Overdue tracking on the dashboard"]),
        ("grc-approval-workflows", "Approval workflows", "Multi-step approvals, built visually.", "Design approval chains for policies, risk acceptance, task closure, DPIAs and BIAs, by role, named user, owner or BU manager.", ["Conditions by risk level, type or domain", "Progress stepper on every record", "Full audit trail of every decision"]),
        ("grc-framework-library", "Framework library", "38+ frameworks, ready when you are.", "Start assessments from the central library (ISO, NIST, NCA ECC and OTCC, SACS-002, SOC 2, CMMC and more) or import and version your own.", ["Filter by collection, region and industry", "Duplicate and customize any framework", "Excel, CSV, JSON, XML, Word and PDF import"]),
    ]
    tour_html = ""
    for i, (img, lab, h, p, li) in enumerate(tour):
        tour_html += f'''<div class="split {"reverse" if i % 2 else ""}" style="margin-bottom:80px">
<div class="reveal"><span class="eyebrow">{lab}</span><h3 style="font-size:1.7rem">{h}</h3><p>{p}</p>{checks(li)}</div>
{shot(d, img, "Xploit GRC " + lab.lower() + " screen", "Real product screen", w=1100, h=687)}</div>'''
    more = [("grc-checklist-studio", "Checklist studio", "80 ready-to-run security checklists for OT, cloud, identity and more."),
            ("grc-bia", "Business impact analysis", "Impact over time drives criticality and RTO."),
            ("grc-data-privacy", "Data privacy", "RoPA, DPIAs, data subject requests and 72-hour breach clocks."),
            ("grc-asset-inventory", "IT & OT asset inventory", "Criticality, CIA, exposure and owners for every system."),
            ("grc-third-party", "Third-party register", "Criticality, data access, rating and reassessment dates."),
            ("grc-findings", "Findings register", "Audit, assessment and vendor findings in one list."),
            ("grc-sso", "SSO & integrations", "Entra ID, Okta, Google, REST API keys and webhooks."),
            ("grc-reports", "Reports & exports", "Executive PDF, compliance reports and Excel registers."),
            ("grc-my-work", "My work", "Every approval, task and requirement assigned to you.")]
    more_html = "".join(f'<div class="card reveal" style="padding:0;overflow:hidden"><img src="{url(d, "assets/img/products/"+im+".webp")}" alt="Xploit GRC {esc(t)} screen" width="860" height="537" loading="lazy" decoding="async" style="border-bottom:1px solid var(--line)"><div style="padding:22px"><h3>{esc(t)}</h3><p>{esc(x)}</p></div></div>' for im, t, x in more)
    modules = [("Dashboard & Executive Reporting", "See your posture at a glance and brief leadership in minutes.", ["Cybersecurity posture index", "Compliance progress by framework", "Risk exposure & heatmaps", "Open findings & remediation status"]),
               ("Governance & Policy Management", "A living policy library with real accountability.", ["Central policy repository", "Create, review and manage policies", "Version control & approval workflows", "Acknowledgment tracking"]),
               ("Risk Management", "Clear, defensible scoring from identification to treatment.", ["Cybersecurity risk register", "Identification & assessment", "Inherent and residual scoring (L × I)", "Treatment plans, owners & tracking"]),
               ("Compliance Management", "Assess once, see gaps instantly, prove it with evidence.", ["Centralized compliance monitoring", "Control & requirement assessment", "Gap identification", "Evidence collection & status tracking"]),
               ("Framework Management", "Built-in library, multi-format import, or build your own, fully versioned.", ["38+ frameworks out of the box", "Version control & comparison", "Publish / unpublish per framework", "Add new standards without code"]),
               ("Asset Management", "An IT and OT inventory focused on what GRC needs.", ["Centralized asset inventory", "Ownership & classification", "CIA ratings & business criticality", "RTO / RPO tracking"]),
               ("Findings & Remediation", "One action engine across audits, risks, gaps and vendors.", ["Central findings register", "Assign corrective actions", "Priorities, deadlines & task board", "Progress tracking & accountability"]),
               ("Audit Management", "Plan, execute and close audits in one workspace.", ["Internal & external audits", "Audit planning & scope", "Evidence management", "Findings & corrective actions"]),
               ("Third-Party Risk Management", "Know which suppliers can hurt you, and act on it.", ["Vendor security assessments", "Supplier risk tracking", "Configurable questionnaires", "Third-party compliance monitoring"])]
    mod_html = "".join(f'<div class="card reveal"><span class="eyebrow" style="margin-bottom:10px">{i+1:02d}</span><h3>{esc(t)}</h3><p style="margin-bottom:14px">{esc(s)}</p>{checks([esc(x) for x in li])}</div>' for i, (t, s, li) in enumerate(modules))
    fws = [("International Standards", ["ISO/IEC 27001:2022", "ISO/IEC 27002:2022", "ISO/IEC 27005", "ISO/IEC 42001", "ISO 22301", "ISO 31000"]),
           ("Cybersecurity Frameworks", ["NIST CSF 2.0", "NIST SP 800-53", "CIS Controls v8.1", "COBIT 2019", "MITRE ATT&CK", "NCA ECC", "SAMA CSF"]),
           ("Privacy & Data Protection", ["GDPR", "ISO/IEC 27701", "HIPAA Security Rule", "UAE PDPL", "Saudi PDPL"]),
           ("Cloud & Service Compliance", ["SOC 2", "PCI DSS 4.0.1", "ISO/IEC 27017", "ISO/IEC 27018", "CSA CCM v4"]),
           ("Industrial & OT Cybersecurity", ["IEC 62443", "NCA OTCC", "Aramco SACS-002", "NIST SP 800-82", "NERC CIP"]),
           ("Government & Defense", ["CMMC Level 1", "CMMC Level 2", "NIST SP 800-171", "FedRAMP", "EU NIS2", "EU DORA"])]
    fw_html = "".join(f'<div class="fw-group reveal"><h3>{esc(t)} <small>{len(l)}</small></h3>{chips(l, "cyan" if "OT" in t else "")}</div>' for t, l in fws)
    uses = [("Water & power utility", "NCA OTCC readiness across desalination and power plants", ["Inventory PLCs, SCADA and HMIs per plant", "Run OT checklists at each site", "Track OTCC and IEC 62443 gaps in one view", "Report plant-by-plant readiness to the board"], "NCA OTCC · IEC 62443 · NCA ECC"),
            ("Defense supplier", "CMMC Level 2 readiness for a DoD contract", ["Scope CUI systems and owners", "Assess 110 NIST SP 800-171 requirements", "Turn NOT MET items into POA&M tasks", "Export SSP evidence and readiness reports"], "CMMC L2 · NIST SP 800-171"),
            ("SaaS scale-up", "SOC 2 and ISO 27001 with one set of evidence", ["Run both frameworks side by side", "Upload evidence once, reuse it everywhere", "Automate policy approvals and acknowledgments", "Give auditors restricted read-only access"], "SOC 2 · ISO 27001 · ISO 27701"),
            ("Oil & gas contractor", "Aramco SACS-002 compliance as a third party", ["Identify your third-party class and scope", "Assess SACS-002 control areas", "Collect evidence for Aramco reviews", "Track remediation to closure"], "SACS-002 · NCA ECC"),
            ("Consultancy / vCISO", "Many clients, one login", ["Separate, isolated workspace per client", "Reuse your checklists and frameworks", "Standard reports across every engagement", "Switch clients in one click"], "Any framework"),
            ("Privacy team", "UAE and Saudi PDPL in practice", ["Build the RoPA for every processing activity", "Screen and approve DPIAs", "Answer data subject requests on time", "Log breaches against the 72-hour clock"], "UAE PDPL · Saudi PDPL · GDPR")]
    use_html = "".join(f'<div class="card reveal"><span class="eyebrow" style="margin-bottom:12px">{esc(a)}</span><h3>{esc(b)}</h3><div style="height:8px"></div>{checks([esc(x) for x in li])}<p class="note">{esc(t)}</p></div>' for a, b, li, t in uses)
    plans = [("Starter", "Up to 5 users", "4,900", "≈ AED 18,000 / year", "For SMBs and a first ISO 27001 or NCA ECC project", False, "Request a POC"),
             ("Growth", "Up to 15 users", "9,900", "≈ AED 36,400 / year", "For mid-size teams running multiple frameworks", True, "Request a POC"),
             ("Business", "Up to 40 users", "19,900", "≈ AED 73,100 / year", "For multi-site organizations with IT and OT teams", False, "Request a POC"),
             ("Enterprise", "Up to 100 users", "34,900", "≈ AED 128,200 / year", "For groups, utilities and critical infrastructure. 100+ users: $250 per extra user", False, "Contact sales")]
    plan_html = "".join(f'<div class="plan reveal {"popular" if pop else ""}">{"<span class=pop>MOST POPULAR</span>" if pop else ""}<h3>{n}</h3><span class="users">{u}</span><div class="price">${p}<small> / year</small></div><span class="aed">{a}</span><p>{t}</p><a class="btn {"btn-primary" if pop else "btn-ghost"}" href="{url(d, "contact/?type=poc&interest=xploit-grc")}">{c}</a></div>' for n, u, p, a, t, pop, c in plans)

    body = hero + f'''
<section class="section"><div class="container">
{section_head("Introducing Xploit GRC", "One platform for your entire security program.", "Xploit GRC brings governance, risk, compliance, assets, audits and third parties into one connected workspace, so every control, risk, policy and piece of evidence tells the same story.")}
<div class="grid grid-3">
{card("database", "Centralized management", "Policies, risks, assets and controls in one source of truth.")}
{card("clipboard", "Simplified compliance", "Assess requirements, attach evidence, close gaps, fast.")}
{card("network", "Integrated risk", "Risks linked to assets, controls, vendors and findings.")}
{card("refresh", "Continuous improvement", "Recurring assessments, KPIs and KRIs that show progress.")}
{card("layers", "Multi-framework", "ISO, NIST, NCA, SOC 2, CMMC and IEC 62443 side by side.")}
{card("chart", "Actionable insights", "Role-based dashboards and executive reports in one click.")}
</div>
<div style="margin-top:56px">{shot(d, "grc-dashboard", "Xploit GRC CISO dashboard with posture index, compliance progress by framework and risk exposure", "Xploit GRC, CISO dashboard. Real screens, no mock-ups.", w=1100, h=687)}</div>
</div></section>

{grc_poc}
<section class="section section-alt"><div class="container">
{section_head("Deployment", "Your platform, your way.", "Choose the deployment model that fits your security, data-residency and operational requirements. Every option runs the same full platform.")}
<div class="grid grid-2">
<div class="card reveal"><div class="ico">{icon("cloud")}</div><h3>SaaS</h3><p>Fully managed and tenant-isolated by design, with daily backups, encryption, MFA and a full audit trail. Optional KSA or UAE data residency and dedicated hosting are available.</p><div style="height:14px"></div>{checks(["Fast onboarding, no infrastructure to run", "Tenant isolation, SSO and audit trail", "KSA / UAE data residency option"])}</div>
<div class="card reveal"><div class="ico">{icon("server")}</div><h3>On-premises</h3><p>Deploy Xploit GRC inside your own environment when policy, sovereignty or OT segregation requires your GRC data to stay on your infrastructure.</p><div style="height:14px"></div>{checks(["Full control over data and hosting", "Fits regulated and critical-infrastructure environments", "Same modules, frameworks and workflows as SaaS"])}</div>
</div>
<div class="grid grid-3" style="margin-top:22px">
{card("layers", "Enterprise flexibility", "Business units, granular roles, SSO and approval workflows at scale.")}
{card("chart", "Scalability", "Add frameworks, versions and tenants without redevelopment.")}
{card("database", "Centralized compliance", "One connected data model instead of scattered files and trackers.")}
</div></div></section>

<section class="section" id="features"><div class="container">
{section_head("Product tour", "See how the work actually gets done.", "Real screens from Xploit GRC.")}
{tour_html}
</div></section>

<section class="section section-alt"><div class="container">
{section_head("More from the platform", "Every module shares one data model.")}
<div class="grid grid-3">{more_html}</div>
</div></section>

<section class="section"><div class="container">
{section_head("How it works", "From first framework to board report.")}
<div class="steps">
<div class="step reveal"><span class="num">01</span><h3>Choose your frameworks</h3><p>Pick from the library or import your own: ISO 27001, NCA ECC, IEC 62443 and more.</p></div>
<div class="step reveal"><span class="num">02</span><h3>Map assets &amp; risks</h3><p>Load IT and OT assets, rate criticality and register risks with clear L × I scoring.</p></div>
<div class="step reveal"><span class="num">03</span><h3>Assess &amp; collect evidence</h3><p>Assess requirements, run checklists and attach evidence once for every framework.</p></div>
<div class="step reveal"><span class="num">04</span><h3>Remediate &amp; report</h3><p>Assign tasks, approve through workflows and brief leadership with live dashboards.</p></div>
</div></div></section>

<section class="section section-alt"><div class="container">
{section_head("Platform capabilities", "Nine connected modules. Nothing your program doesn't need.", "Designed for CISOs, compliance leads and auditors.")}
<div class="grid grid-3">{mod_html}</div>
<div style="margin-top:28px">{chips(["Visual approval workflows", "Business impact analysis", "RoPA, DPIAs & DSRs", "80 security checklists", "SSO, API & webhooks"], "red")}</div>
</div></section>

<section class="section"><div class="container">
{section_head("Supported frameworks", "Every standard you answer to. One place.", "Start from the built-in library, version it, and extend it with any regulation or internal framework as your requirements evolve.")}
<div class="grid grid-3">{fw_html}</div>
<p class="note">Plus your own: import any regulation or internal framework from Excel, CSV, JSON, XML, Word or PDF. Xploit GRC tracks readiness; it does not issue certifications or authorizations.</p>
</div></section>

<section class="section section-alt"><div class="container">
{section_head("Example use cases", "What teams do with Xploit GRC.", "Illustrative scenarios showing how the platform fits real programs across IT and OT.")}
<div class="grid grid-3">{use_html}</div>
</div></section>

<section class="section"><div class="container">
{section_head("Why Xploit GRC", "Enterprise-grade GRC without enterprise-level complexity.", "Built by practitioners who have run ISO 27001, SOC 2, CMMC and IEC 62443 programs, and wanted tools that remove work instead of creating it.")}
<div class="split" style="align-items:start">
<div class="table-wrap reveal"><table class="data"><caption class="sr-only">Spreadsheets compared with Xploit GRC</caption><thead><tr><th scope="col">Capability</th><th scope="col">Spreadsheets</th><th scope="col">Xploit GRC</th></tr></thead><tbody>
<tr><td>One evidence file, many frameworks</td><td>—</td><td class="text-red">✓</td></tr>
<tr><td>Live compliance &amp; risk dashboards</td><td>—</td><td class="text-red">✓</td></tr>
<tr><td>Approval workflows &amp; audit trail</td><td>—</td><td class="text-red">✓</td></tr>
<tr><td>Version-controlled frameworks</td><td>—</td><td class="text-red">✓</td></tr>
<tr><td>IT and OT in one register</td><td>—</td><td class="text-red">✓</td></tr>
</tbody></table></div>
<div class="grid grid-2">
{card("eye", "Simple &amp; intuitive", "Clean screens, sensible defaults, every feature within two clicks.")}
{card("refresh", "Less admin overhead", "Tasks, reminders and approvals that run themselves.")}
{card("gauge", "Compliance visibility", "Know where you stand per framework, domain and owner.")}
{card("check", "Practical by design", "Focused on GRC, not trying to be your SIEM or CMDB.")}
</div></div></div></section>

<section class="section section-alt"><div class="container">
{section_head("Built for every security team", "From a first ISO 27001 project to a multi-entity program.")}
<div class="grid grid-4">
{card("building", "SMBs", "Get audit-ready fast with templates, checklists and sensible defaults.")}
{card("landmark", "Enterprises", "Business units, granular roles, SSO and approval workflows at scale.")}
{card("briefcase", "Consultants &amp; MSPs", "Every client in its own isolated workspace, from one login.")}
{card("user-check", "CISOs &amp; auditors", "A board-ready view across every site, plant and business unit, plus restricted auditor access.")}
</div></div></section>

<section class="section" id="pricing"><div class="container">
{section_head("Pricing", "Simple pricing. Every feature included.", "Pick a plan by the number of users who create or edit records. Billed annually, with no per-framework or per-module fees.")}
<div class="plans">{plan_html}</div>
<div class="grid grid-3" style="margin-top:28px">
<div class="card reveal"><h3>Every plan includes</h3>{checks(["All modules: risk, compliance, assets, BIA, audits, vendors, privacy", "Full framework library + unlimited custom frameworks", "Workflows, task board, checklists and reports", "SSO, API keys and webhooks", "Unlimited read-only viewers", "Free time-boxed access for external auditors", "Daily backups, audit trail, encryption and MFA"])}</div>
<div class="card reveal"><h3>Consultants &amp; vCISOs</h3><p>Partner plan: $2,900 / year per client workspace (up to 5 users), your consultants free across all clients. Reseller margins available.</p><div class="divider" style="margin:20px 0"></div><h3>Optional services</h3><p>Onboarding from $2,500 · Premium support +15% · KSA / UAE data residency or dedicated hosting +40% · Extra storage $500 / 500 GB</p></div>
<div class="card reveal"><h3>Flexible terms</h3>{checks(["14-day free trial", "10% off 2-year and 15% off 3-year terms", "Add users anytime, prorated", "On-premises deployment: contact sales for licensing"])}</div>
</div>
<p class="note">Prices in USD, billed annually, excluding VAT. AED amounts are approximate.</p>
</div></section>
''' + other_products(d, "xploit-grc") + cta_band(d, "Take control of your cybersecurity governance.", "Arrange a Proof of Concept and see how Xploit GRC brings your risks, controls, policies, frameworks and evidence together.", ("Request a GRC POC", "contact/?type=poc&interest=xploit-grc"), ("See pricing", "products/xploit-grc/#pricing")) + sticky_cta("Xploit GRC: evaluate it on your own program", "Request a GRC POC", "#poc")
    desc = "Xploit GRC is cybersecurity GRC software, available as SaaS or on-premises: risk registers, compliance and control assessments, 38+ frameworks, audits, evidence, IT/OT assets, policies and executive dashboards."
    offers = {"@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "4900", "highPrice": "34900", "description": "Annual subscription by number of editing users"}
    return path, page(d, path, "Xploit GRC: GRC Software, SaaS & On-Prem", desc, body, "sp",
                      prod_ld("Xploit GRC", desc, path, "BusinessApplication", offers, "Web, On-premises"), crumbs,
                      keywords="Cybersecurity GRC Software, GRC platform, risk register, compliance management software, ISO 27001 software, NCA ECC compliance, IEC 62443, on-premises GRC")

# ---------------------------------------------------------------------------
def scenarios():
    d = 2
    path = "products/ot-attack-scenarios/"
    crumbs = [("Products", "products/"), ("OT Cyber Attack Scenarios", path)]
    btns = f'<a class="btn btn-cyan" href="{SITE["range"]}" target="_blank" rel="noopener">Explore Free OT Attack Scenarios {icon("external")}</a><a class="btn btn-ghost" href="#units">See the 10 units</a>'
    side = f'''<h3>Free resource</h3>
<div class="kpi-row" style="margin-top:4px"><div><strong class="text-cyan">10</strong><span>scenario units</span></div><div><strong class="text-cyan">14</strong><span>exam questions</span></div><div><strong class="text-cyan">$0</strong><span>always free</span></div></div>
<div style="height:16px"></div>{checks(["Runs in your browser", "XP, levels, streaks and achievements", "Certification exam (pass 11/14)", "Progress saved locally on your device"], "cyan")}'''
    hero = page_hero(d, crumbs, "Free resource · OT cyber range", "Defend the plant. One decision at a time.",
                     "A free OT cybersecurity awareness and attack-scenario platform. Work through ten immersive OT/ICS incidents drawn from real attack patterns, make the calls, see the consequences, and earn your certificate.", btns, side, ot=True, eyebrow_cyan=True)
    units = [("UNIT-01 · REMOVABLE MEDIA", "8 MIN", "The USB Stick in the Car Park", "A found USB device, a curious operator, and one decision that can reach the PLC network."),
             ("UNIT-02 · REMOTE ACCESS", "9 MIN", "The Vendor Who Called Twice", "An urgent support call, remote access to a live PLC, and a caller who is not who he claims to be."),
             ("UNIT-03 · PATCH & CHANGE", "8 MIN", "The Unpatched HMI", "A critical vulnerability advisory lands mid-production. Patch now, patch later, or something smarter?"),
             ("UNIT-04 · PHISHING", "8 MIN", "Phishing the Control Room", "An email 'from the SCADA vendor' arrives with an urgent firmware notice, crafted for people exactly like you."),
             ("UNIT-05 · NETWORK SECURITY", "9 MIN", "The Cable That Crossed the Zone", "A convenient network shortcut quietly connects the office LAN to the control network, until you find it."),
             ("UNIT-06 · INCIDENT RESPONSE", "10 MIN", "Ransomware at the Plant", "Screens lock across the site. The next thirty minutes decide whether production, and safety, survive the day."),
             ("UNIT-07 · CONTROL INTEGRITY", "9 MIN", "PLC Logic Manipulation", "A pump behaves strangely, the HMI shows normal, and the controller logic no longer matches the golden master."),
             ("UNIT-08 · ACCESS CONTROL", "8 MIN", "Default Passwords Expose Critical Systems", "Brand-new RTUs, factory credentials, and a contractor who plans to 'change them later'."),
             ("UNIT-09 · PHYSICAL SECURITY", "8 MIN", "The Fake Maintenance Technician", "Hi-vis vest, toolbox, confident smile, urgent job, and no appointment in the system."),
             ("UNIT-10 · REMOTE ACCESS", "9 MIN", "Compromised Vendor Remote Access", "The 03:00 session comes from your trusted vendor's real account, but their engineer is on leave.")]
    uh = "".join(f'<div class="unit reveal"><div class="meta"><span>{esc(a)}</span><span>{b}</span></div><h3>{esc(c)}</h3><p>{esc(x)}</p></div>' for a, b, c, x in units)
    ach = [("First Response", "Complete your first module"), ("On Watch", "3-day learning streak"), ("Zero Defects", "Score 100% on a module quiz"),
           ("Senior Operator", "Reach Level 5"), ("Full Coverage", "Complete all 10 modules"), ("Certified Defender", "Pass the final exam")]
    ah = "".join(f'<div class="industry reveal">{icon("award")}<span><strong style="display:block">{a}</strong><span class="small muted" style="font-weight:400">{b}</span></span></div>' for a, b in ach)
    body = hero + f'''
<section class="section"><div class="container">
{section_head("What it is", "A practical learning environment for industrial cyber risk.", "The OT Cyber Range turns industrial cybersecurity concepts into decisions you actually make, so the right reflexes are already there when a real incident starts.", cyan=True)}
<div class="grid grid-3">
{card("factory", "Industrial cybersecurity scenarios", "Realistic incidents set in control rooms, substations and plants, built around ICS and SCADA environments.", cyan=True)}
{card("alert", "OT threat awareness", "USB drops, rogue vendors, phishing, ransomware, logic manipulation and physical intrusion.", cyan=True)}
{card("cpu", "ICS &amp; SCADA attack concepts", "Understand how attacks move from the office LAN to PLCs and HMIs, and how to stop them.", cyan=True)}
{card("target", "Practical, decision-based learning", "Make the call at each step and see the operational consequences of every choice.", cyan=True)}
{card("gauge", "Understand industrial cyber risk", "Connect cyber events to production, safety and physical outcomes.", cyan=True)}
{card("graduation", "Built for OT people", "Designed for OT engineers, operators, cybersecurity professionals and students.", cyan=True)}
</div></div></section>

<section class="section section-alt" id="units"><div class="container">
{section_head("Training units", "Ten incidents. Ten decisions that matter.", cyan=True)}
<div class="grid grid-2">{uh}</div>
</div></section>

<section class="section"><div class="container"><div class="split">
<div class="reveal"><span class="eyebrow cyan">Certification &amp; gamification</span><h2>Earn XP. Level up. Get certified.</h2>
<p>Progress through operator grades, keep your learning streak, unlock achievements, and once all ten units are complete, sit the 14-question final exam. Score 11 or more to earn your certificate.</p>
<div class="btn-row" style="margin-top:24px"><a class="btn btn-cyan" href="{SITE["range"]}" target="_blank" rel="noopener">Start training free {icon("external")}</a></div></div>
<div class="grid grid-2">{ah}</div>
</div></div></section>

<section class="section section-alt"><div class="container">
{section_head("Who it's for", "Free for anyone protecting industrial systems.", cyan=True)}
<div class="grid grid-3">
{card("settings", "OT engineers &amp; operators", "Build instinct for the situations you're most likely to face on shift.", cyan=True)}
{card("shield", "Cybersecurity professionals", "Learn how OT incidents differ from IT, and why safety changes every decision.", cyan=True)}
{card("graduation", "Students &amp; career changers", "A hands-on introduction to industrial cybersecurity, at no cost.", cyan=True)}
</div>
<p class="note">Want this for your whole workforce, on authentic hardware? See the <a class="text-cyan" href="{url(d, "products/scada-simulator/")}">SCADA Simulator</a> or our <a class="text-cyan" href="{url(d, "services/ot-industrial-cybersecurity/")}">OT security services</a>. For accredited courses, visit <a class="text-cyan" href="{SITE["academy"]}" target="_blank" rel="noopener">Xploit Academy</a>.</p>
</div></section>
''' + other_products(d, "ot-attack-scenarios") + f'''<section class="section"><div class="container"><div class="cta-band reveal" style="border-color:rgba(34,211,238,.35)">
<span class="eyebrow cyan">Free · No cost, ever</span><h2>Explore Free OT Attack Scenarios</h2><p>Open the OT Cyber Range in your browser and complete your first unit in under ten minutes.</p>
<div class="btn-row"><a class="btn btn-cyan" href="{SITE["range"]}" target="_blank" rel="noopener">Explore Free OT Attack Scenarios {icon("external")}</a><a class="btn btn-ghost" href="{url(d, "contact/?type=sales&interest=scada-simulator")}">Talk to us about OT training</a></div></div></div></section>'''
    desc = "Free OT cybersecurity attack scenarios: ten browser-based OT/ICS incident simulations covering USB drops, rogue vendors, PLC logic manipulation and industrial ransomware, with XP, levels and a final certification exam."
    ld = prod_ld("OT Cyber Range: Free OT Attack Scenarios", desc, path, "EducationalApplication", {"@type": "Offer", "price": "0", "priceCurrency": "USD"})
    return path, page(d, path, "Free OT Cybersecurity Attack Scenarios: OT Cyber Range", desc, body, "sp", ld, crumbs,
                      keywords="OT Cybersecurity, free OT training, ICS security awareness, SCADA attack scenarios, OT cyber range, industrial cybersecurity training")

# ---------------------------------------------------------------------------
def scada():
    d = 2
    path = "products/scada-simulator/"
    crumbs = [("Products", "products/"), ("SCADA Simulator", path)]
    btns = f'<a class="btn btn-cyan" href="{url(d, "contact/?type=demo&interest=scada-simulator")}">Request a demo {icon("arrow")}</a><a class="btn btn-ghost" href="#video">Watch the video</a>'
    def seg(name, opts, default):
        return "".join(f'<input type="radio" name="{name}" id="{name}-{i}" value="{o}" {"checked" if o==default else ""}><label for="{name}-{i}">{o}</label>' for i, o in enumerate(opts))
    side = f'''<div id="scada-config">
<h3>Tailor-made for your needs</h3>
<fieldset><legend>Real-world simulation</legend><div class="seg">{seg("sector", ["Electricity", "City metro", "City water", "Oil factory"], "Electricity")}</div></fieldset>
<fieldset><legend>PLCs</legend><div class="seg">{seg("plc", ["Siemens", "ABB", "Rockwell", "Mitsubishi"], "Siemens")}</div></fieldset>
<fieldset><legend>Size</legend><div class="seg">{seg("size", ["Mini", "Small", "Medium", "Large"], "Medium")}</div></fieldset>
<p class="config-summary">Your setup: <span>Electricity, Siemens PLCs, Medium size</span></p>
<div class="btn-row"><a class="btn btn-wa" data-wa href="{SITE["wa"]}" target="_blank" rel="noopener">{WA_SVG} Request on WhatsApp</a><a class="btn btn-ghost" data-mail href="mailto:{SITE["email"]}">Email</a></div>
</div>'''
    hero = page_hero(d, crumbs, "SCADA Simulator · OT awareness &amp; testing", "Break a replica, not your plant.",
                     "Train your team and test your defenses on a tailor-made OT cyber range with authentic PLCs and a miniature replica of your plant.", btns, side, ot=True, eyebrow_cyan=True)
    hero = hero.replace('class="page-hero-card"', 'class="page-hero-card config"')
    body = hero + f'''
<section class="section" id="video"><div class="container">
{section_head("See it in action", "The simulator, live.", cyan=True)}
<div class="grid grid-2">
<figure class="reveal"><div class="video"><iframe src="https://www.youtube-nocookie.com/embed/KTmBNggqOjI?rel=0" title="Xploit SCADA Simulator in action" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div><figcaption>See the simulator in action</figcaption></figure>
<figure class="reveal"><div class="video"><iframe src="https://www.youtube-nocookie.com/embed/LgsVGpsAslw?rel=0" title="SCADA Simulator attack stages" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div><figcaption>See the attack stages</figcaption></figure>
</div></div></section>

<section class="section section-alt"><div class="container">
{section_head("Why a simulator", "A risk-free place to get it right.", "Your live operations can't be a training ground. The simulator replicates real operating environments, from water plants to power generation and distribution facilities, so your people can learn and test without touching production.", cyan=True)}
<div class="grid grid-4">
{card("graduation", "Staff training", "Build hands-on OT skills on realistic systems, not slides.", cyan=True)}
{card("settings", "System modification testing", "Try changes in the simulator before they reach the plant.", cyan=True)}
{card("shield", "Cyber threat preparation", "Rehearse attacks and your response in a safe environment.", cyan=True)}
{card("gauge", "Efficiency optimization", "Explore how your systems behave and where they can improve.", cyan=True)}
</div></div></section>

<section class="section"><div class="container"><div class="split">
<div class="reveal"><span class="eyebrow cyan">Industrial process simulation</span><h2>If it can happen in your plant, we can simulate it.</h2>
<p>We replicate the environment you depend on, then trigger the events you could never rehearse in real life, so your team sees the consequences and practices the response.</p>
<div class="grid grid-2" style="margin-top:20px">
<div><h3 style="font-size:1rem">What we can replicate</h3>{checks(["Wastewater treatment plants", "Power grids", "City lights", "Metro stations and trains", "and many more"], "cyan")}</div>
<div><h3 style="font-size:1rem">Risks we can simulate</h3>{checks(["Explosions", "Lights off", "Blackouts", "Flooding", "and many more"], "cyan")}</div>
</div>
<p class="note">Plus any cybersecurity risk scenario, tested on the same replica.</p></div>
{shot(d, "scada-cabinet", "Line drawing of a cabinet holding a detailed miniature model of an industrial site", "Miniature plant replica", frame=False, w=940, h=690)}
</div></div></section>

<section class="section section-alt"><div class="container">
{section_head("Architecture", "Your plant's whole stack, in one simulator.", cyan=True)}
<div class="split" style="margin-bottom:72px">
<div class="reveal"><h3 style="font-size:1.5rem">A miniature replica with Level 0 devices</h3><p>The system links to Level 0 devices, including sensors and pumps, all interacting with a miniature replica of the plant. Your team sees physical cause and effect, for a highly authentic learning experience.</p>
<h3 style="font-size:1.5rem;margin-top:30px">Authentic PLC integration</h3><p>PLCs sit at the heart of the simulation, connected to the Level 0 devices. Practical training and testing scenarios closely mimic real-world industrial operations.</p>{chips(["Siemens", "ABB", "Rockwell", "Mitsubishi"], "cyan")}</div>
{shot(d, "scada-plc-level0", "Diagram connecting a PLC rack to Level 0 devices on the miniature plant", "PLC rack connected to Level 0 devices", frame=False, w=1000, h=673)}
</div>
<div class="split reverse" style="margin-bottom:72px">
<div class="reveal"><h3 style="font-size:1.5rem">Your security stack, replicated</h3><p>Replicate your existing security infrastructure so you can test it thoroughly and improve it.</p>{checks(["Firewalls", "Intrusion detection and prevention (IDS/IPS)", "Security information and event management (SIEM)", "Antivirus and endpoint protection"], "cyan")}</div>
{shot(d, "scada-server-rack", "Line drawing of the simulator's server rack", "Simulator server rack", frame=False, w=1000, h=740)}
</div>
<div class="split" style="margin-bottom:72px">
<div class="reveal"><h3 style="font-size:1.5rem">Virtualized workstations</h3><p>Explore the crucial workstations in depth, and understand how the whole system fits together.</p>{checks(["Human-machine interface (HMI)", "Engineering stations", "Historians and databases"], "cyan")}</div>
{shot(d, "scada-workstations", "Three workstation screens showing a process diagram, control panels and a trend chart", "HMI, engineering and historian workstations", frame=False, w=1000, h=303)}
</div>
<div class="split reverse" style="margin-bottom:72px">
<div class="reveal"><h3 style="font-size:1.5rem">Realistic configuration transfer</h3><p>Mirror your production system's configurations, security settings and patch levels, so the simulator stays a high-fidelity copy of what you actually run.</p></div>
{shot(d, "scada-config-transfer", "Screen showing configuration moving from a production system to the simulation system", "Configuration transfer from production to simulation", frame=False, w=1000, h=402)}
</div>
<div class="split">
<div class="reveal"><h3 style="font-size:1.5rem">Network traffic simulation</h3><p>Typical network traffic gives a complete and accurate representation of daily operations.</p>{chips(["OPC", "APC", "SMB", "FTP", "HTTP", "HTTPS"], "cyan")}</div>
{shot(d, "scada-network-traffic", "Diagram of network traffic flowing between two systems", "Simulated operational network traffic", frame=False, w=1000, h=382)}
</div>
</div></section>

<section class="section"><div class="container">
{section_head("Optional add-on · Practical testing", "Then attack it.", "Add attack simulations to rigorously test your defenses and your team's response. Scenarios run across the full attack chain, from first reconnaissance to final impact.")}
<ol class="chain reveal">{"".join(f"<li>{s}</li>" for s in ["Reconnaissance", "Resource development", "Initial access", "Execution", "Persistence", "Privilege escalation", "Defense evasion", "Credential access", "Discovery", "Lateral movement", "Collection", "Command and control", "Exfiltration", "Impact"])}</ol>
</div></section>

<section class="section section-alt"><div class="container">
{section_head("Who uses it", "A practical tool for everyone responsible for OT.", cyan=True)}
<div class="grid grid-3">
{card("factory", "Industrial organizations", "Utilities, oil and gas, manufacturing and transport operators training staff and validating changes.", cyan=True)}
{card("shield", "Cybersecurity teams", "Test detection and response for OT-specific attacks against a faithful replica.", cyan=True)}
{card("settings", "OT engineers", "Practice safe operations and incident response on authentic PLCs and HMIs.", cyan=True)}
{card("briefcase", "Consultants", "Demonstrate industrial risk to stakeholders with physical cause and effect.", cyan=True)}
{card("graduation", "Training providers", "Deliver hands-on ICS/SCADA courses on real hardware.", cyan=True)}
{card("radar", "Free warm-up", "Start with our free OT attack scenarios before hands-on sessions.", url(d, "products/ot-attack-scenarios/"), cyan=True, link="Explore free scenarios")}
</div></div></section>
''' + other_products(d, "scada-simulator") + cta_band(d, "See it built for your plant.", "Tell us your sector, PLCs and team size, and we'll walk you through the right setup.", ("Request a SCADA Simulator demo", "contact/?type=demo&interest=scada-simulator"))
    desc = "The Xploit SCADA Simulator is an OT cyber range with authentic Siemens, ABB, Rockwell or Mitsubishi PLCs and a miniature plant replica, for OT cybersecurity awareness training and practical attack testing."
    ld = prod_ld("Xploit SCADA Simulator", desc, path, "SecurityApplication", None, "Hardware + Software")
    ld["@type"] = ["SoftwareApplication", "Product"]
    return path, page(d, path, "SCADA Simulator: OT Cyber Range & Testing", desc, body, "sp", ld, crumbs,
                      keywords="SCADA Simulator, OT cyber range, ICS training, SCADA security training, PLC training, OT cybersecurity testing, industrial cybersecurity")



def products_hub():
    d = 1
    path = "products/"
    crumbs = [("Products", path)]
    btns = f'<a class="btn btn-primary" href="{url(d, "products/firewall-security-analyzer/")}#free-trial">XFSA Free Trial {icon("arrow")}</a><a class="btn btn-ghost" href="{url(d, "contact/?type=poc")}">Request a POC</a>'
    hero = page_hero(d, crumbs, "Cybersecurity products", "Platforms that make security stick.",
                     "Commercial SaaS and practical industrial cybersecurity solutions, built by the same practitioners who deliver our services.", btns,
                     f'<h3>Portfolio</h3>{checks(["SafeMind: awareness SaaS", "Xploit GRC: SaaS or on-premises", "Firewall Security Analyzer: firewall audits", "SCADA Simulator: OT awareness & testing", "OT Attack Scenarios: free"], "cyan")}', ot=True, eyebrow_cyan=True)
    blocks = [
        ("safemind", "SafeMind", "Security awareness SaaS", "Microlearning, unlimited phishing simulations, AI-powered learning journeys, reporting and Microsoft Teams and Slack tips.", "safemind-admin-overview", 938, 406),
        ("xploit-grc", "Xploit GRC", "Governance, risk &amp; compliance platform", "38+ frameworks, risk registers, audits, evidence, IT/OT assets, workflows and executive dashboards. SaaS or on-premises.", "grc-dashboard", 1100, 687),
        ("firewall-security-analyzer", "Xploit Firewall Security Analyzer", "Firewall configuration audit &amp; compliance", "Automated firewall audits with CVE detection, risky-rule analysis, compliance scoring against NIST SP 800-53 and PCI DSS, and evidence-backed remediation.", "xfsa-executive-summary", 1000, 1089),
        ("scada-simulator", "SCADA Simulator", "OT awareness &amp; testing platform", "Authentic PLCs, Level 0 devices and a miniature plant replica for hands-on training and attack testing.", "scada-plc-level0", 1000, 673),
        ("ot-attack-scenarios", "OT Cyber Attack Scenarios", "Free OT awareness range", "Ten browser-based OT/ICS incident scenarios with XP, levels and a certification exam. Free.", None, 0, 0),
    ]
    out = ""
    for i, (s, n, sub, t, img, w, h) in enumerate(blocks):
        vis = shot(d, img, f"{n} product screen", None, frame=(img and img.startswith(("grc", "safemind"))), w=w, h=h) if img else f'<div class="grid grid-2 reveal"><div class="unit"><div class="meta"><span>UNIT-02 · REMOTE ACCESS</span><span>9 MIN</span></div><h3>The Vendor Who Called Twice</h3></div><div class="unit"><div class="meta"><span>UNIT-08 · ACCESS CONTROL</span><span>8 MIN</span></div><h3>Default Passwords Expose Critical Systems</h3></div><div class="unit"><div class="meta"><span>UNIT-09 · PHYSICAL</span><span>8 MIN</span></div><h3>The Fake Maintenance Technician</h3></div><div class="unit"><div class="meta"><span>UNIT-10 · REMOTE ACCESS</span><span>9 MIN</span></div><h3>Compromised Vendor Remote Access</h3></div></div>'
        offers = {"firewall-security-analyzer": ("Request a Free Trial", url(d, "products/firewall-security-analyzer/") + "#free-trial"),
                  "safemind": ("Request a SafeMind POC", url(d, "products/safemind/") + "#poc"),
                  "xploit-grc": ("Request a GRC POC", url(d, "products/xploit-grc/") + "#poc"),
                  "scada-simulator": ("Request a demo", url(d, "contact/?type=demo&interest=scada-simulator"))}
        primary = f'<a class="btn btn-cyan" href="{SITE["range"]}" target="_blank" rel="noopener">Explore Free OT Attack Scenarios {icon("external")}</a>' if s == "ot-attack-scenarios" else f'<a class="btn btn-primary" href="{offers[s][1]}">{offers[s][0]}</a>'
        out += f'''<div class="split {"reverse" if i % 2 else ""}" style="margin-bottom:96px"><div class="reveal"><span class="eyebrow {"cyan" if s in ("scada-simulator","ot-attack-scenarios") else ""}">{sub}</span><h2>{n}</h2><p class="lead">{t}</p><div class="btn-row"><a class="btn btn-ghost" href="{url(d, "products/"+s+"/")}">Learn more {icon("arrow")}</a>{primary}</div></div>{vis}</div>'''
    body = hero + f'<section class="section"><div class="container">{out}</div></section>' + cta_band(d, "Want to evaluate a platform?", "Request a free XFSA trial, a SafeMind or Xploit GRC Proof of Concept, or a SCADA Simulator demo.", ("Contact Xploit", "contact/?type=poc"))
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": "Xploit Security products",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": abs_url(f"products/{s}/")} for i, (s, n, _, _, _) in enumerate(PRODUCTS)]}
    return path, page(d, path, "Products: SafeMind, Xploit GRC, SCADA Simulator",
                      "Xploit Security products: SafeMind awareness SaaS, Xploit GRC, Xploit Firewall Security Analyzer, the SCADA Simulator OT cyber range, and free OT attack scenarios.",
                      body, "sp", ld, crumbs, keywords="Cybersecurity GRC Software, Cybersecurity Awareness SaaS, SCADA Simulator, OT cyber range, security products")

ALL = [products_hub, safemind, grc, scenarios, scada]
