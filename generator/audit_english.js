const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
let count=0,bad=0;
// Only our six generated, reviewed illustrations may be embedded in standalone output.
const images=path.join(__dirname,'english','u01','images');
const approvedImages=new Set(fs.readdirSync(images).filter(f=>f.endsWith('.webp')).map(f=>'data:image/webp;base64,'+fs.readFileSync(path.join(images,f)).toString('base64')));
assert.equal(approvedImages.size,6);
for(let i=1;i<=6;i++){
  try{
    const dir=path.join(__dirname,'english','u01'),ctx={};ctx.window=ctx;vm.createContext(ctx);
    vm.runInContext(fs.readFileSync(path.join(dir,'common.js'),'utf8')+fs.readFileSync(path.join(dir,'tests',`de0${i}.js`),'utf8'),ctx);
    const t=ctx.TEST_FN({}),questions=t.questions;assert.equal(questions.length,24);
    assert.equal(t.meta.subject,'en');assert.equal(t.levels.reduce((s,l)=>s+l.pts*questions.filter(q=>q.level===l.id).length,0),100);
    const expected=['tb','kha','gioi'].flatMap((lv,k)=>Array([10,8,6][k]).fill(lv));
    const kinds=new Set();
    questions.forEach((q,k)=>{
      assert.equal(q.level,expected[k],`q${k+1}`);assert.ok(q.stem&&q.why&&t.lessons[q.lesson]);kinds.add(q.type);
      assert.ok(['mc','pic','tf','text','match','reorder'].includes(q.type));
      if(q.type==='mc'||q.type==='pic'){
        assert.equal(q.opts.length,4);assert.equal(new Set(q.opts).size,4);assert.ok(Number.isInteger(q.answer)&&q.answer>=0&&q.answer<4);
        if(q.type==='pic')assert.ok(q.fig.includes('<img')&&q.fig.includes('alt="'));
      }else if(q.type==='text')assert.ok(q.answers.length&&q.answers.every(a=>typeof a==='string'&&a.trim()));
      else if(q.type==='match'){assert.ok(q.pairs.length>=3);assert.equal(new Set(q.pairs.map(p=>p.right)).size,q.pairs.length);assert.equal(new Set(q.pairs.map(p=>p.left)).size,q.pairs.length);}
      else if(q.type==='reorder')assert.ok(q.items.length>=3&&q.items.every(w=>typeof w==='string'&&w.trim()));
      else {assert.ok(q.items.length>=2);assert.ok(q.items.every(it=>typeof it.a==='boolean'));}
      for(const src of JSON.stringify(q).match(/data:image\/[^"\\]+/g)||[])assert.ok(approvedImages.has(src),'Unknown embedded image; book scans are forbidden');
    });
    assert.ok(kinds.size>=4,'Too little variation');count++;
  }catch(e){bad++;console.error('English Unit1 de'+i,e.message);}
}
console.log(`English audit: ${count}/6 tests, ${count*24} questions, ${bad} issues`);
if(bad)process.exitCode=1;
