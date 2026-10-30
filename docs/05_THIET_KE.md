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

## Mẫu Tiếng Anh Unit 1

Màu nhận diện Unit 1: `#8B4E84`, nền `#F2E4F1` (tím hoa); chế độ tối `#DAB1D5/#3F2B3D`. Giữ nền/hero hồng anh đào, font và hiệu ứng chung. Một poster 1080px/PNG và reader cho điện thoại/tablet như Toán. SVG từ vựng tự vẽ, không dùng ảnh SGK. Câu nối dùng select, sắp từ dùng nút bấm; không đòi kéo-thả. Hồ sơ đọc lặp chỉ hiển thị một lần theo nhóm và có liên kết quay lại.

## Phong cách tranh từ vựng đã duyệt — 30/10/2026

Unit 1 dùng minh họa nét mềm, đổ bóng nhẹ, màu dịu theo mẫu cá heo chủ repo duyệt. Tranh phải rõ chủ thể ở kích thước câu hỏi, không ghi đáp án lên hình. Thành phố/đồng quê cần bối cảnh dễ phân biệt; hình học Toán vẫn dùng SVG chính xác. Thực hiện theo `docs/playbooks/TRANH_MINH_HOA.md`; nguồn/prompt ở `generator/english/u01/images/`.

## Hồng sáng Tiếng Anh — chủ repo duyệt 30/10/2026

Nguồn generator/english/theme.css và theme.js. Nền #FFF0F6, thẻ #FFF8FC, đầu trang #FFE0EE → #FFC2DD, nút #FFB3D1 với chữ #702344, viền #F2A7C7, chữ chính #54233D. Mặc định sáng độc lập prefers-color-scheme. Nút Sáng/Tối lưu riêng bằng mia5:ui-en-theme, dùng chung các trang Anh; Math vẫn theo thiết kế cũ. Không thêm bộ lọc CSS phủ lên tranh; PNG tổng quan được sinh lại từ cùng HTML.

## Mở rộng hồng sáng ra toàn website — yêu cầu tiếp theo ngày 30/10/2026

Bảng màu hồng sáng và nút Sáng/Tối nay dùng chung cho toàn bộ 53 trang, cả Toán và Anh, trang chủ chung, reader, poster và HTML tự chứa. Hai file nguồn chuyển từ generator/english/theme.* sang generator/theme.css và theme.js; web dùng site/assets/theme.css/js. Khóa lựa chọn chung mia5:ui-theme; khi chưa có khóa mới, kế thừa lựa chọn chủ động cũ mia5:ui-en-theme. Chọn Sáng ghi rõ khóa mới nên không bị khóa cũ ép về Tối. Không có lựa chọn trước đó thì luôn sáng, độc lập hệ điều hành. Quy định “chỉ đổi Anh/Toán giữ màu cũ” trong mục trước là phạm vi giai đoạn trước, đã được yêu cầu mới thay thế.
