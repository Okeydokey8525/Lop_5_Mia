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

## Kiểm chứng local

- Audit độc lập **288 câu**, đọc dữ kiện từ JS đã xuất và giải bằng Fraction; không gọi bộ giải generator. Kiểm hình khai triển bằng gấp 3D, sáu pháp tuyến khác nhau; kiểm ngược diện tích/thể tích, đổi đơn vị, thời gian và làm tròn: đạt.
- Toàn site: **204/204 đề đạt 100/100**, 266 HTML không lỗi trình duyệt; audit **60 Toán +144 Anh** đạt; **2252 tham chiếu** không lỗi.
- Hai trình duyệt Chromium/WebKit đã đạt 12/12 đề, từ chối nhầm diện tích/thể tích, hộp không nắp, đổi giờ/phút và thời gian nghỉ; nhận dấu phẩy, reload/xem lại giữ kết quả, reset cách ly.
- Profile Chromium đóng/mở thật: cd9-de1/cd10-de1 giữ đáp án/best/last/xem lại; Back, cross-tab, nháp và storage đầy đạt. Theme, home và nháp hồi quy đạt; audit và browser 7–8 vẫn đạt.
- Hai tổng quan đã kiểm lại bản cuối sau sửa tương phản: mỗi trình duyệt 32 bố cục (hai trang × tám chiều rộng × hai theme), đạt và chữ sơ đồ đọc rõ. Responsive toàn site đạt 4256 tổ hợp; 13 nhóm local đều đạt. CI và Pages thật đã hoàn tất, xem phần xuất bản bên dưới.

Bằng chứng local ở artifacts/math910-local, math910-local-chromium, math910-local-webkit. Bản dựng cuối: artifacts/math910-build-final.log. CI tiếp tục giữ toàn bộ cổng Anh/audio/study cũ, thêm audit/browsers/persistence 9–10.

## Giới hạn và tiếp theo

Chưa cho học sinh làm thử hoặc kiểm trên iPad thật. Lưu theo thiết bị/trình duyệt/origin, chưa đồng bộ tài khoản. Đã có sách đầy đủ, nhưng chủ đề 11–12 chưa được giao triển khai trong đợt này.


## Xuất bản và kiểm chứng web thật

- Hoàn tất 2026-11-20T20:11:05+07:00. Commit tính năng `479c3e53fabce4654953d12c2dd2406372c51205`; [Actions 44736105247](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/44736105247), attempt 2: build và deploy đều success.
- Lượt 1 chủ động dừng sau hơn 10 phút tải gói hệ thống rất chậm, trước bước build/QA. Đã giữ log ci-attempt1.log; lượt 2 chạy lại cùng commit và toàn bộ cổng kiểm tra, không bỏ bước hoặc sửa nguồn để vượt cổng.
- CI Linux dựng lại từ nguồn, audit độc lập 288 câu mới, toàn site 204/204 đề và 4256 bố cục; hai trình duyệt cho 12 đề mới, 32 bố cục tổng quan mỗi trình duyệt, kiểm lưu bài 9–10 và toàn bộ cổng Anh/audio/study cũ đều đạt.
- HTTPS thật: 28 tài nguyên khớp byte bản local (14 HTML mới, index/catalog, một đề Toán cũ và assets chung); hai PNG giải mã được, rộng 1080px. Không so byte PNG giữa Windows/Linux. Số lần tải lại do lỗi mạng: 0.
- Chromium và WebKit: 12/12 đề đạt 100/100, từ chối đáp án sai điển hình, dấu phẩy, lưu/xem lại, 32 bố cục tổng quan không tràn và mực sơ đồ đọc rõ ở cả hai theme. Trang chọn môn cập nhật đúng 60 đề Toán và tiến độ.
- Profile Chromium trên origin HTTPS đóng/mở thật: giữ đáp án/best/last/xem lại không tăng lượt, Back/cross-tab/nháp/storage đầy đạt. Dùng profile QA riêng, không đụng dữ liệu của bé.
- Bằng chứng: artifacts/math910-online/release.json, ci.json, ci-run.log, assets.json, chromium-report.json, webkit-report.json, persistence-report.json và log từng nhóm. Ảnh ở math910-online-chromium/-webkit. Local có qa-results.json, final-manifest.json, source-inventory.json, các report full/responsive/persistence và chromium/webkit-report-final.json.
- Chưa kiểm iPad thật hoặc xác nhận độ khó bằng học sinh. Lưu vẫn theo trình duyệt/thiết bị/origin.

Địa chỉ:

- https://okeydokey8525.github.io/Lop_5_Mia/Toan5/ChuDe9_DienTichVaTheTichHinhKhoi/TongQuan_ChuDe9.html
- https://okeydokey8525.github.io/Lop_5_Mia/Toan5/ChuDe10_ThoiGianVaChuyenDong/TongQuan_ChuDe10.html
