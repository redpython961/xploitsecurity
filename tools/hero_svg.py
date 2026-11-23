"""Hero illustration: enterprise IT (red) converging with industrial OT (cyan) behind a shared security core."""

HERO_SVG = r'''<svg viewBox="0 0 560 500" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="hv-t hv-d">
<title id="hv-t">IT and OT convergence</title>
<desc id="hv-d">Enterprise IT systems on the left and industrial OT systems on the right connect through a central Xploit security core.</desc>
<defs>
  <radialGradient id="core" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#ef0f0d" stop-opacity=".55"/><stop offset="1" stop-color="#ef0f0d" stop-opacity="0"/></radialGradient>
  <linearGradient id="panel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#151a24"/><stop offset="1" stop-color="#0b0e14"/></linearGradient>
  <linearGradient id="beamR" x1="0" x2="1"><stop offset="0" stop-color="#ef0f0d" stop-opacity=".1"/><stop offset="1" stop-color="#ef0f0d"/></linearGradient>
  <linearGradient id="beamC" x1="1" x2="0"><stop offset="0" stop-color="#22d3ee" stop-opacity=".1"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>
  <style>
    .ln{fill:none;stroke-width:1.6;stroke-dasharray:5 7;animation:flow 2.4s linear infinite}
    .lr{stroke:url(#beamR)} .lc{stroke:url(#beamC)}
    @keyframes flow{to{stroke-dashoffset:-48}}
    .pulse{animation:pulse 3s ease-in-out infinite;transform-origin:280px 250px}
    @keyframes pulse{0%,100%{opacity:.55;transform:scale(1)}50%{opacity:1;transform:scale(1.06)}}
    .blink{animation:blink 1.6s steps(2) infinite} @keyframes blink{50%{opacity:.2}}
    .lbl{font:600 10px 'JetBrains Mono',monospace;letter-spacing:.14em}
    .sub{font:500 9px 'JetBrains Mono',monospace;fill:#7d8696;letter-spacing:.03em}
    @media (prefers-reduced-motion: reduce){.ln,.pulse,.blink{animation:none}}
  </style>
</defs>
<!-- zone labels -->
<text x="20" y="28" class="lbl" fill="#ff3b30">ENTERPRISE IT</text>
<text x="540" y="28" class="lbl" fill="#22d3ee" text-anchor="end">INDUSTRIAL OT</text>
<line x1="20" y1="38" x2="160" y2="38" stroke="#ef0f0d" stroke-opacity=".4"/>
<line x1="400" y1="38" x2="540" y2="38" stroke="#22d3ee" stroke-opacity=".4"/>

<!-- IT side nodes -->
<g>
  <rect x="20" y="64" width="172" height="74" rx="12" fill="url(#panel)" stroke="#ef0f0d" stroke-opacity=".35"/>
  <path d="M44 90a10 10 0 0 1 19-4 8 8 0 0 1 12 7 7 7 0 0 1-2 14H45a9 9 0 0 1-1-17z" fill="none" stroke="#ff3b30" stroke-width="1.8"/>
  <text x="92" y="96" class="lbl" fill="#f3f5f8">CLOUD</text><text x="92" y="112" class="sub">AWS · AZURE · GCP</text>

  <rect x="20" y="158" width="172" height="74" rx="12" fill="url(#panel)" stroke="#ef0f0d" stroke-opacity=".35"/>
  <rect x="40" y="178" width="34" height="13" rx="3" fill="none" stroke="#ff3b30" stroke-width="1.8"/><rect x="40" y="196" width="34" height="13" rx="3" fill="none" stroke="#ff3b30" stroke-width="1.8"/>
  <circle cx="47" cy="184.5" r="1.6" fill="#22c55e" class="blink"/><circle cx="47" cy="202.5" r="1.6" fill="#22c55e"/>
  <text x="92" y="190" class="lbl" fill="#f3f5f8">DATA CENTER</text><text x="92" y="206" class="sub">SERVERS · AD · DB</text>

  <rect x="20" y="252" width="172" height="74" rx="12" fill="url(#panel)" stroke="#ef0f0d" stroke-opacity=".35"/>
  <rect x="40" y="272" width="30" height="22" rx="3" fill="none" stroke="#ff3b30" stroke-width="1.8"/><path d="M36 300h38" stroke="#ff3b30" stroke-width="1.8"/>
  <text x="92" y="284" class="lbl" fill="#f3f5f8">ENDPOINTS</text><text x="92" y="300" class="sub">USERS · EMAIL</text>

  <rect x="20" y="346" width="172" height="74" rx="12" fill="url(#panel)" stroke="#ef0f0d" stroke-opacity=".35"/>
  <path d="M40 368h30M40 378h30M40 388h20" stroke="#ff3b30" stroke-width="1.8"/><rect x="36" y="362" width="38" height="34" rx="3" fill="none" stroke="#ff3b30" stroke-opacity=".6"/>
  <text x="92" y="378" class="lbl" fill="#f3f5f8">APPLICATIONS</text><text x="92" y="394" class="sub">WEB · MOBILE</text>
</g>

<!-- OT side nodes -->
<g transform="translate(-22 0)">
  <rect x="390" y="64" width="172" height="74" rx="12" fill="url(#panel)" stroke="#22d3ee" stroke-opacity=".35"/>
  <rect x="410" y="80" width="40" height="28" rx="3" fill="none" stroke="#22d3ee" stroke-width="1.8"/><path d="M414 100l8-8 6 5 8-9 10 6" fill="none" stroke="#22d3ee" stroke-width="1.6"/>
  <text x="462" y="96" class="lbl" fill="#f3f5f8">SCADA</text><text x="462" y="112" class="sub">HMI · HISTORIAN</text>

  <rect x="390" y="158" width="172" height="74" rx="12" fill="url(#panel)" stroke="#22d3ee" stroke-opacity=".35"/>
  <rect x="410" y="174" width="40" height="40" rx="3" fill="none" stroke="#22d3ee" stroke-width="1.8"/><path d="M418 182h8M418 190h8M418 198h8M434 182v24" stroke="#22d3ee" stroke-width="1.6"/>
  <circle cx="443" cy="204" r="1.8" fill="#fbbf24" class="blink"/>
  <text x="462" y="190" class="lbl" fill="#f3f5f8">PLC / DCS</text><text x="462" y="206" class="sub">SIEMENS · ABB</text>

  <rect x="390" y="252" width="172" height="74" rx="12" fill="url(#panel)" stroke="#22d3ee" stroke-opacity=".35"/>
  <path d="M410 300v-20a10 10 0 0 1 20 0v20zM430 290h12v10h-12" fill="none" stroke="#22d3ee" stroke-width="1.8"/><circle cx="420" cy="288" r="3" fill="none" stroke="#22d3ee"/>
  <text x="462" y="284" class="lbl" fill="#f3f5f8">FIELD DEVICES</text><text x="462" y="300" class="sub">PUMPS · SENSORS</text>

  <rect x="390" y="346" width="172" height="74" rx="12" fill="url(#panel)" stroke="#22d3ee" stroke-opacity=".35"/>
  <path d="M420 398l10-34 10 34M423 386h14M418 398h24M430 364v-6" fill="none" stroke="#22d3ee" stroke-width="1.8"/>
  <text x="462" y="378" class="lbl" fill="#f3f5f8">UTILITIES</text><text x="462" y="394" class="sub">POWER · WATER</text>
</g>

<!-- connection beams -->
<path class="ln lr" d="M192 101 C220 101 220 230 250 240"/>
<path class="ln lr" d="M192 195 C215 195 225 240 250 246"/>
<path class="ln lr" d="M192 289 C215 289 225 258 250 254"/>
<path class="ln lr" d="M192 383 C220 383 220 270 250 260"/>
<path class="ln lc" d="M368 101 C340 101 340 230 310 240"/>
<path class="ln lc" d="M368 195 C345 195 335 240 310 246"/>
<path class="ln lc" d="M368 289 C345 289 335 258 310 254"/>
<path class="ln lc" d="M368 383 C340 383 340 270 310 260"/>

<!-- core -->
<circle cx="280" cy="250" r="92" fill="url(#core)" class="pulse"/>
<circle cx="280" cy="250" r="60" fill="#0b0e14" stroke="#ef0f0d" stroke-opacity=".55" stroke-width="1.5"/>
<circle cx="280" cy="250" r="72" fill="none" stroke="#ffffff" stroke-opacity=".08" stroke-dasharray="2 6"/>
<path d="M280 212l30 11v22c0 20-30 33-30 33s-30-13-30-33v-22z" fill="none" stroke="#f3f5f8" stroke-width="2"/>
<path d="M266 234l28 28M294 234l-28 28" stroke="#ef0f0d" stroke-width="5" stroke-linecap="round"/>
<circle cx="250" cy="226" r="3" fill="#22d3ee"/><circle cx="310" cy="276" r="3" fill="#fbbf24"/>

<!-- bottom status -->
<rect x="150" y="448" width="260" height="34" rx="17" fill="#0b0e14" stroke="#ffffff" stroke-opacity=".12"/>
<circle cx="172" cy="465" r="4" fill="#22c55e" class="blink"/>
<text x="186" y="469" class="lbl" fill="#b6bdc9">ONE PARTNER · IT + OT</text>
</svg>'''
