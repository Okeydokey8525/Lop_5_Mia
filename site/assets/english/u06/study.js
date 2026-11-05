(function(){'use strict';
 const words=JSON.parse(document.getElementById('study-data').textContent),byId=Object.fromEntries(words.map(w=>[w.id,w]));
 const $=s=>document.querySelector(s),key='mia5:learn:en-u06-preview-v1',correct=new Set();
 let marks={},storageError=false;
 function readMarks(){try{const raw=JSON.parse(localStorage.getItem(key)||'null'),out={};if(raw&&raw.schema===1&&raw.words&&typeof raw.words==='object')words.forEach(w=>{if(['practised','review'].includes(raw.words[w.id]))out[w.id]=raw.words[w.id]});return out;}catch(e){storageError=true;return {};}}
 function renderMarks(saved){
  let practised=0,review=0;
  words.forEach(w=>{const state=marks[w.id];if(state==='practised')practised++;if(state==='review')review++;document.querySelectorAll('[data-mark="'+w.id+'"]').forEach(b=>b.setAttribute('aria-pressed',String(state===b.dataset.value)));$('[data-mark-status="'+w.id+'"]').textContent=state==='practised'?'✓ Em đã đánh dấu đã luyện':state==='review'?'♡ Em muốn ôn lại từ/cụm này':'Chưa đánh dấu';});
  $('#progress').textContent=practised+'/4 từ/cụm đã luyện · '+review+' cần ôn';
  $('#storage-status').textContent=storageError?'Chưa lưu được trên trình duyệt này. Lựa chọn hiện tại chỉ giữ khi trang còn mở.':saved?'✓ Đã lưu lựa chọn trên trình duyệt này, tách khỏi điểm đề.':'Lựa chọn tự đánh dấu được lưu trên trình duyệt này, tách khỏi điểm đề.';
 }
 marks=readMarks();renderMarks();
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
  if(!voices.length){const o=document.createElement('option');o.textContent='Chưa có giọng tiếng Anh';select.appendChild(o);$('#voice-status').textContent='Chưa tìm được giọng Anh. Em có thể bấm Tìm lại giọng, xem chữ và luyện viết.';}
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
 document.addEventListener('click',e=>{
  const b=e.target.closest('button');if(!b)return;
  if(b.hasAttribute('data-stop'))stop('Đã dừng. Em có thể bấm nghe lại.');
  else if(b.dataset.hide){const meaning=$('#meaning-'+b.dataset.hide);meaning.hidden=!meaning.hidden;b.setAttribute('aria-expanded',String(!meaning.hidden));b.textContent=meaning.hidden?'Hiện nghĩa để kiểm tra':'Ẩn nghĩa để thử nhớ';}
  else if(b.dataset.mark){storageError=false;const fresh=readMarks();marks=storageError?marks:fresh;if(marks[b.dataset.mark]===b.dataset.value)delete marks[b.dataset.mark];else marks[b.dataset.mark]=b.dataset.value;try{localStorage.setItem(key,JSON.stringify({schema:1,words:marks}));storageError=false;}catch(e){storageError=true;}renderMarks(true);}
  else if(b.dataset.say)speak([{text:byId[b.dataset.say].word}],b.hasAttribute('data-slow'));
  else if(b.dataset.spell){const w=byId[b.dataset.spell],letters=Array.from(w.word).flatMap((c,i)=>c===' '?[]:[{text:c.toUpperCase(),letter:w.id+'-'+i,wordEnd:w.word[i+1]===' '}]);speak(letters,false,'Đã đánh vần xong. Bấm Nghe cụm từ để đọc lại cách nói tự nhiên.');}
  else if(b.dataset.text)speak([{text:b.dataset.text}],false,b.hasAttribute('data-turn')?'Đến lượt em: nói câu trả lời của B. Trang không thu âm hoặc chấm giọng.':null);
  else if(b.dataset.check){
   const id=b.dataset.check;let ok=false,message='';
   if(id==='room'){const chosen=$('input[name="room"]:checked');ok=!!chosen&&chosen.value==='library';message=ok?'Đúng rồi! Library là thư viện, có nhiều sách.':chosen?'Thử lại nhé! Tìm tranh có kệ sách và các bạn đang đọc.':'Em chọn một tranh rồi kiểm tra nhé.';}
   if(id==='spelling'){ok=$('#spelling').value.trim().toLowerCase()==='computer';message=ok?'Đúng rồi! Computer có chữ t sau u.':'Viết cả từ nhé: computer. Chữ còn thiếu là t; em thử gõ lại.';}
   if(id==='sentence'){ok=$('#sentence').value.trim().toLowerCase()==='on';message=ok?'Đúng rồi! It is on the first floor.':'Dùng on the + tầng + floor. Em thử điền lại nhé.';}
   if(ok)correct.add(id);else correct.delete(id);$('#feedback-'+id).textContent=message;updatePractice();
  }
 });
 function updatePractice(){$('#practice-progress').textContent=correct.size===3?'🌸 Em đã làm đúng cả 3 bài! Có thể quay lại ôn những từ đã đánh dấu.':'Em đã làm đúng '+correct.size+'/3 bài luyện trong lần mở trang này.';}
 document.addEventListener('input',e=>{if(!e.target.closest('.exercise'))return;const id=e.target.name==='room'?'room':e.target.id;if(['room','spelling','sentence'].includes(id)){correct.delete(id);$('#feedback-'+id).textContent='';updatePractice();}});
 $('#demo').onclick=()=>speak([{text:'Hello! Let us learn about our school rooms.'}],false);
 $('#stop').onclick=()=>stop('Đã dừng. Em có thể bấm nghe lại.');$('#refresh').onclick=()=>{stop('Em chọn giọng rồi bấm Nghe nhé.');populate();};select.onchange=()=>{stop('Đã đổi giọng. Em bấm nghe để thử nhé.');$('#voice-status').textContent='Đang chọn: '+select.selectedOptions[0].textContent;};
 if(available)synth.addEventListener('voiceschanged',populate);
 document.addEventListener('visibilitychange',()=>{if(document.hidden)stop('Đã dừng khi trang ẩn. Bấm Nghe để tiếp tục.');});window.addEventListener('pagehide',()=>stop());
 window.addEventListener('pageshow',e=>{if(e.persisted){storageError=false;marks=readMarks();renderMarks();}});window.addEventListener('storage',e=>{if(e.key===key||e.key===null){storageError=false;marks=readMarks();renderMarks();}});
 populate();
})();
