from g5lib import *
Q=[]
Q.append(mc('tb',32,'Hình tam giác có ba cạnh bằng nhau gọi là:',['tam giác vuông','tam giác tù','tam giác đều','tam giác nhọn'],2,
 'Tam giác có ba cạnh bằng nhau gọi là tam giác đều. Mỗi góc của tam giác đều bằng 60°.'))
Q.append(mc('tb',32,'Chu vi của hình nào được tính bằng 3,14 nhân với đường kính?',['hình tam giác','hình thang','hình tròn','hình chữ nhật'],2,
 'Chu vi hình tròn C = 3,14 × d, với d là đường kính.'))
Q.append(fill('tb',33,'Tính chu vi.',[B('Hình chữ nhật dài 12 cm, rộng 7 cm có chu vi',(D(12)+7)*2,'cm'),B('Hình vuông cạnh 9 cm có chu vi',D(9)*4,'cm')],
 f'(12 + 7) × 2 = {n((D(12)+7)*2)} cm. 9 × 4 = {n(D(9)*4)} cm.'))
Q.append(fill('tb',33,'Tính diện tích.',[B('Hình chữ nhật dài 15 m, rộng 6 m có diện tích',D(15)*6,'m²'),B('Hình vuông cạnh 8 dm có diện tích',D(8)*8,'dm²')],
 '15 × 6 = 90 m². 8 × 8 = 64 dm².'))
Q.append(mc('tb',33,'Hình vuông có cạnh 2,5 m. Chu vi hình vuông là:',['5 m','6,25 m','10 m','12,5 m'],2,
 '2,5 × 4 = 10 (m).'))
t=[(D(9),D(4),'cm'),(D(6),D(8),'dm')]
Q.append(fill('tb',33,'Tính diện tích hình tam giác.',[B(f'Đáy {n(a)} {u}, cao {n(h)} {u}:',tri(a,h),u+'²') for a,h,u in t]+[],
 '9 × 4 : 2 = 18 cm². 6 × 8 : 2 = 24 dm² (tam giác vuông có hai cạnh góc vuông 6 dm và 8 dm cũng tính như vậy).'))
a,b,h=D(10),D(6),D(5)
Q.append(mc('tb',33,'Hình thang có hai đáy 10 dm và 6 dm, chiều cao 5 dm. Diện tích hình thang là:',['80 dm²',n(trap(a,b,h))+' dm²','16 dm²','30 dm²'],1,
 f'({n(a)} + {n(b)}) × {n(h)} : 2 = {n(trap(a,b,h))} (dm²).'))
r=D(2)
Q.append(fill('tb',33,'Hình tròn có bán kính 2 dm.',[B('Chu vi hình tròn là',circ_r(r),'dm'),B('Diện tích hình tròn là',disc(r),'dm²')],
 f'Chu vi: 3,14 × 2 × 2 = {n(circ_r(r))} dm. Diện tích: 3,14 × 2 × 2 = {n(disc(r))} dm².'))
Q.append(tf('tb',32,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Hình vuông có bốn cạnh bằng nhau.',True),('Hình tam giác có thể có hai góc vuông.',False),('Hình thang có hai cạnh đáy song song.',True),('Đường kính của hình tròn gấp đôi bán kính.',True)],
 'a), c), d) đúng. b) Sai: trong một hình tam giác chỉ có nhiều nhất một góc vuông.'))
x1,y1=D(6)*5,tri(10,6); x2,y2=trap(8,4,3),D(16); x3,y3=disc(1),D(4)
Q.append(fill('tb',33,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL('Diện tích hình chữ nhật 6 cm × 5 cm',cmp(x1,y1),'diện tích tam giác đáy 10 cm, cao 6 cm'),SEL('Diện tích hình thang đáy 8 cm và 4 cm, cao 3 cm',cmp(x2,y2),'diện tích hình vuông cạnh 4 cm'),SEL('Diện tích hình tròn bán kính 1 cm',cmp(x3,y3),'diện tích hình vuông cạnh 2 cm')],
 f'6 × 5 = {n(x1)} và 10 × 6 : 2 = {n(y1)}. (8 + 4) × 3 : 2 = {n(x2)} > 16. 3,14 × 1 × 1 = {n(x3)} < 4.'))
# KHÁ
s,Wd=D(96),D(6); L=s/Wd; cv=(L+Wd)*2
Q.append(fill('kha',33,'Hình chữ nhật có diện tích 96 m² và chiều rộng 6 m.',[B('Chiều dài là',L,'m'),B('Chu vi là',cv,'m')],
 f'Chiều dài: 96 : 6 = {n(L)} m. Chu vi: ({n(L)} + 6) × 2 = {n(cv)} m.'))
cv=D(36); c=cv/4; s=c*c
Q.append(fill('kha',33,'Hình vuông có chu vi 36 cm.',[B('Cạnh hình vuông là',c,'cm'),B('Diện tích hình vuông là',s,'cm²')],
 f'Cạnh: 36 : 4 = {n(c)} cm. Diện tích: {n(c)} × {n(c)} = {n(s)} cm².'))
s,a=D(45),D(10); h=s*2/a
Q.append(mc('kha',33,'Hình tam giác có diện tích 45 cm² và đáy 10 cm. Chiều cao của hình tam giác là:',['4,5 cm','9 cm','18 cm','450 cm'],1,
 f'Chiều cao = 45 × 2 : 10 = {n(h)} (cm).'))
s,h,a=D(72),D(6),D(15); tong=s*2/h; b=tong-a
Q.append(fill('kha',33,'Hình thang có diện tích 72 m², chiều cao 6 m, đáy lớn 15 m.',[B('Tổng độ dài hai đáy là',tong,'m'),B('Đáy bé là',b,'m')],
 f'Tổng hai đáy: 72 × 2 : 6 = {n(tong)} m. Đáy bé: {n(tong)} − 15 = {n(b)} m.'))
c=D('25.12'); dd=c/PI; r=dd/2
Q.append(mc('kha',33,'Hình tròn có chu vi 25,12 cm. Bán kính của hình tròn đó là:',['2 cm','4 cm','8 cm','12,56 cm'],1,
 f'Đường kính: 25,12 : 3,14 = {n(dd)} cm. Bán kính: {n(dd)} : 2 = {n(r)} cm.'))
s=D(50)*30; sa=disc(5)
Q.append(fill('kha',33,'Mảnh đất hình chữ nhật dài 50 m, rộng 30 m có một sân tròn bán kính 5 m.',[B('Diện tích sân tròn là',sa,'m²'),B('Diện tích phần đất còn lại là',s-sa,'m²')],
 f'Sân tròn: 3,14 × 5 × 5 = {n(sa)} m². Phần còn lại: 50 × 30 − {n(sa)} = {n(s)} − {n(sa)} = {n(s-sa)} m².'))
it=[('Hình tròn đường kính 6 cm',circ_d(6)),('Hình vuông cạnh 5 cm',D(20)),('Hình chữ nhật 7 cm × 4 cm',D(22)),('Hình vuông cạnh 6,5 cm',D('26'))]
it.sort(key=lambda t:t[1])
Q.append(order('kha',33,'Tính chu vi mỗi hình rồi sắp xếp theo thứ tự chu vi từ bé đến lớn.',[t for t,_ in it],'<',
 'Chu vi: '+'; '.join(f'{t} → {n(v)} cm' for t,v in it)+'.'))
Q.append(tf('kha',33,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Chu vi hình chữ nhật bằng chiều dài cộng chiều rộng rồi nhân 2.',True),('Hai hình chữ nhật có chu vi bằng nhau thì diện tích cũng bằng nhau.',False),('Giữ nguyên chiều cao, đáy tam giác gấp đôi thì diện tích gấp đôi.',True),('Bán kính hình tròn gấp đôi thì chu vi cũng gấp đôi.',True)],
 'a), c), d) đúng. b) Sai: ví dụ hình chữ nhật 6 × 4 và 7 × 3 đều có chu vi 20 nhưng diện tích 24 và 21 khác nhau.'))
# GIỎI
L,Wd,c=D(20),D(12),D('0.4'); s=L*Wd; g=c*c
Q.append(fill('gioi',33,'Sân hình chữ nhật dài 20 m, rộng 12 m được lát bằng gạch hình vuông cạnh 0,4 m.',[B('Diện tích sân là',s,'m²'),B('Diện tích một viên gạch là',g,'m²'),B('Số viên gạch cần lát là',s/g,'viên')],
 f'Sân: 20 × 12 = {n(s)} m². Một viên: 0,4 × 0,4 = {n(g)} m². Số viên: {n(s)} : {n(g)} = {n(s/g)} viên.'))
a,b,h=D(36),D(24),D(20); s=trap(a,b,h); hoa=s*D('0.4')
Q.append(fill('gioi',33,'Mảnh đất hình thang có hai đáy 36 m và 24 m, chiều cao 20 m. Người ta dành 0,4 diện tích để trồng hoa, phần còn lại trồng rau.',[B('Diện tích mảnh đất là',s,'m²'),B('Diện tích trồng hoa là',hoa,'m²'),B('Diện tích trồng rau là',s-hoa,'m²')],
 f'Diện tích: (36 + 24) × 20 : 2 = {n(s)} m². Trồng hoa: {n(s)} × 0,4 = {n(hoa)} m². Trồng rau: {n(s)} − {n(hoa)} = {n(s-hoa)} m².'))
a,s=D(15),D(90); h=s*2/a; a2=D(10); s2=tri(a2,h)
Q.append(fill('gioi',33,'Hình tam giác có đáy 15 cm và diện tích 90 cm².',[B('Chiều cao của tam giác là',h,'cm'),B('Tam giác khác có cùng chiều cao nhưng đáy 10 cm, diện tích là',s2,'cm²')],
 f'Chiều cao: 90 × 2 : 15 = {n(h)} cm. Tam giác thứ hai: 10 × {n(h)} : 2 = {n(s2)} cm².'))
cv=(D(12)+8)*2; c=cv/4; s1=D(12)*8; s2=c*c
Q.append(mc('gioi',33,'Hình vuông có chu vi bằng chu vi hình chữ nhật dài 12 cm, rộng 8 cm. Diện tích hình vuông lớn hơn diện tích hình chữ nhật là:',['4 cm²','8 cm²','96 cm²','100 cm²'],0,
 f'Chu vi hình chữ nhật: (12 + 8) × 2 = {n(cv)} cm. Cạnh hình vuông: {n(cv)} : 4 = {n(c)} cm, diện tích {n(s2)} cm². Hình chữ nhật: 12 × 8 = {n(s1)} cm². Hiệu: {n(s2)} − {n(s1)} = {n(s2-s1)} (cm²).'))
dd=D(12); c=circ_d(dd); s=disc(dd/2); p=D(55000)
Q.append(fill('gioi',33,'Bể bơi hình tròn có đường kính 12 m. Hàng rào quanh bể giá 55 000 đồng một mét.',[B('Chu vi bể là',c,'m'),B('Diện tích mặt bể là',s,'m²'),B('Tiền làm hàng rào quanh bể là',c*p,'đồng')],
 f'Chu vi: 3,14 × 12 = {n(c)} m. Bán kính 6 m nên diện tích: 3,14 × 6 × 6 = {n(s)} m². Tiền rào: {n(c)} × 55 000 = {n(c*p)} đồng.',fig=fig_circ('d','12 m','Bể bơi')))
Q.append(tf('gioi',33,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Tam giác đáy 8 cm, cao 6 cm có diện tích 24 cm².',True),('Hình thang đáy 6 cm và 10 cm, cao 4 cm có diện tích 32 cm².',True),('Hình tròn đường kính 10 cm có diện tích 78,5 cm².',True),('Hình vuông cạnh 6 cm có chu vi (cm) lớn hơn diện tích (cm²) về số đo.',False)],
 f'a) Đúng: 8 × 6 : 2 = 24. b) Đúng: (6 + 10) × 4 : 2 = 32. c) Đúng: bán kính 5 cm, 3,14 × 5 × 5 = {n(disc(5))}. d) Sai: chu vi 24 cm bé hơn diện tích 36 cm².'))
write6(4,Q)
