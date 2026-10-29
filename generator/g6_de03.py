from g5lib import *
Q=[]
def E(items,fn=None):
    return [B(e+' =',v) for e,v in items]
def W(items): return '; '.join(f'{e} = {n(v)}' for e,v in items)+'.'
a=[('36,8 + 25,7',D('36.8')+D('25.7')),('52,34 − 17,9',D('52.34')-D('17.9')),('4,6 × 3',D('4.6')*3)]
Q.append(fill('tb',31,'Tính.',E(a),W(a)))
Q.append(mc('tb',31,'Kết quả của phép tính 0,4 × 0,5 là:',['2','0,2','0,02','20'],1,
 '4 × 5 = 20, hai thừa số có tất cả 2 chữ số ở phần thập phân nên tích là 0,20 = 0,2.'))
a=[('18,6 : 3',D('18.6')/3),('7,5 : 5',D('7.5')/5),('9 : 4',D(9)/4)]
Q.append(fill('tb',31,'Tính.',E(a),W(a)+' Với 9 : 4 chia tiếp phần dư bằng cách thêm chữ số 0: 9 : 4 = 2,25.'))
Q.append(mc('tb',31,'Kết quả của phép tính 7,8 × 100 là:',['78','780','7 800','0,78'],1,
 'Nhân với 100 thì chuyển dấu phẩy sang phải hai chữ số: 7,8 × 100 = 780.'))
c,v=D(2)*D(28500),D(3)*D(8500)
Q.append(fill('tb',31,'Ở cửa hàng, cam giá 28 500 đồng một ki-lô-gam, vở giá 8 500 đồng một quyển.',[B('Mua 2 kg cam hết',c,'đồng'),B('Mua 3 quyển vở hết',v,'đồng')],
 f'2 kg cam: 28 500 × 2 = {n(c)} đồng. 3 quyển vở: 8 500 × 3 = {n(v)} đồng.'))
t=D('1.5')*30000
Q.append(mc('tb',31,'Bưởi giá 30 000 đồng một ki-lô-gam. Mua 1,5 kg bưởi hết bao nhiêu tiền?',['4 500 đồng','45 000 đồng','31 500 đồng','450 000 đồng'],1,
 f'1,5 × 30 000 = {n(t)} (đồng).'))
Q.append(fill('tb',31,'Mẹ có 100 000 đồng, mua rau hết 24 500 đồng.',[B('Mẹ còn lại',D(100000)-D(24500),'đồng')],
 f'100 000 − 24 500 = {n(D(100000)-D(24500))} (đồng).'))
Q.append(tf('tb',31,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('5,6 + 2,4 = 8.',True),('10 − 3,5 = 6,5.',True),('2,5 × 4 = 100.',False),('6 : 0,5 = 12.',True)],
 'a) Đúng. b) Đúng. c) Sai: 2,5 × 4 = 10. d) Đúng: chia cho 0,5 là nhân với 2.'))
x1,x2,x3=D('12.5')+D('7.5'),D('3.2')*5,D('8.4')/2
Q.append(fill('tb',31,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL('12,5 + 7,5',cmp(x1,20),'20'),SEL('3,2 × 5',cmp(x2,15),'15'),SEL('8,4 : 2',cmp(x3,D('4.5')),'4,5')],
 f'12,5 + 7,5 = {n(x1)}. 3,2 × 5 = {n(x2)} > 15. 8,4 : 2 = {n(x3)} < 4,5.'))
t=D('8.5')+D('3.25')
Q.append(mc('tb',31,'Bình xăng có 8,5 l, đổ thêm 3,25 l. Bình xăng có tất cả:',[n(t)+' l','5,25 l','11,25 l','27,625 l'],0,
 f'8,5 + 3,25 = {n(t)} (l).'))
# KHÁ
vai,ren=D('2.5')*64000,D('1.5')*20000; tg=vai+ren
Q.append(fill('kha',31,'Cô Hoa mua 2,5 m vải giá 64 000 đồng một mét và 1,5 m ren giá 20 000 đồng một mét.',[B('Tiền mua vải là',vai,'đồng'),B('Tiền mua ren là',ren,'đồng'),B('Tổng tiền là',tg,'đồng')],
 f'Vải: 2,5 × 64 000 = {n(vai)} đồng. Ren: 1,5 × 20 000 = {n(ren)} đồng. Tổng: {n(vai)} + {n(ren)} = {n(tg)} đồng.'))
a=[('7,35 + 18,9 + 3,75',D('7.35')+D('18.9')+D('3.75')),('90 − 45,68',D(90)-D('45.68')),('2,45 × 1,2',D('2.45')*D('1.2'))]
Q.append(fill('kha',31,'Tính.',E(a),W(a)))
Q.append(fill('kha',31,'Có 7,2 l nước ép cần rót vào các chai.',[B('Nếu mỗi chai chứa 0,6 l thì rót được',D('7.2')/D('0.6'),'chai'),B('Nếu mỗi chai chứa 0,45 l thì rót được',D('7.2')/D('0.45'),'chai')],
 f'7,2 : 0,6 = {n(D("7.2")/D("0.6"))} chai. 7,2 : 0,45 = {n(D("7.2")/D("0.45"))} chai (chuyển dấu phẩy sang phải hai chữ số: 720 : 45).'))
r=D(25)-D('12.75')-D('7.5')
Q.append(mc('kha',31,'Một bao gạo nặng 25 kg. Đã bán 12,75 kg rồi bán thêm 7,5 kg. Bao gạo còn lại:',[n(r)+' kg','20,25 kg','5,25 kg','45,25 kg'],0,
 f'Đã bán: 12,75 + 7,5 = {n(D("12.75")+D("7.5"))} kg. Còn lại: 25 − {n(D("20.25"))} = {n(r)} kg.'))
a=[('25,5 × 4',D('25.5')*4),('0,8 × 12,5',D('0.8')*D('12.5')),('3,6 : 0,9',D('3.6')/D('0.9'))]
Q.append(fill('kha',31,'Tính nhẩm.',E(a),W(a)))
n1=D('8.5'); n2=n1*2; n3=n2+D('3.5'); tt=n1+n2+n3
Q.append(fill('kha',31,'Ngày thứ nhất cửa hàng bán 8,5 kg gạo. Ngày thứ hai bán gấp 2 lần ngày thứ nhất. Ngày thứ ba bán nhiều hơn ngày thứ hai 3,5 kg.',[B('Ngày thứ hai bán',n2,'kg'),B('Ngày thứ ba bán',n3,'kg'),B('Cả ba ngày bán',tt,'kg')],
 f'Ngày thứ hai: 8,5 × 2 = {n(n2)} kg. Ngày thứ ba: {n(n2)} + 3,5 = {n(n3)} kg. Cả ba ngày: {n(n1)} + {n(n2)} + {n(n3)} = {n(tt)} kg.'))
it=[('3,6 + 1,4',D(5)),('2,5 × 3',D('7.5')),('9,6 : 4',D('2.4')),('10 − 3,7',D('6.3'))]
it.sort(key=lambda t:t[1])
Q.append(order('kha',31,'Tính giá trị mỗi phép tính rồi sắp xếp các kết quả theo thứ tự từ bé đến lớn.',[t for t,_ in it],'<',
 'Kết quả: '+'; '.join(f'{t} = {n(v)}' for t,v in it)+'.'))
Q.append(tf('kha',31,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('3,6 : 0,1 = 36.',True),('4,8 × 0,5 = 24.',False),('0,25 × 4 = 1.',True),('5,5 − 2,75 = 2,75.',True)],
 'a) Đúng. b) Sai: nhân với 0,5 là chia 2, 4,8 × 0,5 = 2,4. c) Đúng. d) Đúng.'))
# GIỎI
ct,ha,ot=D('3.5')*18000,D('2.4')*25000,D('0.8')*60000; tg=ct+ha+ot; tl=D(200000)-tg
Q.append(fill('gioi',31,'Chị Lan mua 3,5 kg cà chua giá 18 000 đồng một ki-lô-gam, 2,4 kg hành giá 25 000 đồng một ki-lô-gam và 0,8 kg ớt giá 60 000 đồng một ki-lô-gam. Chị đưa 200 000 đồng.',[B('Chị phải trả tất cả',tg,'đồng'),B('Chị được trả lại',tl,'đồng')],
 f'Cà chua: 3,5 × 18 000 = {n(ct)} đồng. Hành: 2,4 × 25 000 = {n(ha)} đồng. Ớt: 0,8 × 60 000 = {n(ot)} đồng. Tổng: {n(tg)} đồng. Trả lại: 200 000 − {n(tg)} = {n(tl)} đồng.'))
a_,b_=D('15.5'),D('14.5'); s=a_+b_; t=D(1200)/s
Q.append(fill('gioi',31,'Bể nước chứa được 1 200 l. Vòi A chảy 15,5 l mỗi phút, vòi B chảy 14,5 l mỗi phút. Hai vòi cùng chảy vào bể lúc bể cạn.',[B('Mỗi phút cả hai vòi chảy được',s,'l'),B('Bể đầy sau',t,'phút')],
 f'Mỗi phút: 15,5 + 14,5 = {n(s)} l. Thời gian đầy bể: 1 200 : {n(s)} = {n(t)} phút.'))
b=D('0.35')*24; p=D(18500)
Q.append(fill('gioi',31,'Để làm một chiếc bánh cần 0,35 kg bột. Làm 24 chiếc bánh, bột giá 18 500 đồng một ki-lô-gam.',[B('Cần tất cả',b,'kg bột'),B('Tiền mua bột là',b*p,'đồng')],
 f'Số bột: 0,35 × 24 = {n(b)} kg. Tiền bột: {n(b)} × 18 500 = {n(b*p)} đồng.'))
x=D(12)/D('2.5')
Q.append(mc('gioi',31,'Tìm x biết x × 2,5 = 12. Giá trị của x là:',[n(x),'30','9,5','0,48'],0,
 f'x = 12 : 2,5 = {n(x)}. Kiểm tra: {n(x)} × 2,5 = 12.'))
va,vb,t=D('48.5'),D(52),D('2.5')
Q.append(fill('gioi',31,'Xe A đi với vận tốc 48,5 km một giờ, xe B đi với vận tốc 52 km một giờ. Cả hai xe cùng đi trong 2,5 giờ.',[B('Xe A đi được',va*t,'km'),B('Xe B đi được',vb*t,'km'),B('Xe B đi nhiều hơn xe A',vb*t-va*t,'km')],
 f'Xe A: 48,5 × 2,5 = {n(va*t)} km. Xe B: 52 × 2,5 = {n(vb*t)} km. Hiệu: {n(vb*t)} − {n(va*t)} = {n(vb*t-va*t)} km.'))
Q.append(tf('gioi',31,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('(3,5 + 1,5) × 2 = 3,5 + 1,5 × 2.',False),('4,2 × 0,5 = 4,2 : 2.',True),('8,4 : 0,2 = 8,4 × 5.',True),('25,6 : 6,4 = 4.',True)],
 'a) Sai: (3,5 + 1,5) × 2 = 10 còn 3,5 + 1,5 × 2 = 6,5. b) Đúng: nhân với 0,5 giống chia cho 2. c) Đúng: chia cho 0,2 giống nhân với 5. d) Đúng: 6,4 × 4 = 25,6.'))
write6(3,Q)
