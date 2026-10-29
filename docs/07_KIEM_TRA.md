# 07 — Kiểm tra chất lượng (QA)

Cần Node.js + `playwright` (Chromium) và Python 3. Cài: `npm i -D playwright` rồi `npx playwright install chromium`. Chạy trong `generator/`.

## Công cụ
| Lệnh | Việc |
|---|---|
| `node audit.js 5,6` | Mỗi đề đúng 24 câu, 10/8/6; mc hợp lệ (đáp án nằm trong 0–3, 4 phương án không trùng); câu `order` sắp đúng. Truyền số chủ đề; nếu bỏ trống thì chạy `1,2,3,4`. |
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
5. **Link kiểm tra phân biệt hoa thường**: mọi `href` trỏ tới file có thật với **đúng chữ hoa/chữ thường** (Windows không báo lỗi, GitHub Pages thì 404). Viết `generator/check_links.py` nếu chưa có.
6. Trang chủ liệt kê đúng số đề; mốc cầu thang đúng.
7. Đã chạy lại QA cho **tất cả** chủ đề cũ (không làm hỏng).
8. Trên bản deploy: mở trang thật, làm thử 1 đề, nộp, tải lại xem tiến độ còn không.

## Việc cần người thật
Em gái chưa làm thử đề nào. Sau khi deploy, nhờ chủ repo cho em làm thử và ghi lại câu nào khó hiểu, rồi sửa đề. Đừng khẳng định "đề dễ/khó phù hợp" khi chưa có phản hồi này.
