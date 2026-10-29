// Independent value calculation for existing order questions. Unknown forms fail.
function value(text,stem=''){
  const s=String(text).replace(/\u00a0/g,' ').replace(/,/g,'.').replace(/−/g,'-').trim();
  if(/^[\d\s.]+$/.test(s))return Number(s.replace(/\s/g,''));
  const fraction=s.match(/^\{(?:(\d+)\s+)?(\d+)\/(\d+)\}$/);
  if(fraction)return Number(fraction[1]||0)+Number(fraction[2])/Number(fraction[3]);
  const expression=s.replace(/\s/g,'').match(/^([\d.]+)([+\-×:])([\d.]+)$/);
  if(expression){const a=Number(expression[1]),b=Number(expression[3]);return {'+':()=>a+b,'-':()=>a-b,'×':()=>a*b,':':()=>a/b}[expression[2]]();}
  const units={'km²':1e6,ha:1e4,'m²':1,'dm²':.01,'cm²':.0001,km:1000,m:1,dm:.1,cm:.01,mm:.001,'tấn':1000,'tạ':100,'yến':10,kg:1,g:.001,l:1,ml:.001};
  const measure=/([\d.]+(?:\s+\d{3})*)\s*(km²|cm²|dm²|m²|ha|km|dm|cm|mm|ml|kg|tấn|tạ|yến|m|g|l)/g;
  const parts=[...s.matchAll(measure)];
  if(parts.length&&s.replace(measure,'').trim()==='')return parts.reduce((n,p)=>n+Number(p[1].replace(/\s/g,''))*units[p[2]],0);
  const n=[...s.matchAll(/\d+(?:\.\d+)?/g)].map(m=>Number(m[0]));
  const shape=(s+' '+stem).toLowerCase(),perimeter=stem.includes('chu vi');
  if(shape.includes('hình tròn')){const radius=s.includes('đường kính')?n[0]/2:n[0];return perimeter?2*3.14*radius:3.14*radius*radius;}
  if(shape.includes('hình vuông'))return perimeter?n[0]*4:n[0]*n[0];
  if(shape.includes('chữ nhật'))return perimeter?(n[0]+n[1])*2:n[0]*n[1];
  if(shape.includes('tam giác'))return n[0]*n[1]/2;
  if(shape.includes('hình thang'))return (n[0]+n[1])*n[2]/2;
  return NaN;
}
function values(q){
  const result=q.items.map(s=>value(s,q.stem));
  if(result.every(Number.isFinite))return result;
  // Named pupils are ranked from the actual table attached to the question.
  if(q.fig){try{const table=JSON.parse(q.fig),map=new Map(table.rows.map(r=>[r[0],value(r[1])]));return q.items.map(s=>map.get(s));}catch{}}
  return result;
}
module.exports={value,values};
