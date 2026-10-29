from g5lib import *
Q=[]
Q.append(mc('tb',25,'Cánh buồm bên phải trong sách có ba góc đều nhọn. Cánh buồm đó có dạng hình:',['tam giác nhọn','tam giác vuông','tam giác tù','tam giác đều'],0,
 'Tam giác có cả ba góc nhọn gọi là hình tam giác nhọn.'))
Q.append(mc('tb',25,'AH là đường cao ứng với đáy BC của hình tam giác ABC. Khi đó AH và BC tạo thành góc:',['nhọn','vuông','tù','bẹt'],1,
 'Đường cao của hình tam giác vuông góc với cạnh đáy tương ứng, nên AH và BC tạo thành góc vuông.'))
a,h=D(12),D(9)
Q.append(fill('tb',25,'Cánh buồm hình tam giác có kích thước như hình.',[B('Diện tích cánh buồm là',tri(a,h),'dm²')],
 f'{n(a)} × {n(h)} : 2 = {n(tri(a,h))} (dm²).',fig=fig_tri('acute','12 dm','9 dm','Cánh buồm')))
a,h=D('3.6'),D('2.5')
Q.append(fill('tb',25,'Mái hiên có dạng hình tam giác, đáy 3,6 m và chiều cao 2,5 m.',[B('Diện tích mái hiên là',tri(a,h),'m²')],
 f'{n(a)} × {n(h)} : 2 = {n(a*h)} : 2 = {n(tri(a,h))} (m²).'))
a,h=D(14),D(9)
Q.append(mc('tb',25,'Diện tích hình tam giác có độ dài đáy 14 cm và chiều cao 9 cm là:',['126 cm²',n(tri(a,h))+' cm²','23 cm²','63 cm'],1,
 f'{n(a)} × {n(h)} : 2 = {n(tri(a,h))} (cm²). Chú ý đơn vị diện tích là cm², không phải cm.'))
Q.append(tf('tb',25,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Tam giác có một góc tù gọi là tam giác tù.',True),('Tam giác đều có ba cạnh bằng nhau.',True),('Tam giác vuông có hai góc vuông.',False),('Tam giác nhọn có cả ba góc nhọn.',True)],
 'a), b), d) đúng. c) Sai: tam giác vuông chỉ có đúng một góc vuông.'))
t=[(D(6),D(5),'cm'),(D(8),D(3),'dm'),(D('2.4'),D(5),'m')]
Q.append(fill('tb',25,'Tính diện tích hình tam giác.',[B(f'Đáy {n(a)} {u}, cao {n(h)} {u}:',tri(a,h),u+'²') for a,h,u in t],
 '; '.join(f'{n(a)} × {n(h)} : 2 = {n(tri(a,h))} {u}²' for a,h,u in t)+'.'))
a,h=D(5),D(8)
Q.append(mc('tb',25,'Diện tích hình tam giác có đáy 5 m và chiều cao 8 m là:',['40 m²',n(tri(a,h))+' m²','13 m²','20 m'],1,
 f'{n(a)} × {n(h)} : 2 = {n(tri(a,h))} (m²).'))
a,h=D(9),D(12)
Q.append(fill('tb',25,'Tấm kính hình tam giác vuông, hai cạnh góc vuông dài 9 cm và 12 cm.',[B('Diện tích tấm kính là',tri(a,h),'cm²')],
 f'Hai cạnh góc vuông là đáy và chiều cao: 9 × 12 : 2 = {n(tri(a,h))} (cm²).',fig=fig_tri('right','12 cm','9 cm','Tấm kính hình tam giác vuông')))
x1,y1=tri(6,4),tri(8,3); x2,y2=tri(5,6),D(14); x3,y3=tri(10,2),D(12)
Q.append(fill('tb',25,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL('Diện tích tam giác đáy 6 cm, cao 4 cm',cmp(x1,y1),'diện tích tam giác đáy 8 cm, cao 3 cm'),SEL('Diện tích tam giác đáy 5 cm, cao 6 cm',cmp(x2,y2),'14 cm²'),SEL('Diện tích tam giác đáy 10 cm, cao 2 cm',cmp(x3,y3),'12 cm²')],
 f'6 × 4 : 2 = {n(x1)} và 8 × 3 : 2 = {n(y1)}, nên {cmp(x1,y1)}. 5 × 6 : 2 = {n(x2)} {cmp(x2,y2)} 14. 10 × 2 : 2 = {n(x3)} {cmp(x3,y3)} 12.'))
# KHÁ
s,a=D(27),D(9); hh=s*2/a; s2,h2=D(40),D(8); aa=s2*2/h2
Q.append(fill('kha',25,'Tìm số chưa biết của hình tam giác.',[B('Diện tích 27 m², đáy 9 m, chiều cao là',hh,'m'),B('Diện tích 40 dm², chiều cao 8 dm, đáy là',aa,'dm')],
 f'Chiều cao = 27 × 2 : 9 = {n(hh)} m. Đáy = 40 × 2 : 8 = {n(aa)} dm.'))
a,h=D(6),D('2.5'); s=tri(a,h); l=D('0.2')
Q.append(fill('kha',25,'Hai bức tường hồi của một ngôi nhà đều là hình tam giác, đáy 6 m và chiều cao 2,5 m. Mỗi mét vuông tường cần 0,2 lít sơn.',[B('Diện tích một bức tường hồi là',s,'m²'),B('Diện tích hai bức tường hồi là',s*2,'m²'),B('Số lít sơn cần dùng là',s*2*l,'lít')],
 f'Một bức: 6 × 2,5 : 2 = {n(s)} m². Hai bức: {n(s)} × 2 = {n(s*2)} m². Sơn: {n(s*2)} × 0,2 = {n(s*2*l)} lít.'))
Q.append(mc('kha',25,'Tam giác ABC có đáy BC = 12 cm, đường cao AH = 7 cm. M là trung điểm của BC (BM = 6 cm). Diện tích tam giác ABM là:',['84 cm²','42 cm²','21 cm²','10,5 cm²'],2,
 f'Tam giác ABM có đáy BM = 6 cm và cùng chiều cao AH = 7 cm: 6 × 7 : 2 = {n(tri(6,7))} (cm²). Bằng một nửa diện tích tam giác ABC.'))
a,h=D('7.5'),D('4.8')
Q.append(fill('kha',25,'Tam giác MNP có đáy 7,5 cm và chiều cao 4,8 cm.',[B('Diện tích tam giác MNP là',tri(a,h),'cm²'),B('Tam giác có cùng chiều cao nhưng đáy gấp đôi (15 cm) có diện tích',tri(15,h),'cm²')],
 f'7,5 × 4,8 : 2 = {n(tri(a,h))} cm². 15 × 4,8 : 2 = {n(tri(15,h))} cm², gấp đôi diện tích tam giác MNP.'))
d1,d2=tri(10,6),tri(10,9)
Q.append(mc('kha',25,'Hai hình tam giác cùng đáy 10 cm, chiều cao lần lượt là 6 cm và 9 cm. Diện tích hình thứ hai lớn hơn diện tích hình thứ nhất:',['15 cm²','45 cm²','30 cm²','3 cm²'],0,
 f'Hình thứ nhất: 10 × 6 : 2 = {n(d1)} cm². Hình thứ hai: 10 × 9 : 2 = {n(d2)} cm². Hiệu: {n(d2)} − {n(d1)} = {n(d2-d1)} (cm²).'))
a,h=D('1.5'),D('2.4'); s=tri(a,h)
Q.append(fill('kha',25,'Mỗi cánh buồm hình tam giác có đáy 1,5 m và chiều cao 2,4 m.',[B('Diện tích một cánh buồm là',s,'m²'),B('Diện tích vải để may 5 cánh buồm là',s*5,'m²')],
 f'Một cánh: 1,5 × 2,4 : 2 = {n(s)} m². Năm cánh: {n(s)} × 5 = {n(s*5)} m².'))
it=[('Đáy 10 cm, cao 3 cm',tri(10,3)),('Đáy 7 cm, cao 4 cm',tri(7,4)),('Đáy 8 cm, cao 6 cm',tri(8,6)),('Đáy 5 cm, cao 5 cm',tri(5,5))]
it.sort(key=lambda t:t[1])
Q.append(order('kha',25,'Tính diện tích mỗi tam giác rồi sắp xếp theo thứ tự diện tích từ bé đến lớn.',[t for t,_ in it],'<',
 'Diện tích: '+'; '.join(f'{t} → {n(v)} cm²' for t,v in it)+'.'))
Q.append(tf('kha',25,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Tam giác đáy 8 cm, cao 5 cm có diện tích 20 cm².',True),('Giữ nguyên chiều cao, đáy tăng gấp 3 lần thì diện tích tăng gấp 3 lần.',True),('Đáy và chiều cao cùng tăng gấp đôi thì diện tích cũng chỉ tăng gấp đôi.',False),('Hai tam giác có diện tích bằng nhau thì chúng có cùng đáy.',False)],
 'a) Đúng: 8 × 5 : 2 = 20. b) Đúng. c) Sai: đáy gấp đôi và chiều cao gấp đôi thì diện tích gấp 4 lần. d) Sai: ví dụ tam giác đáy 6 cm, cao 4 cm và tam giác đáy 8 cm, cao 3 cm đều có diện tích 12 cm² nhưng đáy khác nhau.'))
# GIỎI
a,h=D('2.4'),D('1.8'); s=tri(a,h); p=D(180000)
Q.append(fill('gioi',25,'Mái hiên hình tam giác vuông có hai cạnh góc vuông dài 2,4 m và 1,8 m. Lợp mái bằng tôn, giá 180 000 đồng một mét vuông.',[B('Diện tích mái hiên là',s,'m²'),B('Tiền mua tôn là',s*p,'đồng')],
 f'Diện tích: 2,4 × 1,8 : 2 = {n(s)} m². Tiền tôn: {n(s)} × 180 000 = {n(s*p)} đồng.',fig=fig_tri('right','2,4 m','1,8 m','Mái hiên')))
a,h=D(45),D(32); s=tri(a,h)
Q.append(fill('gioi',25,'Mảnh đất hình tam giác có đáy 45 m, chiều cao 32 m. Người ta trồng cây, mỗi cây chiếm 4 m² đất.',[B('Diện tích mảnh đất là',s,'m²'),B('Số cây trồng được là',s/4,'cây')],
 f'Diện tích: 45 × 32 : 2 = {n(s)} m². Số cây: {n(s)} : 4 = {n(s/4)} cây.'))
a,h=D(10),D('2.4'); L,hw=D(10),D(5); s1=tri(a,h); s2=L*hw; door=D('4.5')
Q.append(fill('gioi',29,'Mặt trước ngôi nhà gồm phần mái hình tam giác và thân nhà hình chữ nhật như hình. Cửa ra vào chiếm 4,5 m² không phải sơn.',[B('Diện tích phần mái hình tam giác là',s1,'m²'),B('Diện tích cả mặt trước ngôi nhà là',s1+s2,'m²'),B('Diện tích cần sơn là',s1+s2-door,'m²')],
 f'Mái: 10 × 2,4 : 2 = {n(s1)} m². Thân nhà: 10 × 5 = {n(s2)} m². Cả mặt trước: {n(s1+s2)} m². Trừ cửa: {n(s1+s2)} − 4,5 = {n(s1+s2-door)} m².',fig=fig_house('10 m','5 m','2,4 m','Mặt trước ngôi nhà')))
s,h=D(84),D(12); a=s*2/h; a2=a+6; s2=tri(a2,h)
Q.append(mc('gioi',25,'Mảnh đất hình tam giác có diện tích 84 m² và chiều cao 12 m. Người ta mở rộng đáy thêm 6 m, giữ nguyên chiều cao. Diện tích mảnh đất mới là:',['90 m²','120 m²','168 m²','60 m²'],1,
 f'Đáy cũ: 84 × 2 : 12 = {n(a)} m. Đáy mới: {n(a)} + 6 = {n(a2)} m. Diện tích mới: {n(a2)} × 12 : 2 = {n(s2)} (m²).'))
ab,ac,bc=D(12),D(16),D(20); s=tri(ab,ac); ah=s*2/bc
Q.append(fill('gioi',25,'Tam giác ABC vuông tại A có AB = 12 cm, AC = 16 cm, BC = 20 cm.',[B('Diện tích tam giác ABC là',s,'cm²'),B('Đường cao AH ứng với đáy BC dài',ah,'cm')],
 f'Lấy AB và AC làm đáy và chiều cao: 12 × 16 : 2 = {n(s)} cm². Lấy BC làm đáy: AH = diện tích × 2 : BC = {n(s)} × 2 : 20 = {n(ah)} (cm).',fig=fig_tri('right','AC = 16 cm','AB = 12 cm','Tam giác ABC vuông tại A')))
a,h=D(30),D(40); s=tri(a,h); p=D(90000)
Q.append(fill('gioi',25,'Cô Mai cắt 8 lá cờ hình tam giác, mỗi lá có đáy 30 cm và chiều cao 40 cm. Vải giá 90 000 đồng một mét vuông.',[B('Diện tích một lá cờ là',s,'cm²'),B('Diện tích vải cho 8 lá cờ là',s*8/10000,'m²'),B('Tiền mua vải cho 8 lá cờ là',s*8/10000*p,'đồng')],
 f'Một lá: 30 × 40 : 2 = {n(s)} cm². Tám lá: {n(s)} × 8 = {n(s*8)} cm² = {n(s*8/10000)} m² (1 m² = 10 000 cm²). Tiền vải: {n(s*8/10000)} × 90 000 = {n(s*8/10000*p)} đồng.'))
write5(2,Q)
