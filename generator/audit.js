const fs=require('fs'),vm=require('vm');
const {values}=require('./audit_order');
process.chdir(__dirname);
const H={angles:()=>'',table:(head,rows)=>JSON.stringify({head,rows}),rect:()=>'',numline:()=>'',n:x=>{const neg=x<0,p=String(Math.abs(x)).split('.');return (neg?'-':'')+p[0].replace(/\B(?=(\d{3})+(?!\d))/g,' ')+(p[1]?','+p[1]:'')}};
let bad=0;
let checked=0;
for(const cd of (process.argv[2]||'1,2,3,4,5,6').split(',').map(Number)) for(let i=1;i<=6;i++){ if(!fs.existsSync(`tests/cd${cd}/de0${i}.js`)){console.error('MISSING',cd,i);bad++;continue;}
  checked++;
  const f=`tests/cd${cd}/de0${i}.js`; const ctx={}; ctx.window=ctx;
  vm.createContext(ctx); vm.runInContext(fs.readFileSync(`common/cd${cd}.js`,'utf8')+fs.readFileSync(f,'utf8'),ctx);
  const T=ctx.window.TEST_FN(H);
  T.questions.forEach((q,k)=>{
    const id=`cd${cd}de${i}q${k+1}`;
    if(q.type==='order'){
      const v=values(q); if(!v.every(Number.isFinite)||!['<','>'].includes(q.sep||'<')){console.log('ORDER INVALID',id);bad++;}
      else for(let j=1;j<v.length;j++) if(!(q.sep==='>'?v[j]<v[j-1]:v[j]>v[j-1])){console.log('ORDER BAD',id,q.items);bad++;break;}
    }
    if(q.type==='mc'){ if(!Number.isInteger(q.answer)||q.answer<0||q.answer>=4||q.opts.length!==4||new Set(q.opts).size!==4){console.log('MC BAD',id);bad++} }
    if(!q.stem||!q.why||!T.lessons[q.lesson]||!['mc','tf','fill','order'].includes(q.type)){console.log('SCHEMA BAD',id);bad++;}
    if(q.type==='tf'&&(!q.items.length||q.items.some(it=>typeof it.a!=='boolean'))){console.log('TF BAD',id);bad++;}
    if(q.type==='fill') q.blanks.forEach((b,bi)=>{
      if(b.kind==='sel'){ const m=b.pre.replace(/\{.*?\}/g,m=>{const[a,c]=m.slice(1,-1).split('/');return a/c}).replace(/[^\d.,]/g,'');}
    });
  });
  const n=T.questions.length, lv={}; T.questions.forEach(q=>lv[q.level]=(lv[q.level]||0)+1);
  if(n!==24||lv.tb!==10||lv.kha!==8||lv.gioi!==6){console.log('COUNT BAD',f,lv);bad++}
  const sequence=['tb','kha','gioi'].flatMap((l,k)=>Array([10,8,6][k]).fill(l));
  if(T.questions.some((q,k)=>q.level!==sequence[k])||T.questions.reduce((s,q)=>s+(T.levels.find(l=>l.id===q.level)?.pts||0),0)!==100){console.log('LEVEL/POINTS BAD',f);bad++;}
}
console.log('audit done, tests:',checked,'issues:',bad);
if(bad||!checked)process.exitCode=1;
if(!process.argv[2]){
  const result=require('node:child_process').spawnSync(process.execPath,[require('node:path').join(__dirname,'audit_english.js')],{stdio:'inherit'});
  if(result.status!==0)process.exitCode=1;
}
