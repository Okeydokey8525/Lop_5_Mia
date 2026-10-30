# 08 — Cây thư mục, build và deploy hiện hành

Cập nhật 30/10/2026. Các bản ghi kiểm chứng trước đó giữ trong `history/2026-10-30_TRUOC_SAP_XEP_08_CAY_THU_MUC_VA_DEPLOY.md`. Trạng thái sản phẩm đọc ở [01](01_TINH_TRANG.md).

## Không gian làm việc trên máy

```text
C:/LeDucLuong/Mia/
├─ HUONG_DAN_THU_MUC.md
├─ Lop_5_Mia/                       repo đang phát triển
├─ tai_lieu/sach/                   PDF gốc, ngoài repo public
└─ luu_tru/
   ├─ ban_giao_ban_dau/             Toan5/ và poster.png cũ, chỉ tham khảo
   ├─ anh_kiem_tra_20261029/         ảnh render/đối chiếu cũ từ _to_delete
   └─ SAP_XEP_20261030.json          đường dẫn trước/sau và SHA-256
```

Ngày 30/10 đã di chuyển 119 file, kiểm tra SHA-256 trước/sau, không xóa file. Bản cũ không phải nguồn build. PDF không được chép trở lại repo; cấu trúc ngoài repo chỉ có trên máy này, không tự xuất hiện khi git clone ở máy khác.

## Cây repo

```text
Lop_5_Mia/
├─ AGENTS.md, README.md
├─ .agents/skills/mia-learning-illustrations/SKILL.md
├─ docs/
│  ├─ README.md                    mục lục và thứ tự đọc
│  ├─ 01..09_*.md                  quy ước/trạng thái hiện hành
│  ├─ breakdowns/                  bài học, phân rã công việc tiếp theo
│  ├─ playbooks/                   quy trình áp dụng lại
│  └─ history/                     snapshot cũ, không dùng làm hướng dẫn mới
├─ generator/                      nguồn sinh đề, engine, fonts
│  ├─ common/, tests/, assets/     nguồn Toán đã bàn giao
│  ├─ english/u01/
│  │  ├─ content.py, NOTES.md      nội dung gốc + trang sách đã đối chiếu
│  │  ├─ images/*.webp, PROMPTS.md tranh nguồn + prompt (PROMPTS ở images/)
│  │  ├─ listening.py, listening.html  nguồn mẫu nghe 3 cấp
│  │  └─ common.js, tests/         dữ liệu JS sinh từ content.py
│  ├─ package.json, package-lock.json
│  └─ out/{Toan5,TiengAnh5}/       HTML tự chứa, không commit
├─ tools/                         build, serve, QA, templates/home.html
├─ site/                          chỉ thư mục này được xuất bản
│  ├─ index.html, catalog.json, .nojekyll
│  ├─ assets/                     font/engine/overview, english/u01/*.webp
│  ├─ Toan5/                      36 đề, 6 tổng quan HTML/PNG, trang chủ
│  └─ TiengAnh5/                   Unit 1: 6 đề, mẫu nghe, tổng quan HTML/PNG, trang chủ
├─ artifacts/                     ảnh/báo cáo QA tự sinh, không commit
└─ .github/workflows/pages.yml
```

Giữ đường dẫn nguồn hiện có để không phá import Python, script Node hoặc các URL/ID tiến độ đã bàn giao. Không gom tất cả Python/JS theo phần mở rộng; chúng liên kết theo pipeline. `docs/`, skill và ảnh nguồn được quản lý Git, còn out/node_modules/artifacts là dữ liệu sinh/cài lại được. Không tạo thêm repo hoặc bản website hoạt động cạnh tranh trong thư mục lưu trữ.

## Build

Cần Node 24, Python 3.13+. Chạy từ gốc repo:

```text
npm ci --prefix generator
npx --prefix generator playwright install chromium
node tools/build.js --regenerate
node generator/audit.js
python tools/check_links.py
python tools/serve.py
```

Terminal khác: `node tools/qa.js --no-shots`, `node tools/responsive.js --no-shots`. Có thể bỏ `--no-shots` để lưu ảnh. HTTP local ở `http://127.0.0.1:8765/Lop_5_Mia/`. Chi tiết/giới hạn kiểm tra ở [07](07_KIEM_TRA.md).

`--regenerate` sinh lại dữ liệu Toán CĐ4–6; Anh luôn sinh từ content.py. Node gọi Python để tạo HTML/assets, rồi gọi Chromium trực tiếp để render 7 PNG. Trên Windows không đưa Chromium thành tiến trình con của Python Microsoft Store vì từng gặp lệch filesystem/cache trình duyệt.

`node tools/build.js --standalone` xuất HTML tự chứa cho cả hai môn trong generator/out, không cập nhật site. Web dùng CSS/JS/ảnh chung; standalone nhúng cùng tài nguyên. Với tranh Anh, picture() nhúng WebP, bước web trích đúng byte vào assets và đổi URL tương đối. Renderer chờ font và giải mã ảnh trước chụp poster. Nguồn fonts.css vẫn dùng được nhưng script tạo lại font gốc chưa có trong repo.

## GitHub Pages

Website: https://okeydokey8525.github.io/Lop_5_Mia/. Nguồn Pages là GitHub Actions. Workflow chạy khi push main, PR hoặc dispatch; build, audit, kiểm tra link, 42 đề, QA mẫu nghe và 848 tổ hợp responsive. Chỉ deploy sau khi các bước đạt; PR chỉ kiểm tra. Số lượng hiện tại phải cập nhật theo catalog khi thêm unit.

Chỉ site/ được upload; không xuất bản nguồn, docs hay sách. Giữ URL tương đối và đúng hoa/thường. Tiến độ local/file không chuyển sang origin online; không đổi ID nếu chỉ sửa tranh/giao diện.

Khi được giao xuất bản: push thay đổi đã kiểm tra, chờ workflow và deploy thành công, rồi kiểm tra chính URL thật và tài nguyên mới. Không dùng build local hoặc trạng thái push thành công để báo website đã chạy đúng. Nếu chỉ được giao tài liệu thì kiểm tra tài liệu, không cần chạy lại toàn bộ render/test sản phẩm.
