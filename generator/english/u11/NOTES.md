# Unit 11 - Family time

Nguồn: SGK Tiếng Anh 5 Global Success, sách học sinh tập hai, trang in 6-11; Wordlist 74-75. Đã xem đủ sáu trang bài học và Wordlist trực tiếp từ bản scan 79 trang PDF, ngày 18/11/2026. File, SHA256 và quy tắc trang được ghi trong kế hoạch tập hai ở docs/breakdowns. Không đưa sách/scan vào repo.

## Phạm vi

- Lesson 1 (6-7): Did you + nguyên mẫu? Yes, I did./No, I didn't.; swim/swam, take photos/took photos, collect seashells/collected seashells, walk on the beach/walked on the beach; with my mother/father/brother/family.
- Lesson 2 (8-9): What did your family do in/there...?; When did...go...?; took a boat trip around the bay, ate seafood, saw some interesting places, bought souvenirs. Thời gian last weekend, last summer, yesterday; địa danh Ha Long, Nha Trang, Sydney, Singapore và các nơi khác xuất hiện trong trang bài học.
- Lesson 3 (10-11): nhịp/trọng âm câu hỏi, đọc chuyến đi theo ngày và hoạt động, viết theo thẻ, nhật ký ảnh. Không dùng bài hát/đoạn đọc nguyên bản.

## Quyết định nội dung

- Sáu hồ sơ chuyến đi tự soạn. Cùng nơi có thể khác người, ngày hoặc hoạt động; không dùng liên tưởng địa danh thay đọc hiểu.
- Sáu đề x 24 câu/100 điểm; 10/8/6 theo ba cấp, sáu nghe (hai/cấp). Nghe Giỏi tách thông tin Saturday/Sunday và hai trường dữ liệu; không tăng độ khó chỉ bằng tăng tốc độ.
- Các câu viết chấm tự động yêu cầu rõ điểm bắt đầu, thứ tự hoặc cụm cần điền; không quảng cáo đó là chấm mọi cách diễn đạt tự do. Dạng full form không nhận viết tắt; câu không bắt buộc full form chấp nhận didn't và dấu nháy cong.
- 16 từ/cụm, ba nhóm (4/4/8), sáu hội thoại, 12 bài luyện (4/nhóm), tiến độ học riêng. Đánh vần là tên chữ cái; đọc từ/cụm là cách nói tự nhiên.
- Bốn tranh hoạt động mới theo style đã duyệt, không giả làm ảnh địa danh. Prompt và đường dẫn ảnh gốc ở images/PROMPTS.md.

## Âm thanh thử nghiệm trên Unit 11

- 91 file WAV PCM mono 22050 Hz, tạo từ lời tự soạn bằng Microsoft Zira Desktop (en-US), rate -1. Là giọng tổng hợp, chưa được người dùng duyệt bằng tai.
- Alphabet dùng SayAs.SpellOut để phát tên chữ cái, không đọc A như mạo từ. Cả lời nghe, từ, ví dụ, hội thoại/A-only và ABC đều có file.
- Trang ưu tiên âm thanh kèm bài; có thể chọn giọng thiết bị nếu trình duyệt cung cấp. Không yêu cầu Speech API hoặc gói giọng trên máy học sinh để dùng file nghe.
- Nghe chậm phát ở 0.8 lần, giữ cao độ nếu trình duyệt hỗ trợ. Không tự phát; dừng/hủy khi đổi nhóm, đổi giọng, ẩn hoặc rời trang. Lỗi file/mạng có thể thử lại hoặc đọc lời thay thế.
- Manifest khai báo chính xác text/file. Build thường/CI dùng WAV đã lưu, không tạo lại giọng và không cần Windows. Web trích file tương đối; standalone nhúng WAV.
- Tạo lại có chủ đích: từ generator chạy `python -m english.u11.audio_source`, rồi từ root chạy `powershell -File tools/generate_english_audio.ps1 -Unit u11 -Force`. Yêu cầu Windows và giọng Zira Desktop trên máy tác giả. Không dùng quy trình này để cài gì lên máy bé.
- Không sao chép audio sách; không thu âm, nhận dạng hoặc chấm nói. Kết quả kiểm tra tự động không thay thế nghe duyệt, kiểm trên máy bé hoặc nhận xét độ khó của học sinh.

## Định danh và hồi quy

ID đề: en-u11-de1-v1 đến en-u11-de6-v1. Key học: mia5:learn:en-u11-v1. Giữ nguyên r01/r02 và mọi ID/đáp án cũ. QA device-voice mô phỏng được chạy riêng với QA phát file thực khi không có Speech API.
