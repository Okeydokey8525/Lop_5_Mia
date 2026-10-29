# 05 — Hệ thống thiết kế (GIỮ NGUYÊN)

Chủ repo rất thích thiết kế hiện tại. Mọi chủ đề mới (kể cả Tiếng Anh) phải trông như cùng một bộ.

## Nguồn sự thật
Giao diện nằm trong `generator/engine.css`, `engine.js`, `fonts.css`, `gen_index.py`, `gen_overview.py`. Muốn biết chi tiết hãy **mở file HTML đã build trong `site/` bằng trình duyệt** và đọc CSS. Không thiết kế lại từ đầu.

## Font
`Baloo 2` (tiêu đề, số, nhấn) và `Be Vietnam Pro` (chữ thường), nhúng base64 trong `fonts.css`. Hỗ trợ đầy đủ tiếng Việt. Tiếng Anh dùng cùng font (kiểm tra hiển thị ký tự đặc biệt nếu có).

## Bảng màu hiện hành — hồng anh đào

Chủ repo duyệt thay màu và cải thiện responsive ngày 29/10/2026. Bộ xanh ngọc cũ được thay bằng:

| Thành phần | Màu |
|---|---|
| Nền | `#FFF5F8` |
| Thẻ nội dung | `#FFFFFF` |
| Đầu trang sáng | `#FCE4EC` → `#F8BBD0` |
| Nút/chọn chính | `#B83F6B` |
| Chữ chính / chữ phụ | `#4A2433` / `#7A5363` |
| Viền | `#EDCFDA` |
| Nền tối / thẻ tối | `#21161D` / `#2F2029` |
| Đầu trang tối | `#432A38` → `#583347` |

Sáu chủ đề có màu chữ/nhấn trầm và nền pastel đi kèm: hồng `#B83F6B/#FCE4EC`, đào `#94523F/#FCE6DC`, bạc hà `#3E7266/#E3F0EB`, lavender `#77528F/#EEE5F5`, xanh trời `#4A6F9D/#E5EDF8`, tím hồng `#955077/#F4E4EE`. Giữ phân biệt đúng/sai/đúng một phần bằng xanh lá/đỏ/vàng cùng nhãn chữ.

## Trang tổng quan (poster)
- Bản poster rộng **1080px**, xuất PNG bằng `tools/render_overviews.js`; trên màn hình ≤820px mặc định đọc từng bài, chữ thân bài 17px và bố cục dọc. Có nút chuyển giữa hai cách xem. Không thu nhỏ toàn bộ poster để làm chế độ đọc mặc định nữa.
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

## Sửa lỗi hiển thị ngày 29/10/2026

Giữ toàn bộ hệ thống thiết kế. Đã mở rộng khung SVG cho tam giác vuông và ao trong khu đất để nhãn dài không bị cắt; dịch nhẹ nhãn chiều rộng của hình chữ nhật và dải cây xanh vào trong khung. Không đổi số liệu hay đáp án. QA tự động kiểm tra biên nhãn bằng tọa độ SVG sau biến đổi, đồng thời đã xem ảnh render.

## Responsive đã chuẩn hóa

Khung câu hỏi dùng cột grid `minmax(0,1fr)`, SVG bị giới hạn bởi chiều rộng thật của thẻ; xử lý chữ dài và đáp án ở 320–360px. Nút cảm ứng chính tối thiểu 44px. Liên kết chọn môn đặt trong hero, tránh bị khối hướng dẫn đè. Trang tổng quan thu gọn menu đề; bảng giá trị số giữ các cột và cuộn bên trong vùng bảng. Giữ font, hiệu ứng giảm chuyển động và khóa localStorage.

Thanh nộp/kết quả được đo bằng ResizeObserver; khoảng trống cuối trang theo chiều cao thực tế, tránh che câu cuối ở màn hình 320–360px sau khi nộp.
