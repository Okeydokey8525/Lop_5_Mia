(function(){'use strict';
 const data=JSON.parse(document.getElementById('study-data').textContent),words=data.words,byId=Object.fromEntries(words.map(w=>[w.id,w])),questions=data.exercises,byQuestion=Object.fromEntries(questions.map(q=>[q.id,q]));
 const $=s=>document.querySelector(s),key=data.key,pending=new Map();let storageError=false,reviewOnly=false,saveTimer;
 const empty=()=>({schema:1,words:{},practice:{},group:data.groups[0].id});
 function normalise(value){return value.trim().toLowerCase().replace(/[’‘]/g,"'").replace(/\s+/g,' ').replace(/[.!?]+$/,'');}
 function isCorrect(q,answer){return [q.answer,...q.alternatives||[]].some(a=>normalise(answer)===normalise(a));}
 function readState(){
  const clean=empty();
  try{let raw=JSON.parse(localStorage.getItem(key)||'null'),legacy=false;if(!raw&&data.legacyKey){raw=JSON.parse(localStorage.getItem(data.legacyKey)||'null');legacy=true;}if(!raw||raw.schema!==1)return clean;
   words.forEach(w=>{if((!legacy||data.legacyWords.includes(w.id))&&['practised','review'].includes(raw.words?.[w.id]))clean.words[w.id]=raw.words[w.id];});
   if(legacy)return clean;
   questions.forEach(q=>{const r=raw.practice?.[q.id];if(!r||r.signature!==q.signature||typeof r.answer!=='string'||r.answer.length>250||typeof r.checked!=='boolean')return;if(q.kind!=='text'&&r.answer!==''&&!q.options.includes(r.answer))return;clean.practice[q.id]={answer:r.answer,checked:r.checked,signature:q.signature};});
   if(data.groups.some(g=>g.id===raw.group))clean.group=raw.group;return clean;
  }catch(e){storageError=true;return clean;}
 }
 let state=readState();
 function storageStatus(saved){$('#storage-status').textContent=storageError?'Chưa lưu được trên trình duyệt này. Em hãy giữ trang mở để làm tiếp.':saved?'✓ Đã lưu lựa chọn và bài luyện trên trình duyệt này.':'Tự đánh dấu và câu trả lời được lưu riêng trên trình duyệt này.';}
 function progress(){
  let practised=0,review=0;
  words.forEach(w=>{const status=state.words[w.id];if(status==='practised')practised++;if(status==='review')review++;document.querySelectorAll('[data-mark="'+w.id+'"]').forEach(b=>b.setAttribute('aria-pressed',String(status===b.dataset.value)));$('[data-mark-status="'+w.id+'"]').textContent=status==='practised'?'✓ Em đã đánh dấu đã luyện':status==='review'?'♡ Em muốn ôn lại từ/cụm này':'Chưa đánh dấu';});
  $('#progress').textContent=practised+'/'+words.length+' từ/cụm đã luyện · '+review+' cần ôn';
  const done=questions.filter(q=>state.practice[q.id]?.checked&&isCorrect(q,state.practice[q.id].answer)).length;
  $('#practice-total').textContent='Bài luyện đã làm đúng: '+done+'/'+questions.length+'.';
  const groupQuestions=questions.filter(q=>q.group===state.group),groupDone=groupQuestions.filter(q=>state.practice[q.id]?.checked&&isCorrect(q,state.practice[q.id].answer)).length;
  $('#practice-progress').textContent=groupDone===groupQuestions.length?'🌸 Em đã làm đúng cả '+groupDone+' bài trong nhóm này!':'Em đã làm đúng '+groupDone+'/'+groupQuestions.length+' bài trong nhóm này.';
 }
 function filter(){
  const group=data.groups.find(g=>g.id===state.group);let visible=0;
  document.querySelectorAll('.word-card').forEach(card=>{const show=reviewOnly?state.words[card.dataset.word]==='review':card.dataset.group===state.group;card.hidden=!show;if(show)visible++;});
  document.querySelectorAll('.dialogue,.exercise,.tip[data-group]').forEach(el=>el.hidden=reviewOnly||el.dataset.group!==state.group);
  $('#dialogues').hidden=reviewOnly;$('#practice').hidden=reviewOnly;$('#review-empty').hidden=!reviewOnly||visible>0;
  $('#only-review').setAttribute('aria-pressed',String(reviewOnly));$('#only-review').textContent=reviewOnly?'← Trở lại nhóm bài học':'♡ Chỉ xem từ cần ôn';
  document.querySelectorAll('[data-group-select]').forEach(b=>b.setAttribute('aria-pressed',String(!reviewOnly&&b.dataset.groupSelect===state.group)));
  $('#group-summary').textContent=reviewOnly?'Các từ/cụm cần ôn: '+visible+'.':group.name+' · '+visible+' từ/cụm · Chọn một nhóm khác khi em sẵn sàng.';
 }
 function flush(patch){
  if(!pending.size&&!patch)return;clearTimeout(saveTimer);storageError=false;const fresh=readState(),next=storageError?state:fresh;
  pending.forEach((value,id)=>next.practice[id]=value);pending.clear();
  if(patch?.word){if(patch.value)next.words[patch.word]=patch.value;else delete next.words[patch.word];}if(patch?.group)next.group=patch.group;
  state=next;try{localStorage.setItem(key,JSON.stringify(state));storageError=false;}catch(e){storageError=true;}storageStatus(true);progress();filter();
 }
 function answer(q){const el=$('[data-exercise="'+q.id+'"]');return q.kind==='picture'?(el.querySelector('input:checked')?.value||''):el.querySelector('[data-answer]').value;}
 function feedback(q,value){$('#feedback-'+q.id).textContent=value===''?'Em nhập hoặc chọn một đáp án rồi kiểm tra nhé.':isCorrect(q,value)?'Đúng rồi! '+(q.success||q.hint):'Thử lại nhé! '+q.hint;}
 function restore(){
  questions.forEach(q=>{const r=state.practice[q.id],el=$('[data-exercise="'+q.id+'"]');if(q.kind==='picture')el.querySelectorAll('input').forEach(i=>i.checked=i.value===(r?.answer||''));else el.querySelector('[data-answer]').value=r?.answer||'';$('#feedback-'+q.id).textContent='';if(r?.checked)feedback(q,r.answer);});progress();filter();storageStatus(false);
 }
 restore();
 const synth=window.speechSynthesis,available=!!(synth&&window.SpeechSynthesisUtterance),select=$('#voice');
 let voices=[],sequence=0,utterance=null,startTimer,endTimer,gapTimer;
 function clearHighlight(){document.querySelectorAll('[data-letter].active').forEach(el=>el.classList.remove('active'));}
 function playStatus(message){$('#play-status').textContent=message;$('#mini-status').textContent=message;}
 function stop(message){sequence++;clearTimeout(startTimer);clearTimeout(endTimer);clearTimeout(gapTimer);if(available)synth.cancel();utterance=null;clearHighlight();$('#stop').disabled=true;$('#mini-player').hidden=true;if(message)playStatus(message);}
 function populate(){
  const previous=select.value;voices=available?synth.getVoices().filter(v=>/^en(?:[-_]|$)/i.test(v.lang)):[];
  voices.sort((a,b)=>Number(b.lang==='en-GB')-Number(a.lang==='en-GB')||a.name.localeCompare(b.name));select.replaceChildren();
  voices.forEach(v=>{const o=document.createElement('option');o.value=v.voiceURI;o.textContent=v.name+' · '+v.lang;select.appendChild(o);});
  if(voices.some(v=>v.voiceURI===previous))select.value=previous;
  document.querySelectorAll('[data-audio],[data-say],[data-spell]').forEach(b=>b.disabled=!voices.length);select.disabled=!voices.length;
  if(!voices.length){const o=document.createElement('option');o.textContent='Chưa có giọng tiếng Anh';select.appendChild(o);$('#voice-settings').open=true;$('#voice-status').textContent='Chưa tìm được giọng Anh. Em có thể bấm Tìm lại giọng, xem chữ và luyện viết.';}
  else $('#voice-status').textContent='Đang chọn: '+select.selectedOptions[0].textContent;
 }
 function speak(items,slow,finish){
  stop();const voice=voices.find(v=>v.voiceURI===select.value);if(!voice){$('#play-status').textContent='Chưa có giọng Anh. Em vẫn có thể xem chữ và luyện viết.';return;}
  const token=sequence;$('#stop').disabled=false;$('#mini-player').hidden=false;
  function next(index){
   if(token!==sequence)return;
   if(index===items.length){utterance=null;clearHighlight();$('#stop').disabled=true;$('#mini-player').hidden=true;playStatus(finish||'Đã nghe xong. Em đọc lại một lần nhé!');return;}
   const item=items[index],u=new SpeechSynthesisUtterance(item.text);utterance=u;u.voice=voice;u.lang=voice.lang;u.rate=slow?0.72:0.9;u.pitch=1;u.volume=1;
   playStatus('Đang chuẩn bị giọng đọc…');
   const fail=()=>{if(token===sequence)stop('Chưa phát được âm thanh. Em chọn giọng khác hoặc xem chữ nhé.');};
   u.onstart=()=>{if(token!==sequence)return;clearTimeout(startTimer);clearHighlight();if(item.letter)$('[data-letter="'+item.letter+'"]').classList.add('active');playStatus(item.letter?'Đang đánh vần: '+item.text:slow?'Đang nghe chậm…':'Đang nghe…');endTimer=setTimeout(fail,60000);};
   u.onend=()=>{if(token!==sequence)return;clearTimeout(startTimer);clearTimeout(endTimer);gapTimer=setTimeout(()=>next(index+1),item.wordEnd?550:items.length>1?160:0);};
   u.onerror=fail;startTimer=setTimeout(fail,12000);try{synth.speak(u);}catch(e){fail();}
  }
  next(0);
 }
 document.addEventListener('click',event=>{
  const b=event.target.closest('button');if(!b)return;
  if(b.hasAttribute('data-stop'))stop('Đã dừng. Em có thể bấm nghe lại.');
  else if(b.dataset.groupSelect){stop('Đã đổi nhóm. Em bấm Nghe khi sẵn sàng.');reviewOnly=false;flush({group:b.dataset.groupSelect});}
  else if(b.id==='only-review'){stop('Em có thể chọn một từ để nghe lại.');reviewOnly=!reviewOnly;filter();}
  else if(b.dataset.hide){const meaning=$('#meaning-'+b.dataset.hide);meaning.hidden=!meaning.hidden;b.setAttribute('aria-expanded',String(!meaning.hidden));b.textContent=meaning.hidden?'Hiện nghĩa để kiểm tra':'Ẩn nghĩa để thử nhớ';}
  else if(b.dataset.mark){const id=b.dataset.mark;flush({word:id,value:state.words[id]===b.dataset.value?null:b.dataset.value});if(reviewOnly&&b.closest('.word-card').hidden){stop();$('#word-title').focus({preventScroll:true});}}
  else if(b.dataset.say)speak([{text:byId[b.dataset.say].word}],b.hasAttribute('data-slow'));
  else if(b.dataset.spell){const w=byId[b.dataset.spell],letters=Array.from(w.word).flatMap((c,i)=>c===' '?[]:[{text:c.toUpperCase(),letter:w.id+'-'+i,wordEnd:w.word[i+1]===' '}]);speak(letters,false,'Đã đánh vần xong. Bấm Nghe từ/cụm để luyện cách nói tự nhiên.');}
  else if(b.dataset.text)speak([{text:b.dataset.text}],b.hasAttribute('data-slow'),b.hasAttribute('data-turn')?'Đến lượt em: nói câu trả lời của B. Trang không thu âm hoặc chấm giọng.':null);
  else if(b.dataset.check){const q=byQuestion[b.dataset.check],value=answer(q);pending.set(q.id,{answer:value,checked:true,signature:q.signature});flush();feedback(q,value);}
 });
 function changed(event){const el=event.target.closest('[data-exercise]');if(!el)return;const q=byQuestion[el.dataset.exercise],value={answer:answer(q),checked:false,signature:q.signature};state.practice[q.id]=value;pending.set(q.id,value);$('#feedback-'+q.id).textContent='';progress();clearTimeout(saveTimer);saveTimer=setTimeout(()=>flush(),250);}
 document.addEventListener('input',changed);document.addEventListener('change',changed);
 $('#demo').onclick=()=>speak([{text:data.unit===6?'Hello! Let us learn about our school rooms.':'Hello! Let us talk about our favourite school activities.'}],false);
 $('#stop').onclick=()=>stop('Đã dừng. Em có thể bấm nghe lại.');$('#refresh').onclick=()=>{stop('Em chọn giọng rồi bấm Nghe nhé.');populate();};select.onchange=()=>{stop('Đã đổi giọng. Em bấm nghe để thử nhé.');$('#voice-status').textContent='Đang chọn: '+select.selectedOptions[0].textContent;};
 if(available)synth.addEventListener('voiceschanged',populate);
 document.addEventListener('visibilitychange',()=>{if(document.hidden){flush();stop('Đã dừng khi trang ẩn. Bấm Nghe để tiếp tục.');}});window.addEventListener('pagehide',()=>{flush();stop();});
 window.addEventListener('pageshow',e=>{if(e.persisted){flush();storageError=false;state=readState();restore();}});window.addEventListener('storage',e=>{if(e.key===key||e.key===null){flush();storageError=false;state=readState();restore();}});
 populate();
})();
