# 01 — Tình trạng dự án

Cập nhật: 2026-10-29.

## Đã xong: Toán 5 tập một (Kết nối tri thức với cuộc sống)
6 chủ đề, mỗi chủ đề có 1 trang tổng quan (HTML + PNG) và 6 đề, tổng **36 đề**, 108 sao trên trang chủ.

| CĐ | Thư mục | Tên | Bài |
|---|---|---|---|
| 1 | `ChuDe1_OnTapVaBoSung` | Ôn tập và bổ sung | 1–9 |
| 2 | `ChuDe2_SoThapPhan` | Số thập phân | 10–14 |
| 3 | `ChuDe3_DonViDoDienTich` | Đơn vị đo diện tích | 15–18 |
| 4 | `ChuDe4_PhepTinhSoThapPhan` | Các phép tính với số thập phân | 19–24 |
| 5 | `ChuDe5_HinhPhangChuViDienTich` | Một số hình phẳng, chu vi và diện tích | 25–29 |
| 6 | `ChuDe6_OnTapHocKi1` | Ôn tập học kì 1 | 30–35 |

Trang tổng quan CĐ3 và CĐ4 hiển thị số trang SGK.

### Kiểm chứng local ngày 29/10/2026 (Codex)

- Đã chốt cây thư mục ở `docs/08`; giữ `generator/`, `docs/`, `site/Toan5/`, thêm `tools/`, tài nguyên chung và trang chủ chọn môn.
- Build UTF-8 trên Windows; sinh lại CĐ4–6 không thay đổi dữ liệu JS. Trước sửa SVG, bản standalone khớp 43/43 nội dung HTML đã giao (chuẩn hóa xuống dòng). Sau sửa nhãn hình, đã đối chiếu 864/864 câu: nội dung, dữ liệu, đáp án và lời giải không đổi.
- Audit đủ 36 đề: 0 lỗi, đã sửa cảnh báo giảm dần và bổ sung kiểm tra các câu sắp xếp có đơn vị/phép tính/hình học/bảng.
- Chromium qua HTTP với tiền tố `/Lop_5_Mia/`: 36/36 đề 100/100, 44 trang không tràn ngang ở 400px, không lỗi console/request; kiểm tra link động và 196 tham chiếu tĩnh.
- Kiểm tra nộp thiếu câu, hủy xác nhận, điểm một phần, làm lại, giữ điểm tốt nhất, tiến độ và thống kê sau tải lại. Đã xem ảnh 6 poster và hình minh họa; giữ nguyên các PNG nguồn đã giao.
- Trang chủ chung đã có; Tiếng Anh chỉ hiển thị đang chuẩn bị. Chưa làm Unit 1 theo phạm vi chủ repo chốt.
- Online đã đạt lúc 29/10/2026 18:22:52 UTC+7: https://okeydokey8525.github.io/Lop_5_Mia/ — 36/36 đề 100/100, 44 trang không tràn ngang ở 400px, không lỗi console/request; lưu điểm và tải lại đạt. 53/53 file công khai khớp byte với local. Chi tiết và workflow ở `docs/08`.

### QA từ bản bàn giao (trước đợt chuẩn hóa)
- 36/36 đề: `audit.js` không lỗi; `tall.js` tự điền đúng hết ra 100/100, không lỗi console.
- Trang chủ: 36 đề trong `DATA`, mọi link tới file có thật.
- Trang tổng quan và trang chủ không bị tràn ngang ở màn hình 400px.
- Rebuild từ bộ nguồn `generator/` cho ra file **giống hệt** `site/Toan5/` (đã so sánh từng file HTML).

### Chưa kiểm tra / chưa làm
- Em gái **chưa làm thử** các đề thật, nên câu nào khó hiểu thì chưa biết.
- GitHub Pages đã bật nguồn GitHub Actions và kiểm tra trên URL thật; local dùng cùng tiền tố `/Lop_5_Mia/`.
- Đã sửa khung/nhãn SVG tam giác vuông, ao trong khu đất và nhãn chiều rộng để chữ không bị cắt. QA kiểm tra biên nhãn SVG ở mọi hình câu hỏi.
- Đã có `tools/check_links.py` kiểm tra hoa/thường trên Windows và Linux.
- `generator/fonts.css` là file sinh sẵn từ `@fontsource/baloo-2` và `@fontsource/be-vietnam-pro` (nhúng base64); script sinh file này **không còn trong repo**. Nếu cần đổi font phải tự tạo lại.
- `gen_overview.py` cho CĐ2 đọc `generator/assets/poster_cd2.html` (áp phích dựng sẵn). CĐ1, CĐ3–6 sinh từ code.
- Tiến độ lưu theo trình duyệt và theo địa chỉ web: khi chuyển từ `file://` sang `https://` thì tiến độ cũ không mang theo.

## Việc kế tiếp (theo thứ tự)
1. **Cấu trúc, build/QA, trang chủ chung và Pages đã hoàn tất** — `docs/08_CAY_THU_MUC_VA_DEPLOY.md`.
2. **Tiếng Anh 5 tập 1** (Starter, Unit 1–10, Review 1–2) — `docs/09_TIENG_ANH.md`.
3. **Toán học kì 2** — chờ chủ repo đưa sách.

## Toán học kì 2 (chỗ trống, chủ repo điền)
- File sách: _chưa có_
- Danh sách chủ đề/bài/số trang: _chưa có_

## Tiếng Anh 5 tập 2 (chỗ trống)
- _chưa có sách_
