"""Original exercises grounded in printed pages 4–39; all arithmetic is exact."""
from fractions import Fraction
from g4lib import B, D, SEL, cmp, d, fill, mc, n, order, tf, write

LESSONS7 = {36: ('Tỉ số. Tỉ số phần trăm', 4), 37: ('Tỉ lệ bản đồ và ứng dụng', 8),
    38: ('Tìm hai số khi biết tổng và tỉ số của hai số đó', 12),
    39: ('Tìm hai số khi biết hiệu và tỉ số của hai số đó', 15),
    40: ('Tìm tỉ số phần trăm của hai số', 18), 41: ('Tìm giá trị phần trăm của một số', 21),
    42: ('Máy tính cầm tay', 23), 43: ('Thực hành và trải nghiệm sử dụng máy tính cầm tay', 27),
    44: ('Luyện tập chung', 28)}
LESSONS8 = {45: ('Thể tích của một hình', 30), 46: ('Xăng-ti-mét khối. Đề-xi-mét khối', 33),
    47: ('Mét khối', 35), 48: ('Luyện tập chung', 38)}


def frac(pre, a, b, post=''):
    f = Fraction(a, b)
    return dict(pre=pre, kind='frac', ans=[f.numerator, f.denominator], post=post, reduced=True)


def choice(level, lesson, stem, correct, wrong, why, i, fig=None):
    opts = [str(correct)] + list(map(str, wrong))
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    return mc(level, lesson, stem, opts, opts.index(str(correct)), why, fig)


def bars(a, b, label_a='Nhóm A', label_b='Nhóm B'):
    rows = ''
    for y, count, label in [(35, a, label_a), (93, b, label_b)]:
        rows += f'<text x="12" y="{y+23}" font-size="19" fill="currentColor">{label}</text>'
        rows += ''.join(f'<rect x="{136+k*36}" y="{y}" width="36" height="32" fill="var(--soft)" stroke="currentColor" stroke-width="2"/>' for k in range(count))
    width=150+max(a,b)*36
    return f'<div class="fig"><figure><svg style="width:{width}px;max-width:100%;height:auto" width="{width}" height="145" viewBox="0 0 {width} 145" role="img" aria-label="Sơ đồ hai nhóm với các phần bằng nhau">{rows}</svg><figcaption>Mỗi ô biểu diễn một phần bằng nhau.</figcaption></figure></div>'


def cubes(heights):
    """One cube deep; every cube is visible. No hidden-block inference."""
    size, dx, dy = 34, 12, 11
    maxh = max(heights)
    shapes = ''
    for col, h in enumerate(heights):
        x = 18 + col * 49
        for row in range(h):
            y = 20 + (maxh - 1 - row) * size
            shapes += f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="var(--soft)" stroke="currentColor" stroke-width="2"/>'
            shapes += f'<path d="M{x+size},{y} l{dx},-{dy} v{size} l-{dx},{dy} Z" fill="#F6B4CD" stroke="currentColor" stroke-width="2"/>'
        top = 20 + (maxh - h) * size
        shapes += f'<path d="M{x},{top} l{dx},-{dy} h{size} l-{dx},{dy} Z" fill="#FFE5EF" stroke="currentColor" stroke-width="2"/>'
    w, h = 30 + len(heights) * 49, 40 + maxh * size
    return f'<div class="fig"><figure><svg style="width:{w}px;max-width:100%;height:auto" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Các cột khối lập phương, tất cả các khối đều nhìn thấy">{shapes}</svg><figcaption>Hình chỉ sâu một khối; không có khối bị che phía sau.</figcaption></figure></div>'


def table(headers, rows):
    return '<div class="fig"><table><thead><tr>' + ''.join(f'<th>{s}</th>' for s in headers) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{s}</td>' for s in row) + '</tr>' for row in rows) + '</tbody></table></div>'


CONTEXT7 = [
    ('Góc học tập', 'bút chì', 'bút màu', 'chiếc', 'quyển vở', 12000),
    ('Hội chợ của lớp', 'thiệp hồng', 'thiệp xanh', 'tấm', 'túi vải', 40000),
    ('Vườn cây nhỏ', 'cây hoa', 'cây rau', 'cây', 'bình tưới', 60000),
    ('Ngày hội thể thao', 'cờ đỏ', 'cờ vàng', 'lá', 'quả bóng', 80000),
    ('Chuyến đi khám phá', 'vé trẻ em', 'vé người lớn', 'vé', 'chiếc mũ', 50000),
    ('Dự án xanh của lớp', 'chai nhựa', 'vỏ hộp', 'chiếc', 'sổ tay', 20000),
]


def questions7(i):
    ctx, obj_a, obj_b, unit, product, price = CONTEXT7[i-1]
    a, b, part = [(2,3,7),(3,5,6),(4,7,5),(3,4,8),(5,7,4),(2,5,9)][i-1]
    small, large = a*part, b*part
    total, diff = small+large, large-small
    percent = [15,20,25,30,10,12][i-1]
    scale, map_cm = [2000,5000,1000,10000,2500,4000][i-1], D(i+2)
    real_m = map_cm*scale/100
    Q = []
    Q.append(fill('tb',36,f'{ctx} có {small} {obj_a} và {large} {obj_b}. Viết tỉ số dưới dạng phân số tối giản.',
        [frac(f'Số {obj_a} so với số {obj_b}:',small,large)],f'Tỉ số là {small}/{large} = {a}/{b}. Đọc đúng thứ tự hai nhóm.'))
    Q.append(fill('tb',36,f'Vẫn với {small} {obj_a} và {large} {obj_b}, hãy phân biệt hai tỉ số.',
        [frac(f'Số {obj_b} so với số {obj_a}:',large,small),frac(f'Số {obj_a} so với tổng số đồ vật:',small,total)],
        f'Tổng: {small} + {large} = {total}. Hai tỉ số lần lượt là {b}/{a} và {a}/{a+b}.'))
    Q.append(choice('tb',36,f'Tỉ số {{{percent}/100}} viết thành tỉ số phần trăm là:',f'{percent}%',
        [f'{n(D(percent)/100)}%',f'{percent*10}%',f'{100-percent}%'],f'{percent}/100 = {percent}%.',i))
    base=D(200+40*i); value=base*percent/100
    Q.append(fill('tb',41,f'Tính {percent}% của {n(base)}.',[B('Kết quả là',value)],f'{n(base)} × {percent} : 100 = {n(value)}.'))
    Q.append(choice('tb',37,f'Tỉ lệ 1 : {n(scale)} cho biết 1 cm trên bản đồ ứng với:',f'{n(scale)} cm ngoài thực tế',
        [f'{n(scale)} m ngoài thực tế','1 cm ngoài thực tế',f'{n(scale)} km ngoài thực tế'],
        'Độ dài trên bản đồ và độ dài thật phải dùng cùng một đơn vị khi áp dụng tỉ lệ.',i+1))
    Q.append(fill('tb',37,f'Trên sơ đồ giả định tỉ lệ 1 : {n(scale)}, đoạn đường dài {n(map_cm)} cm.',[B('Độ dài thật là',real_m,'m')],
        f'{n(map_cm)} × {n(scale)} = {n(map_cm*scale)} cm = {n(real_m)} m.'))
    Q.append(fill('tb',38,f'Hai nhóm có tất cả {total} {unit}. Số của nhóm A bằng {{{a}/{b}}} số của nhóm B.',
        [B('Nhóm A có',small,unit),B('Nhóm B có',large,unit)],f'Tổng số phần: {a} + {b} = {a+b}. Một phần: {total} : {a+b} = {part}. Nhóm A: {part} × {a} = {small}; nhóm B: {part} × {b} = {large}.',bars(a,b)))
    Q.append(fill('tb',39,f'Nhóm B có nhiều hơn nhóm A {diff} {unit}. Số của nhóm A bằng {{{a}/{b}}} số của nhóm B.',
        [B('Nhóm A có',small,unit),B('Nhóm B có',large,unit)],f'Hiệu số phần: {b} − {a} = {b-a}. Một phần: {diff} : {b-a} = {part}. Nhóm A: {part} × {a} = {small}; nhóm B: {part} × {b} = {large}.'))
    key, role, wrong = [('CE','xóa số vừa nhập',['tắt máy','hiện kết quả','nhập phép nhân']),('OFF','tắt máy',['hiện kết quả','xóa riêng số vừa nhập','bật máy']),('=','hiện kết quả',['tắt máy','nhập số 0','xóa số vừa nhập']),('ON/C','bật máy hoặc xóa toàn bộ phép tính',['chỉ xóa chữ số cuối','nhập dấu chia','nhập dấu trừ']),('CE','xóa số vừa nhập',['đổi đơn vị','tự kiểm tra lời giải','hiện kết quả']),('=','hiện kết quả',['nhập dấu cộng','tắt máy','xóa số vừa nhập'])][i-1]
    Q.append(choice('tb',42,f'Trên loại máy tính cơ bản minh họa trong sách, phím {key} dùng để:',role,wrong,f'Phím {key}: {role}. Cách ghi phím có thể khác tùy máy.',i+2))
    x,y = D('12.5')+i,D(4+i)
    Q.append(fill('tb',42,f'Dùng máy tính hoặc tính rồi kiểm tra: {n(x)} × {n(y)}.',[B('Màn hình cần hiện',x*y)],f'{n(x)} × {n(y)} = {n(x*y)}.'))
    checked,all_=D(15+3*i),D(60)
    Q.append(fill('kha',40,f'Bảng kiểm kê tại {ctx.lower()}: tổng {n(all_)} đồ vật, {n(checked)} đồ vật màu hồng.',
        [B('Tỉ số phần trăm màu hồng là',checked/all_*100,'%'),B('Tỉ số phần trăm còn lại là',(all_-checked)/all_*100,'%')],
        f'{n(checked)} : {n(all_)} × 100 = {n(checked/all_*100)}%. Còn lại: 100% − {n(checked/all_*100)}% = {n((all_-checked)/all_*100)}%.',table(['Màu hồng','Màu khác','Tổng'],[[n(checked),n(all_-checked),n(all_)]])))
    reverse_m=real_m+D(scale)/100
    Q.append(fill('kha',37,f'Một đoạn đường giả định dài {n(reverse_m)} m. Sơ đồ có tỉ lệ 1 : {n(scale)}.',[B('Độ dài trên sơ đồ là',reverse_m*100/scale,'cm')],
        f'Đổi {n(reverse_m)} m = {n(reverse_m*100)} cm. Chia {n(scale)} được {n(reverse_m*100/scale)} cm.'))
    more=part+3; s,l=a*more,b*more
    Q.append(fill('kha',38,f'Hai tổ làm {s+l} {unit}. Tổ một làm bằng {{{a}/{b}}} tổ hai.',[B('Tổ một làm',s,unit),B('Tổ hai làm',l,unit)],
        f'Một phần: {s+l} : ({a} + {b}) = {more}. Hai tổ: {more} × {a} = {s}; {more} × {b} = {l}.'))
    Q.append(fill('kha',39,f'Tổ hai làm hơn tổ một {l-s} {unit}. Tổ hai làm bằng {{{b}/{a}}} tổ một.',[B('Tổ một làm',s,unit),B('Tổ hai làm',l,unit)],
        f'Tỉ số tổ hai : tổ một = {b} : {a}. Một phần: {l-s} : ({b} − {a}) = {more}. Tổ một {s}, tổ hai {l}.'))
    discount=D(price)*percent/100
    Q.append(fill('kha',41,f'Một {product} giá {n(price)} đồng được giảm {percent}% giá niêm yết.',[B('Số tiền giảm là',discount,'đồng'),B('Giá sau giảm là',D(price)-discount,'đồng')],
        f'Giảm: {n(price)} × {percent} : 100 = {n(discount)} đồng. Còn trả: {n(price)} − {n(discount)} = {n(D(price)-discount)} đồng.'))
    p,q=D('17.5')+i,D('6.25')+i
    Q.append(fill('kha',40,'Tính với tỉ số phần trăm.',[B(f'{n(p)}% + {n(q)}% =',p+q,'%'),B(f'{n(p)}% × 2 =',p*2,'%')],f'Cộng: {n(p+q)}%; nhân: {n(p*2)}%. Giữ kí hiệu % sau kết quả.'))
    fractions=sorted([Fraction(i,10),Fraction(i+2,10),Fraction(i+1,10),Fraction(i+3,10)])
    Q.append(order('kha',36,'Sắp xếp các tỉ số từ bé đến lớn.',[f'{{{f.numerator}/{f.denominator}}}' for f in fractions],'<',
        'Quy đồng về mẫu số 10 rồi so sánh tử số: '+ ' < '.join(str(f) for f in fractions)+'.'))
    Q.append(tf('kha',44,'Chọn Đúng hoặc Sai cho mỗi nhận xét.',[(f'{percent}% = {{{percent}/100}}.',True),('Tỉ số của A và B luôn bằng tỉ số của B và A.',False),
        ('Tìm số bé theo tổng và tỉ số: chia tổng cho tổng số phần, rồi nhân số phần của số bé.',True),('Đổi 1 m thành 1 cm rồi dùng tỉ lệ bản đồ là đúng.',False)],
        f'{percent}% là {percent}/100. Đảo thứ tự thường làm đổi tỉ số. Tổng–tỉ dùng tổng số phần. 1 m = 100 cm.'))
    Q.append(fill('gioi',38,f'Hai nhóm góp {total*3} {unit}, số của nhóm A bằng {{{a}/{b}}} nhóm B. Sau đó nhóm A dùng {small} {unit}.',
        [B('Ban đầu nhóm A có',small*3,unit),B('Nhóm A còn',small*2,unit)],f'Một phần: {total*3} : {a+b} = {part*3}. Nhóm A: {part*3} × {a} = {small*3}. Còn: {small*3} − {small} = {small*2}.'))
    Q.append(fill('gioi',39,f'Hai tổ bán {product}. Tổ B bán nhiều hơn tổ A {diff} chiếc; số tổ A bằng {{{a}/{b}}} số tổ B. Mỗi chiếc bán {n(price)} đồng.',
        [B('Tổ B bán',large,'chiếc'),B('Tổ B thu',large*price,'đồng')],f'Một phần: {diff} : ({b} − {a}) = {part}. Tổ B bán {part} × {b} = {large} chiếc; thu {large} × {n(price)} = {n(large*price)} đồng.'))
    Q.append(fill('gioi',37,f'Sơ đồ giả định tỉ lệ 1 : {n(scale)}: từ A đến B dài {n(map_cm)} cm, từ B đến C dài {n(map_cm+1)} cm. Đi từ A qua B tới C.',
        [B('Tổng độ dài trên sơ đồ là',map_cm*2+1,'cm'),B('Quãng đường thật là',(map_cm*2+1)*scale/100,'m')],
        f'Cộng hai chặng: {n(map_cm)} + {n(map_cm+1)} = {n(map_cm*2+1)} cm. Nhân {n(scale)} rồi chia 100: {n((map_cm*2+1)*scale/100)} m.'))
    count=8+i; raw=D(price)*count; payable=raw*(100-percent)/100
    Q.append(fill('gioi',43,f'Gian hàng giả định giảm {percent}% tổng tiền khi mua từ 10 {product} trở lên. Mỗi chiếc giá {n(price)} đồng. Mua {count} chiếc. Có thể dùng máy tính.',
        [B('Tiền trước giảm là',raw,'đồng'),B('Thực tế phải trả',payable if count>=10 else raw,'đồng')],
        f'Tổng: {count} × {n(price)} = {n(raw)} đồng. '+(f'{count} ≥ 10 nên giảm {percent}%, còn {n(payable)} đồng.' if count>=10 else f'{count} < 10 nên không được giảm, trả {n(raw)} đồng.')))
    amount=D(50000+10000*i); fee=D(3000+1000*i); reserve=amount*percent/100
    Q.append(fill('gioi',43,f'Lớp có {n(amount)} đồng, dành {percent}% để mua hạt giống và {n(fee)} đồng mua nhãn. Phần còn lại dùng mua giấy. Dùng máy tính để kiểm tra.',
        [B('Tiền hạt giống là',reserve,'đồng'),B('Tiền mua giấy là',amount-reserve-fee,'đồng')],
        f'Hạt giống: {n(amount)} × {percent} : 100 = {n(reserve)}. Giấy: {n(amount)} − {n(reserve)} − {n(fee)} = {n(amount-reserve-fee)} đồng.'))
    plan=D(100+20*i); achieved=D([110,115,120,125,130,140][i-1]); done=plan*achieved/100
    Q.append(fill('gioi',44,f'Kế hoạch thu gom {n(plan)} chai nhựa. Lớp thực tế thu {n(done)} chai.',[B('Đã đạt',done/plan*100,'% kế hoạch'),B('Vượt kế hoạch', (done-plan)/plan*100,'%')],
        f'Đạt: {n(done)} : {n(plan)} × 100 = {n(achieved)}%. Vượt: ({n(achieved)} − 100)% = {n(achieved-100)}%. Không nhầm phần đã đạt và phần vượt.'))
    return Q


CONTEXT8 = ['Góc xếp hình','Phòng thí nghiệm nhỏ','Gian hàng đồ dùng','Nước cho vườn cây','Kho hàng gọn gàng','Thử thách thể tích']


def questions8(i):
    Q=[]; u=D(i)+D('0.25'); v=D(i)+D('0.75'); heights=[i%3+1,2,3,1]; count=sum(heights)
    Q.append(choice('tb',46,'Một xăng-ti-mét khối là thể tích của:', 'hình lập phương cạnh 1 cm',
        ['hình vuông cạnh 1 cm','hình lập phương cạnh 1 dm','đoạn thẳng dài 1 cm'],'Đơn vị thể tích gắn với khối lập phương, không phải hình phẳng hay độ dài.',i))
    Q.append(fill('tb',45,'Mỗi khối nhỏ trong hình có cùng kích thước. Đếm số khối.',[B('Hình gồm',count,'khối')],
        'Đếm theo từng cột: '+' + '.join(map(str,heights))+f' = {count} khối.',cubes(heights)))
    Q.append(fill('tb',46,'Đổi về xăng-ti-mét khối.',[B(f'{n(u)} dm³ =',u*1000,'cm³')],f'1 dm³ = 1 000 cm³. {n(u)} × 1 000 = {n(u*1000)} cm³.'))
    Q.append(choice('tb',47,'1 m³ bằng bao nhiêu dm³?', '1 000 dm³',['10 dm³','100 dm³','1 000 000 dm³'],'1 m³ = 1 000 dm³. Không nhầm hệ số đổi thể tích với độ dài hoặc diện tích.',i+1))
    Q.append(fill('tb',47,'Đổi về đề-xi-mét khối.',[B(f'{n(v)} m³ =',v*1000,'dm³')],f'{n(v)} × 1 000 = {n(v*1000)} dm³.'))
    cm=D(1250+250*i)
    Q.append(fill('tb',46,'Đổi về đề-xi-mét khối.',[B(f'{n(cm)} cm³ =',cm/1000,'dm³')],f'{n(cm)} : 1 000 = {n(cm/1000)} dm³.'))
    Q.append(tf('tb',45,'Chọn Đúng hoặc Sai.',[('Hình lập phương có sáu mặt là các hình vuông bằng nhau.',True),('Hình hộp chữ nhật có ba kích thước: dài, rộng, cao.',True),
        ('Xếp lại cùng số khối nhỏ, không thêm bớt, thì tổng thể tích thay đổi.',False)],'Khối lập phương có sáu mặt vuông bằng nhau. Xếp lại không thêm bớt khối thì tổng thể tích được giữ nguyên.'))
    aa,bb=D(300+100*i),D('0.9')+D(i)/10
    Q.append(fill('tb',46,'Đọc bảng và điền dấu so sánh.',[SEL(f'{n(aa)} cm³',cmp(aa,bb*1000),f'{n(bb)} dm³')],f'{n(bb)} dm³ = {n(bb*1000)} cm³; so sánh {n(aa)} với {n(bb*1000)}.',
        table(['Hộp A','Hộp B'],[[f'{n(aa)} cm³',f'{n(bb)} dm³']])))
    Q.append(fill('tb',46,'Tính với cùng đơn vị.',[B(f'{n(u)} dm³ + {n(v)} dm³ =',u+v,'dm³'),B(f'{n(v)} dm³ − {n(u)} dm³ =',v-u,'dm³')],f'Cộng được {n(u+v)} dm³; trừ được {n(v-u)} dm³.'))
    Q.append(choice('tb',47,'Đơn vị nào phù hợp nhất để ghi thể tích nước trong một bể bơi lớn?', 'm³',['cm','cm²','g'],'Thể tích nước bể bơi lớn thường được ghi bằng mét khối; cm là độ dài, cm² là diện tích, g là khối lượng.',i+2))
    Q.append(fill('kha',46,'Đổi số đo có hai đơn vị.',[B(f'{i+1} dm³ {125+i*10} cm³ =',D(i+1)*1000+125+i*10,'cm³'),B(f'{i+1} dm³ {125+i*10} cm³ =',D(i+1)+D(125+i*10)/1000,'dm³')],
        f'Phần dm³ nhân 1 000 để đổi sang cm³; hoặc phần cm³ chia 1 000 để đổi sang dm³, rồi cộng. Kết quả: {n(D(i+1)*1000+125+i*10)} cm³ = {n(D(i+1)+D(125+i*10)/1000)} dm³.'))
    measures=[(D(i)*1000+100,f'{n(D(i)+D("0.1"))} dm³'),(D(i)*1000+200,f'{n(D(i)*1000+200)} cm³'),(D(i)*1000+300,f'{n((D(i)*1000+300)/1000000)} m³'),(D(i)*1000+400,f'{n(D(i)+D("0.4"))} dm³')]
    Q.append(order('kha',48,'Sắp xếp các số đo thể tích từ bé đến lớn.',[s for _,s in measures],'<','Đổi tất cả về cm³: '+' < '.join(n(x) for x,_ in measures)+'.'))
    Q.append(fill('kha',47,'Đổi về cùng đơn vị rồi so sánh.',[SEL(f'{n(u)} m³',cmp(u*1000,u*1000-10),f'{n(u*1000-10)} dm³'),SEL(f'{n(v*1000)} cm³','=',f'{n(v)} dm³')],
        f'{n(u)} m³ = {n(u*1000)} dm³, lớn hơn {n(u*1000-10)} dm³. {n(v*1000)} cm³ = {n(v)} dm³.'))
    per, layers = 5+i, 2+i%3
    Q.append(fill('kha',45,f'Một mô hình có {layers} lớp. Mỗi lớp có đúng {per} khối lập phương nhỏ bằng nhau, kể cả khối bị che. Các lớp xếp kín, không có khoảng trống.',
        [B('Cả mô hình có',per*layers,'khối')],f'Đếm theo lớp: {per} × {layers} = {per*layers} khối. Không chỉ đếm các mặt nhìn thấy.'))
    initial=D(50+10*i); removed=D(12+i)
    Q.append(fill('kha',45,f'Khối ban đầu gồm {n(initial)} khối nhỏ bằng nhau. Tháo {n(removed)} khối ra, rồi chia số khối còn lại thành hai phần bằng nhau.',
        [B('Số khối còn lại là',initial-removed,'khối'),B('Mỗi phần có',(initial-removed)/2,'khối')],f'Còn {n(initial)} − {n(removed)} = {n(initial-removed)} khối; chia 2 được {n((initial-removed)/2)} khối.'))
    # Keep counts integral: the remaining count is explicitly constructed as even.
    if (initial-removed)%2:
        initial+=1
        Q[-1]=fill('kha',45,f'Có {n(initial)} khối nhỏ bằng nhau. Tháo {n(removed)} khối rồi chia phần còn lại thành hai nhóm bằng nhau.',[B('Còn lại',initial-removed,'khối'),B('Mỗi nhóm có',(initial-removed)/2,'khối')],f'({n(initial)} − {n(removed)}) : 2 = {n((initial-removed)/2)} khối mỗi nhóm.')
    bottles=4+i; each=D('0.25')
    Q.append(fill('kha',46,f'Có {bottles} chai, mỗi chai chứa {n(each)} lít nước. Cho biết 1 lít = 1 dm³.',[B('Tổng lượng nước là',bottles*each,'dm³'),B('Tổng lượng nước là',bottles*each*1000,'cm³')],f'{bottles} × 0,25 = {n(bottles*each)} lít = {n(bottles*each)} dm³ = {n(bottles*each*1000)} cm³.'))
    Q.append(tf('kha',48,'Nhận xét về đổi đơn vị thể tích.',[(f'{i} m³ = {i*1000} dm³.',True),(f'{i} dm³ = {i*100} cm³.',False),('1 m³ = 1 000 000 cm³.',True),('1 dm³ = 0,001 m³.',True)],
        'Hai đơn vị thể tích liền nhau hơn kém 1 000 lần; m³ sang cm³ qua hai bậc nên nhân 1 000 000.'))
    morning, afternoon=D(i+1),D(500+100*i)
    Q.append(fill('kha',47,'Đọc bảng lượng nước đã tưới trong ngày.',[B('Tổng cả ngày là',morning+afternoon/1000,'m³')],f'{n(afternoon)} dm³ = {n(afternoon/1000)} m³. Tổng: {n(morning)} + {n(afternoon/1000)} = {n(morning+afternoon/1000)} m³.',
        table(['Buổi sáng','Buổi chiều'],[[f'{n(morning)} m³',f'{n(afternoon)} dm³']])))
    h2=[2+i%2,1,3,2,1]; add=3+i
    Q.append(fill('gioi',48,f'Mỗi khối nhỏ trong hình có thể tích 1 cm³. Thêm {add} khối cùng loại để tạo hình mới.',[B('Thể tích hình ban đầu là',sum(h2),'cm³'),B('Thể tích hình mới là',sum(h2)+add,'cm³')],
        'Ban đầu: '+' + '.join(map(str,h2))+f' = {sum(h2)} cm³. Thêm {add} cm³ được {sum(h2)+add} cm³.',cubes(h2)))
    water=D(2+i)*D('0.5'); cup=D(250)
    Q.append(fill('gioi',46,f'Bình có {n(water)} lít nước. Rót đầy các cốc, mỗi cốc chứa 250 cm³. Biết 1 lít = 1 dm³; bỏ qua hao hụt.',[B('Bình chứa',water*1000,'cm³'),B('Rót đầy được',water*1000/cup,'cốc')],f'{n(water)} × 1 000 = {n(water*1000)} cm³. Số cốc: {n(water*1000)} : 250 = {n(water*1000/cup)}.'))
    capacity=D(5+i); occupied=D(60+5*i); free=capacity*(100-occupied)/100
    Q.append(fill('gioi',47,f'Thùng chứa có thể tích {n(capacity)} m³. Hàng chiếm {n(occupied)}% thể tích thùng.',[B('Phần trống chiếm',100-occupied,'%'),B('Thể tích phần trống là',free,'m³'),B('Đổi phần trống ra',free*1000,'dm³')],
        f'Phần trống: 100% − {n(occupied)}% = {n(100-occupied)}%. Thể tích: {n(capacity)} × {n(100-occupied)} : 100 = {n(free)} m³ = {n(free*1000)} dm³.'))
    use=D(11+i); first=D(6000); second=D(8000); cost=10*first+(use-10)*second
    Q.append(fill('gioi',47,f'Bảng giá nước GIẢ ĐỊNH: 10 m³ đầu giá 6 000 đồng/m³; phần dùng vượt 10 m³ giá 8 000 đồng/m³. Gia đình dùng {n(use)} m³. Không tính phí khác.',[B('Tiền 10 m³ đầu là',10*first,'đồng'),B('Tổng tiền là',cost,'đồng')],
        f'10 × 6 000 = 60 000 đồng. Phần vượt: {n(use)} − 10 = {n(use-10)} m³. Tổng: 60 000 + {n(use-10)} × 8 000 = {n(cost)} đồng.'))
    year=D(144+12*i); avg=year/12
    Q.append(fill('gioi',48,f'Trong 12 tháng, gia đình dùng tổng cộng {n(year)} m³ nước.',[B('Trung bình mỗi tháng dùng',avg,'m³'),B('Đổi trung bình mỗi tháng ra',avg*1000,'dm³')],f'{n(year)} : 12 = {n(avg)} m³ = {n(avg*1000)} dm³.'))
    layers,per,minus=3+i%2,8+i,2+i
    Q.append(fill('gioi',48,f'Mô hình có {layers} lớp, mỗi lớp {per} khối 1 dm³, không có khoảng trống. Tháo {minus} khối khỏi mô hình.',[B('Ban đầu có',layers*per,'khối'),B('Thể tích còn lại là',(layers*per-minus)*1000,'cm³')],
        f'Ban đầu {layers} × {per} = {layers*per} khối. Còn {layers*per} − {minus} = {layers*per-minus} khối, tức {layers*per-minus} dm³ = {n((layers*per-minus)*1000)} cm³.'))
    return Q


def generate():
    for cd, builder in [(7,questions7),(8,questions8)]:
        for i in range(1,7):
            write(i,builder(i),cd=cd)
