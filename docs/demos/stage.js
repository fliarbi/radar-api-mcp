/* Deterministic, source-qualified animation frames. No network requests. */
(() => {
  const h = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const clamp = n => Math.max(0, Math.min(1, n));
  const ease = n => 1 - (1 - clamp(n)) ** 3;
  const colors = ['#285ad9','#137f82','#77539b','#c27722','#b54747'];
  const usd = value => value == null ? 'Not returned' : `${value < 0 ? '−' : ''}$${Math.abs(value/1e6).toLocaleString('en-US',{maximumFractionDigits:3})}M`;
  const pct = value => `${value < 0 ? '−' : ''}${Math.abs(value).toFixed(2)}%`;
  const svg = (body, w=1120, ht=440, cls='chart') => `<svg class="${cls}" viewBox="0 0 ${w} ${ht}" role="img">${body}</svg>`;
  const text = (x,y,value,cls='',anchor='start') => `<text x="${x}" y="${y}" class="${cls}" text-anchor="${anchor}">${h(value)}</text>`;
  const line = (x1,y1,x2,y2,cls='gridline') => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="${cls}"/>`;
  const pill = (value,cls='') => `<span class="tag ${cls}">${h(value)}</span>`;
  const cell = (main,sub='') => `<strong>${h(main)}</strong>${sub ? `<small>${h(sub)}</small>` : ''}`;
  const table = (headers,rows,widths=[]) => `<table class="results-table"><colgroup>${widths.map(w=>`<col style="width:${w}%">`).join('')}</colgroup><thead><tr>${headers.map(v=>`<th>${h(v)}</th>`).join('')}</tr></thead><tbody>${rows.map(row=>`<tr>${row.map(v=>`<td>${v}</td>`).join('')}</tr>`).join('')}</tbody></table>`;
  const note = value => `<div class="view-note">${h(value)}</div>`;
  let story = window.RADAR_DEMOS.find(s => s.id === new URLSearchParams(location.search).get('demo')) || window.RADAR_DEMOS[0];

  function peers(s,p,detail) {
    if(detail) return {title:'Five payment companies, side by side',subtitle:'Company domains, recorded stages, locations and complete product descriptions',body:table(['Company','Stage','Location','Recorded product focus'],s.rows.map(r=>[cell(r.name,r.domain),pill(r.stage),h(r.city),h(r.description)]),[22,14,18,46])};
    const groups=['Seed','Series A','Series B'].map(stage=>({stage,rows:s.rows.filter(r=>r.stage===stage)}));
    let x=0;
    const segments=groups.map((g,i)=>{const w=g.rows.length/s.rows.length*1120; const start=x; x+=w; return `<rect x="${start}" y="0" width="${w*p}" height="64" fill="${colors[i]}"/>`+text(start+w/2,42,`${g.rows.length} ${g.rows.length===1?'company':'companies'}`,'white','middle');}).join('');
    return {title:'A payments landscape you can inspect',subtitle:'Distribution of the five selected peer cards by their recorded funding stage',body:`<div class="distribution">${svg(segments,1120,64)}</div><div class="stage-groups">${groups.map((g,i)=>`<section><h3 style="color:${colors[i]}">${h(g.stage)}</h3>${g.rows.map(r=>`<div class="peer-name">${h(r.name)}<span>${h(r.city)}</span></div>`).join('')}</section>`).join('')}</div>${note('Selected sample: 5 of 15 captured cards. The stage mix is not a market-share estimate.')}`};
  }

  function finance(s,p,detail) {
    const margins=s.rows.map(r=>r.metrics.net_income.value/r.metrics.revenue.value*100);
    if(detail) {
      const defs=[['Revenue','revenue'],['Net income','net_income'],['Operating income','operating_income'],['EBITDA','ebitda'],['Earnings per share','eps']];
      const rows=defs.map(([label,key])=>[h(label),...s.rows.map(r=>{
        const metric=r.metrics[key];
        return metric ? `<span class="number ${metric.value<0?'loss':''}">${key==='eps'?`${metric.value.toFixed(2)} / share`:usd(metric.value)}</span>` : '<span class="missing">Not returned</span>';
      })]);
      rows.push(['Net margin <small>Calculated: net income ÷ revenue</small>',...margins.map(v=>`<span class="number ${v<0?'loss':''}">${pct(v)}</span>`)]);
      return {title:'The full financial comparison',subtitle:'FY2025 labels · USD absolute metrics; EPS currency not supplied by source',body:table(['Metric','Qualys','Mastech Digital'],rows,[42,29,29])+note('Source type: news_report. Missing EBITDA and operating income remain missing, never zero.')};
    }
    let chart='';
    for(const tick of [0,200,400,600]) {const y=365-tick*.46;chart+=line(65,y,750,y)+text(45,y+7,`${tick}`,'axis','end');}
    chart+=text(750,26,'USD millions','axis','end');
    s.rows.forEach((r,i)=>{
      const cx=240+i*340;
      [['revenue',colors[0],-64],['net_income',colors[1],36]].forEach(([key,color,offset])=>{
        const value=r.metrics[key].value/1e6, height=Math.abs(value)*.46*p, y=value<0?365:365-height;
        chart+=`<rect x="${cx+offset-32}" y="${y}" width="64" height="${height}" rx="3" fill="${value<0?colors[4]:color}"/>`;
        chart+=`<g opacity="${clamp((p-.55)/.45)}">`+text(cx+offset,value<0?400:y-16,usd(r.metrics[key].value),`value ${value<0?'red':''}`,'middle')+'</g>';
      });
      chart+=text(cx-14,443,r.name,'company-axis','middle');
    });
    return {title:'Revenue and profit, on the same scale',subtitle:'Qualys and Mastech Digital · saved FY2025 observations',body:`<div class="finance-overview"><div><div class="legend"><span><i style="background:${colors[0]}"></i>Revenue</span><span><i style="background:${colors[1]}"></i>Net income</span></div>${svg(chart,790,470)}</div><aside class="metric-rail"><h3>Net margin</h3>${s.rows.map((r,i)=>`<div class="rail-metric"><span>${h(r.name)}</span><strong class="${margins[i]<0?'loss':''}">${pct(margins[i])}</strong></div>`).join('')}<p>Calculated from the returned revenue and net income.</p><p class="loss">Mastech reports a $0.609M loss.</p></aside></div>`};
  }

  function founder(s,p,detail) {
    const person=s.person;
    if(detail) return {title:`${person.name}: the recorded profile`,subtitle:'Expand the professional record while keeping ambiguous identity matches visible',body:`<div class="profile-details"><section><h3>Education</h3>${person.education.map(r=>`<div class="education-row">${cell(r.institution,[r.degree,r.years].filter(Boolean).join(' · ') || 'Dates and degree not supplied')}</div>`).join('')}<p class="subtle">Unknown start years stay unknown; source labels are retained.</p></section><section><h3>Recorded skills</h3><div class="skill-cloud">${person.skills.map(v=>pill(v)).join('')}</div><div class="unresolved"><h3>${h(s.unresolved)}</h3><p>No professional match in the saved lookup. LinkedIn remains unresolved.</p></div></section></div><div class="linkedin-wide"><b>LinkedIn</b><span>${h(person.linkedin_url)}</span></div>`};
    const connectors=svg(`<path d="M 370 245 H 570 M 570 80 V 410 M 570 80 H 700 M 570 245 H 700 M 570 410 H 700" fill="none" stroke="#bdd0e3" stroke-width="3" stroke-dasharray="1600" stroke-dashoffset="${1600*(1-p)}"/>`,1120,490,'profile-wires');
    return {title:'A founder profile, connected to its evidence',subtitle:'Recorded Razorpay affiliation · identity and current role are not independently verified',body:`<div class="profile-map">${connectors}<section class="person-node"><span class="person-initials">SK</span><h3>${h(person.name)}</h3><p>${h(person.current_title)} at ${h(person.current_company)}</p><span>${h(person.current_company_domain)}</span></section><div class="profile-node location-node"><span>Recorded location</span><strong>${h(person.location)}</strong></div><div class="profile-node education-node"><span>Education</span><strong>IIT Roorkee</strong><p>${h(person.education[0].degree)} · source end year 2012</p></div><div class="profile-node link-node"><span>LinkedIn profile from source</span><strong>linkedin.com/in/kumarshashank</strong></div></div>`};
  }

  function startups(s,p,detail) {
    if(detail) return {title:'Your GenAI company shortlist',subtitle:'Five fictional examples showing the fields returned to your research UI',body:table(['Company','Founded','US location','Product focus'],s.rows.map(r=>[cell(r[0],r[1]),h(r[2]),h(r[3]),h(r[4])]),[29,12,24,35])+note('Open classification, founders, technology and funding in separate field requests.')};
    let chart='';
    const x=year=>430+(Number(year)-2021)*208;
    [2021,2022,2023,2024].forEach(year=>{chart+=line(x(year),45,x(year),411)+text(x(year),449,year,'axis','middle');});
    s.rows.forEach((r,i)=>{const y=75+i*76;chart+=text(0,y-3,r[0],'company-axis')+text(0,y+24,r[4],'axis')+line(390,y,x(r[2]),y,'connector')+`<circle cx="${x(r[2])}" cy="${y}" r="${12*p}" fill="${colors[i]}"/>`;});
    return {title:'Five product directions in generative AI',subtitle:'Founding-year dot plot · US startups founded since 2021 · illustrative cohort',body:`${svg(chart,1120,475)}${note('Each dot is one fictional company. Position shows founding year, not growth or investment quality.')}`};
  }

  function funding(s,p,detail) {
    const rows=[...s.rows].sort((a,b)=>parseInt(a[2])-parseInt(b[2]));
    const amount=r=>Number(r[4].replace(/[$M]/g,''));
    const total=rows.reduce((n,r)=>n+amount(r),0);
    if(detail) return {title:'The April funding ledger',subtitle:'Illustrative announcements, with round amount and publication date kept separate',body:table(['Company','Published in 2026','Round','Amount'],s.rows.map(r=>[cell(r[0],r[1]),h(r[2]),pill(r[3]),`<span class="number">${h(r[4])}</span>`]),[38,24,18,20])+`<div class="funding-summary"><div><strong>$${total.toFixed(1)}M</strong><span>Sum of these four fictional rounds</span></div><div><strong>1–30 April</strong><span>Publication dates, not transaction closing dates</span></div></div>`};
    const x=day=>70+(day-1)*35;
    let chart='';
    chart+=line(55,180,1100,180,'timeline-axis');
    [1,10,20,30].forEach(day=>{chart+=line(x(day),171,x(day),190,'timeline-axis')+text(x(day),215,`${day} Apr`,'axis','middle');});
    rows.forEach((r,i)=>{const day=parseInt(r[2]), above=i%2===0, y=above?87:314; const xx=x(day);chart+=line(xx,180,xx,above?y+20:y-20,'connector')+`<circle cx="${xx}" cy="180" r="${12*p}" fill="${r[3]==='Seed'?colors[1]:colors[0]}"/>`+text(xx,y,r[4],'funding-amount','middle')+text(xx,above?y-36:y+38,r[0],'funding-name','middle')+text(xx,above?y+47:y+69,`${r[2]} · ${r[3]}`,'axis','middle');});
    return {title:'San Francisco funding through April 2026',subtitle:'Four fictional announcements across a fixed publication window',body:`<div class="legend"><span><i style="background:${colors[0]}"></i>Series A</span><span><i style="background:${colors[1]}"></i>Seed</span><span class="legend-right">City checked separately from funding news</span></div>${svg(chart,1120,445)}${note('Filter exact San Francisco city after reading geography. A Bay Area mention is not a city match.')}`};
  }

  function apps(s,p,detail) {
    if(detail) {
      const l=s.legal;
      return {title:'From a ranked app to a legal record',subtitle:'Selected example: Demo Orbit · illustrative developer-to-company association',body:`<div class="legal-join"><section><span class="join-label">App result</span><h3>Demo Orbit</h3><strong class="big-number">54.2M</strong><p>Stored Google Play installs</p><div class="app-domain">${h(s.rows[0][1])}</div></section><div class="join-arrow">→</div><section><span class="join-label">Developer field</span><h3>${h(l.developer)}</h3><p>Website: ${h(l.domain)}</p><div class="association">Website match<br>Ownership unverified</div></section><div class="join-arrow">→</div><section><span class="join-label">Company legal field</span><h3>${h(l.company)}</h3><dl><dt>Jurisdiction</dt><dd>${h(l.jurisdiction)}</dd><dt>Registry reference</dt><dd>${h(l.registry)}</dd></dl></section></div>${note('Read the developer and legal fields separately. Keep uncertain or missing company joins visible.')}`};
    }
    const max=60;
    let chart='';
    [0,20,40,60].forEach(n=>{const x=315+n/60*710;chart+=line(x,10,x,435)+text(x,471,`${n}M`,'axis','middle');});
    s.rows.forEach((r,i)=>{const y=28+i*43, length=r[2]/1e6/max*710*p;chart+=text(0,y+7,String(i+1).padStart(2,'0'),'rank')+text(48,y+7,r[0],'app-name')+`<line x1="315" y1="${y}" x2="${315+length}" y2="${y}" stroke="${i===0?colors[0]:'#b9ccf0'}" stroke-width="12" stroke-linecap="round"/><circle cx="${315+length}" cy="${y}" r="8" fill="${i===0?colors[0]:'#7299d8'}"/>`+text(340+length,y+7,`${(r[2]/1e6).toFixed(1)}M`,'app-value');});
    return {title:'Top 10 apps by recorded installs',subtitle:'Illustrative Google Play Dating cohort · all ten ranks on one screen',body:svg(chart,1120,490)};
  }

  function excel(s,p,detail) {
    if(detail) return {title:'A workbook that keeps contact provenance',subtitle:'Preview of a client-created Excel export; synthetic records only',body:`<div class="sheet-heading"><span class="excel-symbol">X</span><b>${h(s.filename)}</b><span>Illustrated save</span></div>${table(['Founder','Company','Email','Contact source'],s.rows.map(r=>[h(r[0]),h(r[1]),r[2]?`<span class="email">${h(r[2])}</span>`:'<span class="missing">Not returned</span>',h(r[3])]),[23,23,29,25])}<div class="export-detail"><strong>3 rows retained</strong><span>Person email, company mailbox and missing email stay distinct.</span></div>${note('The agent writes the workbook locally. Radar has no Excel-export or message-sending endpoint.')}`};
    const circumference=2*Math.PI*138;
    let ring='';
    const labels=['Person record email','Company mailbox','No email returned'];
    for(let i=0;i<3;i++)ring+=`<circle cx="240" cy="224" r="138" fill="none" stroke="${colors[i]}" stroke-width="42" stroke-dasharray="${(circumference/3-6)*p} ${circumference}" stroke-dashoffset="${-i*circumference/3}" transform="rotate(-90 240 224)"/>`;
    ring+=text(240,224,'3','donut-total','middle')+text(240,265,'founder rows','axis','middle');
    return {title:'What the contact export actually contains',subtitle:'Three synthetic rows, with fallback and missing-data status preserved',body:`<div class="contact-overview">${svg(ring,480,450)}<section class="contact-legend">${labels.map((label,i)=>`<div><i style="background:${colors[i]}"></i><strong>1</strong><span>${label}</span></div>`).join('')}<p>A company mailbox is not a founder’s personal email. Missing rows remain in the export.</p><span class="scope-label">Contacts scope + paid linked plan required</span></section></div>`};
  }

  const views={peers,finance,founder,startups,funding,apps,excel};
  const titles={peers:'Research your competitive landscape',finance:'Compare company financials',founder:'Explore founder profiles',startups:'Find your next company shortlist',funding:'Research funding as of a date',apps:'Explore apps and their companies',excel:'Build a founder contact workbook'};
  function render(t) {
    const time=Math.max(0,Math.min(story.duration,t)), s=story;
    const exit=ease((time-6.4)/1.1), enter=ease((time-6.8)/.9);
    const detail=time>=18.5, change=ease((time-18.5)/.75);
    const reveal=detail?change:enter;
    const chartProgress=ease((time-(detail?19:7.5))/1.4);
    const result=views[s.view](s,chartProgress,detail);
    const typed=s.prompt.slice(0,Math.floor(s.prompt.length*clamp((time-.65)/4.2)));
    const phase=time<6.4?'Prompt':detail?'Details':'Results';
    document.getElementById('stage').innerHTML=`<header class="film-top"><div class="brand"><span class="radar-mark"></span><b>Radar</b><span>${h(s.client)} + MCP</span></div><span class="provenance ${s.kind}">${h(s.badge)}</span></header><section class="search-scene" aria-hidden="${exit===1}" style="transform:translateX(${-1450*exit}px);opacity:${1-exit}"><div class="search-caption">Ask a question. Explore the evidence.</div><h1>${h(titles[s.view])}</h1><div class="search-box"><span class="search-icon"></span><div class="prompt-text">${typed?h(typed):'<span class="placeholder">Describe your research…</span>'}<span class="type-cursor" style="opacity:${time<5.2?(Math.floor(time*2.5)%2?0:1):0}"></span></div><div class="submit-arrow">↵</div></div><div class="search-hint">${time<4.9?'One prompt, connected company intelligence.':'Turn the request into a full research view.'}</div></section><section class="result-scene" aria-hidden="${time<6.8}" style="transform:translateX(${(1-enter)*1280}px);opacity:${enter}"><div class="result-heading"><div><h2>${h(result.title)}</h2><p>${h(result.subtitle)}</p></div><span class="view-count">${detail?'2 / 2':'1 / 2'}</span></div><div class="full-result" style="opacity:${reveal};transform:translateY(${detail?(1-change)*24:0}px)">${result.body}</div><div class="source-footer">${h(s.footnote)}</div></section><footer class="film-bottom"><span>Concept UI · ${s.kind==='captured'?'saved Radar responses':'illustrative data'} · no live requests</span><span>${phase}</span><div class="film-progress" style="width:${time/s.duration*100}%"></div></footer>`;
    document.documentElement.dataset.demo=s.id;
    document.documentElement.dataset.frameTime=time;
    document.documentElement.dataset.phase=time<6.4?'prompt':time<7.7?'transition':detail?'detail':'overview';
  }
  window.setDemo=id=>{story=window.RADAR_DEMOS.find(s=>s.id===id);if(!story)throw new Error('Unknown demo');render(0);};
  window.renderFrame=render;
  window.getDemo=()=>story;
  render(Number(new URLSearchParams(location.search).get('t')||0));
})();
