"""Study summaries, original examples and exact SVG diagrams; no book scans."""
from .content import LESSONS7, LESSONS8, bars, cubes


def sheets(gen_sheet):
    colours = {7: ('#A15B27','#FFF0DF'),8: ('#316F87','#E2F3F8')}
    bodies7 = [
        ('Đọc đúng thứ tự: số đứng trước so với số đứng sau.',
         'Có 8 bút hồng và 12 bút xanh. Tỉ số bút hồng : bút xanh = 8 : 12 = 2 : 3; bút hồng : tất cả = 8 : 20 = 2 : 5.<br><b>Phần trăm:</b> 35/100 = 35%; 1/4 = 25%. Tỉ số có thể lớn hơn 1, nên phần trăm có thể lớn hơn 100%.'),
        ('Đổi về cùng đơn vị trước khi dùng tỉ lệ.',
         '<b>Tỉ lệ 1 : 2 000:</b> 1 cm trên bản đồ ứng với 2 000 cm ngoài thực tế.<br>Trên bản đồ 4 cm → thật 4 × 2 000 = 8 000 cm = 80 m.<br>Thật 90 m = 9 000 cm → bản đồ 9 000 : 2 000 = 4,5 cm.<br><b>Lưu ý:</b> không đo kích thước bằng thước trên màn hình; dùng số đo ghi trong đề.'),
        ('Biết tổng → dùng tổng số phần bằng nhau.',
         bars(2,3)+'Tổng 45 chiếc; nhóm A bằng 2/3 nhóm B.<br>Tổng số phần: 2 + 3 = 5. Một phần: 45 : 5 = 9 chiếc.<br>Nhóm A: 9 × 2 = 18 chiếc. Nhóm B: 45 − 18 = 27 chiếc.<br><b>Kiểm tra:</b> 18 + 27 = 45 và 18 : 27 = 2 : 3.'),
        ('Biết hiệu → dùng hiệu số phần bằng nhau.',
         bars(3,5)+'Nhóm B hơn A 14 chiếc; A bằng 3/5 nhóm B.<br>Hiệu số phần: 5 − 3 = 2. Một phần: 14 : 2 = 7 chiếc.<br>Nhóm A: 7 × 3 = 21; nhóm B: 7 × 5 = 35 chiếc.<br><b>Kiểm tra:</b> 35 − 21 = 14 và 21 : 35 = 3 : 5.'),
        ('Tìm phần trăm của A so với B: A : B × 100%.',
         'Có 21 trong 60 đồ vật màu hồng: 21 : 60 = 0,35 = 35%.<br>Đạt 125% kế hoạch nghĩa là vượt 25% kế hoạch, không phải vượt 125%.<br><b>Thương không kết thúc:</b> đọc yêu cầu đề về lấy chữ số; sách có bài lấy thương đến bốn chữ số thập phân. Các đề này dùng số chia hết, không yêu cầu đoán cách làm tròn.'),
        ('Tìm p% của A: A × p : 100.',
         '20% của 75 = 75 × 20 : 100 = 15.<br>Món đồ 80 000 đồng giảm 15%: giảm 12 000 đồng; còn trả 68 000 đồng.<br><b>Chú ý:</b> tiền giảm khác với tiền phải trả. Tính phần trăm theo đúng số gốc được nêu.'),
        ('Máy tính giúp kiểm tra; em vẫn phải chọn đúng phép tính.',
         '<b>ON/C:</b> bật máy/xóa toàn bộ; <b>OFF:</b> tắt; <b>CE:</b> xóa số vừa nhập; <b>=:</b> hiện kết quả (tùy máy có nhãn khác).<br>Kiểm tra 18,5 × 6 = 111 bằng máy tính hoặc ứng dụng.<br><b>Thứ tự phép tính:</b> một số máy cơ bản tính theo thứ tự bấm. Với 4 + 3 × 2, tính 3 × 2 = 6 trước, rồi cộng 4 được 10. Không mặc định mọi máy đều tự ưu tiên phép nhân.'),
        ('Đọc điều kiện khuyến mãi trước khi bấm máy.',
         'Gian hàng giả định bán túi 40 000 đồng/chiếc. Giảm 20% khi mua từ 10 chiếc.<br>Mua 9 chiếc: 9 × 40 000 = 360 000 đồng, không đủ điều kiện giảm.<br>Mua 12 chiếc: 480 000 đồng trước giảm; trả 480 000 × 80 : 100 = 384 000 đồng.<br>Em có thể dùng máy tính riêng; trang này không có máy tính nhúng.'),
        ('Đọc đề → chọn dạng → tính → thử lại.',
         'Có tổng và tỉ số: chia theo tổng số phần. Có hiệu và tỉ số: chia theo hiệu số phần.<br>Bản đồ: đổi đơn vị trước. Phần trăm: phân biệt số gốc, phần đã làm và phần còn lại.<br>Ô trả lời có sẵn dấu %: chỉ nhập số. Đọc lời giải sau khi nộp và thử lại câu sai.'),
    ]
    bodies8 = [
        ('Thể tích nói lên phần không gian một hình chiếm chỗ.',
         cubes([2,1,3])+'Hình trên có 2 + 1 + 3 = 6 khối nhỏ bằng nhau. Xếp lại sáu khối thì tổng thể tích không đổi.<br><b>Khối lập phương:</b> sáu mặt vuông bằng nhau. <b>Hình hộp chữ nhật:</b> có chiều dài, chiều rộng, chiều cao.<br>Với hình nhiều lớp, đếm đủ khối trong từng lớp, kể cả phần bị che; không chỉ đếm các mặt nhìn thấy.'),
        ('1 dm³ = 1 000 cm³.',
         '1 cm³ là thể tích khối lập phương cạnh 1 cm; 1 dm³ là thể tích khối lập phương cạnh 1 dm.<br>2,35 dm³ = 2 350 cm³; 480 cm³ = 0,48 dm³.<br>3 dm³ 25 cm³ = 3 025 cm³ = 3,025 dm³.<br><b>Nước:</b> 1 lít = 1 dm³. Ví dụ 0,75 lít = 750 cm³.'),
        ('1 m³ = 1 000 dm³ = 1 000 000 cm³.',
         '1 m³ là thể tích khối lập phương cạnh 1 m.<br>m³ → dm³ → cm³: mỗi bước nhân 1 000. Đi ngược lại thì chia 1 000 mỗi bước.<br>0,006 m³ = 6 dm³ = 6 000 cm³.<br><b>Không nhầm:</b> độ dài mỗi bậc × 10; diện tích × 100; thể tích × 1 000.'),
        ('Đổi cùng đơn vị → tính → ghi đơn vị ở kết quả.',
         cubes([1,3,2,1])+'Nếu mỗi khối nhỏ 1 cm³ thì hình trên có thể tích 7 cm³. Thêm 4 khối cùng loại được 11 cm³.<br>Đếm theo lớp: 3 lớp, mỗi lớp 8 khối → 8 + 8 + 8 = 24 khối. Đây là đếm khối, chưa học công thức thể tích hình hộp ở chủ đề 9.<br><b>Thử tại nhà:</b> dùng khối đồ chơi cùng cỡ, xếp hai hình khác nhau với cùng số khối. Nhờ người lớn cùng kiểm tra.'),
    ]
    output=[]
    for cd, source, bodies, shorts, intro in [
        (7,LESSONS7,bodies7,['Tỉ số','Bản đồ','Tổng–tỉ','Hiệu–tỉ','Tìm phần trăm','Giá trị phần trăm','Máy tính','Thực hành','Ôn chung'],'Chọn đúng số gốc và đọc đúng thứ tự tỉ số.'),
        (8,LESSONS8,bodies8,['Đếm khối','cm³ và dm³','m³','Luyện tập'],'Đếm đủ khối, đổi đúng đơn vị.')]:
        col,bg=colours[cd]
        lessons=[]
        for (num,(title,pg)),(head,body) in zip(source.items(),bodies):
            lessons.append(dict(n=num,title=title,pg=pg,col=col,bg=bg,dk=col,head=head,
                body=lambda c,text=body: '<div style="font-size:24px;line-height:1.65">'+text+'</div>'))
        title='TỈ SỐ VÀ CÁC BÀI TOÁN LIÊN QUAN' if cd==7 else 'THỂ TÍCH. ĐƠN VỊ ĐO THỂ TÍCH'
        sheet=gen_sheet(cd,title,f'Bài {min(source)} đến Bài {max(source)} · Toán 5, tập hai',col,bg,lessons,shorts,intro,
            'Xem từng bài rồi luyện sáu đề, từ nhận biết đến vận dụng nhiều bước. Bài làm được lưu trên trình duyệt này.',
            f'Bám sách Toán 5, tập hai (Kết nối tri thức với cuộc sống), trang {4 if cd==7 else 30}–{29 if cd==7 else 39}. Ví dụ và bài tập tự soạn.')
        output.append((cd,sheet,col))
    from .overviews910 import sheets as extra_sheets
    return output + extra_sheets(gen_sheet)
