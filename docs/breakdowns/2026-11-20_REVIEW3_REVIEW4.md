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

Đang kiểm chứng. Log local ở `artifacts/reviews34-local/`, runner hai Review ở `artifacts/topics-r03-r04-local/`; audio ở `artifacts/unitR3-local[-webkit]/` và `unitR4-local[-webkit]/`. Sẽ ghi kết quả thực chạy, commit/CI và địa chỉ Pages sau khi đạt; chưa coi nguồn đã viết là đã xuất bản.

## Bài học đã áp dụng

- Không mặc định mọi Review sau R1 là Units 6–10; scope tính đúng theo số Review, mỗi câu phải có tag.
- Giữ yêu cầu ít nhất bốn kiểu câu. Audit đầu tiên phát hiện đề đọc của cả hai Review chỉ có ba kiểu; đã thêm chọn đáp án vào bài đọc trước lần build cuối, giữ gate nguyên.
- Hàm ảnh Unit 18 nhận `by bus`, khác tên asset `bus`; gọi đúng API khi tái dùng. Lỗi tác giả phát hiện trước build, không đổi nội dung Unit cũ.
- File nghe cần hỗ trợ đường dẫn `ReviewN_…` trong bước trích WAV. Kiểm từ manifest đến byte web, không chỉ nút nghe sáng lên.
- Rà theo mẫu câu, không chỉ nhìn tag năm Unit: bổ sung nơi đến dịp Tết, hoạt động ngày đặc biệt và nơi tham quan mùa hè vào đề; giữ nơi muốn đến trên bản đồ khác nơi dự định hè. QA có ca trả lời hoạt động thay nơi đến và trả lời nơi trên bản đồ thay nơi hè để kiểm đúng kỹ năng.

## Còn lại ngoài đợt

Starter tập một; nâng Unit 1 thành study đầy đủ; bốn bộ kiểm tra giữa HK1/cuối HK1/giữa HK2/cuối HK2 riêng; thay audio tập một; đồng bộ thiết bị/tài khoản; thu âm/chấm nói. Đã hoàn thành các Unit/Review không có nghĩa đã có đủ những mục này. Bé từng được báo đang học Unit 3; không mặc định Review 3–4 là phần cần làm ngay.
