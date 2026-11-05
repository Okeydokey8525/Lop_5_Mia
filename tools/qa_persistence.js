// Persistent on-disk browser profile: verify a real close/relaunch, not only reload.
const fs=require('node:fs'),os=require('node:os'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require('../generator/node_modules/playwright');
const BASE=(process.argv.slice(2).find(a=>!a.startsWith('--'))||'http://127.0.0.1:8765/Lop_5_Mia/').replace(/\/?$/,'/');
const OUT=path.resolve(__dirname,'../artifacts',BASE.includes('127.0.0.1')?'persistence-local':'persistence-online');fs.mkdirSync(OUT,{recursive:true});
let fixtures=[{subject:'Toan5',file:'ChuDe1_OnTapVaBoSung/De1_KhoiDong.html',overview:'ChuDe1_OnTapVaBoSung/TongQuan_ChuDe1.html',id:'cd1-de1'},
{subject:'TiengAnh5',file:'Unit1_AllAboutMe/De1_KhoiDong.html',overview:'Unit1_AllAboutMe/TongQuan_Unit1.html',id:'en-u01-de1-v2'}];
const selection=process.argv.find(a=>a.startsWith('--units='));
if(selection){const tests=JSON.parse(fs.readFileSync(path.resolve(__dirname,'../site/catalog.json'),'utf8')).tests;fixtures=selection.split('=')[1].split(',').map(Number).map(n=>{assert.ok(Number.isInteger(n)&&n>=1);const t=tests.find(t=>t.id.startsWith('en-u'+String(n).padStart(2,'0')+'-de1-'));assert.ok(t,'Unknown unit '+n);const [subject,dir,file]=t.file.split('/');return {subject,file:dir+'/'+file,overview:dir+'/TongQuan_Unit'+n+'.html',id:t.id};});}
async function fillCorrect(page,mode='all'){
  await page.evaluate(mode=>{
    window.__quiz.Q.forEach((q,i)=>{
      if(mode==='half'&&i%2) return;
      const el=document.getElementById('q'+(i+1));
      const set=(x,v)=>{x.value=v;x.dispatchEvent(new Event('input',{bubbles:true}));x.dispatchEvent(new Event('change',{bubbles:true}));};
      if(q.type==='listen')q.fields.forEach((f,k)=>set(el.querySelector('[data-listen-field="'+k+'"]'),f.answer));
      else if(q.type==='mc'||q.type==='pic'){const x=el.querySelectorAll('input')[q.answer];x.checked=true;x.dispatchEvent(new Event('change',{bubbles:true}));}
      else if(q.type==='tf')q.items.forEach((it,k)=>{const x=el.querySelector(`input[name="q${i}_${k}"][value="${it.a?'d':'s'}"]`);x.checked=true;x.dispatchEvent(new Event('change',{bubbles:true}));});
      else if(q.type==='order'||q.type==='reorder')q.items.forEach((_,k)=>el.querySelector(`[data-add="${k}"]`).click());
      else if(q.type==='text')set(el.querySelector('.text-in'),q.answers[0]);
      else if(q.type==='match')q.pairs.forEach((_,k)=>set(el.querySelector(`[data-pair="${k}"]`),String(k)));
      else q.blanks.forEach((b,k)=>{const row=el.querySelectorAll('.bl')[k];
        if(b.kind==='num')set(row.querySelector('[data-p=v]'),String(b.ans).replace('.',','));
        else if(b.kind==='sel')set(row.querySelector('select'),b.ans);
        else {const parts=b.kind==='frac'?['n','d']:['w','n','d'];parts.forEach((p,j)=>set(row.querySelector(`[data-p=${p}]`),b.ans[j]));}
      });
    });
  },mode);
}
async function main(){
 const profile=fs.mkdtempSync(path.join(os.tmpdir(),'mia-persistence-')),errors=[];let context;
 const launch=async()=>{context=await chromium.launchPersistentContext(profile,{viewport:{width:390,height:844},reducedMotion:'reduce'});context.on('page',p=>p.on('pageerror',e=>errors.push(e.message)));return context.pages()[0]};
 try{
  let p=await launch();p.on('pageerror',e=>errors.push(e.message));
  for(const f of fixtures){
   await p.goto(BASE+f.subject+'/index.html');
   await p.goto(BASE+f.subject+'/'+f.file);await fillCorrect(p);await p.fill('#stuName','Mia');await p.click('#goBtn');
   assert.match(await p.locator('#draftStatus').textContent(),/Đã lưu kết quả/);
   await p.goBack();assert.equal(await p.locator('.stop.done a[href="'+f.file+'"]').count(),1);
   assert.match(await p.locator('.stop.done a[href="'+f.file+'"]').textContent(),/Đã hoàn thành/);
  }
  await context.close();context=null;p=await launch();
  for(const f of fixtures){
   await p.goto(BASE+f.subject+'/'+f.file);assert.match(await p.locator('.saved-result').textContent(),/100\/100/);
   const read=()=>p.evaluate(id=>localStorage.getItem('mia5:'+id),f.id),before=await read();
   await p.click('#reviewSaved');assert.match(await p.locator('.score').textContent(),/100\s*\/\s*100/);
   assert.equal(await read(),before,'Review must not increment attempts or change saved result');
   assert.equal(await p.locator('.fb.ok').count(),24);await p.click('#again');
   await p.click('#goBtn');await p.click('#yes');
   const lower=JSON.parse(await read());assert.equal(lower.best,100);assert.equal(lower.last,0);assert.equal(lower.tries,2);
   assert.equal(lower.review.baseResult,'','Do not recursively embed earlier result snapshots');
   await p.reload();await p.click('#reviewSaved');assert.match(await p.locator('.score').textContent(),/0\s*\/\s*100/);
   assert.equal(JSON.parse(await read()).tries,2);
   await p.goto(BASE+f.subject+'/'+f.overview);assert.equal(await p.locator('.foot .completed').count(),1);
   assert.match(await p.locator('.foot .completed').textContent(),/100\/100/);
   await p.goto(BASE+f.subject+'/index.html');
   // Exercise a cached page's event handler and live updates from a separate tab.
   await p.evaluate(()=>window.dispatchEvent(new PageTransitionEvent('pageshow',{persisted:true})));
   assert.match(await p.locator('.stop.done a[href="'+f.file+'"] .attempt-note').textContent(),/Gần nhất: 0\/100/);
   const tab=await context.newPage();await tab.goto(BASE+f.subject+'/'+f.file);await fillCorrect(tab);await tab.click('#goBtn');
   await p.waitForFunction(h=>Array.from(document.querySelectorAll('.stop.done a')).find(a=>a.getAttribute('href')===h).querySelector('.attempt-note').textContent.includes('100/100'),f.file);await tab.close();
   await p.goto(BASE+f.subject+'/'+f.file);await fillCorrect(p,'half');
   await p.click('#reviewSaved');assert.match(await p.locator('#draftStatus').textContent(),/đang làm lượt mới/);
   await p.reload();assert.match(await p.locator('#draftStatus').textContent(),/Đã khôi phục/);assert.equal(await p.locator('#reviewSaved').count(),0);
   await p.click('#discardDraft');await p.click('#confirmDiscard');
   for(const theme of ['light','dark']){
    await p.evaluate(t=>localStorage.setItem('mia5:ui-theme',t),theme);await p.reload();
    for(const width of [320,390,768,1280]){await p.setViewportSize({width,height:844});await p.evaluate(()=>document.fonts.ready);assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Saved summary must fit viewport');}
   }
   await p.setViewportSize({width:390,height:844});await p.screenshot({path:path.join(OUT,f.subject+'-saved.png')});
   await p.goto(BASE+f.subject+'/index.html');await p.locator('.stop.done a[href="'+f.file+'"]').scrollIntoViewIfNeeded();await p.screenshot({path:path.join(OUT,f.id+'-progress.png')});
  }
  const f=fixtures[0],key='mia5:'+f.id;
  await p.goto(BASE+f.subject+'/'+f.file);
  await p.evaluate(k=>{const r=JSON.parse(localStorage.getItem(k));delete r.review;localStorage.setItem(k,JSON.stringify(r))},key);
  await p.reload();assert.match(await p.locator('.saved-result').textContent(),/100\/100/);assert.equal(await p.locator('#reviewSaved').count(),0,'Legacy scores remain visible without invented answers');
  const old=await p.evaluate(k=>localStorage.getItem(k),key);
  // A full/blocked store must not erase the existing best or falsely promise persistence.
  await p.evaluate(()=>{Storage.prototype.setItem=function(){throw new DOMException('Full','QuotaExceededError')}});
  await p.click('#goBtn');await p.click('#yes');assert.match(await p.locator('#saveStatus').textContent(),/chưa lưu được kết quả/);
  assert.equal(await p.evaluate(k=>localStorage.getItem(k),key),old);
 }finally{if(context)await context.close();}
 assert.deepEqual(errors,[]);fs.writeFileSync(path.join(OUT,selection?'units-report.json':'report.json'),JSON.stringify({base:BASE,browserRestart:true,subjects:new Set(fixtures.map(f=>f.subject)).size,tests:fixtures.map(f=>f.id),reviewWithoutResubmit:true,bestRetained:true,backNavigation:true,crossTab:true,errors,checkedAt:new Date().toISOString()},null,2));
 console.log('Persistence PASS: browser close/relaunch, saved answers/review, best/last, Back and cross-tab updates for '+fixtures.map(f=>f.id).join(', ')+'.');
}
main().catch(e=>{console.error(e);process.exitCode=1});
