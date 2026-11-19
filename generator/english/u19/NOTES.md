# Unit 19 — Places of interest

Đã xem đủ trang in 58–63 (PDF 60–65), Global Success 5 tập hai, ngày 19/11/2026. Nguồn ngoài repo: `05-sgk-tieng-anh-5-global-success-tap-hai_268202616.pdf`, SHA256 `65e57b1193689e5a66f0ad9ce754388c6332d772c7d892c8f7b40660072713f9` đã kiểm lại. Scan giữ ngoài public repo.

## Phạm vi sách

- Lesson 1, 58–59: What do you think of…? I think it’s/they’re…; peaceful, exciting, beautiful, fantastic. Ban Gioc Waterfall, Hoi An Old Town, Sydney Opera House, Petronas Twin Towers; phần luyện có Ba Be Lake, Huong Pagoda, Mui Ne Beach; bài hát nhắc Ba Na Hills, Dau Go Cave.
- Lesson 2, 60–61: How far is it from…to…? It’s about…kilometres; địa danh/cặp thành phố và số, đọc sơ đồ, cộng hai chặng trên cùng tuyến. Không sao chép các khoảng cách địa lý thành dữ kiện mới không có nguồn.
- Lesson 3, 62–63: ngữ điệu xuống ở câu hỏi Wh; bài đọc Sentosa Island tìm place/transport/activities/food/hotel; viết dream holiday khoảng 40 từ theo sáu gợi ý và project giới thiệu nơi muốn đến.

## Quyết định nội dung

Sáu đề tự soạn, 24 câu/100 điểm, 10 TB/8 Khá/6 Giỏi; sáu nghe mỗi đề, hai mỗi cấp. Nghe TB một dữ kiện; Khá có câu hỏi/bối cảnh; Giỏi hai dữ kiện và phân biệt hai người. Thẻ và khoảng cách từ trường giả định ghi rõ là imaginary, không tuyên bố trường hay tuyến đường thực. Cùng nơi có thể khác cảm nhận và khác điểm xuất phát. Cộng 3+4 chỉ khi đề nêu cùng tuyến school → museum → lake, không suy quãng đường thẳng.

It is cho một địa điểm; they are cho Petronas Twin Towers. Think of; How far is it from…to…? One kilometre, số nhiều kilometres. Full form không nhận it's/they're; dạng thông thường cho phép rút gọn tương đương. Viết tự chấm có mở đầu, thứ tự và dữ kiện; gợi ý bài 40 từ trên tổng quan để luyện cùng người lớn, không giả vờ chấm luận tự do/nói bằng máy.

Study 20 từ/cụm, ba nhóm places 8/opinions 6/distance 6, sáu hội thoại, 12 bài luyện, bốn mỗi nhóm. Distance là từ giải thích chức năng How far. ABC là tên chữ cái, không phải phonics. Bốn tranh generic waterfall/lake/cave/old town; không buộc nhận tên địa danh cụ thể hoặc đoán tính từ chủ quan từ tranh.

ID `en-u19-deN-v1`, khóa học `mia5:learn:en-u19-v1`; không đổi các ID/đáp án/tiến độ cũ. Nguồn tranh/prompt ở `images/PROMPTS.md`; PNG gốc giữ ngoài repo. Không chép scan, song/chant, đoạn đọc hoặc audio gốc sách.

## Audio và kiểm chứng

104 WAV, 14,977,248 byte, Microsoft Zira Desktop en-US rate -1, PCM16 mono 22050Hz; ABC dùng SpellOut. Tạo manifest từ generator: `python -m english.u19.audio_source`; tạo WAV từ root: `powershell -File tools/generate_english_audio.ps1 -Unit u19`. Build thường/CI dùng WAV đã lưu, iPad không cần cài giọng Windows.

Giữ runtime dùng một AudioElement, dừng/đổi nhóm/pagehide/lỗi-thử lại, không autoplay. QA đủ file/PCM/peak/duration/timeout và thao tác phát thật trên Chromium/WebKit; speech mô phỏng được ghi riêng. Không coi WebKit trên Windows là iPad của bé. Chưa người duyệt phát âm bằng tai; chưa kiểm thiết bị thật. WebKit Windows fileURL/WAV dataURI chưa xác nhận phát, Chromium standalone kiểm thực tế.

Trạng thái nghiệm thu và bằng chứng ở `docs/breakdowns/2026-11-19_UNIT19.md`.
