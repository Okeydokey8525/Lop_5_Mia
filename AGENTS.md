# AGENTS.md — Lớp 5 Mia (đọc file này đầu tiên)

Repo: https://github.com/Okeydokey8525/Lop_5_Mia (public). Chủ repo: Lê Đức Lương (sinh viên IT năm cuối), dùng cho việc dạy em gái lớp 5.
Trả lời và viết nội dung cho học sinh **bằng tiếng Việt**. Chủ repo thích: nói thẳng, đúng sự thật, không bịa, kiểm tra kỹ rồi mới báo xong.

## Dự án là gì
Bộ đề kiểm tra trực tuyến cho học sinh lớp 5, bản web dùng tài nguyên chung; có thể xuất mỗi đề thành **một file HTML tự chứa** (không cần server), tiến độ lưu bằng `localStorage`.
- **Toán 5** (Kết nối tri thức với cuộc sống, tập một): Chủ đề 1–6, 36 đề, **đã xong**.
- **Toán 5 học kì 2:** chủ repo sẽ đưa sách sau. Chưa làm. Xem mục "Chỗ trống" bên dưới.
- **Tiếng Anh 5** (Global Success, tập 1): đã làm mẫu Unit 1, 1 tổng quan + 6 đề, chủ repo đã xem và duyệt bộ tranh sửa; các unit khác chưa triển khai. Đặc tả ở `docs/09_TIENG_ANH.md`.

## Phạm vi đã chốt ngày 29/10/2026

Chủ repo yêu cầu ưu tiên cấu trúc, chuẩn hóa build/QA, kiểm chứng bộ Toán, trang chủ chung và GitHub Pages. Đợt giao diện đã hoàn tất. Sau đó chủ repo yêu cầu làm mẫu **Unit 1 Tiếng Anh** theo kế hoạch đã chốt; chưa làm các unit còn lại. Cây thư mục giữ `generator/`, `docs/`, `site/Toan5/`, thêm `tools/` và `site/assets/`; xem `docs/08`.

Lệnh từ gốc repo: `node tools/build.js --regenerate`, `node generator/audit.js`, `python tools/check_links.py`, `python tools/serve.py` rồi `node tools/qa.js` ở terminal khác. Không sửa trực tiếp `site/`; trang chủ chung sinh từ `tools/templates/home.html`. PDF nằm ngoài repo.

## Việc của bạn (Codex)
1. Làm tiếp Tiếng Anh 5 theo `docs/09_TIENG_ANH.md`, mỗi unit là một chủ đề, mỗi chủ đề có 1 trang tổng quan + 6 đề.
2. Sắp xếp lại cây thư mục cho gọn và đưa site lên GitHub Pages (hoặc Vercel) theo `docs/08_CAY_THU_MUC_VA_DEPLOY.md`. Bạn được tự quyết cây cuối cùng, nhưng phải ghi quyết định vào file đó.
3. Khi chủ repo đưa PDF Toán học kì 2: thêm các chủ đề Toán tiếp theo (`docs/06_THEM_CHU_DE_MOI.md`).

## Giao diện đã được duyệt

Ngày 29/10/2026, chủ repo duyệt đổi sang hồng anh đào và sửa responsive. Giữ font, nội dung, hiệu ứng và tiến độ; màu hiện hành ở `docs/05_THIET_KE.md`. Trang tổng quan có chế độ đọc từng bài cho màn hình ≤820px và poster 1080px cho màn hình lớn/in. `node tools/build.js` build cả HTML, tài nguyên và PNG; `python tools/build.py` chỉ là bước HTML/assets. Không gọi renderer Chromium từ Python Microsoft Store trên Windows vì tiến trình con có thể nhìn sai đường dẫn cache trình duyệt.

## Tiếng Anh — cấu trúc hiện hành

Nguồn Unit 1 ở `generator/english/u01/content.py`, ghi nhận trang đã đọc ở `NOTES.md`; `common.js` và `tests/*.js` sinh từ nguồn này. `generator/gen_english.py` dùng chung khung đề, tổng quan và trang chủ. Sản phẩm ở `site/TiengAnh5/`, ID `en-u01-de1..6`. `site/catalog.json` liệt kê chính xác 42 đề (36 Toán, 6 Anh) để QA đối chiếu đủ file. Không xóa điểm môn khác khi reset một môn. Giao diện bằng tiếng Việt, câu hỏi tiếng Anh. Chưa có nghe/nói. Chưa mở rộng ngoài Unit 1; chờ chủ repo giao chủ đề tiếp theo.

## Bài học và quy trình dùng lại

Khi làm tranh bài học, đọc `.agents/skills/mia-learning-illustrations/SKILL.md` và `docs/playbooks/TRANH_MINH_HOA.md`. Bài học thực tế ở `docs/breakdowns/2026-10-30_BAI_HOC_UNIT1.md`; công việc tiếp theo ở `docs/breakdowns/KE_HOACH_TIEP_THEO.md`. Mục lục ở `docs/README.md`; `docs/history/` là snapshot cũ, không phải trạng thái hiện hành. Tranh Unit 1 đã được chủ repo duyệt và cập nhật đủ sáu hình ngày 30/10/2026. Sách trên máy này nay ở `../tai_lieu/sach/`, bản bàn giao cũ ở `../luu_tru/`; không dùng bản cũ làm nguồn sửa.

## Quy tắc cứng
1. **Giữ nguyên thiết kế** hiện có (`docs/05_THIET_KE.md`): màu, font, bố cục trang tổng quan, hiệu ứng trang chủ. Chỉ thêm, không đổi giao diện cũ trừ khi chủ repo yêu cầu.
2. **Đáp án phải do code tính ra** từ cùng số liệu của đề (Python `Decimal`/`Fraction`). Không gõ tay đáp án và lời giải riêng rẽ.
3. **Không bịa nội dung sách.** Nội dung bám đúng mục lục/bài của sách; chỗ nào không đọc được thì ghi rõ và hỏi chủ repo. Đề, hình vẽ và bài toán là **tự soạn**, không chép nguyên văn sách.
4. **Không commit sách giáo khoa** (PDF, ảnh scan, văn bản trích) vào repo public. Đã có trong `.gitignore`. Giữ sách ở thư mục ngoài repo.
5. Mỗi đề Toán: 24 câu = 10 Trung bình + 8 Khá + 6 Giỏi (3/5/5 điểm, tổng 100). Đề Tiếng Anh dùng cùng khung (xem `docs/04_QUY_CACH_DE.md`).
6. **Chạy QA trước khi báo xong** (`docs/07_KIEM_TRA.md`): audit số câu, tự làm đúng hết ra 100/100 không lỗi console, kiểm tra link (phân biệt hoa thường), xem ảnh render bằng mắt.
7. Việc xóa file hoặc đổi tên hàng loạt: ghi kế hoạch trước, không xóa nội dung đã giao cho chủ repo mà chưa hỏi.
8. Đường dẫn trong site phải **tương đối** (Pages dạng project nằm dưới `/Lop_5_Mia/`).
9. Báo cáo cuối: ngắn, nói đã làm gì, đã kiểm tra gì, còn gì chưa chắc.

## Bản đồ tài liệu
| File | Nội dung |
|---|---|
| `docs/01_TINH_TRANG.md` | Đã xong gì, việc kế tiếp |
| `docs/02_KIEN_TRUC.md` | Pipeline sinh đề, build, `localStorage` |
| `docs/03_SCHEMA_CAU_HOI.md` | Các dạng câu hỏi và cú pháp |
| `docs/04_QUY_CACH_DE.md` | Quy cách mỗi đề, xếp loại, văn phong |
| `docs/05_THIET_KE.md` | Hệ thống thiết kế cần giữ |
| `docs/06_THEM_CHU_DE_MOI.md` | Quy trình thêm chủ đề |
| `docs/07_KIEM_TRA.md` | QA và tiêu chí đạt |
| `docs/08_CAY_THU_MUC_VA_DEPLOY.md` | Cây thư mục, GitHub Pages / Vercel |
| `docs/09_TIENG_ANH.md` | Đặc tả Tiếng Anh 5 |

## Chỗ trống (chủ repo sẽ điền sau)
- **Toán học kì 2:** tên bài, số trang, PDF sách. Khi có, điền vào `docs/01_TINH_TRANG.md` mục "Toán học kì 2" rồi làm theo `docs/06_THEM_CHU_DE_MOI.md`.
- **Tiếng Anh 5 tập 2:** chưa có.
