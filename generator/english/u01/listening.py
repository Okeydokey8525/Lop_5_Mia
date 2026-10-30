"""Six-question listening prototype, separate from scored exams."""
import json
from pathlib import Path
from english.u01.content import picture

LEVELS=[('tb','Trung bình','Nghe một câu ngắn, tìm thông tin trực tiếp.'),('kha','Khá','Nghe hai câu, nhận ra thông tin được hỏi.'),('gioi','Giỏi','Nghe đoạn giới thiệu, kết hợp hai thông tin.')]

def sample_data():
    def field(label,answer,options=None,alternatives=()):
        return dict(label=label,answer=answer,options=options,alternatives=list(alternatives))
    # Facts are the source for both the spoken passage and the marked answers.
    mai=dict(name='Mai',cls='5B',spoken_class='five B',place='countryside',sport='table tennis')
    linh=dict(name='Linh',sport='table tennis')
    an=dict(name='An',place='city',food='a sandwich',animal='a dolphin')
    colour='pink'
    intro=f"Hello. My name is {mai['name']}."
    home=f"I live in the {mai['place']}."
    sport=f"My name is {linh['name']}. My favourite sport is {linh['sport']}."
    colour_dialogue=f"What is your favourite colour? My favourite colour is {colour}."
    an_passage=f"My name is {an['name']}. I live in the {an['place']}. My favourite food is {an['food']}. My favourite animal is {an['animal']}."
    mai_passage=f"My name is {mai['name']}. I am in Class {mai['cls']}. I live in the {mai['place']}. My favourite sport is {mai['sport']}."
    return [
      dict(id='tb1',level='tb',prompt='Listen and choose the name.',hint='Nghe và chọn tên bạn vừa giới thiệu.',speech=intro,transcript=intro,meaning='Xin chào. Mình tên là Mai.',fields=[field('Tên bạn là gì?',mai['name'],['Mai','Linh','An','Minh'])]),
      dict(id='tb2',level='tb',prompt='Listen and choose the picture.',hint='Nghe và chọn tranh chỉ nơi bạn sống.',speech=home,transcript=home,meaning='Mình sống ở nông thôn.',fields=[field('Bạn sống ở đâu?',mai['place'],['city','countryside'])],pictures=[picture('city',280),picture('countryside',280)]),
      dict(id='kha1',level='kha',prompt='What is Linh’s favourite sport?',hint='Nghe hai câu, tìm môn thể thao Linh yêu thích.',speech=sport,transcript=sport,meaning='Mình tên là Linh. Môn thể thao yêu thích của mình là bóng bàn.',fields=[field('Môn thể thao yêu thích?',linh['sport'],['football','table tennis','swimming','basketball'])]),
      dict(id='kha2',level='kha',prompt='Listen and choose the favourite colour.',hint='Nghe lời hỏi và trả lời, chọn màu yêu thích.',speech=colour_dialogue,transcript=colour_dialogue,meaning='Màu yêu thích của bạn là gì? Màu yêu thích của mình là hồng.',fields=[field('Màu yêu thích?',colour,['blue','green','pink','red'])]),
      dict(id='gioi1',level='gioi',prompt='Listen to An. Choose the home and favourite food.',hint='Nghe đoạn giới thiệu, chọn đúng cả nơi sống và món ăn.',speech=an_passage,transcript=an_passage,meaning='Mình tên là An. Mình sống ở thành phố. Món ăn yêu thích là bánh mì kẹp. Con vật yêu thích là cá heo.',fields=[field('Nơi sống?',an['place'],['city','countryside']),field('Món ăn yêu thích?',an['food'],['pizza','a sandwich','fish and chips'])]),
      dict(id='gioi2',level='gioi',prompt='Listen to Mai. Write the class and favourite sport.',hint='Điền lớp (ví dụ 5A) và tên môn thể thao bằng tiếng Anh.',speech=mai_passage.replace(mai['cls'],mai['spoken_class']),transcript=mai_passage,meaning='Mình tên là Mai. Mình học lớp 5B, sống ở nông thôn và thích môn bóng bàn.',fields=[field('Lớp của Mai?',mai['cls'],alternatives=['class '+mai['cls'],mai['spoken_class'],'class '+mai['spoken_class']]),field('Môn thể thao yêu thích?',mai['sport'])]),
    ]

def render_listening():
    root=Path(__file__).resolve().parents[2]
    data=sample_data()
    assert [sum(q['level']==lv for q in data) for lv,*_ in LEVELS]==[2,2,2]
    for q in data:
        for f in q['fields']:
            assert f['answer'] and (f['options'] is None or f['answer'] in f['options'])
    template=(Path(__file__).parent/'listening.html').read_text(encoding='utf-8')
    return template.replace('__FONTS__',(root/'fonts.css').read_text(encoding='utf-8')).replace('__DATA__',json.dumps(dict(levels=LEVELS,questions=data),ensure_ascii=False).replace('</',r'<\/'))
