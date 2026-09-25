(() => {
  const stories = window.RADAR_DEMOS;
  const $ = id => document.getElementById(id);
  let current = stories.find(s => '#'+s.id === location.hash) || stories[0];
  let playing = !matchMedia('(prefers-reduced-motion: reduce)').matches;
  function media(restart = false) {
    const suffix = playing ? '.gif' : '.png';
    $('demo-image').src = 'media/' + current.id + suffix + (restart && playing ? '?replay='+Date.now() : '');
    $('demo-image').alt = current.title + '. ' + current.badge + '. ' + current.takeaway;
    $('play').textContent = playing ? 'Pause animation' : 'Play animation';
    $('play').setAttribute('aria-pressed',String(playing));
  }
  function select(story) {
    current = story;
    history.replaceState(null,'','#'+story.id);
    [...$('story-tabs').children].forEach(button => {
      const active = button.dataset.id === story.id;
      button.classList.toggle('active',active);button.setAttribute('aria-current',active?'true':'false');
    });
    $('prompt').textContent = story.prompt;
    $('takeaway').textContent = story.takeaway;
    $('data-label').textContent = story.badge;
    $('data-label').className = 'data-label '+story.kind;
    $('data-note').textContent = story.footnote;
    $('duration').textContent = story.duration+' seconds · loops · 1280 × 800';
    $('guide').href = story.guide;
    $('download').href = 'media/'+story.id+'.gif';
    $('poster').href = 'media/'+story.id+'.png';
    $('full-size').href = 'media/'+story.id+'.gif';
    $('recipe').textContent = JSON.stringify(story.steps.map(step => step.type === 'radar' ? {name:step.name,arguments:{request:step.request}} : {client_action:step.label,detail:step.name}),null,2);
    $('copy-status').textContent = '';
    media();
  }
  for (const story of stories) {
    const button = document.createElement('button');
    button.type = 'button';button.className = 'story-tab';button.dataset.id = story.id;
    const label = document.createElement('span');label.textContent = story.nav;
    const note = document.createElement('small');note.textContent = story.kind === 'captured' ? 'Saved Radar data' : 'Illustrative sample data';
    button.append(label,note);button.addEventListener('click',() => select(story));$('story-tabs').append(button);
  }
  $('play').addEventListener('click',() => {playing=!playing;media(true);});
  $('replay').addEventListener('click',() => {playing=true;media(true);});
  $('copy-prompt').addEventListener('click',async () => {
    $('copy-status').textContent='Copying prompt…';
    let timeout;
    try {
      await Promise.race([navigator.clipboard.writeText(current.prompt),new Promise((_,reject)=>{timeout=setTimeout(()=>reject(new Error('Clipboard unavailable')),1000);})]);
      $('copy-status').textContent='Prompt copied';
    }
    catch {const selection=window.getSelection();const range=document.createRange();range.selectNodeContents($('prompt'));selection.removeAllRanges();selection.addRange(range);$('copy-status').textContent='Prompt selected; copy it with your keyboard.';}
    finally {clearTimeout(timeout);}
  });
  matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change',event => {if(event.matches){playing=false;media();}});
  select(current);
})();
