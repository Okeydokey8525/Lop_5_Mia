// Real media decoding/playback with Speech API removed: regression for grey buttons.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{pathToFileURL}=require('node:url');
const {chromium,webkit}=require('../generator/node_modules/playwright');
const BASE=(process.argv.slice(2).find(a=>!a.startsWith('--'))||'http://127.0.0.1:8765/Lop_5_Mia/').replace(/\/?$/,'/'),isWebkit=process.argv.includes('--webkit');
const OUT=path.resolve(__dirname,'../artifacts/unit11-'+(BASE.includes('127.0.0.1')?'local':'online')+(isWebkit?'-webkit':''));fs.mkdirSync(OUT,{recursive:true});
const folder='TiengAnh5/Unit11_FamilyTime/',study=folder+'HocTuVaPhatAm.html';
function noSpeech(){
 Object.defineProperty(window,'speechSynthesis',{value:undefined,configurable:true});window.SpeechSynthesisUtterance=undefined;
 window.__media=[];const play=HTMLMediaElement.prototype.play;
 HTMLMediaElement.prototype.play=function(){const entry={src:this.src,rate:this.playbackRate,started:false,ended:false};__media.push(entry);this.addEventListener('playing',()=>entry.started=true,{once:true});this.addEventListener('ended',()=>entry.ended=true,{once:true});return play.call(this);};
}
(async()=>{const b=await (isWebkit?webkit:chromium).launch();const errors=[],decoded=[];try{
 const ctx=await b.newContext({viewport:isWebkit?{width:768,height:1024}:{width:390,height:844},...(isWebkit?{isMobile:true,hasTouch:true,deviceScaleFactor:2}:{}),reducedMotion:'reduce'});await ctx.addInitScript(noSpeech);
 const p=await ctx.newPage();p.on('pageerror',e=>errors.push(e.message));await p.goto(BASE+study);
 assert.equal(await p.evaluate(()=>window.speechSynthesis),undefined);
 assert.equal(await p.locator('#voice').inputValue(),'mia-recorded');assert.equal(await p.locator('[data-say="swim"]').first().isDisabled(),false);
 assert.equal(await p.evaluate(()=>__media.length),0,'No autoplay');
 const clips=await p.locator('#mia-audio-data').evaluate(el=>JSON.parse(el.textContent).clips);
 const catalog=await (await p.request.get(BASE+'catalog.json')).json(),tests=catalog.tests.filter(t=>t.id.startsWith('en-u11-'));assert.equal(tests.length,6);
 // Also retain the browser's native utterance constructor: a recorded voice is
 // not a SpeechSynthesisVoice and must never be assigned to that native setter.
 const regular=await b.newPage();regular.on('pageerror',e=>errors.push(e.message));
 await regular.goto(BASE+study);if(!isWebkit)assert.equal(await regular.evaluate(()=>typeof SpeechSynthesisUtterance),'function');
 await regular.click('[data-say="swim"]:not([data-slow])');await regular.waitForFunction(()=>document.querySelector('#play-status').textContent.includes('Đã nghe xong'));
 await regular.goto(BASE+tests[0].file);await regular.click('#q1 [data-speech-play]:not([data-slow])');await regular.waitForFunction(()=>document.querySelector('#q1 .speech-state').textContent.includes('Đã nghe xong'));await regular.close();
 for(const t of tests){await p.goto(BASE+t.file);Object.assign(clips,await p.locator('#mia-audio-data').evaluate(el=>JSON.parse(el.textContent).clips));assert.equal(await p.locator('[data-speech-play]').first().isDisabled(),false);}
 const manifest=JSON.parse(fs.readFileSync(path.resolve(__dirname,'../generator/english/u11/audio/manifest.json'),'utf8'));
 assert.deepEqual(Object.keys(clips).sort(),manifest.clips.map(c=>c.text).sort());
 // Every published clip must load and decode to non-silent audio, not just return HTTP 200.
 for(const [text,src] of Object.entries(clips)){
  const info=await p.evaluate(async src=>{
   const r=await fetch(src);if(!r.ok)throw Error('Audio HTTP '+r.status);const bytes=await r.arrayBuffer(),Context=window.AudioContext||window.webkitAudioContext;
   if(Context){const c=new Context();try{const a=await c.decodeAudioData(bytes);let peak=0;for(const s of a.getChannelData(0))peak=Math.max(peak,Math.abs(s));return {duration:a.duration,peak,validation:'Web Audio decode'};}finally{await c.close();}}
   // Windows WebKit lacks Web Audio. Validate the PCM payload and require its
   // real HTML media decoder to recognize the file's duration instead.
   const view=new DataView(bytes);let offset=12,peak=0,pcm=false;
   while(offset+8<=view.byteLength){const key=String.fromCharCode(...new Uint8Array(bytes,offset,4)),size=view.getUint32(offset+4,true),start=offset+8;if(start+size>view.byteLength)throw Error('Truncated WAV');
    if(key==='fmt ')pcm=view.getUint16(start,true)===1&&view.getUint16(start+14,true)===16;
    if(key==='data'){for(let i=start;i+1<start+size;i+=2)peak=Math.max(peak,Math.abs(view.getInt16(i,true)/32768));}offset=start+size+(size%2);
   }if(!pcm)throw Error('Expected PCM16 WAV');
   const a=new Audio();a.preload='metadata';const duration=await new Promise((resolve,reject)=>{const timer=setTimeout(()=>reject(Error('Audio metadata timeout')),10000);a.onloadedmetadata=()=>{clearTimeout(timer);resolve(a.duration);};a.onerror=()=>{clearTimeout(timer);reject(Error('Audio metadata error'));};a.src=src;});a.removeAttribute('src');a.load();return {duration,peak,validation:'PCM16 payload and HTML media metadata'};
  },src);
  assert.ok(info.duration>0.1&&info.peak>0.001,text);decoded.push({text,...info});
 }
 await p.goto(BASE+study);await p.click('[data-say="swim"]:not([data-slow])');await p.waitForFunction(()=>document.querySelector('#play-status').textContent.includes('Đã nghe xong'));
 assert.ok(await p.evaluate(()=>__media.at(-1).started&&__media.at(-1).ended));assert.equal(await p.evaluate(()=>__media.at(-1).rate),1);
 await p.click('[data-say="swim"][data-slow]');await p.waitForFunction(()=>document.querySelector('#play-status').textContent.includes('Đã nghe xong'));assert.ok(Math.abs(await p.evaluate(()=>__media.at(-1).rate)-0.8)<0.001);
 await p.click('[data-spell="swim"]');await p.waitForFunction(()=>document.querySelector('#play-status').textContent.includes('Đã đánh vần xong'));
 assert.deepEqual(await p.evaluate(()=>__media.slice(-4).map(e=>Object.entries(JSON.parse(document.querySelector('#mia-audio-data').textContent).clips).find(([t,s])=>new URL(s,location.href).href===e.src)[0])),['S','W','I','M']);
 assert.equal(await p.locator('[data-letter].active').count(),0);
 await p.click('[data-spell="collect-seashells"]');await p.waitForFunction(()=>document.querySelector('[data-letter].active'));
 await p.click('[data-stop]');const stopped=await p.evaluate(()=>__media.length);await p.waitForTimeout(1000);assert.equal(await p.evaluate(()=>__media.length),stopped);assert.equal(await p.locator('[data-letter].active').count(),0);
 // Hidden pages stop the queue; switching groups cannot resume the previous one.
 await p.click('[data-spell="swim"]');await p.waitForFunction(()=>document.querySelector('[data-letter].active'));
 await p.click('[data-group-select="trip"]');assert.equal(await p.locator('#mini-player').isHidden(),true);
 await p.click('[data-text]:visible');await p.waitForFunction(()=>document.querySelector('#play-status').textContent.includes('Đã nghe xong'));
 await p.click('[data-group-select="beach"]');await p.locator('#voice-settings').evaluate(el=>el.open=true);
 await p.screenshot({path:path.join(OUT,'audio-no-speech-api.png'),fullPage:true});
 // A real failed audio request must show an error and permit retry.
 const broken=await ctx.newPage();let failAudio=true;
 if(isWebkit){
  // WebKit Windows media loading bypasses Playwright routing. Keep the real
  // decoder/network, but redirect this attempt to a real HTTP 404 instead.
  await broken.addInitScript(()=>{window.__failAudio=true;const d=Object.getOwnPropertyDescriptor(HTMLMediaElement.prototype,'src');Object.defineProperty(HTMLMediaElement.prototype,'src',{...d,set(v){d.set.call(this,window.__failAudio?new URL('missing-unit11-audio.wav',new URL(v,location.href)).href:v);}});});
 }else await broken.route('**/audio/*.wav',route=>failAudio?route.abort():route.continue());
 await broken.goto(BASE+study);await broken.click('[data-say="swim"]:not([data-slow])');await broken.waitForFunction(()=>document.querySelector('#play-status').textContent.includes('Chưa phát được'));
 failAudio=false;if(isWebkit)await broken.evaluate(()=>window.__failAudio=false);await broken.click('[data-say="swim"]:not([data-slow])');await broken.waitForFunction(()=>document.querySelector('#play-status').textContent.includes('Đã nghe xong'));await broken.close();
 // Play one item from each listening level in the real formal exam.
 await p.goto(BASE+tests[0].file);
 for(const id of [1,11,21]){await p.click(`#q${id} [data-speech-play]:not([data-slow])`);await p.waitForFunction(id=>document.querySelector('#q'+id+' .speech-state').textContent.includes('Đã nghe xong'),id);}
 assert.ok(await p.evaluate(()=>__media.length===3&&__media.every(e=>e.started&&e.ended)));
 if(BASE.includes('127.0.0.1')){
  await p.goto(pathToFileURL(path.resolve(__dirname,'../generator/out',study)).href);
  assert.ok(await p.locator('#mia-audio-data').evaluate(el=>Object.values(JSON.parse(el.textContent).clips).every(s=>s.startsWith('data:audio/wav;base64,'))));
  // File-URL audio is unsupported in Windows Playwright WebKit. The iPad path
  // is the HTTPS site tested above; standalone playback is gated in Chromium.
  if(!isWebkit){await p.click('[data-say="swim"]:not([data-slow])');await p.waitForFunction(()=>document.querySelector('#play-status').textContent.includes('Đã nghe xong'));}
 }
 assert.deepEqual(errors,[]);fs.writeFileSync(path.join(OUT,'audio-report.json'),JSON.stringify({base:BASE,browser:isWebkit?'webkit':'chromium',speechApiAbsent:true,decoded,actualPlayback:true,slowRate:0.8,spelling:true,cancelledQueue:true,failedRequestRetry:true,formalLevels:3,standalone:BASE.includes('127.0.0.1')&&!isWebkit,standaloneEmbeddingChecked:BASE.includes('127.0.0.1'),standaloneLimitation:isWebkit?'File-URL audio not verified; Windows WebKit cannot play the embedded WAV. Use HTTP/Pages.':null,earReviewed:false,studentDeviceVerified:false,errors},null,2));
 console.log(`Unit 11 recorded audio PASS: ${decoded.length} non-silent decoded clips, real playback with no Speech API, slow/spelling/cancel/retry, three exam levels. Human pronunciation/device review pending.`);
 }finally{await b.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
