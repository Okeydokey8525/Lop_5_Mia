const fs=require('fs'),vm=require('vm');
const H={angles:()=>'',table:()=>'',rect:()=>'',numline:()=>'',n:x=>{const neg=x<0,p=String(Math.abs(x)).split('.');return (neg?'-':'')+p[0].replace(/\B(?=(\d{3})+(?!\d))/g,' ')+(p[1]?','+p[1]:'')}};
let bad=0;
for(const cd of (process.argv[2]||'1,2,3,4').split(',').map(Number)) for(let i=1;i<=6;i++){ if(!fs.existsSync(`tests/cd${cd}/de0${i}.js`)) continue;
  const f=`tests/cd${cd}/de0${i}.js`; const ctx={}; ctx.window=ctx;
  vm.createContext(ctx); vm.runInContext(fs.readFileSync(`common/cd${cd}.js`,'utf8')+fs.readFileSync(f,'utf8'),ctx);
  const T=ctx.window.TEST_FN(H);
  T.questions.forEach((q,k)=>{
    const id=`cd${cd}de${i}q${k+1}`;
    if(q.type==='order'){
      const toNum=s=>{const m=s.replace(/\s/g,'').replace(',','.');return /^[\d.]+$/.test(m)?parseFloat(m):NaN};
      const v=q.items.map(toNum); if(v.every(x=>!isNaN(x))){ for(let j=1;j<v.length;j++) if(!(v[j]>v[j-1])){console.log('ORDER BAD',id,q.items);bad++;break;} }
    }
    if(q.type==='mc'){ if(q.answer<0||q.answer>=q.opts.length||new Set(q.opts).size!==q.opts.length){console.log('MC BAD',id);bad++} }
    if(q.type==='fill') q.blanks.forEach((b,bi)=>{
      if(b.kind==='sel'){ const m=b.pre.replace(/\{.*?\}/g,m=>{const[a,c]=m.slice(1,-1).split('/');return a/c}).replace(/[^\d.,]/g,'');}
    });
  });
  const n=T.questions.length, lv={}; T.questions.forEach(q=>lv[q.level]=(lv[q.level]||0)+1);
  if(n!==24||lv.tb!==10||lv.kha!==8||lv.gioi!==6){console.log('COUNT BAD',f,lv);bad++}
}
console.log('audit done, issues:',bad);
