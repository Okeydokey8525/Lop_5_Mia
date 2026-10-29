const fs=require('fs');const f=process.argv[2];
const ctx={};ctx.window=ctx;require('vm').createContext(ctx);require('vm').runInContext(fs.readFileSync(process.argv[3],'utf8')+fs.readFileSync(f,'utf8'),ctx);
const T=ctx.window.TEST_FN({n:x=>x});
T.questions.forEach((q,i)=>{ if(q.type==='fill') console.log(i+1,q.blanks.map(b=>(b.kind==='sel'?b.pre+' ['+b.ans+'] '+b.post:b.pre+' '+b.ans+' '+(b.post||''))).join(' | ')); if(q.type==='mc') console.log(i+1,'MC ans=',q.opts[q.answer]); if(q.type==='order') console.log(i+1,q.items.join(' '+q.sep+' ')) });
