// Shared regression for assigned English units, including saved progress and listening.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require('../generator/node_modules/playwright');
const NUMBERS=(process.argv.find(a=>a.startsWith('--units='))||'--units=2,3').split('=')[1].split(',').map(Number);
assert.ok(NUMBERS.length&&NUMBERS.every(n=>Number.isInteger(n)&&n>=2)&&new Set(NUMBERS).size===NUMBERS.length);
const KEYS=NUMBERS.map(n=>'u'+String(n).padStart(2,'0'));
const BASE=(process.argv.slice(2).find(a=>!a.startsWith('--'))||'http://127.0.0.1:8765/Lop_5_Mia/').replace(/\/?$/,'/');
const OUT=path.resolve(__dirname,'../artifacts','units'+NUMBERS.join('')+(BASE.includes('127.0.0.1')?'-local':'-online'));fs.mkdirSync(OUT,{recursive:true});
function fixture(){const voice={name:'English fixture',lang:'en-GB',voiceURI:'fixture'};window.__speech={calls:[],getVoices:()=>[voice],addEventListener(){},removeEventListener(){},cancel(){},speak(u){this.calls.push({text:u.text,rate:u.rate});u.onstart?.()}};Object.defineProperty(window,'speechSynthesis',{value:__speech});window.SpeechSynthesisUtterance=class{constructor(t){this.text=t}};}
async function fill(p){await p.evaluate(()=>__quiz.Q.forEach((q,i)=>{const e=document.getElementById('q'+(i+1)),set=(x,v)=>{x.value=v;x.dispatchEvent(new Event('input',{bubbles:true}));x.dispatchEvent(new Event('change',{bubbles:true}))};if(q.type==='listen')q.fields.forEach((f,k)=>set(e.querySelector('[data-listen-field="'+k+'"]'),f.answer));else if(['mc','pic'].includes(q.type)){const x=e.querySelectorAll('input')[q.answer];x.checked=true;x.dispatchEvent(new Event('change',{bubbles:true}))}else if(q.type==='text')set(e.querySelector('.text-in'),q.answers[0]);else if(q.type==='match')q.pairs.forEach((_,k)=>set(e.querySelector('[data-pair="'+k+'"]'),String(k)));else if(q.type==='reorder')q.items.forEach((_,k)=>e.querySelector('[data-add="'+k+'"]').click());else if(q.type==='tf')q.items.forEach((it,k)=>{const x=e.querySelector(`input[name="q${i}_${k}"][value="${it.a?'d':'s'}"]`);x.checked=true;x.dispatchEvent(new Event('change',{bubbles:true}))});}));}
(async()=>{const b=await chromium.launch();const errors=[];try{
 const p=await b.newPage({viewport:{width:390,height:844},reducedMotion:'reduce'});p.on('pageerror',e=>errors.push(e.message));await p.addInitScript(fixture);
 const catalog=await (await p.request.get(BASE+'catalog.json')).json(),tests=catalog.tests.filter(t=>KEYS.includes(t.id.split('-')[1]));const english=catalog.tests.filter(t=>t.subject==='en'),unitCount=new Set(english.map(t=>t.id.split('-')[1])).size;assert.equal(tests.length,KEYS.length*6);assert.equal(new Set(catalog.tests.map(t=>t.id)).size,catalog.tests.length);
 for(const t of tests){
  await p.goto(BASE+t.file);assert.equal(await p.locator('.listen-block').count(),6);
  assert.deepEqual(await p.evaluate(()=>['tb','kha','gioi'].map(l=>__quiz.Q.filter(q=>q.type==='listen'&&q.level===l).length)),[2,2,2]);
  const missing=await p.evaluate(()=>__quiz.Q.filter(q=>q.type==='listen').flatMap(q=>q.fields.filter(f=>!q.transcript.toLowerCase().includes(f.answer.toLowerCase())).map(f=>f.answer)));assert.deepEqual(missing,[],'Listening answers must agree with transcript');
  if(t.id==='en-u05-de1-v1'){
   const variants=await p.evaluate(()=>{const q=__quiz.Q.find(q=>q.type==='text'&&!q.exactForm&&q.answers[0].startsWith('I would')),full=__quiz.Q.find(q=>q.type==='text'&&q.exactForm&&q.answers[0]==='I would');return [__quiz.textIsCorrect(q.answers[0].replace('I would','I’d'),q.answers),__quiz.textIsCorrect('I’d',full.answers,true),__quiz.textIsCorrect('I would extra',full.answers,true)]});assert.deepEqual(variants,[true,false,false]);
  }
  for(const qid of [1,11,21]){await p.click(`#q${qid} [data-speech-play]:not([data-slow])`);assert.equal(await p.evaluate(()=>__speech.calls.at(-1).text),await p.evaluate(i=>__quiz.Q[i-1].speech,qid));}
  if(t.file.includes('De2_')){await p.evaluate(()=>document.fonts.ready);await p.addStyleTag({content:'#bar{visibility:hidden!important}'});for(const q of await p.locator('.q:has(.en-figure)').all()){await q.screenshot({path:path.join(OUT,t.id+'-'+await q.getAttribute('id')+'.png')});}}
  await p.addStyleTag({content:'#bar{visibility:visible!important}'});await fill(p);await p.click('#goBtn');assert.match(await p.locator('.score').textContent(),/100\s*\/\s*100/);await p.reload();assert.equal(await p.evaluate(id=>JSON.parse(localStorage.getItem('mia5:'+id)).best,t.id),100);
 }
 // Start the draft/partial-score scenario afresh in this isolated QA browser.
 await p.evaluate(ids=>ids.forEach(id=>{localStorage.removeItem('mia5:'+id);localStorage.removeItem('mia5:draft:'+id)}),tests.map(t=>t.id));
 for(const unit of KEYS){
  const t=tests.find(t=>t.id.startsWith('en-'+unit+'-de6-'));
  await p.goto(BASE+t.file);await fill(p);await p.fill('#stuName','Mia');await p.click('#q1 summary');await p.waitForTimeout(300);await p.reload();assert.match(await p.locator('#prog').textContent(),/24\/24/);assert.match(await p.locator('#q1 .listen-support').textContent(),/Đã dùng/);assert.equal(await p.locator('#stuName').inputValue(),'Mia');
  await p.click('#goBtn');assert.match(await p.locator('.score').textContent(),/100\s*\/\s*100/);assert.equal(await p.evaluate(id=>localStorage.getItem('mia5:draft:'+id),t.id),null);
  await p.reload();assert.equal(await p.evaluate(id=>JSON.parse(localStorage.getItem('mia5:'+id)).best,t.id),100);
  await p.click('#q21 [data-listen-field="0"]');await p.evaluate(()=>{const q=__quiz.Q[20],e=document.querySelector('#q21 [data-listen-field="0"]');e.value=q.fields[0].answer;e.dispatchEvent(new Event('change',{bubbles:true}))});await p.click('#goBtn');await p.click('#yes');assert.match(await p.locator('#q21 .fb').textContent(),/2,5\/5/);
 }
 await p.goto(BASE+'TiengAnh5/index.html');assert.equal(await p.locator('#sDone').textContent(),String(KEYS.length));assert.equal(await p.locator('#sStar').textContent(),String(KEYS.length*3));assert.equal(await p.locator('.topic').count(),unitCount);
 await p.goto(BASE);assert.ok((await p.locator('#english-progress').textContent()).includes(`${KEYS.length}/${english.length} đề · ${KEYS.length*3}/${english.length*3} sao`));
 // Reset English must clear new IDs/drafts, while preserving maths and legacy results.
 await p.evaluate(()=>{localStorage.setItem('mia5:cd1-de1','math');localStorage.setItem('mia5:en-u01-de1','legacy');localStorage.setItem('mia5:draft:en-u02-de1-v1','draft')});await p.goto(BASE+'TiengAnh5/index.html');await p.click('#reset');await p.click('#yes');
 assert.equal(await p.evaluate(()=>localStorage.getItem('mia5:cd1-de1')),'math');assert.equal(await p.evaluate(()=>localStorage.getItem('mia5:en-u01-de1')),'legacy');assert.deepEqual(await p.evaluate(keys=>Object.keys(localStorage).filter(k=>keys.some(unit=>k.startsWith('mia5:en-'+unit+'-')||k.startsWith('mia5:draft:en-'+unit+'-'))),KEYS),[]);
 // New posters/readers and subject chooser at phone/tablet/desktop sizes and actual themes.
 for(const theme of ['light','dark']){
  await p.evaluate(t=>localStorage.setItem('mia5:ui-theme',t),theme);
  for(const width of [320,390,768,1366]){
   await p.setViewportSize({width,height:844});
   for(const file of ['index.html','TiengAnh5/index.html',...NUMBERS.map(n=>tests.find(t=>t.id.startsWith('en-u'+String(n).padStart(2,'0')+'-')).file.replace(/De[^/]+$/,`TongQuan_Unit${n}.html`))]){
    await p.goto(BASE+file);await p.evaluate(()=>document.fonts.ready);await p.locator('.en-figure img').evaluateAll(imgs=>Promise.all(imgs.map(i=>i.decode())));assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),file);
    if(width===390&&theme==='light')await p.screenshot({path:path.join(OUT,file.replaceAll('/','_')+'-mobile.png'),fullPage:true});
   }
  }
 }
 // Verify both standalone exports include images and the same grading behavior.
 if(BASE.includes('127.0.0.1'))for(const folder of NUMBERS.map(n=>tests.find(t=>t.id.startsWith('en-u'+String(n).padStart(2,'0')+'-')).file.split('/')[1])){await p.goto(require('node:url').pathToFileURL(path.resolve(__dirname,'../generator/out/TiengAnh5',folder,'De2_TuVungVaHinhAnh.html')).href);await p.locator('.en-figure img').evaluateAll(imgs=>Promise.all(imgs.map(i=>i.decode())));assert.ok(await p.locator('.en-figure img').first().getAttribute('src').then(s=>s.startsWith('data:image/webp')));await fill(p);await p.click('#goBtn');assert.match(await p.locator('.score').textContent(),/100\s*\/\s*100/);}
 assert.deepEqual(errors,[]);fs.writeFileSync(path.join(OUT,'report.json'),JSON.stringify({base:BASE,tests:tests.length,allFullMarks:true,listeningQuestions:tests.length*6,layoutCases:(NUMBERS.length+2)*8,levels:[2,2,2],draftsAndResults:true,partialPoints:true,resetIsolated:true,standalone:BASE.includes('127.0.0.1'),errors},null,2));console.log(`Units ${NUMBERS.join(',')} QA PASS: ${tests.length} exams at 100/100, ${tests.length*6} listening questions, speech text, drafts, retained best scores, partial grading, aggregate progress, isolated reset${BASE.includes('127.0.0.1')?' and standalone exports':''}. Speech mocked.`);
 }finally{await b.close()}})().catch(e=>{console.error(e);process.exitCode=1});
