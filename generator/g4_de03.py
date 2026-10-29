from g4lib import *
Q=[]
# ===== TRUNG BÌNH =====
w,k=D('0.35'),5; r=w*k
Q.append(mc('tb',21,f'Mỗi chiếc bánh nặng {n(w)} kg. Mẹ làm {k} chiếc bánh như vậy. Tất cả các chiếc bánh nặng:',['0,175 kg',n(r)+' kg','17,5 kg','1,05 kg'],1,
 f'Khối lượng {k} chiếc bánh: {n(w)} × {k} = {n(r)} (kg). Có hai chữ số ở phần thập phân của thừa số nên tích cũng có hai chữ số ở phần thập phân (1,75).'))
a=[(D('0.6'),5),(D('1.25'),8),(D('2.4'),7)]
Q.append(fill('tb',21,'Đặt tính rồi tính.',[B(f'{n(x)} × {y} =',x*y) for x,y in a],
 'Nhân như nhân hai số tự nhiên rồi dùng dấu phẩy tách ở tích bấy nhiêu chữ số kể từ phải sang trái như phần thập phân của thừa số. '+'; '.join(f'{n(x)} × {y} = {n(x*y)}' for x,y in a)+'.'))
l,k=D('4.8'),6; r=l/k
Q.append(mc('tb',22,f'Mẹ chia đều {n(l)} l sữa vào {k} chai. Mỗi chai đựng:',[n(r)+' l','8 l','0,08 l','1,2 l'],0,
 f'Mỗi chai đựng: {n(l)} : {k} = {n(r)} (l). Chia phần nguyên 4 : 6 được 0, viết 0 rồi viết dấu phẩy, chia tiếp 48 : 6 = 8.'))
a=[(D('7.5'),5),(D('9.36'),6),(D('14.4'),12)]
Q.append(fill('tb',22,'Đặt tính rồi tính.',[B(f'{n(x)} : {y} =',x/y) for x,y in a],
 'Chia phần nguyên rồi viết dấu phẩy vào thương, chia tiếp các chữ số ở phần thập phân. '+'; '.join(f'{n(x)} : {y} = {n(x/y)}' for x,y in a)+'.'))
w,k=D('1.5'),4; r=w*k
Q.append(mc('tb',21,f'Một mẻ bánh cần {n(w)} kg bột. Làm {k} mẻ bánh như vậy thì cần bao nhiêu ki-lô-gam bột?',['5,5 kg',n(r)+' kg','60 kg','0,6 kg'],1,
 f'Số bột cần dùng: {n(w)} × {k} = {n(r)} (kg).'))
a=[(D('1.5'),D('2.4')),(D('0.8'),D('0.5')),(D('2.5'),D('0.6'))]
Q.append(fill('tb',21,'Đặt tính rồi tính (nhân hai số thập phân).',[B(f'{n(x)} × {n(y)} =',x*y) for x,y in a],
 'Nhân như nhân hai số tự nhiên, rồi đếm tất cả chữ số ở phần thập phân của hai thừa số để tách ở tích. '+'; '.join(f'{n(x)} × {n(y)} = {n(x*y)}' for x,y in a)+'.'))
v,k=D(26),8; r=v/k
Q.append(mc('tb',22,f'Để may {k} bộ quần áo như nhau cần {n(v)} m vải. Để may một bộ quần áo cần bao nhiêu mét vải?',['3,25 m','3,2 m','3,5 m','0,325 m'],0,
 f'Số mét vải may một bộ: {n(v)} : {k} = {n(r)} (m). Phép chia này còn dư nên ta viết dấu phẩy vào thương và viết thêm chữ số 0 vào số dư để chia tiếp.'))
Q.append(fill('tb',23,'Tính nhẩm.',[B('2,5 × 10 =',D('2.5')*10),B('0,38 × 100 =',D('0.38')*100),B('45 : 10 =',D(45)/10)],
 'Nhân với 10; 100;… thì chuyển dấu phẩy sang bên phải một; hai;… chữ số: 2,5 × 10 = 25; 0,38 × 100 = 38. Chia cho 10 thì chuyển dấu phẩy sang bên trái một chữ số: 45 : 10 = 4,5.'))
x,k=D('1.2'),4; r=x/k
Q.append(mc('tb',22,f'Kết quả của phép tính <b>{n(x)} : {k}</b> là:',[n(r),'3','0,03','0,48'],0,
 f'Chia 1,2 cho 4: viết 1,2 thành 1,20 rồi chia, được {n(r)}. Kiểm tra: {n(r)} × 4 = {n(x)}.'))
t=[(D('0.5'),D(6),D(3),'×'),(D('4.8'),D(4),D('1.5'),':'),(D('2.5'),D('2.5'),D(6),'×')]
def val(x,y,o): return x*y if o=='×' else x/y
Q.append(fill('tb',21,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL(f'{n(x)} {o} {n(y)}',cmp(val(x,y,o),z),n(z)) for x,y,z,o in t],
 '; '.join(f'{n(x)} {o} {n(y)} = {n(val(x,y,o))}, mà {n(val(x,y,o))} {cmp(val(x,y,o),z)} {n(z)}' for x,y,z,o in t)+'.'))
# ===== KHÁ =====
kg1,l1=D('3.6'),D('2.4'); r1=kg1/l1; r2=D('0.75')/D('0.25')
Q.append(fill('kha',22,'Nhào 3,6 kg bột mì cần 2,4 l nước. Một chai sữa đựng 0,75 l, mỗi cốc đựng 0,25 l.',[B('Mỗi lít nước nhào được',r1,'kg bột'),B('Chai sữa rót được đầy',r2,'cốc')],
 f'Mỗi lít nước nhào được: 3,6 : 2,4 = 36 : 24 = {n(r1)} kg bột. Số cốc: 0,75 : 0,25 = 75 : 25 = {n(r2)} cốc. Khi chia cho số thập phân, ta chuyển dấu phẩy của cả số bị chia và số chia sang phải cùng số chữ số.'))
a=[(D('4.3'),D('3.6')),(D('6.8'),D('0.52')),(D('7.5'),D('3.4'))]
Q.append(fill('kha',21,'Tính.',[B(f'{n(x)} × {n(y)} =',x*y) for x,y in a],
 '; '.join(f'{n(x)} × {n(y)} = {n(x*y)}' for x,y in a)+'. Đếm tất cả chữ số ở phần thập phân của hai thừa số để tách ở tích: 4,3 × 3,6 có 2 chữ số, 6,8 × 0,52 có 3 chữ số, 7,5 × 3,4 có 2 chữ số (25,50 = 25,5).'))
Q.append(tf('kha',22,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('2,5 : 0,5 = 5.',True),('0,6 : 0,2 = 0,3.',False),('1,2 × 0,5 = 0,6.',True),('4,5 : 1,5 = 0,3.',False)],
 'a) Đúng: 25 : 5 = 5. b) Sai: 0,6 : 0,2 = 6 : 2 = 3. c) Đúng: 12 × 5 = 60, có hai chữ số ở phần thập phân nên 0,60 = 0,6. d) Sai: 4,5 : 1,5 = 45 : 15 = 3.'))
tt,rate,kgs=D(75),D('0.64'),D(75); r=rate*kgs
Q.append(mc('kha',21,'Xay xát 1 kg thóc được 0,64 kg gạo. Cô Bình xay xát 75 kg thóc loại đó thì được bao nhiêu ki-lô-gam gạo?',['4,8 kg',n(r)+' kg','480 kg','0,48 kg'],1,
 f'Số ki-lô-gam gạo: 0,64 × 75 = {n(r)} (kg).'))
tot,k=D('7.56'),6; r=tot/k; r2=r*2
Q.append(fill('kha',22,'Mẹ chia đều 7,56 kg đường vào 6 hộp.',[B('Mỗi hộp đựng',r,'kg đường'),B('Hai hộp đựng',r2,'kg đường')],
 f'Mỗi hộp: 7,56 : 6 = {n(r)} kg. Hai hộp: {n(r)} × 2 = {n(r2)} kg.'))
bot,k=D('0.15'),12; r1=bot*k; r2=D('2.7')/bot
Q.append(fill('kha',21,'Mỗi chiếc bánh cần 0,15 kg bột.',[B('12 chiếc bánh cần',r1,'kg bột'),B('Có 2,7 kg bột thì làm được',r2,'chiếc bánh')],
 f'12 chiếc bánh cần: 0,15 × 12 = {n(r1)} kg. Với 2,7 kg bột làm được: 2,7 : 0,15 = 270 : 15 = {n(r2)} chiếc bánh.'))
ex=[('2,4 × 2,5',D('2.4')*D('2.5')),('7,5 : 2,5',D('7.5')/D('2.5')),('1,5 × 3,2',D('1.5')*D('3.2')),('9 : 1,8',D(9)/D('1.8'))]
ex.sort(key=lambda t:t[1])
Q.append(order('kha',22,'Mẹ ghi thời gian nướng các khay bánh (đơn vị: phút) bằng những phép tính sau. Tính rồi sắp xếp theo thứ tự từ ngắn đến dài.',[e for e,_ in ex],'<',
 'Kết quả: '+'; '.join(f'{e} = {n(v)}' for e,v in ex)+'. Sắp xếp từ bé đến lớn được thứ tự như trên.'))
v,k=D('1.25'),5; r=v/k
Q.append(mc('kha',22,f'Một chai nước cam {n(v)} l được rót đều vào {k} cốc. Mỗi cốc đựng:',[n(r)+' l','0,5 l','0,025 l','6,25 l'],0,
 f'Mỗi cốc đựng: {n(v)} : {k} = {n(r)} (l).'))
# ===== GIỎI =====
v,cs,gia=D(12),D('0.75'),18000; sc=v/cs; tien=sc*gia
Q.append(fill('gioi',22,'Cô Lan ép được 12 l nước cam, rót vào các chai nhỏ, mỗi chai đựng 0,75 l. Mỗi chai nước cam bán với giá 18 000 đồng.',[B('Rót được đầy',sc,'chai'),B('Bán hết số chai đó được',tien,'đồng')],
 f'Số chai: 12 : 0,75 = 1 200 : 75 = {n(sc)} chai. Số tiền: {n(sc)} × 18 000 = {n(tien)} đồng.'))
m1=D('1.25'); m2=m1+D('0.4'); m3=(m1+m2)/2; tong=m1+m2+m3
Q.append(fill('gioi',20,'Cửa hàng làm ba mẻ bánh. Mẻ một dùng 1,25 kg bột. Mẻ hai dùng nhiều hơn mẻ một 0,4 kg bột. Mẻ ba dùng số bột bằng một nửa tổng số bột của hai mẻ đầu.',[B('Mẻ hai dùng',m2,'kg bột'),B('Mẻ ba dùng',m3,'kg bột'),B('Cả ba mẻ dùng',tong,'kg bột')],
 f'Mẻ hai: 1,25 + 0,4 = {n(m2)} kg. Hai mẻ đầu: 1,25 + {n(m2)} = {n(m1+m2)} kg. Mẻ ba: {n(m1+m2)} : 2 = {n(m3)} kg. Cả ba mẻ: {n(m1+m2)} + {n(m3)} = {n(tong)} kg.'))
rong,dai=D('0.6'),D('2.4'); dt=rong*dai; tien=dt*1500000
Q.append(fill('gioi',21,'Mặt bàn bếp hình chữ nhật có chiều rộng 0,6 m và chiều dài 2,4 m. Người ta phủ đá lên mặt bàn, giá 1 500 000 đồng cho mỗi mét vuông.',[B('Diện tích mặt bàn là',dt,'m²'),B('Tiền phủ đá là',tien,'đồng')],
 f'Diện tích mặt bàn: 0,6 × 2,4 = {n(dt)} m². Tiền phủ đá: {n(dt)} × 1 500 000 = {n(tien)} đồng.'))
bot,k=D('4.5'),6; m=bot/k; m2=m+D('0.15')
Q.append(mc('gioi',22,'Có 4,5 kg bột mì chia đều cho 6 mẻ bánh. Sau đó cô thợ làm bánh thêm vào mỗi mẻ 0,15 kg bột. Bây giờ mỗi mẻ có bao nhiêu ki-lô-gam bột?',[n(m2)+' kg','0,6 kg','0,75 kg','1,5 kg'],0,
 f'Mỗi mẻ lúc đầu có: 4,5 : 6 = {n(m)} kg. Sau khi thêm: {n(m)} + 0,15 = {n(m2)} kg.'))
c5,l5=D(5),D('2.1'); r1=l5/c5; r2=D('4.2')/r1
Q.append(fill('gioi',22,'Ép 5 kg cam được 2,1 l nước cam. Mỗi ki-lô-gam cam ép được lượng nước như nhau.',[B('Mỗi ki-lô-gam cam ép được',r1,'l nước'),B('Muốn ép được 4,2 l nước cam cần',r2,'kg cam')],
 f'Mỗi ki-lô-gam cam ép được: 2,1 : 5 = {n(r1)} l. Để ép 4,2 l cần: 4,2 : {n(r1)} = 420 : 42 = {n(r2)} kg cam.'))
a=[(D('7.2')/4,'× 4 = 7,2'),(D(15)/D('2.5'),'sao cho 15 : ? = 2,5'),(D('3.2')*D('0.5'),': 0,5 = 3,2')]
Q.append(fill('gioi',22,'Tìm số thích hợp.',[B('',a[0][0],'× 4 = 7,2'),B('15 :',a[1][0],'= 2,5'),B('',a[2][0],': 0,5 = 3,2')],
 f'Tìm thừa số chưa biết: 7,2 : 4 = {n(a[0][0])}. Tìm số chia: 15 : 2,5 = {n(a[1][0])}. Tìm số bị chia: 3,2 × 0,5 = {n(a[2][0])}.'))
write(3,Q)
