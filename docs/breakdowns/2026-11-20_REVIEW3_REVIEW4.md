# Review 3 và Review 4 · ôn Tiếng Anh 5 tập hai

Giao việc ngày 20/11/2026: tiếp các phần ôn tập sau Unit 20. Thực hiện hai Review còn thiếu theo sách, không thêm Unit 21 hoặc tự coi Review là bộ kiểm tra giữa/cuối kỳ.

## Nguồn và phạm vi

- PDF tập hai ngoài repo: `C:\LeDucLuong\Mia\tai_lieu\sach\05-sgk-tieng-anh-5-global-success-tap-hai_268202616.pdf`; SHA256 `65e57b1193689e5a66f0ad9ce754388c6332d772c7d892c8f7b40660072713f9`, kiểm lại trong lượt này.
- Đã mở riêng tám trang: Review 3 trang in 36–39 / PDF 38–41; Review 4 trang in 70–73 / PDF 72–75. Render giữ ngoài repo tại `luu_tru/english-volume2-planning/reviews-NN.png`. Không đưa PDF/scan sách lên public.
- Review 3 ôn Units 11–15: chuyến đi gia đình, Tết, ngày đặc biệt, thói quen/tần suất, lời thoại sức khỏe. Extension nhóm thực phẩm riêng, không thay nội dung chính.
- Review 4 ôn Units 16–20: thời tiết/trang phục, truyện, phương tiện, cảm nhận/khoảng cách, kế hoạch hè. Extension thể loại truyện riêng.
- Viết mở khoảng 40 từ: Trung thu đã qua ở Review 3; kỳ nghỉ ở Review 4. Có gợi ý thực hành với người thân, chưa chấm bài luận hay nói.

## Sản phẩm

| | Review 3 | Review 4 |
|---|---|---|
| Nguồn | `generator/english/r03/` | `generator/english/r04/` |
| Web | `TiengAnh5/Review3_Units11_15/` | `TiengAnh5/Review4_Units16_20/` |
| Tổng quan | `TongQuan_Review3.html/.png` | `TongQuan_Review4.html/.png` |
| Trang học | `HocTuVaPhatAm.html` | `HocTuVaPhatAm.html` |
| Đề/câu/nghe | 6/144/36 | 6/144/36 |
| Học từ/hội thoại/luyện | 18/6/12 | 18/6/12 |
| WAV | 105 / 15.125.250 byte | 102 / 14.582.164 byte |
| ID đề | `en-r03-deN-v1` | `en-r04-deN-v1` |
| Khóa học | `mia5:learn:en-r03-v1` | `mia5:learn:en-r04-v1` |

Mỗi đề 24 câu, 100 điểm, 10 trung bình/8 khá/6 giỏi; hai câu nghe mỗi cấp. Mỗi câu khai báo `sourceUnits`; mỗi đề đủ đúng năm Unit trong phạm vi. Bài đọc/lời nghe/hội thoại tự soạn; dữ kiện giả định, lời khuyên theo role-play, không suy triệu chứng thành đáp án chữa bệnh. Câu tự chấm nêu rõ mở đầu/thứ tự; giữ nhận viết tắt thông thường, yêu cầu full form kiểm riêng.

Học từ có phát thường/chậm, ABC tên chữ cái, ví dụ, hội thoại và lượt em đáp, đánh dấu cần ôn, 12 bài tự lưu. Audio file ưu tiên, vẫn phát khi không có giọng hệ thống/Speech API; không yêu cầu cài voice trên iPad. Không tự phát hoặc ghi âm. Kiểm chứng bằng trình duyệt không thay cho người nghe duyệt hoặc thử iPad thật.

Tái dùng tám tranh từ Units 11/12/13/14 và 17/18/19/20, đã xem lại ảnh nguồn và bản poster; nguồn/prompt tại Unit gốc, chi tiết NOTES của Review. Audit chỉ cho đúng tám nguồn, không mở quyền ảnh tùy ý.

## Tích hợp

Registry xếp Review 3 sau Unit 15, Review 4 sau Unit 20. Tổng Anh 20 Unit + 4 Review = **144 đề/3456 câu**; toàn site **180 đề/238 HTML/30 tổng quan HTML-PNG**. Study đầy đủ **23 trang/372 từ-cụm/139 hội thoại/276 bài/552 layout**; Unit 1 vẫn mẫu nghe.

Build trích audio theo cả Unit và Review; mở tác giả/QA audio để chọn R3/R4. Không đổi engine, storage schema hoặc ID/câu hỏi/đáp án cũ. Các thay đổi site cũ chỉ index Anh, trang chọn môn và catalog. Toán giữ nguyên.

## Kiểm chứng

Đã hoàn tất local, CI và kiểm tra Pages thật; kết quả và thời điểm xác nhận ở các mục cuối. Log local ở `artifacts/reviews34-local/`, runner hai Review ở `artifacts/topics-r03-r04-local/`; audio ở `artifacts/unitR3-local[-webkit]/` và `unitR4-local[-webkit]/`. Báo cáo phân biệt bản nguồn, kiểm tra local, CI và Pages thật.

## Bài học đã áp dụng

- Không mặc định mọi Review sau R1 là Units 6–10; scope tính đúng theo số Review, mỗi câu phải có tag.
- Giữ yêu cầu ít nhất bốn kiểu câu. Audit đầu tiên phát hiện đề đọc của cả hai Review chỉ có ba kiểu; đã thêm chọn đáp án vào bài đọc trước lần build cuối, giữ gate nguyên.
- Hàm ảnh Unit 18 nhận `by bus`, khác tên asset `bus`; gọi đúng API khi tái dùng. Lỗi tác giả phát hiện trước build, không đổi nội dung Unit cũ.
- File nghe cần hỗ trợ đường dẫn `ReviewN_…` trong bước trích WAV. Kiểm từ manifest đến byte web, không chỉ nút nghe sáng lên.
- Rà theo mẫu câu, không chỉ nhìn tag năm Unit: bổ sung nơi đến dịp Tết, hoạt động ngày đặc biệt và nơi tham quan mùa hè vào đề; giữ nơi muốn đến trên bản đồ khác nơi dự định hè. QA có ca trả lời hoạt động thay nơi đến và trả lời nơi trên bản đồ thay nơi hè để kiểm đúng kỹ năng.

## Còn lại ngoài đợt

Starter tập một; nâng Unit 1 thành study đầy đủ; bốn bộ kiểm tra giữa HK1/cuối HK1/giữa HK2/cuối HK2 riêng; thay audio tập một; đồng bộ thiết bị/tài khoản; thu âm/chấm nói. Đã hoàn thành các Unit/Review không có nghĩa đã có đủ những mục này. Bé từng được báo đang học Unit 3; không mặc định Review 3–4 là phần cần làm ngay.


## Kiểm chứng local của bản tính năng

- Build sạch từ nguồn: `node tools/build.js --regenerate`, đủ 30 PNG. Audit Toán 36 đề + Anh 144 đề/3456 câu, không lỗi. 2060 tham chiếu đúng hoa/thường.
- Toàn site: **180/180 đề đạt 100/100**, 238 HTML không lỗi trình duyệt; sai/điểm phần/biến thể/reset cách ly đạt. **3808** tổ hợp trang/kích thước/theme không tràn ngang. Theme 238 trang và trang chủ 10 trường hợp đạt.
- Runner riêng: 12 đề mới/72 nghe, full form/did + take/be going to/on foot, nháp/best/điểm phần/tổng/reset/standalone đạt. Hồi quy Unit 10 + Review 1–2 thêm 18 đề/108 nghe đạt với bộ QA đã mở rộng.
- Persistence dùng hồ sơ trình duyệt trên đĩa: đóng/mở lại, đáp án đã nộp/xem lại, best/last, Back và cập nhật giữa tab đều đạt cho cả hai Review.
- Study: 36 từ, 12 hội thoại, 24 bài, lưu đáp án sau đóng/mở, sửa signature chỉ xóa câu liên quan, khóa cách ly, blocked storage/no voice, 48 layout đạt. Phần này mô phỏng giọng.
- Audio thật: Chromium và WebKit mỗi trình duyệt đều kiểm đủ 105+102 WAV, giải mã/metadata và PCM không im lặng; phát trên app không Speech API, native constructor, thường/chậm, ABC, hủy hàng đợi, đổi nhóm, lỗi/thử lại và ba cấp nghe đề. Chromium standalone phát đạt; Windows WebKit chỉ xác nhận nhúng đủ audio, chưa phát file URL. Pagehide được kiểm tra cho việc lưu nháp study; chưa có assertion riêng về dừng audio đang phát khi pagehide.
- Đã xem tám ảnh nguồn, tám thẻ câu hỏi điện thoại, hai poster, hai reader điện thoại, study sáng/tối. Source inventory đúng 207 WAV/29.707.414 byte; file hash theo text, đúng manifest, không clip thừa.
- Mười nhóm local exit 0; bằng chứng `qa-results.json`, `source-inventory.json`, log từng nhóm và bản sao study/audio-batch trong `artifacts/reviews34-local/`. Chưa coi local là CI hoặc Pages; chưa nghe duyệt bằng tai hay thử iPad của bé.


## CI và Pages đã xác nhận

Xác nhận hoàn tất: **2026-11-20T13:35:55+07:00**. Commit tính năng `52cee0c85557288c225133599bccc8235a256773`. [Actions 44642906838](https://github.com/Okeydokey8525/Lop_5_Mia/actions/runs/44642906838), attempt 1, build và deploy đều success trên đúng commit. Pages triển khai lúc 07:32 ngày 20/11/2026 (UTC+7).

CI chạy lại toàn bộ nguồn và gate: 180/180 đề đạt 100/100, 238 HTML, 2060 tham chiếu đúng, 3808 trường hợp responsive; 23 trang study với 372 từ-cụm/139 hội thoại/276 bài/552 layout; 24 gate audio thật (Units 11–20 và Review 3–4 × Chromium/WebKit), gồm đủ 105 và 102 clip của hai Review. Log `artifacts/reviews34-online/ci-run.log`, trạng thái/head/job tại `ci.json`.

Kiểm tra trên HTTPS Pages:

- **237 tài nguyên khớp byte** bản nguồn: 16 HTML hai Review, 207 WAV, tám tranh tái dùng và sáu tài nguyên chung/index/catalog. PNG không so byte giữa Windows/Linux vì môi trường font/render khác nhau.
- 12/12 đề mới đạt 100/100; đủ 72 câu nghe; nháp/điểm phần/best/reset cách ly, full form và phân biệt hoạt động/nơi đến, nơi trên bản đồ/nơi dự định hè đều đạt. Phần chức năng này mô phỏng giọng; gate audio bên dưới dùng phát thật.
- Hồ sơ trình duyệt trên đĩa đóng/mở lại giữ đáp án, xem lại bài đã nộp, best/last; Back và cập nhật giữa tab đạt.
- Study 36 từ/12 hội thoại/24 bài/48 layout; lưu sau đóng/mở, signature guard, cách ly khóa và tình huống giọng/storage bị chặn đạt (giọng mô phỏng).
- Audio thật: cả Chromium lẫn WebKit đều đạt toàn bộ 105+102 clip, không Speech API, giải mã/PCM có âm thanh, phát thường/chậm, ABC, hủy hàng đợi/đổi nhóm, lỗi/thử lại và nghe đề ba mức.

Bằng chứng tổng hợp: `artifacts/reviews34-online/release.json`, `assets.json`, `study-report.json`, `audio-batch-report.json`, log reviews/persistence/study/audio và `artifacts/unitR3-online[-webkit]/audio-report.json`, `unitR4-online[-webkit]/audio-report.json`. Phiên trước bị ngắt khi CI đang chạy, chưa nghiệm thu online; lượt tiếp đã xác nhận CI xong và chạy lại nghiệm thu từ đầu. Không có sửa runtime hoặc giảm gate sau commit tính năng.

Đường dẫn:

- [Review 3 · Units 11–15](https://okeydokey8525.github.io/Lop_5_Mia/TiengAnh5/Review3_Units11_15/TongQuan_Review3.html)
- [Review 4 · Units 16–20](https://okeydokey8525.github.io/Lop_5_Mia/TiengAnh5/Review4_Units16_20/TongQuan_Review4.html)

Chưa nghe duyệt bằng tai, chưa có kết quả từ chính iPad của bé, chưa chấm phát âm/bài luận. Tiến độ vẫn theo cùng origin/thiết bị/trình duyệt; không đồng bộ tài khoản. Starter và bốn bộ kiểm tra giữa/cuối kỳ riêng vẫn ngoài đợt này.
