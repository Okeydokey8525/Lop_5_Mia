from g5lib import *
Q=[]
# ===== TRUNG BÌNH =====
Q.append(mc('tb',25,'Hình tam giác có một góc vuông gọi là:',['hình tam giác nhọn','hình tam giác vuông','hình tam giác tù','hình tam giác đều'],1,
 'Tam giác có 3 góc nhọn là tam giác nhọn; có một góc vuông là tam giác vuông; có một góc tù là tam giác tù; có 3 cạnh bằng nhau là tam giác đều.'))
Q.append(mc('tb',25,'Hình tam giác đều có 3 góc bằng nhau. Mỗi góc của tam giác đều bằng:',['30°','45°','60°','90°'],2,
 'Tam giác đều có 3 cạnh bằng nhau và 3 góc bằng nhau, mỗi góc bằng 60°.'))
a,h=D(8),D(5)
Q.append(fill('tb',25,'Tính diện tích hình tam giác trong hình.',[B('Diện tích là',tri(a,h),'cm²')],
 f'Diện tích hình tam giác bằng đáy nhân chiều cao rồi chia 2: {n(a)} × {n(h)} : 2 = {n(tri(a,h))} (cm²).',fig=fig_tri('acute','8 cm','5 cm','Hình tam giác')))
Q.append(mc('tb',26,'Hình thang có:',['một cặp cạnh đối song song','hai cặp cạnh đối song song','bốn góc vuông','bốn cạnh bằng nhau'],0,
 'Hình thang có một cặp cạnh đối diện song song, hai cạnh đó gọi là hai cạnh đáy.'))
a,b,h=D(9),D(5),D(4)
Q.append(fill('tb',26,'Tính diện tích hình thang trong hình.',[B('Diện tích là',trap(a,b,h),'cm²')],
 f'Diện tích hình thang bằng tổng hai đáy nhân chiều cao rồi chia 2: ({n(a)} + {n(b)}) × {n(h)} : 2 = {n(trap(a,b,h))} (cm²).',fig=fig_trap('9 cm','5 cm','4 cm','Hình thang')))
r=D('4.5')
Q.append(mc('tb',27,f'Hình tròn có bán kính {n(r)} cm thì đường kính là:',['2,25 cm',n(r*2)+' cm','4,5 cm','18 cm'],1,
 f'Đường kính gấp 2 lần bán kính: {n(r)} × 2 = {n(r*2)} (cm).'))
dd,r2=D(6),D(5)
Q.append(fill('tb',27,'Tính chu vi hình tròn.',[B('Đường kính 6 cm thì chu vi là',circ_d(dd),'cm'),B('Bán kính 5 cm thì chu vi là',circ_r(r2),'cm')],
 f'Chu vi = 3,14 × đường kính: 3,14 × {n(dd)} = {n(circ_d(dd))} cm. Chu vi = 3,14 × bán kính × 2: 3,14 × {n(r2)} × 2 = {n(circ_r(r2))} cm.'))
r=D(3)
Q.append(mc('tb',27,f'Diện tích hình tròn có bán kính {n(r)} dm là:',['18,84 dm²','9,42 dm²',n(disc(r))+' dm²','56,52 dm²'],2,
 f'Diện tích hình tròn = 3,14 × bán kính × bán kính: 3,14 × {n(r)} × {n(r)} = {n(disc(r))} (dm²).'))
Q.append(tf('tb',27,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Diện tích hình tam giác bằng đáy nhân chiều cao rồi chia 2.',True),('Hình thang có hai cạnh đáy song song với nhau.',True),('Đường kính dài gấp đôi bán kính.',True),('Chu vi hình tròn bằng 3,14 nhân với bán kính.',False)],
 'a), b), c) đúng. d) Sai: chu vi hình tròn bằng 3,14 nhân với đường kính, hoặc 3,14 nhân với bán kính rồi nhân 2.'))
t=[(D(10),D(5),'dm'),(D(4),D(4),'m'),(D(20),D(10),'cm')]
Q.append(fill('tb',25,'Tính diện tích các hình tam giác.',[B(f'Đáy {n(a)} {u}, cao {n(h)} {u}:',tri(a,h),u+'²') for a,h,u in t],
 '; '.join(f'{n(a)} × {n(h)} : 2 = {n(tri(a,h))} {u}²' for a,h,u in t)+'.'))
# ===== KHÁ =====
a,h=D(6),D(6)
a2,h2=D('7.5'),D(4)
Q.append(fill('kha',25,'Tấm kính hình tam giác vuông có hai cạnh góc vuông là đáy và chiều cao.',[B('Tấm kính có hai cạnh góc vuông 6 m và 6 m, diện tích',tri(a,h),'m²'),B('Tấm kính khác có hai cạnh góc vuông 7,5 dm và 4 dm, diện tích',tri(a2,h2),'dm²')],
 f'Tam giác vuông có thể lấy hai cạnh góc vuông làm đáy và chiều cao. 6 × 6 : 2 = {n(tri(a,h))} m². 7,5 × 4 : 2 = {n(tri(a2,h2))} dm².'))
s,a=D(36),D(9); hh=s*2/a
s2,hh2=D(48),D(6); aa=s2*2/hh2
Q.append(fill('kha',25,'Tìm số chưa biết của hình tam giác.',[B('Diện tích 36 cm², đáy 9 cm, chiều cao là',hh,'cm'),B('Diện tích 48 m², chiều cao 6 m, đáy là',aa,'m')],
 f'Chiều cao = diện tích × 2 : đáy = 36 × 2 : 9 = {n(hh)} cm. Đáy = diện tích × 2 : chiều cao = 48 × 2 : 6 = {n(aa)} m.'))
a,b,h=D(120),D(80),D(50); s=trap(a,b,h)
Q.append(mc('kha',26,'Thửa ruộng hình thang có kích thước như hình. Diện tích thửa ruộng là:',['10 000 m²','5 000 m²','2 500 m²','12 000 m²'],1,
 f'({n(a)} + {n(b)}) × {n(h)} : 2 = {n(s)} (m²).',fig=fig_trap('120 m','80 m','50 m','Thửa ruộng hình thang')))
s,a,b=D(84),D(14),D(10); hh=s*2/(a+b)
Q.append(fill('kha',26,'Hình thang có diện tích 84 cm², đáy lớn 14 cm, đáy bé 10 cm.',[B('Chiều cao hình thang là',hh,'cm')],
 f'Chiều cao = diện tích × 2 : tổng hai đáy = 84 × 2 : (14 + 10) = 168 : 24 = {n(hh)} (cm).'))
dd=D('0.5'); c=circ_d(dd)
Q.append(fill('kha',27,'Bánh xe đạp của bạn Nam có đường kính 0,5 m.',[B('Chu vi bánh xe là',c,'m'),B('Bánh xe lăn 20 vòng trên đường đi được',c*20,'m')],
 f'Chu vi bánh xe: 3,14 × {n(dd)} = {n(c)} m. Lăn 20 vòng đi được: {n(c)} × 20 = {n(c*20)} m.'))
dd=D(10); r=dd/2
Q.append(mc('kha',27,'Diện tích hình tròn có đường kính 10 cm là:',['314 cm²','78,5 cm²','31,4 cm²','157 cm²'],1,
 f'Bán kính = 10 : 2 = 5 cm. Diện tích = 3,14 × 5 × 5 = {n(disc(r))} (cm²).'))
it=[('Hình tam giác: đáy 10 cm, cao 6 cm',tri(10,6)),('Hình thang: đáy 6 cm và 4 cm, cao 5 cm',trap(6,4,5)),('Hình tròn: bán kính 3 cm',disc(3)),('Hình chữ nhật: dài 8 cm, rộng 4 cm',D(32))]
it.sort(key=lambda t:t[1])
Q.append(order('kha',27,'Tính diện tích mỗi hình rồi sắp xếp theo thứ tự diện tích từ bé đến lớn.',[t for t,_ in it],'<',
 'Diện tích: '+'; '.join(f'{t.split(":")[0]} = {n(v)} cm²' for t,v in it)+'.'))
x1,y1=circ_d(4),D(12); x2,y2=tri(8,5),D(20); x3,y3=trap(4,6,3),D(16)
Q.append(fill('kha',27,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL('Chu vi hình tròn đường kính 4 cm',cmp(x1,y1),'12 cm'),SEL('Diện tích tam giác đáy 8 cm, cao 5 cm',cmp(x2,y2),'20 cm²'),SEL('Diện tích hình thang đáy 4 cm và 6 cm, cao 3 cm',cmp(x3,y3),'16 cm²')],
 f'Chu vi: 3,14 × 4 = {n(x1)} cm, {cmp(x1,y1)} 12. Tam giác: 8 × 5 : 2 = {n(x2)} cm², {cmp(x2,y2)} 20. Hình thang: (4 + 6) × 3 : 2 = {n(x3)} cm², {cmp(x3,y3)} 16.'))
# ===== GIỎI =====
a,b,h=D(24),D(16),D(12); s=trap(a,b,h); kg=D('1.5')
Q.append(fill('gioi',26,'Mảnh vườn hình thang như hình. Mỗi mét vuông thu hoạch được 1,5 kg rau.',[B('Diện tích mảnh vườn là',s,'m²'),B('Cả vườn thu hoạch được',s*kg,'kg rau')],
 f'Diện tích: ({n(a)} + {n(b)}) × {n(h)} : 2 = {n(s)} m². Số rau: {n(s)} × 1,5 = {n(s*kg)} kg.',fig=fig_trap('24 m','16 m','12 m','Mảnh vườn hình thang')))
r=D(5); c=circ_r(r); s=disc(r)
Q.append(fill('gioi',27,'Ao cá hình tròn có bán kính 5 m. Cứ mỗi mét vuông mặt ao thả 2 con cá giống.',[B('Chu vi bờ ao là',c,'m'),B('Diện tích mặt ao là',s,'m²'),B('Số cá giống cần thả là',s*2,'con')],
 f'Chu vi: 3,14 × 5 × 2 = {n(c)} m. Diện tích: 3,14 × 5 × 5 = {n(s)} m². Số cá giống: {n(s)} × 2 = {n(s*2)} con.',fig=fig_circ('r','5 m','Ao cá')))
a,h=D(8),D(3); L,hw=D(8),D(4); s1=tri(a,h); s2=L*hw
Q.append(fill('gioi',29,'Hình ngôi nhà gồm phần mái hình tam giác và thân nhà hình chữ nhật như hình.',[B('Diện tích phần mái là',s1,'m²'),B('Diện tích phần thân nhà là',s2,'m²'),B('Diện tích cả hình là',s1+s2,'m²')],
 f'Mái: 8 × 3 : 2 = {n(s1)} m². Thân nhà: 8 × 4 = {n(s2)} m². Cả hình: {n(s1)} + {n(s2)} = {n(s1+s2)} m².',fig=fig_house('8 m','4 m','3 m','Hình ngôi nhà')))
b=D(30); a=b*2; h=b; s=trap(a,b,h)
Q.append(mc('gioi',26,'Thửa ruộng hình thang có đáy bé 30 m, đáy lớn gấp 2 lần đáy bé, chiều cao bằng đáy bé. Diện tích thửa ruộng là:',['900 m²','1 350 m²','1 800 m²','2 700 m²'],1,
 f'Đáy lớn: 30 × 2 = {n(a)} m. Chiều cao: {n(h)} m. Diện tích: ({n(a)} + {n(b)}) × {n(h)} : 2 = {n(s)} (m²).'))
dd=D(8); r=dd/2; s=disc(r); p=D(45000)
Q.append(fill('gioi',27,'Bể bơi trẻ em hình tròn có đường kính 8 m. Người ta sơn đáy bể, giá sơn 45 000 đồng một mét vuông.',[B('Diện tích đáy bể là',s,'m²'),B('Tiền sơn đáy bể là',s*p,'đồng')],
 f'Bán kính: 8 : 2 = 4 m. Diện tích đáy: 3,14 × 4 × 4 = {n(s)} m². Tiền sơn: {n(s)} × 45 000 = {n(s*p)} đồng.',fig=fig_circ('d','8 m','Bể bơi trẻ em')))
Q.append(tf('gioi',29,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Tam giác đáy 6 cm, cao 4 cm và tam giác đáy 4 cm, cao 6 cm có diện tích bằng nhau.',True),('Hình tròn bán kính 2 cm có chu vi (cm) bằng diện tích (cm²) về số đo.',True),('Bán kính gấp đôi thì diện tích hình tròn cũng chỉ gấp đôi.',False),('Hình thang có hai đáy 5 cm và 7 cm, chiều cao 4 cm có diện tích 24 cm².',True)],
 f'a) Đúng: cả hai đều bằng 6 × 4 : 2 = 12 cm². b) Đúng: chu vi 3,14 × 2 × 2 = {n(circ_r(2))}, diện tích 3,14 × 2 × 2 = {n(disc(2))}. c) Sai: bán kính gấp đôi thì diện tích gấp 4 lần. d) Đúng: (5 + 7) × 4 : 2 = {n(trap(5,7,4))} cm².'))
write5(1,Q)
