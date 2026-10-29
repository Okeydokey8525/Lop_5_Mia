const { chromium } = require('playwright'); const path=require('path');
(async()=>{ const [,, file, out]=process.argv; const b=await chromium.launch(); const p=await b.newPage({viewport:{width:700,height:900}});
 const errs=[]; p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+path.resolve(file)); await p.waitForTimeout(500);
 const els=await p.$$('.q:has(.fig)'); console.log('figs q',els.length);
 let i=0; for(const e of els){ await e.screenshot({path:`${out}_${i++}.png`}); }
 console.log(errs); await b.close(); })();
