# --- CD5 & CD6 overview content
def S_(col): return f'fill="#ffffff" stroke="{col}" stroke-width="4" stroke-linejoin="round"'
def tri_set(col,hl):
    items=[('nhọn','<polygon points="60,10 14,70 106,70"'),('vuông','<polygon points="22,10 22,70 106,70"'),('tù','<polygon points="8,12 44,72 108,72"'),('đều','<polygon points="62,6 22,75 102,75"')]
    out=''
    for name,poly in items:
        out+=f'<div style="display:flex;flex-direction:column;align-items:center;gap:2px"><svg width="120" height="80" viewBox="0 0 120 80">{poly} {S_(col)}/></svg><span style="font-size:20px;font-weight:700;color:{col}">tam giác {name}</span></div>'
    return f'<div style="display:flex;flex-wrap:wrap;gap:14px;justify-content:space-between">{out}</div>'
def tri_h(col):
    return f'''<svg width="190" height="120" viewBox="0 0 190 120"><polygon points="90,10 20,100 170,100" {S_(col)}/><line x1="90" y1="10" x2="90" y2="100" stroke="#f08a10" stroke-width="3" stroke-dasharray="6 5"/><path d="M90 88 h10 v12" fill="none" stroke="#f08a10" stroke-width="2.5"/><text x="98" y="62" font-size="20" font-weight="700" fill="{col}">h</text><text x="95" y="118" font-size="20" font-weight="700" text-anchor="middle" fill="{col}">a</text></svg>'''
def trap_ov(col):
    return f'''<svg width="210" height="145" viewBox="0 0 210 145"><polygon points="62,30 142,30 192,118 14,118" {S_(col)}/><line x1="62" y1="30" x2="62" y2="118" stroke="#f08a10" stroke-width="3" stroke-dasharray="6 5"/><path d="M62 106 h10 v12" fill="none" stroke="#f08a10" stroke-width="2.5"/><text x="102" y="22" font-size="20" font-weight="700" text-anchor="middle" fill="{col}">b</text><text x="102" y="140" font-size="20" font-weight="700" text-anchor="middle" fill="{col}">a</text><text x="70" y="80" font-size="20" font-weight="700" fill="{col}">h</text></svg>'''
def circ_ov(col):
    return f'''<svg width="170" height="130" viewBox="0 0 170 130"><circle cx="85" cy="65" r="52" {S_(col)}/><line x1="33" y1="65" x2="137" y2="65" stroke="#f08a10" stroke-width="3.5"/><circle cx="85" cy="65" r="4" fill="{col}"/><text x="85" y="54" font-size="20" font-weight="700" text-anchor="middle" fill="{col}">d</text><text x="112" y="88" font-size="20" font-weight="700" text-anchor="middle" fill="{col}">r</text><text x="78" y="90" font-size="18" font-weight="700" text-anchor="end" fill="{col}">O</text></svg>'''
def house_ov(col):
    return f'''<svg width="210" height="150" viewBox="0 0 210 150"><polygon points="105,8 20,62 190,62" fill="#ffe0cc" stroke="{col}" stroke-width="4" stroke-linejoin="round"/><rect x="20" y="62" width="170" height="70" fill="#ffffff" stroke="{col}" stroke-width="4"/><text x="105" y="52" font-size="15" font-weight="700" text-anchor="middle" fill="{col}">tam giác</text><text x="105" y="104" font-size="18" font-weight="700" text-anchor="middle" fill="{col}">hình chữ nhật</text></svg>'''
def pond_ov(col):
    return f'''<svg width="230" height="130" viewBox="0 0 230 130"><rect x="14" y="10" width="202" height="108" fill="#ffffff" stroke="{col}" stroke-width="4"/><circle cx="115" cy="64" r="34" fill="#b7dcf2" stroke="{col}" stroke-width="4"/><text x="115" y="69" font-size="18" font-weight="700" text-anchor="middle" fill="{col}">ao tròn</text></svg>'''
LESSONS5=[
 dict(n=25,col='#c4470a',bg='#fde9dc',dk='#8a2f05',title='Hình tam giác. Diện tích hình tam giác',pg=91,head='Nhận biết các loại tam giác và tính diện tích.',
  body=lambda c: f'''
{tri_set(c['dk'],c['bg'])}
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{tri_h(c['dk'])}
<div style="flex:1 1 280px;display:flex;flex-direction:column;gap:10px">{chip(c['bg'],'#17303a','<b>S = a × h : 2</b>')}<div style="font-size:23px">a là đáy, h là chiều cao (đường cao vuông góc với đáy). Cùng một đơn vị đo.</div></div></div>
{box(c['bg'],'<b>Ví dụ:</b> đáy 4 cm, chiều cao 3 cm thì S = 4 × 3 : 2 = <b>6 cm²</b>.')}'''),
 dict(n=26,col='#1565c0',bg='#e3f0fc',dk='#0d47a1',title='Hình thang. Diện tích hình thang',pg=98,head='Hình thang có một cặp cạnh đối song song.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{trap_ov(c['dk'])}
<div style="flex:1 1 280px;display:flex;flex-direction:column;gap:10px">{chip(c['bg'],'#17303a','<b>S = (a + b) × h : 2</b>')}<div style="font-size:23px">a và b là hai cạnh đáy song song, h là chiều cao (độ dài đường cao).</div></div></div>
{box(c['bg'],'<b>Ví dụ:</b> đáy 9 cm và 5 cm, chiều cao 4 cm thì S = (9 + 5) × 4 : 2 = <b>28 cm²</b>.')}
{box(c['bg'],'<b>Tìm chiều cao:</b> h = S × 2 : (a + b). Ví dụ S = 84 cm², hai đáy 14 cm và 10 cm: h = 84 × 2 : 24 = <b>7 cm</b>.')}'''),
 dict(n=27,col='#2e7d32',bg='#e4f4e5',dk='#1b5e20',title='Đường tròn. Chu vi và diện tích hình tròn',pg=105,head='Tâm, bán kính, đường kính, chu vi và diện tích.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{circ_ov(c['dk'])}
<div style="flex:1 1 280px;display:flex;flex-direction:column;gap:10px">{chip(c['bg'],'#17303a','<b>d = r × 2</b>')}{chip(c['bg'],'#17303a','<b>C = 3,14 × d</b> hay C = 3,14 × r × 2')}{chip(c['bg'],'#17303a','<b>S = 3,14 × r × r</b>')}</div></div>
{box(c['bg'],'<b>Ví dụ:</b> hình tròn đường kính 2 dm có chu vi 3,14 × 2 = <b>6,28 dm</b>. Hình tròn bán kính 10 cm có diện tích 3,14 × 10 × 10 = <b>314 cm²</b>.')}
{box(c['bg'],'<b>Chú ý:</b> bán bính gấp đôi thì chu vi gấp đôi, nhưng diện tích gấp 4 lần.'.replace('bán bính','bán kính'))}'''),
 dict(n=28,col='#6a1b9a',bg='#f1e4f7',dk='#4a148c',title='Thực hành và trải nghiệm đo, vẽ, lắp ghép, tạo hình',pg=113,head='Ghép các hình cơ bản thành ngôi nhà, con thuyền, bông hoa.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{house_ov(c['dk'])}
<div style="flex:1 1 280px;display:flex;flex-direction:column;gap:10px">{chip(c['bg'],'#17303a','Mái nhà: hình <b>tam giác</b>')}{chip(c['bg'],'#17303a','Thân nhà: hình <b>chữ nhật</b>')}</div></div>
{box(c['bg'],'<b>Diện tích hình ghép</b> = tổng diện tích các hình thành phần (không chồng lên nhau). Ví dụ mái 6 m² và thân nhà 18 m² thì cả hình là 6 + 18 = <b>24 m²</b>.')}'''),
 dict(n=29,col='#00695c',bg='#dff3ef',dk='#004d40',title='Luyện tập chung',pg=116,head='Cắt bớt một phần thì lấy diện tích cả hình trừ đi phần cắt.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{pond_ov(c['dk'])}
<div style="flex:1 1 280px;display:flex;flex-direction:column;gap:10px"><div style="font-size:23px">Khu đất hình chữ nhật 30 m × 20 m có ao tròn bán kính 4 m.</div></div></div>
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','Khu đất: 30 × 20 = <b>600 m²</b>')}{chip(c['bg'],'#17303a','Ao: 3,14 × 4 × 4 = <b>50,24 m²</b>')}{chip(c['bg'],'#17303a','Còn lại: 600 − 50,24 = <b>549,76 m²</b>')}</div>
{box(c['bg'],'<b>Mẹo:</b> vẽ hình, ghi số đo lên hình, chia hình thành các hình quen thuộc rồi mới tính.')}'''),
]
def unit_table(col,rows):
    tr=''.join(f'<div style="display:flex;gap:8px;align-items:center"><span style="flex:none;width:110px;background:{col};color:#fff;border-radius:10px;padding:4px 0;text-align:center;font-weight:800;font-size:21px">{h}</span><span style="font-size:23px">{t}</span></div>' for h,t in rows)
    return f'<div style="display:flex;flex-direction:column;gap:8px">{tr}</div>'
LESSONS6=[
 dict(n=30,col='#c2185b',bg='#fce4ec',dk='#8e0f43',title='Ôn tập số thập phân',pg=120,head='Đọc, viết, so sánh và làm tròn số thập phân.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','23,81: hai mươi ba phẩy <b>tám mươi mốt</b>')}{chip(c['bg'],'#17303a','Trong 2,03: chữ số 3 ở hàng <b>phần trăm</b>')}</div>
{box(c['bg'],'<b>So sánh:</b> so phần nguyên trước, bằng nhau thì so lần lượt phần mười, phần trăm, phần nghìn. Ví dụ 4,09 &lt; 4,1; 12,50 = 12,5.')}
{box(c['bg'],'<b>Làm tròn:</b> nhìn chữ số bên phải hàng cần làm tròn. Bé hơn 5 thì giữ nguyên, từ 5 trở lên thì cộng thêm 1. Ví dụ 7,46 ≈ <b>7,5</b> (phần mười) và 12,375 ≈ <b>12,38</b> (phần trăm).')}'''),
 dict(n=31,col='#1565c0',bg='#e3f0fc',dk='#0d47a1',title='Ôn tập các phép tính với số thập phân',pg=123,head='Cộng, trừ, nhân, chia và nhân chia với 10; 100; 0,1; 0,01.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','24,6 + 5,75 = <b>30,35</b>')}{chip(c['bg'],'#17303a','40 − 12,8 = <b>27,2</b>')}{chip(c['bg'],'#17303a','3,5 × 4 = <b>14</b>')}{chip(c['bg'],'#17303a','9 : 4 = <b>2,25</b>')}</div>
{box(c['bg'],'<b>Cộng, trừ:</b> dấu phẩy thẳng cột. <b>Nhân:</b> đếm số chữ số thập phân của hai thừa số. <b>Chia:</b> chuyển dấu phẩy của số chia và số bị chia sang phải cùng số chữ số.')}
{box(c['bg'],'<b>Dời dấu phẩy:</b> × 10; 100; 1 000 sang phải, : 10; 100; 1 000 sang trái. × 0,1 giống : 10; : 0,1 giống × 10.')}'''),
 dict(n=32,col='#2e7d32',bg='#e4f4e5',dk='#1b5e20',title='Ôn tập một số hình phẳng',pg=127,head='Nhận biết hình, đáy và đường cao tương ứng.',
  body=lambda c: f'''
{tri_set(c['dk'],c['bg'])}
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a','Hình thang: <b>một cặp</b> cạnh đối song song')}{chip(c['bg'],'#17303a','Hình tròn: d = r × 2')}</div>
{box(c['bg'],'<b>Đường cao</b> của hình tam giác hay hình thang luôn <b>vuông góc</b> với cạnh đáy tương ứng.')}'''),
 dict(n=33,col='#c4470a',bg='#fde9dc',dk='#8a2f05',title='Ôn tập diện tích, chu vi một số hình phẳng',pg=130,head='Tất cả công thức cần nhớ trong một bảng.',
  body=lambda c: f'''
{unit_table(c['col'],[('Chữ nhật','P = (dài + rộng) × 2; S = dài × rộng'),('Vuông','P = cạnh × 4; S = cạnh × cạnh'),('Tam giác','S = a × h : 2'),('Hình thang','S = (a + b) × h : 2'),('Hình tròn','C = 3,14 × d; S = 3,14 × r × r')])}
{box(c['bg'],'<b>Ví dụ:</b> hình thang đáy 14 cm và 10 cm, cao 7 cm có S = (14 + 10) × 7 : 2 = <b>84 cm²</b>.')}'''),
 dict(n=34,col='#6a1b9a',bg='#f1e4f7',dk='#4a148c',title='Ôn tập đo lường',pg=133,head='Đổi các đơn vị đo độ dài, khối lượng và diện tích.',
  body=lambda c: f'''
{unit_table(c['col'],[('Độ dài','1 km = 1 000 m; 1 m = 10 dm = 100 cm = 1 000 mm'),('Khối lượng','1 tấn = 10 tạ = 1 000 kg; 1 kg = 1 000 g'),('Diện tích','1 km² = 100 ha; 1 ha = 10 000 m²; 1 m² = 100 dm²'),('Thể tích','1 l = 1 000 ml')])}
{box(c['bg'],'<b>Ví dụ:</b> 3 km 250 m = <b>3,25 km</b>; 2,35 tạ = <b>235 kg</b>; 0,12 km² = <b>12 ha</b>.')}'''),
 dict(n=35,col='#00695c',bg='#dff3ef',dk='#004d40',title='Ôn tập chung',pg=135,head='Hỗn số, phân số, số thập phân trong một bài.',
  body=lambda c: f'''
<div style="display:flex;flex-wrap:wrap;gap:12px">{chip(c['bg'],'#17303a',fr(17,5)+' = <b>'+mix(3,2,5)+'</b>')}{chip(c['bg'],'#17303a',mix(3,2,5)+' = <b>'+fr(17,5)+'</b>')}{chip(c['bg'],'#17303a',fr(7,20)+' = '+fr(35,100)+' = <b>0,35</b>')}</div>
{box(c['bg'],'<b>Phân số:</b> cùng mẫu số thì cộng (trừ) tử số, khác mẫu số thì quy đồng trước. Ví dụ '+fr(5,6)+' − '+fr(1,4)+' = '+fr(10,12)+' − '+fr(3,12)+' = <b>'+fr(7,12)+'</b>.')}
{box(c['bg'],'<b>Tính thuận tiện:</b> 3,7 × 6,5 + 3,7 × 3,5 = 3,7 × (6,5 + 3,5) = 3,7 × 10 = <b>37</b>.')}'''),
]
def cd5_sheet():
    return gen_sheet(5,'MỘT SỐ HÌNH PHẲNG, CHU VI VÀ DIỆN TÍCH','Năm bài học từ Bài 25 đến Bài 29 · Toán 5, tập một','#c4470a','#fde9dc',LESSONS5,['Tam giác','Hình thang','Hình tròn','Lắp ghép','Luyện tập chung'],
     'Ba hình mới cần nhớ: tam giác, hình thang, hình tròn.','Mỗi hình có một công thức. Em chỉ cần xác định đúng đáy, chiều cao hoặc bán kính rồi thay số. Nhớ đổi các số đo về cùng một đơn vị.','Theo sách Toán 5, tập một (Kết nối tri thức với cuộc sống), Chủ đề 5')
def cd6_sheet():
    return gen_sheet(6,'ÔN TẬP HỌC KÌ 1','Sáu bài học từ Bài 30 đến Bài 35 · Toán 5, tập một','#c2185b','#fce4ec',LESSONS6,['Số thập phân','Phép tính','Hình phẳng','Chu vi, diện tích','Đo lường','Ôn tập chung'],
     'Nhìn lại toàn bộ kiến thức học kì 1.','Số thập phân, các phép tính, hình phẳng, đo lường, phân số. Làm xong sáu đề này là em đã sẵn sàng cho bài kiểm tra cuối kì.','Theo sách Toán 5, tập một (Kết nối tri thức với cuộc sống), Chủ đề 6')
