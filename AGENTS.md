# AGENTS.md — Lớp 5 Mia (đọc file này đầu tiên)

Repo: https://github.com/Okeydokey8525/Lop_5_Mia (public). Chủ repo: Lê Đức Lương (sinh viên IT năm cuối), dùng cho việc dạy em gái lớp 5.
Trả lời và viết nội dung cho học sinh **bằng tiếng Việt**. Chủ repo thích: nói thẳng, đúng sự thật, không bịa, kiểm tra kỹ rồi mới báo xong.

## Dự án là gì
Bộ đề kiểm tra trực tuyến cho học sinh lớp 5, mỗi đề là **một file HTML tự chứa** (không cần server), tiến độ lưu bằng `localStorage`.
- **Toán 5** (Kết nối tri thức với cuộc sống, tập một): Chủ đề 1–6, 36 đề, **đã xong**.
- **Toán 5 học kì 2:** chủ repo sẽ đưa sách sau. Chưa làm. Xem mục "Chỗ trống" bên dưới.
- **Tiếng Anh 5** (Global Success, Sách học sinh tập 1, 83 trang scan): **việc tiếp theo**. Đặc tả ở `docs/09_TIENG_ANH.md`.

## Việc của bạn (Codex)
1. Làm tiếp Tiếng Anh 5 theo `docs/09_TIENG_ANH.md`, mỗi unit là một chủ đề, mỗi chủ đề có 1 trang tổng quan + 6 đề.
2. Sắp xếp lại cây thư mục cho gọn và đưa site lên GitHub Pages (hoặc Vercel) theo `docs/08_CAY_THU_MUC_VA_DEPLOY.md`. Bạn được tự quyết cây cuối cùng, nhưng phải ghi quyết định vào file đó.
3. Khi chủ repo đưa PDF Toán học kì 2: thêm các chủ đề Toán tiếp theo (`docs/06_THEM_CHU_DE_MOI.md`).

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
