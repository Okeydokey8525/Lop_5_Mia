from g5lib import *
Q=[]
Q.append(mc('tb',25,'Công thức S = a × h : 2 dùng để tính diện tích của hình:',['hình tam giác','hình thang','hình tròn','hình chữ nhật'],0,
 'Diện tích hình tam giác bằng độ dài đáy nhân chiều cao rồi chia 2: S = a × h : 2.'))
a,b,h=D(7),D(3),D(4)
Q.append(mc('tb',26,'Hình thang có hai đáy 7 cm và 3 cm, chiều cao 4 cm. Diện tích hình thang là:',['40 cm²',n(trap(a,b,h))+' cm²','28 cm²','10 cm²'],1,
 f'({n(a)} + {n(b)}) × {n(h)} : 2 = {n(trap(a,b,h))} (cm²).'))
Q.append(fill('tb',26,'Tính diện tích.',[B('Tam giác đáy 12 m, cao 5 m:',tri(12,5),'m²'),B('Hình thang đáy 8 dm và 4 dm, cao 3 dm:',trap(8,4,3),'dm²')],
 f'12 × 5 : 2 = {n(tri(12,5))} m². (8 + 4) × 3 : 2 = {n(trap(8,4,3))} dm².'))
r=D(7)
Q.append(fill('tb',27,'Hình tròn có bán kính 7 cm.',[B('Chu vi hình tròn là',circ_r(r),'cm'),B('Diện tích hình tròn là',disc(r),'cm²')],
 f'Chu vi: 3,14 × 7 × 2 = {n(circ_r(r))} cm. Diện tích: 3,14 × 7 × 7 = {n(disc(r))} cm².'))
Q.append(mc('tb',25,'Tấm kính hình tam giác vuông có hai cạnh góc vuông dài 6 m và 6 m. Diện tích tấm kính là:',['36 m²',n(tri(6,6))+' m²','12 m²','18 m'],1,
 f'6 × 6 : 2 = {n(tri(6,6))} (m²).'))
L,Wd=D(15),D(8)
Q.append(fill('tb',29,'Vườn rau hình chữ nhật dài 15 m, rộng 8 m.',[B('Diện tích vườn rau là',L*Wd,'m²'),B('Chu vi vườn rau là',(L+Wd)*2,'m')],
 f'Diện tích: 15 × 8 = {n(L*Wd)} m². Chu vi: (15 + 8) × 2 = {n((L+Wd)*2)} m.'))
Q.append(tf('tb',29,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Hình thang có hai cạnh đáy song song.',True),('Tam giác đều có ba góc bằng nhau và mỗi góc bằng 60°.',True),('Đường kính bằng 3,14 nhân với bán kính.',False),('Diện tích hình tròn bằng 3,14 × r × r.',True)],
 'a), b), d) đúng. c) Sai: đường kính bằng bán kính nhân 2.'))
x1,y1=tri(10,4),trap(4,6,4); x2,y2=circ_d(6),disc(3); x3,y3=tri(7,6),trap(5,3,5)
Q.append(fill('tb',29,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL('Diện tích tam giác đáy 10 cm, cao 4 cm',cmp(x1,y1),'diện tích hình thang đáy 4 cm và 6 cm, cao 4 cm'),SEL('Chu vi hình tròn đường kính 6 cm',cmp(x2,y2),'diện tích hình tròn bán kính 3 cm'),SEL('Diện tích tam giác đáy 7 cm, cao 6 cm',cmp(x3,y3),'diện tích hình thang đáy 5 cm và 3 cm, cao 5 cm')],
 f'10 × 4 : 2 = {n(x1)} và (4 + 6) × 4 : 2 = {n(y1)}, {cmp(x1,y1)}. 3,14 × 6 = {n(x2)} và 3,14 × 3 × 3 = {n(y2)}, {cmp(x2,y2)}. 7 × 6 : 2 = {n(x3)} và (5 + 3) × 5 : 2 = {n(y3)}, {cmp(x3,y3)}.'))
r=D(5)
Q.append(mc('tb',27,'Vườn hoa hình tròn có bán kính 5 m. Chu vi vườn hoa là:',['15,7 m',n(circ_r(r))+' m','78,5 m','62,8 m'],1,
 f'3,14 × 5 × 2 = {n(circ_r(r))} (m).'))
t=[(D(4),D(6)),(D(10),D(5)),(D(7),D(8))]
Q.append(fill('tb',25,'Hoàn thành bảng diện tích hình tam giác (đơn vị: cm).',[B(f'Đáy {n(a)} cm, cao {n(h)} cm:',tri(a,h),'cm²') for a,h in t],
 '; '.join(f'{n(a)} × {n(h)} : 2 = {n(tri(a,h))}' for a,h in t)+'.'))
# KHÁ
a,b,h=D(30),D(20),D(16); s=trap(a,b,h)
Q.append(fill('kha',26,'Vườn hình thang có hai đáy 30 m và 20 m, chiều cao 16 m. Cứ 2 m² trồng được một cây.',[B('Diện tích vườn là',s,'m²'),B('Số cây trồng được là',s/2,'cây')],
 f'Diện tích: (30 + 20) × 16 : 2 = {n(s)} m². Số cây: {n(s)} : 2 = {n(s/2)} cây.'))
r=D(10); c=circ_r(r); s=disc(r)
Q.append(fill('kha',27,'Sân chơi hình tròn có bán kính 10 m. Người ta chia đều sân thành 4 khu vực bằng nhau.',[B('Chu vi sân chơi là',c,'m'),B('Diện tích sân chơi là',s,'m²'),B('Diện tích mỗi khu vực là',s/4,'m²')],
 f'Chu vi: 3,14 × 10 × 2 = {n(c)} m. Diện tích: 3,14 × 10 × 10 = {n(s)} m². Mỗi khu: {n(s)} : 4 = {n(s/4)} m².'))
s,h=D(60),D(8); a=s*2/h
Q.append(mc('kha',25,'Hình tam giác có diện tích 60 dm² và chiều cao 8 dm. Độ dài đáy là:',['7,5 dm','15 dm','30 dm','480 dm'],1,
 f'Đáy = diện tích × 2 : chiều cao = 60 × 2 : 8 = {n(a)} (dm).'))
a,h,L,hw=D(16),D(3),D(16),D(6); s1=tri(a,h); s2=L*hw
Q.append(fill('kha',29,'Hình ngôi nhà gồm mái hình tam giác và thân nhà hình chữ nhật như hình.',[B('Diện tích mái là',s1,'m²'),B('Diện tích cả hình là',s1+s2,'m²')],
 f'Mái: 16 × 3 : 2 = {n(s1)} m². Thân nhà: 16 × 6 = {n(s2)} m². Cả hình: {n(s1)} + {n(s2)} = {n(s1+s2)} m².',fig=fig_house('16 m','6 m','3 m','Hình ngôi nhà')))
dd=D(6); r=dd/2
Q.append(mc('kha',27,'Diện tích hình tròn có đường kính 6 dm là:',['18,84 dm²',n(disc(r))+' dm²','113,04 dm²','9,42 dm²'],1,
 f'Bán kính: 6 : 2 = 3 dm. Diện tích: 3,14 × 3 × 3 = {n(disc(r))} (dm²).'))
dd=D('0.4'); c=circ_d(dd)
Q.append(fill('kha',27,'Bánh xe của chiếc xe đẩy có đường kính 0,4 m.',[B('Chu vi bánh xe là',c,'m'),B('Bánh xe lăn 25 vòng thì xe đi được',c*25,'m')],
 f'Chu vi: 3,14 × 0,4 = {n(c)} m. Đi được: {n(c)} × 25 = {n(c*25)} m.'))
it=[('Hình tam giác đáy 9 cm, cao 4 cm',tri(9,4)),('Hình thang đáy 6 cm và 8 cm, cao 3 cm',trap(6,8,3)),('Hình tròn bán kính 2 cm',disc(2)),('Hình chữ nhật 4 cm × 5 cm',D(20))]
it.sort(key=lambda t:t[1])
Q.append(order('kha',29,'Tính diện tích mỗi hình rồi sắp xếp theo thứ tự diện tích từ bé đến lớn.',[t for t,_ in it],'<',
 'Diện tích: '+'; '.join(f'{t} → {n(v)} cm²' for t,v in it)+'.'))
Q.append(tf('kha',29,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Hình thang có diện tích 40 cm², chiều cao 5 cm thì tổng hai đáy là 16 cm.',True),('Hình tròn đường kính 10 cm có diện tích 78,5 cm².',True),('Tam giác có đáy 8 cm và diện tích 20 cm² thì chiều cao là 5 cm.',True),('Chu vi hình tròn gấp đôi thì diện tích hình tròn cũng chỉ gấp đôi.',False)],
 'a) Đúng: 40 × 2 : 5 = 16. b) Đúng: bán kính 5 cm, 3,14 × 5 × 5 = 78,5. c) Đúng: 20 × 2 : 8 = 5. d) Sai: chu vi gấp đôi thì bán kính gấp đôi, diện tích gấp 4 lần.'))
# GIỎI
L,Wd,r=D(36),D(20),D(5); s=L*Wd; sa=disc(r); sr=s-sa; kg=D(2)
Q.append(fill('gioi',29,'Khu vườn hình chữ nhật dài 36 m, rộng 20 m có một ao tròn bán kính 5 m. Phần đất còn lại trồng rau, mỗi mét vuông thu hoạch 2 kg rau.',[B('Diện tích ao là',sa,'m²'),B('Diện tích đất trồng rau là',sr,'m²'),B('Số rau thu hoạch được là',sr*kg,'kg')],
 f'Ao: 3,14 × 5 × 5 = {n(sa)} m². Đất trồng rau: 36 × 20 − {n(sa)} = {n(sr)} m². Rau: {n(sr)} × 2 = {n(sr*kg)} kg.'))
a,b,h=D(45),D(35),D(20); s=trap(a,b,h); p=D(12000)
Q.append(fill('gioi',26,'Mảnh đất hình thang có đáy 45 m và 35 m, chiều cao 20 m được cho thuê với giá 12 000 đồng một mét vuông mỗi tháng.',[B('Diện tích mảnh đất là',s,'m²'),B('Tiền thuê một tháng là',s*p,'đồng'),B('Tiền thuê trong 12 tháng là',s*p*12,'đồng')],
 f'Diện tích: (45 + 35) × 20 : 2 = {n(s)} m². Một tháng: {n(s)} × 12 000 = {n(s*p)} đồng. 12 tháng: {n(s*p)} × 12 = {n(s*p*12)} đồng.'))
dd=D(6); r=dd/2; c=circ_d(dd); s=disc(r); pd=D(40000); pt=D(150000)
Q.append(fill('gioi',27,'Sân khấu hình tròn có đường kính 6 m. Viền đèn LED chạy quanh mép sân khấu, giá 40 000 đồng một mét. Thảm trải kín mặt sân khấu, giá 150 000 đồng một mét vuông.',[B('Chu vi sân khấu là',c,'m'),B('Tiền mua đèn viền là',c*pd,'đồng'),B('Diện tích sân khấu là',s,'m²'),B('Tiền mua thảm là',s*pt,'đồng')],
 f'Chu vi: 3,14 × 6 = {n(c)} m. Tiền đèn: {n(c)} × 40 000 = {n(c*pd)} đồng. Bán kính 3 m, diện tích: 3,14 × 3 × 3 = {n(s)} m². Tiền thảm: {n(s)} × 150 000 = {n(s*pt)} đồng.'))
s,h=D(96),D(8); tong=s*2/h; b=tong/3; a=b*2
Q.append(mc('gioi',26,'Hình thang có chiều cao 8 cm, diện tích 96 cm², đáy lớn gấp 2 lần đáy bé. Độ dài đáy bé là:',['8 cm','12 cm','16 cm','6 cm'],0,
 f'Tổng hai đáy: 96 × 2 : 8 = {n(tong)} cm. Đáy lớn gấp 2 lần đáy bé nên tổng bằng 3 lần đáy bé: đáy bé = {n(tong)} : 3 = {n(b)} cm, đáy lớn = {n(a)} cm.'))
a,h=D('3.6'),D('2.5'); s=tri(a,h); p=D(65000)
Q.append(fill('gioi',25,'Biển quảng cáo hình tam giác có đáy 3,6 m và chiều cao 2,5 m. Sơn biển giá 65 000 đồng một mét vuông.',[B('Diện tích một biển là',s,'m²'),B('Tiền sơn một biển là',s*p,'đồng'),B('Tiền sơn hai biển là',s*p*2,'đồng')],
 f'Diện tích: 3,6 × 2,5 : 2 = {n(s)} m². Một biển: {n(s)} × 65 000 = {n(s*p)} đồng. Hai biển: {n(s*p)} × 2 = {n(s*p*2)} đồng.'))
Q.append(tf('gioi',29,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Tam giác đáy 12 cm, cao 5 cm có diện tích bằng nửa hình chữ nhật 12 cm × 5 cm.',True),('Hình tròn bán kính 5 cm có chu vi 31,4 cm và diện tích 78,5 cm².',True),('Hình thang đáy 8 cm và 12 cm, cao 5 cm có diện tích 50 cm².',True),('Giữ nguyên đáy, chiều cao tam giác gấp 3 lần thì diện tích gấp 6 lần.',False)],
 f'a) Đúng: 12 × 5 : 2 = {n(tri(12,5))} = 60 : 2. b) Đúng: C = {n(circ_r(5))}, S = {n(disc(5))}. c) Đúng: (8 + 12) × 5 : 2 = {n(trap(8,12,5))}. d) Sai: chiều cao gấp 3 lần thì diện tích cũng chỉ gấp 3 lần.'))
write5(6,Q)
