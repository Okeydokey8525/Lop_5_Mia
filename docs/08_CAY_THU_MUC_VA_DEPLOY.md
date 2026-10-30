# 08 — Cây thư mục và GitHub Pages

## Quyết định ngày 29/10/2026

Giữ `generator/` làm nguồn sinh đề và `docs/` làm tài liệu. Giữ nguyên `site/Toan5/`, tên các đề và khóa `mia5:cd{n}-de{i}`. Không chuyển hàng loạt sang `src/` vì chưa cần thiết cho phạm vi hiện tại và có thể làm hỏng đường dẫn cũ. Không xóa bản `Toan5/` ngoài repo.

```text
Lop_5_Mia/
├─ AGENTS.md, README.md, .gitignore, .gitattributes
├─ docs/                         tài liệu bàn giao và quyết định
├─ generator/                    nguồn Python/JS, engine, font, dữ liệu câu hỏi
│  ├─ common/, tests/, assets/   giữ nguyên các nguồn đang có
│  ├─ package.json, package-lock.json
│  └─ out/Toan5/                 HTML tự chứa, không commit
├─ tools/
│  ├─ build.js, build.py         điều phối build + bước Python HTML/assets
│  ├─ render_overviews.js        xuất 6 PNG đồng bộ với giao diện
│  ├─ responsive.js              8 kích thước × sáng/tối, kiểm tra đọc/touch
│  ├─ check_links.py             kiểm tra link đúng hoa/thường
│  ├─ serve.py                   HTTP local tại /Lop_5_Mia/
│  ├─ qa.js                      kiểm thử trình duyệt local/online
│  └─ templates/home.html        nguồn trang chủ chung
├─ site/                         chỉ thư mục này được xuất bản
│  ├─ index.html                 trang chọn môn; Tiếng Anh đang chuẩn bị
│  ├─ .nojekyll
│  ├─ assets/                    fonts.css, engine.css/js, overview.css/js dùng chung
│  └─ Toan5/                     36 đề + 6 tổng quan HTML/PNG + trang chủ Toán
├─ artifacts/                    ảnh và báo cáo QA, không commit
└─ .github/workflows/pages.yml   build → QA → deploy
```

## Build và tài nguyên chung

Chạy từ gốc repo:

```text
npm ci --prefix generator
npx --prefix generator playwright install chromium
node tools/build.js --regenerate
```

`--regenerate` sinh lại dữ liệu CĐ4–6 từ Python trước khi build. CĐ1–3 giữ nguồn JS đã bàn giao. Bản web tự cập nhật vào `site/`; không còn bước chép thủ công từ `generator/out/`.

`python tools/build.py --standalone` chỉ xuất HTML tự chứa vào `generator/out/Toan5/` để gửi file lẻ; không cập nhật `site/`. Có thể dùng cùng `--regenerate`.

Bản web chia sẻ font/engine/CSS ở `site/assets/`. CSS font vẫn nhúng dữ liệu base64 gốc, không đổi bộ font và không tải font từ bên thứ ba. Riêng tổng HTML và tài nguyên chung giảm từ 12.572.440 byte xuống khoảng 932.665 byte (không tính PNG). Sau đợt đổi màu được chủ repo duyệt, cả sáu PNG được xuất lại từ HTML và font nhúng để trang chủ hiển thị đúng màu. Không xóa hoặc đổi tên PNG; bản giao ban đầu còn trong lịch sử Git (`db1d936`). QA lưu ảnh kiểm tra riêng trong `artifacts/`.

## Deploy

Địa chỉ: https://okeydokey8525.github.io/Lop_5_Mia/

Chọn GitHub Pages với nguồn **GitHub Actions**. Workflow `.github/workflows/pages.yml` chạy khi push `main`, kiểm tra PR hoặc chạy thủ công. CI dùng Python 3.13, Node 24, cài phụ thuộc bằng lockfile, sinh lại đề, build web, audit, kiểm tra link và chạy hồi quy 36 đề trên Chromium dưới đúng tiền tố `/Lop_5_Mia/`. Chỉ deploy khi toàn bộ bước trước đạt. PR chỉ kiểm tra, không deploy.

Chỉ `site/` được đưa vào Pages artifact. Không xuất bản `generator/`, `docs/`, PDF hoặc ảnh scan. Trong trường hợp CI thất bại, bản Pages trước đó vẫn được giữ.

- Mọi đường dẫn nội bộ tương đối; công cụ link kiểm tra chính xác hoa/thường cả trên Windows.
- Không đổi khóa tiến độ. `localStorage` theo origin và trình duyệt; tiến độ từ file/local không tự chuyển lên GitHub Pages, cũng không đồng bộ thiết bị.
- Giữ giao diện Toán cũ; chỉ thêm liên kết về trang chọn môn.
- Tiếng Anh chưa có đề, không tạo liên kết giả hoặc trang lỗi.

## Kiểm chứng

Local: 36/36 đề đạt 100/100, 44 trang không tràn ngang ở 400px, 196 tham chiếu tĩnh hợp lệ; đã kiểm tra liên kết dựng bằng JavaScript, giữ điểm tốt nhất, nộp thiếu câu, làm lại và tải lại tiến độ. Trước sửa nhãn SVG, bản HTML tự chứa tái tạo khớp nội dung 43/43 HTML đã giao (chuẩn hóa xuống dòng). Sau đó chỉ chỉnh khung/nhãn hình để tránh cắt chữ; đã đối chiếu 864/864 câu với commit bàn giao, nội dung, dữ liệu, đáp án và lời giải không đổi.

Online đã kiểm tra lúc **29/10/2026 18:22:52 UTC+7** tại https://okeydokey8525.github.io/Lop_5_Mia/.

- GitHub Actions build và deploy thành công cho commit mã nguồn `5d9dcde`: https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/40864588679.
- Chạy `node tools/qa.js https://okeydokey8525.github.io/Lop_5_Mia/ --no-shots`: 36/36 đề đạt 100/100, 44 trang không tràn ngang ở 400px, không lỗi console/request; link động, nhãn SVG, nộp thiếu câu, làm lại, giữ điểm cao nhất và tiến độ sau tải lại đều đạt.
- Tải trực tiếp 53 file xuất bản (HTML, PNG, CSS, JS) và so sánh byte với build local: 53/53 khớp. `.nojekyll` là chỉ thị build, không nằm trong phép so sánh tài nguyên công khai này.
- Báo cáo local: `artifacts/local/report.json`; online: `artifacts/online/report.json`, `artifacts/online/files.json` (không commit vì là kết quả QA sinh tự động).
- Chưa có phản hồi làm thử của em gái; không dùng QA tự động để khẳng định độ khó phù hợp hoặc mọi đáp án đã được giải độc lập.

## Build và responsive sau đợt hồng anh đào

Dùng `node tools/build.js --regenerate` từ gốc repo. Node gọi Python để sinh HTML/assets, sau đó gọi Chromium trực tiếp để xuất PNG. `node tools/build.js --standalone` xuất HTML tự chứa; không cần render PNG. `python tools/build.py` vẫn dùng được cho riêng HTML/assets, nhưng không phải lệnh build web đầy đủ.

Reader và poster dùng cùng một nguồn nội dung; reader được dựng từ cây poster, không có bộ văn bản riêng để lệch nhau. Nội dung bảng giá trị 7 hàng được giữ nguyên và cho cuộn bên trong bảng. Menu chọn đề thu gọn bằng `details`, thao tác được bằng bàn phím/cảm ứng.

CI chạy thêm `node tools/responsive.js --no-shots`: toàn bộ 44 trang ở 320/360/390/400/768/820/1024/1366px, cả sáng/tối; so sánh đủ nội dung reader/poster, chuyển chế độ, mở menu và thao tác nộp bài cảm ứng.

## Kiểm chứng online sau đổi màu

Đã kiểm tra 29/10/2026 18:54:48 UTC+7, mã giao diện `5575173`, workflow: https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/40868615954.

- GitHub Actions build và deploy đạt, bao gồm audit, link, 36 đề và 704 tổ hợp responsive trên Linux.
- Chạy trực tiếp trên URL thật: 704 tổ hợp đều đạt, không tràn ngang; kiểm tra đủ nội dung reader, chuyển view, menu, cảm ứng và khoảng trống dưới câu cuối sau nộp. Không lỗi console/request trong bộ làm bài; 36/36 đề 100/100, điểm và thống kê còn sau tải lại.
- 49/49 HTML/CSS/JS online khớp byte với build local. 6/6 PNG online hợp lệ, rộng 1080px. PNG được render trên Linux CI nên không yêu cầu khớp từng pixel/byte với bản Windows; nội dung lấy từ cùng HTML và font nhúng.
- Báo cáo: `artifacts/responsive-online/report.json`, `artifacts/online/report.json`, `artifacts/online/files-sakura.json` (không commit). Ảnh kiểm tra thủ công ở `artifacts/responsive-local/`.
- Đây là mô phỏng Chromium, chưa thay thế thử trực tiếp trên máy tính bảng/điện thoại thật của em; chưa làm nội dung Tiếng Anh.

## Cấu trúc sau mẫu Unit 1 Tiếng Anh

- Nguồn: `generator/english/u01/{content.py,NOTES.md,common.js,tests/de01..06.js}` và `generator/gen_english.py`.
- Sản phẩm: `site/TiengAnh5/index.html`, `Unit1_AllAboutMe/` gồm 6 đề + tổng quan HTML/PNG. Trang chủ chung có liên kết thật và tiến độ mỗi môn.
- `site/catalog.json`: 42 đề nguồn để QA kiểm tra đầy đủ. Tổng 52 HTML, 7 PNG tổng quan.
- Build Node sinh cả hai môn, renderer xuất 7 PNG. CI hiện kiểm tra 42 đề và 832 tổ hợp responsive trước khi deploy.
- Unit 1 online đã đạt lúc 29/10/2026 20:08:05 UTC+7: https://okeydokey8525.github.io/Lop_5_Mia/TiengAnh5/.
- Mã giao diện `c0ae972`, workflow build/deploy thành công: https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/40878450105.
- QA trên URL thật: 42/42 đề 100/100, 52 HTML, không lỗi console/request; 832 tổ hợp responsive đều đạt. Kiểm tra nhận biến thể chữ, từ sai/thừa, dạng đầy đủ, nối sai/điểm phần, sắp/xóa lại, tham chiếu hồ sơ và reset tách môn đều đạt.
- 58 HTML/CSS/JS/JSON online khớp byte với local. 7 PNG online hợp lệ, rộng 1080px; PNG do Linux CI render nên không yêu cầu byte trùng bản Windows.
- Báo cáo ở `artifacts/online/report.json`, `artifacts/responsive-online/report.json`, `artifacts/online/files-unit1.json`. Hình đã xem ở `artifacts/english-review/`, `artifacts/local/`, `artifacts/responsive-local/`.
- Đã kiểm tra 6 đề Anh standalone qua file URL cũng 100/100, không lỗi. Chưa thử trên máy thật của em, chưa xác nhận độ khó phù hợp; chưa có nghe/chấm nói. Dừng ở Unit 1 để chủ repo xem mẫu trước khi làm các unit khác.

### Tài nguyên tranh Unit 1 (30/10/2026)

`generator/english/u01/images/*.webp` là nguồn, kèm `PROMPTS.md`. `content.picture()` nhúng ảnh để standalone hoạt động ngoại tuyến. Bước web trong `tools/build.py` trích cùng byte ảnh ra `site/assets/english/u01/`, đổi sang URL tương đối; không sửa trực tiếp site. Renderer chờ giải mã tất cả ảnh trước khi chụp PNG.
