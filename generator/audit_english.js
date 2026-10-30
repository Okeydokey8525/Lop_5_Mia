const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
let count=0,bad=0;
// Explicit per-unit inventories: unrelated images or book scans cannot enter output.
const inventories={u01:['city','countryside','dolphin','pink','sandwich','table-tennis'],u02:['house','flat','building','tower'],u03:['friendly','helpful','clever','active'],u04:['play-the-violin','surf-the-internet','go-for-a-walk','water-the-flowers'],u05:['firefighter','reporter','gardener','writer']};
for(const [unit,names] of Object.entries(inventories)){
const images=path.join(__dirname,'english',unit,'images');
assert.deepEqual(fs.readdirSync(images).filter(f=>f.endsWith('.webp')).sort(),names.map(n=>n+'.webp').sort());
const approvedImages=new Set(names.map(n=>'data:image/webp;base64,'+fs.readFileSync(path.join(images,n+'.webp')).toString('base64')));
for(let i=1;i<=6;i++){
  try{
    const dir=path.join(__dirname,'english',unit),ctx={};ctx.window=ctx;vm.createContext(ctx);
    vm.runInContext(fs.readFileSync(path.join(dir,'common.js'),'utf8')+fs.readFileSync(path.join(dir,'tests',`de0${i}.js`),'utf8'),ctx);
    const t=ctx.TEST_FN({}),questions=t.questions;assert.equal(questions.length,24);
    assert.equal(t.meta.subject,'en');assert.equal(t.levels.reduce((s,l)=>s+l.pts*questions.filter(q=>q.level===l.id).length,0),100);
    const expected=['tb','kha','gioi'].flatMap((lv,k)=>Array([10,8,6][k]).fill(lv));
    const kinds=new Set();
    questions.forEach((q,k)=>{
      assert.equal(q.level,expected[k],`q${k+1}`);assert.ok(q.stem&&q.why&&t.lessons[q.lesson]);kinds.add(q.type);
      assert.ok(['mc','pic','tf','text','match','reorder','listen'].includes(q.type));
      if(q.type==='listen'){
        assert.ok(q.speech&&q.transcript&&q.fields.length);
        q.fields.forEach(f=>{assert.ok(f.answer&&f.label);if(f.options){assert.ok(f.options.includes(f.answer));assert.equal(new Set(f.options).size,f.options.length)}});
      }else if(q.type==='mc'||q.type==='pic'){
        assert.equal(q.opts.length,4);assert.equal(new Set(q.opts).size,4);assert.ok(Number.isInteger(q.answer)&&q.answer>=0&&q.answer<4);
        if(q.type==='pic')assert.ok(q.fig.includes('<img')&&q.fig.includes('alt="'));
      }else if(q.type==='text')assert.ok(q.answers.length&&q.answers.every(a=>typeof a==='string'&&a.trim()));
      else if(q.type==='match'){assert.ok(q.pairs.length>=3);assert.equal(new Set(q.pairs.map(p=>p.right)).size,q.pairs.length);assert.equal(new Set(q.pairs.map(p=>p.left)).size,q.pairs.length);}
      else if(q.type==='reorder')assert.ok(q.items.length>=3&&q.items.every(w=>typeof w==='string'&&w.trim()));
      else {assert.ok(q.items.length>=2);assert.ok(q.items.every(it=>typeof it.a==='boolean'));}
      for(const src of JSON.stringify(q).match(/data:image\/[^"\\]+/g)||[])assert.ok(approvedImages.has(src),'Unknown embedded image; book scans are forbidden');
    });
    assert.equal(questions.filter(q=>q.type==='listen').length,6);
    for(const lv of ['tb','kha','gioi'])assert.equal(questions.filter(q=>q.type==='listen'&&q.level===lv).length,2);
    assert.ok(kinds.size>=4,'Too little variation');count++;
  }catch(e){bad++;console.error('English '+unit+' de'+i,e.message);}
}
}
console.log(`English audit: ${count}/${Object.keys(inventories).length*6} tests, ${count*24} questions, ${bad} issues`);
if(bad)process.exitCode=1;
