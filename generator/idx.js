const fs=require('node:fs'); const shotDir=require('node:path').join(__dirname,'out','qa'); fs.mkdirSync(shotDir,{recursive:true}); process.chdir(__dirname);
const {pathToFileURL}=require('node:url');
const { chromium } = require('playwright'); const path=require('path');
(async()=>{
 const b=await chromium.launch(); const ctx=await b.newContext({viewport:{width:1200,height:900}});
 const root=path.resolve('out/Toan5');
 const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto(pathToFileURL(path.join(root,'index.html')).href); await p.waitForTimeout(1000);
 await p.screenshot({path:path.join(shotDir,'i_top.png')}); await p.screenshot({path:path.join(shotDir,'i_full0.png'),fullPage:true});
 // làm đề 2 CD1 đúng hết + đề 1 CD2 sai nửa
 for(const [f,mode] of [['ChuDe1_OnTapVaBoSung/De2_MotNgayOTruong.html','all'],['ChuDe2_SoThapPhan/De1_KhoiDong.html','half']]){
  const t=await ctx.newPage(); await t.goto(pathToFileURL(path.join(root,f)).href); await t.waitForTimeout(300);
  await t.evaluate((mode)=>{const Q=window.__quiz.Q;Q.forEach((q,i)=>{if(mode==='half'&&i%3!==0)return;const el=document.getElementById('q'+(i+1));const set=(x,v)=>{x.value=v;x.dispatchEvent(new Event('input',{bubbles:true}));x.dispatchEvent(new Event('change',{bubbles:true}))};
   if(q.type==='mc'){const r=el.querySelectorAll('input')[q.answer];r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}))}
   else if(q.type==='tf'){q.items.forEach((it,k)=>{const r=el.querySelector(`input[name="q${i}_${k}"][value="${it.a?'d':'s'}"]`);r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}))})}
   else if(q.type==='order'){q.items.forEach((_,k)=>{el.querySelector(`[data-add="${k}"]`).click()})}
   else q.blanks.forEach((b,bi)=>{const row=el.querySelectorAll('.bl')[bi];if(b.kind==='num')set(row.querySelector('[data-p=v]'),String(b.ans).replace('.',','));else if(b.kind==='sel')set(row.querySelector('select'),b.ans);else if(b.kind==='frac'){set(row.querySelector('[data-p=n]'),b.ans[0]);set(row.querySelector('[data-p=d]'),b.ans[1])}else{set(row.querySelector('[data-p=w]'),b.ans[0]);set(row.querySelector('[data-p=n]'),b.ans[1]);set(row.querySelector('[data-p=d]'),b.ans[2])}})})},mode);
  await t.click('#goBtn'); if(mode==='half'){await t.waitForTimeout(150);await t.click('#yes')} await t.waitForTimeout(300);
  console.log(f,(await t.textContent('.score')).replace(/\s+/g,' ')); await t.close();
 }
 await p.reload(); await p.waitForTimeout(900);
 console.log('stats',await p.evaluate(()=>[sDone.textContent,sStar.textContent,sBest.textContent,goTxt.textContent,go.getAttribute('href')]));
 await p.screenshot({path:path.join(shotDir,'i_full1.png'),fullPage:true});
 const m=await ctx.newPage(); await m.setViewportSize({width:390,height:800}); await m.goto(pathToFileURL(path.join(root,'index.html')).href); await m.waitForTimeout(900);
 console.log('mobile scrollW',await m.evaluate(()=>document.documentElement.scrollWidth)); await m.screenshot({path:path.join(shotDir,'i_m.png'),fullPage:true});
 console.log('errs',errs); await b.close();
})().catch(e=>{console.error(e);process.exitCode=1;});
