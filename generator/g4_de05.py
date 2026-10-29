from g4lib import *
Q=[]
def rect_fig(a,b,cap):
    return ('<div class="fig"><figure><svg viewBox="0 0 190 100" role="img" aria-label="Hình chữ nhật dài %s, rộng %s" style="width:190px">'
     '<rect x="18" y="14" width="150" height="66" rx="3" fill="var(--soft)" stroke="currentColor" stroke-width="2.4"/>'
     '<text x="93" y="95" text-anchor="middle" font-size="12" fill="currentColor" font-family="inherit" font-weight="700">%s</text>'
     '<text x="10" y="50" text-anchor="middle" font-size="12" fill="currentColor" font-family="inherit" font-weight="700" transform="rotate(-90 10 50)">%s</text>'
     '</svg><figcaption>%s</figcaption></figure></div>')%(a,b,a,b,cap)
# ===== TRUNG BÌNH =====
dai,rong=D('4.3'),D('3.6'); dt=dai*rong
Q.append(mc('tb',21,f'Phòng của Nam hình chữ nhật có chiều dài {n(dai)} m và chiều rộng {n(rong)} m. Diện tích phòng của Nam là:',['15,48 m²','154,8 m²','1,548 m²','7,9 m²'],0,
 f'Diện tích hình chữ nhật bằng chiều dài nhân chiều rộng: {n(dai)} × {n(rong)} = {n(dt)} (m²). Hai thừa số có tất cả 2 chữ số ở phần thập phân nên tích có 2 chữ số ở phần thập phân.'))
a,b=D('7.5'),D('3.4'); cv=(a+b)*2
Q.append(fill('tb',19,'Mảnh vườn hình chữ nhật có chiều dài 7,5 m và chiều rộng 3,4 m.',[B('Nửa chu vi mảnh vườn là',a+b,'m'),B('Chu vi mảnh vườn là',cv,'m')],
 f'Nửa chu vi (tổng chiều dài và chiều rộng): 7,5 + 3,4 = {n(a+b)} m. Chu vi: {n(a+b)} × 2 = {n(cv)} m.'))
c=D('2.5'); cv=c*4
Q.append(mc('tb',21,f'Một viên gạch men hình vuông có cạnh dài {n(c)} dm. Chu vi viên gạch đó là:',['5 dm',n(cv)+' dm','6,25 dm','25 dm'],1,
 f'Chu vi hình vuông bằng cạnh nhân 4: {n(c)} × 4 = {n(cv)} (dm).'))
a=[(D('8.5'),D('3.25')),(D('12'),D('4.75')),(D('6.07'),D('2.8'))]
Q.append(fill('tb',20,'Đặt tính rồi tính.',[B(f'{n(x)} − {n(y)} =',x-y) for x,y in a],
 '; '.join(f'{n(x)} − {n(y)} = {n(x-y)}' for x,y in a)+'. Nhớ viết các chữ số ở cùng hàng thẳng cột và thêm chữ số 0 vào phần thập phân khi cần.'))
c=D('6.4'); dt=c*c
Q.append(mc('tb',21,f'Sân chơi hình vuông có cạnh dài {n(c)} m. Diện tích sân chơi là:',['25,6 m²',n(dt)+' m²','4,096 m²','12,8 m²'],1,
 f'Diện tích hình vuông bằng cạnh nhân cạnh: {n(c)} × {n(c)} = {n(dt)} (m²).'))
a=[(D('7.5'),D('3.4')),(D('21.9'),D('5.1')),(D('3.08'),D('0.73'))]
Q.append(fill('tb',21,'Đặt tính rồi tính.',[B(f'{n(x)} × {n(y)} =',x*y) for x,y in a],
 '; '.join(f'{n(x)} × {n(y)} = {n(x*y)}' for x,y in a)+'.'))
dt,rong=D('20.4'),D('4'); r=dt/rong
Q.append(mc('tb',22,f'Mảnh vườn hình chữ nhật có diện tích {n(dt)} m² và chiều rộng {n(rong)} m. Chiều dài mảnh vườn là:',[n(r)+' m','81,6 m','16,4 m','0,51 m'],0,
 f'Chiều dài bằng diện tích chia cho chiều rộng: {n(dt)} : {n(rong)} = {n(r)} (m).'))
Q.append(fill('tb',23,'Tính nhẩm.',[B('7,6 × 10 =',D('7.6')*10),B('0,5 × 100 =',D('0.5')*100),B('62 : 100 =',D(62)/100)],
 'Nhân với 10; 100 thì chuyển dấu phẩy sang phải một; hai chữ số: 7,6 × 10 = 76; 0,5 × 100 = 50. Chia cho 100 thì chuyển dấu phẩy sang trái hai chữ số: 62 : 100 = 0,62.'))
a,b=D('1.25'),D('0.9'); r=a+b
Q.append(mc('tb',19,f'Một thanh gỗ dài {n(a)} m, một thanh sắt dài {n(b)} m. Nối hai thanh với nhau được thanh dài:',['2,15 m','2,34 m','1,34 m','21,5 m'],0,
 f'Độ dài sau khi nối: {n(a)} + {n(b)} = {n(r)} (m). Viết 0,9 thành 0,90 để đặt tính.'))
t=[(D('6.4'),D('2.5'),D(15),'×'),(D('20.4'),D(4),D('5.1'),':'),(D('3.25'),D('2.75'),D(7),'+')]
def val(x,y,o): return x*y if o=='×' else x/y if o==':' else x+y
Q.append(fill('tb',21,'Chọn dấu &gt;, &lt;, = thích hợp.',[SEL(f'{n(x)} {o} {n(y)}',cmp(val(x,y,o),z),n(z)) for x,y,z,o in t],
 '; '.join(f'{n(x)} {o} {n(y)} = {n(val(x,y,o))}, mà {n(val(x,y,o))} {cmp(val(x,y,o),z)} {n(z)}' for x,y,z,o in t)+'.'))
# ===== KHÁ =====
a,b=D('17.5'),D('15'); dai=a+b; dt=a*dai; cv=(a+dai)*2
Q.append(fill('kha',20,'Sân trường tiểu học hình chữ nhật có chiều rộng 17,5 m, chiều dài hơn chiều rộng 15 m.',[B('Chiều dài sân là',dai,'m'),B('Chu vi sân là',cv,'m'),B('Diện tích sân là',dt,'m²')],
 f'Chiều dài: 17,5 + 15 = {n(dai)} m. Chu vi: (17,5 + {n(dai)}) × 2 = {n(cv)} m. Diện tích: 17,5 × {n(dai)} = {n(dt)} m².'))
dt,rong=D('292.8'),D('9.6'); dai=dt/rong; cv=(dai+rong)*2
Q.append(fill('kha',22,'Mặt sàn một nhà kính trồng rau hình chữ nhật có diện tích 292,8 m² và chiều rộng 9,6 m.',[B('Chiều dài mặt sàn là',dai,'m'),B('Chu vi mặt sàn là',cv,'m')],
 f'Chiều dài: 292,8 : 9,6 = 2 928 : 96 = {n(dai)} m. Chu vi: ({n(dai)} + 9,6) × 2 = {n(cv)} m.'))
Q.append(tf('kha',21,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Hình vuông cạnh 2,5 m có diện tích 6,25 m².',True),('Hình vuông cạnh 2,5 m có chu vi 10 m.',True),('Hình chữ nhật dài 5 m, rộng 1,2 m có diện tích 60 m².',False),('Hình chữ nhật có diện tích 24 m², chiều dài 8 m thì chiều rộng 3 m.',True)],
 'a) Đúng: 2,5 × 2,5 = 6,25. b) Đúng: 2,5 × 4 = 10. c) Sai: 5 × 1,2 = 6 m². d) Đúng: 24 : 8 = 3.'))
dai,rong,gia=D('6.5'),D('4.2'),D(180000); dt=dai*rong; tien=dt*gia
Q.append(mc('kha',21,'Phòng khách hình chữ nhật dài 6,5 m, rộng 4,2 m được lát sàn gỗ giá 180 000 đồng cho mỗi mét vuông. Số tiền lát sàn là:',['1 890 000 đồng','4 914 000 đồng',n(tien)+' đồng','49 140 000 đồng'],2,
 f'Diện tích sàn: 6,5 × 4,2 = {n(dt)} m². Tiền lát sàn: {n(dt)} × 180 000 = {n(tien)} đồng.'))
tuong,cuaso=D('5.2')*D('3'),D('1.5')*D('1.2'); sơn=tuong-cuaso
Q.append(fill('kha',21,'Bức tường dài 5,2 m, cao 3 m có một ô cửa sổ dài 1,5 m, rộng 1,2 m (không sơn ô cửa).',[B('Diện tích bức tường là',tuong,'m²'),B('Diện tích ô cửa sổ là',cuaso,'m²'),B('Diện tích cần sơn là',sơn,'m²')],
 f'Bức tường: 5,2 × 3 = {n(tuong)} m². Ô cửa sổ: 1,5 × 1,2 = {n(cuaso)} m². Diện tích cần sơn: {n(tuong)} − {n(cuaso)} = {n(sơn)} m².'))
ex=[('3,5 × 4,2',D('3.5')*D('4.2')),('9,6 : 3',D('9.6')/3),('5,75 + 2,5',D('5.75')+D('2.5')),('20 − 6,45',D(20)-D('6.45'))]
ex.sort(key=lambda t:t[1])
Q.append(order('kha',21,'Diện tích bốn căn phòng (đơn vị: mét vuông) được ghi bằng những phép tính sau. Tính rồi sắp xếp theo thứ tự từ hẹp đến rộng.',[e for e,_ in ex],'<',
 'Kết quả: '+'; '.join(f'{e} = {n(v)}' for e,v in ex)+'. Sắp xếp từ bé đến lớn được thứ tự như trên.'))
dai,rong=D('4.8'),D('3.5'); dt=dai*rong
Q.append(mc('kha',21,f'Tấm thảm hình chữ nhật dài {n(dai)} m, rộng {n(rong)} m phủ kín một phần sàn. Diện tích tấm thảm là:',[n(dt)+' m²','8,3 m²','1,68 m²','168 m²'],0,
 f'Diện tích tấm thảm: {n(dai)} × {n(rong)} = {n(dt)} (m²).'))
day,dai=D('2.4'),D('0.7'); nua=day/2; rong=nua-dai; dt=dai*rong
Q.append(fill('kha',22,'Bác thợ uốn một sợi dây đồng dài 2,4 m thành khung hình chữ nhật có chiều dài 0,7 m (dùng hết sợi dây).',[B('Nửa chu vi khung là',nua,'m'),B('Chiều rộng khung là',rong,'m'),B('Diện tích hình chữ nhật đó là',dt,'m²')],
 f'Sợi dây dài bằng chu vi nên nửa chu vi là 2,4 : 2 = {n(nua)} m. Chiều rộng: {n(nua)} − 0,7 = {n(rong)} m. Diện tích: 0,7 × {n(rong)} = {n(dt)} m².'))
# ===== GIỎI =====
dt,rong=D('83.52'),D('8.7'); dai=dt/rong; cv=(dai+rong)*2
Q.append(fill('gioi',22,'Khu vườn trồng cây ăn quả hình chữ nhật có diện tích 83,52 m² và chiều rộng 8,7 m. Người ta làm hàng rào quanh vườn.',[B('Chiều dài khu vườn là',dai,'m'),B('Hàng rào dài',cv,'m')],
 f'Chiều dài: 83,52 : 8,7 = 8 352 : 870 = {n(dai)} m. Hàng rào là chu vi: ({n(dai)} + 8,7) × 2 = {n(cv)} m.'))
dai,rong=D('9.5'),D('6.4'); dt=dai*rong; gach=D('0.5')*D('0.5'); sv=dt/gach
Q.append(fill('gioi',22,'Phòng học hình chữ nhật dài 9,5 m, rộng 6,4 m được lát gạch hình vuông cạnh 0,4 m.',[B('Diện tích phòng học là',dt,'m²'),B('Mỗi viên gạch có diện tích',D('0.4')*D('0.4'),'m²'),B('Cần dùng',dt/(D('0.4')*D('0.4')),'viên gạch')],
 f'Diện tích phòng: 9,5 × 6,4 = {n(dt)} m². Mỗi viên gạch: 0,4 × 0,4 = 0,16 m². Số viên gạch: {n(dt)} : 0,16 = {n(dt/(D("0.4")*D("0.4")))} viên.'))
dai,rong=D('12.5'),D('8.4'); dt=dai*rong; mat=dt/2; tien=mat*D(95000)
Q.append(fill('gioi',21,'Ông Sơn Hà dùng một nửa diện tích mảnh đất hình chữ nhật dài 12,5 m, rộng 8,4 m để xây nhà. Chi phí xây nhà là 95 000 đồng cho mỗi mét vuông.',[B('Diện tích mảnh đất là',dt,'m²'),B('Diện tích xây nhà là',mat,'m²'),B('Chi phí xây nhà là',tien,'đồng')],
 f'Diện tích mảnh đất: 12,5 × 8,4 = {n(dt)} m². Diện tích xây nhà: {n(dt)} : 2 = {n(mat)} m². Chi phí: {n(mat)} × 95 000 = {n(tien)} đồng.'))
dt1=D('15')*D('6.5'); dt2=D('9.9')*D('9.9'); ch=dt2-dt1
Q.append(mc('gioi',21,'Mảnh đất A hình chữ nhật dài 15 m, rộng 6,5 m. Mảnh đất B hình vuông có cạnh 9,9 m. Câu nào sau đây đúng?',[f'Mảnh đất A rộng hơn mảnh đất B {n(ch)} m².',f'Mảnh đất B rộng hơn mảnh đất A {n(ch)} m².','Mảnh đất B rộng hơn mảnh đất A 5,1 m².','Hai mảnh đất rộng bằng nhau.'],1,
 f'Diện tích mảnh A: 15 × 6,5 = {n(dt1)} m². Diện tích mảnh B: 9,9 × 9,9 = {n(dt2)} m². Vì {n(dt2)} − {n(dt1)} = {n(ch)} nên mảnh B rộng hơn mảnh A {n(ch)} m².'))
dai,rong,cao=D('8.5'),D('6'),D('3.2'); xq=(dai+rong)*2*cao; cua=D('4.6'); can=xq-cua; son=can/D('9')
Q.append(fill('gioi',21,'Bốn bức tường của một căn phòng hình chữ nhật dài 8,5 m, rộng 6 m, cao 3,2 m cần sơn. Các cửa chiếm 4,6 m² không sơn. Mỗi lít sơn phủ được 9 m² tường.',[B('Diện tích bốn bức tường là',xq,'m²'),B('Diện tích cần sơn là',can,'m²'),B('Cần dùng',son,'lít sơn')],
 f'Chu vi phòng: (8,5 + 6) × 2 = 29 m. Diện tích bốn bức tường: 29 × 3,2 = {n(xq)} m². Diện tích cần sơn: {n(xq)} − 4,6 = {n(can)} m². Số lít sơn: {n(can)} : 9 = {n(son)} lít.'))
Q.append(tf('gioi',23,'Chọn Đúng hoặc Sai cho mỗi câu.',
 [('Nhân 6,8 với 0,5 cũng bằng chia 6,8 cho 2.',True),('Mảnh đất vuông cạnh 12 m có diện tích 14,4 m².',False),('Nếu chiều dài tăng 10 lần, chiều rộng giữ nguyên thì diện tích tăng 10 lần.',True),('Chia số 72,5 cho 0,1 được 7,25.',False)],
 'a) Đúng: 6,8 × 0,5 = 3,4 và 6,8 : 2 = 3,4. b) Sai: 12 × 12 = 144 m². c) Đúng: diện tích = dài × rộng nên nhân dài với 10 thì diện tích cũng gấp 10 lần. d) Sai: chia cho 0,1 thì chuyển dấu phẩy sang phải một chữ số, 72,5 : 0,1 = 725.'))
write(5,Q)
