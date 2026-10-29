from g5lib import *
Q=[]
Q.append(mc('tb',26,'Hình thang ABCD có AB song song với DC. Hai cạnh đáy của hình thang là:',['AB và DC','AD và BC','AB và AD','DC và BC'],0,
 'Hai cạnh đối diện song song của hình thang gọi là hai cạnh đáy: AB và DC. Hai cạnh còn lại AD và BC là hai cạnh bên.'))
Q.append(mc('tb',26,'Đường cao của hình thang là đoạn thẳng:',['nối hai đỉnh đối diện','vuông góc với hai cạnh đáy','song song với cạnh bên','chia đôi hình thang'],1,
 'Đường cao của hình thang vuông góc với hai cạnh đáy. Độ dài đường cao gọi là chiều cao.'))
a,b,h=D(10),D(6),D(5)
Q.append(fill('tb',26,'Tính diện tích hình thang trong hình.',[B('Diện tích là',trap(a,b,h),'cm²')],
 f'({n(a)} + {n(b)}) × {n(h)} : 2 = {n(trap(a,b,h))} (cm²).',fig=fig_trap('10 cm','6 cm','5 cm','Hình thang')))
a,b,h=D(18),D(12),D(7)
Q.append(fill('tb',26,'Hình thang có đáy lớn 18 m, đáy bé 12 m và chiều cao 7 m.',[B('Diện tích hình thang là',trap(a,b,h),'m²')],
 f'({n(a)} + {n(b)}) × {n(h)} : 2 = {n(a+b)} × {n(h)} : 2 = {n(trap(a,b,h))} (m²).'))
a,b,h=D(8),D(4),D(5)
Q.append(mc('tb',26,'Hình thang có hai đáy 8 dm và 4 dm, chiều cao 5 dm. Diện tích hình thang là:',['60 dm²',n(trap(a,b,h))+' dm²','17 dm²','30 dm'],1,
 f'({n(a)} + {n(b)}) × {n(h)} : 2 = {n(trap(a,b,h))} (dm²).'))
Q.append(tf('tb',26,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Hình thang có hai cạnh đáy song song với nhau.',True),('Diện tích hình thang bằng tổng hai đáy nhân chiều cao rồi chia 2.',True),('Hai cạnh bên của hình thang luôn song song với nhau.',False),('Chiều cao của hình thang là độ dài đường cao.',True)],
 'a), b), d) đúng. c) Sai: chỉ hai cạnh đáy song song với nhau, hai cạnh bên thường không song song.'))
t=[(D(6),D(4),D(3),'cm'),(D(12),D(8),D(5),'dm'),(D('2.5'),D('1.5'),D(3),'m')]
Q.append(fill('tb',26,'Tính diện tích hình thang.',[B(f'Đáy {n(a)} {u} và {n(b)} {u}, cao {n(h)} {u}:',trap(a,b,h),u+'²') for a,b,h,u in t],
 '; '.join(f'({n(a)} + {n(b)}) × {n(h)} : 2 = {n(trap(a,b,h))} {u}²' for a,b,h,u in t)+'.'))
a,b,h=D(15),D(9),D(6)
Q.append(mc('tb',26,'Diện tích hình thang có đáy lớn 15 cm, đáy bé 9 cm và chiều cao 6 cm là:',['144 cm²',n(trap(a,b,h))+' cm²','30 cm²','90 cm²'],1,
 f'({n(a)} + {n(b)}) × {n(h)} : 2 = {n(trap(a,b,h))} (cm²).'))
a,b,h=D(25),D(15),D(12)
Q.append(fill('tb',26,'Thửa ruộng hình thang có kích thước như hình.',[B('Diện tích thửa ruộng là',trap(a,b,h),'m²')],
 f'({n(a)} + {n(b)}) × {n(h)} : 2 = {n(trap(a,b,h))} (m²).',fig=fig_trap('25 m','15 m','12 m','Thửa ruộng')))
x1,y1=trap(6,4,5),D(25); x2,y2=trap(10,4,3),D(20); x3,y3=trap(9,5,2),D(15)
Q.append(fill('tb',26,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL('Diện tích hình thang đáy 6 cm và 4 cm, cao 5 cm',cmp(x1,y1),'25 cm²'),SEL('Diện tích hình thang đáy 10 cm và 4 cm, cao 3 cm',cmp(x2,y2),'20 cm²'),SEL('Diện tích hình thang đáy 9 cm và 5 cm, cao 2 cm',cmp(x3,y3),'15 cm²')],
 f'(6 + 4) × 5 : 2 = {n(x1)}, {cmp(x1,y1)} 25. (10 + 4) × 3 : 2 = {n(x2)}, {cmp(x2,y2)} 20. (9 + 5) × 2 : 2 = {n(x3)}, {cmp(x3,y3)} 15.'))
# KHÁ
s,a,b=D(90),D(13),D(5); h=s*2/(a+b); s2,h2=D(60),D(8); tong=s2*2/h2
Q.append(fill('kha',26,'Tìm số chưa biết của hình thang.',[B('Diện tích 90 m², hai đáy 13 m và 5 m, chiều cao là',h,'m'),B('Diện tích 60 m², chiều cao 8 m, tổng hai đáy là',tong,'m')],
 f'Chiều cao = diện tích × 2 : tổng hai đáy = 90 × 2 : (13 + 5) = {n(h)} m. Tổng hai đáy = 60 × 2 : 8 = {n(tong)} m.'))
a,b,h=D(60),D(40),D(25); s=trap(a,b,h); r=s/100*50
Q.append(fill('kha',26,'Ruộng bậc thang hình thang có đáy 60 m và 40 m, chiều cao 25 m. Cứ 100 m² thu được 50 kg lúa.',[B('Diện tích thửa ruộng là',s,'m²'),B('Số lúa thu được là',r,'kg')],
 f'Diện tích: ({n(a)} + {n(b)}) × {n(h)} : 2 = {n(s)} m². Số lúa: {n(s)} : 100 × 50 = {n(r)} kg.'))
b=D(6); a=b*3; h=D(5)
Q.append(mc('kha',26,'Hình thang có đáy bé 6 dm, đáy lớn gấp 3 lần đáy bé, chiều cao 5 dm. Diện tích hình thang là:',['60 dm²','120 dm²','90 dm²','30 dm²'],0,
 f'Đáy lớn: 6 × 3 = {n(a)} dm. Diện tích: ({n(a)} + {n(b)}) × {n(h)} : 2 = {n(trap(a,b,h))} (dm²).'))
a,b,h=D(12),D(8),D(6); s1=b*h; s2=(a-b)*h/2
Q.append(fill('kha',26,'Hình thang vuông có đáy lớn 12 cm, đáy bé 8 cm, chiều cao 6 cm. Cắt hình thang thành một hình chữ nhật (đáy bé × chiều cao) và một hình tam giác vuông.',[B('Diện tích hình chữ nhật là',s1,'cm²'),B('Diện tích hình tam giác vuông là',s2,'cm²'),B('Diện tích hình thang là',s1+s2,'cm²')],
 f'Hình chữ nhật: 8 × 6 = {n(s1)} cm². Tam giác vuông có đáy 12 − 8 = 4 cm và cao 6 cm: 4 × 6 : 2 = {n(s2)} cm². Cả hình thang: {n(s1)} + {n(s2)} = {n(s1+s2)} cm². Kiểm tra bằng công thức: (12 + 8) × 6 : 2 = {n(trap(a,b,h))} cm².'))
s,tong=D(96),D(24); h=s*2/tong
Q.append(mc('kha',26,'Hình thang có diện tích 96 m², tổng hai đáy là 24 m. Chiều cao của hình thang là:',['4 m','8 m','16 m','2,4 m'],1,
 f'Chiều cao = diện tích × 2 : tổng hai đáy = 96 × 2 : 24 = {n(h)} (m).'))
a,b,h=D(9),D(4),D('3.6'); s=trap(a,b,h); L=D(100)
Q.append(fill('kha',26,'Mặt cắt ngang của một con đê là hình thang có đáy lớn 9 m, đáy bé 4 m, chiều cao 3,6 m. Con đê dài 100 m.',[B('Diện tích mặt cắt ngang là',s,'m²'),B('Thể tích đất đắp con đê là',s*L,'m³')],
 f'Diện tích mặt cắt: (9 + 4) × 3,6 : 2 = {n(s)} m². Thể tích: {n(s)} × 100 = {n(s*L)} m³.'))
it=[('Đáy 10 cm và 6 cm, cao 4 cm',trap(10,6,4)),('Đáy 8 cm và 4 cm, cao 5 cm',trap(8,4,5)),('Đáy 12 cm và 5 cm, cao 3 cm',trap(12,5,3)),('Đáy 9 cm và 9 cm, cao 4 cm',trap(9,9,4))]
it.sort(key=lambda t:t[1])
Q.append(order('kha',26,'Tính diện tích mỗi hình thang rồi sắp xếp theo thứ tự diện tích từ bé đến lớn.',[t for t,_ in it],'<',
 'Diện tích: '+'; '.join(f'{t} → {n(v)} cm²' for t,v in it)+'.'))
Q.append(tf('kha',26,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Hai hình thang có cùng hai đáy và cùng chiều cao thì có diện tích bằng nhau.',True),('Giữ nguyên đáy lớn và chiều cao, tăng đáy bé thì diện tích giảm.',False),('Giữ nguyên hai đáy, chiều cao gấp đôi thì diện tích gấp đôi.',True),('Hình thang đáy 6 cm và 4 cm, cao 5 cm có diện tích 25 cm².',True)],
 'a) Đúng vì công thức chỉ phụ thuộc hai đáy và chiều cao. b) Sai: đáy bé tăng thì tổng hai đáy tăng nên diện tích tăng. c) Đúng. d) Đúng: (6 + 4) × 5 : 2 = 25.'))
# GIỎI
a,b,h=D(48),D(32),D(25); s=trap(a,b,h); kg=D('0.7'); p=D(12000)
Q.append(fill('gioi',26,'Thửa ruộng bậc thang hình thang có đáy lớn 48 m, đáy bé 32 m, chiều cao 25 m. Mỗi mét vuông thu 0,7 kg lúa, mỗi ki-lô-gam lúa bán được 12 000 đồng.',[B('Diện tích thửa ruộng là',s,'m²'),B('Số lúa thu được là',s*kg,'kg'),B('Số tiền bán lúa là',s*kg*p,'đồng')],
 f'Diện tích: (48 + 32) × 25 : 2 = {n(s)} m². Lúa: {n(s)} × 0,7 = {n(s*kg)} kg. Tiền: {n(s*kg)} × 12 000 = {n(s*kg*p)} đồng.',fig=fig_trap('48 m','32 m','25 m','Thửa ruộng bậc thang')))
a,b,h=D(40),D(24),D(15); s=trap(a,b,h)
Q.append(fill('gioi',26,'Mảnh đất hình thang có đáy 40 m và 24 m, chiều cao 15 m. Người ta chia đều mảnh đất thành 6 luống rau.',[B('Diện tích mảnh đất là',s,'m²'),B('Diện tích mỗi luống rau là',s/6,'m²')],
 f'Diện tích: (40 + 24) × 15 : 2 = {n(s)} m². Mỗi luống: {n(s)} : 6 = {n(s/6)} m².'))
a,b,h,L=D('2.4'),D('1.6'),D('1.5'),D(5); s=trap(a,b,h); v=s*L
Q.append(fill('gioi',26,'Bể nước có mặt cắt ngang hình thang đáy lớn 2,4 m, đáy bé 1,6 m, chiều cao 1,5 m, bể dài 5 m. 1 m³ nước bằng 1 000 lít.',[B('Diện tích mặt cắt ngang là',s,'m²'),B('Thể tích bể là',v,'m³'),B('Bể chứa đầy được',v*1000,'lít nước')],
 f'Diện tích mặt cắt: (2,4 + 1,6) × 1,5 : 2 = {n(s)} m². Thể tích: {n(s)} × 5 = {n(v)} m³. Số lít: {n(v)} × 1 000 = {n(v*1000)} lít.'))
h,s,hieu=D(12),D(180),D(6); tong=s*2/h; a=(tong+hieu)/2
Q.append(mc('gioi',26,'Hình thang có chiều cao 12 m, diện tích 180 m², đáy lớn hơn đáy bé 6 m. Độ dài đáy lớn là:',['12 m','15 m','18 m','24 m'],2,
 f'Tổng hai đáy: 180 × 2 : 12 = {n(tong)} m. Đáy lớn: ({n(tong)} + 6) : 2 = {n(a)} m, đáy bé: {n(a-hieu)} m.'))
a,b,h=D(50),D(30),D(20); s=trap(a,b,h); p=D(15000)
Q.append(fill('gioi',26,'Một mảnh đất hình thang có đáy 50 m và 30 m, chiều cao 20 m được cho thuê, giá 15 000 đồng một mét vuông mỗi tháng.',[B('Diện tích mảnh đất là',s,'m²'),B('Tiền thuê đất một tháng là',s*p,'đồng')],
 f'Diện tích: (50 + 30) × 20 : 2 = {n(s)} m². Tiền thuê một tháng: {n(s)} × 15 000 = {n(s*p)} đồng.'))
Q.append(tf('gioi',29,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Hình thang đáy 5 cm và 7 cm, cao 4 cm có diện tích 24 cm².',True),('Tăng mỗi đáy thêm 2 cm, giữ nguyên chiều cao 4 cm thì diện tích tăng thêm 4 cm².',False),('Giữ nguyên chiều cao, hai đáy cùng gấp đôi thì diện tích gấp đôi.',True),('Hình thang đáy 8 cm và 6 cm, cao 5 cm có diện tích gấp đôi tam giác đáy 7 cm, cao 5 cm.',True)],
 f'a) Đúng: (5 + 7) × 4 : 2 = {n(trap(5,7,4))}. b) Sai: tổng hai đáy tăng 4 cm nên diện tích tăng 4 × 4 : 2 = 8 cm². c) Đúng vì tổng hai đáy gấp đôi. d) Đúng: hình thang {n(trap(8,6,5))} cm² và tam giác {n(tri(7,5))} cm², {n(trap(8,6,5))} = {n(tri(7,5))} × 2.'))
write5(3,Q)
