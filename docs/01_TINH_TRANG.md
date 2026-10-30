# 01 — Tình trạng hiện hành

Cập nhật 30/10/2026. Bản lịch sử trước khi gom tài liệu nằm trong `history/`; không dùng những số liệu cũ làm trạng thái hiện tại.

## Đã bàn giao

- Website: https://okeydokey8525.github.io/Lop_5_Mia/ — GitHub Pages qua Actions.
- Toán 5 tập một: 6 chủ đề, 36 đề, mỗi đề 24 câu/100 điểm; ID `cd{n}-de{i}` giữ nguyên.
- Tiếng Anh 5 tập một: Unit 1 — All about me!, 1 tổng quan HTML/PNG + 6 đề (144 câu). Các hồ sơ và câu hỏi tự soạn, bám trang 10–15 đã đọc. Đã tích hợp nghe vào 6 đề (6 câu nghe/đề), vẫn có mẫu nghe riêng, chưa có chấm nói.
- Toàn site: 42 đề chính thức, 53 HTML, 7 tổng quan HTML/PNG. Danh sách đề có nguồn chính là `site/catalog.json`.
- Giao diện hồng anh đào, tối màu tím mận; reader trên màn hình ≤820px, poster để xem/in. Tiến độ theo origin/trình duyệt, không đồng bộ thiết bị.
- Chủ repo đã xem Unit 1, phản hồi hình khó nhận diện và duyệt mẫu cá heo. Ngày 30/10 đã áp dụng phong cách mới cho đủ 6 tranh ở tổng quan/câu hỏi, giữ nguyên 144 câu và đáp án. Không suy rộng việc duyệt tranh thành giao làm unit tiếp theo.

| CĐ Toán | Thư mục | Nội dung | Bài |
|---|---|---|---|
| 1 | `ChuDe1_OnTapVaBoSung` | Ôn tập và bổ sung | 1–9 |
| 2 | `ChuDe2_SoThapPhan` | Số thập phân | 10–14 |
| 3 | `ChuDe3_DonViDoDienTich` | Đơn vị đo diện tích | 15–18 |
| 4 | `ChuDe4_PhepTinhSoThapPhan` | Các phép tính với số thập phân | 19–24 |
| 5 | `ChuDe5_HinhPhangChuViDienTich` | Một số hình phẳng, chu vi và diện tích | 25–29 |
| 6 | `ChuDe6_OnTapHocKi1` | Ôn tập học kì 1 | 30–35 |

## Bằng chứng gần nhất cho sản phẩm

Mã thay tranh `4798597`; [workflow build và deploy đạt](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/40976976768).

- Local và CI: audit 36 Toán + 6 Anh không lỗi; làm đúng theo đáp án khai báo 42/42 đề đạt 100/100; 832 tổ hợp responsive (52 trang × 8 chiều rộng × 2 theme). Local kiểm tra 251 tham chiếu tĩnh, 0 lỗi; 6 đề Anh standalone đạt.
- Live sau sửa tranh: 6 ảnh khớp byte với nguồn; 7 trang Unit 1 × 3 chiều rộng × 2 theme = 42 trường hợp, đủ ảnh, đúng tỷ lệ, không tràn ngang/lỗi trình duyệt. Báo cáo: `artifacts/online/artwork-live-report.json`.
- Lần kiểm tra toàn bộ live trước đó, 29/10/2026 20:08:05 UTC+7: 42/42 đề đạt, 832 tổ hợp responsive; kiểm tra biến thể chữ, câu sai, điểm phần, hồ sơ, reset riêng từng môn đạt. Báo cáo trong artifacts không phải nguồn nội dung.
- Chưa có dữ liệu em gái làm bài; mô phỏng Chromium chưa thay thế thử thiết bị thật, và tự điền đúng không phải giải độc lập toàn bộ đáp án.

## Nguồn và việc tiếp theo

Nguồn Anh: `generator/english/u01/content.py`, `NOTES.md`, `images/`. Nguồn sách ở thư mục ngoài repo `../tai_lieu/sach/`. Mở [08](08_CAY_THU_MUC_VA_DEPLOY.md) để tìm cây và lệnh; mở [bản đồ tài liệu](README.md) để tiếp nhận.

Chỉ tiếp tục Starter/Unit/Review khác khi chủ repo giao. Pipeline Anh hiện còn chỗ đăng ký riêng u01, cần tổng quát hóa khi mở rộng; xem [phân rã công việc](breakdowns/KE_HOACH_TIEP_THEO.md).

## Đầu vào còn thiếu

- Toán học kì 2: chưa có PDF, danh sách chủ đề/bài/số trang; chưa làm chủ đề 7–8.
- Tiếng Anh 5 tập hai: chưa có sách.
- Phản hồi học sinh về mức độ khó và câu chưa rõ: chưa có.

## Mẫu nghe ba cấp — 30/10/2026

Theo yêu cầu xem mẫu trước, bổ sung `TiengAnh5/Unit1_AllAboutMe/LuyenNghe_Mau.html`, liên kết từ trang chủ Anh. 6 câu: 2 Trung bình (tên/nơi sống), 2 Khá (môn thể thao/màu), 2 Giỏi (đoạn 4 câu, tìm 2 thông tin). Chấm 8 ý trong 6 câu, không tính điểm/sao đề chính thức và không ghi localStorage.

Có chọn giọng tiếng Anh, thử giọng, nghe bình thường/chậm, dừng, xem lời nghe/nghĩa, kiểm tra từng câu/cả mẫu, làm lại. Nguồn: `generator/english/u01/listening.py` và `listening.html`; lời nghe và đáp án sinh từ cùng dữ kiện. Chỉ dùng giọng thiết bị, không dùng audio SGK hoặc tạo file thu âm. Phụ thuộc giọng cài sẵn/dịch vụ của trình duyệt; bản HTML tự chứa không bảo đảm phát offline trên mọi máy.

QA chuyên biệt mô phỏng speech để kiểm tra điều khiển, lỗi, giọng đến trễ, timeout, chấm sai/thiếu/đúng và reset. Microsoft Edge trên máy hiện tại đã phát sinh sự kiện bắt đầu/kết thúc với Microsoft Zira en-US; đây không phải đánh giá phát âm bằng tai. Cần chủ repo nghe cả ba cấp trên thiết bị dùng thật trước khi triển khai hàng loạt. Tổng responsive hiện 53×8×2 = 848 trường hợp; các bằng chứng 832 ở trên là lịch sử trước mẫu nghe.

## Unit 1 có nghe và hồng sáng — đợt triển khai đã được duyệt

Chủ repo duyệt mẫu ba cấp và yêu cầu áp dụng cho Unit 1, đồng thời duyệt bảng hồng sáng. Mỗi đề hiện 24 câu = 10 TB/8 Khá/6 Giỏi, 100 điểm; thay 6 câu (vị trí 1/2, 11/14, 21/24) bằng 2 câu nghe mỗi cấp. Cộng 36 câu nghe trong 6 đề. Nội dung nghe/đáp án sinh từ cùng dữ kiện trong exam_listening.py. Không tự triển khai unit khác.

ID lưu điểm mới `en-u01-de1-v2` đến `en-u01-de6-v2`; điểm cũ không nhập vào thống kê mới và không bị reset khi xóa tiến độ bộ mới. Kết quả lưu phiên bản và các câu đã dùng hỗ trợ xem lời nghe; không trừ điểm vì nghe lại/chậm/xem chữ. Sau nộp tự mở lời nghe, vẫn nghe lại được.

Theme Tiếng Anh dùng chung theme.css/js ở generator/english, mặc định hồng sáng ngay cả khi OS tối; nút Sáng/Tối lưu lựa chọn riêng. Áp dụng trang chủ Anh, tổng quan/reader/PNG, sáu đề và mẫu. Màu và khóa tiến độ Toán giữ nguyên. QA chuyên biệt: tools/qa_english_unit1.js. Các mục mẫu/thống kê trước đây là lịch sử của giai đoạn trước tích hợp.

## Hồng sáng và Sáng/Tối toàn site

Theo yêu cầu tiếp theo của chủ repo, đã mở rộng theme sang trang chủ chung và toàn bộ Toán, không chỉ Anh. Cả 53 trang dùng một nguồn theme và khóa mia5:ui-theme; dữ liệu điểm không đổi. Giữ lựa chọn chủ động trước đây ở Anh khi chưa có lựa chọn chung. Cập nhật build cả standalone và bảy PNG; thêm qa_theme.js và kiểm tra responsive theo theme thực. Những mục trên ghi màu chỉ áp dụng Anh là lịch sử của giai đoạn trước yêu cầu này.

## Trang chủ chọn môn có phản hồi động viên

Đã thực hiện đúng bốn phần chủ repo duyệt: lời chào và hình sách/ngôi sao cả trên điện thoại, thẻ môn phản hồi nhẹ, thanh tiến độ/sao thật, động viên một lần khi quay lại sau lượt luyện tập mới. Giữ phạm vi chỉ trang chọn môn; không thêm hiệu ứng vào đề hoặc trang tổng quan. Tên lấy từ tên đã lưu hoặc Mia; không thêm tài khoản. Có hỗ trợ giảm chuyển động; không đổi nội dung, điểm hay ID đề. Nguồn và cơ chế mốc chúc mừng trong docs02, kiểm tra trong docs07.

## Sau kiểm tra chéo: sửa chấm phân số, đồng hồ và lưu nháp

Đã sửa hai lỗi tái hiện trên website: nhập 3.9 hoặc 3abc ở tử không còn được hiểu thành 3; thao tác sắp xếp số/từ khởi động đồng hồ trước khi dựng lại nút. So sánh phân số/hỗn số bằng số nguyên chính xác sau kiểm tra chuỗi và giới hạn số nguyên an toàn.

Đã thêm nháp cho toàn bộ 42 đề: các ô, lựa chọn, thứ tự số/từ, tên, thời gian và hỗ trợ nghe. Rời/tải lại trang rồi mở đúng đề sẽ khôi phục; đồng hồ chỉ chạy lại sau tương tác, không cộng thời gian đóng/ẩn trang. Nút Bỏ bản nháp có xác nhận, không xóa điểm đã nộp. Trang môn hiển thị Đang làm dở và ưu tiên nút Tiếp tục bài đang làm cho nháp mới nhất. Nháp không tính là đề đã hoàn thành. Sau nộp thành công xóa nháp, điểm/sao vẫn lưu như trước. Không có đồng bộ thiết bị; khi storage bị chặn báo không lưu được.

Nguồn engine.js/css và gen_index.py; QA hồi quy tools/qa_drafts.js. Nội dung/đáp án đề và ID kết quả giữ nguyên.
