from g5lib import *
Q=[]
Q.append(mc('tb',30,'Số thập phân "hai mươi ba phẩy tám mươi mốt" viết là:',['23,81','23,081','203,81','2,381'],0,
 'Hai mươi ba là phần nguyên (23), tám mươi mốt là phần thập phân gồm hai chữ số (81): 23,81.'))
Q.append(mc('tb',30,'Chữ số 5 trong số 12,057 thuộc hàng nào?',['hàng chục','hàng phần mười','hàng phần trăm','hàng phần nghìn'],2,
 'Sau dấu phẩy: chữ số 0 ở hàng phần mười, chữ số 5 ở hàng phần trăm, chữ số 7 ở hàng phần nghìn.'))
Q.append(fill('tb',30,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL('4,09',cmp('4.09','4.1'),'4,1'),SEL('12,50',cmp('12.5','12.5'),'12,5'),SEL('0,98',cmp('0.98','0.89'),'0,89')],
 'So sánh phần nguyên trước, nếu bằng nhau thì so sánh từng hàng ở phần thập phân. 4,09 < 4,1 (phần mười 0 < 1). 12,50 = 12,5 (thêm chữ số 0 vào cuối phần thập phân không đổi giá trị). 0,98 > 0,89 (phần mười 9 > 8).'))
Q.append(fill('tb',30,'Làm tròn số thập phân.',[B('Làm tròn 7,46 đến hàng phần mười được',rnd('7.46',1)),B('Làm tròn 7,46 đến số tự nhiên gần nhất được',rnd('7.46',0)),B('Làm tròn 3,142 đến hàng phần trăm được',rnd('3.142',2))],
 'Nhìn chữ số ngay bên phải hàng cần làm tròn: bé hơn 5 thì giữ nguyên, từ 5 trở lên thì cộng thêm 1. 7,46 ≈ 7,5 (chữ số 6 ≥ 5). 7,46 ≈ 7 (chữ số 4 < 5). 3,142 ≈ 3,14 (chữ số 2 < 5).'))
a=[('24,6 + 5,75',D('24.6')+D('5.75')),('40 − 12,8',D(40)-D('12.8')),('3,5 × 4',D('3.5')*4)]
Q.append(fill('tb',31,'Tính.',[B(e+' =',v) for e,v in a],'; '.join(f'{e} = {n(v)}' for e,v in a)+'.'))
a=[('12,5 × 0,4',D('12.5')*D('0.4')),('9,6 : 3',D('9.6')/3),('6,25 × 100',D('6.25')*100)]
Q.append(fill('tb',31,'Tính.',[B(e+' =',v) for e,v in a],'; '.join(f'{e} = {n(v)}' for e,v in a)+'. Nhân với 100 thì chuyển dấu phẩy sang phải hai chữ số.'))
Q.append(mc('tb',34,'3 km 250 m viết dưới dạng số đo có đơn vị là ki-lô-mét là:',['3,025 km','3,25 km','32,5 km','325 km'],1,
 '250 m = 0,25 km nên 3 km 250 m = 3,25 km.'))
Q.append(fill('tb',34,'Số?',[B('4,5 kg =',D('4.5')*1000,'g'),B('2,35 tạ =',D('2.35')*100,'kg'),B('0,7 tấn =',D('0.7')*1000,'kg')],
 '1 kg = 1 000 g nên 4,5 kg = 4 500 g. 1 tạ = 100 kg nên 2,35 tạ = 235 kg. 1 tấn = 1 000 kg nên 0,7 tấn = 700 kg.'))
Q.append(mc('tb',32,'Muốn tính diện tích hình tam giác, ta:',['lấy đáy cộng chiều cao rồi chia 2','lấy đáy nhân chiều cao','lấy đáy nhân chiều cao rồi chia 2','lấy đáy nhân 2 rồi nhân chiều cao'],2,
 'Diện tích hình tam giác bằng độ dài đáy nhân chiều cao (cùng một đơn vị đo) rồi chia 2.'))
Q.append(mc('tb',33,'Hình chữ nhật dài 12 cm, rộng 5 cm có diện tích là:',['17 cm²','34 cm²','60 cm²','60 cm'],2,
 '12 × 5 = 60 (cm²).'))
# KHÁ
Q.append(fill('kha',30,'Viết số thập phân.',[B('3 đơn vị, 4 phần mười, 7 phần nghìn viết là',D('3.407')),B('25 đơn vị và 6 phần trăm viết là',D('25.06'))],
 '3 đơn vị 4 phần mười 7 phần nghìn: phần mười 4, phần trăm 0, phần nghìn 7 nên 3,407. 25 đơn vị 6 phần trăm: phần mười 0, phần trăm 6 nên 25,06.'))
a=[('100 − 37,45',D(100)-D('37.45')),('8,4 × 2,5',D('8.4')*D('2.5')),('35,52 : 4,8',D('35.52')/D('4.8'))]
Q.append(fill('kha',31,'Tính.',[B(e+' =',v) for e,v in a],'; '.join(f'{e} = {n(v)}' for e,v in a)+'. Với 35,52 : 4,8 chuyển dấu phẩy của cả hai số sang phải một chữ số được 355,2 : 48.'))
kg,p=D('3.5'),D(42000); t=kg*p; th=D(200000)-t
Q.append(fill('kha',31,'Mẹ mua 3,5 kg táo, giá 42 000 đồng một ki-lô-gam, đưa cho cô bán hàng 200 000 đồng.',[B('Tiền mua táo là',t,'đồng'),B('Cô bán hàng trả lại',th,'đồng')],
 f'Tiền táo: 3,5 × 42 000 = {n(t)} đồng. Tiền trả lại: 200 000 − {n(t)} = {n(th)} đồng.'))
Q.append(mc('kha',33,'Hình thang có hai đáy 12 cm và 8 cm, chiều cao 5 cm. Diện tích hình thang là:',['50 cm²','100 cm²','40 cm²','25 cm²'],0,
 f'(12 + 8) × 5 : 2 = {n(trap(12,8,5))} (cm²).'))
dd=D(8); r=dd/2
Q.append(fill('kha',33,'Hình tròn có đường kính 8 cm.',[B('Chu vi hình tròn là',circ_d(dd),'cm'),B('Diện tích hình tròn là',disc(r),'cm²')],
 f'Chu vi: 3,14 × 8 = {n(circ_d(dd))} cm. Bán kính 4 cm nên diện tích: 3,14 × 4 × 4 = {n(disc(r))} cm².'))
Q.append(fill('kha',34,'Số?',[B('4 km² 37 ha =',D(437),'ha'),B('5 dm² 24 cm² =',D(524),'cm²'),B('6,35 tấn =',D(6350),'kg')],
 '1 km² = 100 ha nên 4 km² 37 ha = 400 + 37 = 437 ha. 1 dm² = 100 cm² nên 5 dm² 24 cm² = 500 + 24 = 524 cm². 6,35 tấn = 6,35 × 1 000 = 6 350 kg.'))
it=['4,09','4,9','4,089','4,1']; it.sort(key=lambda s:D(s.replace(',','.')))
Q.append(order('kha',30,'Sắp xếp các số sau theo thứ tự từ bé đến lớn.',[x for x in it],'<',
 'Phần nguyên đều là 4. So sánh phần mười: 0 (4,09 và 4,089), 1 (4,1), 9 (4,9). Giữa 4,089 và 4,09: phần trăm 8 < 9. Thứ tự: 4,089 < 4,09 < 4,1 < 4,9.'))
Q.append(tf('kha',35,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('{17/5} = {3 2/5}.',True),('{3/4} + {1/4} = {4/8}.',False),('{7/20} = 0,35.',True),('{2 1/3} = {7/3}.',True)],
 'a) Đúng: 17 : 5 được 3 dư 2. b) Sai: cộng hai phân số cùng mẫu thì giữ nguyên mẫu số: 3/4 + 1/4 = 4/4 = 1. c) Đúng: 7/20 = 35/100 = 0,35. d) Đúng: 2 × 3 + 1 = 7 nên 2 1/3 = 7/3.'))
# GIỎI
Q.append(fill('gioi',35,'Tính (viết kết quả là phân số tối giản hoặc hỗn số).',[FR('{2/5} + {3/10} =',Fraction(7,10)),FR('{5/6} − {1/4} =',Fraction(7,12)),MX('{7/2} =',Fraction(7,2))],
 '2/5 + 3/10 = 4/10 + 3/10 = 7/10. 5/6 − 1/4 = 10/12 − 3/12 = 7/12. 7/2: 7 : 2 được 3 dư 1 nên bằng 3 1/2.'))
Q.append(fill('gioi',35,'Tính bằng cách thuận tiện.',[FR('{2/7} × {4/9} + {2/7} × {5/9} =',Fraction(2,7)),MX('{5/7} + {8/11} + {2/7} =',Fraction(19,11))],
 '2/7 × 4/9 + 2/7 × 5/9 = 2/7 × (4/9 + 5/9) = 2/7 × 1 = 2/7. 5/7 + 8/11 + 2/7 = (5/7 + 2/7) + 8/11 = 1 + 8/11 = 1 8/11.'))
th,ca=D('2.5')*135000,D('1.2')*85000; tong=th+ca; tl=D(500000)-tong
Q.append(fill('gioi',31,'Mẹ mua 2,5 kg thịt, giá 135 000 đồng một ki-lô-gam, và 1,2 kg cá, giá 85 000 đồng một ki-lô-gam. Mẹ đưa 500 000 đồng.',[B('Tiền mua thịt là',th,'đồng'),B('Tiền mua cá là',ca,'đồng'),B('Tổng số tiền phải trả là',tong,'đồng'),B('Mẹ được trả lại',tl,'đồng')],
 f'Thịt: 2,5 × 135 000 = {n(th)} đồng. Cá: 1,2 × 85 000 = {n(ca)} đồng. Tổng: {n(th)} + {n(ca)} = {n(tong)} đồng. Trả lại: 500 000 − {n(tong)} = {n(tl)} đồng.'))
km=D('0.35')
Q.append(fill('gioi',34,'Một khu rừng có diện tích 0,35 km².',[B('Diện tích khu rừng là',km*100,'ha'),B('Diện tích khu rừng là',km*1000000,'m²')],
 f'1 km² = 100 ha nên 0,35 km² = 0,35 × 100 = {n(km*100)} ha. 1 km² = 1 000 000 m² nên 0,35 km² = {n(km*1000000)} m².'))
L=D(240); Wd=L/4; s=L*Wd
Q.append(fill('gioi',34,'Khu đất hình chữ nhật có chiều dài 240 m, chiều rộng bằng {1/4} chiều dài.',[B('Chiều rộng khu đất là',Wd,'m'),B('Diện tích khu đất là',s,'m²'),B('Diện tích khu đất là',s/10000,'ha')],
 f'Chiều rộng: 240 : 4 = {n(Wd)} m. Diện tích: 240 × {n(Wd)} = {n(s)} m². Đổi sang héc-ta: {n(s)} : 10 000 = {n(s/10000)} ha.'))
Q.append(tf('gioi',31,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('0,5 × 0,1 = 0,05.',True),('6,3 : 0,1 = 0,63.',False),('{3/4} = 0,75.',True),('Hình tròn bán kính 3 cm có chu vi 18,84 cm.',True)],
 f'a) Đúng. b) Sai: chia cho 0,1 là chuyển dấu phẩy sang phải một chữ số, 6,3 : 0,1 = 63. c) Đúng: 3/4 = 75/100. d) Đúng: 3,14 × 3 × 2 = {n(circ_r(3))}.'))
write6(1,Q)
