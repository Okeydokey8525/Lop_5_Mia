from g4lib import *
Q=[]
# ===== TRUNG BÌNH =====
Q.append(fill('tb',23,'Tính nhẩm (nhân với 10; 100; 1 000).',[B('4,7 × 10 =',D('4.7')*10),B('0,35 × 100 =',D('0.35')*100),B('2,08 × 1 000 =',D('2.08')*1000)],
 'Nhân một số thập phân với 10; 100; 1 000;… ta chuyển dấu phẩy sang bên phải một; hai; ba;… chữ số (viết thêm chữ số 0 nếu cần): 4,7 × 10 = 47; 0,35 × 100 = 35; 2,08 × 1 000 = 2 080.'))
x=D('47.5'); r=x*D('0.1')
Q.append(mc('tb',23,f'Kết quả của phép tính <b>{n(x)} × 0,1</b> là:',['475',n(r),'0,475','47,05'],1,
 f'Nhân một số thập phân với 0,1 thì chuyển dấu phẩy sang bên trái một chữ số: {n(x)} × 0,1 = {n(r)}.'))
Q.append(fill('tb',23,'Tính nhẩm (chia cho 10; 100; 1 000).',[B('56,3 : 10 =',D('56.3')/10),B('0,8 : 100 =',D('0.8')/100),B('341 : 1 000 =',D(341)/1000)],
 'Chia một số thập phân cho 10; 100; 1 000;… ta chuyển dấu phẩy sang bên trái một; hai; ba;… chữ số (viết thêm chữ số 0 nếu cần): 56,3 : 10 = 5,63; 0,8 : 100 = 0,008; 341 : 1 000 = 0,341.'))
x=D('6.3'); r=x/D('0.01')
Q.append(mc('tb',23,f'Kết quả của phép tính <b>{n(x)} : 0,01</b> là:',['0,063',n(r),'63','6 300'],1,
 f'Chia một số thập phân cho 0,01 thì chuyển dấu phẩy sang bên phải hai chữ số: {n(x)} : 0,01 = {n(r)}.'))
Q.append(fill('tb',23,'Số?',[B('10,4 mm =',D('10.4')/10,'cm'),B('12,6 cm =',D('12.6')/100,'m'),B('3,7 m =',D('3.7')/1000,'km')],
 '1 cm = 10 mm nên 10,4 mm = 10,4 : 10 = 1,04 cm. 1 m = 100 cm nên 12,6 cm = 12,6 : 100 = 0,126 m. 1 km = 1 000 m nên 3,7 m = 3,7 : 1 000 = 0,0037 km.'))
ch,tay=D('24.8'),D('0.1'); r=ch/tay
Q.append(mc('tb',23,f'Mỗi tờ giấy dày {n(tay)} mm. Một chồng giấy dày {n(ch)} mm có tất cả bao nhiêu tờ giấy?',['2,48 tờ','24,8 tờ',n(r)+' tờ','2 480 tờ'],2,
 f'Số tờ giấy: {n(ch)} : {n(tay)} = {n(r)} (tờ). Chia cho 0,1 thì chuyển dấu phẩy sang bên phải một chữ số.'))
Q.append(fill('tb',23,'Số?',[B('23,45 kg =',D('23.45')*1000,'g'),B('6,89 l =',D('6.89')*1000,'ml'),B('3,5 tạ =',D('3.5')*10,'yến')],
 '1 kg = 1 000 g nên 23,45 kg = 23 450 g. 1 l = 1 000 ml nên 6,89 l = 6 890 ml. 1 tạ = 10 yến nên 3,5 tạ = 35 yến.'))
Q.append(mc('tb',23,'Đổi 0,5 kg ra gam, ta được:',['5 g','50 g','500 g','5 000 g'],2,
 '1 kg = 1 000 g nên 0,5 kg = 0,5 × 1 000 = 500 g.'))
t=[(D('3.5'),D(10),D(35),'×'),(D('4.2'),D(100),D('0.5'),':'),(D('0.8'),D(100),D(70),'×')]
def val(x,y,o): return x*y if o=='×' else x/y
Q.append(fill('tb',23,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL(f'{n(x)} {o} {n(y)}',cmp(val(x,y,o),z),n(z)) for x,y,z,o in t],
 '; '.join(f'{n(x)} {o} {n(y)} = {n(val(x,y,o))}, mà {n(val(x,y,o))} {cmp(val(x,y,o),z)} {n(z)}' for x,y,z,o in t)+'.'))
Q.append(mc('tb',23,'Một chai nước có 0,25 l. Số mi-li-lít nước trong chai là:',['25 ml','250 ml','2 500 ml','2,5 ml'],1,
 '1 l = 1 000 ml nên 0,25 l = 0,25 × 1 000 = 250 ml.'))
# ===== KHÁ =====
v=D('10.8'); s1=v/100; s2=s1/D('0.01'); s3=s2*D('0.01'); s4=s3*100
Q.append(fill('kha',23,'Cho số 10,8. Thực hiện liên tiếp các phép tính sau, điền kết quả mỗi bước: 10,8 : 100 → ? : 0,01 → ? × 0,01 → ? × 100 → ?',[B('10,8 : 100 =',s1),B('Rồi chia cho 0,01 được',s2),B('Rồi nhân với 0,01 được',s3),B('Rồi nhân với 100 được',s4)],
 f'10,8 : 100 = {n(s1)} (dấu phẩy sang trái 2 chữ số). {n(s1)} : 0,01 = {n(s2)} (dấu phẩy sang phải 2 chữ số). {n(s2)} × 0,01 = {n(s3)} (sang trái 2 chữ số). {n(s3)} × 100 = {n(s4)} (sang phải 2 chữ số).'))
tong=D('937.8'); m1=tong/10; m2=m1*25
Q.append(fill('kha',22,'Một chiếc máy xúc lớn xúc 10 lần được 937,8 tấn quặng, mỗi lần xúc được lượng quặng như nhau.',[B('Trung bình mỗi lần xúc được',m1,'tấn quặng'),B('Xúc 25 lần được',m2,'tấn quặng')],
 f'Mỗi lần xúc: 937,8 : 10 = {n(m1)} tấn. 25 lần xúc: {n(m1)} × 25 = {n(m2)} tấn.'))
Q.append(tf('kha',23,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('0,5 × 0,1 = 0,05.',True),('3,6 : 0,1 = 0,36.',False),('0,9 : 0,3 = 3.',True),('7,2 × 0,01 = 7,2 : 100.',True)],
 'a) Đúng: 5 × 1 = 5 và có hai chữ số ở phần thập phân nên 0,05. b) Sai: chia cho 0,1 thì chuyển dấu phẩy sang phải một chữ số, 3,6 : 0,1 = 36. c) Đúng: 0,9 : 0,3 = 9 : 3 = 3. d) Đúng: nhân với 0,01 và chia cho 100 đều là chuyển dấu phẩy sang trái hai chữ số, cùng bằng 0,072.'))
Q.append(mc('kha',23,'Chia đều 0,3 l giấm vào 10 ống nghiệm. Mỗi ống nghiệm có bao nhiêu lít giấm?',['3 l','0,3 l','0,03 l','0,003 l'],2,
 'Mỗi ống: 0,3 : 10 = 0,03 (l). Chia cho 10 thì chuyển dấu phẩy sang bên trái một chữ số, viết thêm chữ số 0.'))
ch,td=D(12),D('0.08'); s1=ch/td; s2=td*24
Q.append(fill('kha',22,'Mỗi tờ giấy mỏng dày 0,08 mm.',[B('Một chồng giấy dày 12 mm có',s1,'tờ'),B('24 tờ giấy xếp chồng lên nhau dày',s2,'mm')],
 f'Số tờ giấy: 12 : 0,08 = 1 200 : 8 = {n(s1)} tờ. Độ dày của 24 tờ: 0,08 × 24 = {n(s2)} mm.'))
a=[('4,98 + 15,7',D('4.98')+D('15.7')),('52 − 4,91',D(52)-D('4.91')),('0,73 × 6,5',D('0.73')*D('6.5')),('104,89 : 8,5',D('104.89')/D('8.5'))]
Q.append(fill('kha',24,'Tính.',[B(e+' =',v) for e,v in a],
 '; '.join(f'{e} = {n(v)}' for e,v in a)+'. Với 104,89 : 8,5, chuyển dấu phẩy của cả hai số sang phải một chữ số được 1 048,9 : 85 = 12,34.'))
ex=[('3,14 × 0,1',D('3.14')*D('0.1')),('3,14 × 100',D('3.14')*100),('31,4 : 10',D('31.4')/10),('314 : 0,001',D(314)/D('0.001'))]
ex.sort(key=lambda t:t[1])
Q.append(order('kha',23,'Tính nhẩm rồi sắp xếp các phép tính sau theo thứ tự kết quả từ bé đến lớn.',[e for e,_ in ex],'<',
 'Kết quả: '+'; '.join(f'{e} = {n(v)}' for e,v in ex)+'. Sắp xếp từ bé đến lớn được thứ tự như trên.'))
Q.append(mc('kha',21,'Biết 36 × 24 = 864. Không thực hiện phép tính, hãy cho biết <b>3,6 × 2,4</b> bằng bao nhiêu?',['86,4','8,64','0,864','864'],1,
 '3,6 và 2,4 mỗi số có một chữ số ở phần thập phân, tất cả hai chữ số. Giữ nguyên các chữ số của 864 rồi tách hai chữ số ở phần thập phân kể từ phải sang trái: 8,64.'))
# ===== GIỎI =====
kg=D('2.7'); a1=kg*D('0.1'); a2=kg*10; a3=kg*D('0.01')
Q.append(fill('gioi',23,'Một thanh nhôm dài 1 m nặng 2,7 kg. Cùng loại nhôm đó, thanh nhôm nặng bao nhiêu nếu dài:',[B('0,1 m thì nặng',a1,'kg'),B('10 m thì nặng',a2,'kg'),B('0,01 m thì nặng',a3,'kg')],
 f'Cùng một loại nhôm thì khối lượng tỉ lệ với chiều dài. Thanh 0,1 m: 2,7 × 0,1 = {n(a1)} kg. Thanh 10 m: 2,7 × 10 = {n(a2)} kg. Thanh 0,01 m: 2,7 × 0,01 = {n(a3)} kg.'))
v1,v2=D('12.5'),D('3.5'); t1=v1/D('0.1'); t2=(v2*10)/D('0.1')
Q.append(fill('gioi',23,'Mỗi tờ giấy trong quyển vở dày 0,1 mm. Quyển vở thứ nhất dày 12,5 mm. Chồng vở thứ hai dày 3,5 cm.',[B('Quyển vở thứ nhất có',t1,'tờ giấy'),B('Chồng thứ hai có',t2,'tờ giấy')],
 f'Quyển thứ nhất: 12,5 : 0,1 = {n(t1)} tờ. Đổi 3,5 cm = 35 mm nên chồng thứ hai có 35 : 0,1 = {n(t2)} tờ.'))
s=D('1.32')+D('3.48'); q=D('8.16')/s; h=D('0.34')/2; r=q-h
Q.append(fill('gioi',24,'Tính giá trị của biểu thức 8,16 : (1,32 + 3,48) − 0,34 : 2 theo từng bước.',[B('1,32 + 3,48 =',s),B('8,16 : '+n(s)+' =',q),B('Giá trị của biểu thức là',r)],
 f'Làm trong ngoặc trước: 1,32 + 3,48 = {n(s)}. Chia: 8,16 : {n(s)} = {n(q)}. Tính 0,34 : 2 = {n(h)}. Trừ: {n(q)} − {n(h)} = {n(r)}.'))
m=[D('15.4'),D('22.1'),D('12')]; tm=sum(m); tbm=tm/3; m2=[D('15.6'),D('18.9'),D('12.3')]; tb2=sum(m2)/3
Q.append(fill('gioi',24,'Một trạm đo mưa đo ba lần mỗi tháng. Tháng Một đo được 15,4 mm; 22,1 mm; 12 mm. Tháng Hai đo được 15,6 mm; 18,9 mm; 12,3 mm. Lượng mưa trung bình bằng tổng ba lần đo chia cho 3.',[B('Tổng ba lần đo tháng Một là',tm,'mm'),B('Lượng mưa trung bình tháng Một là',tbm,'mm'),B('Lượng mưa trung bình tháng Hai là',tb2,'mm')],
 f'Tháng Một: 15,4 + 22,1 + 12 = {n(tm)} mm, trung bình {n(tm)} : 3 = {n(tbm)} mm. Tháng Hai: 15,6 + 18,9 + 12,3 = {n(sum(m2))} mm, trung bình {n(sum(m2))} : 3 = {n(tb2)} mm.'))
Q.append(tf('gioi',24,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('(5,3 + 4,7) × 0,1 = 5,3 × 0,1 + 4,7 × 0,1.',True),('2,5 × 6,1 = 6,1 × 2,5.',True),('(15 × 6) × 0,25 = 15 × (6 × 0,25).',True),('3,2 × 0,5 = 3,2 × 5.',False)],
 'a) Đúng: nhân một tổng với một số thì bằng tổng các tích, cả hai vế đều bằng 1. b) Đúng: tính chất giao hoán của phép nhân. c) Đúng: tính chất kết hợp của phép nhân, cả hai vế đều bằng 22,5. d) Sai: 3,2 × 0,5 = 1,6 còn 3,2 × 5 = 16.'))
a=D('2.5')*D('3.7')*4; b=D('0.56')*D('4.7')+D('5.3')*D('0.56'); c=D('6.84')*D('0.2')*5
Q.append(fill('gioi',24,'Tính bằng cách thuận tiện.',[B('2,5 × 3,7 × 4 =',a),B('0,56 × 4,7 + 5,3 × 0,56 =',b),B('6,84 × 0,2 × 5 =',c)],
 f'2,5 × 3,7 × 4 = (2,5 × 4) × 3,7 = 10 × 3,7 = {n(a)}. 0,56 × 4,7 + 5,3 × 0,56 = 0,56 × (4,7 + 5,3) = 0,56 × 10 = {n(b)}. 6,84 × 0,2 × 5 = 6,84 × (0,2 × 5) = 6,84 × 1 = {n(c)}.'))
write(6,Q)
