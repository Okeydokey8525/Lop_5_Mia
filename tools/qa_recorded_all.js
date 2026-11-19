// Run the existing real-audio gates with bounded concurrency and separate logs.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{spawn}=require('node:child_process');
const args=process.argv.slice(2),base=args.find(a=>!a.startsWith('--'))||'http://127.0.0.1:8765/Lop_5_Mia/';
const units=(args.find(a=>a.startsWith('--units='))||'--units=11,12,13,14,15,16,17,18').split('=')[1].split(',').map(Number);
const jobs=Number((args.find(a=>a.startsWith('--jobs='))||'--jobs=3').split('=')[1]);
assert.ok(units.length&&units.every(n=>[11,12,13,14,15,16,17,18].includes(n))&&new Set(units).size===units.length);
assert.ok(Number.isInteger(jobs)&&jobs>=1&&jobs<=4);
const out=path.resolve(__dirname,'../artifacts/audio-batch-'+(base.includes('127.0.0.1')?'local':'online'));fs.mkdirSync(out,{recursive:true});
const queue=units.flatMap(unit=>[false,true].map(webkit=>({unit,webkit}))),results=[];let cursor=0;
async function worker(){
 while(cursor<queue.length){
  const task=queue[cursor++],name='u'+task.unit+'-'+(task.webkit?'webkit':'chromium'),log=path.join(out,name+'.log'),fd=fs.openSync(log,'w');
  let code;
  try{code=await new Promise((resolve,reject)=>{const child=spawn(process.execPath,[path.join(__dirname,'qa_recorded_audio.js'),base,'--unit='+task.unit,...(task.webkit?['--webkit']:[])],{stdio:['ignore',fd,fd],windowsHide:true});child.once('error',reject);child.once('close',resolve);});}
  finally{fs.closeSync(fd);}
  results.push({...task,code,log:path.relative(out,log)});console.log(name+(code===0?' PASS':' FAIL')+'\n'+fs.readFileSync(log,'utf8').slice(-1500));
 }
}
Promise.all(Array.from({length:Math.min(jobs,queue.length)},worker)).then(()=>{
 fs.writeFileSync(path.join(out,'report.json'),JSON.stringify({base,units,jobs,results},null,2));
 if(results.some(r=>r.code!==0)){process.exitCode=1;return;}
 console.log(`Recorded audio batch PASS: ${results.length} gates; Chromium and WebKit for Units ${units.join(',')}.`);
}).catch(e=>{console.error(e);process.exitCode=1;});
