from g5lib import *
Q=[]
def E(items): return [B(e+' =',v) for e,v in items]
def W(items): return '; '.join(f'{e} = {n(v)}' for e,v in items)+'.'
Q.append(mc('tb',35,'Chuyển phân số {17/5} thành hỗn số, ta được:',['{3 2/5}','{3 1/5}','{2 3/5}','{5 3/17}'],0,
 '17 : 5 được 3 dư 2 nên {17/5} = {3 2/5}.'))
Q.append(mc('tb',35,'Phân số {3/4} viết dưới dạng số thập phân là:',['0,75','0,34','0,43','7,5'],0,
 '{3/4} = {75/100} = 0,75 (nhân cả tử số và mẫu số với 25).'))
Q.append(fill('tb',35,'Tính (viết kết quả là phân số tối giản).',[FR('{3/8} + {1/8} =',Fraction(1,2)),FR('{7/9} − {4/9} =',Fraction(1,3)),FR('{2/5} × {5/6} =',Fraction(1,3))],
 '3/8 + 1/8 = 4/8 = 1/2. 7/9 − 4/9 = 3/9 = 1/3. 2/5 × 5/6 = 10/30 = 1/3.'))
a=[('45,6 + 8,95',D('45.6')+D('8.95')),('70 − 28,45',D(70)-D('28.45')),('6,5 × 4',D('6.5')*4)]
Q.append(fill('tb',31,'Tính.',E(a),W(a)))
a=[('8,4 : 4',D('8.4')/4),('0,75 × 100',D('0.75')*100),('15 : 6',D(15)/6)]
Q.append(fill('tb',31,'Tính.',E(a),W(a)))
Q.append(mc('tb',30,'Làm tròn số 12,375 đến hàng phần trăm, ta được:',['12,37','12,38','12,4','12,3'],1,
 'Chữ số ở hàng phần nghìn là 5 nên làm tròn lên: 12,375 ≈ 12,38.'))
Q.append(fill('tb',30,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL('{1/2}',cmp(D('0.5'),D('0.5')),'0,5'),SEL('3,45',cmp('3.45','3.5'),'3,5'),SEL('{1 1/4}',cmp('1.25','1.2'),'1,2')],
 '{1/2} = 0,5. 3,45 < 3,5 vì phần mười 4 < 5. {1 1/4} = 1,25 > 1,2.'))
Q.append(mc('tb',32,'Diện tích hình tam giác có đáy 10 cm và chiều cao 6 cm là:',['60 cm²',n(tri(10,6))+' cm²','16 cm²','30 cm'],1,
 f'10 × 6 : 2 = {n(tri(10,6))} (cm²).'))
Q.append(fill('tb',33,'Tính.',[B('Chu vi hình tròn đường kính 5 cm là',circ_d(5),'cm'),B('Diện tích hình tròn bán kính 3 cm là',disc(3),'cm²')],
 f'3,14 × 5 = {n(circ_d(5))} cm. 3,14 × 3 × 3 = {n(disc(3))} cm².'))
Q.append(tf('tb',35,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('{4/9} + {2/7} = {6/16}.',False),('{2 1/3} = {7/3}.',True),('0,5 × 0,1 = 0,05.',True),('1 ha = 10 000 m².',True)],
 'a) Sai: hai phân số khác mẫu số phải quy đồng rồi mới cộng, 4/9 + 2/7 = 28/63 + 18/63 = 46/63. b) Đúng. c) Đúng. d) Đúng.'))
# KHÁ
Q.append(fill('kha',35,'Chuyển đổi (viết hỗn số hoặc phân số tối giản).',[MX('{7/3} =',Fraction(7,3)),MX('{23/10} =',Fraction(23,10)),FR('{3 2/5} =',Fraction(17,5))],
 '7 : 3 được 2 dư 1 nên {7/3} = {2 1/3}. 23 : 10 được 2 dư 3 nên {23/10} = {2 3/10}. {3 2/5} = {3 × 5 + 2/5} = {17/5}.'))
Q.append(fill('kha',35,'Tính.',[MX('{5/7} + {3/4} =',Fraction(5,7)+Fraction(3,4)),FR('{4/5} − {2/3} =',Fraction(4,5)-Fraction(2,3))],
 '5/7 + 3/4 = 20/28 + 21/28 = 41/28 = 1 13/28. 4/5 − 2/3 = 12/15 − 10/15 = 2/15.'))
x=(D('4.5')+D('1.5'))*D('2.5')-D('3.2'); y=D('8.16')/(D('1.32')+D('3.48'))
Q.append(fill('kha',31,'Tính giá trị của biểu thức.',[B('(4,5 + 1,5) × 2,5 − 3,2 =',x),B('8,16 : (1,32 + 3,48) =',y)],
 f'(4,5 + 1,5) × 2,5 − 3,2 = 6 × 2,5 − 3,2 = 15 − 3,2 = {n(x)}. 8,16 : (1,32 + 3,48) = 8,16 : 4,8 = {n(y)}.'))
tong=3*D(4500)+6*D(7500); tl=D(100000)-tong
Q.append(mc('kha',31,'Nam mua 3 bút bi giá 4 500 đồng một chiếc và 6 quyển vở giá 7 500 đồng một quyển. Nam đưa 100 000 đồng. Cô bán hàng trả lại cho Nam:',[n(tl)+' đồng',n(tong)+' đồng','45 000 đồng','13 500 đồng'],0,
 f'Bút: 4 500 × 3 = 13 500 đồng. Vở: 7 500 × 6 = 45 000 đồng. Tổng: {n(tong)} đồng. Trả lại: 100 000 − {n(tong)} = {n(tl)} đồng.'))
Q.append(fill('kha',33,'Tính diện tích.',[B('Hình thang đáy 14 cm và 10 cm, cao 7 cm có diện tích',trap(14,10,7),'cm²'),B('Hình tròn bán kính 5 cm có diện tích',disc(5),'cm²')],
 f'(14 + 10) × 7 : 2 = {n(trap(14,10,7))} cm². 3,14 × 5 × 5 = {n(disc(5))} cm².'))
a=[('4,25 tấn',D(4250),'kg'),('3,6 ha',D(36000),'m²'),('0,45 km',D(450),'m')]
Q.append(fill('kha',34,'Số?',[B(e+' =',v,u) for e,v,u in a],'1 tấn = 1 000 kg nên 4,25 tấn = 4 250 kg. 1 ha = 10 000 m² nên 3,6 ha = 36 000 m². 1 km = 1 000 m nên 0,45 km = 450 m.'))
Q.append(order('kha',35,'Sắp xếp các số sau theo thứ tự từ bé đến lớn.',['0,05','0,45','{1/2}','{3/5}'],'<',
 'Đổi về số thập phân: 0,05; 0,45; {1/2} = 0,5; {3/5} = 0,6. Thứ tự: 0,05 < 0,45 < {1/2} < {3/5}.'))
Q.append(tf('kha',35,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Hình tam giác đáy 8 cm, cao 5 cm có diện tích 20 cm².',True),('Hình tròn bán kính 4 cm có chu vi 25,12 cm.',True),('3,6 : 0,1 = 0,36.',False),('{3/4} < 0,8.',True)],
 'a) Đúng: 8 × 5 : 2 = 20. b) Đúng: 3,14 × 4 × 2 = 25,12. c) Sai: chia cho 0,1 là chuyển dấu phẩy sang phải một chữ số, 3,6 : 0,1 = 36. d) Đúng: {3/4} = 0,75 < 0,8.'))
# GIỎI
L,Wd,dd=D(40),D(25),D(8); s=L*Wd; sa=disc(dd/2)
Q.append(fill('gioi',33,'Mảnh vườn hình chữ nhật dài 40 m, rộng 25 m, có một ao tròn đường kính 8 m. Phần còn lại trồng rau.',[B('Diện tích mảnh vườn là',s,'m²'),B('Diện tích ao là',sa,'m²'),B('Diện tích trồng rau là',s-sa,'m²')],
 f'Vườn: 40 × 25 = {n(s)} m². Bán kính ao 4 m: 3,14 × 4 × 4 = {n(sa)} m². Trồng rau: {n(s)} − {n(sa)} = {n(s-sa)} m².'))
th,ca=D('1.5')*140000,D('0.5')*90000; tg=th+ca; tl=D(300000)-tg
Q.append(fill('gioi',31,'Mẹ mua 1,5 kg thịt giá 140 000 đồng một ki-lô-gam và 0,5 kg cá giá 90 000 đồng một ki-lô-gam. Mẹ đưa 300 000 đồng.',[B('Tiền mua thịt là',th,'đồng'),B('Tiền mua cá là',ca,'đồng'),B('Mẹ được trả lại',tl,'đồng')],
 f'Thịt: 1,5 × 140 000 = {n(th)} đồng. Cá: 0,5 × 90 000 = {n(ca)} đồng. Tổng: {n(tg)} đồng. Trả lại: 300 000 − {n(tg)} = {n(tl)} đồng.'))
a=D('0.25')*D('6.3')*4; b=D('3.7')*D('6.5')+D('3.7')*D('3.5')
Q.append(fill('gioi',31,'Tính bằng cách thuận tiện.',[B('0,25 × 6,3 × 4 =',a),B('3,7 × 6,5 + 3,7 × 3,5 =',b),FR('{3/7} × {5/9} + {3/7} × {4/9} =',Fraction(3,7))],
 f'0,25 × 6,3 × 4 = (0,25 × 4) × 6,3 = 1 × 6,3 = {n(a)}. 3,7 × 6,5 + 3,7 × 3,5 = 3,7 × (6,5 + 3,5) = 3,7 × 10 = {n(b)}. {{3/7}} × {{5/9}} + {{3/7}} × {{4/9}} = {{3/7}} × ({{5/9}} + {{4/9}}) = {{3/7}} × 1 = {{3/7}}.'))
x=D('10.2')-D('3.75')
Q.append(mc('gioi',31,'Tìm x biết x + 3,75 = 10,2. Giá trị của x là:',[n(x),'13,95','7,55','6,55'],0,
 f'x = 10,2 − 3,75 = {n(x)}. Kiểm tra: {n(x)} + 3,75 = 10,2.'))
r=D(3); s=disc(r); v=s*D('1.5')
Q.append(fill('gioi',33,'Bể nước hình tròn có bán kính 3 m, nước sâu 1,5 m. 1 m³ nước bằng 1 000 lít.',[B('Diện tích đáy bể là',s,'m²'),B('Thể tích nước trong bể là',v,'m³'),B('Thể tích nước đó là',v*1000,'lít')],
 f'Diện tích đáy: 3,14 × 3 × 3 = {n(s)} m². Thể tích: {n(s)} × 1,5 = {n(v)} m³. Đổi sang lít: {n(v)} × 1 000 = {n(v*1000)} lít.'))
Q.append(tf('gioi',35,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('{5/6} − {1/4} = {7/12}.',True),('Hình tam giác đáy 12 cm, cao 5 cm có diện tích 30 cm².',True),('Hình thang đáy 6 cm và 10 cm, cao 4 cm có diện tích 32 cm².',True),('8,4 : 0,2 = 4,2.',False)],
 'a) Đúng: 10/12 − 3/12 = 7/12. b) Đúng: 12 × 5 : 2 = 30. c) Đúng: (6 + 10) × 4 : 2 = 32. d) Sai: chia cho 0,2 giống nhân với 5, 8,4 : 0,2 = 42.'))
write6(6,Q)
