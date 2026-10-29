from g5lib import *
Q=[]
def E(items): return [B(e+' =',v,u) for e,v,u in items]
def W(items): return '; '.join(f'{e} = {n(v)} {u}' for e,v,u in items)+'.'
a=[('28 m 15 cm',D(2815),'cm'),('13,7 m',D(137),'dm'),('9,02 km',D(9020),'m')]
Q.append(fill('tb',34,'Số?',E(a),'1 m = 100 cm nên 28 m 15 cm = 2 815 cm. 1 m = 10 dm nên 13,7 m = 137 dm. 1 km = 1 000 m nên 9,02 km = 9 020 m.'))
a=[('4 kg 500 g',D(4500),'g'),('3,42 tạ',D(342),'kg'),('6,35 tấn',D(6350),'kg')]
Q.append(fill('tb',34,'Số?',E(a),'1 kg = 1 000 g nên 4 kg 500 g = 4 500 g. 1 tạ = 100 kg nên 3,42 tạ = 342 kg. 1 tấn = 1 000 kg nên 6,35 tấn = 6 350 kg.'))
Q.append(mc('tb',34,'5 m 6 cm viết dưới dạng số đo có đơn vị là mét là:',['5,6 m','5,06 m','56 m','5,006 m'],1,
 '6 cm = 0,06 m nên 5 m 6 cm = 5,06 m.'))
a=[('4 ha',D(40000),'m²'),('6,5 ha',D(65000),'m²'),('700 ha',D(7),'km²')]
Q.append(fill('tb',34,'Số?',E(a),'1 ha = 10 000 m² nên 4 ha = 40 000 m²; 6,5 ha = 65 000 m². 1 km² = 100 ha nên 700 ha = 7 km².'))
a=[('2,75 m²',D(275),'dm²'),('5 dm² 24 cm²',D(524),'cm²'),('90 000 m²',D(9),'ha')]
Q.append(fill('tb',34,'Số?',E(a),'1 m² = 100 dm² nên 2,75 m² = 275 dm². 5 dm² 24 cm² = 500 cm² + 24 cm² = 524 cm². 1 ha = 10 000 m² nên 90 000 m² = 9 ha.'))
Q.append(mc('tb',34,'1 héc-ta (ha) bằng:',['100 m²','1 000 m²','10 000 m²','100 000 m²'],2,
 '1 ha là diện tích hình vuông cạnh 100 m, nên 1 ha = 100 × 100 = 10 000 m².'))
a=[('6,34 km + 5,8 km',D('6.34')+D('5.8'),'km'),('7,6 kg − 2,75 kg',D('7.6')-D('2.75'),'kg'),('28,6 ha × 5',D('28.6')*5,'ha')]
Q.append(fill('tb',34,'Tính.',E(a),W(a)))
Q.append(tf('tb',34,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('1 km² = 100 ha.',True),('1 tạ = 1 000 kg.',False),('1 m² = 100 dm².',True),('1 tấn = 1 000 kg.',True)],
 'a), c), d) đúng. b) Sai: 1 tạ = 100 kg, còn 1 tấn = 1 000 kg.'))
Q.append(mc('tb',34,'Đổi 0,6 l ra mi-li-lít, ta được:',['6 ml','60 ml','600 ml','6 000 ml'],2,
 '1 l = 1 000 ml nên 0,6 l = 0,6 × 1 000 = 600 ml.'))
Q.append(fill('tb',34,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL('2,5 km',cmp(2500,2500),'2 500 m'),SEL('3,2 tạ',cmp(320,300),'300 kg'),SEL('450 g',cmp('0.45','0.5'),'0,5 kg')],
 '2,5 km = 2 500 m. 3,2 tạ = 320 kg > 300 kg. 450 g = 0,45 kg < 0,5 kg.'))
# KHÁ
a=[('3 tấn 50 kg',D('3.05'),'tấn'),('4 m 8 cm',D('4.08'),'m'),('2 kg 75 g',D('2.075'),'kg')]
Q.append(fill('kha',34,'Số?',E(a),'50 kg = 0,05 tấn nên 3 tấn 50 kg = 3,05 tấn. 8 cm = 0,08 m nên 4 m 8 cm = 4,08 m. 75 g = 0,075 kg nên 2 kg 75 g = 2,075 kg.'))
a=[('15,6 km × 4',D('15.6')*4,'km'),('93,17 km² : 7',D('93.17')/7,'km²'),('12 kg − 4 kg 250 g',D(12)-D('4.25'),'kg')]
Q.append(fill('kha',34,'Tính.',E(a),W(a)+' Chú ý 4 kg 250 g = 4,25 kg.'))
Q.append(mc('kha',34,'Diện tích Hồ Gươm khoảng 0,12 km². Diện tích đó bằng bao nhiêu héc-ta?',['1,2 ha','12 ha','120 ha','1 200 ha'],1,
 '1 km² = 100 ha nên 0,12 km² = 0,12 × 100 = 12 ha.'))
L=D(450); Wd=L/3; s=L*Wd
Q.append(fill('kha',34,'Khu đất hình chữ nhật có chiều dài 450 m, chiều rộng bằng {1/3} chiều dài.',[B('Chiều rộng khu đất là',Wd,'m'),B('Diện tích khu đất là',s,'m²'),B('Diện tích khu đất là',s/10000,'ha')],
 f'Chiều rộng: 450 : 3 = {n(Wd)} m. Diện tích: 450 × {n(Wd)} = {n(s)} m². Đổi sang héc-ta: {n(s)} : 10 000 = {n(s/10000)} ha.'))
Q.append(mc('kha',34,'Rót hết 20 l dầu vào các chai, mỗi chai chứa 0,5 l. Số chai cần dùng là:',['10 chai','20 chai','40 chai','80 chai'],2,
 f'20 : 0,5 = {n(D(20)/D("0.5"))} (chai). Chia cho 0,5 giống nhân với 2.'))
Q.append(fill('kha',34,'Xe tải chở 3,5 tấn gạo, mỗi bao gạo nặng 50 kg.',[B('Xe chở được',D('3.5')*1000/50,'bao gạo'),B('Số gạo chở được là',D('3.5')*10,'tạ')],
 f'3,5 tấn = 3 500 kg. Số bao: 3 500 : 50 = {n(D("3.5")*1000/50)} bao. 1 tấn = 10 tạ nên 3,5 tấn = 35 tạ.'))
it=[('2 400 m',D(2400)),('2 450 m',D(2450)),('2,5 km',D(2500)),('2 km 600 m',D(2600))]
Q.append(order('kha',34,'Đổi về cùng một đơn vị rồi sắp xếp các độ dài sau theo thứ tự từ bé đến lớn.',[t for t,_ in it],'<',
 'Đổi ra mét: 2 400 m; 2 450 m; 2,5 km = 2 500 m; 2 km 600 m = 2 600 m. Thứ tự: 2 400 m < 2 450 m < 2,5 km < 2 km 600 m.'))
Q.append(tf('kha',34,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('0,5 km² = 50 ha.',True),('2,5 tấn lớn hơn 2 400 kg.',True),('1 000 ml = 1 l.',True),('3 m² 5 dm² = 3,5 m².',False)],
 'a) Đúng: 0,5 × 100 = 50 ha. b) Đúng: 2,5 tấn = 2 500 kg > 2 400 kg. c) Đúng. d) Sai: 5 dm² = 0,05 m² nên 3 m² 5 dm² = 3,05 m².'))
# GIỎI
km=D('2.4'); ha=km*100; per=D(1600)
Q.append(fill('gioi',34,'Khu rừng có diện tích 2,4 km². Cứ mỗi héc-ta trồng được 1 600 cây.',[B('Diện tích khu rừng là',ha,'ha'),B('Số cây trồng được là',ha*per,'cây')],
 f'2,4 km² = 2,4 × 100 = {n(ha)} ha. Số cây: {n(ha)} × 1 600 = {n(ha*per)} cây.'))
t=D('4.5'); kg=t*1000; bao=kg/60; p=D(45000)
Q.append(fill('gioi',34,'Một hợp tác xã thu hoạch 4,5 tấn cà phê, đóng vào các bao, mỗi bao 60 kg. Giá cà phê là 45 000 đồng một ki-lô-gam.',[B('Số bao cà phê là',bao,'bao'),B('Bán hết số cà phê thu được',kg*p,'đồng')],
 f'4,5 tấn = {n(kg)} kg. Số bao: {n(kg)} : 60 = {n(bao)} bao. Tiền bán: {n(kg)} × 45 000 = {n(kg*p)} đồng.'))
ha=D('1.2'); m2=ha*10000; kg=m2/100*65
Q.append(fill('gioi',34,'Thửa ruộng rộng 1,2 ha. Cứ 100 m² thu hoạch được 65 kg lúa.',[B('Diện tích thửa ruộng là',m2,'m²'),B('Thu hoạch được',kg,'kg lúa'),B('Số lúa đó là',kg/1000,'tấn')],
 f'1,2 ha = 1,2 × 10 000 = {n(m2)} m². Số lúa: {n(m2)} : 100 × 65 = {n(kg)} kg = {n(kg/1000)} tấn.'))
s=D(80)*50
Q.append(mc('gioi',34,'Mảnh vườn hình chữ nhật dài 80 m, rộng 50 m. Diện tích mảnh vườn là bao nhiêu héc-ta?',['0,04 ha','0,4 ha','4 ha','40 ha'],1,
 f'Diện tích: 80 × 50 = {n(s)} m². Đổi: {n(s)} : 10 000 = {n(s/10000)} ha.'))
a_,b_,c_=D('1.2'),D('8.5'),D('0.75'); tk=a_+b_+c_
Q.append(fill('gioi',34,'Nam đi bộ 1,2 km, đi xe buýt 8,5 km và đi xe đạp 750 m để tới nhà bà.',[B('Quãng đường Nam đã đi là',tk*1000,'m'),B('Quãng đường Nam đã đi là',tk,'km')],
 f'Đổi 750 m = 0,75 km. Tổng quãng đường: 1,2 + 8,5 + 0,75 = {n(tk)} km = {n(tk*1000)} m.'))
Q.append(tf('gioi',34,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('5 km 40 m = 5,04 km.',True),('3,5 kg = 3 kg 500 g.',True),('250 ml = 0,25 l.',True),('1,5 ha = 1 500 m².',False)],
 'a) Đúng: 40 m = 0,04 km. b) Đúng: 0,5 kg = 500 g. c) Đúng: 250 : 1 000 = 0,25. d) Sai: 1,5 ha = 1,5 × 10 000 = 15 000 m².'))
write6(5,Q)
