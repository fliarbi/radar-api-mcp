#!/usr/bin/env node
/* Node 22+, Chrome, FFmpeg. Uses local files and Chrome's debugging protocol only. */
import {spawn} from 'node:child_process';
import {mkdtemp, mkdir, readFile, writeFile, rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join, resolve, dirname} from 'node:path';
import {fileURLToPath, pathToFileURL} from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const value = flag => args.includes(flag) ? args[args.indexOf(flag)+1] : null;
const selected = value('--id');
const stills = args.includes('--stills');
const fps = Number(value('--fps') || 10);
const chrome = value('--chrome') || process.env.CHROME_BIN || '/usr/bin/google-chrome';
const ffmpeg = value('--ffmpeg') || process.env.FFMPEG_BIN || 'ffmpeg';
const stories = JSON.parse(await readFile(join(root, 'docs/demos/demo-data.json'), 'utf8')).filter(s => !selected || s.id === selected);
if (!stories.length || !Number.isInteger(fps) || fps < 5 || fps > 20) throw new Error('Invalid demo or frame rate');
const profile = await mkdtemp(join(tmpdir(), 'radar-demo-chrome-'));
const browser = spawn(chrome, ['--headless=new', '--no-sandbox', '--disable-dev-shm-usage', '--disable-background-networking', '--disable-component-update', '--disable-sync', '--no-first-run', '--disable-default-apps', '--remote-debugging-port=0', `--user-data-dir=${profile}`, 'about:blank'], {stdio:['ignore','ignore','pipe']});
let ws;
try {
  const endpoint = await new Promise((res, rej) => {
    let err = '';
    const timer = setTimeout(() => rej(new Error('Chrome startup timed out')), 15000);
    browser.stderr.on('data', data => {
      err += data.toString();
      const match = err.match(/DevTools listening on (ws:\/\/[^\s]+)/);
      if (match) {clearTimeout(timer); res(match[1]);}
    });
    browser.once('error', rej);
    browser.once('exit', code => {clearTimeout(timer); rej(new Error(`Chrome exited ${code}`));});
  });
  ws = new WebSocket(endpoint);
  await new Promise((res,rej) => {ws.addEventListener('open',res,{once:true});ws.addEventListener('error',rej,{once:true});});
  let nextId = 0;
  const pending = new Map();
  ws.addEventListener('message', event => {
    const data = JSON.parse(event.data);
    if (pending.has(data.id)) {
      const p = pending.get(data.id);pending.delete(data.id);clearTimeout(p.timer);
      if (data.error) p.reject(new Error(data.error.message)); else p.resolve(data.result);
    }
  });
  const send = (method, params = {}, sessionId = undefined) => new Promise((res,rej) => {
    const id = ++nextId;
    const timer = setTimeout(() => {pending.delete(id);rej(new Error(`Timed out: ${method}`));},30000);
    pending.set(id,{resolve:res,reject:rej,timer});
    ws.send(JSON.stringify({id,method,params,...(sessionId ? {sessionId} : {})}));
  });
  const {targetId} = await send('Target.createTarget',{url:'about:blank'});
  const {sessionId} = await send('Target.attachToTarget',{targetId,flatten:true});
  const call = (method,params) => send(method,params,sessionId);
  const evaluate = async expression => {
    const r = await call('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});
    if (r.exceptionDetails) throw new Error(r.exceptionDetails.text + ': ' + r.exceptionDetails.exception?.description);
    return r.result.value;
  };
  await call('Page.enable');
  await call('Emulation.setDeviceMetricsOverride',{width:1280,height:800,deviceScaleFactor:1,mobile:false});
  await call('Page.navigate',{url:pathToFileURL(join(root,'docs/demos/stage.html')).href});
  for (let i=0;i<100;i++) {
    if (await evaluate('typeof window.renderFrame === "function"')) break;
    if (i === 99) throw new Error('Animation page did not load');
    await new Promise(r => setTimeout(r,50));
  }
  await evaluate('document.fonts.ready.then(() => true)');
  const snapshot = async path => {
    const r = await call('Page.captureScreenshot',{format:'png',fromSurface:true,captureBeyondViewport:false});
    await writeFile(path,Buffer.from(r.data,'base64'));
  };
  await mkdir(join(root,'docs/demos/media'),{recursive:true});
  const measurements = [];
  for (const story of stories) {
    await evaluate(`window.setDemo(${JSON.stringify(story.id)});window.renderFrame(${story.duration-1});true`);
    const geometry = await evaluate(`(() => {
      const q=s=>document.querySelector(s), rect=e=>({top:e.getBoundingClientRect().top,bottom:e.getBoundingClientRect().bottom,height:e.getBoundingClientRect().height});
      return {prompt:rect(q('.prompt')),lastTool:rect([...document.querySelectorAll('.tool-row')].at(-1)),readLabel:rect(q('.read-label')),pane:rect(q('.request-pane')),resultContent:rect(q('.result-content')),footnote:rect(q('.result-footnote')),documentWidth:document.documentElement.scrollWidth};
    })()`);
    measurements.push({id:story.id,...geometry});
    await snapshot(join(root,'docs/demos/media',story.id+'.png'));
    if (!stills) {
      const frames = join(root,'qa/private/demo-frames',story.id);
      await mkdir(frames,{recursive:true});
      for(let n=0;n<Math.round(story.duration*fps);n++){
        await evaluate(`window.renderFrame(${n/fps});true`);
        await snapshot(join(frames,'frame-'+String(n).padStart(5,'0')+'.png'));
      }
      const output = join(root,'docs/demos/media',story.id+'.gif');
      await new Promise((res,rej) => {
        const encoder = spawn(ffmpeg,['-hide_banner','-loglevel','error','-y','-framerate',String(fps),'-i',join(frames,'frame-%05d.png'),'-filter_complex','[0:v]split[a][b];[a]palettegen=stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle','-loop','0',output],{stdio:['ignore','ignore','pipe']});
        let error='';encoder.stderr.on('data',d=>{error+=d.toString();});encoder.on('error',rej);encoder.on('exit',code=>code===0?res():rej(new Error(error)));
      });
    }
    console.log(JSON.stringify({id:story.id,rendered:stills?'poster':'gif + poster',seconds:story.duration}));
  }
  await writeFile(join(root,'qa/private/demo-layout.json'),JSON.stringify(measurements,null,2)+'\n');
  await send('Browser.close');
} finally {
  ws?.close();
  browser.kill('SIGTERM');
  await new Promise(r => setTimeout(r,150));
  await rm(profile,{recursive:true,force:true,maxRetries:4,retryDelay:100});
}
