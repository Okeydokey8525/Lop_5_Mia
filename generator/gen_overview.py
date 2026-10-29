import re, pathlib, sys
sys.path.insert(0,'.')
from cfg import *
W=pathlib.Path(__file__).parent
fonts=(W/'fonts.css').read_text(encoding='utf-8')
DISP="font-family:'Baloo 2','Be Vietnam Pro',sans-serif"
def fr(n,d,big=False):
    fs='.82em'
    return f'<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1.15;font-size:{fs};margin:0 6px"><span style="border-bottom:3px solid currentColor;padding:0 8px 2px">{n}</span><span style="padding-top:2px">{d}</span></span>'
def mix(w,n,d): return f'<span style="white-space:nowrap">{w}{fr(n,d)}</span>'
def chip(bg,fg,html): return f'<div style="background:{bg};color:{fg};border-radius:16px;padding:10px 18px;font-size:26px;font-weight:600">{html}</div>'
def box(bg,html,fg='inherit'): return f'<div style="background:{bg};color:{fg};border-radius:16px;padding:12px 18px;font-size:24px">{html}</div>'

LESSONS1=[
 dict(n=1,col='#955077',bg='#F4E4EE',dk='#8e0f43',title='Ôn tập số tự nhiên',pg=6,head='Đọc, viết, so sánh và làm tròn các số có nhiều chữ số.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','5 chục nghìn, 2 nghìn, 8 trăm, 1 chục, 4 đơn vị = <b>52 814</b>')}</div>
<p style="margin:0;font-size:24px">52 814 đọc là: <b>năm mươi hai nghìn tám trăm mười bốn</b>.</p>
{box(c['bg'],'<b>So sánh:</b> số nào có nhiều chữ số hơn thì lớn hơn. Cùng số chữ số thì so từng hàng, từ trái sang phải.')}
{box(c['bg'],'<b>Làm tròn:</b> nhìn chữ số bên phải hàng cần làm tròn. Bé hơn 5 thì làm tròn xuống, từ 5 trở lên thì làm tròn lên. Ví dụ 48 362 ≈ <b>48 000</b>.')}'''),
 dict(n=2,col='#4A6F9D',bg='#E5EDF8',dk='#0d47a1',title='Ôn tập các phép tính với số tự nhiên',pg=9,head='Cộng, trừ, nhân, chia và tính nhanh cho thuận tiện.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','4 850 − 125 × 6 = 4 850 − 750 = <b>4 100</b>')}{chip(c['bg'],'#4A2433','(2 400 + 600) : 5 = <b>600</b>')}</div>
{box(c['bg'],'<b>Thứ tự tính:</b> trong ngoặc trước, nhân chia trước, cộng trừ sau.')}
{box(c['bg'],'<b>Tính thuận tiện:</b> ghép các số thành tròn chục, tròn trăm. Ví dụ 25 × 37 × 4 = (25 × 4) × 37 = 100 × 37 = <b>3 700</b>.')}'''),
 dict(n=3,col='#3E7266',bg='#E3F0EB',dk='#1b5e20',title='Ôn tập phân số',pg=11,head='Phân số chỉ một phần của cả một vật, rút gọn và so sánh phân số.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','Chia bánh 8 phần, ăn 3 phần: '+fr(3,8))}{chip(c['bg'],'#4A2433',fr(18,24)+' = '+fr('18 : 6','24 : 6')+' = <b>'+fr(3,4)+'</b>')}</div>
{box(c['bg'],'<b>Phân số bằng nhau:</b> nhân (hoặc chia) cả tử số và mẫu số với cùng một số khác 0. <b>Rút gọn</b> cho đến khi được phân số tối giản.')}
{box(c['bg'],'<b>So sánh:</b> cùng mẫu số thì tử số lớn hơn là lớn hơn. Khác mẫu số thì quy đồng mẫu số rồi so sánh. Ví dụ '+fr(2,3)+' = '+fr(8,12)+' bé hơn '+fr(3,4)+' = '+fr(9,12)+'.')}'''),
 dict(n=4,col='#77528F',bg='#EEE5F5',dk='#4a148c',title='Phân số thập phân',pg=14,head='Phân số có mẫu số là 10; 100; 1 000;…',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433',fr(3,10)+' · '+fr(57,100)+' · '+fr(365,1000)+' là phân số thập phân')}{chip(c['bg'],'#4A2433',fr(7,20)+' <b>không</b> phải phân số thập phân')}</div>
{box(c['bg'],'<b>Cách viết:</b> nhân cả tử số và mẫu số với cùng một số để mẫu số thành 10, 100, 1 000. Ví dụ '+fr(3,5)+' = '+fr('3 × 2','5 × 2')+' = <b>'+fr(6,10)+'</b>.')}
{box(c['bg'],'Phân số thập phân là cửa ngõ để học <b>số thập phân</b> ở Chủ đề 2.')}'''),
 dict(n=5,col='#477B70',bg='#dff3ef',dk='#004d40',title='Ôn tập các phép tính với phân số',pg=16,head='Cộng, trừ, nhân, chia phân số.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433',fr(7,9)+' − '+fr(4,9)+' = '+fr(3,9)+' = <b>'+fr(1,3)+'</b>')}{chip(c['bg'],'#4A2433',fr(2,3)+' × '+fr(3,4)+' = '+fr(6,12)+' = <b>'+fr(1,2)+'</b>')}</div>
{box(c['bg'],'<b>Cùng mẫu số:</b> cộng (trừ) tử số, giữ nguyên mẫu số.')}
{box(c['bg'],'<b>Nhân:</b> tử số nhân tử số, mẫu số nhân mẫu số. <b>Chia:</b> nhân với phân số đảo ngược. Ví dụ '+fr(4,5)+' : '+fr(2,3)+' = '+fr(4,5)+' × '+fr(3,2)+' = <b>'+fr(6,5)+'</b>.')}'''),
 dict(n=6,col='#94523F',bg='#FCE6DC',dk='#8a2f05',title='Cộng, trừ hai phân số khác mẫu số',pg=20,head='Quy đồng mẫu số rồi mới cộng hoặc trừ.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','Tô đổ '+fr(1,5)+' l, Việt đổ '+fr(1,2)+' l. Cả hai đổ bao nhiêu?')}</div>
{box(c['bg'],'<b>Bước 1:</b> mẫu số 5 và 2 không chia hết cho nhau, lấy mẫu số chung 5 × 2 = 10.<br><b>Bước 2:</b> '+fr(1,5)+' = '+fr(2,10)+'; '+fr(1,2)+' = '+fr(5,10)+'.<br><b>Bước 3:</b> '+fr(2,10)+' + '+fr(5,10)+' = <b>'+fr(7,10)+'</b> (l).')}
{box(c['bg'],'Trừ cũng làm như vậy: '+fr(3,4)+' − '+fr(1,6)+' = '+fr(9,12)+' − '+fr(2,12)+' = <b>'+fr(7,12)+'</b>.')}'''),
 dict(n=7,col='#9a6200',bg='#fdf0d3',dk='#6b4300',title='Hỗn số',pg=23,head='Một số gồm phần nguyên và phần phân số bé hơn 1.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','5 cái bánh chia cho 4 bạn, mỗi bạn được '+mix(1,1,4)+' cái')}{chip(c['bg'],'#4A2433',mix(1,1,4)+' đọc là <b>một và một phần tư</b>')}</div>
{box(c['bg'],'<b>Phân số → hỗn số:</b> chia tử số cho mẫu số. Thương là phần nguyên, số dư là tử số của phần phân số. Ví dụ '+fr(7,2)+' = <b>'+mix(3,1,2)+'</b>.')}
{box(c['bg'],'<b>Hỗn số → phân số:</b> phần nguyên × mẫu số + tử số. Ví dụ '+mix(2,1,3)+' = '+fr('2 × 3 + 1',3)+' = <b>'+fr(7,3)+'</b>.')}'''),
 dict(n=8,col='#37474f',bg='#e6ebee',dk='#263238',title='Ôn tập hình học và đo lường',pg=26,head='Đổi đơn vị khối lượng và nhận biết các loại góc.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','1 yến = <b>10</b> kg')}{chip(c['bg'],'#4A2433','1 tạ = <b>100</b> kg')}{chip(c['bg'],'#4A2433','1 tấn = <b>1 000</b> kg')}</div>
<div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center">
<svg width="150" height="86" viewBox="0 0 150 86"><path d="M14 74 H140 M14 74 L62 14" stroke="{c['dk']}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M44 74 A30 30 0 0 0 28 49" stroke="#94523F" stroke-width="4" fill="none"/></svg>
<svg width="110" height="86" viewBox="0 0 110 86"><path d="M18 74 H100 M18 74 V8" stroke="{c['dk']}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M18 56 H36 V74" stroke="#94523F" stroke-width="4" fill="none"/></svg>
<svg width="150" height="86" viewBox="0 0 150 86"><path d="M60 74 H140 M60 74 L16 22" stroke="{c['dk']}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M84 74 A24 24 0 0 0 72 53" stroke="#94523F" stroke-width="4" fill="none"/></svg>
<div style="flex:1 1 260px;font-size:24px"><b>Góc nhọn</b> bé hơn 90°, <b>góc vuông</b> bằng 90°, <b>góc tù</b> lớn hơn 90°. Dùng thước đo góc để kiểm tra.</div></div>
{box(c['bg'],'Ví dụ: 6 yến = 60 kg; 2 tạ = 200 kg; 5 tấn = 50 tạ.')}'''),
 dict(n=9,col='#b71c1c',bg='#fde4e4',dk='#7f1313',title='Luyện tập chung',pg=29,head='Gộp tất cả kĩ năng để giải bài toán có lời văn.',
  body=lambda c: f'''
{box(c['bg'],'<b>Bài toán trong sách:</b> Nam mua 2 bút bi giá 4 500 đồng một chiếc và 7 quyển vở giá 7 000 đồng một quyển. Nam đưa 100 000 đồng. Cô bán hàng trả lại bao nhiêu tiền?')}
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','Bút bi: 4 500 × 2 = 9 000')}{chip(c['bg'],'#4A2433','Vở: 7 000 × 7 = 49 000')}{chip(c['bg'],'#4A2433','Tất cả: 9 000 + 49 000 = 58 000')}{chip(c['bg'],'#4A2433','Trả lại: 100 000 − 58 000 = <b>42 000</b> đồng')}</div>
{box(c['bg'],'<b>Mẹo giải toán nhiều bước:</b> đọc kĩ đề, tìm cái đề hỏi, tính từng bước nhỏ, rồi kiểm tra lại kết quả.')}'''),
]
def lesson_block(L):
    c=L
    return f'''<div style="display:flex;background:#ffffff;border-radius:32px;overflow:hidden">
<div style="flex:none;width:210px;box-sizing:border-box;background:{c['bg']};color:{c['dk']};padding:28px 18px;display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center">
<span style="font-size:26px;font-weight:700">Bài</span>
<span style="{DISP};font-weight:800;font-size:104px;line-height:.9">{c['n']}</span>
<span style="font-size:24px;font-weight:700;line-height:1.25">{c['title']}</span>
<span style="margin-top:auto;font-size:20px;font-weight:600">SGK trang {c['pg']}</span>
</div>
<div style="flex:1;min-width:0;padding:28px 32px;display:flex;flex-direction:column;gap:16px">
<p style="margin:0;font-size:30px;font-weight:700;line-height:1.3;color:{c['col']}">{c['head']}</p>
{c['body'](c)}
</div></div>'''
def nb(html):
    def seg(m):
        return '>'+re.sub(r'(?<=\d) (?=\d{3}(?!\d))','\u00a0',m.group(1))+'<'
    return re.sub(r'>([^<]*)<',seg,html)
def cd1_sheet():
    chips=''.join(f'<span style="background:{L["col"]};color:#ffffff;border-radius:999px;padding:6px 20px;font-size:22px;font-weight:700">Bài {L["n"]} · {s}</span>' for L,s in zip(LESSONS1,['Số tự nhiên','Phép tính','Phân số','Thập phân','Phép tính phân số','Khác mẫu số','Hỗn số','Hình và đo lường','Luyện tập chung']))
    blocks='\n\n'.join(lesson_block(L) for L in LESSONS1)
    return nb(f'''<div style="width:1080px;box-sizing:border-box;padding:40px;background:#FFF5F8;color:#4A2433;font-family:'Be Vietnam Pro',system-ui,sans-serif;font-size:26px;line-height:1.4;display:flex;flex-direction:column;gap:28px">
<div style="display:flex;align-items:center;gap:32px;background:#B83F6B;color:#ffffff;border-radius:32px;padding:34px 40px">
<div style="flex:none;width:160px;height:160px;border-radius:50%;background:#fff3d6;color:#B83F6B;display:flex;flex-direction:column;align-items:center;justify-content:center;{DISP};font-weight:800;line-height:1"><span style="font-size:28px">Chủ đề</span><span style="font-size:96px">1</span></div>
<div style="display:flex;flex-direction:column;gap:6px;min-width:0">
<h1 style="margin:0;{DISP};font-weight:800;font-size:68px;line-height:1">ÔN TẬP VÀ BỔ SUNG</h1>
<p style="margin:0;font-size:26px;font-weight:600">Chín bài học từ Bài 1 đến Bài 9 · Toán 5, tập một</p>
</div></div>
<div style="display:flex;flex-wrap:wrap;gap:12px">{chips}</div>
<div style="background:#ffffff;border-radius:32px;padding:30px 40px;display:flex;flex-direction:column;gap:10px">
<p style="margin:0;font-size:30px;font-weight:700;color:#B83F6B">Chủ đề này ôn lại những gì em đã học để chuẩn bị cho lớp 5.</p>
<p style="margin:0">Số tự nhiên → phép tính → phân số → phân số thập phân → hỗn số → hình học và đo lường. Em nắm chắc phần này thì các chủ đề sau sẽ nhẹ nhàng hơn nhiều.</p>
</div>
{blocks}
<p style="margin:0;font-size:20px;font-weight:600;text-align:center">Theo sách Toán 5, tập một (Kết nối tri thức với cuộc sống), trang 6 đến 31</p>
</div>''')
def cd2_sheet():
    s=open(W/'assets'/'poster_cd2.html',encoding='utf-8').read()
    m=re.search(r'(<div style="width:1080px.*)</body>',s,re.S)
    return m.group(1).strip()
def page(title,sheet,cd,color):
    css=(W/'overview.css').read_text(encoding='utf-8')
    js=(W/'overview.js').read_text(encoding='utf-8')
    links=''.join(f'<a href="De{i}_{slug}.html">Đề {i} · {name}</a>' for i,(slug,name,_) in enumerate(cd['tests'],1))
    return f'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title><style>{fonts}</style><style>{css}</style><style>:root{{--c:{color}}}</style></head><body>
<nav class="nav" aria-label="Điều hướng chủ đề"><a class="home" href="../index.html">← Trang chủ</a><button class="view-toggle" id="view-toggle" type="button" aria-pressed="false">Đọc từng bài</button><details class="jump"><summary>Chọn đề</summary><div>{links}</div></details></nav>
<div id="clip"><div id="sheetw">{sheet}</div></div>
<div id="reader" aria-label="Tổng quan theo từng bài"></div>
<p class="ready">Em đã xem xong rồi? Làm bài kiểm tra nhé!</p><div class="foot">{links}</div>
<script>{js}</script></body></html>'''
# --- CD3 & CD4 overview content (appended to gen_overview.py)
def vert(rows,res,col):
    t='\n'.join(rows)
    return f'<div style="display:inline-block;background:#ffffff;border:3px solid {col};border-radius:14px;padding:10px 20px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:28px;font-weight:700;line-height:1.35;white-space:pre;text-align:right;color:#4A2433">{t}\n<span style="display:block;border-top:3px solid {col}"></span><span style="color:{col}">{res}</span></div>'
def grid100(col):
    cells=''.join(f'<rect x="{10+i*13}" y="{10+j*13}" width="13" height="13" fill="none" stroke="{col}" stroke-opacity=".45" stroke-width="1"/>' for i in range(10) for j in range(10))
    return f'<svg width="160" height="150" viewBox="0 0 150 150"><rect x="10" y="10" width="130" height="130" fill="#ffffff" stroke="{col}" stroke-width="4"/>{cells}<rect x="10" y="10" width="13" height="13" fill="#9D315A"/><rect x="10" y="10" width="130" height="130" fill="none" stroke="{col}" stroke-width="4"/></svg>'
def unitrow(col,bg):
    names=['km²','ha','m²','dm²','cm²','mm²']
    cells=''.join(f'<div style="flex:1;background:{col};color:#fff;border-radius:12px;padding:8px 0;text-align:center;font-weight:800;font-size:26px">{n}</div>' for n in names)
    gaps=''.join(f'<div style="flex:1;text-align:center;font-size:20px;font-weight:700;color:{col}">× 100</div>' for _ in names[:-1])
    return f'<div style="display:flex;gap:8px">{cells}</div><div style="display:flex;gap:8px;padding:0 4%"><div style="flex:1;text-align:center;font-size:20px;font-weight:700;color:{col}">× 100 ở mỗi bậc, đi sang trái thì chia 100</div></div>'
LESSONS3=[
 dict(n=15,col='#3E7266',bg='#E3F0EB',dk='#1b5e20',title='Ki-lô-mét vuông. Héc-ta',pg=53,head='Hai đơn vị để đo những mảnh đất rất rộng.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{grid100(c['dk'])}
<div style="flex:1 1 300px;display:flex;flex-direction:column;gap:10px">{chip(c['bg'],'#4A2433','<b>1 km²</b> là diện tích hình vuông cạnh 1 km')}{chip(c['bg'],'#4A2433','<b>1 ha</b> là diện tích hình vuông cạnh 100 m')}</div></div>
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','1 ha = <b>10 000</b> m²')}{chip(c['bg'],'#4A2433','1 km² = <b>100</b> ha')}{chip(c['bg'],'#4A2433','1 km² = <b>1 000 000</b> m²')}</div>
{box(c['bg'],'Hình vuông to có 100 ô nhỏ, mỗi ô là 1 ha. Ví dụ: ruộng 3 ha = 30 000 m²; 25 000 m² = <b>2,5 ha</b>.')}'''),
 dict(n=16,col='#4A6F9D',bg='#E5EDF8',dk='#0d47a1',title='Các đơn vị đo diện tích',pg=56,head='Cứ hai đơn vị liền nhau thì gấp (kém) nhau 100 lần.',
  body=lambda c: f'''
{unitrow(c['col'],c['bg'])}
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','1 m² = <b>100</b> dm²')}{chip(c['bg'],'#4A2433','1 dm² = <b>100</b> cm²')}{chip(c['bg'],'#4A2433','1 cm² = <b>100</b> mm²')}</div>
{box(c['bg'],'<b>Đổi đơn vị:</b> sang đơn vị nhỏ hơn thì nhân 100, 10 000,… Sang đơn vị lớn hơn thì chia. Ví dụ 3,5 m² = 3,5 × 100 = <b>350 dm²</b>; 4 m² 35 dm² = <b>4,35 m²</b>.')}'''),
 dict(n=17,col='#94523F',bg='#FCE6DC',dk='#8a2f05',title='Thực hành và trải nghiệm với một số đơn vị đo đại lượng',pg=60,head='Đo thật và tính diện tích những thứ quanh em.',
  body=lambda c: f'''
{box(c['bg'],'<b>Tình huống:</b> phòng hình chữ nhật dài 6 m, rộng 4,5 m. Lát gạch vuông cạnh 50 cm. Cần bao nhiêu viên gạch?')}
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','Phòng: 6 × 4,5 = <b>27 m²</b>')}{chip(c['bg'],'#4A2433','Gạch: 0,5 × 0,5 = <b>0,25 m²</b>')}{chip(c['bg'],'#4A2433','Số viên: 27 : 0,25 = <b>108</b>')}</div>
{box(c['bg'],'<b>Nhớ:</b> trước khi tính phải đổi các số đo về cùng một đơn vị (50 cm = 0,5 m).')}'''),
 dict(n=18,col='#77528F',bg='#EEE5F5',dk='#4a148c',title='Luyện tập chung',pg=62,head='Kết hợp đổi đơn vị với diện tích và bài toán có lời văn.',
  body=lambda c: f'''
{box(c['bg'],'<b>Ví dụ:</b> mảnh đất hình chữ nhật dài 120 m, rộng 80 m. Diện tích bao nhiêu héc-ta?')}
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','120 × 80 = <b>9 600 m²</b>')}{chip(c['bg'],'#4A2433','9 600 : 10 000 = <b>0,96 ha</b>')}</div>
{box(c['bg'],'<b>Mẹo:</b> đề cho đơn vị nào, đề hỏi đơn vị nào? Tính diện tích trước rồi mới đổi đơn vị ở bước cuối.')}'''),
]
LESSONS4=[
 dict(n=19,col='#955077',bg='#F4E4EE',dk='#8e0f43',title='Phép cộng số thập phân',pg=65,head='Viết các số sao cho dấu phẩy thẳng cột rồi cộng như số tự nhiên.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{vert([' 35,60','+ 4,87'],'40,47',c['dk'])}
<div style="flex:1 1 300px;font-size:24px"><b>35,6 + 4,87:</b> viết 35,6 thành 35,60 cho đủ hai chữ số ở phần thập phân. Cộng từ phải sang trái, đặt dấu phẩy thẳng cột.</div></div>
{box(c['bg'],'Kết quả: 35,6 + 4,87 = <b>40,47</b>.')}'''),
 dict(n=20,col='#4A6F9D',bg='#E5EDF8',dk='#0d47a1',title='Phép trừ số thập phân',pg=68,head='Cũng viết dấu phẩy thẳng cột, thêm chữ số 0 nếu cần.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{vert(['12,50','− 4,68'],' 7,82',c['dk'])}
<div style="flex:1 1 300px;font-size:24px"><b>12,5 − 4,68:</b> viết 12,5 thành 12,50 rồi trừ từ phải sang trái, nhớ khi cần mượn.</div></div>
{box(c['bg'],'Kiểm tra bằng phép cộng: 7,82 + 4,68 = 12,50 <b>đúng</b>.')}'''),
 dict(n=21,col='#3E7266',bg='#E3F0EB',dk='#1b5e20',title='Phép nhân số thập phân',pg=71,head='Nhân như số tự nhiên rồi đếm số chữ số ở phần thập phân.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','2,4 × 1,5: tính 24 × 15 = 360')}{chip(c['bg'],'#4A2433','Hai thừa số có 2 chữ số thập phân')}{chip(c['bg'],'#4A2433','2,4 × 1,5 = 3,60 = <b>3,6</b>')}</div>
{box(c['bg'],'<b>Quy tắc:</b> nhân như số tự nhiên, rồi tách ở tích bao nhiêu chữ số thập phân bằng tổng số chữ số thập phân của hai thừa số.')}'''),
 dict(n=22,col='#94523F',bg='#FCE6DC',dk='#8a2f05',title='Phép chia số thập phân',pg=76,head='Chia một số thập phân cho số tự nhiên và cho số thập phân.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','17,5 : 4 = <b>4,375</b>')}{chip(c['bg'],'#4A2433','4,2 : 0,6 = 42 : 6 = <b>7</b>')}</div>
{box(c['bg'],'<b>Chia cho số tự nhiên:</b> chia phần nguyên, đặt dấu phẩy ở thương khi hạ chữ số đầu tiên của phần thập phân. Dư thì thêm 0 và chia tiếp.')}
{box(c['bg'],'<b>Chia cho số thập phân:</b> chuyển dấu phẩy của số chia và số bị chia sang phải cùng số chữ số như nhau rồi chia.')}'''),
 dict(n=23,col='#77528F',bg='#EEE5F5',dk='#4a148c',title='Nhân, chia với 10; 100; 1 000;… hoặc 0,1; 0,01; 0,001',pg=83,head='Chỉ cần dời dấu phẩy.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','3,45 × 10 = <b>34,5</b>')}{chip(c['bg'],'#4A2433','3,45 × 100 = <b>345</b>')}{chip(c['bg'],'#4A2433','3,45 × 1 000 = <b>3 450</b>')}</div>
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','56,7 : 10 = <b>5,67</b>')}{chip(c['bg'],'#4A2433','56,7 : 100 = <b>0,567</b>')}</div>
{box(c['bg'],'<b>Nhân</b> với 10; 100; 1 000: dấu phẩy sang <b>phải</b>. <b>Chia</b> cho 10; 100; 1 000: dấu phẩy sang <b>trái</b>. Nhân với 0,1 giống chia cho 10; chia cho 0,1 giống nhân với 10.')}'''),
 dict(n=24,col='#b71c1c',bg='#fde4e4',dk='#7f1313',title='Luyện tập chung',pg=88,head='Biểu thức, tính thuận tiện và bài toán có lời văn.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','(4,5 + 1,5) × 2,5 − 3,2 = 6 × 2,5 − 3,2 = 15 − 3,2 = <b>11,8</b>')}{chip(c['bg'],'#4A2433','0,25 × 6,3 × 4 = (0,25 × 4) × 6,3 = <b>6,3</b>')}</div>
{box(c['bg'],'<b>Bài toán:</b> mua 2,5 kg táo, mỗi ki-lô-gam 36 000 đồng, đưa 100 000 đồng. Tiền táo 2,5 × 36 000 = 90 000 đồng; được trả lại 100 000 − 90 000 = <b>10 000 đồng</b>.')}
{box(c['bg'],'<b>Mẹo:</b> trong ngoặc trước, nhân chia trước, cộng trừ sau. Ước lượng kết quả trước để biết dấu phẩy có hợp lí không.')}'''),
]
def gen_sheet(num,title,sub,col,bg,lessons,short,intro1,intro2,foot):
    chips=''.join(f'<span style="background:{L["col"]};color:#ffffff;border-radius:999px;padding:6px 20px;font-size:22px;font-weight:700">Bài {L["n"]} · {s}</span>' for L,s in zip(lessons,short))
    blocks='\n\n'.join(lesson_block(L).replace('<span style="margin-top:auto;font-size:20px;font-weight:600">SGK trang None</span>','') for L in lessons)
    return nb(f'''<div style="width:1080px;box-sizing:border-box;padding:40px;background:{bg};color:#4A2433;font-family:'Be Vietnam Pro',system-ui,sans-serif;font-size:26px;line-height:1.4;display:flex;flex-direction:column;gap:28px">
<div style="display:flex;align-items:center;gap:32px;background:{col};color:#ffffff;border-radius:32px;padding:34px 40px">
<div style="flex:none;width:160px;height:160px;border-radius:50%;background:#fff3d6;color:{col};display:flex;flex-direction:column;align-items:center;justify-content:center;{DISP};font-weight:800;line-height:1"><span style="font-size:28px">Chủ đề</span><span style="font-size:96px">{num}</span></div>
<div style="display:flex;flex-direction:column;gap:6px;min-width:0">
<h1 style="margin:0;{DISP};font-weight:800;font-size:60px;line-height:1.05">{title}</h1>
<p style="margin:0;font-size:26px;font-weight:600">{sub}</p>
</div></div>
<div style="display:flex;flex-wrap:wrap;gap:12px">{chips}</div>
<div style="background:#ffffff;border-radius:32px;padding:30px 40px;display:flex;flex-direction:column;gap:10px">
<p style="margin:0;font-size:30px;font-weight:700;color:{col}">{intro1}</p>
<p style="margin:0">{intro2}</p>
</div>
{blocks}
<p style="margin:0;font-size:20px;font-weight:600;text-align:center">{foot}</p>
</div>''')
def cd3_sheet():
    return gen_sheet(3,'ĐƠN VỊ ĐO DIỆN TÍCH','Bốn bài học từ Bài 15 đến Bài 18 · Toán 5, tập một','#3E7266','#E3F0EB',LESSONS3,['Km² và ha','Bảng đơn vị','Thực hành','Luyện tập chung'],
     'Đo những mảnh đất nhỏ và to đều cần đúng đơn vị.','Từ mi-li-mét vuông đến ki-lô-mét vuông, cứ hai đơn vị liền nhau hơn kém nhau 100 lần. Ngoại lệ dễ quên: 1 ha = 10 000 m² và 1 km² = 100 ha.','Theo sách Toán 5, tập một (Kết nối tri thức với cuộc sống), Chủ đề 3')
def cd4_sheet():
    return gen_sheet(4,'CÁC PHÉP TÍNH VỚI SỐ THẬP PHÂN','Sáu bài học từ Bài 19 đến Bài 24 · Toán 5, tập một','#77528F','#EEE5F5',LESSONS4,['Cộng','Trừ','Nhân','Chia','Nhân, chia 10; 100;…','Luyện tập chung'],
     'Số thập phân cũng cộng, trừ, nhân, chia như số tự nhiên.','Điều cần chú ý nhất là vị trí của dấu phẩy: thẳng cột khi cộng trừ, đếm chữ số thập phân khi nhân, và dời dấu phẩy khi nhân chia với 10; 100; 1 000;…','Theo sách Toán 5, tập một (Kết nối tri thức với cuộc sống), Chủ đề 4')
# --- CD5 & CD6 overview content
def S_(col): return f'fill="#ffffff" stroke="{col}" stroke-width="4" stroke-linejoin="round"'
def tri_set(col,hl):
    items=[('nhọn','<polygon points="60,10 14,70 106,70"'),('vuông','<polygon points="22,10 22,70 106,70"'),('tù','<polygon points="8,12 44,72 108,72"'),('đều','<polygon points="62,6 22,75 102,75"')]
    out=''
    for name,poly in items:
        out+=f'<div style="display:flex;flex-direction:column;align-items:center;gap:2px"><svg width="120" height="80" viewBox="0 0 120 80">{poly} {S_(col)}/></svg><span style="font-size:20px;font-weight:700;color:{col}">tam giác {name}</span></div>'
    return f'<div style="display:flex;flex-wrap:wrap;gap:14px;justify-content:space-between">{out}</div>'
def tri_h(col):
    return f'''<svg width="190" height="120" viewBox="0 0 190 120"><polygon points="90,10 20,100 170,100" {S_(col)}/><line x1="90" y1="10" x2="90" y2="100" stroke="#9D315A" stroke-width="3" stroke-dasharray="6 5"/><path d="M90 88 h10 v12" fill="none" stroke="#9D315A" stroke-width="2.5"/><text x="98" y="62" font-size="20" font-weight="700" fill="{col}">h</text><text x="95" y="118" font-size="20" font-weight="700" text-anchor="middle" fill="{col}">a</text></svg>'''
def trap_ov(col):
    return f'''<svg width="210" height="145" viewBox="0 0 210 145"><polygon points="62,30 142,30 192,118 14,118" {S_(col)}/><line x1="62" y1="30" x2="62" y2="118" stroke="#9D315A" stroke-width="3" stroke-dasharray="6 5"/><path d="M62 106 h10 v12" fill="none" stroke="#9D315A" stroke-width="2.5"/><text x="102" y="22" font-size="20" font-weight="700" text-anchor="middle" fill="{col}">b</text><text x="102" y="140" font-size="20" font-weight="700" text-anchor="middle" fill="{col}">a</text><text x="70" y="80" font-size="20" font-weight="700" fill="{col}">h</text></svg>'''
def circ_ov(col):
    return f'''<svg width="170" height="130" viewBox="0 0 170 130"><circle cx="85" cy="65" r="52" {S_(col)}/><line x1="33" y1="65" x2="137" y2="65" stroke="#9D315A" stroke-width="3.5"/><circle cx="85" cy="65" r="4" fill="{col}"/><text x="85" y="54" font-size="20" font-weight="700" text-anchor="middle" fill="{col}">d</text><text x="112" y="88" font-size="20" font-weight="700" text-anchor="middle" fill="{col}">r</text><text x="78" y="90" font-size="18" font-weight="700" text-anchor="end" fill="{col}">O</text></svg>'''
def house_ov(col):
    return f'''<svg width="210" height="150" viewBox="0 0 210 150"><polygon points="105,8 20,62 190,62" fill="#ffe0cc" stroke="{col}" stroke-width="4" stroke-linejoin="round"/><rect x="20" y="62" width="170" height="70" fill="#ffffff" stroke="{col}" stroke-width="4"/><text x="105" y="52" font-size="15" font-weight="700" text-anchor="middle" fill="{col}">tam giác</text><text x="105" y="104" font-size="18" font-weight="700" text-anchor="middle" fill="{col}">hình chữ nhật</text></svg>'''
def pond_ov(col):
    return f'''<svg width="230" height="130" viewBox="0 0 230 130"><rect x="14" y="10" width="202" height="108" fill="#ffffff" stroke="{col}" stroke-width="4"/><circle cx="115" cy="64" r="34" fill="#b7dcf2" stroke="{col}" stroke-width="4"/><text x="115" y="69" font-size="18" font-weight="700" text-anchor="middle" fill="{col}">ao tròn</text></svg>'''
LESSONS5=[
 dict(n=25,col='#94523F',bg='#FCE6DC',dk='#8a2f05',title='Hình tam giác. Diện tích hình tam giác',pg=91,head='Nhận biết các loại tam giác và tính diện tích.',
  body=lambda c: f'''
{tri_set(c['dk'],c['bg'])}
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{tri_h(c['dk'])}
<div style="flex:1 1 280px;display:flex;flex-direction:column;gap:10px">{chip(c['bg'],'#4A2433','<b>S = a × h : 2</b>')}<div style="font-size:23px">a là đáy, h là chiều cao (đường cao vuông góc với đáy). Cùng một đơn vị đo.</div></div></div>
{box(c['bg'],'<b>Ví dụ:</b> đáy 4 cm, chiều cao 3 cm thì S = 4 × 3 : 2 = <b>6 cm²</b>.')}'''),
 dict(n=26,col='#00838f',bg='#dff3f6',dk='#006064',title='Hình thang. Diện tích hình thang',pg=98,head='Hình thang có một cặp cạnh đối song song.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{trap_ov(c['dk'])}
<div style="flex:1 1 280px;display:flex;flex-direction:column;gap:10px">{chip(c['bg'],'#4A2433','<b>S = (a + b) × h : 2</b>')}<div style="font-size:23px">a và b là hai cạnh đáy song song, h là chiều cao (độ dài đường cao).</div></div></div>
{box(c['bg'],'<b>Ví dụ:</b> đáy 9 cm và 5 cm, chiều cao 4 cm thì S = (9 + 5) × 4 : 2 = <b>28 cm²</b>.')}
{box(c['bg'],'<b>Tìm chiều cao:</b> h = S × 2 : (a + b). Ví dụ S = 84 cm², hai đáy 14 cm và 10 cm: h = 84 × 2 : 24 = <b>7 cm</b>.')}'''),
 dict(n=27,col='#3E7266',bg='#E3F0EB',dk='#1b5e20',title='Đường tròn. Chu vi và diện tích hình tròn',pg=105,head='Tâm, bán kính, đường kính, chu vi và diện tích.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{circ_ov(c['dk'])}
<div style="flex:1 1 280px;display:flex;flex-direction:column;gap:10px">{chip(c['bg'],'#4A2433','<b>d = r × 2</b>')}{chip(c['bg'],'#4A2433','<b>C = 3,14 × d</b> hay C = 3,14 × r × 2')}{chip(c['bg'],'#4A2433','<b>S = 3,14 × r × r</b>')}</div></div>
{box(c['bg'],'<b>Ví dụ:</b> hình tròn đường kính 2 dm có chu vi 3,14 × 2 = <b>6,28 dm</b>. Hình tròn bán kính 10 cm có diện tích 3,14 × 10 × 10 = <b>314 cm²</b>.')}
{box(c['bg'],'<b>Chú ý:</b> bán bính gấp đôi thì chu vi gấp đôi, nhưng diện tích gấp 4 lần.'.replace('bán bính','bán kính'))}'''),
 dict(n=28,col='#77528F',bg='#EEE5F5',dk='#4a148c',title='Thực hành và trải nghiệm đo, vẽ, lắp ghép, tạo hình',pg=113,head='Ghép các hình cơ bản thành ngôi nhà, con gà, bông hoa.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{house_ov(c['dk'])}
<div style="flex:1 1 280px;display:flex;flex-direction:column;gap:10px">{chip(c['bg'],'#4A2433','Mái nhà: hình <b>tam giác</b>')}{chip(c['bg'],'#4A2433','Thân nhà: hình <b>chữ nhật</b>')}</div></div>
{box(c['bg'],'<b>Diện tích hình ghép</b> = tổng diện tích các hình thành phần (không chồng lên nhau). Ví dụ mái 6 m² và thân nhà 18 m² thì cả hình là 6 + 18 = <b>24 m²</b>.')}'''),
 dict(n=29,col='#477B70',bg='#dff3ef',dk='#004d40',title='Luyện tập chung',pg=116,head='Cắt bớt một phần thì lấy diện tích cả hình trừ đi phần cắt.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{pond_ov(c['dk'])}
<div style="flex:1 1 280px;display:flex;flex-direction:column;gap:10px"><div style="font-size:23px">Khu đất hình chữ nhật 30 m × 20 m có ao tròn bán kính 4 m.</div></div></div>
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','Khu đất: 30 × 20 = <b>600 m²</b>')}{chip(c['bg'],'#4A2433','Ao: 3,14 × 4 × 4 = <b>50,24 m²</b>')}{chip(c['bg'],'#4A2433','Còn lại: 600 − 50,24 = <b>549,76 m²</b>')}</div>
{box(c['bg'],'<b>Mẹo:</b> vẽ hình, ghi số đo lên hình, chia hình thành các hình quen thuộc rồi mới tính.')}'''),
]
def unit_table(col,rows):
    tr=''.join(f'<div style="display:flex;gap:8px;align-items:center"><span style="flex:none;width:110px;background:{col};color:#fff;border-radius:10px;padding:4px 0;text-align:center;font-weight:800;font-size:21px">{h}</span><span style="font-size:23px">{t}</span></div>' for h,t in rows)
    return f'<div style="display:flex;flex-direction:column;gap:8px">{tr}</div>'
LESSONS6=[
 dict(n=30,col='#955077',bg='#F4E4EE',dk='#8e0f43',title='Ôn tập số thập phân',pg=120,head='Đọc, viết, so sánh và làm tròn số thập phân.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','23,81: hai mươi ba phẩy <b>tám mươi mốt</b>')}{chip(c['bg'],'#4A2433','Trong 2,03: chữ số 3 ở hàng <b>phần trăm</b>')}</div>
{box(c['bg'],'<b>So sánh:</b> so phần nguyên trước, bằng nhau thì so lần lượt phần mười, phần trăm, phần nghìn. Ví dụ 4,09 &lt; 4,1; 12,50 = 12,5.')}
{box(c['bg'],'<b>Làm tròn:</b> nhìn chữ số bên phải hàng cần làm tròn. Bé hơn 5 thì giữ nguyên, từ 5 trở lên thì cộng thêm 1. Ví dụ 7,46 ≈ <b>7,5</b> (phần mười) và 12,375 ≈ <b>12,38</b> (phần trăm).')}'''),
 dict(n=31,col='#4A6F9D',bg='#E5EDF8',dk='#0d47a1',title='Ôn tập các phép tính với số thập phân',pg=123,head='Cộng, trừ, nhân, chia và nhân chia với 10; 100; 0,1; 0,01.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','24,6 + 5,75 = <b>30,35</b>')}{chip(c['bg'],'#4A2433','40 − 12,8 = <b>27,2</b>')}{chip(c['bg'],'#4A2433','3,5 × 4 = <b>14</b>')}{chip(c['bg'],'#4A2433','9 : 4 = <b>2,25</b>')}</div>
{box(c['bg'],'<b>Cộng, trừ:</b> dấu phẩy thẳng cột. <b>Nhân:</b> đếm số chữ số thập phân của hai thừa số. <b>Chia:</b> chuyển dấu phẩy của số chia và số bị chia sang phải cùng số chữ số.')}
{box(c['bg'],'<b>Dời dấu phẩy:</b> × 10; 100; 1 000 sang phải, : 10; 100; 1 000 sang trái. × 0,1 giống : 10; : 0,1 giống × 10.')}'''),
 dict(n=32,col='#3E7266',bg='#E3F0EB',dk='#1b5e20',title='Ôn tập một số hình phẳng',pg=127,head='Nhận biết hình, đáy và đường cao tương ứng.',
  body=lambda c: f'''
{tri_set(c['dk'],c['bg'])}
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433','Hình thang: <b>một cặp</b> cạnh đối song song')}{chip(c['bg'],'#4A2433','Hình tròn: d = r × 2')}</div>
{box(c['bg'],'<b>Đường cao</b> của hình tam giác hay hình thang luôn <b>vuông góc</b> với cạnh đáy tương ứng.')}'''),
 dict(n=33,col='#94523F',bg='#FCE6DC',dk='#8a2f05',title='Ôn tập diện tích, chu vi một số hình phẳng',pg=130,head='Tất cả công thức cần nhớ trong một bảng.',
  body=lambda c: f'''
{unit_table(c['col'],[('Chữ nhật','P = (dài + rộng) × 2; S = dài × rộng'),('Vuông','P = cạnh × 4; S = cạnh × cạnh'),('Tam giác','S = a × h : 2'),('Hình thang','S = (a + b) × h : 2'),('Hình tròn','C = 3,14 × d; S = 3,14 × r × r')])}
{box(c['bg'],'<b>Ví dụ:</b> hình thang đáy 14 cm và 10 cm, cao 7 cm có S = (14 + 10) × 7 : 2 = <b>84 cm²</b>.')}'''),
 dict(n=34,col='#77528F',bg='#EEE5F5',dk='#4a148c',title='Ôn tập đo lường',pg=133,head='Đổi các đơn vị đo độ dài, khối lượng và diện tích.',
  body=lambda c: f'''
{unit_table(c['col'],[('Độ dài','1 km = 1 000 m; 1 m = 10 dm = 100 cm = 1 000 mm'),('Khối lượng','1 tấn = 10 tạ = 1 000 kg; 1 kg = 1 000 g'),('Diện tích','1 km² = 100 ha; 1 ha = 10 000 m²; 1 m² = 100 dm²'),('Thể tích','1 l = 1 000 ml')])}
{box(c['bg'],'<b>Ví dụ:</b> 3 km 250 m = <b>3,25 km</b>; 2,35 tạ = <b>235 kg</b>; 0,12 km² = <b>12 ha</b>.')}'''),
 dict(n=35,col='#477B70',bg='#dff3ef',dk='#004d40',title='Ôn tập chung',pg=135,head='Hỗn số, phân số, số thập phân trong một bài.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#4A2433',fr(17,5)+' = <b>'+mix(3,2,5)+'</b>')}{chip(c['bg'],'#4A2433',mix(3,2,5)+' = <b>'+fr(17,5)+'</b>')}{chip(c['bg'],'#4A2433',fr(7,20)+' = '+fr(35,100)+' = <b>0,35</b>')}</div>
{box(c['bg'],'<b>Phân số:</b> cùng mẫu số thì cộng (trừ) tử số, khác mẫu số thì quy đồng trước. Ví dụ '+fr(5,6)+' − '+fr(1,4)+' = '+fr(10,12)+' − '+fr(3,12)+' = <b>'+fr(7,12)+'</b>.')}
{box(c['bg'],'<b>Tính thuận tiện:</b> 3,7 × 6,5 + 3,7 × 3,5 = 3,7 × (6,5 + 3,5) = 3,7 × 10 = <b>37</b>.')}'''),
]
def cd5_sheet():
    return gen_sheet(5,'MỘT SỐ HÌNH PHẲNG, CHU VI VÀ DIỆN TÍCH','Năm bài học từ Bài 25 đến Bài 29 · Toán 5, tập một','#4A6F9D','#E5EDF8',LESSONS5,['Tam giác','Hình thang','Hình tròn','Lắp ghép','Luyện tập chung'],
     'Ba hình mới cần nhớ: tam giác, hình thang, hình tròn.','Mỗi hình có một công thức. Em chỉ cần xác định đúng đáy, chiều cao hoặc bán kính rồi thay số. Nhớ đổi các số đo về cùng một đơn vị.','Theo sách Toán 5, tập một (Kết nối tri thức với cuộc sống), Chủ đề 5')
def cd6_sheet():
    return gen_sheet(6,'ÔN TẬP HỌC KÌ 1','Sáu bài học từ Bài 30 đến Bài 35 · Toán 5, tập một','#955077','#F4E4EE',LESSONS6,['Số thập phân','Phép tính','Hình phẳng','Chu vi, diện tích','Đo lường','Ôn tập chung'],
     'Nhìn lại toàn bộ kiến thức học kì 1.','Số thập phân, các phép tính, hình phẳng, đo lường, phân số. Làm xong sáu đề này là em đã sẵn sàng cho bài kiểm tra cuối kì.','Theo sách Toán 5, tập một (Kết nối tri thức với cuộc sống), Chủ đề 6')

if __name__ == '__main__':
    for cd,sheet,color in [(CDS[0],cd1_sheet(),'#B83F6B'),(CDS[1],cd2_sheet(),'#94523F'),(CDS[2],cd3_sheet(),'#3E7266'),(CDS[3],cd4_sheet(),'#77528F'),(CDS[4],cd5_sheet(),'#4A6F9D'),(CDS[5],cd6_sheet(),'#955077')]:
        d=W/'out'/ROOT/cd['dir']; d.mkdir(parents=True,exist_ok=True)
        (d/(cd['overview']+'.html')).write_text(page(f"Toán 5 · Chủ đề {cd['n']} · Tổng quan",sheet,cd,color),encoding='utf-8',newline='\n')
    print('ok')
