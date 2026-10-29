# 05 — Hệ thống thiết kế (GIỮ NGUYÊN)

Chủ repo rất thích thiết kế hiện tại. Mọi chủ đề mới (kể cả Tiếng Anh) phải trông như cùng một bộ.

## Nguồn sự thật
Giao diện nằm trong `generator/engine.css`, `engine.js`, `fonts.css`, `gen_index.py`, `gen_overview.py`. Muốn biết chi tiết hãy **mở file HTML đã build trong `site/` bằng trình duyệt** và đọc CSS. Không thiết kế lại từ đầu.

## Font
`Baloo 2` (tiêu đề, số, nhấn) và `Be Vietnam Pro` (chữ thường), nhúng base64 trong `fonts.css`. Hỗ trợ đầy đủ tiếng Việt. Tiếng Anh dùng cùng font (kiểm tra hiển thị ký tự đặc biệt nếu có).

## Màu mỗi chủ đề (màu nhấn của trang tổng quan và đầu trang đề)
| CĐ | Màu |
|---|---|
| 1 | `#0a6f73` (xanh ngọc) |
| 2 | `#c4470a` (cam đất) |
| 3 | `#2e7d32` (xanh lá) |
| 4 | `#6a1b9a` (tím) |
| 5 | `#1565c0` (xanh dương) |
| 6 | `#c2185b` (hồng đậm) |

Chủ đề mới phải chọn màu **khác các màu trên** và không trùng màu nền các khối bài học bên trong cùng poster (đã từng lỗi: đầu trang CĐ5 trùng cam với CĐ2 và với màu bài học; đã sửa thành xanh dương và đổi bài 26 sang xanh ngọc).
Màu nhấn chung cho nét gạch/đường cao: `#e8741a`.

## Trang tổng quan (poster)
- Rộng **1080px**, xuất PNG 1080px bằng `png.js`; cũng là trang HTML xem được trên điện thoại (không tràn ngang ở 400px).
- Bố cục: tiêu đề chủ đề + màu chủ đề, lời mở đầu, các khối bài học (tên bài, số trang SGK nếu biết, ý chính, ví dụ, hình SVG), đường dẫn tới 6 đề.
- Hình minh họa là **SVG tự vẽ**, hình học phải đúng thật (xem lỗi bên dưới).

## Trang chủ (`index.html`)
Có hiệu ứng thu hút (cầu thang tiến độ 1/9/18/27/36 sao, thống kê đề đã làm/sao/điểm cao nhất, nút "tiếp tục", hoạt ảnh vào theo độ trễ, màu theo chủ đề). DATA lấy từ `cfg.CDS`; thêm chủ đề là tự xuất hiện. Cầu thang mốc sao phải cập nhật khi tổng số đề thay đổi (`gen_index.py`).

## Trang làm bài
Đầu trang (hero) có tên sách, tên đề, chủ đề, số câu/điểm/phút; thanh tiến độ và đồng hồ; nộp bài hiện điểm + xếp loại + lời giải từng câu; nút đề trước/đề tiếp/trang chủ. Lỗi đã gặp và cần tránh: nhãn SVG bị cắt khỏi khung, nhãn đè lên cạnh hình.

## Các lỗi thiết kế đã gặp (đừng lặp lại)
1. Nhãn "b" của hình thang bị cắt: viewBox quá chật → mở rộng viewBox và dời nhãn.
2. Nhãn mái nhà đè cạnh: hạ nhãn xuống, giảm cỡ chữ.
3. Hình "tam giác tù" vẽ thực ra là tam giác nhọn: kiểm tra bằng số đo/góc thật.
4. Hình "tam giác đều" không đều: dùng tỉ lệ `62,6 22,75 102,75`.
5. Tiêu đề bài ghi nội dung **không có trong sách** ("con thuyền"): chỉ ghi thứ sách thật sự có.
**Quy tắc: render PNG, mở và nhìn bằng mắt từng poster và từng câu có hình trước khi giao.**

## Tiếng Anh
Giữ nguyên bộ khung/màu/hiệu ứng; trang tổng quan Tiếng Anh thay công thức bằng **từ vựng, mẫu câu, hình minh họa** của unit. Cách trình bày cụ thể ở `docs/09_TIENG_ANH.md`.
