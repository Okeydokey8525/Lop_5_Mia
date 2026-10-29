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
