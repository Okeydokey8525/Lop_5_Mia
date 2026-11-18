// Optional recorded voice for pages with a complete, unit-owned audio manifest.
(function(){'use strict';
 const el=document.getElementById('mia-audio-data');if(!el)return;
 const data=JSON.parse(el.textContent),native=window.speechSynthesis;
 const voice={name:'Âm thanh có sẵn · Anh Mỹ (Zira)',lang:'en-US',voiceURI:'mia-recorded',localService:true};
 // Reuse one media element for the whole spelling queue (per-element playback
 // permission on iPad); only start playback from a learner's button press.
 const player=new Audio();let sequence=0;
 function cancel(){sequence++;player.onplaying=player.onended=player.onerror=null;player.pause();if(native)native.cancel();}
 function speak(u){
  if(u.voice?.voiceURI!==voice.voiceURI){
   if(native&&window.SpeechSynthesisUtterance){const v=new SpeechSynthesisUtterance(u.text);for(const k of ['voice','lang','rate','pitch','volume','onstart','onend','onerror'])v[k]=u[k];native.speak(v);}
   else u.onerror?.({error:'voice-unavailable'});return;
  }
  cancel();const token=sequence,src=data.clips[u.text];
  if(!src){u.onerror?.({error:'audio-unavailable'});return;}
  const audio=player;let failed=false;
  const fail=()=>{if(token!==sequence||failed)return;failed=true;cancel();u.onerror?.({error:'audio-unavailable'});};
  audio.preload='none';audio.src=src;audio.volume=u.volume??1;audio.playbackRate=(u.rate||0.9)/0.9;audio.preservesPitch=true;
  audio.onplaying=()=>{if(token===sequence)u.onstart?.();};
  audio.onended=()=>{if(token!==sequence)return;audio.onplaying=audio.onended=audio.onerror=null;u.onend?.();};
  audio.onerror=fail;try{audio.play().catch(fail);}catch(e){fail();}
 }
 window.MiaRecorded={getVoices:()=>[voice,...(native?.getVoices()||[])],cancel,speak,
  addEventListener:(name,fn)=>native?.addEventListener(name,fn),removeEventListener:(name,fn)=>native?.removeEventListener(name,fn)};
})();
