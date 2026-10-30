---
name: mia-learning-illustrations
description: Create or revise vocabulary illustrations for the Lop_5_Mia learning site, integrating source assets and checking quiz, reader, poster and standalone output. Use for lesson-picture work in this repository, not exact mathematical diagrams or unrelated websites.
---

# Tranh học tập Lớp 5 Mia

Đọc `AGENTS.md` từ gốc repo. Quy trình chi tiết và tiêu chí nghiệm thu: `docs/playbooks/TRANH_MINH_HOA.md`. Lỗi thực tế và bằng chứng: `docs/breakdowns/2026-10-30_BAI_HOC_UNIT1.md`.

- Kiểm kê hình từ nguồn của unit, gồm tổng quan và mọi câu hỏi. Mục tiêu là trẻ nhận ra chủ thể ở kích thước thực; không thêm chữ đáp án lên tranh.
- Theo phong cách/mẫu chủ repo đã duyệt. Yêu cầu xem mẫu trước thì dừng ở mẫu; chỉ triển khai toàn bộ sau khi được giao. Skill không cấp quyền mở rộng unit hay tự deploy.
- Dùng công cụ tạo ảnh khi có sẵn cho minh họa từ vựng; giữ SVG/code cho hình học cần đúng số đo. Lưu file nguồn build trong repo, prompt cạnh ảnh, giữ bản gốc và không đưa scan SGK vào Git.
- Sửa nguồn generator; build tạo web asset tương đối và standalone tự chứa. Bảo toàn câu hỏi, đáp án và khóa tiến độ khi chỉ đổi hình.
- Kiểm tra giải mã ảnh trước xuất PNG, tỷ lệ ở reader, kích thước nhỏ và sáng/tối. Audit Unit 1 hiện chỉ chấp nhận sáu WebP đã duyệt; nếu mở rộng phải đăng ký ảnh/đơn vị mới có chủ đích, không tắt audit.
- Chạy QA phù hợp theo docs07; xem ảnh render cuối cùng. Phân biệt kiểm chứng local, live, mô phỏng trình duyệt và phản hồi học sinh trong báo cáo.
