# 07 — Kiểm tra chất lượng (QA)

## Luồng chính thức (từ gốc repo, Windows hoặc Linux)

Cần Python 3.13+ và Node.js 24. Cài phụ thuộc: `npm ci --prefix generator`, sau đó `npx --prefix generator playwright install chromium` (Linux CI dùng thêm `--with-deps`).

```text
python tools/build.py --regenerate
node generator/audit.js
python tools/check_links.py
python tools/serve.py
```

Giữ server chạy, mở terminal thứ hai:

```text
node tools/qa.js
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
