# Mẫu học từ và phát âm — Unit 6

## Phạm vi được giao

Mẫu trước khi mở rộng. Bốn phòng học, hai hội thoại và ba bài thực hành trên một trang riêng; liên kết từ tổng quan. Giữ nội dung/ID của 78 đề, không thêm cơ chế chấm nói hoặc thay các trang tổng quan khác. Nguồn study.py/html/css/js trong english/u06; build sinh web có tài nguyên dùng chung và standalone tự chứa.

## Quyết định dạy học

Nghe từ/cụm luyện cách nói; ABC đọc tên chữ cái để nhớ cách viết, không gọi đó là phonics. Đánh vần từng chữ bằng utterance riêng, tách từ trong cụm và highlight theo onstart, không nhét nguyên chuỗi vào TTS. Mẹo computer nhấn âm thứ hai, không bắt bé đọc IPA hoặc dùng phiên âm Việt. Hai hội thoại nghe trước, sau đó chỉ nghe A để bé tự đáp; không ghi âm/chấm đúng sai. Ba bài thực hành nhận phản hồi và được làm lại, không áp lực thời gian.

Đã luyện/Cần ôn là lựa chọn tự đánh dấu, không khẳng định năng lực phát âm. Khóa riêng có schema và danh sách từ cho phép, lưu ngay sau bấm và báo lỗi storage. Ba bài luyện không lưu thành điểm đề. Âm thanh chỉ bắt đầu khi bấm, một chuỗi tại một thời điểm; dừng cả chuỗi khi đổi nút/giọng/ẩn trang, bỏ callback muộn. Player nổi để không phải cuộn về đầu tìm nút Dừng.

## Kiểm chứng và bài học

Bộ QA riêng mô phỏng speech để kiểm tra logic và UI, dùng hồ sơ riêng thật trên đĩa để đóng/mở. Edge thật phát xong 4 cụm và 12 chữ computer room (David en-US) không lỗi; sự kiện API không chứng minh phát âm đã được nghe duyệt. Người dùng chọn giọng có sẵn trên thiết bị và nghe thử trước khi quyết định triển khai hàng loạt.

Chạy QA tải nhiều tài nguyên lộ lỗi local ERR_CONNECTION_REFUSED. Server Python mặc định backlog 5, đã tăng lên 128 và chuyển log server sang artifact khi chạy cổng thử 8766. Các lượt lỗi không tính PASS, không bỏ assertion hoặc thêm retry che lỗi. Kết quả cuối local/CI/live cập nhật trong docs/01_TINH_TRANG.md. Đợi người dùng duyệt mẫu trước khi mở rộng Unit 1–7.
