# Toán tập hai — Chủ đề 7–8

## Giao việc và nguồn

Chủ repo đã giao triển khai chủ đề 7–8 sau khi xác nhận PDF mới. Đã đọc riêng từng trang in 4–39, Bài 36–48; xem [NOTES nguồn](../../generator/math_volume2/NOTES.md). PDF 70 trang là bản thiếu phần sau: bài học dừng ở trang in 67. Không cần thêm sách để làm hai chủ đề này; cần bổ sung cho chủ đề 10–12.

## Kết quả triển khai

- Chủ đề 7 **Tỉ số và các bài toán liên quan**, Bài 36–44: tổng quan HTML/PNG/reader, sáu đề/144 câu.
- Chủ đề 8 **Thể tích. Đơn vị đo thể tích**, Bài 45–48: tổng quan HTML/PNG/reader, sáu đề/144 câu.
- Ba cấp 10/8/6 câu, 100 điểm; bốn dạng mc/tf/fill/order, lời giải từng câu, hình SVG đúng số phần/khối. Không sao chép câu hay hình sách.
- Bảo toàn ID và nội dung cũ; hai nhóm mới dùng `cd7-deN`, `cd8-deN`, cơ chế lưu nháp/kết quả/xem lại/best/last hiện hành. Lưu theo trình duyệt và địa chỉ web, chưa đồng bộ tài khoản.
- Toán hiện có **8 chủ đề/48 đề/1152 câu** (tập một sáu chủ đề; tập hai hai chủ đề). Anh giữ 144 đề/3456 câu. Toàn site **192 đề/252 HTML/32 tổng quan HTML+PNG**.
- Nguồn: `generator/math_volume2/`, wrapper/tests sinh tự động; registry `cfg.py`, tổng quan dùng bộ dựng chung. Quyết định cấu trúc ở docs08.
- Chủ đề 7 màu phụ cam đất `#A15B27/#FFF0DF`; chủ đề 8 xanh hồ `#316F87/#E2F3F8`, khung giao diện hồng sáng hiện có. Màu tối riêng trong trang Toán.

## Kiểm chứng

Local đã đạt toàn bộ 11 nhóm kiểm tra trên bản build cuối:

- Audit: 48 đề Toán +144 đề Anh, 0 lỗi; audit độc lập 288 câu mới từ dữ kiện đã sinh, số phần/khối và quan hệ thử ngược đều đạt.
- Link: 2156 tham chiếu HTML/CSS, 0 lỗi. Toàn site 192/192 đề đạt 100/100, 252 HTML không lỗi trình duyệt; sai/điểm phần và reset cách ly giữ nguyên.
- Responsive: 4032 tổ hợp (252 trang ×8 chiều rộng ×2 theme), 0 tràn ngang; reader giữ đủ chữ và thao tác chạm, câu cuối không bị thanh kết quả che.
- Riêng hai chủ đề: 12/12 đề trên Chromium và WebKit; từ chối đảo tỉ số, phân số chưa tối giản khi đề yêu cầu, phần trăm sai hệ số và thể tích sai hệ số; nhận dấu phẩy thập phân. Mỗi trình duyệt 16 bố cục tổng quan đúng theme; ảnh đã xem ở sáng/tối.
- Standalone: đề 1 của mỗi chủ đề chạy file HTML tự chứa và đạt 100/100 trên Chromium. Không suy WebKit file:// từ kiểm tra HTTP.
- Lưu bài: profile Chromium đóng/mở thật, khôi phục đáp án và xem lại không tăng lượt; best/last, Back, cập nhật tab khác, nháp, reset cách ly, storage đầy đều đạt cho cd7-de1/cd8-de1. Engine nháp và theme/home hồi quy đạt.
- Đã xem hai poster đầy đủ (cắt từng đoạn để đọc), reader điện thoại và hai sơ đồ trong đề. Kiểm kê xác nhận không thay đổi file câu hỏi/wrapper cũ hoặc trang Anh; ba file site cũ thay đổi chỉ là index Toán, index chung và catalog.

Bằng chứng local: artifacts/math78-local/qa-results.json, source-inventory.json, full-report.json, responsive-report.json, các report Chromium/WebKit/persistence và log từng nhóm. CI và web thật còn chờ triển khai; không coi local là đã xuất bản.

## Giới hạn và phần tiếp theo

- Chưa có học sinh làm thử để xác nhận độ khó hoặc thời lượng. Không tuyên bố đã kiểm trên iPad thật.
- Máy tính cầm tay dùng riêng hoặc ứng dụng; chưa có máy tính nhúng.
- Bản sách đủ phạm vi chủ đề 9 nhưng chưa được giao triển khai; chủ đề 10 chỉ có phần đầu, 11–12 thiếu trang bài học.
- Không đổi hoặc commit hai thay đổi có sẵn trước tác vụ: AGENTS.md và kế hoạch ôn Anh cả năm chưa được theo dõi.
