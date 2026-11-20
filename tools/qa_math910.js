// Real answer controls, misconception rejection, drafts and local standalone exports.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{pathToFileURL}=require('node:url');
const {chromium,webkit}=require('../generator/node_modules/playwright');
const ROOT=path.resolve(__dirname,'..'),BASE=(process.argv.slice(2).find(a=>!a.startsWith('--'))||'http://127.0.0.1:8765/Lop_5_Mia/').replace(/\/?$/,'/');
const browserName=process.argv.includes('--webkit')?'webkit':'chromium';
const OUT=path.join(ROOT,'artifacts','math910-'+(BASE.includes('127.0.0.1')?'local':'online')+'-'+browserName);fs.mkdirSync(OUT,{recursive:true});
const tests=require('../site/catalog.json').tests.filter(t=>/^cd(?:9|10)-de/.test(t.id));
async function fill(p){await p.evaluate(()=>__quiz.Q.forEach((q,i)=>{const e=document.getElementById('q'+(i+1)),set=(x,v)=>{x.value=v;x.dispatchEvent(new Event('input',{bubbles:true}));x.dispatchEvent(new Event('change',{bubbles:true}));};
 if(q.type==='mc'){const x=e.querySelectorAll('input')[q.answer];x.checked=true;x.dispatchEvent(new Event('change',{bubbles:true}));}
 else if(q.type==='tf')q.items.forEach((it,k)=>{const x=e.querySelector(`input[name="q${i}_${k}"][value="${it.a?'d':'s'}"]`);x.checked=true;x.dispatchEvent(new Event('change',{bubbles:true}));});
 else if(q.type==='order'){e.querySelector('[data-clr]').click();q.items.forEach((_,k)=>e.querySelector(`[data-add="${k}"]`).click());}
 else q.blanks.forEach((b,k)=>{const row=e.querySelectorAll('.bl')[k];if(b.kind==='num')set(row.querySelector('[data-p=v]'),String(b.ans).replace('.',','));else if(b.kind==='sel')set(row.querySelector('select'),b.ans);else ['n','d'].forEach((part,j)=>set(row.querySelector(`[data-p=${part}]`),String(b.ans[j])));});
}));}
async function main(){const b=await (browserName==='webkit'?webkit:chromium).launch(),errors=[],cases=[];try{
 const p=await b.newPage({viewport:{width:390,height:844},reducedMotion:'reduce'});p.on('pageerror',e=>errors.push(e.message));
 assert.equal(tests.length,12);
 for(const t of tests){await p.goto(BASE+t.file);const diagram=p.locator(t.id.startsWith('cd9')?'#q3 svg':'#q7 svg');assert.ok((await diagram.boundingBox()).width>=240,'Diagram must remain legible on a phone');await fill(p);
  const negatives=await p.evaluate(()=>{const Q=__quiz.Q,g=__quiz.gradeBlank;
   if(TEST_EXTRA.id.startsWith('cd9')){const surface=Q[2].blanks[0],open=Q[10].blanks[1],closed=Q[3].blanks[0];return [g(surface,{v:String(Q[6].blanks[0].ans)}).ok,g(open,{v:String(closed.ans)}).ok,g(surface,{v:String(surface.ans).replace('.',',')}).ok];}
   const duration=Q[8].blanks[0],minute=Q[2].blanks[1],speed=Q[13].blanks[1];return [g(duration,{v:String(duration.ans*60)}).ok,g(minute,{v:'75'}).ok,g(speed,{v:String(speed.ans*2/2.5)}).ok,g(duration,{v:String(duration.ans).replace('.',',')}).ok];
  });assert.deepEqual(negatives,t.id.startsWith('cd9')?[false,false,true]:[false,false,false,true]);
  await p.click('#goBtn');assert.match(await p.locator('.score').textContent(),/100\s*\/\s*100/);assert.equal(await p.locator('.fb.ok').count(),24);
  await p.reload();assert.match(await p.locator('.saved-result').textContent(),/100\/100/);await p.click('#reviewSaved');assert.equal(await p.locator('.fb.ok').count(),24);cases.push(t.id);
 }
 for(const cd of [9,10]){const t=tests.find(t=>t.id===`cd${cd}-de1`),folder=t.file.slice(0,t.file.lastIndexOf('/'));
  for(const theme of ['light','dark']){await p.goto(BASE);await p.evaluate(t=>localStorage.setItem('mia5:ui-theme',t),theme);
   for(const width of [320,360,390,400,768,820,1024,1366]){await p.setViewportSize({width,height:900});await p.goto(BASE+folder+`/TongQuan_ChuDe${cd}.html`);await p.evaluate(()=>document.fonts.ready);assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    assert.equal(await p.evaluate(()=>document.documentElement.dataset.theme),theme);assert.equal(await p.locator('#reader .reader-lesson').count(),7);assert.ok(await p.locator('.foot .completed').count()===6);
    assert.ok(await p.locator('#reader svg').evaluateAll(xs=>xs.length>0&&xs.every(x=>getComputedStyle(x).color==='rgb(74, 36, 51)')),'Diagram ink stays dark on the white reader panel in both themes');
    if(width===390||width===1366)await p.screenshot({path:path.join(OUT,`overview-${cd}-${theme}-${width}.png`),fullPage:true});
   }
  }
  await p.setViewportSize({width:390,height:844});await p.goto(BASE+t.file);await p.click('#reviewSaved');await p.locator(cd===9?'#q3':'#q7').screenshot({path:path.join(OUT,`diagram-${cd}.png`)});
  if(cd===9)await p.locator('#q2').screenshot({path:path.join(OUT,'nets-9.png')});
  if(BASE.includes('127.0.0.1')&&browserName==='chromium'){await p.goto(pathToFileURL(path.join(ROOT,'generator/out',t.file)).href);await fill(p);await p.click('#goBtn');assert.match(await p.locator('.score').textContent(),/100\s*\/\s*100/);}
 }
 await p.goto(BASE+'Toan5/index.html');assert.equal(await p.locator('#sDone').textContent(),'12');
 assert.match(await p.locator('#topics').textContent(),/Tập hai · Chủ đề 7–10/);
 assert.equal(await p.locator('#cd9 .stop.done,#cd10 .stop.done').count(),12);
 // Reset only mathematics; English remains isolated.
 await p.evaluate(()=>localStorage.setItem('mia5:en-u01-de1-v2',JSON.stringify({best:80,max:100,tries:1})));
 await p.click('#reset');await p.click('#yes');assert.equal(await p.locator('#sDone').textContent(),'0');assert.equal(await p.evaluate(()=>JSON.parse(localStorage.getItem('mia5:en-u01-de1-v2')).best),80);
 assert.deepEqual(errors,[]);fs.writeFileSync(path.join(OUT,'report.json'),JSON.stringify({base:BASE,browser:browserName,tests:cases,misconceptionsRejected:true,decimalComma:true,savedReview:true,isolatedReset:true,overviewLayouts:32,standalone:BASE.includes('127.0.0.1')&&browserName==='chromium',errors},null,2));
 console.log(`Math 9–10 PASS (${browserName}): 12/12 exams, wrong surface/time/unit rejected, saved review, 32 overview layouts and isolated reset.`);
}finally{await b.close();}}
main().catch(e=>{console.error(e);process.exitCode=1;});
