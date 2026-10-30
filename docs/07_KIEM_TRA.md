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
node tools/responsive.js
```

Server ở `http://127.0.0.1:8765/Lop_5_Mia/`, kiểm tra hoa/thường giống Pages. QA đọc toàn bộ HTML trong `site/`, kiểm tra 44 trang, 36 đề, link và tài nguyên dựng từ JavaScript, 24 câu/100 điểm, tự điền đúng đạt 100/100, lỗi console/request, tràn ngang ở 400px, biên nhãn SVG (có tính phép xoay/biến đổi), thống kê hai trang chủ và lưu tiến độ sau tải lại. Có kiểm tra nộp thiếu câu, hủy xác nhận, điểm một phần, làm lại và giữ điểm cao nhất. Báo cáo/ảnh ở `artifacts/local/`.

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
