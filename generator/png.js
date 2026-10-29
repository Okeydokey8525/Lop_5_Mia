const fs=require('node:fs'); const shotDir=require('node:path').join(__dirname,'out','qa'); fs.mkdirSync(shotDir,{recursive:true}); process.chdir(__dirname);
const {pathToFileURL}=require('node:url');
const { chromium } = require('playwright'); const path=require('path');
(async()=>{
 const b=await chromium.launch();
 for(const [dir,name] of [['ChuDe1_OnTapVaBoSung','TongQuan_ChuDe1'],['ChuDe2_SoThapPhan','TongQuan_ChuDe2'],['ChuDe3_DonViDoDienTich','TongQuan_ChuDe3'],['ChuDe4_PhepTinhSoThapPhan','TongQuan_ChuDe4'],['ChuDe5_HinhPhangChuViDienTich','TongQuan_ChuDe5'],['ChuDe6_OnTapHocKi1','TongQuan_ChuDe6']]){
  const f=path.resolve(`out/Toan5/${dir}/${name}.html`);
  const p=await b.newPage({viewport:{width:1080,height:1000}});
  await p.goto(pathToFileURL(f).href); await p.waitForTimeout(800);
  const over=await p.evaluate(()=>{const r=[];document.querySelectorAll('#sheetw div,#sheetw span,#sheetw p').forEach(e=>{if(e.scrollWidth>e.clientWidth+1&&getComputedStyle(e).display!=='inline')r.push(e.textContent.slice(0,40))});return r.slice(0,8)});
  const h=await p.evaluate(()=>document.getElementById('sheetw').offsetHeight);
  await (await p.$('#sheetw')).screenshot({path:`out/Toan5/${dir}/${name}.png`});
  console.log(name,'h',h,'overflow',over);
  await p.close();
  const m=await b.newPage({viewport:{width:400,height:800}});
  await m.goto(pathToFileURL(f).href); await m.waitForTimeout(600);
  console.log(' mobile scrollW',await m.evaluate(()=>document.documentElement.scrollWidth));
  await m.screenshot({path:path.join(shotDir,`m_${name}.png`)}); await m.close();
 }
 await b.close();
})().catch(e=>{console.error(e);process.exitCode=1;});
