const {pathToFileURL}=require('node:url');
const { chromium } = require('playwright');
const fs=require('fs'), path=require('path');
function walk(d){return fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):[path.join(d,e.name)])}
(async()=>{
  let failures=0;
  const root=process.argv[2]||path.join(__dirname,'../site/Toan5'), only=process.argv[3]||'';
  const files=walk(root).filter(f=>/^De\d_.*\.html$/.test(path.basename(f))&&f.includes(only));
  const b=await chromium.launch();
  for(const f of files){
    const p=await b.newPage({viewport:{width:420,height:900}});
    const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
    await p.goto(pathToFileURL(path.resolve(f)).href); await p.waitForTimeout(300);
    const info=await p.evaluate(()=>{const Q=window.__quiz.Q;const c={};Q.forEach(q=>c[q.level]=(c[q.level]||0)+1);return {n:Q.length,c,pts:Q.reduce((s,q)=>s+q.pts,0),lessons:[...new Set(Q.map(q=>q.lesson))].sort((a,b)=>a-b).join(',')}});
    await p.evaluate(()=>{
      const Q=window.__quiz.Q;
      Q.forEach((q,i)=>{
        const el=document.getElementById('q'+(i+1));
        const set=(x,v)=>{x.value=v;x.dispatchEvent(new Event('input',{bubbles:true}));x.dispatchEvent(new Event('change',{bubbles:true}))};
        if(q.type==='mc'){const r=el.querySelectorAll('input')[q.answer];r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}))}
        else if(q.type==='tf'){q.items.forEach((it,k)=>{const r=el.querySelector(`input[name="q${i}_${k}"][value="${it.a?'d':'s'}"]`);r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}))})}
        else if(q.type==='order'){q.items.forEach((_,k)=>{el.querySelector(`[data-add="${k}"]`).click()})}
        else q.blanks.forEach((b,bi)=>{const row=el.querySelectorAll('.bl')[bi];
          if(b.kind==='num')set(row.querySelector('[data-p=v]'), String(b.ans).replace('.',','));
          else if(b.kind==='sel')set(row.querySelector('select'),b.ans);
          else if(b.kind==='frac'){set(row.querySelector('[data-p=n]'),b.ans[0]);set(row.querySelector('[data-p=d]'),b.ans[1])}
          else {set(row.querySelector('[data-p=w]'),b.ans[0]);set(row.querySelector('[data-p=n]'),b.ans[1]);set(row.querySelector('[data-p=d]'),b.ans[2])}
        });
      });
    });
    await p.click('#goBtn'); await p.waitForTimeout(250);
    const score=(await p.textContent('.score')).replace(/\s+/g,' ');
    const bad=await p.evaluate(()=>[...document.querySelectorAll('.fb.no,.fb.part')].map(e=>e.closest('[id^=q]').id));
    const links=await p.evaluate(()=>[...document.querySelectorAll('a.btn,a.back')].map(a=>a.getAttribute('href')));
    if(!/100\s*\/\s*100/.test(score)||bad.length||errs.length||info.n!==24||info.pts!==100)failures++;
    console.log(path.basename(f),JSON.stringify(info),'|',score,'| bad:',bad.join(',')||'-','| errs:',errs.length?errs:'-','| links:',links.join(' '));
    await p.close();
  }
  await b.close();
  if(failures||files.length===0)process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1;});
