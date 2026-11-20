"""Seven source-grounded study cards per topic, with original worked examples."""
from .topics910 import LESSONS9, LESSONS10, box_fig, cylinder_net


def sheets(gen_sheet):
    bodies9 = [
        ('Gấp đủ các mặt, không chồng lên nhau.',
         cylinder_net()+'Hình lập phương có 6 mặt vuông bằng nhau; hình hộp chữ nhật có 3 cặp mặt chữ nhật bằng nhau. Hình trụ có 2 đáy tròn bằng nhau và mặt bên trải thành hình chữ nhật.<br><b>Thử:</b> vẽ 4 hình vuông thành hàng, thêm 1 ô trên và 1 ô dưới ô thứ hai; nhờ người lớn cắt rồi gấp. Không phải mọi tấm bìa gồm 6 ô vuông đều gấp được thành lập phương.'),
        ('Phân biệt bốn mặt bên với tất cả các mặt.',
         box_fig(8,4,3)+'Gọi chiều dài a, chiều rộng b, chiều cao h, cùng đơn vị.<br><b>S xung quanh = (a + b) × 2 × h.</b><br><b>S toàn phần hộp kín = S xung quanh + a × b × 2.</b><br>Hộp 8 × 4 × 3 cm: xung quanh 72 cm²; toàn phần 136 cm². Bể không nắp chỉ thêm một đáy: 72 + 32 = 104 cm² (bỏ qua độ dày, mép ghép).'),
        ('Một mặt vuông trước, rồi đếm số mặt cần tính.',
         'Lập phương cạnh c: diện tích một mặt = c × c.<br><b>S xung quanh = c × c × 4.</b><br><b>S toàn phần = c × c × 6.</b><br>Cạnh 5 cm: xung quanh 100 cm²; toàn phần 150 cm². Phủ mặt trên và 4 mặt bên thì chỉ tính 5 mặt, được 125 cm².'),
        ('Thể tích hộp = diện tích đáy × chiều cao.',
         '<b>V = a × b × h</b>, ba kích thước cùng đơn vị.<br>Hộp dài 8 dm, rộng 4 dm, cao 3 dm: V = 8 × 4 × 3 = 96 dm³.<br>Biết V = 96 dm³ và đáy 32 dm²: cao 96 : 32 = 3 dm.<br>Đổi 0,8 m thành 80 cm trước khi nhân với chiều rộng và cao tính bằng cm. Kết quả thể tích dùng đơn vị khối.'),
        ('Lập phương có ba kích thước bằng nhau.',
         '<b>V = c × c × c.</b><br>Cạnh 4 cm: V = 4 × 4 × 4 = 64 cm³.<br>Ghép 2 khối cạnh 4 cm chung trọn một mặt: thể tích 128 cm³; diện tích ngoài (6 + 6 − 2) × 16 = 160 cm². Hai mặt tiếp xúc bị che đi, không cộng vào diện tích ngoài.'),
        ('Ước lượng rồi kiểm tra cách xếp thực tế.',
         'Thùng trong lòng 6 × 4 × 6 dm, hộp nhỏ cạnh 2 dm, xếp thẳng không khe hở: mỗi lớp (6 : 2) × (4 : 2) = 6 hộp; 3 lớp được 18 hộp.<br><b>Không chỉ chia thể tích:</b> phải kiểm tra kích thước hộp nhỏ có xếp vừa từng chiều không.<br>Thực hành cùng người lớn: dùng khối đồ chơi cùng cỡ, ước lượng rồi đếm theo lớp. Không cần cắt vật cứng hay dùng vật sắc.'),
        ('Đọc đơn vị và điều kiện của bình nước.',
         '1 m³ = 1 000 dm³; 1 dm³ = 1 000 cm³ = 1 lít.<br>Bình đáy trong lòng 10 × 6 cm, vật chìm hoàn toàn làm nước dâng 0,5 cm: thể tích vật 10 × 6 × 0,5 = 30 cm³, nếu không tràn và vật không hút nước.<br>Đổ 240 cm³ nước vào bình thành thẳng đứng, đáy 80 cm², đủ cao: nước cao 240 : 80 = 3 cm.<br><b>Tự kiểm:</b> diện tích là đơn vị vuông; thể tích là đơn vị khối. Hộp không nắp khác hộp kín.')]
    bodies10 = [
        ('Giờ, phút, giây đổi theo 60.',
         '1 thế kỉ = 100 năm; 1 năm = 12 tháng; 1 tuần = 7 ngày; 1 ngày = 24 giờ; 1 giờ = 60 phút; 1 phút = 60 giây.<br>2 giờ 15 phút = 135 phút = 2,25 giờ. <b>1 giờ 30 phút = 1,5 giờ</b>, không phải 1,3 giờ.<br>Tháng 1, 3, 5, 7, 8, 10, 12 có 31 ngày; tháng 4, 6, 9, 11 có 30 ngày. Tháng Hai có 28 ngày, năm nhuận có 29 ngày. Năm thường 365 ngày, năm nhuận 366 ngày.'),
        ('Cộng có nhớ, trừ có mượn theo 60.',
         '2 giờ 45 phút + 35 phút = 2 giờ 80 phút = <b>3 giờ 20 phút</b>.<br>4 giờ 10 phút − 1 giờ 45 phút: đổi 4 giờ 10 phút thành 3 giờ 70 phút, được <b>2 giờ 25 phút</b>.<br>Khởi hành 23 giờ 40 phút, đi 50 phút: đến 0 giờ 30 phút ngày hôm sau.<br>Khi đề có giờ ở các nơi khác nhau, dùng bảng chênh lệch giờ được cung cấp; không tự đoán múi giờ.'),
        ('Có thể đổi hết về một đơn vị để tính.',
         '2 phút 35 giây × 4 = 155 × 4 = 620 giây = <b>10 phút 20 giây</b>.<br>6 giờ 30 phút : 3 = 390 : 3 = 130 phút = <b>2 giờ 10 phút</b>.<br>Ở ô điền giờ–phút hoặc phút–giây, phần phút/giây phải từ 0 đến 59. Đừng viết 1 giờ 90 phút khi yêu cầu đã đổi gọn.'),
        ('Vận tốc cho biết quãng đường trong một đơn vị thời gian.',
         route_example()+'<b>v = s : t.</b> Đi đều 18 km trong 0,5 giờ: 18 : 0,5 = 36 km/h.<br>36 km/h = 36 000 m trong 3 600 giây = 10 m/s.<br>Chọn đơn vị tương ứng: km với giờ → km/h; m với giây → m/s. Không chia số km cho số phút rồi ghi km/h.'),
        ('Từ hai đại lượng đã biết, tìm đại lượng còn lại.',
         '<b>s = v × t; t = s : v.</b><br>Đi 40 km/h trong 1 giờ 30 phút: đổi thành 1,5 giờ → s = 60 km.<br>Đi 90 km với 45 km/h: t = 2 giờ.<br>Thời điểm đến = thời điểm đi + thời gian di chuyển + thời gian nghỉ. Nếu hỏi vận tốc lúc chạy, trừ thời gian nghỉ trước khi tính.'),
        ('Đo, ghi đơn vị rồi mới tính; đọc yêu cầu làm tròn.',
         'Thẻ đo giả định: đi 33 m trong 24 giây → v = 33 : 24 = 1,375 m/s; làm tròn đến một chữ số thập phân được <b>1,4 m/s</b>.<br>Đường A: 90 km với 60 km/h mất 1,5 giờ; đường B: 80 km với 40 km/h mất 2 giờ. Đường ngắn hơn chưa chắc đi nhanh hơn.<br>Thực hành: cùng người lớn chọn đoạn đường an toàn, đo độ dài và bấm giờ đi bộ; không thử trên đường xe chạy. Thẻ trong đề là số liệu giả định.'),
        ('Tách từng chặng; thử lại bằng đơn vị.',
         'Chặng một 30 km trong 1 giờ; chặng hai 90 km trong 2 giờ, không nghỉ. Tổng 120 km trong 3 giờ → vận tốc trung bình <b>40 km/h</b>; không lấy trung bình hai vận tốc khi thời gian khác nhau.<br>Đoàn tàu dài 120 m qua hầm dài 180 m: từ đầu tàu vào đến đuôi tàu ra hết, đầu tàu đi 120 + 180 = 300 m.<br>Hai bạn gặp sau 4 phút: đổi 240 giây, tính riêng quãng đường mỗi bạn đã đi rồi cộng nếu cần độ dài đường ban đầu.')]
    output=[]
    for cd,source,bodies,shorts,title,col,bg,pages,intro in [
        (9,LESSONS9,bodies9,['Hình khai triển','Diện tích hộp','Diện tích lập phương','Thể tích hộp','Thể tích lập phương','Thực hành','Ôn chung'],'DIỆN TÍCH VÀ THỂ TÍCH CỦA MỘT SỐ HÌNH KHỐI','#8C5079','#F9E9F3','40–63','Đếm đúng mặt, chọn đúng đơn vị.'),
        (10,LESSONS10,bodies10,['Đổi thời gian','Cộng, trừ','Nhân, chia','Vận tốc','Quãng đường, thời gian','Thực hành','Ôn chung'],'SỐ ĐO THỜI GIAN. VẬN TỐC. CHUYỂN ĐỘNG ĐỀU','#486A9B','#EAF0FA','64–86','Đổi đúng thời gian, đọc rõ lúc chạy và lúc nghỉ.')]:
        lessons=[dict(n=num,title=t,pg=pg,col=col,bg=bg,dk=col,head=head,
            body=lambda c,text=body:'<div style="font-size:24px;line-height:1.65">'+text.replace('<svg style="','<svg style="color:#4A2433;--soft:#FCE4EC;')+'</div>')
            for (num,(t,pg)),(head,body) in zip(source.items(),bodies)]
        sheet=gen_sheet(cd,title,f'Bài {min(source)} đến Bài {max(source)} · Toán 5, tập hai',col,bg,lessons,shorts,intro,
            'Đọc từng bài, xem ví dụ rồi luyện sáu đề theo ba mức độ. Kết quả được lưu trên trình duyệt này.',
            f'Bám sách Toán 5, tập hai (Kết nối tri thức với cuộc sống), trang {pages}. Ví dụ, sơ đồ và đề tự soạn.')
        output.append((cd,sheet,col))
    return output


def route_example():
    from .topics910 import route_fig
    return route_fig(18)
