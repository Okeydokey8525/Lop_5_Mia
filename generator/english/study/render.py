"""Shared learning-page renderer; lesson facts remain beside each unit."""
import html
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).parent
e=html.escape


def floor_diagram(floor):
    floors=['third','second','first','ground']
    rows=''.join(f'<rect x="35" y="{15+i*46}" width="290" height="40" rx="8" fill="{"#FFB3D1" if f==floor else "#FFEAF3"}" stroke="#A33163" stroke-width="{3 if f==floor else 1}"/><text x="180" y="{42+i*46}" text-anchor="middle" font-size="18" fill="#54233D">{f} floor</text>' for i,f in enumerate(floors))
    return f'<svg class="learning-diagram" role="img" aria-label="{e(floor)} floor được tô đậm; ground floor ở dưới cùng" viewBox="0 0 360 210">{rows}</svg>'


def direction_diagram(name):
    if name in ('go upstairs','go downstairs'):
        path='M45 167 H100 V125 H155 V83 H210 V41 H300'
        arrow='M60 145 L270 35' if name=='go upstairs' else 'M270 35 L60 145'
        content=f'<path d="{path}" fill="none" stroke="#7D4560" stroke-width="5"/><path d="{arrow}" stroke="#A33163" stroke-width="9" marker-end="url(#head)"/>'
    elif name in ('turn left','turn right'):
        x=65 if name=='turn left' else 295
        content=f'<path d="M180 180 V75 H{x}" fill="none" stroke="#A33163" stroke-width="10" marker-end="url(#head)"/><text x="180" y="205" text-anchor="middle" font-size="15" fill="#54233D">Bắt đầu ở đây</text>'
    else:
        content='<path d="M65 190 V25 M290 190 V25" stroke="#7D4560" stroke-width="5"/><path d="M180 180 V35" stroke="#A33163" stroke-width="10" marker-end="url(#head)"/>'
        if name=='go past the library':content+='<rect x="25" y="80" width="100" height="65" rx="8" fill="#FFE0EE" stroke="#A33163"/><text x="75" y="118" text-anchor="middle" font-size="16" fill="#54233D">Library</text>'
        else:content+='<text x="180" y="210" text-anchor="middle" font-size="15" fill="#54233D">Đi dọc hành lang</text>'
    # Inline marker has a per-card ID so browser references never cross cards.
    marker='arrow-'+name.replace(' ','-')
    content=content.replace('url(#head)',f'url(#{marker})')
    return f'<svg class="learning-diagram" role="img" aria-label="Sơ đồ minh họa {e(name)}" viewBox="0 0 360 230"><defs><marker id="{marker}" markerWidth="4" markerHeight="4" refX="3" refY="2" orient="auto"><path d="M0 0 L4 2 L0 4 Z" fill="#A33163"/></marker></defs>{content}</svg>'


def letters(word,key):
    offset=0;groups=[]
    for part in word.split(' '):
        groups.append('<span class="word-letters">'+''.join(f'<span data-letter="{key}-{offset+i}">{e(c.upper())}</span>' for i,c in enumerate(part))+'</span>')
        offset+=len(part)+1
    return ''.join(groups)


def render_study(config,picture):
    words=config['words'];by_id={w['id']:w for w in words}
    assert len(by_id)==len(words)
    assert all(w['group'] in {g['id'] for g in config['groups']} for w in words)
    cards=[]
    for w in words:
        key=w['id'];name=w['word']
        fig=picture(w['image'],440) if w.get('image') else floor_diagram(w['floor']) if w.get('floor') else direction_diagram(name) if w.get('direction') else ''
        cards.append(f'''<article class="word-card" id="word-{key}" data-word="{key}" data-group="{w['group']}">
{fig}<h3 lang="en">{e(name)}</h3><p class="meaning" id="meaning-{key}">{e(w['meaning'])}</p><button class="quiet" type="button" data-hide="{key}" aria-controls="meaning-{key}" aria-expanded="true">Ẩn nghĩa để thử nhớ</button>
<div class="controls"><button type="button" data-say="{key}">🔊 Nghe từ/cụm</button><button type="button" data-say="{key}" data-slow>🐢 Nghe chậm</button><button type="button" data-spell="{key}">ABC Đánh vần</button></div><div class="letters" aria-label="Các chữ cái của {e(name)}" lang="en">{letters(name,key)}</div>
<p class="example" lang="en">{e(w['example'])}</p><button class="quiet" type="button" data-text="{e(w['example'],quote=True)}" data-audio>🔊 Nghe câu ví dụ</button>
<div class="self-check"><button type="button" data-mark="{key}" data-value="practised" aria-pressed="false">✓ Em đã luyện</button><button type="button" data-mark="{key}" data-value="review" aria-pressed="false">♡ Cần ôn lại</button></div><p class="mark-status" data-mark-status="{key}">Chưa đánh dấu</p></article>''')
    dialogs=[]
    for d in config['dialogues']:
        dialogs.append(f'''<article class="dialogue" data-group="{d['group']}"><h3>{e(d['title'])}</h3><p lang="en"><b>A:</b> {e(d['a'])}<br><b>B:</b> {e(d['b'])}</p><p>{e(d['meaning'])}</p><div class="controls"><button type="button" data-text="{e(d['a']+' '+d['b'],quote=True)}" data-audio>🔊 Nghe hội thoại</button><button type="button" data-text="{e(d['a']+' '+d['b'],quote=True)}" data-slow data-audio>🐢 Nghe chậm</button><button type="button" data-text="{e(d['a'],quote=True)}" data-turn data-audio>Đến lượt em trả lời</button></div></article>''')
    exercises=[]
    for i,q in enumerate(config['exercises'],1):
        key=q['id'];assert q['answer'] and q['hint'] and q['group'] in {g['id'] for g in config['groups']}
        q['signature']=hashlib.sha256(json.dumps({k:q.get(k) for k in ['id','kind','prompt','answer','alternatives','options','speech']},sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:16]
        audio=f'<button type="button" data-text="{e(q["speech"],quote=True)}" data-audio>🔊 Nghe câu hỏi</button><details><summary>Xem lời nghe</summary><p lang="en">{e(q["speech"])}</p></details>' if q.get('speech') else ''
        if q['kind']=='picture':
            assert q['answer'] in q['options']
            controls='<div class="choice-grid">'+''.join(f'<label class="picture-choice"><input type="radio" name="{key}" value="{v}">{picture(by_id[v]["image"],280)}<span>Tranh {j}</span></label>' for j,v in enumerate(q['options'],1))+'</div>'
        elif q['kind']=='choice':
            assert q['answer'] in q['options']
            controls=f'<label for="answer-{key}">Chọn câu trả lời</label><select id="answer-{key}" data-answer="{key}"><option value="">Chọn một đáp án</option>'+''.join(f'<option value="{e(v,quote=True)}">{e(v)}</option>' for v in q['options'])+'</select>'
        else:controls=f'<label for="answer-{key}">{e(q.get("label","Viết câu trả lời tiếng Anh"))}</label><input id="answer-{key}" data-answer="{key}" lang="en" autocomplete="off" autocapitalize="none" spellcheck="false" maxlength="250">'
        exercises.append(f'<fieldset class="exercise" data-exercise="{key}" data-group="{q["group"]}"><legend>{i} · {e(q["title"])}</legend><p>{e(q["instruction"])}</p><p class="question-en" lang="en">{e(q["prompt"])}</p>{audio}{controls}<button type="button" data-check="{key}">Kiểm tra</button><p class="feedback" id="feedback-{key}" role="status"></p></fieldset>')
    data={**config,'words':[{k:v for k,v in w.items() if k not in ('image','direction','floor')} for w in words]}
    group_buttons=''.join(f'<button type="button" data-group-select="{g["id"]}" aria-pressed="false">{e(g["name"])}</button>' for g in config['groups'])
    tips=''.join(f'<aside class="tip" data-group="{g["id"]}"><h3>Mẹo nhớ</h3><p>{e(g["tip"])}</p></aside>' for g in config['groups'])
    replace={'__TITLE__':f'Unit {config["unit"]} · Học từ và phát âm','__UNIT__':str(config['unit']),'__INTRO__':config['intro'],'__GROUPS__':group_buttons,'__WORDS__':''.join(cards),'__DIALOGUES__':''.join(dialogs),'__EXERCISES__':''.join(exercises),'__TIPS__':tips,'__FONTS__':(ROOT/'fonts.css').read_text(encoding='utf-8'),'__CSS__':(HERE/'study.css').read_text(encoding='utf-8'),'__JS__':(HERE/'study.js').read_text(encoding='utf-8'),'__DATA__':json.dumps(data,ensure_ascii=False).replace('</',r'<\/')}
    result=(HERE/'template.html').read_text(encoding='utf-8')
    for old,new in replace.items():result=result.replace(old,new)
    return result
