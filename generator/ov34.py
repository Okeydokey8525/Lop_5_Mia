# --- CD3 & CD4 overview content (appended to gen_overview.py)
def vert(rows,res,col):
    t='\n'.join(rows)
    return f'<div style="display:inline-block;background:#ffffff;border:3px solid {col};border-radius:14px;padding:10px 20px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:28px;font-weight:700;line-height:1.35;white-space:pre;text-align:right;color:#17303a">{t}\n<span style="display:block;border-top:3px solid {col}"></span><span style="color:{col}">{res}</span></div>'
def grid100(col):
    cells=''.join(f'<rect x="{10+i*13}" y="{10+j*13}" width="13" height="13" fill="none" stroke="{col}" stroke-opacity=".45" stroke-width="1"/>' for i in range(10) for j in range(10))
    return f'<svg width="160" height="150" viewBox="0 0 150 150"><rect x="10" y="10" width="130" height="130" fill="#ffffff" stroke="{col}" stroke-width="4"/>{cells}<rect x="10" y="10" width="13" height="13" fill="#f08a10"/><rect x="10" y="10" width="130" height="130" fill="none" stroke="{col}" stroke-width="4"/></svg>'
def unitrow(col,bg):
    names=['km²','ha','m²','dm²','cm²','mm²']
    cells=''.join(f'<div style="flex:1;background:{col};color:#fff;border-radius:12px;padding:8px 0;text-align:center;font-weight:800;font-size:26px">{n}</div>' for n in names)
    gaps=''.join(f'<div style="flex:1;text-align:center;font-size:20px;font-weight:700;color:{col}">× 100</div>' for _ in names[:-1])
    return f'<div style="display:flex;gap:8px">{cells}</div><div style="display:flex;gap:8px;padding:0 4%"><div style="flex:1;text-align:center;font-size:20px;font-weight:700;color:{col}">× 100 ở mỗi bậc, đi sang trái thì chia 100</div></div>'
LESSONS3=[
 dict(n=15,col='#2e7d32',bg='#e4f4e5',dk='#1b5e20',title='Ki-lô-mét vuông. Héc-ta',pg=None,head='Hai đơn vị để đo những mảnh đất rất rộng.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{grid100(c['dk'])}
<div style="flex:1 1 300px;display:flex;flex-direction:column;gap:10px">{chip(c['bg'],'#17303a','<b>1 km²</b> là diện tích hình vuông cạnh 1 km')}{chip(c['bg'],'#17303a','<b>1 ha</b> là diện tích hình vuông cạnh 100 m')}</div></div>
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','1 ha = <b>10 000</b> m²')}{chip(c['bg'],'#17303a','1 km² = <b>100</b> ha')}{chip(c['bg'],'#17303a','1 km² = <b>1 000 000</b> m²')}</div>
{box(c['bg'],'Hình vuông to có 100 ô nhỏ, mỗi ô là 1 ha. Ví dụ: ruộng 3 ha = 30 000 m²; 25 000 m² = <b>2,5 ha</b>.')}'''),
 dict(n=16,col='#1565c0',bg='#e3f0fc',dk='#0d47a1',title='Các đơn vị đo diện tích',pg=None,head='Cứ hai đơn vị liền nhau thì gấp (kém) nhau 100 lần.',
  body=lambda c: f'''
{unitrow(c['col'],c['bg'])}
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','1 m² = <b>100</b> dm²')}{chip(c['bg'],'#17303a','1 dm² = <b>100</b> cm²')}{chip(c['bg'],'#17303a','1 cm² = <b>100</b> mm²')}</div>
{box(c['bg'],'<b>Đổi đơn vị:</b> sang đơn vị nhỏ hơn thì nhân 100, 10 000,… Sang đơn vị lớn hơn thì chia. Ví dụ 3,5 m² = 3,5 × 100 = <b>350 dm²</b>; 4 m² 35 dm² = <b>4,35 m²</b>.')}'''),
 dict(n=17,col='#c4470a',bg='#fde9dc',dk='#8a2f05',title='Thực hành và trải nghiệm với một số đơn vị đo đại lượng',pg=None,head='Đo thật và tính diện tích những thứ quanh em.',
  body=lambda c: f'''
{box(c['bg'],'<b>Tình huống:</b> phòng hình chữ nhật dài 6 m, rộng 4,5 m. Lát gạch vuông cạnh 50 cm. Cần bao nhiêu viên gạch?')}
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','Phòng: 6 × 4,5 = <b>27 m²</b>')}{chip(c['bg'],'#17303a','Gạch: 0,5 × 0,5 = <b>0,25 m²</b>')}{chip(c['bg'],'#17303a','Số viên: 27 : 0,25 = <b>108</b>')}</div>
{box(c['bg'],'<b>Nhớ:</b> trước khi tính phải đổi các số đo về cùng một đơn vị (50 cm = 0,5 m).')}'''),
 dict(n=18,col='#6a1b9a',bg='#f1e4f7',dk='#4a148c',title='Luyện tập chung',pg=None,head='Kết hợp đổi đơn vị với diện tích và bài toán có lời văn.',
  body=lambda c: f'''
{box(c['bg'],'<b>Ví dụ:</b> mảnh đất hình chữ nhật dài 120 m, rộng 80 m. Diện tích bao nhiêu héc-ta?')}
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','120 × 80 = <b>9 600 m²</b>')}{chip(c['bg'],'#17303a','9 600 : 10 000 = <b>0,96 ha</b>')}</div>
{box(c['bg'],'<b>Mẹo:</b> đề cho đơn vị nào, đề hỏi đơn vị nào? Tính diện tích trước rồi mới đổi đơn vị ở bước cuối.')}'''),
]
LESSONS4=[
 dict(n=19,col='#c2185b',bg='#fce4ec',dk='#8e0f43',title='Phép cộng số thập phân',pg=None,head='Viết các số sao cho dấu phẩy thẳng cột rồi cộng như số tự nhiên.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{vert([' 35,60','+ 4,87'],'40,47',c['dk'])}
<div style="flex:1 1 300px;font-size:24px"><b>35,6 + 4,87:</b> viết 35,6 thành 35,60 cho đủ hai chữ số ở phần thập phân. Cộng từ phải sang trái, đặt dấu phẩy thẳng cột.</div></div>
{box(c['bg'],'Kết quả: 35,6 + 4,87 = <b>40,47</b>.')}'''),
 dict(n=20,col='#1565c0',bg='#e3f0fc',dk='#0d47a1',title='Phép trừ số thập phân',pg=None,head='Cũng viết dấu phẩy thẳng cột, thêm chữ số 0 nếu cần.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{vert(['12,50','− 4,68'],' 7,82',c['dk'])}
<div style="flex:1 1 300px;font-size:24px"><b>12,5 − 4,68:</b> viết 12,5 thành 12,50 rồi trừ từ phải sang trái, nhớ khi cần mượn.</div></div>
{box(c['bg'],'Kiểm tra bằng phép cộng: 7,82 + 4,68 = 12,50 <b>đúng</b>.')}'''),
 dict(n=21,col='#2e7d32',bg='#e4f4e5',dk='#1b5e20',title='Phép nhân số thập phân',pg=None,head='Nhân như số tự nhiên rồi đếm số chữ số ở phần thập phân.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','2,4 × 1,5: tính 24 × 15 = 360')}{chip(c['bg'],'#17303a','Hai thừa số có 2 chữ số thập phân')}{chip(c['bg'],'#17303a','2,4 × 1,5 = 3,60 = <b>3,6</b>')}</div>
{box(c['bg'],'<b>Quy tắc:</b> nhân như số tự nhiên, rồi tách ở tích bao nhiêu chữ số thập phân bằng tổng số chữ số thập phân của hai thừa số.')}'''),
 dict(n=22,col='#c4470a',bg='#fde9dc',dk='#8a2f05',title='Phép chia số thập phân',pg=None,head='Chia một số thập phân cho số tự nhiên và cho số thập phân.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','17,5 : 4 = <b>4,375</b>')}{chip(c['bg'],'#17303a','4,2 : 0,6 = 42 : 6 = <b>7</b>')}</div>
{box(c['bg'],'<b>Chia cho số tự nhiên:</b> chia phần nguyên, đặt dấu phẩy ở thương khi hạ chữ số đầu tiên của phần thập phân. Dư thì thêm 0 và chia tiếp.')}
{box(c['bg'],'<b>Chia cho số thập phân:</b> chuyển dấu phẩy của số chia và số bị chia sang phải cùng số chữ số như nhau rồi chia.')}'''),
 dict(n=23,col='#6a1b9a',bg='#f1e4f7',dk='#4a148c',title='Nhân, chia với 10; 100; 1 000;… hoặc 0,1; 0,01; 0,001',pg=None,head='Chỉ cần dời dấu phẩy.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','3,45 × 10 = <b>34,5</b>')}{chip(c['bg'],'#17303a','3,45 × 100 = <b>345</b>')}{chip(c['bg'],'#17303a','3,45 × 1 000 = <b>3 450</b>')}</div>
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','56,7 : 10 = <b>5,67</b>')}{chip(c['bg'],'#17303a','56,7 : 100 = <b>0,567</b>')}</div>
{box(c['bg'],'<b>Nhân</b> với 10; 100; 1 000: dấu phẩy sang <b>phải</b>. <b>Chia</b> cho 10; 100; 1 000: dấu phẩy sang <b>trái</b>. Nhân với 0,1 giống chia cho 10; chia cho 0,1 giống nhân với 10.')}'''),
 dict(n=24,col='#b71c1c',bg='#fde4e4',dk='#7f1313',title='Luyện tập chung',pg=None,head='Biểu thức, tính thuận tiện và bài toán có lời văn.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','(4,5 + 1,5) × 2,5 − 3,2 = 6 × 2,5 − 3,2 = 15 − 3,2 = <b>11,8</b>')}{chip(c['bg'],'#17303a','0,25 × 6,3 × 4 = (0,25 × 4) × 6,3 = <b>6,3</b>')}</div>
{box(c['bg'],'<b>Bài toán:</b> mua 2,5 kg táo, mỗi ki-lô-gam 36 000 đồng, đưa 100 000 đồng. Tiền táo 2,5 × 36 000 = 90 000 đồng; được trả lại 100 000 − 90 000 = <b>10 000 đồng</b>.')}
{box(c['bg'],'<b>Mẹo:</b> trong ngoặc trước, nhân chia trước, cộng trừ sau. Ước lượng kết quả trước để biết dấu phẩy có hợp lí không.')}'''),
]
def gen_sheet(num,title,sub,col,bg,lessons,short,intro1,intro2,foot):
    chips=''.join(f'<span style="background:{L["col"]};color:#ffffff;border-radius:999px;padding:6px 20px;font-size:22px;font-weight:700">Bài {L["n"]} · {s}</span>' for L,s in zip(lessons,short))
    blocks='\n\n'.join(lesson_block(L).replace('<span style="margin-top:auto;font-size:20px;font-weight:600">SGK trang None</span>','') for L in lessons)
    return nb(f'''<div style="width:1080px;box-sizing:border-box;padding:40px;background:{bg};color:#17303a;font-family:'Be Vietnam Pro',system-ui,sans-serif;font-size:26px;line-height:1.4;display:flex;flex-direction:column;gap:28px">
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
    return gen_sheet(3,'ĐƠN VỊ ĐO DIỆN TÍCH','Bốn bài học từ Bài 15 đến Bài 18 · Toán 5, tập một','#2e7d32','#e4f4e5',LESSONS3,['Km² và ha','Bảng đơn vị','Thực hành','Luyện tập chung'],
     'Đo những mảnh đất nhỏ và to đều cần đúng đơn vị.','Từ mi-li-mét vuông đến ki-lô-mét vuông, cứ hai đơn vị liền nhau hơn kém nhau 100 lần. Ngoại lệ dễ quên: 1 ha = 10 000 m² và 1 km² = 100 ha.','Theo sách Toán 5, tập một (Kết nối tri thức với cuộc sống), Chủ đề 3')
def cd4_sheet():
    return gen_sheet(4,'CÁC PHÉP TÍNH VỚI SỐ THẬP PHÂN','Sáu bài học từ Bài 19 đến Bài 24 · Toán 5, tập một','#6a1b9a','#f1e4f7',LESSONS4,['Cộng','Trừ','Nhân','Chia','Nhân, chia 10; 100;…','Luyện tập chung'],
     'Số thập phân cũng cộng, trừ, nhân, chia như số tự nhiên.','Điều cần chú ý nhất là vị trí của dấu phẩy: thẳng cột khi cộng trừ, đếm chữ số thập phân khi nhân, và dời dấu phẩy khi nhân chia với 10; 100; 1 000;…','Theo sách Toán 5, tập một (Kết nối tri thức với cuộc sống), Chủ đề 4')
