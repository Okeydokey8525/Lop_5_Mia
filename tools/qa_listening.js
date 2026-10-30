const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require('../generator/node_modules/playwright');
const ROOT=path.resolve(__dirname,'..'),BASE=(process.argv[2]||'http://127.0.0.1:8765/Lop_5_Mia/').replace(/\/?$/,'/'),FILE='TiengAnh5/Unit1_AllAboutMe/LuyenNghe_Mau.html';
const OUT=path.join(ROOT,'artifacts',BASE.includes('127.0.0.1')?'listening-local':'listening-online');fs.mkdirSync(OUT,{recursive:true});
async function mock(page,mode='normal'){
 await page.addInitScript(mode=>{
  if(mode==='unsupported'){Object.defineProperty(window,'speechSynthesis',{value:undefined,configurable:true});return}
  const en={name:'Sample English',lang:'en-GB',voiceURI:'sample-en',localService:true},vi={name:'Vietnamese',lang:'vi-VN',voiceURI:'sample-vi'};
  window.__speechMock={voices:mode==='empty'?[]:[vi,en],calls:[],cancels:0,listeners:[],getVoices(){return this.voices},addEventListener(n,f){this.listeners.push(f)},speak(u){this.calls.push(u);u.onstart?.()},cancel(){this.cancels++}};
  Object.defineProperty(window,'speechSynthesis',{value:window.__speechMock,configurable:true});window.SpeechSynthesisUtterance=class{constructor(text){this.text=text}};
 },mode);
}
async function main(){const b=await chromium.launch(),errors=[];try{
 const p=await b.newPage({viewport:{width:390,height:844}});p.on('pageerror',e=>errors.push(e.message));await mock(p);await p.goto(BASE+FILE);await p.evaluate(()=>document.fonts.ready);
 assert.equal(await p.locator('.question').count(),6);for(const id of ['tb','kha','gioi'])assert.equal(await p.locator('#'+id+' .question').count(),2);
 assert.equal(await p.locator('details[open]').count(),0);assert.equal(await p.locator('#voice option').count(),1);assert.match(await p.locator('#voice-status').textContent(),/Sample English/);
 await p.evaluate(()=>{localStorage.setItem('mia5:cd1-de1','keep-math');localStorage.setItem('mia5:en-u01-de1','keep-english')});
 await p.click('#tb1 [data-play]:not([data-slow])');assert.match(await p.locator('#tb1 .play-status').textContent(),/Đang phát/);
 assert.equal(await p.evaluate(()=>__speechMock.calls.at(-1).lang),'en-GB');assert.equal(await p.evaluate(()=>__speechMock.calls.at(-1).rate),.9);
 await p.click('#gioi1 [data-slow]');assert.equal(await p.evaluate(()=>__speechMock.calls.at(-1).rate),.72);assert.equal(await p.locator('#tb1 [data-stop]').isDisabled(),true);
 await p.evaluate(()=>__speechMock.calls[0].onend());assert.match(await p.locator('#gioi1 .play-status').textContent(),/Đang phát/);
 await p.click('#gioi1 [data-stop]');assert.match(await p.locator('#gioi1 .play-status').textContent(),/Đã dừng/);
 await p.click('#tb2 [data-play]:not([data-slow])');await p.evaluate(()=>__speechMock.calls.at(-1).onerror({error:'synthesis-failed'}));assert.match(await p.locator('#tb2 .play-status').textContent(),/Chưa phát được/);
 await p.click('#kha1 [data-play]:not([data-slow])');await p.evaluate(()=>__speechMock.calls.at(-1).onend());assert.match(await p.locator('#kha1 .play-status').textContent(),/Đã nghe xong/);
 await p.evaluate(()=>__listening.questions.forEach(q=>q.fields.forEach((f,k)=>{const fields=[...document.getElementsByName(q.id+'-'+k)];if(f.options)fields.find(e=>e.value===f.answer).checked=true;else fields[0].value=' '+f.answer.toLowerCase()+' ';})));await p.click('button[type=submit]');assert.match(await p.locator('#total').textContent(),/Đúng 8\/8/);
 await p.fill('[name="gioi2-1"]','football');assert.match(await p.locator('#total').textContent(),/5\/6 câu/);await p.click('[data-check=gioi2]');assert.match(await p.locator('#gioi2 .result').textContent(),/1\/2/);
 await p.fill('[name="gioi2-0"]','');await p.click('[data-check=gioi2]');assert.match(await p.locator('#gioi2 .result').textContent(),/chưa trả lời/);
 await p.click('#reset');assert.equal(await p.locator('input:checked').count(),0);assert.equal(await p.locator('details[open]').count(),0);assert.equal(await p.locator('[name="gioi2-0"]').inputValue(),'');assert.equal(await p.evaluate(()=>localStorage.getItem('mia5:cd1-de1')),'keep-math');assert.equal(await p.evaluate(()=>localStorage.getItem('mia5:en-u01-de1')),'keep-english');
 await p.click('#tb1 summary');await p.waitForFunction(()=>document.querySelector('#tb1 .support').textContent.includes('không bị trừ điểm'));
 await p.click('#test-voice');await p.click('#stop-all');assert.match(await p.locator('#voice-status').textContent(),/Đã dừng/);
 const empty=await b.newPage();await mock(empty,'empty');await empty.goto(BASE+FILE);assert.equal(await empty.locator('#tb1 [data-play]').first().isDisabled(),true);assert.match(await empty.locator('#voice-status').textContent(),/Chưa có giọng/);
 await empty.evaluate(()=>{__speechMock.voices=[{name:'English loaded later',voiceURI:'later',lang:'en-US'}];__speechMock.listeners.forEach(f=>f())});assert.equal(await empty.locator('#tb1 [data-play]').first().isDisabled(),false);
 await empty.evaluate(()=>{__speechMock.voices=[];__speechMock.listeners.forEach(f=>f())});assert.equal(await empty.locator('#test-voice').isDisabled(),true);
 const unsupported=await b.newPage();await mock(unsupported,'unsupported');await unsupported.goto(BASE+FILE);assert.equal(await unsupported.locator('#test-voice').isDisabled(),true);await unsupported.click('#tb1 summary');assert.equal(await unsupported.locator('#tb1 details').getAttribute('open'),'');
 // A synthesis service that never starts must not leave the UI permanently playing.
 const stalled=await b.newPage();await stalled.clock.install();await mock(stalled);await stalled.goto(BASE+FILE);await stalled.evaluate(()=>__speechMock.speak=function(u){this.calls.push(u)});await stalled.click('#tb1 [data-play]:not([data-slow])');await stalled.clock.runFor(12500);assert.match(await stalled.locator('#tb1 .play-status').textContent(),/Chưa phát được/);
 for(const scheme of ['light','dark']){await p.emulateMedia({colorScheme:scheme});for(const width of [320,360,390,768,1366]){await p.setViewportSize({width,height:844});assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));const small=await p.locator('button,select,summary').evaluateAll(es=>es.filter(e=>e.getBoundingClientRect().height<44).map(e=>e.textContent));assert.deepEqual(small,[]);if(width===390)await p.screenshot({path:path.join(OUT,scheme+'-mobile.png'),fullPage:true});}}
 assert.deepEqual(errors,[]);fs.writeFileSync(path.join(OUT,'report.json'),JSON.stringify({base:BASE,questions:6,levels:3,answerParts:8,mockedSpeech:true,voiceFallback:true,timeout:true,isolatedStorage:true,errors,checkedAt:new Date().toISOString()},null,2));console.log('Listening QA PASS: 3 levels, 6 questions, 8 answer parts; play/slow/stop/errors/async voices/timeout, scoring/reset, no storage changes, 10 responsive cases. Speech mocked; voice quality needs human review.');
 }finally{await b.close()}}
main().catch(e=>{console.error(e);process.exitCode=1});
