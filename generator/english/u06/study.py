"""Small, unscored overview-learning pilot; not a replacement for the poster."""
import json
from pathlib import Path
from english.u06.content import CORE, MEANINGS, picture


def render_study():
    root=Path(__file__).resolve().parents[2]
    folder=Path(__file__).parent
    data=[dict(id=name.replace(' ','-'),word=name,meaning=meaning) for name,meaning in zip(CORE,MEANINGS)]
    cards=[]
    for item in data:
        name=item['word'];key=item['id']
        cards.append(f'''<article class="word-card" id="word-{key}" data-word="{key}">
{picture(name,440)}<h3 lang="en">{name}</h3><p class="meaning" id="meaning-{key}">{item['meaning']}</p>
<button class="quiet" type="button" data-hide="{key}" aria-controls="meaning-{key}" aria-expanded="true">Ẩn nghĩa để thử nhớ</button>
<div class="controls"><button type="button" data-say="{key}">🔊 Nghe cụm từ</button><button type="button" data-say="{key}" data-slow>🐢 Nghe chậm</button><button type="button" data-spell="{key}">ABC Đánh vần</button></div>
<div class="letters" aria-label="Các chữ cái của {name}" lang="en">{''.join('<span class="word-letters">'+''.join(f'<span data-letter="{key}-{i+j}">{c.upper()}</span>' for j,c in enumerate(word))+'</span>' for i,word in [(sum(len(x)+1 for x in name.split()[:k]),word) for k,word in enumerate(name.split())])}</div>
<p class="word-note">Nghe rồi đọc theo. Đánh vần giúp nhớ chữ; nghe cụm từ giúp luyện cách nói.</p>
<div class="self-check"><button type="button" data-mark="{key}" data-value="practised" aria-pressed="false">✓ Em đã luyện</button><button type="button" data-mark="{key}" data-value="review" aria-pressed="false">♡ Cần ôn lại</button></div><p class="mark-status" data-mark-status="{key}">Chưa đánh dấu</p></article>''')
    options=''.join(f'<label class="picture-choice"><input type="radio" name="room" value="{item["id"]}">{picture(item["word"],280)}<span>Tranh {i}</span></label>' for i,item in enumerate(data,1))
    template=(folder/'study.html').read_text(encoding='utf-8')
    replacements={'__FONTS__':(root/'fonts.css').read_text(encoding='utf-8'),'__CSS__':(folder/'study.css').read_text(encoding='utf-8'),'__JS__':(folder/'study.js').read_text(encoding='utf-8'),'__WORDS__':''.join(cards),'__OPTIONS__':options,'__DATA__':json.dumps(data,ensure_ascii=False).replace('</',r'<\/')}
    for old,new in replacements.items():template=template.replace(old,new)
    return template
