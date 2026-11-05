# Unit 10, Review 1 và Review 2

## Phạm vi đã giao và nguồn sách

Ngày 06/11/2026, chủ repo yêu cầu tiếp ba phần còn lại. Triển khai Unit 10, Review 1, Review 2; Starter để sau. Không tự thêm Unit 11/12, không triển khai học kỳ II hoặc đề thi học kỳ riêng từ kế hoạch chưa duyệt.

Đã render và xem trực tiếp đủ trang in 40–43 và 68–77 trong PDF tập một của chủ repo: Review 1 (40–41) +mở rộng (42–43), Unit 10 (68–73), Review 2 (74–75) +mở rộng (76–77). PDF/scan giữ ngoài repo, tại tai_lieu/sach và luu_tru/english-u10-reviews-review. NOTES cạnh từng nguồn ghi lại ý/từ khóa, không chép bài đọc sách.

## Sản phẩm và nội dung

| Phần | Nội dung | Đề/câu/nghe | Học từ/hội thoại/luyện |
| --- | --- | --- | --- |
| Unit 10 | Did/go/went, nơi đến, việc đã làm, tháng | 6/144/36 | 16/6/12 |
| Review 1 | Ôn tổng hợp Units 1–5, nghề và nơi làm việc | 6/144/36 | 14/6/12 |
| Review 2 | Ôn Units 6–10, tách hai chuyến đi, thứ tự sự kiện | 6/144/36 | 14/6/12 |

Mỗi đề giữ 24 câu/100 điểm, 10/8/6 và nghe hai mỗi cấp. Giỏi kết hợp dữ kiện, không tăng tốc đọc. Bài Review tự soạn từ hồ sơ/đoạn đọc/lời nghe mới, không dùng lại nguyên đề Unit. Gắn `sourceUnits` cho câu Review, audit bắt buộc từng đề phủ đúng 1–5 hoặc 6–10. Bài viết có nhiều cách nói hợp lệ được nhận biến thể; full form không nhận viết tắt. Viết mở trong tổng quan là gợi ý để người lớn xem, không chấm bằng một đáp án duy nhất.

Review 1 dùng địa chỉ giả định, không đoán quốc tịch từ mặt hoặc nghề từ giới tính. Review 2 tách Yesterday/School trip và tháng để trẻ phân biệt hai chuyến đi. Thứ tự sự kiện có câu đọc First/Then/Finally; loại holiday đọc theo thẻ vì nhiều hoạt động có thể thuộc nhiều loại.

## Registry và tương thích

- `UNITS` chỉ giữ mười Unit thật; `REVIEWS` tách r01/r02. `TOPICS` xếp U1–5, Review 1, U6–10, Review 2.
- Catalog thêm kind/topic/overview, không đổi ID cũ. Runner mới nhận `--topics=u10,r01,r02`, đồng thời giữ `--units` cũ.
- Web: `Unit10_OurSchoolTrip/`, `Review1_Units1_5/`, `Review2_Units6_10/`. Review dùng `TongQuan_Review1/2.html`, badge Review 1/2; không tạo Unit R1/R2 trong UI hoặc URL tổng quan.
- ID mới en-u10-deN-v1, en-r01-deN-v1, en-r02-deN-v1; key học tương ứng mia5:learn:en-u10/r01/r02-v1. Dùng chung controller lưu bài/âm thanh, giữ điểm/nháp cũ và cơ chế kế thừa mẫu Unit 6.
- Tham số label/overview cho renderer học từ để Review không có nhãn/link Unit giả. Demo giọng mặc định nói lời chào học Anh chung khi không phải Unit 6/7.
- Màu thẻ môn Anh lấy thứ tự TOPICS để chèn Review không làm lệch CSS theo vị trí. Mốc bậc thang theo 72 đề: 1/18/36/54/72, thay mapping một lượt.

## Tranh và tài nguyên

Bốn tranh Unit 10 tạo bằng built-in ImageGen, mỗi tranh một call: visit the old buildings, plant trees, play games, walk around the lake. Cảnh chung không giả làm địa danh thật; địa điểm lấy tên/thẻ đúng SGK. Nguồn WebP 768×512 tại `generator/english/u10/images/`; prompt đầy đủ và tên PNG gốc tại `PROMPTS.md`. PNG gốc giữ nguyên ngoài repo ở `C:/Users/leduc/.codex/generated_images/01a18754-246d-7f70-96a6-4561091d0511/`.

Hai Review tái dùng tranh được duyệt của các Unit. Audit khai báo whitelist nguồn ảnh riêng của Review, không bỏ kiểm tra data URI hoặc đưa scan sách vào output. Trang học từ được dùng lại tranh phù hợp; không gắn tranh một vật cho từ số nhiều không tương ứng.

## Kiểm chứng local

- Audit 36 Toán +72 Anh/1728 vị trí câu Anh, không lỗi. Kiểm tra 1208 liên kết tĩnh đạt trước lần bổ sung một câu đọc thứ tự sự kiện.
- QA toàn site: 108/108 đề 100/100, 142 HTML không lỗi browser; theme 142 trang và responsive 2272 trường hợp. Sau thêm câu thứ tự sự kiện, chạy lại audit và 18 đề mới, vẫn đạt. CI sẽ kiểm lại toàn bộ bản cuối.
- `qa_english_units.js --topics=u10,r01,r02`: đủ 18 đề/108 nghe, transcript khớp, nháp/tên/hỗ trợ, best/điểm phần/reset, ba standalone có ảnh và 40 trường hợp trang mới/trang chủ. Trạng thái Review và badge đúng; không mang nhãn Unit R.
- `qa_persistence.js --topics=...`: đóng/mở hồ sơ browser thật, giữ câu đã làm, xem lại bài nộp, best/last, Back/cross-tab, không tăng lượt khi xem lại.
- `qa_study.js`: đủ 162 từ/chuỗi ABC, 67 hội thoại, 132 bài luyện và 264 layout/theme, lưu sau browser restart, signature, dấu mẫu cũ, tách dữ liệu, thiếu giọng/storage bị chặn. Speech mô phỏng.
- Edge native thử từ và chuỗi ABC ở cả ba trang, start/end không lỗi. Chưa nghe duyệt bằng tai, đặc biệt địa danh Việt; chưa có phản hồi độ khó từ học sinh.
- Đã xem bằng mắt bốn tranh mới ở kích thước câu hỏi và ba poster PNG cuối. Báo cáo artifacts/topics-u10-r01-r02-local, study-full-local, persistence-local, final-three-local; không đưa artifacts lên Git.

## Bài học

- Review là loại nội dung thật trong sách, không giả thành Unit 11/12 chỉ để vừa pipeline số.
- Đổi cấu trúc registry phải cập nhật catalog, lookup tổng quan, badge, màu theo vị trí, QA, reset và key. Không dựa suy đoán URL từ một số Unit cho mọi loại bài.
- Bài viết/đọc vẫn cần nhiều dạng tương tác phù hợp; audit phát hiện ít dạng thì bổ sung sắp câu/chọn/đúng sai có ý nghĩa, không hạ kiểm tra.
- Các cặp nối cần vế phải khác nhau. Hồ sơ có cùng sở thích hoặc cùng nơi đi phải ghép thêm thời gian hoặc thông tin phân biệt, tránh hai đáp án giống nhau trong ô nối.
- Browser Playwright đã cài phải khớp package-lock. Bản runtime hiện yêu cầu Chromium 1248; tải đúng bằng CLI của dependency đang dùng, không đổi lock hoặc dùng browser lạ để bỏ qua kiểm tra.

## Phần chưa làm

Starter là mục duy nhất chưa triển khai trong tập một. Chưa làm bộ đề giữa/cuối kỳ riêng, chưa có tập hai để soạn phần học kỳ II, chưa có chấm nói hoặc đồng bộ tài khoản. Lưu tiến độ vẫn theo thiết bị/trình duyệt/origin.

## Kiểm chứng sau xuất bản

Đã xuất bản commit `5bba2eb`; [Actions/Pages đạt](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/42103227242). CI kiểm toàn bộ bản cuối: 108 đề/142 HTML, 2272 trường hợp responsive, nghe/nháp/tiến độ/Review/học từ. Trên Pages thật, qa_english_units --topics=u10,r01,r02 đạt 18/18 đề 100/100, đủ 108 nghe, giữ nháp/best, chấm phần/reset cách ly, thứ tự thẻ đúng U1–5/R1/U6–10/R2 và nhãn Review. qa_persistence --topics=... đạt đóng/mở browser, xem lại bài nộp, best/last, Back/cross-tab. qa_study live đạt cả 11 trang: 162 chuỗi ABC, 67 hội thoại, 132 bài luyện, lưu sau browser restart và 264 layout/theme, gồm tương thích mẫu Unit 6. Speech trong runner là mô phỏng.

34 tài nguyên live (24 HTML mới, bốn WebP, ba trang chủ/môn, catalog, home.js và study.js) khớp byte bản nguồn; không so byte PNG giữa Windows/Linux. Edge native local: 26 start/end, không error, chỉ chứng minh phát xong; chưa nghe duyệt phát âm bằng tai hay có đánh giá độ khó của học sinh. Báo cáo: artifacts/topics-u10-r01-r02-online/report.json, final-three-online/assets.json, study-full-online/report.json và persistence-online.
