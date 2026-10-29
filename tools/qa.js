// HTTP browser QA. Optional base URL also runs the same checks on production.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {createRequire}=require('node:module');
const requireGenerator=createRequire(path.resolve(__dirname,'../generator/package.json'));
const {chromium}=requireGenerator('playwright');
const ROOT=path.resolve(__dirname,'..'),SITE=path.join(ROOT,'site');
const BASE=(process.argv.slice(2).find(a=>!a.startsWith('--'))||'http://127.0.0.1:8765/Lop_5_Mia/').replace(/\/?$/,'/');
const SHOTS=!process.argv.includes('--no-shots');
const OUT=path.join(ROOT,'artifacts',BASE.includes('127.0.0.1')?'local':'online');
fs.mkdirSync(OUT,{recursive:true});
function walk(d){return fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):[path.join(d,e.name)]);}
function relative(f){return path.relative(SITE,f).split(path.sep).join('/');}
async function fillCorrect(page,mode='all'){
  await page.evaluate(mode=>{
    window.__quiz.Q.forEach((q,i)=>{
      if(mode==='half'&&i%2) return;
      const el=document.getElementById('q'+(i+1));
      const set=(x,v)=>{x.value=v;x.dispatchEvent(new Event('input',{bubbles:true}));x.dispatchEvent(new Event('change',{bubbles:true}));};
      if(q.type==='mc'){const x=el.querySelectorAll('input')[q.answer];x.checked=true;x.dispatchEvent(new Event('change',{bubbles:true}));}
      else if(q.type==='tf')q.items.forEach((it,k)=>{const x=el.querySelector(`input[name="q${i}_${k}"][value="${it.a?'d':'s'}"]`);x.checked=true;x.dispatchEvent(new Event('change',{bubbles:true}));});
      else if(q.type==='order')q.items.forEach((_,k)=>el.querySelector(`[data-add="${k}"]`).click());
      else q.blanks.forEach((b,k)=>{const row=el.querySelectorAll('.bl')[k];
        if(b.kind==='num')set(row.querySelector('[data-p=v]'),String(b.ans).replace('.',','));
        else if(b.kind==='sel')set(row.querySelector('select'),b.ans);
        else {const parts=b.kind==='frac'?['n','d']:['w','n','d'];parts.forEach((p,j)=>set(row.querySelector(`[data-p=${p}]`),b.ans[j]));}
      });
    });
  },mode);
}
async function overflow(page){
  const sizes=await page.evaluate(()=>({viewport:innerWidth,width:document.documentElement.scrollWidth}));
  assert.ok(sizes.width<=sizes.viewport,`Horizontal overflow ${JSON.stringify(sizes)} at ${page.url()}`);
}
async function links(page){
  const urls=await page.locator('a[href],img[src],script[src],link[rel=stylesheet]').evaluateAll(els=>els.map(e=>e.href||e.src));
  for(const url of new Set(urls)){
    if(!url.startsWith(BASE)||new URL(url).hash)continue;
    const response=await page.request.get(url);assert.equal(response.status(),200,`Broken rendered reference ${url}`);
  }
}
async function main(){
  const browser=await chromium.launch(),errors=[],results=[];
  try{
    const context=await browser.newContext({viewport:{width:400,height:900},reducedMotion:'reduce'});
    context.on('page',p=>{p.on('pageerror',e=>errors.push(`${p.url()}: ${e.message}`));p.on('console',m=>{if(m.type()==='error')errors.push(`${p.url()}: ${m.text()}`);});p.on('requestfailed',r=>errors.push(`${r.url()}: ${r.failure()?.errorText}`));});
    const page=await context.newPage();
    const go=async file=>{const r=await page.goto(BASE+file);assert.equal(r.status(),200,file);await page.evaluate(()=>document.fonts.ready);};
    for(const f of walk(SITE).filter(f=>f.endsWith('.html'))){
      const rel=relative(f);await go(rel);await overflow(page);await links(page);
      if(path.basename(f).startsWith('De')){
        const meta=await page.evaluate(()=>({count:window.__quiz.Q.length,points:window.__quiz.Q.reduce((s,q)=>s+q.pts,0)}));
        assert.deepEqual(meta,{count:24,points:100});
        const clipped=await page.locator('.fig svg text').evaluateAll(els=>els.flatMap(e=>{
          const b=e.getBBox(),svg=e.ownerSVGElement,v=svg.viewBox.baseVal;
          const matrix=svg.getScreenCTM().inverse().multiply(e.getScreenCTM());
          const points=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(matrix));
          return points.some(p=>p.x<v.x-1||p.y<v.y-1||p.x>v.x+v.width+1||p.y>v.y+v.height+1)?[e.textContent]:[];
        }));
        assert.deepEqual(clipped,[],`SVG labels outside viewBox: ${rel}`);
        if(SHOTS){
          // Capture every actual illustration, not only a sample of topics.
          const figs=page.locator('[id^=q] .fig');
          await page.addStyleTag({content:'#bar{visibility:hidden!important}'});
          for(let i=0;i<await figs.count();i++){
            await page.setViewportSize({width:1100,height:900});
            const fig=figs.nth(i),id=await fig.evaluate(e=>e.closest('[id^=q]').id);
            await fig.screenshot({path:path.join(OUT,rel.replaceAll('/','_')+'_'+id+`_${i}.png`)});
          }
          await page.setViewportSize({width:400,height:900});
          await page.addStyleTag({content:'#bar{visibility:visible!important}'});
        }
        await fillCorrect(page);await page.click('#goBtn');await page.locator('.score').waitFor();
        const score=(await page.textContent('.score')).replace(/\s+/g,' ');
        assert.match(score,/100\s*\/\s*100/);assert.equal(await page.locator('.fb.no,.fb.part').count(),0);
        await overflow(page);await links(page);results.push({file:rel,score});console.log('PASS',rel,score);
      }else if(SHOTS){
        if(path.basename(f).startsWith('TongQuan')){
          await page.setViewportSize({width:1080,height:1000});
          await page.locator('#sheetw').screenshot({path:path.join(OUT,path.basename(f,'.html')+'.png')});
        }else{
          await page.screenshot({path:path.join(OUT,rel==='index.html'?'home-mobile.png':'math-mobile.png'),fullPage:true});
          await page.setViewportSize({width:1280,height:900});
          await page.screenshot({path:path.join(OUT,rel==='index.html'?'home-desktop.png':'math-desktop.png'),fullPage:true});
        }
        await page.setViewportSize({width:400,height:900});
      }
    }
    assert.equal(results.length,36);
    await go('Toan5/index.html');assert.equal(await page.locator('#sDone').textContent(),'36');assert.equal(await page.locator('#sStar').textContent(),'108');assert.equal(await page.locator('#sBest').textContent(),'100');
    await go('index.html');assert.match(await page.locator('#math-progress').textContent(),/36\/36/);
    await page.reload();assert.match(await page.locator('#math-progress').textContent(),/108\/108/);
    // Exercise incomplete submission, partial marking, retry and best-score retention.
    const first=results[0].file;await go(first);await fillCorrect(page,'half');await page.click('#goBtn');await page.locator('#yes').waitFor();await page.click('#keep');assert.equal(await page.locator('.score').count(),0);
    await page.click('#goBtn');await page.click('#yes');await page.locator('.score').waitFor();assert.doesNotMatch(await page.locator('.score').textContent(),/^100\s*\//);
    const storage=await page.evaluate(()=>JSON.parse(localStorage.getItem('mia5:cd1-de1')));assert.equal(storage.best,100);assert.ok(storage.last<100);assert.equal(storage.tries,2);
    await page.click('#again');assert.equal(await page.locator('.score').count(),0);await fillCorrect(page);await page.click('#goBtn');await page.locator('.score').waitFor();
    await page.reload();assert.equal(await page.evaluate(()=>JSON.parse(localStorage.getItem('mia5:cd1-de1')).tries),3);
    // Fresh visitor state and light/dark mode of the shared home page.
    const fresh=await browser.newContext({viewport:{width:400,height:900},colorScheme:'dark'}),p=await fresh.newPage();
    await p.goto(BASE);await overflow(p);assert.match(await p.locator('#math-progress').textContent(),/108 sao/);
    if(SHOTS)await p.screenshot({path:path.join(OUT,'home-dark-mobile.png'),fullPage:true});
    await fresh.close();
    assert.deepEqual(errors,[]);
    const report={base:BASE,tests:results.length,htmlPages:walk(SITE).filter(f=>f.endsWith('.html')).length,viewport:400,errors,results,checkedAt:new Date().toISOString(),progress:'reload, home statistics, partial score, retry and best retained'};
    fs.writeFileSync(path.join(OUT,'report.json'),JSON.stringify(report,null,2)+'\n');
    console.log(`QA PASS: ${results.length}/36 tests, 44 pages, no browser errors; progress persisted`);
  }finally{await browser.close();}
}
main().catch(e=>{console.error(e);process.exitCode=1;});
