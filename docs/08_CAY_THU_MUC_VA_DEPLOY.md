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
│  ├─ english/u02/..u05/   content.py, NOTES.md, images/, common.js, tests/
│  ├─ english/units.py             registry Unit 1–5, catalog/ID
│  ├─ package.json, package-lock.json
│  └─ out/{Toan5,TiengAnh5}/       HTML tự chứa, không commit
├─ tools/                         build, serve, QA, templates/home.html
├─ site/                          chỉ thư mục này được xuất bản
│  ├─ index.html, catalog.json, .nojekyll
│  ├─ assets/                     font/engine/overview, english/u01..u05/*.webp
│  ├─ Toan5/                      36 đề, 6 tổng quan HTML/PNG, trang chủ
│  └─ TiengAnh5/                   Unit 1–5: 30 đề, mẫu nghe, 5 tổng quan HTML/PNG, trang chủ
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

`--regenerate` sinh lại dữ liệu Toán CĐ4–6; Anh luôn sinh từ content.py. Node gọi Python để tạo HTML/assets, rồi gọi Chromium trực tiếp để render 18 PNG. Trên Windows không đưa Chromium thành tiến trình con của Python Microsoft Store vì từng gặp lệch filesystem/cache trình duyệt.

`node tools/build.js --standalone` xuất HTML tự chứa cho cả hai môn trong generator/out, không cập nhật site. Web dùng CSS/JS/ảnh chung; standalone nhúng cùng tài nguyên. Với tranh Anh, picture() nhúng WebP, bước web trích đúng byte vào assets và đổi URL tương đối. Renderer chờ font và giải mã ảnh trước chụp poster. Nguồn fonts.css vẫn dùng được nhưng script tạo lại font gốc chưa có trong repo.

## GitHub Pages

Website: https://okeydokey8525.github.io/Lop_5_Mia/. Nguồn Pages là GitHub Actions. Workflow chạy khi push main, PR hoặc dispatch; build, audit, kiểm tra link, 108 đề, QA nghe/Units 1–10/Review 1–2/tiến độ và nháp/học từ và 2272 tổ hợp responsive. Chỉ deploy sau khi các bước đạt; PR chỉ kiểm tra. Số lượng hiện tại phải cập nhật theo catalog khi thêm unit.

Chỉ site/ được upload; không xuất bản nguồn, docs hay sách. Giữ URL tương đối và đúng hoa/thường. Tiến độ local/file không chuyển sang origin online; không đổi ID nếu chỉ sửa tranh/giao diện.

Khi được giao xuất bản: push thay đổi đã kiểm tra, chờ workflow và deploy thành công, rồi kiểm tra chính URL thật và tài nguyên mới. Không dùng build local hoặc trạng thái push thành công để báo website đã chạy đúng. Nếu chỉ được giao tài liệu thì kiểm tra tài liệu, không cần chạy lại toàn bộ render/test sản phẩm.

### Tài nguyên dùng chung cho Anh và phiên bản đề có nghe

Nguồn generator/english/{theme.css,theme.js,speech.js}, được nhúng vào standalone và trích ra site/assets/english khi build web. Module speech dùng riêng các đề có nghe, quản lý một luồng phát và cleanup khi làm lại/rời trang. Nguồn câu nghe generator/english/u01/exam_listening.py thay đúng sáu vị trí trong content.build_tests(); không thêm trang đề mới hoặc đổi URL. Catalog, trang chủ Anh và thống kê ở trang chủ chung cùng đọc ID en-u01-deN-v2, không trộn điểm bộ trước.

### Theme toàn website

Nguồn theme dùng chung tại generator/theme.css và generator/theme.js, xuất ra site/assets/theme.css/js. tools/build.py nhúng vào toàn bộ HTML cả hai môn trước khi xử lý --standalone; bản web tách ra liên kết tương đối. Trang chủ chung cũng được gắn đúng hai tài nguyên này. gen_english.py chỉ nhúng module speech riêng của Anh; không còn nhúng theme theo môn. Mỗi trang có đúng một nút chuyển màu. Hai file theme cũ trong english đã được đổi vị trí bằng Git, không giữ hai nguồn cạnh tranh. 18 PNG tổng quan được xuất lại sau build.

### Nguồn trang chủ chọn môn

Bộ nguồn tools/templates/home.{html,css,js}; CSS/JS xuất riêng ra site/assets/home.{css,js}. Build thay __HOME_TESTS__ bằng đúng danh sách sinh catalog.json trước khi viết HTML. Chỉ root index và hai tài nguyên home đổi khi điều chỉnh hiệu ứng trang chọn môn; không sửa nguồn câu hỏi.

Review có thư mục nguồn `english/r01/`, `r02/`, web `TiengAnh5/Review1_Units1_5/`, `Review2_Units6_10/`; ảnh tái dùng từ các Unit trong assets/english/uNN. Registry TOPICS giữ thứ tự theo sách; catalog có kind/topic/overview để runner không suy tên URL từ số Unit.

### Unit 11 tập hai và âm thanh đi kèm (18/11/2026)

Nguồn `english/u11/`, web `TiengAnh5/Unit11_FamilyTime/`. Nguồn WAV/manifest trong `u11/audio/`, trích ra `site/assets/english/u11/audio/`; standalone nhúng audio. `english/recorded.py` và `recorded.js` chỉ được gắn vào trang có manifest, không thay phương thức nghe của Unit cũ. Công cụ tạo WAV `tools/generate_english_audio.ps1` là bước tác giả riêng, không chạy trong CI. CI cài Chromium và WebKit để kiểm file nghe thật. Bản nguồn có 114 đề/150 HTML/19 poster; cập nhật số kiểm chứng ở bàn giao Unit 11.

### Units 12–13 (19/11/2026)

Nguồn `generator/english/u12/`, `u13/`; web `TiengAnh5/Unit12_OurTetHoliday/`, `Unit13_OurSpecialDays/`. Mỗi nguồn có content/study/overview/NOTES/audio_source, images/PROMPTS, audio/manifest + WAV, common/tests sinh từ Python. Dùng chung recorded.py/js; generator nhận manifest theo Unit, web trích audio trong đúng namespace uNN để clip ABC giống nhau không đổi URL Unit cũ. QA audio nhận `--unit=11|12|13` và `--webkit`. Không thêm thư mục app mới hoặc thư viện runtime. Tổng 126 đề, 166 HTML, 21 poster; chỉ site/ xuất bản.

### Units14–15 — 19/11/2026

Nguồn `generator/english/u14/`, `u15/`; web `TiengAnh5/Unit14_StayingHealthy/`, `Unit15_OurHealth/`. Giữ quy cách content/study/overview/NOTES/audio_source, images/PROMPTS, audio/manifest+WAV và common/tests. Build thường không tạo giọng. Tổng138đề/182HTML/23poster. Công cụ `tools/qa_recorded_all.js` chạy nguyên các gate audio cũ, tối đa3 tiến trình song song trong CI, mỗi Unit/trình duyệt có log riêng; đợi đủ kết quả và trả lỗi nếu bất kỳ gate không đạt. Không giảm nội dung kiểm tra hoặc đổi runtime website.


## Units16–17 — 19/11/2026

Đã bổ sung Unit16 **Seasons and the weather** (tập hai40–45) và Unit17 **Stories for children** (46–51): mỗi Unit6đề/144câu/36nghe, tổng quan HTML/PNG, trang học tự lưu với nghe/chậm/ABC,6hội thoại và12bài luyện. Unit16 có20từ/cụm/98WAV, Unit17 có16từ/cụm/90WAV;8tranh ImageGen mới. Toàn Anh17Unit+2Review=114đề/2736câu; toàn site150đề/198HTML/25poster. Học từ đầy đủ18trang/276từ/109hội thoại/216bài luyện. Xem [bàn giao Units16–17](breakdowns/2026-11-19_UNIT16_UNIT17.md) cho trạng thái local/CI/live và giới hạn iPad thật. Còn **Review3 + Units18–20 + Review4 =5phần/30đề** theo sách; Starter và bộ kiểm tra học kỳ riêng chưa làm.

## Unit18 — 19/11/2026

Bổ sung **Means of transport**, tập hai trang52–57:6đề/144câu/36nghe, tổng quan HTML/PNG, học20từ/cụm với6hội thoại/12bài luyện tự lưu,4tranh phương tiện và84WAV. Trọng tâm want to visit, can + get, by phương tiện/on foot; đọc đúng người và từng chặng theo thẻ giả định. TổngAnh18Unit+2Review=120đề/2880câu; toàn site156đề/206HTML/26poster. Study19trang/296từ/115hội thoại/228bài luyện. Trạng thái local/CI/live và nguồn sách ở [bàn giao Unit18](breakdowns/2026-11-19_UNIT18.md). Còn Review3 + Units19–20 + Review4 =4phần/24đề; không tự mở rộng phần chưa được giao.

## Unit19 — 19/11/2026

Bổ sung **Places of interest**, tập hai trang58–63:6đề/144câu/36nghe, tổng quan HTML/PNG, học20từ/cụm với6hội thoại/12bài luyện tự lưu,4tranh loại địa điểm và104WAV. Trọng tâm think of, it is/they are, How far…from…to…, kilometre/kilometres; ngữ điệu Wh xuống. Thẻ khoảng cách/trường giả định, ý kiến theo người nói; cộng chặng trên cùng tuyến. TổngAnh19Unit+2Review=126đề/3024câu; toànsite162đề/214HTML/27poster. Study20trang/316từ/121hội thoại/240luyện. Nguồn và trạng thái kiểm chứng ở [bàn giao Unit19](breakdowns/2026-11-19_UNIT19.md). Còn Review3 + Unit20 + Review4 =3phần/18đề; Starter và bộ kiểm tra học kỳ riêng chưa làm.


## Unit 20 — 19/11/2026

Bổ sung **Our summer holidays**, tập hai trang 64–69: sáu đề / 144 câu / 36 câu nghe, tổng quan HTML/PNG, 20 từ-cụm với sáu hội thoại và 12 bài luyện tự lưu, bốn tranh hoạt động và 95 WAV kèm bài. Trọng tâm Where…going to visit?/What…going to do?, am/is/are going to + nguyên mẫu; phân biệt last summer và this summer.

Tổng Anh: 20 Unit + 2 Review = **132 đề / 3168 câu**. Toàn site: **168 đề / 222 HTML / 28 tổng quan HTML-PNG**. Study: 21 trang / 336 từ-cụm / 127 hội thoại / 252 bài luyện. Nguồn và trạng thái kiểm chứng: [bàn giao Unit 20](breakdowns/2026-11-19_UNIT20.md). Còn **Review 3 + Review 4 = hai phần / 12 đề**; Starter và bộ kiểm tra học kỳ riêng chưa làm. Không coi đủ 20 Unit là đã hoàn thành các phần ôn tập và kiểm tra.
