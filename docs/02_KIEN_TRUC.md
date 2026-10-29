# 02 — Kiến trúc và pipeline

Hiện trạng (trước khi dọn thư mục): bộ nguồn nằm ở `generator/`, kết quả đã build nằm ở `site/Toan5/`.

## Luồng chạy
```
generator/
  cfg.py              ROOT + CDS: danh sách chủ đề, thư mục, tên file đề, tiêu đề, mô tả
  g4lib.py, g5lib.py  thư viện sinh đề (Decimal/Fraction, hình SVG, ghi file test)
  g4_deNN.py          sinh đề CĐ4 -> tests/cd4/deNN.js   (tương tự g5_*, g6_*)
  tests/cdN/deNN.js   dữ liệu 24 câu: window.TEST_FN=function(H){return MKn([...])}
  common/cdN.js       wrapper MKn: meta, tip, tên bài (lessons), 3 mức độ
  engine.js/.css      engine làm bài (giao diện, chấm điểm, lưu tiến độ)
  fonts.css           font nhúng base64 (Baloo 2 + Be Vietnam Pro)
  build_all.py        ghép fonts + css + common + test + engine -> out/<ROOT>/<thư mục CĐ>/DeN_<Slug>.html
  gen_overview.py     sinh TongQuan_ChuDeN.html (poster 1080px)
  gen_index.py        sinh index.html (DATA lấy từ cfg.CDS)
  png.js              render TongQuan_*.png (1080px) và đo tràn ngang trên mobile
```

Lệnh build đầy đủ (chạy trong `generator/`):
```
python3 g5_de01.py ... g6_de06.py     # sinh lại tests/ nếu sửa generator (g4_* dành cho CĐ4)
python3 build_all.py                  # -> out/Toan5/.../DeN_*.html
python3 gen_overview.py               # -> TongQuan_ChuDeN.html
python3 gen_index.py                  # -> out/Toan5/index.html
node png.js                           # -> TongQuan_ChuDeN.png (cần playwright)
```
Lưu ý: `gen_overview.py` và `gen_index.py` viết vào `out/Toan5/`; `build_all.py` đọc `tests/` đã sinh sẵn nên không cần chạy lại `g*_de*.py` nếu không sửa đề. CĐ1–CĐ3 không có generator Python trong repo (đề nằm sẵn ở `tests/cd1..cd3/*.js`; CĐ4–6 có generator `g4/g5/g6_*.py`).

## Quy ước tên
- Thư mục chủ đề: `ChuDe{n}_{TenKhongDau}`; đề: `De{i}_{Slug}.html`; tổng quan: `TongQuan_ChuDe{n}.html/.png`.
- `id` đề: `cd{n}-de{i}` -> khóa `localStorage`: `mia5:cd{n}-de{i}`.
- `TEST_EXTRA` (do `build_all.py` tiêm vào): `id`, `title`, `theme`, `home` (`../index.html`), `next`, `prev`.

## Dữ liệu tiến độ
`localStorage['mia5:<id>'] = {tries, best, last, max, rank, secs, at}`. Trang chủ đọc các khóa này để tính số đề đã làm, số sao, điểm cao nhất.
Tiến độ **không đồng bộ** giữa trình duyệt hoặc thiết bị. Đổi địa chỉ web (file:// -> github.io) là mất tiến độ cũ. Muốn đồng bộ phải thêm nơi lưu khác; **không làm nếu chủ repo chưa yêu cầu**.

## Điểm cần nhớ khi mở rộng (nợ kỹ thuật đã biết)
1. `build_all.py` hardcode tiêu đề `Toán 5 · Chủ đề ...`, `lang="vi"`, ROOT `Toan5`. Tiếng Anh cần tham số hóa môn học.
2. `audit.js` mặc định chạy `1,2,3,4` nếu không truyền tham số; `png.js`, `idx.js` hardcode `out/Toan5` và danh sách 6 chủ đề.
3. `png.js`, `idx.js` ghi ảnh tạm vào `/tmp/...` (Linux). Trên Windows cần đổi.
4. Mỗi file đề nhúng ~250 KB font base64 + engine (~300 KB/đề). 36 đề ≈ 11 MB. Nên tách `assets/` dùng chung (font + engine + css) khi dọn thư mục.
5. `shot.js` cũ đã bị loại; `qshot.js`, `figs.js`, `show.js` là công cụ phụ: chụp câu hỏi, chụp các câu có hình, in đáp án.
6. Engine có chữ giao diện tiếng Việt cố định (nút, kết quả, xếp loại). Với Tiếng Anh: giữ giao diện (nút, hướng dẫn, kết quả) bằng tiếng Việt, nội dung câu hỏi bằng tiếng Anh.
