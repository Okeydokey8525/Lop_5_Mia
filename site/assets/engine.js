(function(){
'use strict';
var H = window.H = {};
function $(s,r){return (r||document).querySelector(s)}
function $$(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
/* {3/4} -> phân số xếp dọc; {2 3/4} -> hỗn số */
function fmt(s){
  return String(s).replace(/\{(?:(\d+)\s+)?(\d+)\/(\d+)\}/g,function(m,w,n,d){
    var f='<span class="fr"><span class="n">'+n+'</span><span class="d">'+d+'</span></span>';
    return w?'<span class="mix"><span class="wh">'+w+'</span>'+f+'</span>':f;
  });
}
function numStr(v){
  var neg=v<0, s=String(Math.abs(v)).split('.'), i=s[0].replace(/\B(?=(\d{3})+(?!\d))/g,' ');
  return (neg?'−':'')+i+(s[1]?','+s[1]:'');
}
H.n=numStr;
function pts(v){return String(Math.round(v*10)/10).replace('.',',')}
function parseNum(raw){
  var s=String(raw).trim().replace(/[\s ]/g,'');
  if(!s) return NaN;
  if(window.TEST.decimal) s=s.replace(',','.'); else s=s.replace(/[.,]/g,'');
  return /^\d+(\.\d+)?$/.test(s)?Number(s):NaN;
}

/* Hình góc (SVG) */
H.angles=function(list){
  return '<div class="fig">'+list.map(function(a){
    var vx=58,vy=66,L=46,R=15,r=a.r*Math.PI/180,t=(a.r+a.d)*Math.PI/180;
    function P(th,len){return [(vx+len*Math.cos(th)).toFixed(1),(vy-len*Math.sin(th)).toFixed(1)]}
    var e1=P(r,L),e2=P(t,L),a1=P(r,R),a2=P(t,R);
    return '<figure><svg viewBox="0 0 116 84" role="img" aria-label="Góc '+a.l+'">'+
      '<path d="M'+e1[0]+' '+e1[1]+' L'+vx+' '+vy+' L'+e2[0]+' '+e2[1]+'" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'+
      '<path d="M'+a1[0]+' '+a1[1]+' A'+R+' '+R+' 0 0 0 '+a2[0]+' '+a2[1]+'" fill="none" stroke="#e8741a" stroke-width="2"/>'+
      '<circle cx="'+vx+'" cy="'+vy+'" r="2.6" fill="currentColor"/></svg><figcaption>Góc '+a.l+'</figcaption></figure>';
  }).join('')+'</div>';
};


/* Bảng số liệu: H.table(['Món','Giá'],[['Vở','8 500'],...],'chú thích') */
H.table=function(head,rows,cap){
  return '<div class="tblw"><table class="dt">'+(cap?'<caption>'+esc(cap)+'</caption>':'')+'<thead><tr>'+head.map(function(h){return '<th>'+fmt(h)+'</th>'}).join('')+'</tr></thead><tbody>'+
    rows.map(function(r){return '<tr>'+r.map(function(c,i){return (i?'<td>':'<th scope="row">')+fmt(c)+(i?'</td>':'</th>')}).join('')+'</tr>'}).join('')+'</tbody></table></div>';
};
/* Hình chữ nhật có ghi kích thước: H.rect('dài','rộng','đơn vị',{w:..,h:..}) */
H.rect=function(a,b,note){
  return '<div class="fig"><figure><svg viewBox="0 0 190 100" role="img" aria-label="Hình chữ nhật dài '+esc(a)+', rộng '+esc(b)+'" style="width:190px">'+
    '<rect x="18" y="14" width="150" height="66" rx="3" fill="var(--soft)" stroke="currentColor" stroke-width="2.4"/>'+
    '<text x="93" y="95" text-anchor="middle" font-size="12" fill="currentColor" font-family="inherit" font-weight="700">'+esc(a)+'</text>'+
    '<text x="10" y="50" text-anchor="middle" font-size="12" fill="currentColor" font-family="inherit" font-weight="700" transform="rotate(-90 10 50)">'+esc(b)+'</text>'+
    '</svg>'+(note?'<figcaption>'+esc(note)+'</figcaption>':'')+'</figure></div>';
};
/* Tia số có vạch chia: H.numline(0,1,10,[['A',0.3],['B',0.75]],2) */
H.numline=function(min,max,steps,pts,dec){
  var W=320,x0=14,x1=W-14,y=46;
  function X(v){return x0+(v-min)/(max-min)*(x1-x0)}
  function lab(v){return String(+v.toFixed(dec||0)).replace('.',',')}
  var s='<svg viewBox="0 0 '+W+' 96" role="img" aria-label="Tia số" style="width:100%;max-width:420px"><line x1="'+x0+'" y1="'+y+'" x2="'+x1+'" y2="'+y+'" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>';
  for(var i=0;i<=steps;i++){var v=min+(max-min)*i/steps,x=X(v),big=(i===0||i===steps);
    s+='<line x1="'+x+'" y1="'+(y-(big?9:6))+'" x2="'+x+'" y2="'+(y+(big?9:6))+'" stroke="currentColor" stroke-width="2"/>';
    if(big||steps<=5) s+='<text x="'+x+'" y="'+(y+26)+'" text-anchor="middle" font-size="12" font-weight="700" fill="currentColor" font-family="inherit">'+lab(v)+'</text>';}
  (pts||[]).forEach(function(p){var x=X(p[1]);
    s+='<circle cx="'+x+'" cy="'+y+'" r="5.5" fill="#e8741a" stroke="var(--paper)" stroke-width="1.5"/><text x="'+x+'" y="'+(y-16)+'" text-anchor="middle" font-size="14" font-weight="800" fill="#e8741a" font-family="inherit">'+esc(p[0])+'</text>';});
  return '<div class="fig">'+s+'</svg></div>';
};

var T=window.TEST=window.TEST_FN(H), LV={}, Q=T.questions;
if(window.TEST_EXTRA) Object.keys(window.TEST_EXTRA).forEach(function(k){T.meta[k]=window.TEST_EXTRA[k]});
T.levels.forEach(function(l){LV[l.id]=l});
Q.forEach(function(q,i){q.i=i;q.pts=q.pts||LV[q.level].pts});

/* ---------- dựng câu hỏi ---------- */
function fracIn(id,bi){
  return '<span class="fi"><input class="in s" id="'+id+'n" data-b="'+bi+'" data-p="n" inputmode="numeric" autocomplete="off" aria-label="Tử số">'+
         '<input class="in s" id="'+id+'d" data-b="'+bi+'" data-p="d" inputmode="numeric" autocomplete="off" aria-label="Mẫu số"></span>';
}
function blankHtml(b,qi,bi){
  var id='q'+qi+'b'+bi, inner='';
  if(b.kind==='num') inner='<input class="in" id="'+id+'" data-b="'+bi+'" data-p="v" inputmode="decimal" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="Đáp án">';
  else if(b.kind==='frac') inner=fracIn(id,bi);
  else if(b.kind==='mixed') inner='<input class="in w" id="'+id+'w" data-b="'+bi+'" data-p="w" inputmode="numeric" autocomplete="off" aria-label="Phần nguyên">'+fracIn(id,bi);
  else inner='<select class="in" id="'+id+'" data-b="'+bi+'" data-p="v" aria-label="Chọn dấu"><option value="">?</option>'+b.opts.map(function(o){return '<option>'+esc(o)+'</option>'}).join('')+'</select>';
  return '<div class="bl" data-b="'+bi+'">'+(b.pre?'<span class="tx">'+fmt(b.pre)+'</span>':'')+inner+(b.post?'<span class="tx">'+fmt(b.post)+'</span>':'')+'<span class="mark" aria-hidden="true"></span></div>';
}
function blankAnsHtml(b){
  var a=b.ans, v;
  if(b.kind==='num') v='<b>'+numStr(a)+'</b>';
  else if(b.kind==='frac') v='<b>'+fmt('{'+a[0]+'/'+a[1]+'}')+'</b>';
  else if(b.kind==='mixed') v='<b>'+fmt('{'+a[0]+' '+a[1]+'/'+a[2]+'}')+'</b>';
  else v='<b>'+esc(a)+'</b>';
  return (b.pre?fmt(b.pre)+' ':'')+v+(b.post?' '+fmt(b.post):'');
}
function shuffled(n){
  var a=[],i,j,t; for(i=0;i<n;i++)a.push(i);
  do{ for(i=n-1;i>0;i--){j=Math.floor(Math.random()*(i+1));t=a[i];a[i]=a[j];a[j]=t;} }while(n>1&&a.every(function(x,k){return x===k}));
  return a;
}
var ordState={};
function buildOrder(q,host){
  var n=q.items.length, perm=shuffled(n), chosen=[]; ordState[q.i]=chosen;
  host.innerHTML='<div class="ord"><div class="lab">Bấm vào từng số theo thứ tự đúng:</div><div class="slots" data-slots></div><div class="lab">Các số cần sắp xếp:</div><div class="pool" data-pool></div><button type="button" class="clr" data-clr>Xóa làm lại</button></div>';
  var slots=$('[data-slots]',host), pool=$('[data-pool]',host);
  function draw(){
    slots.innerHTML=chosen.map(function(k,p){return (p?'<span class="sep">'+(q.sep||'<')+'</span>':'')+'<button type="button" class="chip pick" data-rm="'+p+'">'+fmt(q.items[k])+'</button>'}).join('')||'<span class="lab">(chưa chọn)</span>';
    pool.innerHTML=perm.filter(function(k){return chosen.indexOf(k)<0}).map(function(k){return '<button type="button" class="chip" data-add="'+k+'">'+fmt(q.items[k])+'</button>'}).join('');
  }
  host.addEventListener('click',function(e){
    var t=e.target.closest('button'); if(!t||t.disabled) return;
    if(t.hasAttribute('data-add')) chosen.push(+t.getAttribute('data-add'));
    else if(t.hasAttribute('data-rm')) chosen.splice(+t.getAttribute('data-rm'),1);
    else if(t.hasAttribute('data-clr')) chosen.length=0; else return;
    draw();
  });
  draw();
}
function buildQ(q){
  var el=document.createElement('article');
  el.className='q lv-'+q.level; el.id='q'+(q.i+1);
  var h='<div class="qh"><span class="qn">Câu '+(q.i+1)+'</span><span class="qt">Bài '+q.lesson+'</span><span class="qp">'+pts(q.pts)+' điểm</span></div><p class="qstem">'+fmt(q.stem)+'</p>'+(q.fig||'')+'<div class="qa" data-qa></div><div class="fb" data-fb hidden></div>';
  el.innerHTML=h;
  var host=$('[data-qa]',el), L='ABCD';
  if(q.type==='mc'){
    host.className='qa opts';
    host.innerHTML=q.opts.map(function(o,k){return '<label class="opt"><input type="radio" name="q'+q.i+'" value="'+k+'"><span class="ol">'+L[k]+'</span><span>'+fmt(o)+'</span></label>'}).join('');
  }else if(q.type==='tf'){
    host.className='qa tfs';
    host.innerHTML=q.items.map(function(it,k){return '<div class="tf" data-k="'+k+'"><span class="tt"><b>'+'abcdef'[k]+')</b> '+fmt(it.t)+'</span><span class="sw"><label><input type="radio" name="q'+q.i+'_'+k+'" value="d"><span>Đúng</span></label><label><input type="radio" name="q'+q.i+'_'+k+'" value="s"><span>Sai</span></label></span></div>'}).join('');
  }else if(q.type==='fill'){
    host.className='qa blanks';
    host.innerHTML=q.blanks.map(function(b,bi){return blankHtml(b,q.i,bi)}).join('');
  }else if(q.type==='order'){
    buildOrder(q,host);
  }
  return el;
}

/* ---------- đọc & chấm ---------- */
function readBlank(row){
  var v={}; $$('[data-p]',row).forEach(function(x){v[x.getAttribute('data-p')]=x.value.trim()}); return v;
}
function gradeBlank(b,v){
  var n,d,w,an,ad,aw;
  if(b.kind==='num'){var x=parseNum(v.v);return {ok:!isNaN(x)&&Math.abs(x-b.ans)<1e-9};}
  if(b.kind==='sel') return {ok:v.v===b.ans};
  n=parseInt(v.n,10); d=parseInt(v.d,10);
  if(!(n>=0&&d>0)) return {ok:false};
  if(b.kind==='frac'){
    an=b.ans[0]; ad=b.ans[1];
    if(b.exact||b.reduced){
      if(n===an&&d===ad) return {ok:true};
      if(n*ad===an*d) return {ok:false,note:b.note||'Giá trị đúng nhưng phân số chưa tối giản.'};
      return {ok:false};
    }
    return {ok:n*ad===an*d};
  }
  w=v.w===''||v.w===undefined?0:parseInt(v.w,10); if(isNaN(w)) return {ok:false};
  aw=b.ans[0]; an=b.ans[1]; ad=b.ans[2];
  if((w*d+n)*ad===(aw*ad+an)*d){
    if(n>=d) return {ok:false,note:'Phần phân số của hỗn số phải bé hơn 1.'};
    return {ok:true};
  }
  return {ok:false};
}
function isDone(q,el){
  var host=$('[data-qa]',el);
  if(q.type==='mc') return !!$('input:checked',host);
  if(q.type==='tf') return q.items.every(function(_,k){return !!$('input[name="q'+q.i+'_'+k+'"]:checked',host)});
  if(q.type==='order') return ordState[q.i].length===q.items.length;
  return $$('.in',host).every(function(x){return x.value.trim()!==''||x.getAttribute('data-p')==='w'});
}
function gradeQ(q,el){
  var host=$('[data-qa]',el), notes=[], frac=0, ansHtml='', L='ABCD';
  if(q.type==='mc'){
    var c=$('input:checked',host), pick=c?+c.value:-1;
    frac=pick===q.answer?1:0;
    $$('.opt',host).forEach(function(o,k){if(k===q.answer)o.classList.add('good');else if(k===pick)o.classList.add('bad')});
    ansHtml=L[q.answer]+'. '+fmt(q.opts[q.answer]);
  }else if(q.type==='tf'){
    var ok=0; ansHtml=[];
    q.items.forEach(function(it,k){
      var c=$('input[name="q'+q.i+'_'+k+'"]:checked',host), val=c?c.value:'', right=(val==='d')===it.a&&val!=='';
      if(right) ok++;
      $('.tf[data-k="'+k+'"]',host).classList.add(right?'good':'bad');
      ansHtml.push('<b>'+'abcdef'[k]+')</b> '+(it.a?'Đúng':'Sai'));
    });
    frac=ok/q.items.length; ansHtml=ansHtml.join(' &nbsp; ');
  }else if(q.type==='order'){
    var s=ordState[q.i], right=s.length===q.items.length&&s.every(function(k,p){return k===p});
    frac=right?1:0; $('.slots',host).classList.add(right?'good':'bad');
    ansHtml=q.items.map(fmt).join(' '+(q.sep||'<')+' ');
  }else{
    var ok2=0, rows=$$('.bl',host); ansHtml=[];
    q.blanks.forEach(function(b,bi){
      var r=gradeBlank(b,readBlank(rows[bi]));
      if(r.ok) ok2++; if(r.note) notes.push(r.note);
      rows[bi].classList.add(r.ok?'good':'bad'); $('.mark',rows[bi]).textContent=r.ok?'✓':'✗';
      ansHtml.push(blankAnsHtml(b));
    });
    frac=ok2/q.blanks.length; ansHtml=ansHtml.join('<br>');
  }
  $$('input,select,button',el).forEach(function(x){x.disabled=true});
  return {frac:frac,notes:notes,ansHtml:ansHtml};
}

/* ---------- trang ---------- */
var root=$('#app'), submitted=false, startedAt=0, timerId=0;
function build(){
  submitted=false; startedAt=0; clearInterval(timerId); ordState={};
  var m=T.meta, total=Q.reduce(function(s,q){return s+q.pts},0);
  var html='<header class="hero"><div class="hero-in">'+(m.home?'<a class="back" href="'+esc(m.home)+'">← Trang chủ</a>':'')+'<p class="eyebrow">'+esc(m.book)+'</p><h1>'+esc(m.title)+'</h1><p class="sub">'+esc(m.topic)+' · '+esc(m.range)+'</p>'+(m.theme?'<p class="theme">'+esc(m.theme)+'</p>':'')+
    '<ul class="chips"><li>'+Q.length+' câu</li><li>'+pts(total)+' điểm</li><li>'+m.minutes+' phút</li><li>3 mức: Trung bình · Khá · Giỏi</li></ul></div></header>'+
    '<section class="intro"><div><label for="stuName">Tên của em</label><input class="name" id="stuName" autocomplete="off" placeholder="Viết tên vào đây"></div><ul>'+
    '<li>Làm theo thứ tự nào cũng được. Câu nào chưa chắc, em có thể làm sau.</li>'+
    (m.tip?'<li>'+m.tip+'</li>':'<li>Ô phân số: số trên là tử số, số dưới là mẫu số.</li>')+
    '<li>Làm xong bấm <b>Nộp bài</b> ở thanh phía dưới để xem điểm và lời giải.</li></ul></section><div id="result"></div><main id="test"></main>';
  root.innerHTML=html;
  var main=$('#test');
  T.levels.forEach(function(l){
    var sec=document.createElement('section'); sec.className='lv lv-'+l.id;
    var qs=Q.filter(function(q){return q.level===l.id});
    sec.innerHTML='<div class="lvh"><span class="st" aria-hidden="true">'+'★'.repeat(l.stars)+'</span><div><h2>'+esc(l.name)+'</h2><p>'+esc(l.desc)+' · '+qs.length+' câu × '+pts(l.pts)+' điểm</p></div></div><div class="qs-wrap"></div>';
    var wrap=$('.qs-wrap',sec); qs.forEach(function(q){wrap.appendChild(buildQ(q))});
    main.appendChild(sec);
  });
  bar('run'); progress();
}
function bar(mode,extra){
  var b=$('#bar'); b.setAttribute('data-mode',mode);
  var inn=$('.bar-in',b);
  if(mode==='run'){
    inn.innerHTML='<div class="stat"><div class="txt"><span id="prog"></span> · <span id="timer">00:00</span></div><div class="pg"><i id="pgi"></i></div></div><button class="btn go" id="goBtn" type="button">Nộp bài</button>';
    $('#goBtn').onclick=trySubmit; progress(); tick();
  }else if(mode==='confirm'){
    inn.innerHTML='<div class="stat txt">Còn '+extra+' câu chưa làm. Em muốn nộp luôn không?</div><div class="conf"><button class="btn alt" type="button" id="keep">Làm tiếp</button><button class="btn" type="button" id="yes">Nộp luôn</button></div>';
    $('#keep').onclick=function(){bar('run')}; $('#yes').onclick=submit;
  }else{
    inn.innerHTML='<div class="stat txt">Đã nộp bài. Xem lại lời giải từng câu bên dưới.</div><div class="conf"><button class="btn alt" type="button" id="top">Xem kết quả</button><button class="btn" type="button" id="again">Làm lại</button></div>';
    $('#top').onclick=function(){$('#result').scrollIntoView({behavior:'smooth',block:'start'})}; $('#again').onclick=function(){build();window.scrollTo(0,0)};
  }
}
function done(){return Q.filter(function(q){return isDone(q,$('#q'+(q.i+1)))}).length}
function progress(){
  if(submitted) return;
  var d=done(), p=$('#prog'); if(!p) return;
  p.textContent='Đã làm '+d+'/'+Q.length; $('#pgi').style.width=(d/Q.length*100)+'%';
}
function tick(){
  var t=$('#timer'); if(!t||submitted) return;
  var s=startedAt?Math.floor((Date.now()-startedAt)/1000):0;
  t.textContent=('0'+Math.floor(s/60)).slice(-2)+':'+('0'+s%60).slice(-2);
}
function startTimer(){ if(startedAt||submitted) return; startedAt=Date.now(); timerId=setInterval(tick,1000); }
function trySubmit(){ var n=Q.length-done(); if(n>0) bar('confirm',n); else submit(); }
function save(score,max,rank,secs){
  if(!T.meta.id) return;
  try{
    var k='mia5:'+T.meta.id, old=JSON.parse(localStorage.getItem(k)||'null')||{tries:0,best:0};
    var sc=Math.round(score*10)/10;
    localStorage.setItem(k,JSON.stringify({tries:old.tries+1,best:Math.max(old.best,sc),last:sc,max:max,rank:rank,secs:secs,at:Date.now()}));
  }catch(e){}
}
function submit(){
  if(submitted) return; submitted=true; clearInterval(timerId);
  var secs=startedAt?Math.round((Date.now()-startedAt)/1000):0;
  var res=Q.map(function(q){
    var el=$('#q'+(q.i+1)), g=gradeQ(q,el), earned=Math.round(q.pts*g.frac*10)/10;
    var st=g.frac===1?'ok':(g.frac===0?'no':'part'), fb=$('[data-fb]',el);
    var vd=st==='ok'?'Đúng rồi! +'+pts(earned)+' điểm':(st==='no'?'Chưa đúng. +0 điểm':'Đúng một phần. +'+pts(earned)+'/'+pts(q.pts)+' điểm');
    fb.className='fb '+st; fb.hidden=false;
    fb.innerHTML='<p class="vd">'+vd+'</p><p class="ans">'+(st==='ok'?'Đáp án: ':'Đáp án đúng: ')+g.ansHtml+'</p>'+(g.notes.length?'<p class="note">'+esc(g.notes[0])+'</p>':'')+'<p class="why">'+fmt(q.why)+'</p>';
    return {q:q,earned:earned,st:st};
  });
  var total=res.reduce(function(s,r){return s+r.earned},0), max=Q.reduce(function(s,q){return s+q.pts},0), pc=total/max*100;
  var rank=pc>=80?'Giỏi':pc>=60?'Khá':pc>=40?'Trung bình':'Cần cố gắng thêm';
  var name=($('#stuName').value||'').trim();
  var rows=T.levels.map(function(l){
    var rs=res.filter(function(r){return r.q.level===l.id}), e=rs.reduce(function(s,r){return s+r.earned},0), mx=rs.reduce(function(s,r){return s+r.q.pts},0);
    var full=rs.filter(function(r){return r.st==='ok'}).length;
    return '<div class="row lv-'+l.id+'"><span class="nm">'+esc(l.name)+'</span><div class="bar-t"><i style="width:'+(e/mx*100)+'%"></i></div><span class="pt">'+pts(e)+'/'+pts(mx)+' · '+full+'/'+rs.length+' câu đúng</span></div>';
  }).join('');
  var weak={}; res.forEach(function(r){if(r.st!=='ok') weak[r.q.lesson]=1});
  var wl=Object.keys(weak).sort(function(a,b){return a-b}).map(function(k){return '<b>Bài '+k+'</b> ('+esc(T.lessons[k])+')'});
  var lvPc={}; T.levels.forEach(function(l){var rs=res.filter(function(r){return r.q.level===l.id});lvPc[l.id]=rs.reduce(function(s,r){return s+r.earned},0)/rs.reduce(function(s,r){return s+r.q.pts},0)});
  var adv=lvPc[T.levels[0].id]<0.7?'Em nên ôn kĩ các câu mức Trung bình trước, vì đó là nền tảng cho các câu khó hơn.':
          lvPc[T.levels[1].id]<0.6?'Phần Trung bình em làm khá chắc. Hãy luyện thêm các câu mức Khá, nhất là những câu bị sai bên dưới.':
          lvPc[T.levels[2].id]<0.6?'Em làm tốt hai mức đầu. Các bài toán có lời văn và tính thuận tiện ở mức Giỏi cần luyện thêm.':'Em nắm rất vững phần này. Em có thể sang chủ đề tiếp theo.';
  var mm=Math.floor(secs/60), ss=secs%60;
  $('#result').innerHTML='<section class="result" id="resultBox"><h2>'+(name?'Kết quả của '+esc(name):'Kết quả bài làm')+'</h2><div class="score"><b>'+pts(total)+'</b><span>/ '+pts(max)+' điểm</span><span class="rank">'+rank+'</span></div>'+
    '<p>Thời gian làm bài: '+mm+' phút '+ss+' giây (đề này dự kiến '+T.meta.minutes+' phút).</p><div class="lvr">'+rows+'</div>'+
    '<p>'+adv+'</p>'+(wl.length?'<p class="review">Phần cần xem lại: '+wl.join('; ')+'.</p>':'<p class="review">Em đã làm đúng tất cả các câu.</p>')+
    '<div class="actions"><button class="btn" type="button" id="firstWrong">Xem các câu chưa đúng</button><button class="btn alt" type="button" id="redo">Làm lại bài</button></div></section>';
  $('#firstWrong').onclick=function(){var w=res.filter(function(r){return r.st!=='ok'})[0]; var t=w?$('#q'+(w.q.i+1)):$('#test'); t.scrollIntoView({behavior:'smooth',block:'start'})};
  $('#redo').onclick=function(){build();window.scrollTo(0,0)};
  save(total,max,rank,secs);
  var nav=(T.meta.prev?'<a class="btn alt" href="'+esc(T.meta.prev)+'">← Đề trước</a>':'')+(T.meta.next?'<a class="btn" href="'+esc(T.meta.next)+'">Đề tiếp theo →</a>':'')+(T.meta.home?'<a class="btn alt" href="'+esc(T.meta.home)+'">Về trang chủ</a>':'');
  if(nav) $('#resultBox .actions').insertAdjacentHTML('beforeend',nav);
  bar('done'); $('#resultBox').scrollIntoView({block:'start'});
}
document.addEventListener('input',function(e){ if(e.target.closest&&e.target.closest('#test')){startTimer();progress()} });
document.addEventListener('change',function(e){ if(e.target.closest&&e.target.closest('#test')){startTimer();progress()} });
document.addEventListener('click',function(e){ if(e.target.closest&&e.target.closest('#test .chip')){startTimer();progress()} });
build();
window.__quiz={Q:Q,build:build,submit:submit};
})();
