# Lớp 5 Mia

Góc luyện tập lớp 5 cho Mia, chạy bằng website tĩnh và lưu điểm trong trình duyệt.

- Toán 5, Kết nối tri thức với cuộc sống, tập một: 6 chủ đề, 36 đề; mỗi đề 24 câu, 100 điểm.
- Tiếng Anh 5, Global Success, tập một: Unit 1–3 (All about me!, Our homes, My foreign friends), 3 tổng quan + 18 đề (432 câu), có nghe ở ba cấp.
- Toán học kì 2: chờ sách.

## Xem và phát triển

Địa chỉ Pages: https://okeydokey8525.github.io/Lop_5_Mia/ (trạng thái triển khai ở `docs/01_TINH_TRANG.md`).

Cần Python 3.13+ và Node 24. Chạy từ gốc repo:

```text
npm ci --prefix generator
npx --prefix generator playwright install chromium
node tools/build.js --regenerate
node generator/audit.js
python tools/check_links.py
python tools/serve.py
```

Mở http://127.0.0.1:8765/Lop_5_Mia/ để xem. Giữ server chạy và dùng terminal khác: `node tools/qa.js`.

Bản web ở `site/` dùng tài nguyên chung. Muốn gửi đề dưới dạng một file HTML tự chứa: `node tools/build.js --standalone`, lấy file trong `generator/out/Toan5/` hoặc `generator/out/TiengAnh5/`.

## Tài liệu và deploy

Đọc `AGENTS.md` trước, sau đó [mục lục docs](docs/README.md). Cấu trúc chính thức và GitHub Actions: `docs/08_CAY_THU_MUC_VA_DEPLOY.md`; hướng dẫn QA: `docs/07_KIEM_TRA.md`.

Workflow chỉ xuất bản `site/` sau khi build và QA đạt. Không đưa PDF sách, ảnh scan hoặc bản trích dài vào repo public. Không sửa trực tiếp HTML đã build; sửa nguồn rồi build lại.

Tiến độ không đồng bộ thiết bị, trình duyệt hoặc từ bản mở file/local sang Pages. Chưa có phản hồi làm thử của học sinh để đánh giá độ khó.

Trang Tiếng Anh: https://okeydokey8525.github.io/Lop_5_Mia/TiengAnh5/. Toàn site hiện 54 đề chính thức và 67 trang HTML; QA dùng `site/catalog.json` để phát hiện thiếu hoặc thừa đề.

Bài học sau sửa Unit 1 và kế hoạch tiếp theo nằm trong `docs/breakdowns/`; quy trình tranh ở `docs/playbooks/TRANH_MINH_HOA.md`; skill dự án ở `.agents/skills/mia-learning-illustrations/SKILL.md`. Cây máy/repo hiện hành nằm trong docs/08, snapshot cũ ở docs/history.

Mẫu nghe Unit 1 (6 câu, 3 cấp, đã duyệt): https://okeydokey8525.github.io/Lop_5_Mia/TiengAnh5/Unit1_AllAboutMe/LuyenNghe_Mau.html. Chạy kiểm tra riêng: `node tools/qa_listening.js`; chưa tính vào điểm/sao sáu đề.

Unit 1 hiện đã có 6 câu nghe trong mỗi đề (2 mỗi cấp), vẫn 24 câu/100 điểm. Phần Anh mặc định hồng sáng, có nút Sáng/Tối. Điểm bộ có nghe dùng phiên bản mới, dữ liệu cũ vẫn giữ. Kiểm tra thêm: node tools/qa_english_unit1.js; node tools/qa_english_units23.js.

Toàn website nay dùng hồng sáng và nút Sáng/Tối chung, giữ lựa chọn khi chuyển Toán/Anh. Nguồn: generator/theme.css/js. Kiểm tra: node tools/qa_theme.js.

Trang chủ chọn môn có lời chào, thanh tiến độ thật và động viên khi hoàn thành thêm lượt luyện tập. Nguồn tools/templates/home.{html,css,js}; kiểm tra node tools/qa_home.js.

Các đề nay tự lưu nháp trên cùng trình duyệt để làm tiếp khi quay lại, gồm đáp án và thời gian đã làm. Danh sách đề ghi Đang làm dở; có nút bỏ nháp, tách khỏi điểm đã nộp. Khi đóng/ẩn trang đồng hồ tạm dừng. Kiểm tra hồi quy: node tools/qa_drafts.js.
