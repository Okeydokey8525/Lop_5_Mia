# 08 — Cây thư mục và deploy (GitHub Pages / Vercel)

Bạn (Codex) được **tự quyết cây thư mục cuối cùng**. Ghi quyết định ở mục "Quyết định" bên dưới. Ràng buộc ở cuối file.

## Hiện trạng (khi bàn giao)
```
Lop_5_Mia/
├─ AGENTS.md, README.md, .gitignore
├─ docs/                      các file tài liệu này
├─ generator/                 bộ nguồn sinh đề (Python + Node)
│  ├─ cfg.py, g4lib.py, g5lib.py, g4_de*.py, g5_de*.py, g6_de*.py
│  ├─ common/cd1..cd6.js      wrapper meta + mức độ
│  ├─ tests/cd1..cd6/de01..06.js
│  ├─ engine.js, engine.css, fonts.css
│  ├─ build_all.py, gen_overview.py, gen_index.py, ov34.py, ov56.py
│  ├─ audit.js, tall.js, png.js, idx.js, figs.js, qshot.js, show.js
│  └─ assets/poster_cd2.html
└─ site/Toan5/                kết quả đã build: index.html + 6 thư mục chủ đề
```
Vấn đề cần giải: nguồn và sản phẩm lẫn kiểu đặt tên theo môn (`Toan5`), `generator` ghi ra `generator/out/` (đã `.gitignore`) rồi phải chép sang `site/`, font nhúng lặp 36 lần.

## Đề xuất (nháp, được phép thay đổi)
```
Lop_5_Mia/
├─ AGENTS.md, README.md
├─ docs/
├─ tools/                     build_all, gen_*, audit, tall, png, idx, check_links
├─ src/
│  ├─ engine/                 engine.js, engine.css, fonts (font tách file riêng)
│  ├─ toan/cd01..cdNN/        cdN.js + generator + tests
│  └─ tieng-anh/u00..u12/     cùng cấu trúc
└─ site/                      sản phẩm build, thư mục được xuất lên Pages
   ├─ index.html              (trang chủ gộp: Toán, Tiếng Anh)
   ├─ toan/…                  các chủ đề Toán
   ├─ tieng-anh/…             các chủ đề Tiếng Anh
   └─ assets/                 font + engine dùng chung (cache được)
```
Gợi ý nhưng không bắt buộc. Nếu đổi tên thư mục Toán thì **giữ nguyên tên file đề** hoặc cập nhật mọi link; giữ khóa `localStorage` (`mia5:cd{n}-de{i}`) để không mất tiến độ nội bộ của chủ đề đã dùng. Khóa cho Tiếng Anh nên có tiền tố môn, ví dụ `mia5:en-u01-de1`.

## Triển khai lên GitHub Pages (khuyến nghị)
Địa chỉ dự kiến: `https://okeydokey8525.github.io/Lop_5_Mia/`.
Cách làm (chọn một):
1. **GitHub Actions** (sạch nhất): workflow dùng `actions/upload-pages-artifact` + `actions/deploy-pages`, build `site/` trong CI. Bật Pages nguồn "GitHub Actions" trong Settings → Pages.
2. **Nhánh/thư mục**: để site trong `docs/` hoặc nhánh `gh-pages` rồi chọn trong Settings → Pages. Nếu chọn `docs/`, chuyển tài liệu markdown sang thư mục khác (ví dụ `notes/`) để tránh lẫn.

Lưu ý:
- Pages miễn phí yêu cầu repo **public** (repo đang public). **Không đưa SGK vào repo.**
- Đường dẫn trong HTML phải **tương đối**, vì site nằm dưới `/Lop_5_Mia/`. Link kiểu `/abc.html` sẽ hỏng.
- Pages **phân biệt hoa thường**; Windows thì không. Phải chạy kiểm tra link (xem `docs/07_KIEM_TRA.md`).
- `localStorage` theo địa chỉ web. Tiến độ đã làm trên máy (file://) không sang bản online; thiết bị khác cũng không đồng bộ. Chủ repo đã được báo; không tự thêm backend.
- Mỗi lần push, Pages mất 1–2 phút để cập nhật; kiểm tra bằng cách mở link thật.
- Cân nhắc đặt tên file Pages không dấu (đã vậy), tránh khoảng trắng.

## Phương án thay thế: Vercel
Vercel host được site tĩnh (không cần build framework): import repo, đặt Output Directory = `site`, Framework = Other. Ưu điểm: preview theo nhánh, repo private vẫn deploy được. Nhược: thêm một nền tảng. Chỉ dùng nếu Pages có vấn đề hoặc chủ repo muốn.

## Kích thước
Hiện mỗi đề ≈ 300 KB (font 248 KB + engine), 36 đề ≈ 11 MB; thêm 78 đề Tiếng Anh sẽ ≈ 35 MB nếu giữ cách nhúng. Nên **tách font/engine/css thành `assets/` dùng chung**; việc này làm thay đổi `build_all.py` và phải chạy lại toàn bộ QA 36 đề Toán. Giữ lựa chọn "nhúng tất cả vào 1 file" làm cờ build (`--standalone`) nếu chủ repo muốn gửi file lẻ cho em qua Zalo/USB.

## Quyết định (Codex điền)
- Cây thư mục chọn: _chưa điền_
- Cách deploy: _chưa điền_
- Có tách `assets/` không: _chưa điền_
- Ngày/giờ kiểm tra bản online: _chưa điền_

## Ràng buộc (không thương lượng)
1. Không làm mất đề, chủ đề, hay file PNG tổng quan.
2. Sau khi dọn thư mục: `tall.js` cho 36 đề Toán vẫn 100/100, mọi link đúng hoa/thường.
3. Không commit SGK; `.gitignore` đã chặn PDF/ảnh thư mục sách.
4. Không làm hỏng khóa `localStorage` hiện có mà không thông báo (hoặc có bước chuyển).
5. Tài liệu `docs/` luôn khớp với cấu trúc thật; sửa file này khi đổi cây.
