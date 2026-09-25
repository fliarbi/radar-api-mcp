/* Deterministic UI animation: source-qualified data only; no requests or tracking. */
(() => {
  const h = (value) => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  const clamp = (n) => Math.max(0, Math.min(1, n));
  const money = n => n == null ? '<span class="missing">Not reported</span>' : `<span class="${n < 0 ? 'negative' : ''}">${n < 0 ? '−' : ''}$${Math.abs(n / 1000000).toLocaleString('en-US', {maximumFractionDigits: 3})}M</span>`;
  const rowStyle = (time, i) => `style="opacity:${clamp((time - 4.6 - i * .14) / .28)}"`;
  let story = window.RADAR_DEMOS.find(s => s.id === new URLSearchParams(location.search).get('demo')) || window.RADAR_DEMOS[0];
  let time = 0;
  const table = (heads, body, cls = '', widths = []) => `<table class="data-table ${cls}"><colgroup>${widths.map(w => `<col style="width:${w}%">`).join('')}</colgroup><thead><tr>${heads.map(x => `<th>${h(x)}</th>`).join('')}</tr></thead><tbody>${body}</tbody></table>`;

  function peers(s, t) {
    const body = s.rows.map((r, i) => `<tr ${rowStyle(t, i)} class="${t > 10 && [0,4].includes(i) ? 'selected' : ''}"><td class="name">${h(r.name)}<span class="secondary-line">${h(r.domain)}</span></td><td><span class="stage-tag">${h(r.stage)}</span></td><td>${h(r.city)}</td><td><span class="description">${h(r.description)}</span></td></tr>`).join('');
    return table(['Company', 'Stage', 'Location', 'Recorded focus'], body, '', [23,13,19,45]);
  }
  function finance(s, t) {
    const max = Math.max(...s.rows.map(r => r.metrics.revenue.value));
    const charts = s.rows.map(r => `<div class="revenue-item"><div class="bar-heading"><span>${h(r.name)} revenue</span><strong>${money(r.metrics.revenue.value)}</strong></div><div class="bar-track"><div class="bar" style="width:${100 * r.metrics.revenue.value / max * clamp((t - 4.8) / 1.2)}%"></div></div></div>`).join('');
    const rows = [['Revenue','revenue'],['Net income','net_income'],['EBITDA','ebitda']].map(([label,key],i) => `<tr ${rowStyle(t,i)}><td class="name">${label}</td>${s.rows.map(r => `<td>${money(r.metrics[key]?.value)}</td>`).join('')}</tr>`).join('');
    return `<div class="revenue-chart">${charts}</div>` + table(['Metric · USD', 'Qualys', 'Mastech Digital'], rows, 'finance-table', [34,33,33]) + `<div class="source-strip"><span><b>Period:</b> FY2025 for both</span><span class="source-label">news_report</span><span><b>End dates:</b> unavailable</span></div><div class="insight" style="opacity:${clamp((t - 10) / .4)}">Missing EBITDA stays blank. A reported loss remains a negative number.</div>`;
  }
  function founder(s,t) {
    const p = s.person;
    return `<div class="founder-layout"><article class="dossier"><div class="person-header"><div class="avatar">SK</div><div><h3>${h(p.name)}</h3><p>${h(p.current_title)} at ${h(p.current_company)}</p></div></div><div class="profile-link"><span class="in-mark">in</span>${h(p.linkedin_url.replace('https://',''))}</div><div class="detail-label">Recorded location</div><div class="detail-value">${h(p.location)}</div><div class="detail-label">Education</div><div class="detail-value">${h(p.education[0].institution)}<span class="secondary-line">${h(p.education[0].degree)}</span></div><div class="skills">${p.skills.slice(0,4).map(v => `<span>${h(v)}</span>`).join('')}</div></article><aside class="identity-check"><h3>Match evidence</h3><div class="check-line">Name + company-domain lookup</div><div class="check-line">Recorded company domain<br><b>${h(p.current_company_domain)}</b></div><div>LinkedIn URL supplied by the source record</div><div class="unresolved" style="opacity:${clamp((t - 10) / .4)}"><b>${h(s.unresolved)}</b>No professional match in the captured lookup. No link guessed.</div></aside></div>`;
  }
  function startups(s,t) {
    return `<div class="chips"><span class="small-chip blue">Generative AI candidates</span><span class="small-chip">US location</span><span class="small-chip">Founded 2021 onward</span></div>` + table(['Company', 'Founded', 'Location', 'Product focus'], s.rows.map((r,i) => `<tr ${rowStyle(t,i)}><td class="name">${h(r[0])}<span class="secondary-line">${h(r[1])}</span></td><td class="year">${h(r[2])}</td><td class="geography-tag">${h(r[3])}</td><td>${h(r[4])}</td></tr>`).join(''),'startup-table',[29,12,25,34]);
  }
  function funding(s,t) {
    return `<div class="funding-window"><div><span>Announcement dates</span><br><strong>01 Apr – 30 Apr 2026</strong></div><div><span>Company location check</span><br><strong>San Francisco city</strong></div></div>` + table(['Company', 'Published', 'Round', 'Amount'], s.rows.map((r,i) => `<tr ${rowStyle(t,i)}><td class="name">${h(r[0])}<span class="secondary-line">${h(r[1])}</span></td><td class="date">${h(r[2])} 2026</td><td><span class="stage-tag">${h(r[3])}</span></td><td class="money">${h(r[4])}</td></tr>`).join(''),'funding-table',[37,23,21,19]);
  }
  function apps(s,t) {
    const rows = s.rows.map((r,i) => `<tr ${rowStyle(t,i)} class="${i === 0 && t > 8 ? 'selected' : ''}"><td>${i+1}</td><td>${h(r[0])}</td><td>${(r[2]/1000000).toFixed(1)}M</td></tr>`).join('');
    const l = s.legal;
    return `<div class="apps-layout"><div>${table(['#','App','Installs'],rows,'apps-table',[9,59,32])}<div class="demo-only">10 fictional apps · descending stored installs</div></div><aside class="legal-panel" style="opacity:${clamp((t-8)/.5)}"><span class="legal-eyebrow">Selected app · illustrative legal record</span><h3>${h(l.company)}</h3><dl>${[['Developer',l.developer],['Company domain',l.domain],['Jurisdiction',l.jurisdiction],['Registry reference',l.registry]].map(([k,v]) => `<div class="legal-field"><dt>${h(k)}</dt><dd>${h(v)}</dd></div>`).join('')}</dl><div class="join-path">App → developer website → company legal field<br>Ownership link still needs review.</div></aside></div>`;
  }
  function excel(s,t) {
    const rows = s.rows.map((r,i) => `<tr ${rowStyle(t,i)}><td>${i+2}</td><td>${h(r[0])}</td><td>${h(r[1])}</td><td class="email">${r[2] ? h(r[2]) : '<span class="missing">Not returned</span>'}</td><td>${h(r[3])}</td></tr>`).join('');
    const exported = t > 10;
    return `<div class="worksheet-bar"><span class="excel-icon">X</span><b>Founders</b><small>Preview of a local workbook</small></div>` + table(['','A · Founder','B · Company','C · Email','D · Source'],rows,'sheet-table',[5,23,22,27,23]) + (exported ? `<div class="export-card" style="opacity:${clamp((t-10)/.5)}"><div><h3 class="code">${h(s.filename)}</h3><p>3 demo rows · source labels retained · no messages sent</p></div><span class="export-status">Illustrated save</span></div>` : '<div class="export-before">Retain the missing email row. Mark the company mailbox separately.</div>') + '<div class="demo-only">Reserved example addresses only. The Excel file is written by the client, not Radar.</div>';
  }
  const views = {peers,finance,founder,startups,funding,apps,excel};
  function render(t) {
    time = Math.max(0, Math.min(story.duration, t));
    const s = story;
    const typed = s.prompt.slice(0, Math.floor(s.prompt.length * clamp(time / 2.6)));
    const ready = time >= 4.6;
    const steps = s.steps.map((step,i) => {
      const start = 2.7 + i * .58;
      const done = time >= start + .54;
      const active = time >= start && !done;
      return `<div class="tool-row ${done ? 'done' : active ? 'active' : 'pending'}"><span class="tool-dot">${done ? '✓' : ''}</span><div><div class="tool-label">${h(step.label)}</div><div class="tool-code ${step.type === 'client' ? 'local-code' : 'code'}">${h(step.name)}</div></div></div>`;
    }).join('');
    document.getElementById('stage').innerHTML = `<header class="topbar"><span class="radar-mark"></span><span class="wordmark">Radar</span><span class="top-divider"></span><span class="top-name">Company intelligence workspace</span><span class="client">${h(s.client)} + Radar MCP</span><span class="concept">Concept UI</span></header><div class="story-heading"><h1>${h(s.title)}</h1><div class="story-meta"><p>Write a request. Let connected tools shape the research view.</p><span class="provenance ${s.kind}">${h(s.badge)}</span></div></div><div class="desk"><aside class="request-pane"><div class="pane-title">Your request <span>Natural language</span></div><div class="prompt">${h(typed)}<span class="cursor" style="opacity:${Math.floor(time*2)%2 ? 0 : 1}"></span></div><div class="tool-heading">${ready ? 'Illustrated tool sequence' : 'Tools that power this view'}</div>${steps}<div class="read-label">Animation only · no live API calls</div></aside><section class="result-pane"><div class="result-header"><h2>${h(s.result_title)}</h2><p>${h(s.result_subtitle)}</p></div>${ready ? `<div class="result-content">${views[s.view](s,time)}</div>` : `<div class="loading"><div class="loading-caption"><span class="loader-orbit" style="transform:rotate(${time*160}deg)"></span>${time < 2.7 ? 'Start with the question you want answered' : 'Building the illustrated result view'}</div><div class="skeleton"></div><div class="skeleton"></div><div class="skeleton"></div><div class="skeleton"></div></div>`}<div class="result-footnote">${h(s.footnote)}</div></section></div><footer class="stage-bottom"><p class="takeaway">${time < 4.6 ? 'One prompt can combine multiple focused Radar reads into a useful research surface.' : h(s.takeaway)}</p><div class="phase-line"><span class="${time < 2.7 ? 'on' : ''}">Write the prompt</span><span class="${time >= 2.7 && time < 4.6 ? 'on' : ''}">Use connected tools</span><span class="${time >= 4.6 && time < 10 ? 'on' : ''}">Inspect the results</span><span class="${time >= 10 ? 'on' : ''}">Keep the evidence</span></div><div class="timeline"><div style="width:${time/s.duration*100}%"></div></div></footer>`;
    document.documentElement.dataset.demo = s.id;
    document.documentElement.dataset.frameTime = time;
  }
  window.setDemo = id => {story = window.RADAR_DEMOS.find(s => s.id === id); if (!story) throw new Error('Unknown demo'); render(0);};
  window.renderFrame = render;
  window.getDemo = () => story;
  render(Number(new URLSearchParams(location.search).get('t') || 0));
})();
