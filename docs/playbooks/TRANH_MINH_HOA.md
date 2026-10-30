# Quy trình tranh minh họa cho bài học

Áp dụng khi thêm hoặc thay tranh trong câu hỏi/tổng quan. Với hình học Toán hoặc sơ đồ cần số đo chính xác, dùng SVG/code có kiểm soát; không thay bằng tranh AI trang trí. Với chủ thể từ vựng cần dễ nhận diện, dùng minh họa rõ hình, thống nhất phong cách đã được chủ repo duyệt.

## Chuẩn bị và chọn mẫu

1. Đọc AGENTS, thiết kế và nguồn câu hỏi của unit. Liệt kê tất cả hình đang được gọi; xác định hình xuất hiện ở câu nào, tổng quan nào. Không chỉ sửa ảnh trong screenshot phản hồi.
2. Xác định ý nghĩa cần truyền đạt và những gì dễ gây nhầm. Chủ thể phải nhận ra ở kích thước hiển thị nhỏ; bối cảnh hỗ trợ từ cần học. Không ghi từ đáp án lên hình.
3. Nếu yêu cầu xem mẫu trước: chỉ tạo mẫu và chờ phản hồi. Nếu đã duyệt phong cách cho cả bộ: tiếp tục hoàn thành phạm vi ấy. Có thể dùng mẫu đã duyệt làm tham chiếu khi công cụ hỗ trợ.

## Lưu nguồn và tích hợp

- Nguồn deploy/build đặt trong `generator/english/uNN/images/`, tên thường, không dấu, ví dụ `table-tennis.webp`; ghi prompt, công cụ, kích thước và nguồn gốc trong `PROMPTS.md`.
- Giữ ảnh gốc ngoài repo nếu nặng; không xóa bản gốc khi chuyển định dạng. Không lấy ảnh scan sách đưa vào repo public.
- Unit 1 hiện dùng WebP 768×512. Đây là lựa chọn của bộ đã duyệt; ảnh mới có thể cần kích thước khác. Nếu đổi tỷ lệ, cập nhật cả thuộc tính width/height, CSS và các kiểm tra đang giả định 3:2.
- Sửa nguồn, không sửa site. `picture()` nhúng ảnh cho standalone; `tools/build.py` trích ảnh dùng chung ra site/assets và đổi URL tương đối. Không để ảnh chỉ tồn tại trong generated_images của máy tác giả.
- Giữ tên đề/ID tiến độ. Nếu chỉ thay tranh, so dữ liệu câu hỏi trước/sau sau khi bỏ trường hình để chứng minh không sửa nội dung/đáp án.

## Kiểm tra có ý nghĩa

- Chạy luồng build/audit/link/browser trong [07](../07_KIEM_TRA.md). Audit ảnh phải nhận đúng file nguồn tự tạo; không bỏ trắng quy tắc để cho mọi data URI đi qua.
- Chờ `img.decode()` trước khi chụp hoặc xuất PNG; chờ `document.fonts.ready` riêng. Kiểm tra ảnh lỗi tải, ảnh méo, cắt mất chủ thể, tràn ngang và độ tương phản ở sáng/tối.
- Xem bằng mắt toàn bộ tranh ở kích thước câu hỏi thực tế; xem reader điện thoại, poster desktop và PNG cuối. Không coi ảnh nguồn đẹp là đủ.
- Mở HTML standalone qua file URL để chứng minh không thiếu tài nguyên. Bản web phải tải qua đúng tiền tố /Lop_5_Mia/ và đúng hoa/thường.
- Nếu phạm vi đã bao gồm deploy: đợi build/deploy thành công rồi mở URL thật, kiểm tra chính tài nguyên và trang đã thay. Nếu chưa được giao deploy, báo rõ chỉ hoàn tất local.

## Bàn giao

Báo ngắn: đã thay hình nào/ở đâu, kiểm tra nào đã đạt, local hay live, và điều chưa được kiểm chứng bởi học sinh. Chỉ cập nhật số liệu thực chạy, lưu báo cáo ở artifacts. Ghi bài học mới nếu có lỗi thực tế, tránh thêm quy tắc từ rủi ro tưởng tượng.
