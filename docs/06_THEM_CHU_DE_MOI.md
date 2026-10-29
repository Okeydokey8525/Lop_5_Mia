# 06 — Quy trình thêm một chủ đề mới

Áp dụng cho Toán học kì 2 và (với phần bổ sung ở `09_TIENG_ANH.md`) cho Tiếng Anh. Làm theo thứ tự; **gom nội dung trước, dựng sau**.

## 0. Gom nội dung
- Đọc mục lục sách (số bài, tên bài, trang). Nếu sách là PDF scan, render từng trang thành ảnh rồi xem; chỗ nào không chắc thì hỏi chủ repo, **không đoán**.
- Lập bảng: bài → ý chính → dạng bài hay gặp → bối cảnh thực tế cho 4 đề giữa.

## 1. Khai báo trong `cfg.py`
Thêm một mục vào `CDS`: `n`, `dir` (`ChuDe{n}_...` không dấu), `name`, `range`, `mk` (`cd{n}`), `overview` (`TongQuan_ChuDe{n}`), `tests` gồm 6 bộ `(slug, tên đề, mô tả)`. Đề 1 luôn là "Khởi động"; đề 6 là đề tổng hợp.

## 2. Wrapper `common/cd{n}.js`
Sao chép `common/cd5.js` rồi sửa: tên hàm `MK{n}`, `meta` (`book`, `title`, `topic`, `range`, `minutes`, `tip`), `lessons` (số bài → tên bài), 3 mức (`tb`/`kha`/`gioi`, 3/5/5 điểm). `decimal:true` nếu đề có số thập phân.

## 3. Sinh đề
Viết `g{n}_de01.py ... de06.py`, dùng chung thư viện `g4lib/g5lib` (hoặc tạo `gNlib.py` kế thừa). Cuối mỗi file gọi `write(i, Q)` (hoặc `write5/write6`; thêm `writeN` cho chủ đề mới và truyền `cd=n`). Quy tắc: đáp án và `why` được tính từ cùng biến.

## 4. Trang tổng quan
Viết `LESSONS{n}` + `cd{n}_sheet()` trong `gen_overview.py`, thêm màu mới vào danh sách vòng lặp cuối file. Màu khác 6 màu đã dùng (`docs/05_THIET_KE.md`).

## 5. Build, QA, giao
```
cd generator
python3 g{n}_de0*.py
python3 build_all.py && python3 gen_overview.py && python3 gen_index.py
node audit.js {n}
node tall.js out/Toan5 ChuDe{n}
node png.js
```
Cập nhật `gen_index.py`: tổng số đề, tổng số sao (3 sao/đề × số đề), mốc cầu thang, câu dẫn. Cập nhật `png.js` (danh sách chủ đề). Chạy `docs/07_KIEM_TRA.md` đầy đủ, kể cả **kiểm tra lại các chủ đề cũ**.

## 6. Cập nhật tài liệu
Sửa `docs/01_TINH_TRANG.md` (bảng chủ đề, số đề), và cây thư mục nếu đổi.
