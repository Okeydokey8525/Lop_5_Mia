from g5lib import *
Q=[]
Q.append(mc('tb',28,'Ngôi nhà có mái là hình tam giác và thân nhà là hình chữ nhật. Muốn tính diện tích cả hình ngôi nhà ta:',['lấy diện tích mái trừ diện tích thân nhà','cộng diện tích mái với diện tích thân nhà','nhân diện tích mái với diện tích thân nhà','chia diện tích thân nhà cho diện tích mái'],1,
 'Hình ngôi nhà được ghép từ hai hình không chồng lên nhau nên diện tích cả hình bằng diện tích mái cộng diện tích thân nhà.'))
Q.append(mc('tb',28,'Con thuyền giấy ghép từ một hình thang (thân thuyền) và một hình tam giác (cánh buồm). Thân thuyền có dạng hình:',['tam giác','hình thang','hình tròn','hình vuông'],1,
 'Theo đề bài, thân thuyền là hình thang và cánh buồm là hình tam giác.'))
a,h,L,hw=D(6),D(2),D(6),D(3); s1=tri(a,h); s2=L*hw
Q.append(fill('tb',29,'Ngôi nhà ghép từ hình tam giác (mái) và hình chữ nhật (thân) như hình.',[B('Diện tích mái là',s1,'m²'),B('Diện tích thân nhà là',s2,'m²'),B('Diện tích cả hình là',s1+s2,'m²')],
 f'Mái: 6 × 2 : 2 = {n(s1)} m². Thân nhà: 6 × 3 = {n(s2)} m². Cả hình: {n(s1)} + {n(s2)} = {n(s1+s2)} m².',fig=fig_house('6 m','3 m','2 m','Hình ngôi nhà')))
s1=D(8)*D(5); s2=tri(8,3)
Q.append(fill('tb',29,'Hình ghép gồm một hình chữ nhật dài 8 cm, rộng 5 cm và một hình tam giác có đáy 8 cm, chiều cao 3 cm (đáy trùng với cạnh dài hình chữ nhật).',[B('Diện tích hình chữ nhật là',s1,'cm²'),B('Diện tích hình tam giác là',s2,'cm²'),B('Diện tích cả hình ghép là',s1+s2,'cm²')],
 f'Hình chữ nhật: 8 × 5 = {n(s1)} cm². Hình tam giác: 8 × 3 : 2 = {n(s2)} cm². Cả hình: {n(s1)} + {n(s2)} = {n(s1+s2)} cm².'))
s=D(6)*4/2
Q.append(mc('tb',29,'Hai hình tam giác bằng nhau ghép lại thành hình chữ nhật dài 6 cm, rộng 4 cm. Diện tích mỗi hình tam giác là:',['24 cm²',n(s)+' cm²','6 cm²','10 cm²'],1,
 f'Diện tích hình chữ nhật: 6 × 4 = 24 cm². Mỗi tam giác bằng một nửa: 24 : 2 = {n(s)} (cm²).'))
s=D(9)*4
Q.append(fill('tb',29,'Ghép hai tam giác vuông bằng nhau thành một hình chữ nhật dài 9 cm, rộng 4 cm.',[B('Diện tích hình chữ nhật là',s,'cm²'),B('Diện tích mỗi hình tam giác vuông là',s/2,'cm²')],
 f'Hình chữ nhật: 9 × 4 = {n(s)} cm². Mỗi tam giác vuông bằng một nửa: {n(s)} : 2 = {n(s/2)} cm².'))
Q.append(tf('tb',29,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Diện tích hình ghép bằng tổng diện tích các hình thành phần (không chồng lên nhau).',True),('Khi cắt bớt một phần, diện tích phần còn lại bằng diện tích cả hình cộng diện tích phần cắt.',False),('Hình thang vuông có thể chia thành một hình chữ nhật và một hình tam giác vuông.',True),('Hình ghép từ hình vuông cạnh 4 cm và tam giác đáy 4 cm, cao 3 cm có diện tích 22 cm².',True)],
 'a), c) đúng. b) Sai: diện tích phần còn lại bằng diện tích cả hình trừ đi diện tích phần cắt. d) Đúng: 4 × 4 + 4 × 3 : 2 = 16 + 6 = 22 (cm²).'))
s=D(10)*6-D(2)*2
Q.append(fill('tb',29,'Từ tấm bìa hình chữ nhật dài 10 cm, rộng 6 cm, người ta cắt bỏ một hình vuông cạnh 2 cm ở góc.',[B('Diện tích tấm bìa lúc đầu là',D(60),'cm²'),B('Diện tích phần bìa còn lại là',s,'cm²')],
 f'Diện tích lúc đầu: 10 × 6 = 60 cm². Hình vuông cắt bỏ: 2 × 2 = 4 cm². Phần còn lại: 60 − 4 = {n(s)} cm².'))
a,h=D(6),D(8)
Q.append(mc('tb',25,'Cánh buồm hình tam giác có đáy 6 dm và chiều cao 8 dm. Diện tích cánh buồm là:',['48 dm²',n(tri(a,h))+' dm²','14 dm²','24 dm'],1,
 f'{n(a)} × {n(h)} : 2 = {n(tri(a,h))} (dm²).'))
x1=D(6)*4+tri(6,2); y1=D(30); x2=D(25)-D(2)*3; y2=D(20); x3=trap(4,8,3)+4; y3=D(21)
Q.append(fill('tb',29,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL('Hình chữ nhật 6 cm × 4 cm ghép tam giác đáy 6 cm, cao 2 cm có diện tích',cmp(x1,y1),'30 cm²'),SEL('Hình vuông cạnh 5 cm cắt bỏ hình chữ nhật 2 cm × 3 cm còn',cmp(x2,y2),'20 cm²'),SEL('Hình thang đáy 4 cm và 8 cm, cao 3 cm, ghép thêm hình chữ nhật 4 cm² có diện tích',cmp(x3,y3),'21 cm²')],
 f'24 + 6 = {n(x1)} {cmp(x1,y1)} 30. 25 − 6 = {n(x2)} {cmp(x2,y2)} 20. (4 + 8) × 3 : 2 + 4 = 18 + 4 = {n(x3)} {cmp(x3,y3)} 21.'))
# KHÁ
a,h,L,hw=D(12),D(4),D(12),D(5); s1=tri(a,h); s2=L*hw
Q.append(fill('kha',29,'Mặt trước ngôi nhà gồm mái hình tam giác và thân nhà hình chữ nhật như hình.',[B('Diện tích phần mái là',s1,'m²'),B('Diện tích cả mặt trước là',s1+s2,'m²')],
 f'Mái: 12 × 4 : 2 = {n(s1)} m². Thân nhà: 12 × 5 = {n(s2)} m². Cả mặt trước: {n(s1)} + {n(s2)} = {n(s1+s2)} m².',fig=fig_house('12 m','5 m','4 m','Mặt trước ngôi nhà')))
L,Wd,r=D(30),D(20),D(4); s=L*Wd; sa=disc(r)
Q.append(fill('kha',29,'Khu đất hình chữ nhật dài 30 m, rộng 20 m, ở giữa có một ao tròn bán kính 4 m như hình.',[B('Diện tích khu đất là',s,'m²'),B('Diện tích ao là',sa,'m²'),B('Diện tích đất không có ao là',s-sa,'m²')],
 f'Khu đất: 30 × 20 = {n(s)} m². Ao: 3,14 × 4 × 4 = {n(sa)} m². Phần đất còn lại: {n(s)} − {n(sa)} = {n(s-sa)} m².',fig=fig_pond('30 m','20 m','4 m','Khu đất có ao tròn')))
s=D(24)*10-tri(6,10)
Q.append(mc('kha',29,'Mảnh vườn hình chữ nhật dài 24 m, rộng 10 m. Người ta cắt một góc hình tam giác vuông có hai cạnh góc vuông 6 m và 10 m để làm ao. Phần vườn còn lại có diện tích:',['270 m²','240 m²','210 m²','180 m²'],2,
 f'Cả vườn: 24 × 10 = 240 m². Ao: 6 × 10 : 2 = {n(tri(6,10))} m². Còn lại: 240 − {n(tri(6,10))} = {n(s)} (m²).'))
s1=D(36); s2=tri(6,4)
Q.append(fill('kha',29,'Hình ghép gồm một hình vuông cạnh 6 cm và một hình tam giác vuông có đáy 6 cm, chiều cao 4 cm.',[B('Diện tích hình vuông là',s1,'cm²'),B('Diện tích hình tam giác là',s2,'cm²'),B('Diện tích hình ghép là',s1+s2,'cm²')],
 f'Hình vuông: 6 × 6 = {n(s1)} cm². Tam giác: 6 × 4 : 2 = {n(s2)} cm². Cả hình: {n(s1)} + {n(s2)} = {n(s1+s2)} cm².'))
s=D(12)*8/2
Q.append(mc('kha',29,'Cắt tấm bìa hình chữ nhật dài 12 cm, rộng 8 cm theo đường chéo thành 2 hình tam giác bằng nhau. Diện tích mỗi hình tam giác là:',['96 cm²',n(s)+' cm²','24 cm²','20 cm²'],1,
 f'Diện tích hình chữ nhật: 12 × 8 = 96 cm². Mỗi tam giác bằng một nửa: 96 : 2 = {n(s)} cm².'))
s1=tri(9,2); s2=D(9)*4; cua=D('4.5'); sn=D('1.2')*2; sp=s1+s2; sc=sp-cua-sn; l=sc*D('0.2')
Q.append(fill('kha',29,'Mặt trước ngôi nhà gồm mái hình tam giác (đáy 9 m, cao 2 m) và thân nhà hình chữ nhật 9 m × 4 m. Có một cửa ra vào 4,5 m² và hai cửa sổ, mỗi cửa 1,2 m² không phải sơn. Mỗi mét vuông cần 0,2 lít sơn.',[B('Diện tích cả mặt trước là',sp,'m²'),B('Diện tích cần sơn là',sc,'m²'),B('Số lít sơn cần dùng là',l,'lít')],
 f'Mái: 9 × 2 : 2 = {n(s1)} m². Thân nhà: 9 × 4 = {n(s2)} m². Cả mặt trước: {n(sp)} m². Trừ cửa: {n(sp)} − 4,5 − 2 × 1,2 = {n(sc)} m². Sơn: {n(sc)} × 0,2 = {n(l)} lít.',fig=fig_house('9 m','4 m','2 m','Mặt trước ngôi nhà')))
it=[('Hình chữ nhật 7 cm × 3 cm',D(21)),('Tam giác đáy 8 cm, cao 6 cm',tri(8,6)),('Hình thang đáy 9 cm và 6 cm, cao 3 cm',trap(9,6,3)),('Hình tròn bán kính 2 cm',disc(2))]
it.sort(key=lambda t:t[1])
Q.append(order('kha',29,'Tính diện tích mỗi hình rồi sắp xếp theo thứ tự diện tích từ bé đến lớn.',[t for t,_ in it],'<',
 'Diện tích: '+'; '.join(f'{t} → {n(v)} cm²' for t,v in it)+'.'))
Q.append(tf('kha',29,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Hai tam giác vuông bằng nhau ghép thành hình chữ nhật thì diện tích hình chữ nhật gấp đôi diện tích mỗi tam giác.',True),('Cắt hình vuông cạnh 2 cm ở một góc hình chữ nhật thì diện tích giảm đi 4 cm².',True),('Hình ghép từ tam giác 12 cm² và hình chữ nhật 30 cm² có diện tích 360 cm².',False),('Diện tích khu đất có ao tròn (trừ ao) bằng diện tích khu đất trừ diện tích ao.',True)],
 'a), b), d) đúng. c) Sai: diện tích hình ghép là 12 + 30 = 42 cm², không phải 12 × 30.'))
# GIỎI
L,Wd,dd=D(40),D(25),D(10); r=dd/2; sa=disc(r); s=L*Wd; p=D(12000)
Q.append(fill('gioi',29,'Khu đất hình chữ nhật dài 40 m, rộng 25 m có một ao tròn đường kính 10 m. Phần đất còn lại được trồng cỏ, giá 12 000 đồng một mét vuông.',[B('Diện tích ao là',sa,'m²'),B('Diện tích đất trồng cỏ là',s-sa,'m²'),B('Tiền trồng cỏ là',(s-sa)*p,'đồng')],
 f'Bán kính ao: 10 : 2 = 5 m. Diện tích ao: 3,14 × 5 × 5 = {n(sa)} m². Đất trồng cỏ: 40 × 25 − {n(sa)} = {n(s-sa)} m². Tiền: {n(s-sa)} × 12 000 = {n((s-sa)*p)} đồng.'))
t1=trap(6,4,D('1.5')); t2=tri(3,4)
Q.append(fill('gioi',29,'Chiếc thuyền gồm thân thuyền hình thang có hai đáy 6 m và 4 m, chiều cao 1,5 m, và cánh buồm hình tam giác có đáy 3 m, chiều cao 4 m.',[B('Diện tích thân thuyền là',t1,'m²'),B('Diện tích cánh buồm là',t2,'m²'),B('Tổng diện tích hình ghép là',t1+t2,'m²')],
 f'Thân thuyền: (6 + 4) × 1,5 : 2 = {n(t1)} m². Cánh buồm: 3 × 4 : 2 = {n(t2)} m². Tổng: {n(t1)} + {n(t2)} = {n(t1+t2)} m².'))
L,Wd=D(6),D(5); s=L*Wd; g=D('0.5')*D('0.5'); sl=s/g; p=D(18000)
Q.append(fill('gioi',29,'Phòng học hình chữ nhật dài 6 m, rộng 5 m được lát bằng gạch hình vuông cạnh 0,5 m. Mỗi viên gạch giá 18 000 đồng.',[B('Diện tích phòng là',s,'m²'),B('Diện tích một viên gạch là',g,'m²'),B('Số viên gạch cần lát là',sl,'viên'),B('Tiền mua gạch là',sl*p,'đồng')],
 f'Diện tích phòng: 6 × 5 = {n(s)} m². Một viên gạch: 0,5 × 0,5 = {n(g)} m². Số viên: {n(s)} : {n(g)} = {n(sl)} viên. Tiền: {n(sl)} × 18 000 = {n(sl*p)} đồng.'))
s=trap(6,10,4)*2
Q.append(mc('gioi',29,'Ghép hai hình thang giống hệt nhau, mỗi hình có hai đáy 6 cm và 10 cm, chiều cao 4 cm, thành một hình mới (không chồng lên nhau). Diện tích hình mới là:',['32 cm²','64 cm²','16 cm²','80 cm²'],1,
 f'Mỗi hình thang: (6 + 10) × 4 : 2 = {n(trap(6,10,4))} cm². Hình mới: {n(trap(6,10,4))} × 2 = {n(s)} (cm²).'))
L,Wd=D(60),D(40); s=L*Wd; sa=disc(10); st=tri(20,15)
Q.append(fill('gioi',29,'Công viên hình chữ nhật dài 60 m, rộng 40 m có một hồ nước hình tròn bán kính 10 m và một vườn hoa hình tam giác đáy 20 m, chiều cao 15 m. Phần còn lại trồng cỏ.',[B('Diện tích hồ nước là',sa,'m²'),B('Diện tích vườn hoa là',st,'m²'),B('Diện tích đất trồng cỏ là',s-sa-st,'m²')],
 f'Công viên: 60 × 40 = {n(s)} m². Hồ: 3,14 × 10 × 10 = {n(sa)} m². Vườn hoa: 20 × 15 : 2 = {n(st)} m². Trồng cỏ: {n(s)} − {n(sa)} − {n(st)} = {n(s-sa-st)} m².'))
Q.append(tf('gioi',29,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Tam giác đáy 6 cm, cao 4 cm có diện tích bằng hình thang đáy 5 cm và 3 cm, cao 3 cm.',True),('Hình vuông cạnh 5 cm ghép với tam giác đáy 5 cm, cao 4 cm có diện tích 35 cm².',True),('Hình vuông cạnh 4 cm cắt bỏ hình tròn bán kính 2 cm còn lại 3,44 cm².',True),('Khu đất 20 m × 10 m có ao tròn bán kính 3 m, phần đất còn lại là 172,74 m².',False)],
 f'a) Đúng: 6 × 4 : 2 = 12 và (5 + 3) × 3 : 2 = {n(trap(5,3,3))}. b) Đúng: 25 + 10 = 35. c) Đúng: 16 − 3,14 × 2 × 2 = 16 − {n(disc(2))} = {n(16-disc(2))}. d) Sai: 200 − 3,14 × 3 × 3 = 200 − {n(disc(3))} = {n(200-disc(3))} m², không phải 172,74.'))
write5(5,Q)
