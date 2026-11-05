# 01 — Tình trạng hiện hành

Cập nhật 06/11/2026. Bản lịch sử trước khi gom tài liệu nằm trong `history/`; không dùng những số liệu cũ làm trạng thái hiện tại.

## Đã bàn giao

- Website: https://okeydokey8525.github.io/Lop_5_Mia/ — GitHub Pages qua Actions.
- Toán 5 tập một: 6 chủ đề, 36 đề, mỗi đề 24 câu/100 điểm; ID `cd{n}-de{i}` giữ nguyên.
- Tiếng Anh 5 tập một: Unit 1–10 và Review 1–2, đặt đúng thứ tự sách. Có 12 tổng quan HTML/PNG +72 đề (1728 câu); mỗi đề 24 câu/100 điểm và sáu nghe (hai mỗi cấp). Units 2–10 và hai Review có học từ/phát âm tự lưu; Unit 1 có mẫu nghe. Chưa chấm nói.
- Toàn site: 108 đề chính thức, 142 HTML, 18 tổng quan HTML/PNG. Danh sách đề có nguồn chính là `site/catalog.json`.
- Giao diện hồng anh đào, tối màu tím mận; reader trên màn hình ≤820px, poster để xem/in. Tiến độ theo origin/trình duyệt, không đồng bộ thiết bị.
- Chủ repo đã xem Unit 1, phản hồi hình khó nhận diện và duyệt mẫu cá heo. Ngày 30/10 đã áp dụng phong cách mới cho đủ 6 tranh ở tổng quan/câu hỏi, giữ nguyên 144 câu và đáp án. Sau đó chủ repo giao Unit 2–3, Unit 4–5 rồi Unit 6–7; đã bổ sung Unit 8–9 theo yêu cầu tiếp theo. đã tiếp tục giao Unit 10, Review 1 và Review 2 ngày 06/11. Chỉ còn Starter trong tập một; chưa triển khai tập hai.

| CĐ Toán | Thư mục | Nội dung | Bài |
|---|---|---|---|
| 1 | `ChuDe1_OnTapVaBoSung` | Ôn tập và bổ sung | 1–9 |
| 2 | `ChuDe2_SoThapPhan` | Số thập phân | 10–14 |
| 3 | `ChuDe3_DonViDoDienTich` | Đơn vị đo diện tích | 15–18 |
| 4 | `ChuDe4_PhepTinhSoThapPhan` | Các phép tính với số thập phân | 19–24 |
| 5 | `ChuDe5_HinhPhangChuViDienTich` | Một số hình phẳng, chu vi và diện tích | 25–29 |
| 6 | `ChuDe6_OnTapHocKi1` | Ôn tập học kì 1 | 30–35 |

## Unit 4–5 — kiểm chứng hiện hành

Thêm Unit 4 Our free-time activities và Unit 5 My future job: 12 đề/288 câu, trong đó 72 nghe, hai tổng quan HTML/PNG và tám tranh tự tạo. Đã xem đủ trang sách 28–39; NOTES trong u04/u05, quyết định/bài học ở `breakdowns/2026-10-30_UNIT4_UNIT5.md`. ID mới en-u04-deN-v1 và en-u05-deN-v1; Unit 1–3 và Toán không đổi.

Local audit đủ 66 đề, 0 lỗi; tự làm đúng 66/66 đề 100/100, 81 HTML không lỗi trình duyệt; 602 tham chiếu tĩnh đúng hoa/thường. Responsive 1296 trường hợp; runner riêng kiểm tra 12 đề mới, 72 nghe, nháp/điểm phần/reset, biến thể would/I’d và full form, 32 trường hợp trang mới/chọn môn, hai standalone có ảnh.

Đã xuất bản commit `56a179e`; [Actions build/deploy đạt](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/41079470268), gồm 66 đề và 1296 trường hợp responsive trên Linux. Trên Pages thật, `qa_english_units.js --units=4,5` đã kiểm tra đủ 12/12 đề 100/100, lưu điểm sau tải lại, 72 câu nghe (speech mô phỏng), nháp/tên/hỗ trợ, điểm phần, thống kê 5 Unit và reset cách ly; 32 trường hợp trang mới/chọn môn. Tám ảnh live khớp byte nguồn. Báo cáo ở artifacts/units45-online/report.json và asset-report.json. Lần này chỉ kiểm chứng trực tiếp 12 đề mới trên live; toàn bộ 66 đề đã kiểm tra local và CI. Chưa đánh giá phát âm bằng tai hoặc độ khó bởi học sinh.

## Unit 2–3 — bằng chứng trước khi thêm Unit 4–5

Đã thêm 12 đề/288 câu, 72 câu nghe và 8 tranh tự tạo; xem `breakdowns/2026-10-30_UNIT2_UNIT3.md`. Local audit 54 đề không lỗi; tự làm đúng 54/54 đề đạt 100/100, 67 HTML; responsive 1072 trường hợp. Kiểm tra thêm hai tổng quan/trang môn/trang chủ sau chỉnh lưới: 32 trường hợp. Kiểm tra 486 tham chiếu tĩnh đúng hoa/thường, 0 lỗi. Luồng nghe, nháp, điểm phần, reset và hai bản standalone mới đạt. Phát âm/độ khó chưa được học sinh đánh giá.

Đã xuất bản commit `5c8e225`; [Actions build/deploy đạt](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/41037419914), gồm hồi quy 54 đề và 1072 trường hợp responsive trên Linux. Trên địa chỉ Pages thật, `qa_english_units23.js` đã đạt: đủ 12 đề mới/72 câu nghe, lời đọc đúng câu (speech mô phỏng), nháp/điểm giữ sau tải lại, chấm phần, tổng tiến độ và reset cách ly; 32 trường hợp trang mới/chọn môn ở sáng/tối. Tám ảnh live khớp byte nguồn. Báo cáo: artifacts/units23-online/report.json và asset-report.json. Không coi kiểm tra tự động này là học sinh đã nghe/đánh giá độ khó.

Lượt kiểm tra toàn site live đầu tiên bị ngắt vì một phản hồi 503 khi tải CSS; tài nguyên kiểm tra lại ba lần đều 200. Sau khi thêm retry giới hạn cho lỗi máy chủ tạm thời vào công cụ kiểm tra, lượt chạy lại toàn bộ đã đạt 54/54 đề 100/100, 67 HTML, không lỗi trình duyệt; thống kê sau tải lại, câu sai/điểm phần và reset riêng từng môn đạt. Báo cáo hoàn chỉnh: artifacts/online/report.json.

## Bằng chứng lịch sử trước Unit 2–3

Mã thay tranh `4798597`; [workflow build và deploy đạt](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/40976976768).

- Local và CI: audit 36 Toán + 6 Anh không lỗi; làm đúng theo đáp án khai báo 42/42 đề đạt 100/100; 832 tổ hợp responsive (52 trang × 8 chiều rộng × 2 theme). Local kiểm tra 251 tham chiếu tĩnh, 0 lỗi; 6 đề Anh standalone đạt.
- Live sau sửa tranh: 6 ảnh khớp byte với nguồn; 7 trang Unit 1 × 3 chiều rộng × 2 theme = 42 trường hợp, đủ ảnh, đúng tỷ lệ, không tràn ngang/lỗi trình duyệt. Báo cáo: `artifacts/online/artwork-live-report.json`.
- Lần kiểm tra toàn bộ live trước đó, 29/10/2026 20:08:05 UTC+7: 42/42 đề đạt, 832 tổ hợp responsive; kiểm tra biến thể chữ, câu sai, điểm phần, hồ sơ, reset riêng từng môn đạt. Báo cáo trong artifacts không phải nguồn nội dung.
- Chưa có dữ liệu em gái làm bài; mô phỏng Chromium chưa thay thế thử thiết bị thật, và tự điền đúng không phải giải độc lập toàn bộ đáp án.

## Nguồn và việc tiếp theo

Nguồn Anh: `generator/english/u01/content.py`, `NOTES.md`, `images/`. Nguồn sách ở thư mục ngoài repo `../tai_lieu/sach/`. Mở [08](08_CAY_THU_MUC_VA_DEPLOY.md) để tìm cây và lệnh; mở [bản đồ tài liệu](README.md) để tiếp nhận.

Chỉ tiếp tục Starter/Unit/Review khác khi chủ repo giao. Pipeline Anh hiện còn chỗ đăng ký riêng u01, cần tổng quát hóa khi mở rộng; xem [phân rã công việc](breakdowns/KE_HOACH_TIEP_THEO.md).

## Đầu vào còn thiếu

- Toán học kì 2: chưa có PDF, danh sách chủ đề/bài/số trang; chưa làm chủ đề 7–8.
- Tiếng Anh 5 tập hai: chưa có sách.
- Phản hồi học sinh về mức độ khó và câu chưa rõ: chưa có.

## Mẫu nghe ba cấp — 30/10/2026

Theo yêu cầu xem mẫu trước, bổ sung `TiengAnh5/Unit1_AllAboutMe/LuyenNghe_Mau.html`, liên kết từ trang chủ Anh. 6 câu: 2 Trung bình (tên/nơi sống), 2 Khá (môn thể thao/màu), 2 Giỏi (đoạn 4 câu, tìm 2 thông tin). Chấm 8 ý trong 6 câu, không tính điểm/sao đề chính thức và không ghi localStorage.

Có chọn giọng tiếng Anh, thử giọng, nghe bình thường/chậm, dừng, xem lời nghe/nghĩa, kiểm tra từng câu/cả mẫu, làm lại. Nguồn: `generator/english/u01/listening.py` và `listening.html`; lời nghe và đáp án sinh từ cùng dữ kiện. Chỉ dùng giọng thiết bị, không dùng audio SGK hoặc tạo file thu âm. Phụ thuộc giọng cài sẵn/dịch vụ của trình duyệt; bản HTML tự chứa không bảo đảm phát offline trên mọi máy.

QA chuyên biệt mô phỏng speech để kiểm tra điều khiển, lỗi, giọng đến trễ, timeout, chấm sai/thiếu/đúng và reset. Microsoft Edge trên máy hiện tại đã phát sinh sự kiện bắt đầu/kết thúc với Microsoft Zira en-US; đây không phải đánh giá phát âm bằng tai. Cần chủ repo nghe cả ba cấp trên thiết bị dùng thật trước khi triển khai hàng loạt. Tổng responsive hiện 53×8×2 = 848 trường hợp; các bằng chứng 832 ở trên là lịch sử trước mẫu nghe.

## Unit 1 có nghe và hồng sáng — đợt triển khai đã được duyệt

Chủ repo duyệt mẫu ba cấp và yêu cầu áp dụng cho Unit 1, đồng thời duyệt bảng hồng sáng. Mỗi đề hiện 24 câu = 10 TB/8 Khá/6 Giỏi, 100 điểm; thay 6 câu (vị trí 1/2, 11/14, 21/24) bằng 2 câu nghe mỗi cấp. Cộng 36 câu nghe trong 6 đề. Nội dung nghe/đáp án sinh từ cùng dữ kiện trong exam_listening.py. Không tự triển khai unit khác.

ID lưu điểm mới `en-u01-de1-v2` đến `en-u01-de6-v2`; điểm cũ không nhập vào thống kê mới và không bị reset khi xóa tiến độ bộ mới. Kết quả lưu phiên bản và các câu đã dùng hỗ trợ xem lời nghe; không trừ điểm vì nghe lại/chậm/xem chữ. Sau nộp tự mở lời nghe, vẫn nghe lại được.

Theme Tiếng Anh dùng chung theme.css/js ở generator/english, mặc định hồng sáng ngay cả khi OS tối; nút Sáng/Tối lưu lựa chọn riêng. Áp dụng trang chủ Anh, tổng quan/reader/PNG, sáu đề và mẫu. Màu và khóa tiến độ Toán giữ nguyên. QA chuyên biệt: tools/qa_english_unit1.js. Các mục mẫu/thống kê trước đây là lịch sử của giai đoạn trước tích hợp.

## Hồng sáng và Sáng/Tối toàn site

Theo yêu cầu tiếp theo của chủ repo, đã mở rộng theme sang trang chủ chung và toàn bộ Toán, không chỉ Anh. Cả 53 trang dùng một nguồn theme và khóa mia5:ui-theme; dữ liệu điểm không đổi. Giữ lựa chọn chủ động trước đây ở Anh khi chưa có lựa chọn chung. Cập nhật build cả standalone và bảy PNG; thêm qa_theme.js và kiểm tra responsive theo theme thực. Những mục trên ghi màu chỉ áp dụng Anh là lịch sử của giai đoạn trước yêu cầu này.

## Trang chủ chọn môn có phản hồi động viên

Đã thực hiện đúng bốn phần chủ repo duyệt: lời chào và hình sách/ngôi sao cả trên điện thoại, thẻ môn phản hồi nhẹ, thanh tiến độ/sao thật, động viên một lần khi quay lại sau lượt luyện tập mới. Giữ phạm vi chỉ trang chọn môn; không thêm hiệu ứng vào đề hoặc trang tổng quan. Tên lấy từ tên đã lưu hoặc Mia; không thêm tài khoản. Có hỗ trợ giảm chuyển động; không đổi nội dung, điểm hay ID đề. Nguồn và cơ chế mốc chúc mừng trong docs02, kiểm tra trong docs07.

## Sau kiểm tra chéo: sửa chấm phân số, đồng hồ và lưu nháp

Đã sửa hai lỗi tái hiện trên website: nhập 3.9 hoặc 3abc ở tử không còn được hiểu thành 3; thao tác sắp xếp số/từ khởi động đồng hồ trước khi dựng lại nút. So sánh phân số/hỗn số bằng số nguyên chính xác sau kiểm tra chuỗi và giới hạn số nguyên an toàn.

Đã thêm nháp cho toàn bộ 42 đề: các ô, lựa chọn, thứ tự số/từ, tên, thời gian và hỗ trợ nghe. Rời/tải lại trang rồi mở đúng đề sẽ khôi phục; đồng hồ chỉ chạy lại sau tương tác, không cộng thời gian đóng/ẩn trang. Nút Bỏ bản nháp có xác nhận, không xóa điểm đã nộp. Trang môn hiển thị Đang làm dở và ưu tiên nút Tiếp tục bài đang làm cho nháp mới nhất. Nháp không tính là đề đã hoàn thành. Sau nộp thành công xóa nháp, điểm/sao vẫn lưu như trước. Không có đồng bộ thiết bị; khi storage bị chặn báo không lưu được.

Nguồn engine.js/css và gen_index.py; QA hồi quy tools/qa_drafts.js. Nội dung/đáp án đề và ID kết quả giữ nguyên.


## Cải thiện nhận biết bài đã lưu (2026-11-05)

Đã sửa nguồn: danh sách môn cập nhật khi trở về bằng Back/bfcache hoặc khi tab khác lưu điểm; nhãn hoàn thành có điểm cao nhất, điểm gần nhất và ngày làm. Tổng quan của cả 11 chủ đề/Unit đánh dấu các đề đã nộp. Mở đề đã làm có bảng kết quả cũ và nút xem lại đáp án của lượt nộp mới nhất (áp dụng từ bản cập nhật này); dữ liệu điểm cũ giữ nguyên nhưng không tự suy đoán câu trả lời cũ. Xem lại không tăng lượt làm. Thông báo lưu thành công/thất bại hiện ngay trong bảng điểm.

Chưa thể khẳng định nguyên nhân mất dấu trên phiên học thực tế của bé vì chưa có dữ liệu trình duyệt đó. Nguồn trước đã lưu điểm bằng localStorage nhưng mở đề vẫn hiện bài trống, tổng quan không có trạng thái và danh sách môn thiếu cập nhật bfcache. Tiến độ vẫn theo trình duyệt/thiết bị/địa chỉ; chưa đồng bộ tài khoản hoặc phục hồi dữ liệu đã bị xóa. Kiểm chứng local: build, audit 66 đề, 602 link; QA 66/66 đề đạt 100/100 khi điền đúng; bộ lưu bền qua đóng/mở browser ở cả hai môn, xem lại không ghi lượt mới, giữ điểm cao nhất, nháp, bản ghi cũ và quota đạt. QA Unit 1, Units 4–5 và trang chọn môn đạt. Responsive toàn site đạt 1296 trường hợp, thêm 32 trường hợp danh sách/tổng quan có dữ liệu hoàn thành đạt. Đã triển khai commit `4d7cbe2`; [CI và Pages đạt](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/41956125824). Trên địa chỉ thật, `qa_persistence.js` đạt ở cả hai môn với hồ sơ thử riêng: nộp → đóng browser → mở lại, xem bài không tăng lượt, Back, tab khác, nháp, điểm cũ và quota. Bốn tài nguyên JS/CSS được đối chiếu live khớp nguồn. Báo cáo `artifacts/persistence-online/report.json`; kiểm tra live lần này tập trung luồng lưu/xem lại ở hai đề đại diện, toàn bộ 66 đề và responsive đã qua local/CI. Không truy cập hoặc sửa dữ liệu trình duyệt của bé.


## Unit 6–7 — bổ sung ngày 2026-11-05

Hai Unit thêm 12 đề/288 câu, trong đó 72 nghe; hai tổng quan HTML/PNG và tám WebP tự tạo. Đã đọc trực tiếp trang in 44–49 và 50–55 (PDF 46–57), đối chiếu Wordlist 79–80; NOTES/PROMPTS nằm trong u06/u07. Unit 6 làm rõ ground floor khác first floor; Unit 7 phân biệt does…like với likes + V-ing và lý do theo từng hồ sơ. Không chép bài đọc hoặc sơ đồ của sách. ID en-u06-deN-v1 và en-u07-deN-v1; nội dung/ID Unit cũ không đổi.

Local: audit 78 đề đạt, 718 liên kết đúng hoa/thường; browser QA 78/78 đề đạt 100/100 khi điền đúng, 95 HTML không lỗi. Bộ Unit 6–7 kiểm tra 12 đề, 72 câu nghe (speech mô phỏng), lưu nháp/tên/hỗ trợ, điểm phần, giữ điểm cao nhất, reset cách ly, thống kê 7 Unit và 32 trường hợp trang/kích thước/theme; standalone có ảnh và chấm đúng. Theme/homepage đã qua QA. Đóng/mở browser cùng hồ sơ riêng ở hai Unit mới đã đạt (xem lại không tăng lượt, giữ best/last, nháp và tab khác); responsive chạy lại riêng đạt 1520 trường hợp, không có lỗi trình duyệt. Lần chạy responsive đầu có một ERR_CONNECTION_REFUSED local và không được tính PASS. Đã xuất bản commit `3d97a1f`; [Actions build/deploy đạt](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/41967235733), gồm 78 đề và 1520 trường hợp responsive trên Linux. Trên web thật, bộ Unit 6–7 đạt đủ 12/12 đề 100/100, 72 câu nghe (speech mô phỏng), nháp/điểm phần/reset và 32 trường hợp layout. Bộ lưu bền kiểm chứng đóng browser rồi mở lại cùng hồ sơ cho en-u06-de1-v1 và en-u07-de1-v1, xem lại không ghi lượt, giữ điểm cao nhất, Back, tab khác và nháp mới. Tám ảnh live khớp byte nguồn. Báo cáo: artifacts/units67-online/report.json, asset-report.json và artifacts/persistence-online/units-report.json. Lần này kiểm tra trực tiếp 12 đề mới trên live; toàn bộ 78 đề và responsive đã qua local/CI. Chưa đánh giá phát âm bằng tai hoặc độ khó bởi học sinh.


## Mẫu học từ và phát âm trên tổng quan Unit 6 (2026-11-05)

Chủ repo yêu cầu làm mẫu trước sau khi rà soát thiếu âm thanh/đánh vần ở tổng quan. Thêm trang riêng `TiengAnh5/Unit6_OurSchoolRooms/HocTuVaPhatAm_Mau.html`, có liên kết từ tổng quan Unit 6. Bốn thẻ phòng dùng lại tranh gốc; nghe thường/chậm, đánh vần từng chữ có highlight và tách cụm thành từng từ, ẩn/hiện nghĩa, mẹo trọng âm computer. Hai hội thoại có nghe cả đoạn hoặc chỉ câu A để bé đáp. Ba bài luyện nhỏ có phản hồi/thử lại, không tính điểm đề. Không thu âm/chấm phát âm.

Tự đánh dấu Đã luyện/Cần ôn dùng khóa riêng `mia5:learn:en-u06-preview-v1`; không đánh dấu tự động từ việc nghe và không đổi điểm/nháp đề. Các lựa chọn này giữ sau đóng/mở cùng browser; ba bài luyện chỉ phản hồi trong phiên hiện tại. Thiếu giọng vẫn đọc chữ/luyện viết; storage bị chặn báo rõ. Thanh Dừng nghe nổi giúp thao tác trên điện thoại. Đây là mẫu, chưa áp dụng các Unit khác.

Local: bộ `qa_study_preview.js` kiểm tra bốn chuỗi đánh vần, nghe thường/chậm, hội thoại, bài luyện đúng/sai, dừng/ẩn trang/callback muộn, không autoplay, hồ sơ đóng/mở, cách ly điểm, storage bị chặn/thiếu giọng và 8 layout/theme; speech trong bộ này mô phỏng. Kiểm tra dịch vụ thật trên Edge: bốn cụm từ +12 chữ của computer room đều có start/end, không error, giọng David en-US; chưa nghe đánh giá bằng tai. Local audit 78 đề/0 lỗi, 734 liên kết, QA 78/78 đề 100/100 và 96 trang không lỗi, theme 96 trang và responsive 1536 trường hợp đạt. Các lượt đầu có ERR_CONNECTION_REFUSED ở server backlog 5 không tính PASS; sau sửa backlog 128 và chạy lại tại cổng 8766 đã đạt. Đã xuất bản commit `9b48466`; [Actions/Pages đạt](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/41970963273). Trên URL thật, `qa_study_preview.js` đạt bốn thẻ/chuỗi chữ, hai hội thoại, ba bài luyện, dừng/callback muộn, đóng/mở hồ sơ, cách ly điểm, thiếu giọng/storage bị chặn và 8 layout (speech mô phỏng). HTML/CSS/JS live khớp byte nguồn. Báo cáo `artifacts/study-online/report.json`, ảnh cùng thư mục; Edge thật kiểm tra riêng ở local, chưa nghe đánh giá bằng tai. Chờ người dùng duyệt mẫu trước khi áp dụng toàn bộ.


## Học tương tác đầy đủ Unit 6 và Unit 7 (2026-11-05)

Chủ repo đã duyệt mẫu và giao làm đầy đủ Unit 6, đồng thời làm Unit 7. Có `HocTuVaPhatAm.html` ở hai Unit, liên kết từ trang tổng quan tương ứng; URL mẫu Unit 6 cũ được giữ như alias cùng nội dung. Unit 6: 14 từ/cụm (4 phòng, 4 tầng, 6 chỉ dẫn), 7 hội thoại, 12 bài luyện. Unit 7: 12 từ/cụm (4 hoạt động, 4 dạng V-ing, 4 lý do), 6 hội thoại, 12 bài luyện. Chia ba nhóm nhỏ, nghe thường/chậm/ABC/câu ví dụ, dừng nổi, giọng đọc thu gọn, xem riêng từ cần ôn. Sơ đồ tầng/hướng đi được vẽ SVG chính xác; dùng lại tranh WebP đã duyệt.

Nguồn dùng chung `generator/english/study/`, dữ kiện tại u06/u07/study.py. Unit 6 kế thừa dấu 4 từ từ key mẫu `mia5:learn:en-u06-preview-v1` khi chưa có key đầy đủ `mia5:learn:en-u06-v1`; Unit 7 dùng `mia5:learn:en-u07-v1`. Key đầy đủ riêng giúp tab mẫu cũ đang mở không ghi đè mất bài luyện mới. Câu trả lời/đã kiểm tra/nhóm bài tự lưu khi nhập hoặc rời trang và khôi phục sau đóng/mở browser. Mỗi câu có signature nội dung để không giữ trạng thái làm đúng khi câu đổi. Không tự nhận đã thuộc từ việc bấm nghe; không thu âm/chấm nói hay đổi điểm/ID đề chính thức.

Local: audit 78 đề, 776 liên kết; bộ đầy đủ 78/78 đề 100/100 với đáp án đúng, 98 HTML không lỗi. `qa_study.js` kiểm tra đủ 26 từ/chuỗi ABC, 13 hội thoại, 24 bài luyện, dấu mẫu cũ, đóng/mở browser, bài đang gõ, đúng/sai, signature, tách Unit/điểm/nháp, storage bị chặn/thiếu giọng và 48 layout/theme. Speech trong bộ tự động là mô phỏng. Theme 98 trang và responsive 1568 trường hợp đạt. Edge thật: 6 cụm từ và hai chuỗi ABC ở hai Unit đều phát xong, 27 utterance start/end không lỗi, giọng David en-US; chưa nghe đánh giá bằng tai. Đã xuất bản commit `ed48e0c`; [Actions/Pages đạt](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/41975762561), bao gồm QA 78 đề, 98 HTML và 1568 trường hợp responsive. Trên URL thật, `qa_study.js` đạt cả hai Unit: đủ 26 chuỗi ABC, 13 hội thoại, 24 bài luyện, kế thừa dấu cũ, lưu khi rời trước debounce, đóng/mở browser, signature, ngăn tab mẫu cũ ghi đè, tách dữ liệu hai Unit/điểm/nháp, thiếu giọng/storage bị chặn và 48 layout. Speech trong kiểm tra live vẫn mô phỏng. Ba HTML và CSS/JS dùng chung live khớp byte nguồn. Báo cáo artifacts/study-full-online/report.json và assets.json. Chưa nghe đánh giá phát âm bằng tai hoặc thử độ khó với học sinh.

## Học từ/phát âm Units 2–5 (2026-11-05)

Đã thêm bốn trang học theo mẫu Units 6–7: Unit 2 có 12 từ/cụm, Unit 3 có 18, Unit 4 có 17, Unit 5 có 15. Mỗi Unit ba nhóm, sáu hội thoại, 12 bài luyện. Có nghe thường/chậm, ABC, câu ví dụ, hội thoại đến lượt em, ẩn nghĩa, cần ôn và lưu bài khi rời/đóng trình duyệt. Key riêng `mia5:learn:en-u02-v1` đến `en-u05-v1`; không thay ID đề, điểm hoặc nháp cũ. Tổng site 102 HTML, vẫn 78 đề. Xem breakdown ngày 2026-11-05 cho nguồn và kiểm chứng.

Kiểm chứng local: audit 78 đề/1008 vị trí câu Tiếng Anh không lỗi; 836 liên kết đúng; QA 78/78 đề đạt 100/100, 102 HTML không lỗi browser; theme 102 trang và responsive 1632 trường hợp đạt. Bộ học từ đạt 88 chuỗi ABC, 37 hội thoại, 72 bài luyện và 144 layout trên cả Units 2–7, gồm lưu sau đóng/mở browser và bảo toàn dữ liệu mẫu cũ. Báo cáo trong artifacts/study-full-local (speech mô phỏng).

Đã xuất bản commit `766f4ed`; [Actions/Pages đạt](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/41980190113), gồm kiểm tra đề, nghe, theme, tiến độ/nháp, học từ và responsive. Trên URL thật, `qa_study.js` đạt cả Units 2–7: 88 từ/chuỗi ABC, 37 hội thoại, 72 bài luyện, lưu sau đóng/mở browser, dấu mẫu cũ, tách dữ liệu và 144 layout/theme. 10 file live (bốn trang học, bốn tổng quan, CSS/JS chung) khớp byte bản local. Báo cáo artifacts/study-full-online/report.json và assets-2-5.json. Native Edge local: nghe từ và đánh vần mỗi Unit 2–5, 42 utterance có start/end, không error; chưa đánh giá bằng tai hay thử độ khó với học sinh.

## Unit 8–9 (05/11/2026)

Đọc trực tiếp đủ trang in 56–67 và Wordlist 80; NOTES cạnh nguồn. Thêm 12 đề/288 câu, 72 nghe, tám tranh ImageGen tự tạo, hai tổng quan HTML/PNG và hai trang học từ/phát âm. Mỗi trang học 15 từ/cụm, sáu hội thoại, 12 bài luyện. Unit 8: vị trí đồ dùng, số ít/nhiều, Whose và sở hữu; Unit 9: địa điểm/hoạt động đã qua, was/were, did + nguyên mẫu. ID mới en-u08-deN-v1/en-u09-deN-v1, key học riêng en-u08/en-u09; không đổi bài/điểm cũ. Xem breakdown 2026-11-05_UNIT8_UNIT9.md.

Local toàn site đạt: 90/90 đề 100/100, 118 HTML không lỗi trình duyệt, theme 118 trang và responsive 1888 trường hợp. Edge native: từ và chuỗi ABC ở hai Unit hoàn tất, không lỗi start/end; chưa nghe đánh giá phát âm bằng tai.

Đã xuất bản bản hoàn chỉnh `a3551a4` (nội dung ở `42c4089`, sửa mốc tiến độ ở `a3551a4`); [Actions/Pages đạt](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/42042821444). CI chạy đủ 90 đề/118 HTML và 1888 trường hợp responsive, nghe/nháp/tiến độ/học từ. Trên URL Pages thật: `qa_english_units.js --units=8,9` đạt 12/12 đề 100/100, 72 nghe, nháp, best, chấm phần, reset cách ly và mốc bậc thang đúng 1/14/27/41/54. `qa_persistence.js --units=8,9` đạt đóng/mở browser, xem lại bài đã nộp, best/last, Back/cross-tab. `qa_study.js` live đạt đủ Units 2–9: 118 từ/chuỗi ABC, 49 hội thoại, 96 bài luyện, lưu sau browser restart và 192 layout/theme. Speech trong các runner là mô phỏng. 28 tài nguyên live (16 HTML mới, tám WebP, trang chủ/môn, catalog và home.js) khớp byte bản nguồn; không so byte PNG giữa hệ render Windows/Linux. Native Edge local có 18 utterance start/end, không lỗi; chưa đánh giá phát âm bằng tai hoặc độ khó với học sinh. Báo cáo artifacts/units89-online/{report,assets}.json, persistence-online và study-full-online/report.json.

## Unit 10 và hai Review (06/11/2026)

Đã đọc đủ 40–43 và 68–77, giữ scan ngoài repo. Thêm 18 đề/432 câu/108 nghe; Unit 10 thêm bốn tranh hoạt động ImageGen, Review tái dùng tranh đã duyệt. Review 1 ôn 1–5, Review 2 ôn 6–10; mỗi câu gắn sourceUnits và audit bắt buộc đúng năm Unit mỗi đề. Học từ mới: Unit 10 có 16 từ/cụm; mỗi Review 14; mỗi phần sáu hội thoại, 12 bài luyện. Metadata kind/topic/overview phân biệt Review với Unit, không tạo Unit 11/12; điểm/nháp cũ giữ nguyên. Xem breakdown 2026-11-06_UNIT10_REVIEW1_REVIEW2.md.

## Kiểm chứng sau xuất bản

Đã xuất bản commit `5bba2eb`; [Actions/Pages đạt](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/42103227242). CI kiểm toàn bộ bản cuối: 108 đề/142 HTML, 2272 trường hợp responsive, nghe/nháp/tiến độ/Review/học từ. Trên Pages thật, qa_english_units --topics=u10,r01,r02 đạt 18/18 đề 100/100, đủ 108 nghe, giữ nháp/best, chấm phần/reset cách ly, thứ tự thẻ đúng U1–5/R1/U6–10/R2 và nhãn Review. qa_persistence --topics=... đạt đóng/mở browser, xem lại bài nộp, best/last, Back/cross-tab. qa_study live đạt cả 11 trang: 162 chuỗi ABC, 67 hội thoại, 132 bài luyện, lưu sau browser restart và 264 layout/theme, gồm tương thích mẫu Unit 6. Speech trong runner là mô phỏng.

34 tài nguyên live (24 HTML mới, bốn WebP, ba trang chủ/môn, catalog, home.js và study.js) khớp byte bản nguồn; không so byte PNG giữa Windows/Linux. Edge native local: 26 start/end, không error, chỉ chứng minh phát xong; chưa nghe duyệt phát âm bằng tai hay có đánh giá độ khó của học sinh. Báo cáo: artifacts/topics-u10-r01-r02-online/report.json, final-three-online/assets.json, study-full-online/report.json và persistence-online.
