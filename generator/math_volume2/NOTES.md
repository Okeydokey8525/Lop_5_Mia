# Toán 5 tập hai — Chủ đề 7–8

## Nguồn đã đọc

- Sách ngoài repo: `C:\LeDucLuong\Mia\tai_lieu\sach\SGK Toán 5, tập hai-mau.pdf`, 51 270 320 byte, 70 trang PDF.
- SHA256: `6c12b550ba8d800e65f4606f5a2c7c850f07b8d29b282d9d60b108ea7b526c0c`.
- Đã xem bìa, đủ hai trang mục lục và từng trang in **4–39** (PDF 6–41), render 1500px ở `C:\LeDucLuong\Mia\luu_tru\math-volume2-planning\`.
- Chủ đề 7: Bài 36–44, trang 4–29. Chủ đề 8: Bài 45–48, trang 30–39. Tên bài/trang trong `content.py`.
- Bản này kết thúc bài học ở trang in 67 rồi tới bìa sau; chưa đủ chủ đề 10–12. Không ghi là đã có toàn bộ tập hai.

## Phạm vi và thiết kế nội dung

- Mỗi chủ đề sáu đề × 24 câu, 10 Trung bình/8 Khá/6 Giỏi, 100 điểm; đủ các bài trong từng đề. Câu hỏi, số liệu, lời giải và ví dụ tự soạn.
- Chủ đề 7 có tỉ số đúng thứ tự, phần trăm cả trên 100%, bản đồ hai chiều, tổng–tỉ/hiệu–tỉ, giảm giá có điều kiện, dự toán và phần vượt kế hoạch. Phân số yêu cầu tối giản. Ô có sẵn dấu % chỉ nhập số.
- Máy tính: nhận biết CE/OFF/ON-C/= theo loại minh họa trong sách; ghi rõ có thể khác máy. Không khẳng định mọi máy đều ưu tiên phép nhân. Bài 43 là bài ứng dụng tự soạn có thể kiểm tra bằng máy riêng, không mô phỏng máy tính trong web.
- Thương phần trăm của bộ đề đều kết thúc; tổng quan giải thích yêu cầu lấy chữ số trong sách, không tự đặt quy tắc làm tròn khác.
- Chủ đề 8 dùng định nghĩa, đếm khối/cột/lớp, bảo toàn thể tích, đổi đơn vị, nước/lít, tính trung bình, phần trăm trống và bảng giá nước **giả định**. Không dạy trước công thức diện tích hay thể tích hình hộp ở chủ đề 9. Đếm theo lớp được sách Bài 48 sử dụng.
- SVG tự dựng chính xác: mỗi cột chỉ sâu một khối, tất cả khối nhìn thấy; đếm khối bị che chỉ khi đề nói rõ số lớp/số khối mỗi lớp. Không đưa scan hoặc tranh sách lên site.
- `Decimal` và `Fraction` dùng cho phép tính; không dùng số thực nhị phân khi soạn đáp án. Các đề dùng cùng bộ dạng bài với số liệu/bối cảnh thay đổi; không tuyên bố là 288 dạng toán khác nhau.

## Build và bảo toàn

- `python generator/gen_math_volume2.py` sinh wrapper `common/cd7.js`, `cd8.js` và 12 file `tests/cd7`, `cd8`. `tools/build.py --regenerate` gọi script này.
- `overviews.py` tạo hai poster và reader từ cùng nguồn. Registry `cfg.py`; giữ nguyên ID `cd1..6-deN`, thêm `cd7-deN`, `cd8-deN`.
- Trang Toán có tiêu đề nhóm tập một/tập hai, 48 đề/144 sao; trang chọn môn cập nhật 8 chủ đề/48 đề. Không đổi nội dung Toán 1–6, Anh hoặc schema lưu bài.

## Kiểm chứng và bài học

- `python tools/audit_math_volume2.py`: đọc JSON JS đã sinh, tính độc lập từ dữ kiện hiển thị bằng `Fraction`, thử ngược tổng/hiệu/tỉ số/giá giảm/bản đồ/thể tích, đếm rect của SVG; kiểm phạm vi và bốn dạng câu.
- `node tools/qa_math_volume2.js` (thêm `--webkit`): cả 12 đề, ngộ nhận tỉ số/phần trăm/đổi đơn vị, dấu phẩy, xem lại kết quả, 16 bố cục reader, reset cách ly. Standalone chỉ chạy Chromium; WebKit Windows kiểm HTTP/HTTPS.
- `node tools/qa_persistence.js --math=7,8`: đóng/mở thật profile, đáp án/kết quả/best/last, nháp, Back và cập nhật tab khác, storage đầy.
- Bài học khi xem bản đầu: CSS engine mặc định SVG chỉ 112px, làm sơ đồ tỉ số quá nhỏ. Hình mới đặt chiều rộng riêng và max-width 100%; phải xem ảnh trên điện thoại, không chỉ kiểm tra không tràn.
- Trạng thái local/CI/live và giới hạn học sinh thật ghi trong bàn giao `docs/breakdowns/2026-11-20_TOAN_CHUDE7_CHUDE8.md`.
