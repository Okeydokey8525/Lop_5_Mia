# Review 3 · Units 11–15

## Nguồn đã đọc ngày 20/11/2026

Global Success 5, tập hai; trang in 36–39, PDF 38–41. Đã mở riêng đủ bốn trang, không chỉ thumbnail. PDF ngoài repo: `C:\LeDucLuong\Mia\tai_lieu\sach\05-sgk-tieng-anh-5-global-success-tap-hai_268202616.pdf`; SHA256 `65e57b1193689e5a66f0ad9ce754388c6332d772c7d892c8f7b40660072713f9`. Bản render ngoài repo ở `luu_tru/english-volume2-planning/reviews-38.png` đến `reviews-41.png`.

- Trang 36: nghe chọn lời đáp và hỏi đáp tổng hợp chuyến đi, Tết, ngày đặc biệt, thói quen.
- Trang 37: nối câu; đọc kế hoạch ngày lễ; viết khoảng 40 từ về Trung thu đã qua. Giữ phân biệt did / will / does / should.
- Extension 38–39: dairy, grains, protein, fruit and vegetables; phân nhóm từ thực phẩm và nói/viết bữa sáng. Nội dung này ghi riêng trong tổng quan, nhóm học từ và một câu đề từ vựng.

## Nội dung tự soạn

Sáu đề × 24 câu/100 điểm, phân cấp 10/8/6; sáu nghe mỗi đề, hai mỗi mức. Mỗi đề khai báo đủ `sourceUnits` 11–15, mỗi câu có nguồn kỹ năng. Không sao chép bài đọc, lời nghe, tranh hoặc bản scan sách. Sáu hồ sơ giả định; quá khứ, việc và nơi đến dịp Tết, hoạt động ngày đặc biệt, đồ ăn/đồ uống, thói quen/tần suất và lời thoại sức khỏe tách trường dữ liệu. Where will…go hỏi nơi; What will…do hỏi hoạt động, khác What food/drinks…have. Các hồ sơ cùng việc đã qua vẫn có thể khác nơi đến/kế hoạch mới.

Lời khuyên lấy đúng dòng role-play, không suy triệu chứng thành một đáp án chữa bệnh. Viết tự chấm chỉ yêu cầu câu theo thẻ và mở đầu/thứ tự rõ. Bài Trung thu khoảng 40 từ/bữa sáng là luyện mở với người thân, chưa chấm bài luận hoặc nói.

Học từ: 18 từ-cụm, sáu hội thoại, 12 bài luyện, ba nhóm × bốn bài; lưu riêng `mia5:learn:en-r03-v1`. Đề `en-r03-deN-v1`, không đổi ID cũ. Nghe thường/chậm, ABC tên chữ cái, dừng/đổi nhóm/thử lại; file WAV Anh Mỹ giọng máy, không cần cài voice trên máy bé. Tạo audio bằng `python -m english.r03.audio_source` (PYTHONPATH=generator), rồi `powershell -File tools/generate_english_audio.ps1 -Unit r03`.

## Tranh tái dùng có chủ đích

Không tạo tranh mới: `u11/images/take-photos.webp`, `u12/images/decorate-the-house.webp`, `u13/images/pizza.webp`, `u14/images/do-morning-exercise.webp`. Nguồn/prompt ở thư mục Unit tương ứng. Dùng trong câu hỏi tranh, reader, poster và học từ. Audit chỉ chấp nhận đúng bốn ảnh này; không đổi hay sao chép sang thư mục Review. Kiểm tra render cuối ở artifacts/reviews34-local và topics-r03-r04-local.

## Bài học kỹ thuật

Review có audio cần build trích asset theo cả `ReviewN_…` và `UnitN_…`, không ghép cứng `uN`. QA phải chọn được R3/R4 và đối chiếu phạm vi riêng, không mặc định mọi Review sau R1 là Units 6–10. Giữ gate đủ kiểu câu (ít nhất bốn), nghe ba mức và toàn bộ clip; bài đọc cần câu chọn, đúng/sai, điền và nghe, không chỉ toàn câu điền.

Xem trạng thái local/CI/live và giới hạn iPad/nghe bằng tai ở `docs/breakdowns/2026-11-20_REVIEW3_REVIEW4.md`.
