# 02 — Kiến trúc và pipeline

Hiện trạng: nguồn ở `generator/`, điều phối build/QA ở `tools/`, kết quả web ở `site/`. Cấu trúc chính thức và lệnh dùng từ gốc repo ở `08_CAY_THU_MUC_VA_DEPLOY.md`.

`node tools/build.js --regenerate` gọi các generator với UTF-8, ghép HTML tự chứa vào `generator/out/Toan5/`, rồi tạo bản web dùng tài nguyên chung ở `site/assets/`. `--standalone` giữ bản tự chứa và không cập nhật site. `node tools/build.js` gọi bước Python rồi `tools/render_overviews.js` để sinh PNG. `overview.css/js` là giao diện và chế độ đọc tổng quan (nhúng vào standalone, tách ra assets cho web). Mẫu trang chủ chung ở `tools/templates/home.html`; trang chủ Toán vẫn sinh từ `gen_index.py`.

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
2. `audit.js` mặc định kiểm tra cả 6 chủ đề và trả exit code lỗi khi không đạt. `tools/qa.js` là luồng QA web chính thức; các tiện ích `png.js`, `idx.js` vẫn dành riêng Toán.
3. Đã đổi URL file bằng `pathToFileURL`; ảnh phụ của `png.js`, `idx.js` nằm ở `generator/out/qa/`, dùng được trên Windows.
4. Bản web đã tách font/engine/CSS vào `site/assets/`; bản standalone tiếp tục nhúng toàn bộ. Không sửa trực tiếp file build trong `site/`.
5. `shot.js` cũ đã bị loại; `qshot.js`, `figs.js`, `show.js` là công cụ phụ: chụp câu hỏi, chụp các câu có hình, in đáp án.
6. Engine có chữ giao diện tiếng Việt cố định (nút, kết quả, xếp loại). Với Tiếng Anh: giữ giao diện (nút, hướng dẫn, kết quả) bằng tiếng Việt, nội dung câu hỏi bằng tiếng Anh.

## Hai môn sau mẫu Unit 1

`build_all.py`, `gen_overview.py`, `gen_index.py` có main guard và cung cấp hàm render dùng lại. `gen_english.py` gọi các hàm này với metadata, dữ liệu Unit 1, tiêu đề và tổng số riêng; không đổi cấu hình Toán. Build đầy đủ ghi cả `out/Toan5` và `out/TiengAnh5`, rồi xuất web hai môn; standalone nhúng engine/font cho cả hai.

Nguồn Anh là `english/u01/content.py`; wrapper và `tests/de*.js` sinh tự động, được commit theo quy ước nguồn đã bàn giao. `site/catalog.json` sinh từ cấu hình nguồn: danh sách đường dẫn, ID và môn của 66 đề. QA so sánh danh sách thực tế với catalog, không chỉ đếm số HTML có sẵn.

## Trang chủ động viên và tiến độ

Nguồn tools/templates/home.html + home.css/js; tools/build.py sinh site/index.html và site/assets/home.css/js. Danh sách đề được nhúng từ đúng registry sinh site/catalog.json, không thêm danh sách khóa/ID riêng trong JS. Điểm đọc từ mia5:{id} hiện hành, kiểm tra best/max là số hợp lệ và xử lý từng bản ghi hỏng riêng; bản Anh trước -v2 không tính vào bộ hiện tại. Sao theo các ngưỡng đã có, không sửa điểm gốc.

Khóa mia5:home-celebrated lưu snapshot tries/at mỗi đề. Khi chưa có snapshot: ghi mốc, không chúc mừng. Khi lượt làm tăng hoặc có thời gian nộp mới: hiện động viên một lần rồi cập nhật mốc. Tải lại hoặc back-forward không lặp lời chúc mừng cùng lượt; pageshow persisted cập nhật tiến độ khi quay lại từ bộ nhớ trang. Khi storage bị chặn vẫn mở được môn và không hiển thị lời chúc mừng lặp. Đây là trạng thái UI, không phải kết quả học tập.

## Nháp bài đang làm

Khóa `mia5:draft:{id}` tách khỏi kết quả `mia5:{id}`. Dữ liệu gồm schema=1, hash nội dung có ý nghĩa (bỏ hình minh họa/index runtime), bản ghi kết quả nền, updatedAt, số câu đã làm, elapsedMs, tên, trạng thái input/select theo câu, thứ tự token, supportUsed. Không lưu DOM, không nhúng đáp án đúng vào nháp, không tự phát lại âm thanh khi khôi phục. Giá trị được gán vào control, không thành HTML.

Lưu sau khoảng 250ms ngừng nhập, định kỳ 5 giây khi đồng hồ chạy, và đồng bộ lúc pagehide/visibility hidden. Đóng/ẩn trang tạm dừng đồng hồ; khôi phục giữ thời gian tích lũy và chỉ tiếp tục khi tương tác. Không lưu kết quả nộp dưới dạng nháp; nộp thành công xóa nháp, nộp nhưng lưu kết quả lỗi thì giữ bản nháp gần nhất. Nháp phải khớp schema, nội dung, hình dạng input/token và kết quả nền; nháp thuộc lượt trước khi có kết quả mới không được phục hồi lại. Nháp hỏng/không tương thích có thông báo; không áp dụng một phần trạng thái sai.

Nút bỏ nháp chỉ xóa khóa nháp của đúng đề; reset môn duyệt các ID trong DATA rồi xóa hai khóa kết quả/nháp tương ứng, giữ môn khác và kết quả Anh phiên bản cũ. Tiến độ trên trang chủ vẫn chỉ dựa vào đề đã nộp. Nháp ở trang môn có nhãn riêng và nút đi tiếp, không cộng sao.

## Unit 2–3

Registry `generator/english/units.py` sinh danh mục đề và dữ liệu trang môn từ cùng cấu hình. `practice.py` tái dùng các dạng câu và nhúng WebP; `overviews.py` dựng tổng quan mới. Mỗi thư mục u02/u03 chứa content.py, NOTES.md, tranh/prompt và JS sinh ra. Build trích ảnh của u01/u02/u03 thành tài nguyên web, standalone nhúng cùng byte. ID mới en-u02-deN-v1 và en-u03-deN-v1; không đổi ID/nội dung/điểm Unit 1 hoặc Toán.

## Mở rộng đến Unit 5

Registry `english/units.py` có thêm DETAILS chứa topic, lessons và màu từng Unit 2–5; gen_english.py không dùng điều kiện Unit 2/else Unit 3 cho Unit mới. Mô tả sáu đề khai báo theo từng Unit. Hàm text của practice.py hỗ trợ các biến thể I would/I’d, He would/He’d, She would/She’d khi không bắt buộc dạng đầy đủ; engine và dữ liệu Unit 1–3/Toán không thay đổi. `tools/qa_english_units.js --units=4,5` dùng chung luồng kiểm chứng với wrapper Unit 2–3; tổng số chủ đề/đề lấy từ catalog.
