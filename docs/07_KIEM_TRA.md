# 07 — Kiểm tra chất lượng (QA)

## Luồng chính thức (từ gốc repo, Windows hoặc Linux)

Cần Python 3.13+ và Node.js 24. Cài phụ thuộc: `npm ci --prefix generator`, sau đó `npx --prefix generator playwright install chromium` (Linux CI dùng thêm `--with-deps`).

```text
node tools/build.js --regenerate
node generator/audit.js
python tools/check_links.py
python tools/serve.py
```

Giữ server chạy, mở terminal thứ hai:

```text
node tools/qa.js
node tools/qa_listening.js
node tools/qa_english_unit1.js
node tools/qa_theme.js
node tools/qa_home.js
node tools/qa_drafts.js
node tools/responsive.js
```

Server ở `http://127.0.0.1:8765/Lop_5_Mia/`, kiểm tra hoa/thường giống Pages. QA đọc toàn bộ HTML trong `site/`, kiểm tra 53 trang, 42 đề (36 Toán + 6 Anh), link và tài nguyên dựng từ JavaScript, 24 câu/100 điểm, tự điền đúng đạt 100/100, lỗi console/request, tràn ngang ở 400px, biên nhãn SVG (có tính phép xoay/biến đổi), thống kê hai trang chủ và lưu tiến độ sau tải lại. Có kiểm tra nộp thiếu câu, hủy xác nhận, điểm một phần, làm lại và giữ điểm cao nhất. Báo cáo/ảnh ở `artifacts/local/`.

Online chạy cùng bộ: `node tools/qa.js https://okeydokey8525.github.io/Lop_5_Mia/ --no-shots`; báo cáo ở `artifacts/online/`. Dữ liệu thử chỉ nằm trong browser context riêng, không ảnh hưởng tiến độ trình duyệt của em.

`--no-shots` bỏ chụp ảnh, không bỏ kiểm tra hành vi. Xem ảnh thủ công vẫn cần ở lần thay đổi giao diện. QA không chứng minh độc lập đáp án toán học của mọi câu: tự điền dùng đáp án khai báo. Audit tính độc lập giá trị của câu sắp xếp, còn kiểm tra nội dung từng câu và mức độ phù hợp vẫn cần rà soát/cho em làm thử.

Audit mặc định đủ 6 chủ đề, phát hiện file đề thiếu và trả exit code khác 0 khi lỗi. Đã sửa kiểm tra giảm dần, bổ sung tính giá trị số đo, phân số, phép tính, diện tích/chu vi và bảng chiều cao cho các câu sắp xếp hiện có.

## Công cụ cũ (chạy trong `generator/`)

## Công cụ
| Lệnh | Việc |
|---|---|
| `node audit.js 5,6` | Mỗi đề đúng 24 câu, 10/8/6; mc hợp lệ (đáp án nằm trong 0–3, 4 phương án không trùng); câu `order` sắp đúng. Truyền số chủ đề; nếu bỏ trống thì chạy `1,2,3,4,5,6`. |
| `node tall.js out/Toan5 [lọc]` | Mở từng đề bằng trình duyệt, **tự điền đáp án đúng**, nộp, đọc điểm và lỗi console. Mong đợi: 100/100, không lỗi. |
| `node png.js` | Render `TongQuan_*.png` 1080px, in phần tử bị tràn, đo `scrollWidth` ở 400px. |
| `node idx.js` | Kiểm tra trang chủ: thống kê, link, tiến độ sau khi làm thử. |
| `node figs.js <file.html> <tiền tố>` | Chụp các câu có hình. |
| `node qshot.js <file.html> <tiền tố> <số câu...>` | Chụp câu chỉ định. |
| `node show.js <test.js> <common/cdN.js>` | In đáp án các câu. |

## Tiêu chí đạt (mọi chủ đề mới)
1. `audit.js`: 0 lỗi.
2. `tall.js`: mọi đề 100/100, **0 lỗi console**.
3. **Xem ảnh bằng mắt**: mở PNG tổng quan và ảnh các câu có hình; nhãn không bị cắt, hình đúng toán học/đúng nghĩa.
4. Mobile 400px: không tràn ngang (trang chủ, tổng quan, đề).
5. **Link kiểm tra phân biệt hoa thường**: mọi `href` trỏ tới file có thật với **đúng chữ hoa/chữ thường** (Windows không báo lỗi, GitHub Pages thì 404). Dùng `python tools/check_links.py` từ gốc repo.
6. Trang chủ liệt kê đúng số đề; mốc cầu thang đúng.
7. Đã chạy lại QA cho **tất cả** chủ đề cũ (không làm hỏng).
8. Trên bản deploy: mở trang thật, làm thử 1 đề, nộp, tải lại xem tiến độ còn không.

## Việc cần người thật
Em gái chưa làm thử đề nào. Sau khi deploy, nhờ chủ repo cho em làm thử và ghi lại câu nào khó hiểu, rồi sửa đề. Đừng khẳng định "đề dễ/khó phù hợp" khi chưa có phản hồi này.

## Kiểm tra responsive và hình ảnh sau đổi màu

`node tools/responsive.js` kiểm tra 704 tổ hợp (44 trang × 8 chiều rộng × 2 chế độ sáng/tối), không chấp nhận tràn ngang toàn trang. Bảng 7 hàng trong tổng quan có cuộn nội bộ, không thu nhỏ chữ. Kiểm tra nội dung reader/poster khớp nhau, cỡ chữ đoạn văn ≥16px, nút chuyển view, menu đề và nút nộp bài cảm ứng. Kết quả/ảnh ở `artifacts/responsive-local/` hoặc `artifacts/responsive-online/` theo URL truyền vào. Thiết bị là mô phỏng Chromium; vẫn cần thử máy thật của em nếu dùng trình duyệt khác.

`node tools/render_overviews.js` xuất lại 6 PNG 1080px ở `site/Toan5/` và bản sao trong `generator/out/Toan5/`. Dùng lệnh build Node đầy đủ để đảm bảo PNG khớp HTML. PNG cũ được giữ trong lịch sử Git.

Kiểm tra bổ sung sau nộp ở 320/360/390/768px: cuộn xuống cuối trang và xác nhận câu cuối nằm phía trên thanh kết quả.

## QA sau mẫu Unit 1

Luồng mặc định hiện audit 36 Toán + 6 Anh. `generator/audit_english.js` xác nhận 144 câu, số mức/điểm, số phương án, dữ liệu chữ/nối/sắp từ/hình và độ đa dạng (ít nhất 4 dạng mỗi đề). QA browser đối chiếu `site/catalog.json`, làm đúng toàn bộ 42 đề và kiểm tra liên kết hồ sơ.

Kiểm tra riêng Tiếng Anh: hoa/thường, nháy cong, rút gọn, yêu cầu dạng đầy đủ, colour/color, từ thừa/sai; thao tác xóa-sắp lại, chọn sai, điểm một phần khi nối; điểm tốt nhất còn sau làm sai; reset Anh không xóa 36 khóa Toán. `tall.js` cũng tự điền mọi dạng mới; có thể chạy `node generator/tall.js site` từ gốc repo.

Responsive hiện 52 HTML × 8 kích thước × 2 chế độ = 832 tổ hợp, 7 tổng quan có reader/poster. Các con số 36/44/704 ở mục cũ là mốc trước khi thêm Anh. Chụp và xem hình mới trước khi giao.

### Tranh Unit 1 — 30/10/2026

Bổ sung kiểm tra ảnh giải mã được (768×512) trong `qa.js`, giữ tỷ lệ 3:2 ở mọi viewport/theme trong `responsive.js`. `audit_english.js` chỉ cho nhúng đúng sáu WebP đã duyệt từ thư mục nguồn, không cho ảnh lạ. Renderer chờ `img.decode()` trước khi xuất PNG; reader giữ chiều cao tự động của ảnh. Đã đối chiếu 144 câu trước/sau bằng dữ liệu (bỏ trường fig): nội dung và đáp án giữ nguyên. Đã xem cả 6 tranh ở kích thước thực và poster xuất lại; standalone Tiếng Anh 6/6 đề đạt 100/100.

### Mẫu nghe ba cấp

`node tools/qa_listening.js [baseURL]` kiểm tra 6 câu/3 cấp/8 ý, phát/chậm/dừng, callback cũ sau chuyển câu, lỗi dịch vụ, giọng tải trễ, không có giọng Anh, thiếu API, timeout khi dịch vụ không bắt đầu, điểm phần/câu thiếu/biến thể chữ, làm lại và giữ nguyên storage đề. Mười trường hợp giao diện (5 chiều rộng × 2 theme) và nút tối thiểu 44px. Báo cáo trong artifacts/listening-local hoặc listening-online. Speech trong bộ này được mô phỏng để CI Linux không cần loa/giọng cài sẵn; không dùng kết quả ấy để khẳng định phát âm hay âm thanh thật đạt.

Kiểm tra dịch vụ thật riêng: thao tác nút ở trình duyệt có giọng Anh, xác nhận start/end; sau đó chủ repo nghe thử bằng tai trên máy/điện thoại. Không tự thêm câu nghe vào sáu đề trước khi duyệt mẫu. Responsive toàn site sau thêm mẫu: 53 trang × 8 chiều rộng × 2 theme = 848.

### Unit 1 chính thức có nghe, phiên bản 2

Audit đếm đủ 6 listen/đề và 2 listen/cấp; main qa và tall hỗ trợ điền các field để kiểm tra 100/100. Chạy thêm node tools/qa_english_unit1.js [baseURL]: 36 câu nghe, điểm phần 2,5/5, mở lời nghe trước/sau nộp, hỗ trợ lưu vào kết quả, replay sau nộp, làm lại không nhân đôi listener, theme mặc định sáng khi OS tối, chuyển và lưu theme giữa các trang, thống kê/reset chỉ dùng ID -v2 và giữ dữ liệu cũ/Toán. 32 trường hợp trang/chiều rộng/theme chủ động, ngoài 848 trường hợp theo OS của responsive chung. Speech QA dùng fixture; vẫn kiểm tra phát thật bằng Edge và nghe đánh giá trên thiết bị học sinh.

### Theme dùng chung toàn site

node tools/qa_theme.js [baseURL]: đủ 53 trang mặc định hồng sáng khi OS tối, đúng một toggle mỗi trang, chọn Tối/Sáng giữ giữa trang chủ chung/Toán/Anh/tổng quan/đề, kế thừa tùy chọn Anh cũ, hoạt động khi localStorage bị chặn, không đổi dữ liệu điểm. responsive.js chủ động ghi theme sáng/tối trước mỗi lượt, vì theme hiện không theo OS: 848 trường hợp là 53 trang × 8 chiều rộng × 2 theme thực. Không diễn giải chỉ thay prefers-color-scheme thành đã kiểm tra theme tối. CI chạy thêm qa_theme.js; xem ảnh render sau khi font tải và hiệu ứng ổn định.

### Trang chủ tạo hứng thú

node tools/qa_home.js [baseURL]: thanh tiến độ/sao theo điểm thật, bỏ bản ghi hỏng/âm và Anh phiên bản cũ, tên không trở thành HTML, lần đầu không chúc mừng điểm lịch sử, một lời động viên cho mỗi lượt mới kể cả làm lại, đóng/tải lại không lặp, trở lại bằng bfcache, storage bị chặn, giảm chuyển động và 10 tổ hợp kích thước/theme. Ảnh/báo cáo trong artifacts/home-local hoặc home-online. Kiểm tra mặc định sáng/tối và toàn bộ 53 trang/42 đề vẫn theo bộ QA chung.

### Hồi quy sau kiểm tra chéo

node tools/qa_drafts.js [baseURL]: ca gốc 3.9/4 phải sai; kiểm tra tử/mẫu/phần nguyên có chữ, thập phân, số âm, mẫu 0, số mũ, số vượt giới hạn, phân số tương đương và yêu cầu tối giản. Kiểm tra bắt đầu bằng order/reorder làm đồng hồ chạy.

Điền đúng rồi tải lại cả Toán/Anh, khôi phục đủ dạng mc/pic/tf/fill/order/text/match/reorder/listen để nộp vẫn 100/100; giữ tên, thời gian và hỗ trợ nghe. Không cộng thời gian nghỉ sau reload; bỏ/giữ nháp, xóa sau nộp, giữ điểm cao nhất, reset hai môn riêng biệt, chặn nháp khác nội dung/lượt nộp, xử lý storage bị chặn. Trang môn có nhãn đang làm dở và CTA mở đúng nháp. Dữ liệu thử nằm trong context riêng. Báo cáo/ảnh ở artifacts/draft-local hoặc draft-online.

## Mốc Unit 1–3 (trước khi thêm Unit 4–5)

54 đề (36 Toán + 18 Anh), 67 HTML, 9 tổng quan; responsive 67×8×2 = 1072. Các số thấp hơn ở trên là lịch sử. Audit Anh có danh sách ảnh cho phép riêng u01/u02/u03, giữ chặn ảnh lạ. Chạy thêm `node tools/qa_english_units23.js [baseURL]`: 12 đề mới, 72 câu nghe, lời đọc khớp đáp án, phát đủ ba cấp, khôi phục nháp/điểm, chấm phần, tổng tiến độ và reset cách ly; standalone local. Speech được mô phỏng, không coi là đánh giá phát âm bằng tai.

Trong lượt quét Pages đã gặp 503 tạm thời khi API kiểm tra tham chiếu tải engine.css; ba lần kiểm tra trực tiếp sau đó đều 200, đúng CSS. `qa.js` thử lại tối đa ba lần chỉ cho 502/503/504, có log mỗi lần; 404/sai hoa thường và lỗi kéo dài vẫn fail. Không coi lần quét bị ngắt là toàn bộ live đã đạt; ghi kết quả lần chạy lại riêng.

## Mốc hiện hành: Unit 1–5

66 đề (36 Toán + 30 Anh), 81 HTML, 11 tổng quan; responsive 81×8×2 = 1296. Audit ảnh có danh sách riêng u01..u05. Chạy thêm `node tools/qa_english_units.js --units=4,5 [baseURL]`; wrapper qa_english_units23.js vẫn chạy Unit 2–3 qua cùng runner, tổng thống kê lấy từ catalog. Runner kiểm tra 12 đề mới/72 câu nghe, mức 2/2/2, speech khớp lời, nháp/kết quả/điểm phần/reset, 32 trường hợp trang ở hai theme, standalone khi local. Riêng Unit 5 kiểm tra nháy cong I’d, I would và yêu cầu full form; không nhận từ thừa. Speech được mô phỏng, không đánh giá chất lượng giọng bằng tai.
