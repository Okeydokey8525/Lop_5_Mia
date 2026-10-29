from g4lib import *
Q=[]
# ===== TRUNG BÌNH =====
a=[(D('6.8'),D('9.7')),(D('5.34'),D('7.49')),(D('18.6'),D('8.72'))]
Q.append(fill('tb',19,'Đặt tính rồi tính.',[B(f'{n(x)} + {n(y)} =',x+y) for x,y in a],
 'Đặt tính sao cho các chữ số ở cùng hàng thẳng cột, cộng như cộng số tự nhiên rồi đặt dấu phẩy ở tổng thẳng cột với các dấu phẩy. '+'; '.join(f'{n(x)} + {n(y)} = {n(x+y)}' for x,y in a)+'.'))
x,y=D('12.5'),D('3.25'); r=x+y
Q.append(mc('tb',19,f'Kết quả của phép tính <b>{n(x)} + {n(y)}</b> là:',[n(r),'15,30','12,75',n(r*10)],0,
 f'Viết {n(x)} thành 12,50 cho cùng số chữ số ở phần thập phân rồi cộng: 12,50 + 3,25 = {n(r)}.'))
a=[(D('5.8'),D('3.9')),(D('17.96'),D('8.5')),(D('9'),D('3.5'))]
Q.append(fill('tb',20,'Đặt tính rồi tính.',[B(f'{n(x)} − {n(y)} =',x-y) for x,y in a],
 'Viết số trừ dưới số bị trừ sao cho các chữ số ở cùng hàng thẳng cột, trừ như trừ số tự nhiên rồi đặt dấu phẩy ở hiệu. '+'; '.join(f'{n(x)} − {n(y)} = {n(x-y)}' for x,y in a)+'. Khi cần có thể viết thêm chữ số 0 vào phần thập phân của số bị trừ.'))
x,y=D('45.2'),D('18.75'); r=x-y
Q.append(mc('tb',20,f'Kết quả của phép tính <b>{n(x)} − {n(y)}</b> là:',['27,55',n(r),'26,55','36,45'],1,
 f'Viết {n(x)} thành 45,20 rồi trừ: 45,20 − 18,75 = {n(r)}.'))
a=[(D('7.8'),6),(D('0.72'),50),(D('2.5'),4)]
Q.append(fill('tb',21,'Đặt tính rồi tính (nhân một số thập phân với một số tự nhiên).',[B(f'{n(x)} × {y} =',x*y) for x,y in a],
 'Nhân như nhân hai số tự nhiên, rồi đếm xem phần thập phân của thừa số có bao nhiêu chữ số thì dùng dấu phẩy tách ở tích bấy nhiêu chữ số kể từ phải sang trái. '+'; '.join(f'{n(x)} × {y} = {n(x*y)}' for x,y in a)+'.'))
x,y=D('3.2'),D('1.5'); r=x*y
Q.append(mc('tb',21,f'Kết quả của phép tính <b>{n(x)} × {n(y)}</b> là:',['48','0,48',n(r),'4,08'],2,
 f'Nhân 32 × 15 = 480. Cả hai thừa số có tất cả 2 chữ số ở phần thập phân nên tách ở tích hai chữ số kể từ phải sang trái: 4,80 = {n(r)}.'))
a=[(D('92.8'),4),(D('19.95'),19),(D('5.28'),4)]
Q.append(fill('tb',22,'Đặt tính rồi tính (chia một số thập phân cho một số tự nhiên).',[B(f'{n(x)} : {y} =',x/y) for x,y in a],
 'Chia phần nguyên trước, khi chia hết phần nguyên thì viết dấu phẩy vào thương rồi chia tiếp từng chữ số ở phần thập phân. '+'; '.join(f'{n(x)} : {y} = {n(x/y)}' for x,y in a)+'.'))
a=[(26,8),(15,8),(6,25)]
Q.append(fill('tb',22,'Chia một số tự nhiên cho một số tự nhiên mà thương là số thập phân.',[B(f'{x} : {y} =',D(x)/D(y)) for x,y in a],
 'Khi còn dư thì viết dấu phẩy vào bên phải thương, viết thêm chữ số 0 vào bên phải số dư rồi chia tiếp. '+'; '.join(f'{x} : {y} = {n(D(x)/D(y))}' for x,y in a)+'. Với 6 : 25, vì 6 bé hơn 25 nên viết 6 thành 6,0 rồi chia: được 0,24.'))
Q.append(fill('tb',23,'Tính nhẩm.',[B('9,63 × 10 =',D('9.63')*10),B('0,94 × 100 =',D('0.94')*100),B('20,7 : 10 =',D('20.7')/10)],
 'Nhân với 10; 100; 1 000;… ta chuyển dấu phẩy sang bên phải một; hai; ba;… chữ số: 9,63 × 10 = 96,3 và 0,94 × 100 = 94. Chia cho 10; 100; 1 000;… ta chuyển dấu phẩy sang bên trái: 20,7 : 10 = 2,07.'))
Q.append(mc('tb',23,'Kết quả của phép tính <b>5,1 × 0,1</b> là:',['51','0,51','5,01','0,051'],1,
 'Nhân một số thập phân với 0,1 thì chuyển dấu phẩy sang bên trái một chữ số: 5,1 × 0,1 = 0,51.'))
# ===== KHÁ =====
a=[(D('7.635'),D('6.249')),(D('23.58'),D('5.271')),(D('4.61'),D('8'))]
Q.append(fill('kha',19,'Đặt tính rồi tính.',[B(f'{n(x)} + {n(y)} =',x+y) for x,y in a],
 'Đặt tính thẳng hàng rồi cộng: '+'; '.join(f'{n(x)} + {n(y)} = {n(x+y)}' for x,y in a)+'. Với số tự nhiên 8 thì viết 8 thành 8,00 cho dễ đặt tính.'))
a=[(D('3.16'),41,'×'),(D('5.4'),39,'×'),(D('144.55'),D('3.5'),':')]
Q.append(fill('kha',21,'Tính.',[B(f'{n(x)} {o} {n(y)} =',x*d(y) if o=='×' else x/d(y)) for x,y,o in a],
 '3,16 × 41 = 129,56 (3,16 có hai chữ số ở phần thập phân). 5,4 × 39 = 210,6 (một chữ số ở phần thập phân). 144,55 : 3,5 = 41,3 (chuyển dấu phẩy ở cả số bị chia và số chia: 1 445,5 : 35 = 41,3).'))
Q.append(tf('kha',24,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('4,5 + 3,25 = 7,75.',True),('8,3 − 2,75 = 5,45.',False),('0,6 × 0,3 = 0,18.',True),('7,2 : 0,9 = 0,8.',False)],
 'a) Đúng. b) Sai: 8,30 − 2,75 = 5,55. c) Đúng: 6 × 3 = 18, có hai chữ số ở phần thập phân nên 0,18. d) Sai: 7,2 : 0,9 = 72 : 9 = 8.'))
Q.append(fill('kha',24,'Tính bằng cách thuận tiện.',[B('6 + 8,46 + 1,54 =',D('6')+D('8.46')+D('1.54')),B('4,8 + 0,73 + 3,2 =',D('4.8')+D('0.73')+D('3.2')),B('2,5 × 8,6 × 4 =',D('2.5')*D('8.6')*4)],
 'Dùng tính chất giao hoán và kết hợp: 6 + 8,46 + 1,54 = 6 + (8,46 + 1,54) = 6 + 10 = 16. 4,8 + 0,73 + 3,2 = (4,8 + 3,2) + 0,73 = 8 + 0,73 = 8,73. 2,5 × 8,6 × 4 = (2,5 × 4) × 8,6 = 10 × 8,6 = 86.'))
g=D(75000)/3; t=g*D('3.5'); b_=D(100000)-t
Q.append(fill('kha',22,'Mẹ của Mai mua 3 kg xoài hết 75 000 đồng. Cô Hà mua 3,5 kg xoài cùng loại đó, đưa cho người bán hàng 100 000 đồng.',
 [B('Giá tiền 1 kg xoài là',g,'đồng'),B('Cô Hà mua xoài hết',t,'đồng'),B('Người bán hàng trả lại cô Hà',b_,'đồng')],
 f'Giá 1 kg xoài: 75 000 : 3 = {n(g)} đồng. Cô Hà mua 3,5 kg hết {n(g)} × 3,5 = {n(t)} đồng. Tiền trả lại: 100 000 − {n(t)} = {n(b_)} đồng.'))
Q.append(fill('kha',23,'Số?',[B('79,6 × 0,01 =',D('79.6')*D('0.01')),B('534,28 : 100 =',D('534.28')/100),B('36,5 : 0,1 =',D('36.5')/D('0.1')),B('86,4 : 0,001 =',D('86.4')/D('0.001'))],
 'Nhân với 0,01 thì chuyển dấu phẩy sang trái 2 chữ số: 0,796. Chia cho 100 thì chuyển dấu phẩy sang trái 2 chữ số: 5,3428. Chia cho 0,1 thì chuyển dấu phẩy sang phải 1 chữ số: 365. Chia cho 0,001 thì chuyển dấu phẩy sang phải 3 chữ số: 86 400.'))
ex=[('0,73 × 6,5',D('0.73')*D('6.5')),('104,89 : 8,5',D('104.89')/D('8.5')),('4,98 + 15,7',D('4.98')+D('15.7')),('52 − 4,91',D('52')-D('4.91'))]
ex.sort(key=lambda t:t[1])
Q.append(order('kha',24,'Tính giá trị rồi sắp xếp các phép tính sau theo thứ tự kết quả từ bé đến lớn.',[e for e,_ in ex],'<',
 'Kết quả: '+'; '.join(f'{e} = {n(v)}' for e,v in ex)+'. Sắp xếp từ bé đến lớn được thứ tự như trên.'))
Q.append(mc('kha',21,'Biết 64 × 57 = 3 648. Không thực hiện phép tính, hãy cho biết <b>6,4 × 5,7</b> bằng bao nhiêu?',['364,8','36,48','3,648','0,3648'],1,
 '6,4 có một chữ số ở phần thập phân, 5,7 có một chữ số ở phần thập phân, tất cả hai chữ số. Giữ nguyên các chữ số của 3 648 rồi tách hai chữ số ở phần thập phân kể từ phải sang trái: 36,48.'))
# ===== GIỎI =====
Q.append(fill('gioi',20,'Tìm số thích hợp.',[B('8,9 +',D('28.501')-D('8.9'),'= 28,501'),B('',D('11.83')+D('6.17'),'− 6,17 = 11,83'),B('',D('21.34')*D('3.8'),': 3,8 = 21,34')],
 'Tìm số hạng chưa biết: 28,501 − 8,9 = 19,601. Tìm số bị trừ: 11,83 + 6,17 = 18. Tìm số bị chia: 21,34 × 3,8 = 81,092.'))
s1=D('131.4')-D('80.8'); s2=s1/D('2.3'); s3=D('21.64')*2; r=s2+s3
Q.append(fill('gioi',24,'Tính giá trị của biểu thức (131,4 − 80,8) : 2,3 + 21,64 × 2 theo từng bước.',[B('131,4 − 80,8 =',s1),B('Rồi chia cho 2,3 được',s2),B('Giá trị của biểu thức là',r)],
 f'Làm trong ngoặc trước: 131,4 − 80,8 = {n(s1)}. Chia: {n(s1)} : 2,3 = {n(s2)}. Nhân: 21,64 × 2 = {n(s3)}. Cộng: {n(s2)} + {n(s3)} = {n(r)}.'))
rong=D('17.5'); dai=rong+15; cv=(rong+dai)*2; dt=rong*dai
Q.append(fill('gioi',24,'Sân trường hình chữ nhật có chiều rộng 17,5 m, chiều dài hơn chiều rộng 15 m.',[B('Chiều dài sân là',dai,'m'),B('Chu vi sân là',cv,'m'),B('Diện tích sân là',dt,'m²')],
 f'Chiều dài: 17,5 + 15 = {n(dai)} m. Chu vi: ({n(dai)} + 17,5) × 2 = {n(cv)} m. Diện tích: {n(dai)} × 17,5 = {n(dt)} m².'))
ha=D('1.45'); mai=ha-D('0.08'); nam=mai+D('0.12'); tot=ha+mai+nam
Q.append(fill('gioi',20,'Hà cao 1,45 m. Mai thấp hơn Hà 0,08 m. Nam cao hơn Mai 0,12 m.',[B('Mai cao',mai,'m'),B('Nam cao',nam,'m'),B('Cả ba bạn cao tổng cộng',tot,'m')],
 f'Mai cao: 1,45 − 0,08 = {n(mai)} m. Nam cao: {n(mai)} + 0,12 = {n(nam)} m. Tổng chiều cao ba bạn: 1,45 + {n(mai)} + {n(nam)} = {n(tot)} m.'))
Q.append(tf('gioi',23,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('3,14 × 100 = 314.',True),('31,4 : 10 = 0,314.',False),('314 : 0,001 = 314 000.',True),('(5,3 + 4,7) × 0,1 = 5,3 × 0,1 + 4,7 × 0,1.',True)],
 'a) Đúng. b) Sai: 31,4 : 10 = 3,14 (chuyển dấu phẩy sang trái một chữ số). c) Đúng: chia cho 0,001 thì chuyển dấu phẩy sang phải 3 chữ số. d) Đúng: nhân một tổng với một số bằng tổng các tích; cả hai vế đều bằng 1.'))
thit=D(120000)*D('2.5'); ca=D(85000)*D('1.5'); thoi=D(500000)-thit-ca
Q.append(fill('gioi',24,'Mẹ mua 2,5 kg thịt giá 120 000 đồng một ki-lô-gam và 1,5 kg cá giá 85 000 đồng một ki-lô-gam. Mẹ đưa cho người bán 500 000 đồng.',
 [B('Tiền mua thịt là',thit,'đồng'),B('Tiền mua cá là',ca,'đồng'),B('Người bán trả lại mẹ',thoi,'đồng')],
 f'Tiền thịt: 120 000 × 2,5 = {n(thit)} đồng. Tiền cá: 85 000 × 1,5 = {n(ca)} đồng. Cả hai: {n(thit)} + {n(ca)} = {n(thit+ca)} đồng. Tiền trả lại: 500 000 − {n(thit+ca)} = {n(thoi)} đồng.'))
write(1,Q)
