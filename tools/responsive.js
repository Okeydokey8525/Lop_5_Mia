const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {createRequire}=require('node:module');
const {chromium}=createRequire(path.resolve(__dirname,'../generator/package.json'))('playwright');
const ROOT=path.resolve(__dirname,'..'),SITE=path.join(ROOT,'site');
const BASE=(process.argv.slice(2).find(a=>!a.startsWith('--'))||'http://127.0.0.1:8765/Lop_5_Mia/').replace(/\/?$/,'/');
const OUT=path.join(ROOT,'artifacts',BASE.includes('127.0.0.1')?'responsive-local':'responsive-online');fs.mkdirSync(OUT,{recursive:true});
const SHOTS=!process.argv.includes('--no-shots');
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):[path.join(d,e.name)]);
async function main(){
  const browser=await chromium.launch(),errors=[],runs=[],files=walk(SITE).filter(f=>f.endsWith('.html'));
  try{
    const p=await browser.newPage({reducedMotion:'reduce'});p.on('pageerror',e=>errors.push(e.message));p.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
    for(const scheme of ['light','dark']){
      await p.emulateMedia({colorScheme:scheme});
      for(const width of [320,360,390,400,768,820,1024,1366]){
        await p.setViewportSize({width,height:900});
        for(const file of files){
          const relative=path.relative(SITE,file).split(path.sep).join('/');
          const response=await p.goto(BASE+relative);assert.equal(response.status(),200,relative);await p.evaluate(()=>document.fonts.ready);
          const distorted=await p.locator('.en-figure img').evaluateAll(async imgs=>{
            await Promise.all(imgs.map(img=>img.decode()));
            return imgs.flatMap(img=>{const r=img.getBoundingClientRect();return r.width&&Math.abs(r.width/r.height-1.5)>.01?[img.src]:[];});
          });assert.deepEqual(distorted,[],`Distorted English illustration: ${relative}`);
          const size=await p.evaluate(()=>({w:innerWidth,scroll:document.documentElement.scrollWidth}));
          assert.ok(size.scroll<=size.w,`${scheme} ${width}px ${relative}: scrollWidth ${size.scroll}`);
          if(path.basename(file).startsWith('TongQuan')){
            assert.equal(await p.locator('body').evaluate(e=>e.classList.contains('reading')),width<=820);
            const text=await p.evaluate(()=>{const normalize=s=>s.replace(/\s+/g,' ').trim();return [normalize(document.querySelector('#sheetw').textContent),normalize(document.querySelector('#reader').textContent)];});
            assert.equal(text[0],text[1],`Reader lost content: ${relative}`);
            if(width===360){
              const sizes=await p.locator('#reader p').evaluateAll(els=>els.map(e=>parseFloat(getComputedStyle(e).fontSize)));
              assert.ok(sizes.every(s=>s>=16),'Reader body text too small');
              await p.click('#view-toggle');assert.equal(await p.locator('#clip').isVisible(),true);await p.click('#view-toggle');assert.equal(await p.locator('#reader').isVisible(),true);
              await p.locator('.jump summary').click();assert.equal(await p.locator('.jump a:visible').count(),6);
              assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
              await p.locator('.jump summary').click();
            }
          }
          if(SHOTS&&[360,768,1366].includes(width)&&(!path.basename(file).startsWith('De')||relative.includes('De2_MaiNhaVaViKeo')||relative.includes('De2_TuVungVaHinhAnh'))){
            const name=relative.replaceAll('/','_').replace('.html','');
            await p.screenshot({path:path.join(OUT,`${scheme}-${width}-${name}.png`),fullPage:width===360&&path.basename(file).startsWith('TongQuan')});
          }
        }
        runs.push({scheme,width,pages:files.length});console.log(`${scheme} ${width}px: ${files.length} pages passed`);
      }
    }
    // Touch viewport: keep the primary submission action tappable and on screen.
    const touch=await browser.newContext({viewport:{width:360,height:740},isMobile:true,hasTouch:true,deviceScaleFactor:2});
    const t=await touch.newPage();await t.goto(BASE+'Toan5/ChuDe5_HinhPhangChuViDienTich/De2_MaiNhaVaViKeo.html');
    const button=await t.locator('#goBtn').boundingBox();assert.ok(button.width>=44&&button.height>=44&&button.y+button.height<=740);
    await t.click('#goBtn');await t.locator('#yes').waitFor();assert.ok((await t.locator('#yes').boundingBox()).height>=44);await t.click('#keep');await touch.close();
    for(const width of [320,360,390,768]){
      const bottom=await browser.newPage({viewport:{width,height:740}});
      await bottom.goto(BASE+'Toan5/ChuDe5_HinhPhangChuViDienTich/De2_MaiNhaVaViKeo.html');await bottom.click('#goBtn');await bottom.click('#yes');
      await bottom.locator('.score').waitFor();await bottom.evaluate(()=>document.fonts.ready);
      await bottom.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
      await bottom.evaluate(()=>scrollTo(0,document.documentElement.scrollHeight));
      const position=await bottom.evaluate(()=>({last:document.querySelector('#q24').getBoundingClientRect().bottom,bar:document.querySelector('#bar').getBoundingClientRect().top}));
      assert.ok(position.last<=position.bar,`Bottom result bar covers the final question at ${width}px`);await bottom.close();
    }
    assert.deepEqual(errors,[]);
    fs.writeFileSync(path.join(OUT,'report.json'),JSON.stringify({base:BASE,runs,pagesChecked:runs.reduce((s,r)=>s+r.pages,0),errors,touch:true,readerTextParity:true,checkedAt:new Date().toISOString()},null,2)+'\n');
    console.log('Responsive PASS:',runs.length*files.length,'page/viewport/theme combinations');
  }finally{await browser.close();}
}
main().catch(e=>{console.error(e);process.exitCode=1;});
