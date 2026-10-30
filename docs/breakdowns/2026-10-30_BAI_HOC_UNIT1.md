# Bài học từ giao diện và tranh Unit 1 — 30/10/2026

## Điều đã xảy ra

Chủ repo phản hồi hình cá heo SVG khó nhận diện; hình thành phố chỉ có các khối nhà nên thiếu bối cảnh cho trẻ. Tự điền đúng 100/100 và không tràn ngang chưa chứng minh tranh giúp học sinh hiểu câu hỏi. Đây là thiếu sót về chất lượng minh họa ở bản mẫu, không phải lỗi đáp án.

Chủ repo duyệt một mẫu cá heo, sau đó duyệt áp dụng phong cách ấy cho đủ sáu tranh. Mã sửa `4798597`, [workflow build/deploy thành công](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/40976976768). Các số liệu dưới đây là bằng chứng của đợt đó, không phải cam kết mọi phiên bản sau đều đạt.

| Vấn đề | Bài học | Cách phòng tránh và bằng chứng cần có |
|---|---|---|
| Cá heo góc cạnh khó nhận ra | Tranh dạy từ phải rõ chủ thể trước khi đẹp | Xem từng tranh ở kích thước thật trong câu hỏi; kiểm tra mõm, vây, đuôi và dáng thân. Không chỉ xem ảnh nguồn phóng to. |
| Thành phố chỉ là vài khối nhà | Trẻ cần ngữ cảnh đủ rõ để phân biệt từ | Thành phố có đường phố, công trình và giao thông; đồng quê có không gian mở, nhà và đồng ruộng. Không gắn nhãn đáp án lên tranh. |
| Bản poster chụp thiếu một số ảnh mới | Chờ font không đồng nghĩa ảnh đã giải mã | `tools/render_overviews.js` chờ `img.decode()` và báo lỗi nếu thất bại; mở PNG cuối cùng bằng mắt. |
| Reader loại bỏ kích thước inline có thể làm ảnh méo | Quy tắc chuyển SVG sang reader không tự phù hợp với raster | Nhánh IMG trong `generator/overview.js` giữ `height:auto`; responsive kiểm tra tỷ lệ 3:2 cho bộ ảnh Unit 1. Không ép mọi ảnh tương lai phải 3:2. |
| Audit cũ chỉ cho SVG và cấm mọi data URI | Kiểm tra phải bám mục đích: tránh scan sách, vẫn hỗ trợ ảnh tự tạo | Audit chỉ chấp nhận đúng sáu WebP nguồn hiện hành; không mở cửa cho mọi ảnh nhúng. Khi thêm unit, mở rộng registry có chủ đích. |
| Ảnh nguồn lớn, lặp lại trong nhiều đề | Tách bản web dùng chung và bản tự chứa | Nguồn WebP ở generator; web trích ra assets bằng URL tương đối; standalone nhúng cùng byte. Không tham chiếu đường dẫn máy cá nhân. |
| Tài liệu nối thêm nhiều lần chứa trạng thái cũ | Hướng dẫn hiện hành phải dễ xác định | 01 và 08 là bản hiện tại, snapshot cũ vào history; README chỉ đường tới nguồn chính. |

## Bằng chứng đã có

- Đối chiếu dữ liệu trước/sau, bỏ trường `fig`: 144 câu giữ nguyên nội dung và đáp án; ID tiến độ không đổi.
- Local: audit 36 Toán + 6 Anh không lỗi; 42 đề tự điền đúng đạt 100/100; 251 tham chiếu tĩnh hợp lệ; 832 tổ hợp trang/chiều rộng/theme đạt. Sáu đề Anh standalone cũng đạt.
- Live sau deploy: 6 ảnh khớp byte với WebP nguồn; 7 trang Unit 1 × 3 chiều rộng (320/768/1366) × 2 theme = 42 trường hợp, ảnh giải mã đủ, giữ tỷ lệ, không tràn ngang/lỗi trình duyệt.
- Báo cáo sinh tự động trong `artifacts/`, không commit. Đây là mô phỏng Chromium; chưa phải thử nghiệm trên thiết bị thật hoặc đánh giá khả năng nhận diện của em gái.

## Điều giữ cho lần sau

Dùng [quy trình tranh](../playbooks/TRANH_MINH_HOA.md). Khi chủ repo yêu cầu một mẫu trước, dừng ở mẫu cho đến khi được duyệt; khi đã duyệt áp dụng, thực hiện đủ phạm vi, không hỏi lại từng hình. Sau sửa phải xem cả câu hỏi, reader và PNG xuất cuối cùng. Không diễn giải điểm QA thành bằng chứng nội dung phù hợp độ tuổi.
