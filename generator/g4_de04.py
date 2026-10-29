from g4lib import *
Q=[]
# ===== TRUNG BÌNH =====
a,b=D('4.43'),D('4.16'); r=a-b
Q.append(mc('tb',20,f'Năm ngoái Nam nhảy xa được {n(b)} m, năm nay Nam nhảy xa được {n(a)} m. Năm nay Nam nhảy xa hơn năm ngoái:',['0,37 m',n(r)+' m','0,17 m','8,59 m'],1,
 f'Muốn biết hơn bao nhiêu mét ta thực hiện phép trừ: {n(a)} − {n(b)} = {n(r)} (m).'))
s,c=D('3.5'),D('2.75'); r1=s+c; d1,d2=D('2.4'),D('1.35'); r2=d1+d2
Q.append(fill('tb',19,'Số?',[B('Việt chạy buổi sáng 3,5 km, buổi chiều 2,75 km. Cả ngày Việt chạy',r1,'km'),B('Nhà cách trường 2,4 km, trường cách bưu điện 1,35 km. Từ nhà qua trường đến bưu điện dài',r2,'km')],
 f'Cả ngày Việt chạy: 3,5 + 2,75 = {n(r1)} km. Từ nhà đến bưu điện: 2,4 + 1,35 = {n(r2)} km.'))
v,t=D('36.5'),2; r=v*t
Q.append(mc('tb',21,f'Một xe máy mỗi giờ đi được {n(v)} km. Hỏi trong {t} giờ xe máy đó đi được bao nhiêu ki-lô-mét?',['38,5 km','7,3 km',n(r)+' km','730 km'],2,
 f'Quãng đường xe máy đi được: {n(v)} × {t} = {n(r)} (km).'))
v1,n1=D('15.8'),D('14.95'); r1=v1-n1; m1,m2=D('3.25'),D('2.8'); r2=m1-m2
Q.append(fill('tb',20,'Số?',[B('Việt chạy 100 m hết 15,8 giây, Nam hết 14,95 giây. Nam chạy nhanh hơn Việt',r1,'giây'),B('Mai nhảy xa 3,25 m, Mi nhảy xa 2,8 m. Mai nhảy xa hơn Mi',r2,'m')],
 f'Nam nhanh hơn: 15,8 − 14,95 = {n(r1)} giây. Mai nhảy xa hơn: 3,25 − 2,8 = {n(r2)} m. Viết 15,8 thành 15,80 và 2,8 thành 2,80 để đặt tính.'))
s,t=D('45.6'),4; r=s/t
Q.append(mc('tb',22,f'Một người đi xe đạp đi được {n(s)} km trong {t} giờ. Trung bình mỗi giờ người đó đi được:',[n(r)+' km','1,14 km','114 km','41,6 km'],0,
 f'Trung bình mỗi giờ đi được: {n(s)} : {t} = {n(r)} (km).'))
v=D('12.5'); r1=v*3; r2=v*D('1.2')
Q.append(fill('tb',21,'Một xe đạp mỗi giờ đi được 12,5 km.',[B('Trong 3 giờ xe đạp đi được',r1,'km'),B('Trong 1,2 giờ xe đạp đi được',r2,'km')],
 f'3 giờ: 12,5 × 3 = {n(r1)} km. 1,2 giờ: 12,5 × 1,2 = {n(r2)} km (12,5 có một chữ số, 1,2 có một chữ số ở phần thập phân nên tích có hai chữ số: 15,00 = 15).'))
a,b=D('12.5'),D('8.75'); r=a+b
Q.append(mc('tb',19,f'Chặng đua thứ nhất dài {n(a)} km, chặng đua thứ hai dài {n(b)} km. Cả hai chặng đua dài:',['20,25 km','21,25 km','20,75 km','212,5 km'],1,
 f'Tổng độ dài hai chặng: {n(a)} + {n(b)} = {n(r)} (km). Viết 12,5 thành 12,50 để đặt tính.'))
a=[(D('42.5'),5),(D(100),8),(D(63),D('4.5'))]
Q.append(fill('tb',22,'Đặt tính rồi tính.',[B(f'{n(x)} : {n(y)} =',x/d(y)) for x,y in a],
 '; '.join(f'{n(x)} : {n(y)} = {n(x/d(y))}' for x,y in a)+'. Với 63 : 4,5, chuyển dấu phẩy của cả hai số sang phải một chữ số được 630 : 45 = 14.'))
Q.append(mc('tb',23,'Kết quả của phép tính <b>3,75 × 100</b> là:',['0,0375','37,5','375','3 750'],2,
 'Nhân một số thập phân với 100 thì chuyển dấu phẩy sang bên phải hai chữ số: 3,75 × 100 = 375.'))
t=[(D('12.5'),D('3.5'),D(16),'+'),(D(10),D('2.75'),D(7),'−'),(D('3.5'),D(2),D(8),'×')]
def val(x,y,o): return x+y if o=='+' else x-y if o=='−' else x*y
Q.append(fill('tb',21,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL(f'{n(x)} {o} {n(y)}',cmp(val(x,y,o),z),n(z)) for x,y,z,o in t],
 '; '.join(f'{n(x)} {o} {n(y)} = {n(val(x,y,o))}, mà {n(val(x,y,o))} {cmp(val(x,y,o),z)} {n(z)}' for x,y,z,o in t)+'.'))
# ===== KHÁ =====
v=D('84.5'); r1=v*D('1.2'); r2=v*D('2.5')
Q.append(fill('kha',21,'Một ô tô đi trên đường cao tốc, mỗi giờ đi được 84,5 km.',[B('Trong 1,2 giờ ô tô đi được',r1,'km'),B('Trong 2,5 giờ ô tô đi được',r2,'km')],
 f'1,2 giờ: 84,5 × 1,2 = {n(r1)} km. 2,5 giờ: 84,5 × 2,5 = {n(r2)} km. Ở mỗi phép nhân, hai thừa số có tất cả hai chữ số ở phần thập phân nên tích có hai chữ số ở phần thập phân rồi bỏ chữ số 0 thừa.'))
x0,them,con=D('4.5'),D('3.75'),D('2.25'); r1=x0+them; r2=r1-con
Q.append(fill('kha',20,'Bình xăng xe máy đang có 4,5 l. Bác Hai đổ thêm 3,75 l xăng. Sau chuyến đi, trong bình còn 2,25 l xăng.',[B('Sau khi đổ thêm, trong bình có',r1,'l xăng'),B('Chuyến đi đã dùng hết',r2,'l xăng')],
 f'Sau khi đổ: 4,5 + 3,75 = {n(r1)} l. Đã dùng: {n(r1)} − 2,25 = {n(r2)} l.'))
Q.append(tf('kha',22,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('2,5 km = 2 500 m.',True),('Đi 0,5 giờ với vận tốc 60 km/giờ thì được 30 km.',True),('Ô tô đi 90 km hết 1,5 giờ thì mỗi giờ đi được 60 km.',True),('12,5 : 0,25 = 5.',False)],
 'a) Đúng: 2,5 × 1 000 = 2 500 m. b) Đúng: 60 × 0,5 = 30 km. c) Đúng: 90 : 1,5 = 900 : 15 = 60 km. d) Sai: 12,5 : 0,25 = 1 250 : 25 = 50.'))
s,t=D(45),D('2.5'); r=s/t
Q.append(mc('kha',22,f'Một người đi xe máy được {n(s)} km hết {n(t)} giờ. Trung bình mỗi giờ người đó đi được bao nhiêu ki-lô-mét?',['1,8 km','18 km','112,5 km','0,18 km'],1,
 f'Mỗi giờ đi được: {n(s)} : {n(t)} = 450 : 25 = {n(r)} km.'))
vg=D('0.4'); r1=vg*D('7.5'); r2=vg*12
Q.append(fill('kha',21,'Một vòng sân vận động dài 0,4 km.',[B('Chạy 7,5 vòng được',r1,'km'),B('Chạy 12 vòng được',r2,'km')],
 f'7,5 vòng: 0,4 × 7,5 = {n(r1)} km. 12 vòng: 0,4 × 12 = {n(r2)} km.'))
s,v=D('78.6'),D('39.3'); r1=s/v; r2=v*3
Q.append(fill('kha',22,'Đoạn đường dài 78,6 km. Một xe máy mỗi giờ đi được 39,3 km.',[B('Xe máy đi hết đoạn đường đó trong',r1,'giờ'),B('Trong 3 giờ xe máy đi được',r2,'km')],
 f'Thời gian đi: 78,6 : 39,3 = 786 : 393 = {n(r1)} giờ. Quãng đường 3 giờ: 39,3 × 3 = {n(r2)} km.'))
ex=[('1,2 × 3',D('1.2')*3),('8,4 : 2',D('8.4')/2),('2,75 + 1,3',D('2.75')+D('1.3')),('9,6 − 5,3',D('9.6')-D('5.3'))]
ex.sort(key=lambda t:t[1])
Q.append(order('kha',21,'Thành tích nhảy xa (đơn vị: mét) của bốn bạn được ghi bằng những phép tính sau. Tính rồi sắp xếp theo thứ tự từ ngắn đến dài.',[e for e,_ in ex],'<',
 'Kết quả: '+'; '.join(f'{e} = {n(v)}' for e,v in ex)+'. Sắp xếp từ bé đến lớn được thứ tự như trên.'))
Q.append(mc('kha',23,'Kết quả của phép tính <b>3,14 × 1 000</b> là:',['31,4','314','3 140','0,00314'],2,
 'Nhân với 1 000 thì chuyển dấu phẩy sang bên phải ba chữ số, viết thêm chữ số 0 cho đủ: 3,14 × 1 000 = 3 140.'))
# ===== GIỎI =====
tg,vong=D('18.75'),3; m1=tg/vong; m2=m1*D('4.5')
Q.append(fill('gioi',22,'Một vận động viên chạy 3 vòng sân vận động hết 18,75 phút, các vòng chạy mất thời gian như nhau.',[B('Mỗi vòng chạy hết',m1,'phút'),B('Chạy 4,5 vòng hết',m2,'phút')],
 f'Mỗi vòng: 18,75 : 3 = {n(m1)} phút. 4,5 vòng: {n(m1)} × 4,5 = {n(m2)} phút.'))
va,vb,t=D('42.5'),D('38.5'),D('2.5'); sa=va*t; sb=vb*t; tot=sa+sb
Q.append(fill('gioi',21,'Hai xe xuất phát cùng một lúc từ hai địa điểm rồi đi ngược chiều nhau. Xe A đi 42,5 km mỗi giờ, xe B đi 38,5 km mỗi giờ. Sau 2,5 giờ:',[B('Xe A đi được',sa,'km'),B('Xe B đi được',sb,'km'),B('Hai xe đi được tất cả',tot,'km')],
 f'Xe A: 42,5 × 2,5 = {n(sa)} km. Xe B: 38,5 × 2,5 = {n(sb)} km. Cả hai xe: {n(sa)} + {n(sb)} = {n(tot)} km.'))
xang=D('2.1')*D('2.5'); tien=xang*24500
Q.append(fill('gioi',21,'Một xe máy đi 100 km hết 2,1 l xăng. Giá xăng là 24 500 đồng một lít. Xe máy đó đi quãng đường 250 km.',[B('Xe máy dùng hết',xang,'l xăng'),B('Tiền xăng phải trả là',tien,'đồng')],
 f'250 km gấp 2,5 lần 100 km nên dùng: 2,1 × 2,5 = {n(xang)} l xăng. Tiền xăng: {n(xang)} × 24 500 = {n(tien)} đồng.'))
s1=D('52.4')*D('3.5'); s2=D('62.6'); tong=s1+s2
Q.append(mc('gioi',21,'Một ô tô đi từ A đến B hết 3,5 giờ, mỗi giờ đi được 52,4 km. Sau đó ô tô đi tiếp từ B đến C dài 62,6 km. Quãng đường từ A đến C dài:',[n(tong)+' km','245,4 km','115 km','25,6 km'],0,
 f'Quãng đường AB: 52,4 × 3,5 = {n(s1)} km. Quãng đường AC: {n(s1)} + 62,6 = {n(tong)} km.'))
a=[D('12.45'),D('11.9'),D('12.05'),D('12.6')]; tot=sum(a); tb=tot/4
Q.append(fill('gioi',22,'Bốn bạn chạy tiếp sức, mỗi bạn chạy một chặng. Thời gian chạy của các bạn lần lượt là 12,45 giây; 11,9 giây; 12,05 giây; 12,6 giây.',[B('Cả đội chạy hết',tot,'giây'),B('Trung bình mỗi bạn chạy hết',tb,'giây')],
 f'Tổng thời gian: 12,45 + 11,9 + 12,05 + 12,6 = {n(tot)} giây. Trung bình mỗi bạn: {n(tot)} : 4 = {n(tb)} giây.'))
Q.append(tf('gioi',23,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('0,25 km = 250 m.',True),('Xe đi 12,5 km mỗi giờ thì trong 0,2 giờ đi được 2,5 km.',True),('18 : 0,6 = 30.',True),('Đi 3,5 giờ với vận tốc 40 km/giờ thì được 14 km.',False)],
 'a) Đúng: 0,25 × 1 000 = 250 m. b) Đúng: 12,5 × 0,2 = 2,5 km. c) Đúng: 18 : 0,6 = 180 : 6 = 30. d) Sai: 40 × 3,5 = 140 km.'))
write(4,Q)
