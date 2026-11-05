# Mở rộng học từ/phát âm đầy đủ Units 6–7

## Phạm vi và nội dung

Người dùng duyệt mẫu Unit 6 rồi giao làm đầy đủ Unit 6 và triển khai Unit 7. Giữ phần học đi kèm tổng quan, không đổi 78 đề chính thức. Unit 6 có 14 từ/cụm (4 phòng, 4 tầng, 6 chỉ dẫn), 7 hội thoại và 12 bài luyện. Unit 7 có 12 từ/cụm (4 nguyên mẫu, 4 dạng V-ing, 4 lý do), 6 hội thoại và 12 bài luyện. Đối chiếu lại trang sách đã render 46 và 53; NOTES cũ ghi phạm vi đủ 44–55. Các trường hợp phủ định và because theo đúng nội dung Unit 7, không gán một lý do cố định cho hoạt động.

## Nguồn và thiết kế

Dữ kiện ở `english/u06/study.py`, `english/u07/study.py`; renderer, template và CSS/JS chung ở `english/study/`. Tái dùng tranh đã duyệt. Sơ đồ tầng/xuống/lên/trái/phải dùng SVG có kiểm soát; ground ở dưới cùng, first ngay trên ground. Chia ba nhóm mỗi Unit, chỉ hiện nhóm đang chọn để trang điện thoại không kéo dài hàng chục thẻ. Có xem riêng các từ cần ôn. Giọng đọc gói trong phần cài đặt thu gọn; player Dừng luôn chạm được khi đang phát.

## Bảo toàn và lưu bài

Unit 6 dùng key đầy đủ `mia5:learn:en-u06-v1`, kế thừa bốn dấu cũ từ `mia5:learn:en-u06-preview-v1` khi key mới chưa có. Không ghi đè key cũ. Bắt buộc tách vì một tab mẫu cũ còn mở chỉ biết schema words bốn từ, có thể xóa dữ liệu practice và từ mở rộng nếu dùng chung key. QA mô phỏng việc tab cũ ghi lại và chứng minh key đầy đủ giữ nguyên. Unit 7 dùng key riêng. Schema 1 mở rộng thêm practice/group, tương thích blob cũ chỉ có words. URL mẫu cũ sinh cùng nội dung với URL đầy đủ, nên bookmark vẫn dùng được. Không tự ghi đã thuộc từ việc nghe; tự đánh dấu và kết quả bài luyện tách khỏi điểm đề.

Bài luyện lưu giá trị và đã kiểm tra, debounce 250ms và flush khi ẩn/rời trang; đóng browser rồi mở lại cùng hồ sơ khôi phục câu đang gõ và phản hồi. Mỗi câu có signature theo dữ kiện chấm/prompt để bài đổi không giữ dấu đúng cũ. Chỉnh câu trả lời phải bỏ trạng thái đã kiểm tra cho tới khi bấm kiểm tra lại. Đọc kho lưu có schema, giới hạn độ dài, enum, whitelist từ/câu và lựa chọn hợp lệ. Thiếu giọng/storage bị chặn vẫn dùng phần chữ và báo rõ.

## Kiểm chứng

`qa_study.js`: mọi chuỗi ABC/giọng đọc ví dụ, 13 hội thoại, 24 bài đúng/sai, không tự nhận thuộc, lọc cần ôn, kế thừa mẫu, URL mẫu, đóng/mở browser, flush ngay trước debounce, signature, tách Unit/điểm/nháp, thiếu giọng, storage bị chặn, standalone và 48 layout/theme. Wrapper tên cũ gọi bộ mới; CI dùng tên chính thức. Speech trong QA là mô phỏng, không chứng minh chất lượng phát âm.

Native Edge thật: 6 cụm từ ở 6 nhóm và 2 chuỗi ABC (turn left, doing projects), 27 utterance có start/end, không error, giọng David en-US. Chưa nghe đánh giá bằng tai hoặc có phản hồi làm thử của học sinh. Local toàn bộ 78 đề/98 HTML, 776 link, theme 98 trang và responsive 1568 trường hợp đạt; CI/Pages đã đạt ở commit ed48e0c; `qa_study.js` live đạt cả hai Unit, gồm khôi phục sau đóng/mở và không bị tab mẫu cũ ghi đè. Chi tiết và liên kết ở docs/01_TINH_TRANG.md.

## Bài học và việc sau

- Tách dữ kiện bài học khỏi cơ chế chung khi mở rộng; không sao chép controller theo từng Unit.
- Tôn trọng dữ liệu người dùng đã thử mẫu: giữ URL, chuyển dấu sang key đầy đủ có whitelist, không đổi tên key cho đẹp rồi mất dấu.
- Giữ cả câu đang gõ, không chỉ đánh dấu từ; có signature và ca đóng/mở thật.
- Thêm âm thanh không đồng nghĩa học hiệu quả: giữ bước thử nhớ, phản hồi sửa và tự chọn cần ôn.
- Chưa tự mở rộng Units 1–5 hoặc 8–10, chưa làm ghi âm/chấm nói.
