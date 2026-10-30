const fs=require('node:fs'),path=require('node:path'),{pathToFileURL}=require('node:url');
const {createRequire}=require('node:module');
const {chromium}=createRequire(path.resolve(__dirname,'../generator/package.json'))('playwright');
const ROOT=path.resolve(__dirname,'..');
async function main(){
  const browser=await chromium.launch();
  try{
    const page=await browser.newPage({viewport:{width:1080,height:1000},colorScheme:'light',reducedMotion:'reduce'});
    const folders=['Toan5','TiengAnh5'].flatMap(subject=>{
      const base=path.join(ROOT,'site',subject);
      return fs.readdirSync(base,{withFileTypes:true}).filter(d=>d.isDirectory()).map(d=>({subject,name:d.name,folder:path.join(base,d.name)}));
    });
    for(const dir of folders){
      const folder=dir.folder;
      const html=fs.readdirSync(folder).find(f=>/^TongQuan_.*\.html$/.test(f));
      if(!html)throw Error('Missing overview: '+folder);
      await page.goto(pathToFileURL(path.join(folder,html)).href);
      await page.evaluate(()=>document.fonts.ready);
      await page.locator('#sheetw img').evaluateAll(imgs=>Promise.all(imgs.map(img=>img.decode())));
      const png=path.join(folder,html.replace('.html','.png'));
      await page.locator('#sheetw').screenshot({path:png});
      const standalone=path.join(ROOT,'generator','out',dir.subject,dir.name,path.basename(png));
      fs.mkdirSync(path.dirname(standalone),{recursive:true});fs.copyFileSync(png,standalone);
      console.log('Poster:',path.relative(ROOT,png));
    }
  }finally{await browser.close();}
}
main().catch(e=>{console.error(e);process.exitCode=1;});
