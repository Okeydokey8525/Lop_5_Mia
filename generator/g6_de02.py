from g5lib import *
Q=[]
Q.append(mc('tb',30,'Số thập phân "không phẩy không mười chín" viết là:',['0,019','0,19','0,0019','0,0109'],0,
 'Phần nguyên là 0, phần thập phân đọc là "không mười chín" tức hai chữ số 0 rồi 19 theo đúng thứ tự phần mười, phần trăm, phần nghìn: 0,019.'))
Q.append(fill('tb',30,'Viết số thập phân.',[B('Hai mươi ba phẩy tám mươi lăm viết là',D('23.85')),B('Không phẩy không năm viết là',D('0.05')),B('Một trăm linh hai phẩy ba viết là',D('102.3'))],
 'Hai mươi ba phẩy tám mươi lăm: 23,85. Không phẩy không năm: 0,05. Một trăm linh hai phẩy ba: 102,3.'))
Q.append(tf('tb',30,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Chữ số 3 trong số 2,03 thuộc hàng phần trăm.',True),('Chữ số 3 trong số 109,37 thuộc hàng chục.',False),('Chữ số 3 trong số 98,213 thuộc hàng phần nghìn.',True),('Chữ số 9 trong số 0,925 thuộc hàng phần mười.',True)],
 'a) Đúng: sau dấu phẩy 0 là phần mười, 3 là phần trăm. b) Sai: chữ số 3 đứng ngay sau dấu phẩy nên thuộc hàng phần mười. c) Đúng: 2 phần mười, 1 phần trăm, 3 phần nghìn. d) Đúng: chữ số 9 ngay sau dấu phẩy.'))
Q.append(mc('tb',30,'Số thập phân lớn nhất trong các số 5,09; 5,9; 5,089; 5,19 là:',['5,09','5,9','5,089','5,19'],1,
 'Phần nguyên đều là 5. So sánh phần mười: 0; 9; 0; 1. Số có phần mười lớn nhất là 5,9.'))
Q.append(fill('tb',30,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL('7,5',cmp('7.5','7.50'),'7,50'),SEL('0,3',cmp('0.3','0.29'),'0,29'),SEL('15,08',cmp('15.08','15.8'),'15,8')],
 '7,5 = 7,50. 0,3 = 0,30 mà 0,30 > 0,29. 15,08 < 15,8 vì phần mười 0 < 8.'))
Q.append(fill('tb',30,'Làm tròn số thập phân.',[B('Làm tròn 18,67 đến hàng phần mười được',rnd('18.67',1)),B('Làm tròn 18,67 đến số tự nhiên gần nhất được',rnd('18.67',0)),B('Làm tròn 0,452 đến hàng phần trăm được',rnd('0.452',2))],
 '18,67 ≈ 18,7 (chữ số 7 ≥ 5 nên thêm 1 vào phần mười). 18,67 ≈ 19 (chữ số 6 ≥ 5). 0,452 ≈ 0,45 (chữ số 2 < 5).'))
Q.append(fill('tb',34,'Số?',[B('8 mm =',D('0.008'),'m'),B('17 ml =',D('0.017'),'l'),B('500 g =',D('0.5'),'kg')],
 '1 m = 1 000 mm nên 8 mm = 0,008 m. 1 l = 1 000 ml nên 17 ml = 0,017 l. 1 kg = 1 000 g nên 500 g = 0,5 kg.'))
Q.append(mc('tb',34,'2 m 5 dm viết dưới dạng số đo có đơn vị là mét là:',['2,05 m','2,5 m','25 m','2,005 m'],1,
 '5 dm = 0,5 m nên 2 m 5 dm = 2,5 m.'))
Q.append(fill('tb',30,'Viết số thập phân.',[B('7 đơn vị và 5 phần mười viết là',D('7.5')),B('4 chục và 6 phần trăm viết là',D('40.06'))],
 '7 đơn vị 5 phần mười: 7,5. 4 chục = 40, thêm 6 phần trăm: phần mười là 0 nên 40,06.'))
Q.append(mc('tb',30,'Số nào bằng 0,5?',['0,05','0,50','5,0','0,005'],1,
 'Viết thêm chữ số 0 vào bên phải phần thập phân thì giá trị không đổi: 0,5 = 0,50.'))
# KHÁ
x=D('12.468')
Q.append(fill('kha',30,'Quãng đường từ nhà Nam đến trường dài 12,468 km. Làm tròn số đo đó:',[B('Đến số tự nhiên gần nhất được',rnd(x,0),'km'),B('Đến hàng phần mười được',rnd(x,1),'km'),B('Đến hàng phần trăm được',rnd(x,2),'km')],
 '12,468 ≈ 12 (chữ số 4 < 5). 12,468 ≈ 12,5 (chữ số 6 ≥ 5). 12,468 ≈ 12,47 (chữ số 8 ≥ 5).'))
it=['6,25','6,5','6,052','5,99']; it.sort(key=lambda s:-D(s.replace(',','.')))
Q.append(order('kha',30,'Sắp xếp các số sau theo thứ tự từ lớn đến bé.',it,'>',
 'So sánh phần nguyên: 5,99 bé nhất. Với 6,5; 6,25; 6,052: phần mười lần lượt 5; 2; 0. Thứ tự: 6,5 > 6,25 > 6,052 > 5,99.'))
Q.append(mc('kha',30,'Số thập phân nào lớn hơn 4,5 và bé hơn 4,6?',['4,45','4,55','4,65','4,6'],1,
 '4,5 = 4,50 và 4,6 = 4,60. Chỉ có 4,55 nằm giữa 4,50 và 4,60.'))
Q.append(mc('kha',30,'Bốn bạn chạy 60 m: Nam 9,8 giây; Mai 10,25 giây; Việt 9,75 giây; Mi 10,2 giây. Bạn chạy nhanh nhất là:',['Nam','Mai','Việt','Mi'],2,
 'Thời gian chạy ít nhất thì nhanh nhất. So sánh: 9,75 < 9,8 < 10,2 < 10,25. Việt chạy nhanh nhất.'))
Q.append(fill('kha',34,'Nam cao 1,45 m, Mai cao 138 cm.',[B('Nam cao hơn Mai',D(7),'cm'),B('Tổng chiều cao của hai bạn là',D('2.83'),'m')],
 'Đổi 1,45 m = 145 cm. Nam cao hơn Mai: 145 − 138 = 7 cm. Tổng chiều cao: 145 + 138 = 283 cm = 2,83 m.'))
Q.append(mc('kha',34,'0,05 km bằng bao nhiêu mét?',['5 m','50 m','500 m','0,5 m'],1,
 '1 km = 1 000 m nên 0,05 km = 0,05 × 1 000 = 50 m.'))
Q.append(tf('kha',30,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('0,6 = 0,60.',True),('12,7 > 12,07.',True),('Làm tròn 3,08 đến hàng phần mười được 3,1.',True),('0,09 > 0,1.',False)],
 'a) Đúng. b) Đúng: phần mười 7 > 0. c) Đúng: chữ số hàng phần trăm là 8 ≥ 5 nên 3,08 ≈ 3,1. d) Sai: 0,09 < 0,10.'))
Q.append(fill('kha',34,'Số?',[B('3,5 tạ =',D(350),'kg'),B('2,7 l =',D(2700),'ml'),B('0,5 ha =',D(5000),'m²')],
 '1 tạ = 100 kg nên 3,5 tạ = 350 kg. 1 l = 1 000 ml nên 2,7 l = 2 700 ml. 1 ha = 10 000 m² nên 0,5 ha = 5 000 m².'))
# GIỎI
v,ao=D('12.5'),D('1.25'); p=D(85000)
Q.append(fill('gioi',31,'Tấm vải dài 12,5 m. Cô Lan cắt mỗi chiếc áo hết 1,25 m vải. Vải giá 85 000 đồng một mét.',[B('Số chiếc áo may được là',v/ao,'chiếc'),B('Tiền mua tấm vải là',v*p,'đồng')],
 f'Số áo: 12,5 : 1,25 = {n(v/ao)} chiếc. Tiền vải: 12,5 × 85 000 = {n(v*p)} đồng.'))
l=D('2.4')/100*250; pr=D(24000)
Q.append(fill('gioi',31,'Xe máy của bác Nam đi 100 km hết 2,4 l xăng. Bác đi quãng đường 250 km. Giá xăng 24 000 đồng một lít.',[B('Số lít xăng cần dùng là',l,'l'),B('Tiền xăng là',l*pr,'đồng')],
 f'Số lít xăng: 2,4 × 250 : 100 = {n(l)} l. Tiền xăng: {n(l)} × 24 000 = {n(l*pr)} đồng.'))
m=[D('85.5'),D('120.5'),D(96),D(78)]; tg=sum(m); tbm=tg/4
Q.append(fill('gioi',31,'Lượng mưa bốn tháng liên tiếp đo được là 85,5 mm; 120,5 mm; 96 mm; 78 mm. Lượng mưa trung bình bằng tổng chia cho 4.',[B('Tổng lượng mưa bốn tháng là',tg,'mm'),B('Lượng mưa trung bình mỗi tháng là',tbm,'mm')],
 f'Tổng: 85,5 + 120,5 + 96 + 78 = {n(tg)} mm. Trung bình: {n(tg)} : 4 = {n(tbm)} mm.'))
Q.append(mc('gioi',30,'Có bao nhiêu số thập phân có một chữ số ở phần thập phân, lớn hơn 2,3 và bé hơn 2,7?',['2 số','3 số','4 số','5 số'],1,
 'Các số đó là 2,4; 2,5; 2,6. Vậy có 3 số.'))
sa=D('24.5'); tr=sa+D('8.7'); to=tr-D('6.9')
Q.append(fill('gioi',31,'Buổi sáng nhiệt độ là 24,5 °C. Buổi trưa nhiệt độ cao hơn buổi sáng 8,7 °C. Buổi tối nhiệt độ thấp hơn buổi trưa 6,9 °C.',[B('Nhiệt độ buổi trưa là',tr,'°C'),B('Nhiệt độ buổi tối là',to,'°C')],
 f'Buổi trưa: 24,5 + 8,7 = {n(tr)} °C. Buổi tối: {n(tr)} − 6,9 = {n(to)} °C.'))
Q.append(tf('gioi',34,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Làm tròn 4,38 đến hàng phần trăm được 4,4.',False),('0,5 km dài hơn 450 m.',True),('3,5 tạ nhẹ hơn 350 kg.',False),('2,05 m = 2 m 5 cm.',True)],
 'a) Sai: 4,38 đã có hai chữ số ở phần thập phân nên làm tròn đến hàng phần trăm vẫn là 4,38 (làm tròn đến hàng phần mười mới được 4,4). b) Đúng: 0,5 km = 500 m > 450 m. c) Sai: 3,5 tạ = 350 kg, bằng nhau. d) Đúng: 0,05 m = 5 cm.'))
write6(2,Q)
