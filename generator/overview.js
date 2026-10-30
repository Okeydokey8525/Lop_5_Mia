(function(){
  const sheet=document.querySelector('#sheetw > div'),reader=document.getElementById('reader');
  const copy=sheet.cloneNode(true);copy.classList.add('reader-sheet');
  const all=[copy,...copy.querySelectorAll('*')];
  for(const el of all){
    el.removeAttribute('id');
    if(el.closest('svg'))continue;
    const s=el.style,oldWidth=parseFloat(s.width),size=parseFloat(s.fontSize);
    if(s.color){s.setProperty('--original-ink',s.color);s.color='var(--reader-ink,var(--original-ink))';}
    if(s.background){s.setProperty('--original-bg',s.background);s.background='var(--reader-surface,var(--original-bg))';}
    if(s.fontSize.endsWith('px'))s.fontSize=(size>=50?32:size>=30?21:17)+'px';
    if(s.padding)s.padding=s.padding.replace(/([\d.]+)px/g,(_,n)=>Math.min(18,Math.round(Number(n)*.55))+'px');
    if(s.gap)s.gap='12px';
    s.minWidth='0';
    if(el.tagName==='IMG'){s.maxWidth='100%';s.height='auto';continue;}
    if(s.width.endsWith('px')){s.removeProperty('width');s.removeProperty('height');}
    if(oldWidth===210){el.classList.add('reader-lesson-label');s.flex='none';s.alignItems='flex-start';s.textAlign='left';s.gap='6px';el.parentElement.classList.add('reader-lesson');el.parentElement.style.flexDirection='column';}
    if(oldWidth===160){el.classList.add('reader-badge');s.width='88px';s.height='88px';el.parentElement.classList.add('reader-header');el.parentElement.style.flexDirection='column';el.parentElement.style.alignItems='flex-start';}
    if(s.display==='flex'&&s.flexDirection!=='column')s.flexWrap='wrap';
    if(s.display==='grid'){
      if(s.gridTemplateColumns.includes('7,')){
        el.classList.add('reader-place-values');s.minWidth='560px';
        const scroll=document.createElement('div');scroll.className='reader-table-scroll';scroll.setAttribute('role','region');scroll.setAttribute('aria-label','Bảng các hàng của số thập phân, có thể cuộn ngang');
        el.replaceWith(scroll);scroll.appendChild(el);
      }else s.gridTemplateColumns='minmax(0,1fr)';
    }
    if(s.whiteSpace==='pre'){s.fontSize='18px';s.maxWidth='100%';s.overflowX='auto';}
  }
  copy.style.padding='16px';copy.style.gap='20px';
  reader.appendChild(copy);
  const toggle=document.getElementById('view-toggle'),w=document.getElementById('sheetw'),clip=document.getElementById('clip');
  let manual=null;
  function fit(){
    const reading=manual===null?matchMedia('(max-width:820px)').matches:manual;
    document.body.classList.toggle('reading',reading);
    toggle.textContent=reading?'Xem poster':'Đọc từng bài';toggle.setAttribute('aria-pressed',String(reading));
    const scale=Math.min(1,document.documentElement.clientWidth/1080);
    w.style.transform='scale('+scale+')';clip.style.height=w.offsetHeight*scale+'px';
    w.style.marginLeft=Math.max(0,(document.documentElement.clientWidth-1080*scale)/2)+'px';
  }
  toggle.onclick=function(){manual=!document.body.classList.contains('reading');fit();};
  window.addEventListener('resize',fit);window.addEventListener('load',fit);document.fonts.ready.then(fit);fit();
})();
