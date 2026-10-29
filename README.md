# Lớp 5 Mia

Góc luyện tập lớp 5 cho Mia, chạy bằng website tĩnh và lưu điểm trong trình duyệt.

- Toán 5, Kết nối tri thức với cuộc sống, tập một: 6 chủ đề, 36 đề; mỗi đề 24 câu, 100 điểm.
- Tiếng Anh 5, Global Success, tập một: đang chuẩn bị, chưa có đề.
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

Bản web ở `site/` dùng tài nguyên chung. Muốn gửi đề dưới dạng một file HTML tự chứa: `python tools/build.py --standalone`, lấy file trong `generator/out/Toan5/`.

## Tài liệu và deploy

Đọc `AGENTS.md` trước, sau đó `docs/`. Cấu trúc chính thức và GitHub Actions: `docs/08_CAY_THU_MUC_VA_DEPLOY.md`; hướng dẫn QA: `docs/07_KIEM_TRA.md`.

Workflow chỉ xuất bản `site/` sau khi build và QA đạt. Không đưa PDF sách, ảnh scan hoặc bản trích dài vào repo public. Không sửa trực tiếp HTML đã build; sửa nguồn rồi build lại.

Tiến độ không đồng bộ thiết bị, trình duyệt hoặc từ bản mở file/local sang Pages. Chưa có phản hồi làm thử của học sinh để đánh giá độ khó.
