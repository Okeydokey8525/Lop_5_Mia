const { chromium } = require('playwright'); const path=require('path');
(async()=>{ const [,, file, out, ...ids]=process.argv; const b=await chromium.launch(); const p=await b.newPage({viewport:{width:600,height:900}});
 await p.goto('file://'+path.resolve(file)); await p.waitForTimeout(400);
 for(const id of ids){ const e=await p.$('#q'+id); await e.screenshot({path:`${out}_${id}.png`}); }
 await b.close(); })();
