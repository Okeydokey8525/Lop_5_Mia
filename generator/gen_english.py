"""Build the approved Unit 1 and the assigned Units 2–3."""
import json
from pathlib import Path
from english.u01.content import TESTS, build_tests, picture
from build_all import page as quiz_page
from gen_overview import page as overview_page, gen_sheet, box
from gen_index import render_index
from english.u01.listening import render_listening

W=Path(__file__).resolve().parent
OUT=W/'out'/'TiengAnh5'
UNIT='Unit1_AllAboutMe'
META=dict(subject='en',version=2,lessonLabel='Phần',book='Tiếng Anh 5 · Global Success · Tập một',
          title='Unit 1 · All about me!',topic='Giới thiệu bản thân và điều em yêu thích',range='Trang 10–15',minutes=40,
          tip='Mỗi đề có 6 câu nghe, chia đều ba mức. Xem lời nghe sẽ ghi nhận đã dùng hỗ trợ, không trừ điểm. Đọc gợi ý trước khi trả lời. Câu nối dùng ô chọn; câu sắp xếp thì bấm từng từ. Ô điền chữ không phân biệt hoa/thường; xem lời giải sau khi nộp.')
LESSONS={1:'Thông tin bản thân',2:'Điều em yêu thích',3:'Đọc và viết'}
LEVELS=[dict(id=lv,name=name,desc=desc,stars=k+1,pts=pts) for k,(lv,name,desc,pts) in enumerate([
    ('tb','Mức 1 · Trung bình','Nhận biết từ và mẫu câu cơ bản',3),
    ('kha','Mức 2 · Khá','Dùng mẫu câu, nối ý và tìm thông tin',5),
    ('gioi','Mức 3 · Giỏi','Kết hợp đọc hiểu và viết câu theo dữ liệu',5)])]


def build_unit1():
    folder=OUT/UNIT;folder.mkdir(parents=True,exist_ok=True)
    (folder/'LuyenNghe_Mau.html').write_text(render_listening(),encoding='utf-8',newline='\n')
    source=W/'english'/'u01';(source/'tests').mkdir(exist_ok=True)
    wrapper='window.MKEN1=function(questions){return '+json.dumps(dict(decimal=False,meta=META,lessons=LESSONS,levels=LEVELS),ensure_ascii=False)[:-1]+',"questions":questions};};\n'
    (source/'common.js').write_text(wrapper,encoding='utf-8',newline='\n')
    for i,((slug,name,theme),questions) in enumerate(zip(TESTS,build_tests()),1):
        data='window.TEST_FN=function(H){return MKEN1('+json.dumps(questions,ensure_ascii=False,indent=1)+');};\n'
        (source/'tests'/f'de{i:02d}.js').write_text(data,encoding='utf-8',newline='\n')
        extra=dict(id=f'en-u01-de{i}-v2',title=f'Đề {i} · {name}',theme=theme,home='../index.html')
        if i>1:extra['prev']=f'De{i-1}_{TESTS[i-2][0]}.html'
        if i<6:extra['next']=f'De{i+1}_{TESTS[i][0]}.html'
        (folder/f'De{i}_{slug}.html').write_text(quiz_page(f'Tiếng Anh 5 · Unit 1 · Đề {i} · {name}',data,extra,wrapper),encoding='utf-8',newline='\n')
    cd=dict(n=1,dir=UNIT,name='All about me!',range='Unit 1 · Trang 10–15',overview='TongQuan_Unit1',tests=TESTS)
    lessons=[
      dict(n=1,col='#8B4E84',bg='#F2E4F1',dk='#65375F',title='Giới thiệu bản thân',pg='10–11',head='Nói tên, lớp và nơi em sống.',body=lambda c:
        box(c['bg'],"<b>My name is Mai.</b> — Tên mình là Mai.<br><b>I am in Class 5D.</b> — Mình học lớp 5D.<br><b>I live in the countryside.</b> — Mình sống ở nông thôn.")+
        '<div style="display:flex;flex-wrap:wrap;gap:20px">'+picture('city',220)+picture('countryside',220)+'</div>'+
        box(c['bg'],'<b>Nhớ theo cụm:</b> in Class + tên lớp; in the city; in the countryside. Khi giới thiệu, I’m và I am có cùng nghĩa.')),
      dict(n=2,col='#9A5545',bg='#FCE7DF',dk='#713C30',title='Điều em yêu thích',pg='12–13',head='Hỏi đúng nhóm: colour, sport, animal, food.',body=lambda c:
        box(c['bg'],"<b>What is your favourite colour?</b> — My favourite colour is pink.<br><b>What is your favourite sport?</b> — It is table tennis.<br><b>What is your favourite animal?</b> — It is a dolphin.<br><b>What is your favourite food?</b> — It is a sandwich.")+
        '<div style="display:flex;flex-wrap:wrap;gap:20px">'+picture('pink',220)+picture('table tennis',220)+picture('dolphin',220)+picture('sandwich',220)+'</div>'+
        box(c['bg'],'<b>Từ khóa:</b> pink — màu hồng; table tennis — bóng bàn; dolphin — cá heo; sandwich — bánh mì kẹp. Chọn đúng nhóm trước khi trả lời.')),
      dict(n=3,col='#4D7395',bg='#E5EFF8',dk='#35516B',title='Đọc và viết',pg='14–15',head='Tìm thông tin trong hồ sơ rồi viết theo mẫu.',body=lambda c:
        box(c['bg'],'<b>Trọng âm đầu:</b> DOL-phin, TEN-nis. Đây là mẹo đọc bằng chữ, không phải bài nghe.')+
        box(c['bg'],'<b>Thẻ tự soạn:</b> Name: An · Class: 5A · Home: city · Colour: pink · Sport: table tennis.<br><b>Viết từ thẻ:</b> My name is An. I am in Class 5A. I live in the city. My favourite sport is table tennis.')+
        box(c['bg'],'<b>Tự kiểm tra:</b> câu có I am hoặc My… is chưa? Đã dùng in Class / in the… đúng chưa? Thông tin có khớp thẻ không?')),
    ]
    sheet=gen_sheet(1,'ALL ABOUT ME!','Unit 1 · Tiếng Anh 5 Global Success · Trang 10–15','#8B4E84','#F2E4F1',lessons,
                    ['Thông tin bản thân','Điều yêu thích','Đọc và viết'],
                    'Một chút về em, một bước làm quen với bạn.','Ôn tên, lớp, nơi sống và những điều yêu thích. Đọc từng bài, rồi thử sáu đề theo nhịp của em.',
                    'Nội dung ôn tập tự soạn, bám Unit 1 · Global Success 5, tập một')
    for old,new in {'#FFF5F8':'#FFF0F6','#4A2433':'#54233D','#FCE4EC':'#FFE0EE','#F8BBD0':'#FFC2DD','#8B4E84':'#A33163','#F2E4F1':'#FFE0EE','#65375F':'#702344','#9A5545':'#A33163','#FCE7DF':'#FFE5F0','#713C30':'#702344','#4D7395':'#A33163','#E5EFF8':'#FFEAF4','#35516B':'#702344'}.items():sheet=sheet.replace(old,new)
    (folder/'TongQuan_Unit1.html').write_text(overview_page('Tiếng Anh 5 · Unit 1 · Tổng quan',sheet,cd,'#8B4E84'),encoding='utf-8',newline='\n')
    # Speech module embedded for standalone export; global theme is injected by tools/build.py.
    for target in folder.glob('*.html'):
        html=target.read_text(encoding='utf-8')
        extra=''.join('<style>'+ (W/'english'/name).read_text(encoding='utf-8-sig')+'</style>' if name.endswith('.css') else '<script>'+(W/'english'/name).read_text(encoding='utf-8-sig')+'</script>' for name in ['speech.js'])
        target.write_text(html.replace('</head>',extra+'</head>'),encoding='utf-8',newline='\n')


def main():
    import importlib
    from english.units import UNITS, index_data, test_id, tests_for
    from english.overviews import sheet
    build_unit1()
    for unit in UNITS[1:]:
        n=unit['n'];unit_tests=tests_for(unit);content=importlib.import_module(f"english.{unit['key']}.content")
        folder=OUT/unit['dir'];folder.mkdir(parents=True,exist_ok=True)
        source=W/'english'/unit['key'];(source/'tests').mkdir(exist_ok=True)
        meta={**META,'version':unit['version'],'title':f"Unit {n} · {unit['name']}",
              'topic':'Nhà ở và địa chỉ' if n==2 else 'Quốc tịch và tính cách của bạn bè','range':f"Trang {unit['pages']}"}
        lessons={1:'Loại nhà',2:'Địa chỉ và khoảng cách',3:'Đọc và viết'} if n==2 else {1:'Quốc gia và quốc tịch',2:'Tính cách',3:'Đọc và viết'}
        wrapper=f'window.MKEN{n}=function(questions){{return '+json.dumps(dict(decimal=False,meta=meta,lessons=lessons,levels=LEVELS),ensure_ascii=False)[:-1]+',"questions":questions};};\n'
        (source/'common.js').write_text(wrapper,encoding='utf-8',newline='\n')
        for i,((slug,name,theme),questions) in enumerate(zip(unit_tests,content.build_tests()),1):
            data=f'window.TEST_FN=function(H){{return MKEN{n}('+json.dumps(questions,ensure_ascii=False,indent=1)+');};\n'
            (source/'tests'/f'de{i:02d}.js').write_text(data,encoding='utf-8',newline='\n')
            extra=dict(id=test_id(unit,i),title=f'Đề {i} · {name}',theme=theme,home='../index.html')
            if i>1:extra['prev']=f'De{i-1}_{TESTS[i-2][0]}.html'
            if i<6:extra['next']=f'De{i+1}_{TESTS[i][0]}.html'
            html=quiz_page(f'Tiếng Anh 5 · Unit {n} · Đề {i} · {name}',data,extra,wrapper)
            speech='<script>'+(W/'english'/'speech.js').read_text(encoding='utf-8-sig')+'</script>'
            (folder/f'De{i}_{slug}.html').write_text(html.replace('</head>',speech+'</head>'),encoding='utf-8',newline='\n')
        cd=dict(n=n,dir=unit['dir'],name=unit['name'],range=f"Unit {n} · Trang {unit['pages']}",overview=f'TongQuan_Unit{n}',tests=unit_tests)
        (folder/f'TongQuan_Unit{n}.html').write_text(overview_page(f'Tiếng Anh 5 · Unit {n} · Tổng quan',sheet(unit,content),cd,'#AD4278' if n==2 else '#AF4771'),encoding='utf-8',newline='\n')
    count=len(UNITS)*6
    index=render_index(index_data()).replace('Toán 5','Tiếng Anh 5').replace('Kết nối tri thức với cuộc sống','Global Success')
    index=index.replace('Mỗi đề làm xong là một bậc thang. Leo đủ 36 bậc là em đã chinh phục cả học kì 1 của Tiếng Anh 5.',
                        'Unit 1–3 đã sẵn sàng: giới thiệu bản thân, ngôi nhà và bạn bè. Mỗi Unit có sáu đề, gồm nghe ở cả ba mức độ.')
    index=index.replace('/ 36 đề',f'/ {count} đề').replace('/ 108 sao',f'/ {count*3} sao')
    for old,new in [('>9</text>','>5</text>'),('>18</text>','>9</text>'),('>27</text>','>14</text>'),('>36</text>','>18</text>')]:index=index.replace(old,new)
    for symbol,letter in [('+','A'),('÷','B'),('×','C'),('=','?'),('%','!')]:index=index.replace('>'+symbol+'</span>','>'+letter+'</span>')
    index=index.replace('</head>','<style>:root[data-theme="light"]{--c2:#AD4278;--c2s:#FFE3F1;--c3:#AF4771;--c3s:#FFE8F1}:root[data-theme="dark"]{--c2:#FFB3D1;--c2s:#513447;--c3:#FFC2DD;--c3s:#513447}</style></head>')
    index=index.replace('</div></header>','</div></header><section class="wrap" style="margin-top:24px;margin-bottom:36px"><a class="cta" href="Unit1_AllAboutMe/LuyenNghe_Mau.html">🔊 Thử giọng nghe · 3 cấp độ</a><p>Mỗi đề Unit 1–3 có 6 câu nghe, chia đều ba mức. Em có thể nghe lại hoặc xem lời nghe khi cần hỗ trợ.</p></section>',1)
    (OUT/'index.html').write_text(index,encoding='utf-8',newline='\n')
    print(f'English built: {len(UNITS)} overviews + {count} tests ({count*24} questions)')


if __name__=='__main__':main()
