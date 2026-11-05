# Học từ và phát âm Units 2–5

## Phạm vi

Mở rộng mẫu đã duyệt của Units 6–7 cho Units 2, 3, 4, 5 theo yêu cầu. Không đổi 78 đề, ID, đáp án, điểm hay nháp của đề chính thức. Trang tổng quan mỗi Unit có nút mở `HocTuVaPhatAm.html`; giữ giao diện hồng sáng và theme chung.

| Unit | Ba nhóm | Từ/cụm | Hội thoại | Bài luyện |
| --- | --- | ---: | ---: | ---: |
| 2 | Nhà ở; địa chỉ và số; gần và xa | 12 | 6 | 12 |
| 3 | Nước/quốc tịch; tính cách; giới thiệu bạn | 18 | 6 | 12 |
| 4 | Hoạt động; like + V-ing; cuối tuần/tần suất | 17 | 6 | 12 |
| 5 | Nghề; ước mơ; lý do | 15 | 6 | 12 |

## Nội dung và tổ chức

Dữ kiện từng Unit ở `generator/english/u02/study.py` đến `u05/study.py`. Dùng chung renderer, controller và CSS của `english/study/`; `author.py` chỉ tạo cấu trúc dữ liệu. Không sao chép controller sang mỗi Unit. Tái dùng tranh đã duyệt; các khái niệm chưa có tranh dùng thẻ chữ, không gắn hình sai nghĩa. Đối chiếu NOTES từng Unit và xem lại trang in 18, 24, 28, 36 ngoài repo. Không sao chép ảnh/audio/hội thoại sách vào site.

Có nghe thường/chậm, ABC từng chữ có tô sáng, ví dụ, ẩn nghĩa, hội thoại nghe cả hai vai hoặc chỉ A để trẻ đáp B, đánh dấu đã luyện/cần ôn và bài luyện có gợi ý. Không tự nhận đã thuộc sau khi nghe. Không ghi âm hoặc chấm nói tự động.

Unit 2 dùng địa chỉ giả định, phân biệt at/in, sixteen/sixty; không đặt tower/building cạnh tranh chỉ bằng hình. Unit 3 không đoán quốc tịch từ mặt, phân biệt tính cách/ngoại hình và is/has. Unit 4 bám like + V-ing, không gán phần trăm tần suất. Unit 5 chỉ chấp nhận viết tắt khi đề cho phép; nghề/lý do không bị gán theo giới tính hoặc thành quan hệ duy nhất.

## Lưu dữ liệu và kiểm thử

Key riêng `mia5:learn:en-u02-v1` đến `mia5:learn:en-u05-v1`. Dùng cùng cơ chế lưu câu đang gõ, đáp án/feedback và nhóm, flush khi rời trang, signature khi nội dung thay đổi. Không đổi key Unit 6/7 hay cơ chế chuyển dấu mẫu cũ. Giới hạn lưu trên cùng thiết bị, trình duyệt và địa chỉ web; không có tài khoản/đồng bộ.

`qa_study.js` mở rộng đủ sáu Unit (88 từ, 37 hội thoại, 72 bài luyện, 144 layout/theme), kiểm tra từng chuỗi ABC, ví dụ, đến lượt em, không tự đánh dấu thuộc, lưu sau đóng/mở hồ sơ browser và tách dữ liệu. Giữ ca Unit 6/7; thêm ca sai/đúng at/in, has/is, watering/water và dạng đầy đủ I would. Speech mô phỏng không chứng minh chất lượng phát âm bằng tai.

## Bài học

- Mở rộng bằng cấu hình bài học; giữ một cơ chế lưu/âm thanh để các Unit có hành vi nhất quán.
- Đếm trang từ bản build thực tế: thêm bốn trang học thành 102 HTML, không tăng số đề chính thức.
- Chờ build xong rồi mới chạy QA đường dẫn mới: chạy sớm có thể tải 404 ngay trước lúc file được tạo.
- Không dùng kiểm tra đáp án tự sinh để thay cho phản biện nội dung; thêm ca sai ở điểm ngữ pháp dễ nhầm.

Kiểm chứng local: audit 78 đề/1008 vị trí câu Tiếng Anh không lỗi; 836 liên kết đúng; QA 78/78 đề đạt 100/100, 102 HTML không lỗi browser; theme 102 trang và responsive 1632 trường hợp đạt. Bộ học từ đạt 88 chuỗi ABC, 37 hội thoại, 72 bài luyện và 144 layout trên cả Units 2–7, gồm lưu sau đóng/mở browser và bảo toàn dữ liệu mẫu cũ. Báo cáo trong artifacts/study-full-local (speech mô phỏng).
