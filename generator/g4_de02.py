from g4lib import *
Q=[]
# ===== TRUNG BÌNH =====
a,b=D('2.5'),D('1.75'); r=a+b
Q.append(mc('tb',19,f'Mẹ mua {n(a)} kg cà chua và {n(b)} kg khoai tây. Mẹ đã mua tất cả bao nhiêu ki-lô-gam hai loại này?',['3,25 kg','4,25 kg','4,5 kg','42,5 kg'],1,
 f'Muốn biết tổng khối lượng ta thực hiện phép cộng: {n(a)} + {n(b)} = {n(r)} (kg). Viết {n(a)} thành 2,50 rồi đặt tính cho thẳng cột.'))
a=[(D('3.4'),D('2.6')),(D('0.75'),D('0.5')),(D('12.5'),D('7.35'))]
Q.append(fill('tb',19,'Đặt tính rồi tính.',[B(f'{n(x)} + {n(y)} =',x+y) for x,y in a],
 'Viết các số hạng sao cho các chữ số ở cùng hàng thẳng cột rồi cộng như cộng số tự nhiên. '+'; '.join(f'{n(x)} + {n(y)} = {n(x+y)}' for x,y in a)+'.'))
a,b=D('2.5'),D('1.2'); r=a-b
Q.append(mc('tb',20,f'Mai mua {n(a)} kg bột mì, đã dùng hết {n(b)} kg. Mai còn lại bao nhiêu ki-lô-gam bột mì?',['1,3 kg','3,7 kg','1,7 kg','13 kg'],0,
 f'Muốn biết còn lại bao nhiêu ta thực hiện phép trừ: {n(a)} − {n(b)} = {n(r)} (kg).'))
a=[(D('9.6'),D('4.8')),(D('15'),D('6.25')),(D('4.07'),D('1.9'))]
Q.append(fill('tb',20,'Đặt tính rồi tính.',[B(f'{n(x)} − {n(y)} =',x-y) for x,y in a],
 'Viết số trừ dưới số bị trừ sao cho các chữ số ở cùng hàng thẳng cột, viết thêm chữ số 0 vào phần thập phân khi cần. '+'; '.join(f'{n(x)} − {n(y)} = {n(x-y)}' for x,y in a)+'.'))
a,b=D('3.45'),D('1.8'); r=a+b
Q.append(mc('tb',19,f'Một quả dưa hấu nặng {n(a)} kg và một quả bưởi nặng {n(b)} kg. Cả hai quả nặng:',['5,25 kg','4,63 kg','5,15 kg','52,5 kg'],0,
 f'{n(a)} + {n(b)} = {n(a)} + 1,80 = {n(r)} (kg).'))
a=[(D('0.75'),6,'Mỗi gói đường nặng 0,75 kg. 6 gói đường nặng'),(D('1.25'),4,'Mỗi chai dầu ăn đựng 1,25 l. 4 chai dầu ăn đựng'),(D('0.35'),12,'Mỗi bó rau nặng 0,35 kg. 12 bó rau nặng')]
units=['kg','l','kg']
Q.append(fill('tb',21,'Mẹ đi chợ mua nhiều món. Số?',[B(t+':',x*y,u) for (x,y,t),u in zip(a,units)],
 'Nhân như nhân hai số tự nhiên rồi tách ở tích số chữ số thập phân bằng số chữ số ở phần thập phân của thừa số. '+'; '.join(f'{n(x)} × {y} = {n(x*y)}' for x,y,_ in a)+'.'))
p=60000; w=D('2.5'); r=p*w
Q.append(mc('tb',21,f'Nho giá {n(p)} đồng một ki-lô-gam. Mẹ mua {n(w)} kg nho thì phải trả bao nhiêu tiền?',['15 000 đồng','150 000 đồng','62 500 đồng','1 500 000 đồng'],1,
 f'Số tiền phải trả: {n(p)} × {n(w)} = {n(r)} đồng. (Có thể tính {n(p)} × 2 = 120 000 và {n(p)} : 2 = 30 000, cộng lại được {n(r)}.)'))
t=[(D('3.5'),D('2.4'),D('5.9'),'+'),(D('8.6'),D('3.25'),D('5'),'−'),(D('12.5'),D('4.8'),D('8'),'−')]
def val(x,y,o): return x+y if o=='+' else x-y
Q.append(fill('tb',20,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL(f'{n(x)} {o} {n(y)}',cmp(val(x,y,o),z),n(z)) for x,y,z,o in t],
 '; '.join(f'{n(x)} {o} {n(y)} = {n(val(x,y,o))}, mà {n(val(x,y,o))} {cmp(val(x,y,o),z)} {n(z)}' for x,y,z,o in t)+'.'))
g=D(25)-D('8.5'); h=D(5)-D('1.25')
Q.append(fill('tb',20,'Số?',[B('Nhà Lan có 25 kg gạo, đã dùng 8,5 kg. Còn lại',g,'kg gạo'),B('Một bao đường 5 kg, đã bán lẻ 1,25 kg. Còn lại',h,'kg đường')],
 f'Gạo còn lại: 25 − 8,5 = {n(g)} kg. Đường còn lại: 5 − 1,25 = {n(h)} kg. Viết số tự nhiên thành số thập phân (25 = 25,0 và 5 = 5,00) cho dễ đặt tính.'))
a,b=D('5'),D('1.75'); r=a-b
Q.append(mc('tb',20,f'Bình nước có {n(a)} l nước. Mai đã rót ra {n(b)} l. Trong bình còn lại:',['3,25 l','4,25 l','3,75 l','6,75 l'],0,
 f'Số lít nước còn lại: {n(a)} − {n(b)} = {n(r)} (l).'))
# ===== KHÁ =====
ca,th,rau=D('2.35'),D('1.8'),D('0.9'); s1=ca+th; s2=s1+rau
Q.append(fill('kha',19,'Mẹ mua 2,35 kg cá, 1,8 kg thịt và 0,9 kg rau.',[B('Cá và thịt nặng',s1,'kg'),B('Cả ba thứ nặng',s2,'kg')],
 f'Cá và thịt: 2,35 + 1,8 = {n(s1)} kg. Cả ba thứ: {n(s1)} + 0,9 = {n(s2)} kg.'))
tot,hu,bien=D(5),D('1.35'),D('0.75'); s1=tot-hu; s2=s1-bien
Q.append(fill('kha',20,'Một túi gạo nặng 5 kg. Mẹ lấy 1,35 kg đổ vào hũ rồi lấy thêm 0,75 kg biếu bà.',[B('Sau khi đổ vào hũ, túi còn',s1,'kg'),B('Sau khi biếu bà, túi còn',s2,'kg')],
 f'Sau khi đổ vào hũ: 5 − 1,35 = {n(s1)} kg. Sau khi biếu bà: {n(s1)} − 0,75 = {n(s2)} kg.'))
Q.append(tf('kha',21,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Chai nước cam 1,5 l rót vừa đủ 6 cốc, mỗi cốc 0,25 l.',True),('3,75 kg + 1,25 kg = 5 kg.',True),('10 − 6,35 = 3,75.',False),('Mua 2,5 kg táo, giá 40 000 đồng một ki-lô-gam thì phải trả 100 000 đồng.',True)],
 'a) Đúng: 0,25 × 6 = 1,5 l. b) Đúng: 3,75 + 1,25 = 5,00. c) Sai: 10,00 − 6,35 = 3,65. d) Đúng: 40 000 × 2,5 = 100 000 đồng.'))
xo=D(30000)*D('1.5'); ca_=D(25000)*2; ts=xo+ca_; tl=D(100000)-ts
Q.append(mc('kha',21,f'Hà có 100 000 đồng. Hà mua 1,5 kg xoài giá 30 000 đồng một ki-lô-gam và 2 kg cam giá 25 000 đồng một ki-lô-gam. Hà còn lại bao nhiêu tiền?',['55 000 đồng','45 000 đồng',f'{n(tl)} đồng','15 000 đồng'],2,
 f'Tiền xoài: 30 000 × 1,5 = {n(xo)} đồng. Tiền cam: 25 000 × 2 = {n(ca_)} đồng. Tổng: {n(ts)} đồng. Còn lại: 100 000 − {n(ts)} = {n(tl)} đồng.'))
bi,ca2=D(18000)*D('2.5'),D(15000)*D('3.2'); tong=bi+ca2
Q.append(fill('kha',21,'Bí đỏ giá 18 000 đồng một ki-lô-gam, cà rốt giá 15 000 đồng một ki-lô-gam. Mẹ mua 2,5 kg bí đỏ và 3,2 kg cà rốt.',[B('Tiền mua bí đỏ là',bi,'đồng'),B('Tiền mua cà rốt là',ca2,'đồng'),B('Mẹ phải trả tất cả',tong,'đồng')],
 f'Bí đỏ: 18 000 × 2,5 = {n(bi)} đồng. Cà rốt: 15 000 × 3,2 = {n(ca2)} đồng. Tổng cộng: {n(bi)} + {n(ca2)} = {n(tong)} đồng.'))
nam=D('36.45'); mai=nam-D('2.7'); viet=mai+D('1.95'); tg=nam+mai+viet
Q.append(fill('kha',20,'Nam cân nặng 36,45 kg. Mai nhẹ hơn Nam 2,7 kg. Việt nặng hơn Mai 1,95 kg.',[B('Mai nặng',mai,'kg'),B('Việt nặng',viet,'kg'),B('Cả ba bạn nặng',tg,'kg')],
 f'Mai: 36,45 − 2,7 = {n(mai)} kg. Việt: {n(mai)} + 1,95 = {n(viet)} kg. Cả ba bạn: 36,45 + {n(mai)} + {n(viet)} = {n(tg)} kg.'))
ex=[('1,25 × 4',D('1.25')*4),('8,2 − 3,75',D('8.2')-D('3.75')),('2,75 + 2,5',D('2.75')+D('2.5')),('12 : 4,8',D(12)/D('4.8'))]
ex.sort(key=lambda t:t[1])
Q.append(order('kha',21,'Mẹ ghi lại khối lượng các túi hàng bằng những phép tính sau. Tính rồi sắp xếp theo thứ tự từ nhẹ đến nặng.',[e for e,_ in ex],'<',
 'Kết quả: '+'; '.join(f'{e} = {n(v)}' for e,v in ex)+'. Sắp xếp từ bé đến lớn được thứ tự như trên.'))
w,k=D('0.45'),8; r=w*k
Q.append(mc('kha',21,f'Mỗi hộp bánh nặng {n(w)} kg. Mẹ mua {k} hộp bánh như vậy. Tất cả các hộp bánh nặng:',[n(r)+' kg','36 kg','0,36 kg','4,5 kg'],0,
 f'Khối lượng {k} hộp bánh: {n(w)} × {k} = {n(r)} (kg).'))
# ===== GIỎI =====
rau_,thit_,con=D(35500),D(89000),D(25500); spent=rau_+thit_; ban=spent+con
Q.append(fill('gioi',19,'Mẹ đi chợ mua rau hết 35 500 đồng, mua thịt hết 89 000 đồng và còn lại 25 500 đồng.',[B('Mẹ đã tiêu',spent,'đồng'),B('Lúc đầu mẹ có',ban,'đồng')],
 f'Số tiền đã tiêu: 35 500 + 89 000 = {n(spent)} đồng. Số tiền lúc đầu: {n(spent)} + 25 500 = {n(ban)} đồng.'))
b1=D('25.5'); b2=b1-D('1.8'); tt=b1+b2; con2=tt-D('17.85')
Q.append(fill('gioi',20,'Bao gạo thứ nhất nặng 25,5 kg. Bao gạo thứ hai nhẹ hơn bao thứ nhất 1,8 kg. Sau đó cửa hàng bán đi 17,85 kg gạo ở cả hai bao.',[B('Bao gạo thứ hai nặng',b2,'kg'),B('Hai bao gạo nặng',tt,'kg'),B('Sau khi bán, hai bao còn lại',con2,'kg')],
 f'Bao thứ hai: 25,5 − 1,8 = {n(b2)} kg. Hai bao: 25,5 + {n(b2)} = {n(tt)} kg. Sau khi bán: {n(tt)} − 17,85 = {n(con2)} kg.'))
A=D(35000)*D('2.4'); Bq=D(33500)*D('2.4'); ch=A-Bq
Q.append(mc('gioi',21,'Cùng mua 2,4 kg vải, cửa hàng A bán giá 35 000 đồng một ki-lô-gam, cửa hàng B bán giá 33 500 đồng một ki-lô-gam. Câu nào sau đây đúng?',[f'Mua ở cửa hàng A đắt hơn cửa hàng B {n(ch)} đồng.',f'Mua ở cửa hàng B đắt hơn cửa hàng A {n(ch)} đồng.','Mua ở cửa hàng A đắt hơn cửa hàng B 1 500 đồng.','Hai cửa hàng bán cùng một số tiền.'],0,
 f'Cửa hàng A: 35 000 × 2,4 = {n(A)} đồng. Cửa hàng B: 33 500 × 2,4 = {n(Bq)} đồng. Chênh lệch: {n(A)} − {n(Bq)} = {n(ch)} đồng nên cửa hàng A đắt hơn.'))
con3=D(20)-D('4.75')-D('6.5'); moi=con3/7
Q.append(fill('gioi',22,'Bình nước dung tích 20 l. Sáng dùng 4,75 l, trưa dùng 6,5 l. Số nước còn lại được chia đều vào 7 chai.',[B('Trong bình còn lại',con3,'l nước'),B('Mỗi chai đựng',moi,'l nước')],
 f'Nước còn lại: 20 − 4,75 − 6,5 = {n(con3)} l. Mỗi chai: {n(con3)} : 7 = {n(moi)} l.'))
tom=D(280000)*D('1.5'); muc=D(150000)*D('0.8'); thoi=D(600000)-tom-muc
Q.append(fill('gioi',21,'Mẹ mua 1,5 kg tôm giá 280 000 đồng một ki-lô-gam và 0,8 kg mực giá 150 000 đồng một ki-lô-gam. Mẹ đưa 600 000 đồng.',[B('Tiền mua tôm là',tom,'đồng'),B('Tiền mua mực là',muc,'đồng'),B('Người bán trả lại mẹ',thoi,'đồng')],
 f'Tôm: 280 000 × 1,5 = {n(tom)} đồng. Mực: 150 000 × 0,8 = {n(muc)} đồng. Cả hai: {n(tom+muc)} đồng. Tiền trả lại: 600 000 − {n(tom+muc)} = {n(thoi)} đồng.'))
Q.append(tf('gioi',19,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Tổng của 4,6 và 5,4 là một số tự nhiên.',True),('Hiệu của 12,5 và 12,05 bằng 0,45.',True),('0,25 × 4 = 1.',True),('0,7 + 0,3 = 0,10.',False)],
 'a) Đúng: 4,6 + 5,4 = 10. b) Đúng: 12,50 − 12,05 = 0,45. c) Đúng: 25 × 4 = 100 nên 0,25 × 4 = 1,00 = 1. d) Sai: 0,7 + 0,3 = 1,0 = 1, không phải 0,10.'))
write(2,Q)
