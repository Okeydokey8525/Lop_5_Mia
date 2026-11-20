# Toán tập hai — Chủ đề 9–10

## Phạm vi và nguồn

Chủ repo giao hai chủ đề tiếp theo sau 7–8, rồi cung cấp bản sách đầy đủ 138 trang. Đã đọc từng trang in 40–86 qua bản sách nhận trước/bản đọc NXB cùng bộ, đối chiếu bìa, mục lục và bốn trang mốc trong bản đầy đủ. Đường dẫn, hash, cách quy đổi trang và phạm vi đọc ghi tại [NOTES910](../../generator/math_volume2/NOTES910.md). Không đưa scan sách lên repo.

- Chủ đề 9: **Diện tích và thể tích của một số hình khối**, Bài 49–55, trang 40–63.
- Chủ đề 10: **Số đo thời gian, vận tốc và chuyển động đều**, Bài 56–62, trang 64–86.
- Mỗi chủ đề có tổng quan HTML/PNG, reader điện thoại, sáu đề/144 câu. Tổng 12 đề/288 câu tự soạn; mỗi đề 10 TB/8 Khá/6 Giỏi, 100 điểm, đủ bảy bài và bốn dạng mc/tf/fill/order. Các đề thay số liệu trong bộ dạng bài chung, không phải 288 dạng khác nhau.
- Hộp không nắp, mặt tiếp xúc, điều kiện vật chìm và cách xếp vừa từng chiều được ghi rõ. Thời gian đổi theo 60, chuẩn hóa phút/giây, qua ngày hôm sau, vận tốc lúc chạy trừ nghỉ; làm tròn theo yêu cầu. Không dạy công thức hình trụ hoặc chuyển động tương đối ngoài phần đã đọc.
- Toán: **10 chủ đề/60 đề/1440 câu**. Anh giữ **144 đề/3456 câu**. Toàn site: **204 đề/266 HTML/34 tổng quan HTML-PNG**.

## Cấu trúc và bảo toàn

Nguồn mới `topics910.py`, `overviews910.py` trong `generator/math_volume2/`; registry/build dùng chung. Thêm `cd9-deN`, `cd10-deN`, không đổi ID/schema cũ. Có lưu nháp, kết quả đã nộp, best/last, sao và xem lại trên cùng origin/trình duyệt.

Màu phụ chủ đề 9 tím hồng, chủ đề 10 xanh; khung hồng sáng giữ nguyên. Ảnh kiểm tra đã phát hiện chữ currentColor quá nhạt trên nền SVG trắng ở reader tối: bản cuối đặt màu mực tối riêng trong SVG tổng quan và có assertion kiểm cả hai theme. Không thay CSS toàn site.

Kiểm kê cho thấy các file site cũ chỉ đổi index chung, index Toán và catalog. Câu hỏi/wrapper cũ, toàn bộ HTML Anh và assets dùng chung giữ nguyên. Hai thay đổi có sẵn AGENTS.md và kế hoạch ôn Anh cả năm không nằm trong commit này.

## Kiểm chứng đang thực hiện

- Audit độc lập **288 câu**, đọc dữ kiện từ JS đã xuất và giải bằng Fraction; không gọi bộ giải generator. Kiểm hình khai triển bằng gấp 3D, sáu pháp tuyến khác nhau; kiểm ngược diện tích/thể tích, đổi đơn vị, thời gian và làm tròn: đạt.
- Toàn site: **204/204 đề đạt 100/100**, 266 HTML không lỗi trình duyệt; audit **60 Toán +144 Anh** đạt; **2252 tham chiếu** không lỗi.
- Hai trình duyệt Chromium/WebKit đã đạt 12/12 đề, từ chối nhầm diện tích/thể tích, hộp không nắp, đổi giờ/phút và thời gian nghỉ; nhận dấu phẩy, reload/xem lại giữ kết quả, reset cách ly.
- Profile Chromium đóng/mở thật: cd9-de1/cd10-de1 giữ đáp án/best/last/xem lại; Back, cross-tab, nháp và storage đầy đạt. Theme, home và nháp hồi quy đạt; audit và browser 7–8 vẫn đạt.
- Hai tổng quan đã kiểm lại bản cuối sau sửa tương phản: mỗi trình duyệt 32 bố cục (hai trang × tám chiều rộng × hai theme), đạt và chữ sơ đồ đọc rõ. Responsive toàn site đang chạy; CI và Pages thật chưa được coi là đạt ở bản ghi này.

Bằng chứng local ở artifacts/math910-local, math910-local-chromium, math910-local-webkit. Bản dựng cuối: artifacts/math910-build-final.log. CI tiếp tục giữ toàn bộ cổng Anh/audio/study cũ, thêm audit/browsers/persistence 9–10.

## Giới hạn và tiếp theo

Chưa cho học sinh làm thử hoặc kiểm trên iPad thật. Lưu theo thiết bị/trình duyệt/origin, chưa đồng bộ tài khoản. Đã có sách đầy đủ, nhưng chủ đề 11–12 chưa được giao triển khai trong đợt này.
