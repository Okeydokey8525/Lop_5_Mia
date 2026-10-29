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

### Đã kiểm tra
- 36/36 đề: `audit.js` không lỗi; `tall.js` tự điền đúng hết ra 100/100, không lỗi console.
- Trang chủ: 36 đề trong `DATA`, mọi link tới file có thật.
- Trang tổng quan và trang chủ không bị tràn ngang ở màn hình 400px.
- Rebuild từ bộ nguồn `generator/` cho ra file **giống hệt** `site/Toan5/` (đã so sánh từng file HTML).

### Chưa kiểm tra / chưa làm
- Em gái **chưa làm thử** các đề thật, nên câu nào khó hiểu thì chưa biết.
- Chưa bật GitHub Pages, chưa thử site chạy dưới đường dẫn `/Lop_5_Mia/`.
- Chưa kiểm tra link phân biệt hoa thường (Windows không phân biệt, Pages thì có).
- `generator/fonts.css` là file sinh sẵn từ `@fontsource/baloo-2` và `@fontsource/be-vietnam-pro` (nhúng base64); script sinh file này **không còn trong repo**. Nếu cần đổi font phải tự tạo lại.
- `gen_overview.py` cho CĐ2 đọc `generator/assets/poster_cd2.html` (áp phích dựng sẵn). CĐ1, CĐ3–6 sinh từ code.
- Tiến độ lưu theo trình duyệt và theo địa chỉ web: khi chuyển từ `file://` sang `https://` thì tiến độ cũ không mang theo.

## Việc kế tiếp (theo thứ tự)
1. **Dọn cây thư mục và đưa lên Pages** — `docs/08_CAY_THU_MUC_VA_DEPLOY.md`.
2. **Tiếng Anh 5 tập 1** (Starter, Unit 1–10, Review 1–2) — `docs/09_TIENG_ANH.md`.
3. **Toán học kì 2** — chờ chủ repo đưa sách.

## Toán học kì 2 (chỗ trống, chủ repo điền)
- File sách: _chưa có_
- Danh sách chủ đề/bài/số trang: _chưa có_

## Tiếng Anh 5 tập 2 (chỗ trống)
- _chưa có sách_
