from g5lib import *
Q=[]
Q.append(mc('tb',27,'Cho hình tròn tâm O. Đoạn thẳng nối tâm O với một điểm trên đường tròn gọi là:',['bán kính','đường kính','chu vi','đường cao'],0,
 'Đoạn thẳng nối tâm với một điểm trên đường tròn là bán kính. Đường kính là đoạn thẳng đi qua tâm và nối hai điểm trên đường tròn.'))
r=D(6)
Q.append(mc('tb',27,'Hình tròn có bán kính 6 cm thì đường kính là:',['3 cm','12 cm','18 cm','36 cm'],1,
 f'Đường kính gấp 2 lần bán kính: 6 × 2 = {n(r*2)} (cm).'))
Q.append(fill('tb',27,'Số?',[B('Đường kính 14 cm thì bán kính là',D(7),'cm'),B('Bán kính 3,5 dm thì đường kính là',D(7),'dm')],
 'Bán kính bằng đường kính chia 2: 14 : 2 = 7 cm. Đường kính bằng bán kính nhân 2: 3,5 × 2 = 7 dm.'))
dd,r=D(10),D(4)
Q.append(fill('tb',27,'Tính chu vi hình tròn.',[B('Đường kính 10 cm, chu vi là',circ_d(dd),'cm'),B('Bán kính 4 m, chu vi là',circ_r(r),'m')],
 f'3,14 × 10 = {n(circ_d(dd))} cm. 3,14 × 4 × 2 = {n(circ_r(r))} m.'))
dd=D(20)
Q.append(mc('tb',27,'Chu vi hình tròn có đường kính 20 cm là:',['31,4 cm',n(circ_d(dd))+' cm','125,6 cm','314 cm'],1,
 f'3,14 × {n(dd)} = {n(circ_d(dd))} (cm).'))
r1,r2=D(2),D(10)
Q.append(fill('tb',27,'Tính diện tích hình tròn.',[B('Bán kính 2 cm, diện tích là',disc(r1),'cm²'),B('Bán kính 10 cm, diện tích là',disc(r2),'cm²')],
 f'3,14 × 2 × 2 = {n(disc(r1))} cm². 3,14 × 10 × 10 = {n(disc(r2))} cm².'))
r=D(5)
Q.append(mc('tb',27,'Diện tích hình tròn có bán kính 5 dm là:',['31,4 dm²','15,7 dm²',n(disc(r))+' dm²','157 dm²'],2,
 f'3,14 × 5 × 5 = {n(disc(r))} (dm²).'))
Q.append(tf('tb',27,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Chu vi hình tròn bằng 3,14 nhân với đường kính.',True),('Diện tích hình tròn bằng 3,14 nhân với bán kính nhân với bán kính.',True),('Bán kính của hình tròn dài gấp 2 lần đường kính.',False),('Mọi bán kính của cùng một hình tròn đều bằng nhau.',True)],
 'a), b), d) đúng. c) Sai: đường kính mới dài gấp 2 lần bán kính.'))
dd=D(1); r=dd/2
Q.append(fill('tb',27,'Mặt bàn tròn có đường kính 1 m.',[B('Chu vi mặt bàn là',circ_d(dd),'m'),B('Diện tích mặt bàn là',disc(r),'m²')],
 f'Chu vi: 3,14 × 1 = {n(circ_d(dd))} m. Bán kính: 1 : 2 = 0,5 m. Diện tích: 3,14 × 0,5 × 0,5 = {n(disc(r))} m².'))
x1,y1=circ_d(5),D(15); x2,y2=circ_d(3),D('9.5'); x3,y3=disc(2),D('12.56')
Q.append(fill('tb',27,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL('Chu vi hình tròn đường kính 5 cm',cmp(x1,y1),'15 cm'),SEL('Chu vi hình tròn đường kính 3 cm',cmp(x2,y2),'9,5 cm'),SEL('Diện tích hình tròn bán kính 2 cm',cmp(x3,y3),'12,56 cm²')],
 f'3,14 × 5 = {n(x1)} {cmp(x1,y1)} 15. 3,14 × 3 = {n(x2)} {cmp(x2,y2)} 9,5. 3,14 × 2 × 2 = {n(x3)} {cmp(x3,y3)} 12,56.'))
# KHÁ
dd=D('0.6'); c=circ_d(dd)
Q.append(fill('kha',27,'Bánh xe đạp của Việt có đường kính 0,6 m.',[B('Chu vi bánh xe là',c,'m'),B('Bánh xe lăn 50 vòng thì xe đi được',c*50,'m')],
 f'Chu vi: 3,14 × 0,6 = {n(c)} m. Đi được: {n(c)} × 50 = {n(c*50)} m.'))
dd=D('0.5'); c=circ_d(dd); L=D(157)
Q.append(fill('kha',27,'Bánh xe có đường kính 0,5 m lăn trên đường, xe đi được 157 m.',[B('Chu vi bánh xe là',c,'m'),B('Số vòng bánh xe đã lăn là',L/c,'vòng')],
 f'Chu vi: 3,14 × 0,5 = {n(c)} m. Số vòng: {n(L)} : {n(c)} = {n(L/c)} vòng.'))
c=D('31.4'); dd=c/PI
Q.append(mc('kha',27,'Hình tròn có chu vi 31,4 cm. Đường kính của hình tròn đó là:',['5 cm','10 cm','20 cm','100 cm'],1,
 f'Đường kính = chu vi : 3,14 = 31,4 : 3,14 = {n(dd)} (cm).'))
dd=D(6); r=dd/2
Q.append(fill('kha',27,'Bể nước hình tròn có đường kính 6 m.',[B('Chu vi bể là',circ_d(dd),'m'),B('Diện tích đáy bể là',disc(r),'m²')],
 f'Chu vi: 3,14 × 6 = {n(circ_d(dd))} m. Bán kính 3 m nên diện tích: 3,14 × 3 × 3 = {n(disc(r))} m².'))
Q.append(mc('kha',27,'Hình tròn có diện tích 12,56 cm². Bán kính của hình tròn đó là:',['1,57 cm','2 cm','4 cm','6,28 cm'],1,
 f'Diện tích = 3,14 × r × r = 12,56 nên r × r = 12,56 : 3,14 = 4. Vì 2 × 2 = 4 nên r = 2 (cm).'))
c=D('6.28'); dd=c/PI; r=dd/2; s=disc(r)
Q.append(fill('kha',27,'Miệng giếng hình tròn có chu vi 6,28 m.',[B('Đường kính miệng giếng là',dd,'m'),B('Bán kính miệng giếng là',r,'m'),B('Diện tích miệng giếng là',s,'m²')],
 f'Đường kính: 6,28 : 3,14 = {n(dd)} m. Bán kính: {n(dd)} : 2 = {n(r)} m. Diện tích: 3,14 × {n(r)} × {n(r)} = {n(s)} m².'))
it=[('Hình tròn bán kính 1 cm',circ_r(1)),('Hình tròn đường kính 3 cm',circ_d(3)),('Hình tròn bán kính 2 cm',circ_r(2)),('Hình tròn đường kính 5 cm',circ_d(5))]
it.sort(key=lambda t:t[1])
Q.append(order('kha',27,'Tính chu vi mỗi hình tròn rồi sắp xếp theo thứ tự chu vi từ bé đến lớn.',[t for t,_ in it],'<',
 'Chu vi: '+'; '.join(f'{t} → {n(v)} cm' for t,v in it)+'.'))
Q.append(tf('kha',27,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Bán kính gấp đôi thì chu vi hình tròn cũng gấp đôi.',True),('Bán kính gấp đôi thì diện tích hình tròn cũng chỉ gấp đôi.',False),('Hình tròn đường kính 6 cm có chu vi 18,84 cm.',True),('Hình tròn đường kính 4 cm có diện tích 12,56 cm².',True)],
 f'a) Đúng. b) Sai: bán kính gấp đôi thì diện tích gấp 4 lần. c) Đúng: 3,14 × 6 = {n(circ_d(6))}. d) Đúng: bán kính 2 cm, 3,14 × 2 × 2 = {n(disc(2))}.'))
# GIỎI
r=D(12); c=circ_r(r)
Q.append(fill('gioi',27,'Sân chơi hình tròn có bán kính 12 m. Hằng ngày bạn Nam chạy 5 vòng quanh mép sân.',[B('Chu vi sân chơi là',c,'m'),B('Mỗi ngày Nam chạy được',c*5,'m')],
 f'Chu vi: 3,14 × 12 × 2 = {n(c)} m. Chạy 5 vòng: {n(c)} × 5 = {n(c*5)} m.',fig=fig_circ('r','12 m','Sân chơi')))
d1,d2=D('0.4'),D('0.6'); c1,c2=circ_d(d1),circ_d(d2); L=D('37.68')
Q.append(fill('gioi',27,'Xe ba bánh có bánh trước đường kính 0,4 m, bánh sau đường kính 0,6 m. Xe đi được quãng đường 37,68 m.',[B('Chu vi bánh trước là',c1,'m'),B('Chu vi bánh sau là',c2,'m'),B('Bánh trước đã lăn',L/c1,'vòng'),B('Bánh sau đã lăn',L/c2,'vòng')],
 f'Chu vi bánh trước: 3,14 × 0,4 = {n(c1)} m. Bánh sau: 3,14 × 0,6 = {n(c2)} m. Số vòng bánh trước: {n(L)} : {n(c1)} = {n(L/c1)}. Số vòng bánh sau: {n(L)} : {n(c2)} = {n(L/c2)}.'))
dd=D(10); r=dd/2; R=r+1; s1=disc(r); s2=disc(R)
Q.append(fill('gioi',27,'Bể bơi hình tròn có đường kính 10 m. Xung quanh bể có lối đi rộng 1 m (lối đi cũng bao quanh bể theo hình vành khăn).',[B('Diện tích mặt bể là',s1,'m²'),B('Diện tích cả bể và lối đi là',s2,'m²'),B('Diện tích lối đi là',s2-s1,'m²')],
 f'Bán kính bể: 10 : 2 = 5 m. Diện tích bể: 3,14 × 5 × 5 = {n(s1)} m². Bán kính cả bể và lối đi: 5 + 1 = 6 m, diện tích: 3,14 × 6 × 6 = {n(s2)} m². Diện tích lối đi: {n(s2)} − {n(s1)} = {n(s2-s1)} m².'))
Q.append(mc('gioi',27,'Hình vuông có cạnh 10 cm, bên trong vẽ một hình tròn có đường kính 10 cm (chạm bốn cạnh). Diện tích phần hình vuông nằm ngoài hình tròn là:',['21,5 cm²','78,5 cm²','43 cm²','100 cm²'],0,
 f'Diện tích hình vuông: 10 × 10 = 100 cm². Hình tròn có bán kính 5 cm nên diện tích: 3,14 × 5 × 5 = {n(disc(5))} cm². Phần còn lại: 100 − {n(disc(5))} = {n(100-disc(5))} (cm²).'))
dd=D(20); c=circ_d(dd); p=D(25000)
Q.append(fill('gioi',27,'Ao hình tròn có đường kính 20 m. Người ta làm hàng rào quanh bờ ao, mỗi mét hàng rào giá 25 000 đồng.',[B('Chu vi bờ ao là',c,'m'),B('Tiền làm hàng rào là',c*p,'đồng')],
 f'Chu vi: 3,14 × 20 = {n(c)} m. Tiền: {n(c)} × 25 000 = {n(c*p)} đồng.',fig=fig_circ('d','20 m','Ao hình tròn')))
Q.append(tf('gioi',27,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Hình tròn bán kính 3 cm có diện tích 28,26 cm².',True),('Hình tròn đường kính 8 cm có chu vi 25,12 cm.',True),('Bán kính gấp 3 lần thì diện tích gấp 9 lần.',True),('Hình tròn bán kính 4 cm có diện tích 25,12 cm².',False)],
 f'a) Đúng: 3,14 × 3 × 3 = {n(disc(3))}. b) Đúng: 3,14 × 8 = {n(circ_d(8))}. c) Đúng: 3 × 3 = 9. d) Sai: 3,14 × 4 × 4 = {n(disc(4))} cm² (25,12 là chu vi).'))
write5(4,Q)
