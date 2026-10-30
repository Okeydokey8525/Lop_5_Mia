(function(){'use strict';
 const catalog=JSON.parse(document.getElementById('home-tests').textContent),marker='mia5:home-celebrated',reduce=matchMedia('(prefers-reduced-motion:reduce)');
 function read(key){try{return JSON.parse(localStorage.getItem(key)||'null')}catch(e){return null}}
 function record(id){const r=read('mia5:'+id);return r&&typeof r==='object'&&Number.isFinite(r.best)&&Number.isFinite(r.max)&&r.max>0&&r.best>=0&&r.best<=r.max?r:null}
 function update(){
  let name='';try{name=localStorage.getItem('mia5:name')||''}catch(e){}name=Array.from(name.trim()).slice(0,24).join('');document.getElementById('welcome').textContent='Chào '+(name||'Mia')+'!';
  const snapshot={},previous=read(marker);const hasBaseline=previous&&typeof previous==='object'&&!Array.isArray(previous);let completedAgain=false;
  for(const subject of ['math','en']){
   const tests=catalog.filter(t=>t.subject===subject);let done=0,stars=0;
   tests.forEach(t=>{const r=record(t.id);if(!r)return;done++;const pct=r.best/r.max*100;stars+=pct>=80?3:pct>=60?2:pct>=40?1:0;const tries=Number.isFinite(r.tries)&&r.tries>0?r.tries:0,at=Number.isFinite(r.at)&&r.at>0?r.at:0;snapshot[t.id]={tries,at};const old=hasBaseline?previous[t.id]:null;if(hasBaseline&&(tries>(Number(old?.tries)||0)||at>(Number(old?.at)||0)))completedAgain=true;});
   const box=document.getElementById(subject==='math'?'math-progress':'english-progress'),count=tests.length,maxStars=count*3;
   box.querySelector('.progress-text').textContent='Hành trình '+(subject==='math'?'Toán':'Tiếng Anh')+': '+done+'/'+count+' đề · '+stars+'/'+maxStars+' sao';
   const bar=box.querySelector('[role=progressbar]');bar.setAttribute('aria-valuenow',String(done));bar.setAttribute('aria-valuemax',String(count));bar.setAttribute('aria-valuetext',done+'/'+count+' đề đã hoàn thành');bar.style.setProperty('--progress',(count?done/count*100:0)+'%');
   box.querySelector('.encourage').textContent=done===count?'Em đã luyện đủ các đề! Có thể ôn lại theo nhịp của mình.':done?'Từng bước một, em đang tiến lên!':subject==='math'?'Bắt đầu với một đề nhỏ nhé!':'Khám phá Unit 1–3 cùng một chút luyện nghe!';
  }
  let saved=false;try{localStorage.setItem(marker,JSON.stringify(snapshot));saved=true}catch(e){}
  const banner=document.getElementById('celebration');banner.hidden=!(completedAgain&&saved);
  const sparkles=banner.querySelector('.sparkles');sparkles.replaceChildren();
  if(!banner.hidden&&!reduce.matches){for(let i=0;i<8;i++){const star=document.createElement('span');star.textContent='★';star.style.setProperty('--x',(-120+i*34)+'px');star.style.setProperty('--y',(-35-(i%3)*22)+'px');star.style.color=i%2?'#ED80B0':'#D89517';sparkles.appendChild(star);}setTimeout(()=>sparkles.replaceChildren(),1100);}
 }
 document.getElementById('dismiss-celebration').onclick=()=>document.getElementById('celebration').hidden=true;
 reduce.addEventListener('change',()=>{if(reduce.matches)document.querySelector('.sparkles').replaceChildren()});
 window.addEventListener('pageshow',e=>{if(e.persisted)update()});
 update();
})();
