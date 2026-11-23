# Xploit Security: Corporate Website

**Securing IT. Protecting OT. Enabling Trust.**

The static corporate website for **Xploit Security** (xploit-security.com), the cybersecurity services and products arm of the Xploit family. It is plain HTML, CSS and JavaScript, built for **GitHub Pages**, with no server, no framework and no build step needed to deploy.

---

## 1. What's in the repository

```
/                          ← GitHub Pages serves this folder (repo root)
├── index.html             Home
├── services/              index.html (hub) + one folder per service
│   ├── cybersecurity-consulting/   vciso/   it-cybersecurity/
│   └── ot-industrial-cybersecurity/   compliance-risk-management/   security-assessments-audits/
├── products/              index.html (hub) + one folder per product
│   └── safemind/   xploit-grc/   firewall-security-analyzer/   ot-attack-scenarios/   scada-simulator/
├── about/  faq/  contact/ each contains index.html
├── 404.html               Custom not-found page (served automatically by GitHub Pages)
├── assets/                css/, js/, fonts/, img/ (brand, products, clients)
├── CNAME  .nojekyll  sitemap.xml  robots.txt  site.webmanifest  favicon.ico
└── tools/                 Generator + QA scripts (not needed by the live site)
```

Each page lives in its own folder, giving clean public URLs such as `xploit-security.com/services/vciso/`. Internal links point directly to each folder's `index.html`, so the site works on GitHub Pages, from a project URL (`username.github.io/repo/`), and when you double-click `index.html` on your computer. The contact form only sends when the site is opened over http/https, not from a local file.

---

## 2. Edit content

The HTML files are **generated**. To change text, navigation or footer:

1. Edit the relevant `tools/pages_*.py` file (content) or `tools/lib.py` (header, mega menu, footer, contact details, SEO template).
2. Rebuild:
   ```bash
   python3 tools/build.py      # requires Python 3.8+, no packages
   python3 tools/check.py      # optional QA: exits non-zero on any broken link or metadata issue
   ```
3. Commit the regenerated files.

Contact details, domain and the form endpoint live in one place, `SITE = {...}` at the top of `tools/lib.py`.

> Quick edits: you *can* edit an `index.html` directly, but the next `build.py` run will overwrite it. Prefer editing the Python source.

**Preview locally**
```bash
python3 -m http.server 8000     # then open http://localhost:8000
```

---

## 3. Deploy on GitHub Pages

1. Create a repository (e.g. `xploit-security-website`) and push the contents of this folder to the `main` branch, root level.
2. In GitHub, go to **Settings → Pages → Build and deployment**, set **Source: Deploy from a branch**, **Branch: `main` / `(root)`**, then **Save**.
3. **Custom domain:** the `CNAME` file already contains `xploit-security.com`. In **Settings → Pages → Custom domain**, enter `xploit-security.com` and save.
4. **DNS** at your domain registrar:

   | Type  | Host | Value |
   |-------|------|-------|
   | A     | @    | 185.199.108.153 |
   | A     | @    | 185.199.109.153 |
   | A     | @    | 185.199.110.153 |
   | A     | @    | 185.199.111.153 |
   | AAAA  | @    | 2606:50c0:8000::153 |
   | AAAA  | @    | 2606:50c0:8001::153 |
   | AAAA  | @    | 2606:50c0:8002::153 |
   | AAAA  | @    | 2606:50c0:8003::153 |
   | CNAME | www  | `<your-github-username>.github.io` |

   Check these values against GitHub's current documentation ("Managing a custom domain for your GitHub Pages site") before you apply them.
5. Once DNS resolves (minutes to a few hours), tick **Enforce HTTPS** in Settings → Pages.
6. Recommended: verify the domain in your GitHub account settings (**Settings → Pages → Verified domains**) to prevent domain takeover.

If you ever use a different domain, update `SITE["domain"]` in `tools/lib.py` (canonical URLs, Open Graph, sitemap and JSON-LD all derive from it) and rebuild.

---

## 4. Contact form: integration (required one-time step)

GitHub Pages can't run server code, so the form posts to **[FormSubmit](https://formsubmit.co)**, a free form-to-email service, using its AJAX endpoint:

```
https://formsubmit.co/ajax/00a61be3578636a903da694c5b5a7a41   ← private alias for hello@xploit-security.com
```

**One-time activation:** click **Activate Form** in the FormSubmit email sent to `hello@xploit-security.com`. Until then, the form tells visitors it is awaiting activation and offers email/WhatsApp. After activation, every submission arrives in that inbox as a formatted table, with the visitor's email set as **Reply-To**. The endpoint already uses FormSubmit's private alias, so your address isn't exposed in the page source.

**What the form sends:** inquiry type (Sales / Product demo / Consulting / General), name, business email, company, country, service or product of interest, inquiry details and consent. A honeypot field (`_honey`) filters bots.

**Behaviour:** submissions are sent with `fetch()`. Success is shown only when FormSubmit confirms delivery. If the request fails, the visitor sees a clear error with a pre-filled `mailto:` link and WhatsApp, so no inquiry is silently lost.

**Deep links:** pre-select the form from any CTA:
- `/contact/?type=demo&interest=xploit-grc`
- `/contact/?type=consulting&interest=vciso`
- `type`: `demo`, `consulting`, `sales`, `general`
- `interest`: any service/product slug (e.g. `safemind`, `scada-simulator`, `compliance-risk-management`)

**Alternatives** (swap `SITE["form_endpoint"]`; the JS posts JSON and expects `{ "success": true }`):
- **Web3Forms**: `https://api.web3forms.com/submit`. Add a hidden `access_key` input in `pages_company.py`.
- **Formspree**: `https://formspree.io/f/<id>`. Returns `{ "ok": true }`, so change the success check in `assets/js/main.js` accordingly.

---

## 5. SEO

Every page has a unique `<title>`, meta description, canonical URL (`https://xploit-security.com/...`), Open Graph and Twitter/X card tags, and JSON-LD structured data:
- `Organization` on all pages, `BreadcrumbList` on inner pages
- `Service` on service pages, `SoftwareApplication` (with offers) on product pages
- `FAQPage` on the FAQ, `ItemList` on hub pages, `WebSite` on the homepage

After launch:
1. Add the site to **Google Search Console** and **Bing Webmaster Tools** and submit `https://xploit-security.com/sitemap.xml`.
2. Use the OG image (`assets/img/brand/og-image.png`, 1200×630) when sharing on LinkedIn. Test with LinkedIn Post Inspector.

---

## 6. Cross-linking with Xploit Academy

- **On this site:** "Training → Xploit Academy" appears in the header, the footer, the About and Contact pages, and links to https://www.xploitacademy.com/.
- **On Xploit Academy:** add a "Services → Xploit Security" link. A ready-to-paste snippet is in `brand-kit/academy-cross-link.html` (delivered alongside this repository).
- **Redirects from the old pages:** NewZenler pages can't send server-side 301s. On each old page (`/xploit-cyber-security-services`, `/safemind`, `/xploit-grc`, `/scada-simulator`), replace the content with a short notice and a link to the new URL. Where NewZenler allows custom head code, add `<link rel="canonical" href="https://xploit-security.com/...">` and/or a meta refresh. A mapping is included in the brand-kit snippet.

---

## 7. Accessibility & performance

- Semantic landmarks, skip link, visible focus states, keyboard-operable mega menu (Esc closes), ARIA on menus/tabs/status, descriptive alt text, `prefers-reduced-motion` respected.
- No frameworks; one CSS file and one ~8 KB JS file; self-hosted WOFF2 fonts with `font-display: swap`; WebP screenshots with explicit dimensions and lazy loading; YouTube embeds via `youtube-nocookie.com` with lazy loading.

---

## 8. Content notes

All service and product content was migrated from the existing Xploit pages (services, SafeMind, Xploit GRC, SCADA Simulator and the free OT Cyber Range). Statistics on the SafeMind page are attributed to their published sources (Verizon DBIR, IBM X-Force, SANS). Customer results are labelled as reported by SafeMind for one client. Client logos come from the existing services page. Review prices before publishing if they have changed.

© Xploit Cyber Security Services, registered in the United Arab Emirates.
