"""Original questions: printed pages 40–86 of Toán 5, tập hai, KNTT."""
from decimal import ROUND_HALF_UP
from g4lib import B, D, SEL, cmp, fill, mc, n, order, tf, write
from .content import choice, table

LESSONS9={49:('Hình khai triển của hình lập phương, hình hộp chữ nhật và hình trụ',40),
    50:('Diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật',44),
    51:('Diện tích xung quanh và diện tích toàn phần của hình lập phương',48),
    52:('Thể tích của hình hộp chữ nhật',51),53:('Thể tích của hình lập phương',54),
    54:('Thực hành tính toán và ước lượng thể tích một số hình khối',58),55:('Luyện tập chung',60)}
LESSONS10={56:('Các đơn vị đo thời gian',64),57:('Cộng, trừ số đo thời gian',67),
    58:('Nhân, chia số đo thời gian với một số',71),59:('Vận tốc của một chuyển động đều',76),
    60:('Quãng đường, thời gian của một chuyển động đều',78),
    61:('Thực hành tính toán và ước lượng về vận tốc, quãng đường, thời gian trong chuyển động đều',82),
    62:('Luyện tập chung',84)}


def box_fig(a,b,h,unit='cm'):
    a,b,h=map(D,map(str,(a,b,h)))
    k=D(140)/max(a,b,h);x,y=D(35),D(65)+h*k;w,ht,dx,dy=a*k,h*k,b*k*D('.48'),b*k*D('.32')
    shapes=f'<path d="M{x},{y} v-{ht} h{w} v{ht} Z" fill="var(--soft)"/><path d="M{x},{y-ht} l{dx},-{dy} h{w} l-{dx},{dy} Z" fill="#FFE0EE"/><path d="M{x+w},{y} l{dx},-{dy} v-{ht} l-{dx},{dy} Z" fill="#F6B4CD"/>'
    labels=f'<text x="{x+w/2}" y="{y+29}" text-anchor="middle">{n(a)} {unit}</text><text x="{x+w+dx+8}" y="{y-ht/2-dy/2}">{n(h)} {unit}</text><text x="{x+w+dx/2+8}" y="{y-dy/2+24}">{n(b)} {unit}</text>'
    return f'<div class="fig"><figure><svg style="width:340px;max-width:100%;height:auto" width="340" height="260" viewBox="0 0 340 260" role="img" aria-label="Hình hộp với chiều dài, rộng và cao đã ghi"><g stroke="currentColor" stroke-width="2" stroke-linejoin="round">{shapes}</g><g fill="currentColor" font-size="18">{labels}</g></svg><figcaption>Chiều dài, chiều rộng và chiều cao dùng cùng đơn vị.</figcaption></figure></div>'


NETS=[[(0,1),(1,1),(2,1),(3,1),(1,0),(1,2)],
      [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0)],
      [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)],
      [(0,1),(1,1),(2,1),(3,1),(4,1),(2,0)]]


def net_gallery(i):
    shift=i%4;shapes=NETS[shift:]+NETS[:shift];html=''
    for label,coords in zip('ABCD',shapes):
        if i%2:coords=[(y,x) for x,y in coords]
        w=(max(x for x,y in coords)+1)*23+16;h=(max(y for x,y in coords)+1)*23+16
        cells=''.join(f'<rect x="{8+x*23}" y="{8+y*23}" width="23" height="23" fill="var(--soft)" stroke="currentColor" stroke-width="2"/>' for x,y in coords)
        data=';'.join(f'{x},{y}' for x,y in coords)
        html+=f'<figure><svg data-cube-net="{data}" style="width:{w}px;max-width:100%;height:auto" viewBox="0 0 {w} {h}" role="img" aria-label="Tấm bìa {label}">{cells}</svg><figcaption>Hình {label}</figcaption></figure>'
    return '<div class="fig" style="gap:24px;align-items:center">'+html+'</div>',(4-shift)%4


def cylinder_net():
    return '<div class="fig"><figure><svg style="width:240px;max-width:100%;height:auto" viewBox="0 0 240 180" role="img" aria-label="Tấm bìa gồm một hình chữ nhật và hai hình tròn ở hai phía đối diện"><g fill="var(--soft)" stroke="currentColor" stroke-width="2"><rect x="25" y="62" width="188.5" height="54"/><circle cx="58" cy="32" r="30"/><circle cx="178" cy="146" r="30"/></g></svg><figcaption>Tấm bìa có đủ các mặt của một hộp kín.</figcaption></figure></div>'


def route_fig(distance):
    return f'<div class="fig"><figure><svg style="width:300px;max-width:100%;height:auto" viewBox="0 0 300 100" role="img" aria-label="Đường đi từ A đến B"><path d="M35 58 H265" stroke="currentColor" stroke-width="4"/><circle cx="35" cy="58" r="8" fill="#F6B4CD"/><circle cx="265" cy="58" r="8" fill="#F6B4CD"/><g fill="currentColor" font-size="20" text-anchor="middle"><text x="35" y="90">A</text><text x="265" y="90">B</text><text x="150" y="35">{n(distance)} km</text></g></svg><figcaption>Sơ đồ minh họa; dùng số đo ghi trong đề.</figcaption></figure></div>'


def sxq(a,b,h):return 2*(a+b)*h
def stp(a,b,h):return 2*(a*b+a*h+b*h)


def questions9(i):
    a,b,h=map(D,[(8,4,3),(9,5,4),(12,6,5),(10,4,6),(15,5,4),(14,6,3)][i-1]);c=D(i+2)
    Q=[]
    Q.append(choice('tb',49,'Tấm bìa trong hình có thể gấp thành hộp kín dạng nào?','hình trụ',['hình cầu','hình lập phương','hình hộp chữ nhật'],
        'Hai hình tròn bằng nhau là hai đáy, hình chữ nhật bao quanh tạo thành mặt bên của hình trụ.',i,cylinder_net()))
    fig,correct=net_gallery(i)
    Q.append(mc('tb',49,'Tấm bìa nào gấp được thành hình lập phương kín, không chồng mặt?',['Hình A','Hình B','Hình C','Hình D'],correct,
        'Hình '+ 'ABCD'[correct]+' gấp được thành sáu mặt vuông riêng biệt. Các tấm còn lại có mặt chồng lên nhau khi gấp.',fig))
    Q.append(fill('tb',50,f'Hộp có chiều dài {n(a)} cm, rộng {n(b)} cm và cao {n(h)} cm.',[B('Diện tích xung quanh là',sxq(a,b,h),'cm²')],f'({n(a)} + {n(b)}) × 2 × {n(h)} = {n(sxq(a,b,h))} cm².',box_fig(a,b,h)))
    Q.append(fill('tb',50,f'Hộp kín dài {n(a)} cm, rộng {n(b)} cm, cao {n(h)} cm.',[B('Diện tích toàn phần là',stp(a,b,h),'cm²')],f'Diện tích xung quanh {n(sxq(a,b,h))}; hai đáy {n(2*a*b)}. Tổng: {n(stp(a,b,h))} cm².'))
    Q.append(choice('tb',51,f'Hình lập phương cạnh {n(c)} cm có diện tích xung quanh là:',f'{n(4*c*c)} cm²',
        [f'{n(c*c)} cm²',f'{n(6*c*c)} cm²',f'{n(3*c*c)} cm²'],f'{n(c)} × {n(c)} × 4 = {n(4*c*c)} cm².',i+1))
    Q.append(fill('tb',51,f'Hình lập phương có cạnh {n(c)} dm.',[B('Diện tích toàn phần là',6*c*c,'dm²')],f'{n(c)} × {n(c)} × 6 = {n(6*c*c)} dm².'))
    Q.append(fill('tb',52,f'Hộp dài {n(a)} dm, rộng {n(b)} dm, cao {n(h)} dm.',[B('Thể tích là',a*b*h,'dm³')],f'{n(a)} × {n(b)} × {n(h)} = {n(a*b*h)} dm³.'))
    Q.append(fill('tb',53,f'Khối lập phương có cạnh {n(c)} cm.',[B('Thể tích là',c*c*c,'cm³')],f'{n(c)} × {n(c)} × {n(c)} = {n(c*c*c)} cm³.'))
    Q.append(fill('tb',55,'So sánh các số đo thể tích.',[SEL(f'{n(c)} dm³','=',f'{n(c*1000)} cm³'),SEL(f'{n(c)} m³','>',f'{n(c*100)} dm³')],
        f'{n(c)} dm³ = {n(c*1000)} cm³; {n(c)} m³ = {n(c*1000)} dm³ > {n(c*100)} dm³.'))
    Q.append(tf('tb',55,'Chọn Đúng hoặc Sai.',[('Diện tích dùng đơn vị vuông; thể tích dùng đơn vị khối.',True),('Diện tích toàn phần của hộp kín chỉ gồm bốn mặt bên.',False),('Thể tích hình lập phương bằng cạnh × cạnh × cạnh.',True)],
        'Hộp kín có hai đáy và bốn mặt bên. Không nhầm diện tích với thể tích.'))
    Q.append(fill('kha',50,f'Bể cá không có nắp, dài {n(a)} dm, rộng {n(b)} dm, cao {n(h)} dm. Bỏ qua độ dày kính và mép ghép.',
        [B('Diện tích kính bốn mặt bên là',sxq(a,b,h),'dm²'),B('Tổng diện tích kính là',sxq(a,b,h)+a*b,'dm²')],
        f'Bốn bên: {n(sxq(a,b,h))} dm². Thêm một đáy {n(a*b)} dm²: tổng {n(sxq(a,b,h)+a*b)} dm²; không cộng nắp.'))
    Q.append(fill('kha',51,f'Bánh dạng hình lập phương cạnh {n(c)} cm được phủ kem trên mặt trên và bốn mặt bên, không phủ mặt dưới.',
        [B('Diện tích cần phủ kem là',5*c*c,'cm²')],f'Có 5 mặt cần phủ, mỗi mặt {n(c*c)} cm². Tổng: {n(c*c)} × 5 = {n(5*c*c)} cm².'))
    length=D('0.8')+D(i)/10;width=D(30+5*i);height=D(20+5*i)
    Q.append(fill('kha',52,f'Thùng có kích thước trong lòng: dài {n(length)} m, rộng {n(width)} cm, cao {n(height)} cm.',
        [B('Chiều dài đổi ra',length*100,'cm'),B('Thể tích trong lòng là',length*100*width*height,'cm³')],
        f'{n(length)} m = {n(length*100)} cm. Thể tích: {n(length*100)} × {n(width)} × {n(height)} = {n(length*100*width*height)} cm³.'))
    base_a,base_b=D(10+i),D(5+i);before,after=D(3),D('3.5')+D(i)/10
    Q.append(fill('kha',52,f'Bình chữ nhật có đáy trong lòng dài {n(base_a)} cm, rộng {n(base_b)} cm. Thả vật chìm hoàn toàn: mực nước từ {n(before)} cm lên {n(after)} cm. Nước không tràn, vật không hút nước.',
        [B('Mực nước tăng',after-before,'cm'),B('Thể tích vật là',base_a*base_b*(after-before),'cm³')],
        f'Độ dâng: {n(after)} − {n(before)} = {n(after-before)} cm. Thể tích vật = thể tích nước dâng: {n(base_a)} × {n(base_b)} × {n(after-before)} = {n(base_a*base_b*(after-before))} cm³.'))
    values=[c*1000+100,c*1000+250,c*1000+500,c*1000+750]
    Q.append(order('kha',55,'Sắp xếp thể tích các hộp từ bé đến lớn.',[f'{n(values[0])} cm³',f'{n(values[1]/1000)} dm³',f'{n(values[2]/1000000)} m³',f'{n(values[3])} cm³'],'<',
        'Đổi về cm³ rồi so sánh: '+' < '.join(n(v) for v in values)+'.'))
    na,nb,nh=2+i%2,2,3;edge=D(2)
    Q.append(fill('kha',54,f'Thùng có kích thước trong lòng dài {na*2} dm, rộng {nb*2} dm, cao {nh*2} dm. Xếp hộp lập phương cạnh 2 dm, các cạnh song song thành thùng, không để khe hở.',
        [B('Mỗi lớp xếp được',na*nb,'hộp'),B('Thùng xếp đầy được',na*nb*nh,'hộp')],f'Mỗi lớp: ({na*2} : 2) × ({nb*2} : 2) = {na*nb}. Có {nh*2} : 2 = {nh} lớp; tổng {na*nb*nh} hộp. Không chỉ chia thể tích nếu chưa kiểm tra cách xếp.'))
    Q.append(tf('kha',53,'Ghép hai khối lập phương cùng cỡ sát nhau, chung trọn một mặt, không chồng thể tích.',[('Thể tích hình ghép gấp hai lần thể tích một khối.',True),
        ('Diện tích toàn phần hình ghép bằng tổng diện tích toàn phần hai khối rời.',False),('Hai mặt tiếp xúc trở thành mặt bên trong hình ghép.',True)],'Thể tích cộng được. Hai mặt tiếp xúc không còn lộ ra nên diện tích ngoài giảm đi.'))
    Q.append(fill('kha',52,f'Hộp có thể tích {n(a*b*h)} dm³, đáy dài {n(a)} dm và rộng {n(b)} dm.',[B('Chiều cao là',h,'dm')],
        f'Diện tích đáy: {n(a)} × {n(b)} = {n(a*b)} dm². Cao: {n(a*b*h)} : {n(a*b)} = {n(h)} dm.'))
    rate=D(12000+1000*i);wall=sxq(a,b,h);opening=D(i+1)
    Q.append(fill('gioi',50,f'Một mô hình phòng dài {n(a)} m, rộng {n(b)} m, cao {n(h)} m. Sơn bốn tường, trừ cửa tổng diện tích {n(opening)} m²; không sơn trần hay sàn. Giá giả định {n(rate)} đồng/m².',
        [B('Diện tích cần sơn là',wall-opening,'m²'),B('Tiền sơn là',(wall-opening)*rate,'đồng')],
        f'Tường: {n(wall)} m²; trừ cửa còn {n(wall-opening)} m². Tiền: {n(wall-opening)} × {n(rate)} = {n((wall-opening)*rate)} đồng.'))
    cut=D(2)
    Q.append(fill('gioi',55,f'Khối gỗ hộp chữ nhật dài {n(a)} dm, rộng {n(b)} dm, cao {n(h)} dm. Cắt bỏ một khối lập phương cạnh {n(cut)} dm nằm hoàn toàn trong khối ban đầu.',
        [B('Thể tích cắt bỏ là',cut**3,'dm³'),B('Thể tích gỗ còn lại là',a*b*h-cut**3,'dm³')],f'Ban đầu {n(a*b*h)} dm³; bỏ {n(cut)} × {n(cut)} × {n(cut)} = {n(cut**3)} dm³. Còn {n(a*b*h-cut**3)} dm³.'))
    Q.append(fill('gioi',51,f'Ghép sát hai khối lập phương cạnh {n(c)} cm, chung trọn một mặt, thành một hộp chữ nhật.',
        [B('Thể tích hình ghép là',2*c**3,'cm³'),B('Diện tích ngoài của hình ghép là',10*c*c,'cm²')],
        f'Thể tích: 2 × {n(c**3)} = {n(2*c**3)} cm³. Diện tích ngoài: (6 + 6 − 2) × {n(c*c)} = {n(10*c*c)} cm².'))
    wa,wb,old=D(8+i),D(4),D(6);newbase=D(2)*wa*wb
    Q.append(fill('gioi',55,f'Có {n(wa*wb*old)} cm³ nước. Đổ hết sang một bình khác có đáy trong lòng diện tích {n(newbase)} cm², thành thẳng đứng, đủ cao. Không hao hụt nước.',
        [B('Mực nước trong bình mới cao',wa*wb*old/newbase,'cm')],f'Chiều cao nước = thể tích : diện tích đáy = {n(wa*wb*old)} : {n(newbase)} = {n(wa*wb*old/newbase)} cm.'))
    small_edge=D(i+2);x,y,z=2,3,2
    Q.append(fill('gioi',54,f'Xếp khít {x*y*z} hộp lập phương cạnh {n(small_edge)} cm thành hộp lớn: {x} hộp theo chiều dài, {y} theo chiều rộng và {z} theo chiều cao.',
        [B('Chiều dài hộp lớn là',x*small_edge,'cm'),B('Thể tích hộp lớn là',x*y*z*small_edge**3,'cm³')],
        f'Kích thước hộp lớn: {n(x*small_edge)} × {n(y*small_edge)} × {n(z*small_edge)} cm. Thể tích: {x*y*z} × {n(small_edge**3)} = {n(x*y*z*small_edge**3)} cm³.'))
    big=D(2)*c;ratio=D(25+5*i);water=big**3*ratio/100
    Q.append(fill('gioi',55,f'Bể lập phương có cạnh trong lòng {n(big)} dm. Nước chiếm {n(ratio)}% dung tích. Biết 1 dm³ = 1 lít.',
        [B('Dung tích bể là',big**3,'lít'),B('Cần thêm để đầy bể',big**3-water,'lít')],f'Dung tích: {n(big)} × {n(big)} × {n(big)} = {n(big**3)} lít. Đang có {n(water)} lít; cần thêm {n(big**3-water)} lít.'))
    return Q


def hm(total):return divmod(int(total),60)
def time_blanks(total,unit='giờ'):
    a,b=hm(total);return [B('Kết quả:',a,unit),B('và',b,'phút' if unit=='giờ' else 'giây')]


def questions10(i):
    Q=[];hh=i+1;mins=15+5*i
    Q.append(fill('tb',56,'Đổi về phút.',[B(f'{hh} giờ {mins} phút =',hh*60+mins,'phút')],f'{hh} × 60 + {mins} = {hh*60+mins} phút.'))
    days=[7,24,60,100,12,60][i-1];stem,unit=[('Một tuần có bao nhiêu ngày?','ngày'),('Một ngày có bao nhiêu giờ?','giờ'),('Một giờ có bao nhiêu phút?','phút'),('Một thế kỉ có bao nhiêu năm?','năm'),('Một năm có bao nhiêu tháng?','tháng'),('Một phút có bao nhiêu giây?','giây')][i-1]
    Q.append(choice('tb',56,stem,f'{days} {unit}',[f'{days+1} {unit}',f'{days*10} {unit}',f'{days-1} {unit}'],f'Đổi đúng đơn vị: {days} {unit}.',i))
    total=(i+1)*60+40+35
    Q.append(fill('tb',57,f'Tính {i+1} giờ 40 phút + 35 phút. Phần phút của kết quả phải nhỏ hơn 60.',time_blanks(total),f'{i+1} giờ 75 phút = {hm(total)[0]} giờ {hm(total)[1]} phút.'))
    diff=(i+3)*60+10-(60+45)
    Q.append(fill('tb',57,f'Tính {i+3} giờ 10 phút − 1 giờ 45 phút. Phần phút nhỏ hơn 60.',time_blanks(diff),f'Đổi ra phút rồi trừ: {(i+3)*60+10} − 105 = {diff} phút = {hm(diff)[0]} giờ {hm(diff)[1]} phút.'))
    mult=3+i;seconds=155*mult
    Q.append(fill('tb',58,f'Tính 2 phút 35 giây × {mult}. Phần giây nhỏ hơn 60.',time_blanks(seconds,'phút'),f'2 phút 35 giây = 155 giây. 155 × {mult} = {seconds} giây = {hm(seconds)[0]} phút {hm(seconds)[1]} giây.'))
    total=(i+5)*60+30;each=total//3
    Q.append(fill('tb',58,f'Chia {i+5} giờ 30 phút cho 3 phần thời gian bằng nhau. Phần phút nhỏ hơn 60.',time_blanks(each),f'{total} : 3 = {each} phút = {hm(each)[0]} giờ {hm(each)[1]} phút mỗi phần.'))
    dist=D(12+3*i);duration=D('.5');speed=dist/duration
    Q.append(fill('tb',59,f'Một xe đi đều quãng đường {n(dist)} km trong {n(duration)} giờ.',[B('Vận tốc là',speed,'km/h')],f'v = s : t = {n(dist)} : {n(duration)} = {n(speed)} km/h.',route_fig(dist)))
    v=D(30+5*i);t=D('1.5');s=v*t
    Q.append(fill('tb',60,f'Xe đi đều với vận tốc {n(v)} km/h trong {n(t)} giờ.',[B('Quãng đường đi được là',s,'km')],f's = v × t = {n(v)} × {n(t)} = {n(s)} km.'))
    time=D(1)+D(i%3)/2;distance=v*time
    Q.append(fill('tb',60,f'Một xe đi đều quãng đường {n(distance)} km với vận tốc {n(v)} km/h.',[B('Thời gian đi là',time,'giờ')],f't = s : v = {n(distance)} : {n(v)} = {n(time)} giờ.'))
    Q.append(tf('tb',56,'Chọn Đúng hoặc Sai.',[('1 giờ 30 phút = 1,3 giờ.',False),('Tháng Hai của năm nhuận có 29 ngày.',True),('Đơn vị km/h cho biết số ki-lô-mét đi trong một giờ.',True),('Muốn tính vận tốc, lấy quãng đường chia thời gian.',True)],'1 giờ 30 phút = 1,5 giờ. Tháng Hai năm nhuận có 29 ngày. Vận tốc có đơn vị độ dài trên thời gian.'))
    kh=D(9+9*i);ms=kh*1000/3600
    Q.append(fill('kha',59,'Đổi đơn vị vận tốc.',[B(f'{n(kh)} km/h =',ms,'m/s')],f'{n(kh)} km/h = ({n(kh*1000)} : 3 600) m/s = {n(ms)} m/s.'))
    measured=D(30+3*i);sec=D(23+i);rounded=(measured/sec).quantize(D('.1'),rounding=ROUND_HALF_UP)
    Q.append(fill('kha',61,f'Trong thẻ đo GIẢ ĐỊNH, một bạn đi {n(measured)} m hết {n(sec)} giây. Tính vận tốc, làm tròn đến một chữ số thập phân.',[B('Vận tốc xấp xỉ',rounded,'m/s')],
        f'Lấy {n(measured)} : {n(sec)}, rồi làm tròn đến hàng phần mười được {n(rounded)} m/s.',table(['Quãng đường','Thời gian'],[[f'{n(measured)} m',f'{n(sec)} giây']])))
    start=7*60+10+5*i;finish=start+105+15
    Q.append(fill('kha',57,f'Chuyến đi khởi hành lúc 7 giờ {10+5*i} phút, di chuyển 1 giờ 45 phút và nghỉ 15 phút. Đến nơi cùng ngày, phần phút nhỏ hơn 60.',
        [B('Đến nơi lúc',hm(finish)[0],'giờ'),B('và',hm(finish)[1],'phút')],f'Tổng thời gian: 105 + 15 = 120 phút = 2 giờ. Đến lúc {hm(finish)[0]} giờ {hm(finish)[1]} phút.'))
    moving=D(120);velocity=D(20+5*i);length=velocity*2
    Q.append(fill('kha',62,f'Xe rời A lúc 7 giờ 45 phút, đến B lúc 10 giờ 15 phút cùng ngày, trong đó nghỉ 30 phút. Quãng đường AB dài {n(length)} km.',
        [B('Thời gian thực chạy là',moving,'phút'),B('Vận tốc khi chạy đều là',velocity,'km/h')],f'Tổng 150 phút, trừ nghỉ 30 phút còn 120 phút = 2 giờ. v = {n(length)} : 2 = {n(velocity)} km/h.'))
    offset=5*i;vals=[70+offset,80+offset,90+offset,100+offset]
    Q.append(order('kha',56,'Sắp xếp các khoảng thời gian từ ngắn đến dài.',[f'{vals[0]} phút',f'{n(D(vals[1])/60)} giờ' if vals[1]%3==0 else f'{vals[1]*60} giây',f'{vals[2]} phút',f'{vals[3]*60} giây'],'<',
        'Đổi tất cả về phút: '+' < '.join(map(str,vals))+'.'))
    va,vb=D(60),D(40);ta,tb=D('1.5'),D(2);da,db=va*ta,vb*tb
    if i%2:da,db,va,vb,ta,tb=db,da,vb,va,tb,ta
    correct='Đường A' if ta<tb else 'Đường B'
    Q.append(choice('kha',61,f'Hai đường giả định: A dài {n(da)} km, đi đều {n(va)} km/h; B dài {n(db)} km, đi đều {n(vb)} km/h. Không nghỉ. Đường nào đi ít thời gian hơn?',
        correct,['Hai đường bằng thời gian','Không thể tính được','Đường B' if correct=='Đường A' else 'Đường A'],f'Đường A mất {n(da)} : {n(va)} = {n(ta)} giờ; B mất {n(db)} : {n(vb)} = {n(tb)} giờ. So sánh thời gian, không chỉ so độ dài.',i))
    number=3+i;eachsec=70+5*i;allsec=number*eachsec
    Q.append(fill('kha',58,f'Làm {number} món đồ giống nhau hết tổng cộng {allsec} giây, mỗi món mất cùng thời gian. Viết thời gian một món theo phút và giây, phần giây nhỏ hơn 60.',
        time_blanks(eachsec,'phút'),f'{allsec} : {number} = {eachsec} giây = {hm(eachsec)[0]} phút {hm(eachsec)[1]} giây.'))
    Q.append(tf('kha',62,'Kiểm tra cách tính.',[('Vận tốc 12 km/h, đi đều trong 30 phút thì được 6 km.',True),('Vận tốc 12 km/h, đi đều trong 30 phút thì được 360 km.',False),('Thời gian nghỉ phải trừ ra khi tính vận tốc lúc đang chạy.',True)],'Đổi 30 phút = 0,5 giờ; 12 × 0,5 = 6 km. Không nhân km/h trực tiếp với số phút.'))
    outward=D('1.5')+D(i-1)/2;v1=D(40);v2=D(50);length=v1*outward;back=length/v2
    Q.append(fill('gioi',60,f'Quãng đường AB dài {n(length)} km. Lượt đi đều {n(v1)} km/h, lượt về trên cùng đường đều {n(v2)} km/h. Không nghỉ.',
        [B('Thời gian lượt đi là',outward*60,'phút'),B('Thời gian lượt về là',back*60,'phút'),B('Tổng thời gian là',(outward+back)*60,'phút')],
        f'Đi: {n(length)} : {n(v1)} = {n(outward)} giờ = {n(outward*60)} phút. Về: {n(length)} : {n(v2)} = {n(back)} giờ = {n(back*60)} phút. Tổng {n((outward+back)*60)} phút.'))
    v1,v2=D(30+5*i),D(40+5*i);d1,d2=v1*D('1.5'),v2*D('.75');pause=10+5*i;whole=135+pause;arrive=8*60+whole
    Q.append(fill('gioi',60,f'Xe khởi hành lúc 8 giờ, đi chặng đầu {n(d1)} km với {n(v1)} km/h, nghỉ {pause} phút, rồi đi {n(d2)} km với {n(v2)} km/h. Mỗi chặng đi đều; đến cùng ngày.',
        [B('Tổng thời gian cả nghỉ là',whole,'phút'),B('Đến nơi lúc',hm(arrive)[0],'giờ'),B('và',hm(arrive)[1],'phút')],
        f'Hai chặng: {n(d1)} : {n(v1)} = 1,5 giờ = 90 phút; {n(d2)} : {n(v2)} = 0,75 giờ = 45 phút. Cộng nghỉ được {whole} phút. Đến {hm(arrive)[0]} giờ {hm(arrive)[1]} phút.'))
    train=D(120+20*i);tunnel=D(180+20*i);v=D(10)
    Q.append(fill('gioi',62,f'Tàu dài {n(train)} m, hầm dài {n(tunnel)} m. Từ lúc đầu tàu chạm cửa vào đến lúc đuôi tàu ra khỏi cửa kia, tàu chạy đều {n(v)} m/s.',
        [B('Đầu tàu phải đi',train+tunnel,'m'),B('Thời gian là',(train+tunnel)/v,'giây')],f'Để cả tàu ra khỏi hầm, đi {n(train)} + {n(tunnel)} = {n(train+tunnel)} m. Thời gian: {n(train+tunnel)} : {n(v)} = {n((train+tunnel)/v)} giây.'))
    slow,fast=D(30+3*i),D(45+3*i);d1,d2=slow,fast*2;average=(d1+d2)/3
    Q.append(fill('gioi',59,f'Xe đi chặng một {n(d1)} km trong 1 giờ, chặng hai {n(d2)} km trong 2 giờ. Không nghỉ. Tính vận tốc trung bình cả hành trình.',
        [B('Tổng quãng đường là',d1+d2,'km'),B('Vận tốc trung bình là',average,'km/h')],f'Tổng quãng đường: {n(d1+d2)} km; tổng thời gian 3 giờ. v = {n(d1+d2)} : 3 = {n(average)} km/h. Không lấy trung bình hai vận tốc khi thời gian hai chặng khác nhau.'))
    minutes=3+i;seconds=minutes*60;v1,v2=D(1),D('1.5')
    Q.append(fill('gioi',62,f'Hai bạn đi từ hai đầu A, B về phía nhau, xuất phát cùng lúc và gặp nhau sau {minutes} phút. Bạn từ A đi đều 1 m/s, bạn từ B đi đều 1,5 m/s.',
        [B('Bạn từ A đã đi',seconds*v1,'m'),B('Bạn từ B đã đi',seconds*v2,'m'),B('Độ dài AB là',seconds*(v1+v2),'m')],
        f'{minutes} phút = {seconds} giây. Hai bạn đi {n(seconds*v1)} m và {n(seconds*v2)} m. AB bằng tổng: {n(seconds*(v1+v2))} m.'))
    start=22*60+30+3*i;travel=90+10*i;rest=15;finish=(start+travel+rest)%1440
    Q.append(fill('gioi',57,f'Xe khởi hành lúc 22 giờ {30+3*i} phút, chạy {travel} phút và nghỉ 15 phút rồi đến nơi vào ngày hôm sau. Phần phút nhỏ hơn 60.',
        [B('Đến nơi lúc',hm(finish)[0],'giờ ngày hôm sau'),B('và',hm(finish)[1],'phút')],
        f'Từ 22 giờ {30+3*i} phút cộng {travel+15} phút. Qua 24 giờ sang ngày hôm sau, đến {hm(finish)[0]} giờ {hm(finish)[1]} phút.'))
    return Q
