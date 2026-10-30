# 09 — Đặc tả Tiếng Anh 5 (Global Success, Sách học sinh tập 1)

Sách của chủ repo: `C:\LeDucLuong\Mia\tai_lieu\sach\SHS Tiếng anh 5 Global Success - Tập 1.pdf` (83 trang, bản **scan ảnh**, không có lớp chữ; nhà xuất bản Giáo dục Việt Nam & Macmillan Education). File này **không** nằm trong repo. Tập 2 chưa có.

## Mục lục (đọc từ trang "Book map", trang 4–5)
| Chủ đề (đề xuất) | Tên | Trang | Cấu trúc câu nổi bật (theo Book map) |
|---|---|---|---|
| E0 | Starter | 7 | Welcoming your classmates back to school; Talking about last summer; Following classroom instructions |
| E1 | Unit 1 – All about me! | 10 | Can you tell me about yourself? / I'm in… / I live in the… / What's your favourite…? |
| E2 | Unit 2 – Our homes | 16 | Do you live in this…? / What's your address? / It's… |
| E3 | Unit 3 – My foreign friends | 22 | What nationality…? / What's he/she like? / He's/She's… |
| E4 | Unit 4 – Our free-time activities | 28 | What does he/she do in his/her free time? / What do you do at the weekend? |
| E5 | Unit 5 – My future job | 34 | What would you like to be in the future? / I'd like to be a… / Why would you like to be a…? |
| E6 | Review 1 | 40 | Ôn Unit 1–5 |
| E7 | Unit 6 – Our school rooms | 44 | Where's the…? / It's on the… / Could you tell me the way to the computer room, please? |
| E8 | Unit 7 – Our favourite school activities | 50 | What school activity does he/she like? / Why does he/she like…? / Because he/she thinks… |
| E9 | Unit 8 – In our classroom | 56 | Where are the…? / They're… / Whose… is this? / It's… |
| E10 | Unit 9 – Our outdoor activities | 62 | Were you at the…? / Yes, we were. / What did you do yesterday? / We… |
| E11 | Unit 10 – Our school trip | 68 | Did they go to…? / Yes, they did. / What did you do on the trip? |
| E12 | Review 2 | 74 | Ôn Unit 6–10 |
| — | Wordlist | 78 | Từ vựng cuối sách (dùng làm nguồn từ, kiểm tra chính tả từng từ) |

Quyết định của chủ repo: **mỗi unit là một chủ đề**. Với Starter và hai bài Review: mặc định mỗi mục là một chủ đề riêng (E0, E6, E12); nếu thấy quá nhỏ có thể gộp Starter vào Unit 1, **hỏi chủ repo trước khi gộp**. Thứ tự hiển thị theo sách: Starter, U1–U5, Review 1, U6–U10, Review 2. Tổng 13 chủ đề × 6 đề = 78 đề.
Bảng trên chép từ Book map; **phải đọc lại từng trang unit** để lấy từ vựng/mẫu câu chính xác, vì Book map chỉ tóm tắt một phần (ví dụ danh sách từ vựng bị cắt).

## Cách đọc PDF scan
1. Render trang: `pdftoppm -r 110 -f 10 -l 15 -png "<đường dẫn PDF>" trang` rồi xem ảnh.
2. Có thể thử OCR (tesseract) nếu cài được, nhưng **luôn đối chiếu bằng mắt** với ảnh trang; không tin OCR 100%.
3. Ghi vào `generator/english/uNN/NOTES.md` (không chứa nguyên văn đoạn dài của sách): từ vựng, mẫu câu, chủ điểm, số trang. Chỉ ghi ý và từ khóa.

## Khung đề (giống Toán)
- Mỗi đề 24 câu = 10 `tb` (3đ) + 8 `kha` (5đ) + 6 `gioi` (5đ) = 100 điểm; xếp loại như `docs/04_QUY_CACH_DE.md`.
- 6 đề/chủ đề: Khởi động (từ vựng cơ bản của unit), 4 đề theo kỹ năng/bối cảnh (ví dụ: Từ vựng và hình ảnh; Mẫu câu và hội thoại; Đọc hiểu; Ngữ pháp và viết câu), 1 đề tổng hợp.
- Giao diện, bài hướng dẫn, nút, kết quả: **bằng tiếng Việt**; nội dung câu hỏi: tiếng Anh, có chú thích tiếng Việt khi cần.
- Mục tiêu theo sách: nghe, nói, đọc, viết. Trên web chỉ làm tốt đọc, viết (điền, sắp xếp, chọn), và nghe nếu kiểm chứng được giọng đọc.

## Dạng câu hỏi (text/match/reorder/pic đã có trong mẫu Unit 1)
| Dạng | Mô tả | Chấm |
|---|---|---|
| `text` | Điền từ/ chữ cái/ cả cụm | So khớp chuỗi, không phân biệt hoa thường, bỏ khoảng trắng thừa, chấp nhận danh sách đáp án thay thế |
| `match` | Nối cột trái với cột phải | Cặp đúng |
| `reorder` | Sắp xếp các từ thành câu đúng | So sánh thứ tự từ (khác dạng `order` số hiện có) |
| `pic` | Chọn đáp án theo tranh | Tranh là SVG/emoji tự vẽ; **không dùng hình trong sách** |
| `listen` (tùy chọn) | Nghe và chọn | Dùng Web Speech API (`speechSynthesis`) |
| `read` | Đọc đoạn ngắn rồi trả lời nhiều câu | Dùng `mc`/`tf` hiện có |

### Lưu ý rủi ro: câu nghe
Giọng đọc của trình duyệt phụ thuộc máy và trình duyệt của em (có thể không có giọng tiếng Anh, phát âm lạ, im lặng trên một số thiết bị). **Phải thử trên Chrome/Edge của chủ repo và trên điện thoại em dùng** trước khi đưa `listen` vào đề; luôn kèm văn bản hiển thị thay thế (nút "Xem chữ"). Nếu không ổn, bỏ câu nghe, **không hứa** là có.
Sách không có file âm thanh trong PDF (audio nằm trong ứng dụng Hoclieu qua QR); không sao chép audio sách.

## Nội dung đề
1. **Bám Book map và nội dung unit**; từ vựng và mẫu câu phải có trong sách. Không đưa ngữ pháp/từ vượt chương trình lớp 5.
2. **Tự soạn** câu, đoạn đọc, hội thoại; không chép đoạn của sách. Có thể dùng tên nhân vật trong sách (Mai, Nam, Linh, Ms Hoa, Mr Long, ...) vì chỉ là tên, nhưng không chép lời thoại.
3. Đáp án nhiễu hợp lý (sai thì, sai ngôi, sai giới từ...). Mỗi câu có `why` giải thích bằng tiếng Việt ngắn.
4. Câu `text` phải liệt kê đủ đáp án chấp nhận được (ví dụ viết tắt và viết đầy đủ: `I'm` / `I am`) và hỗ trợ dấu nháy thẳng/cong.
5. Phải có bộ kiểm tra tự động: `tall.js` điền đáp án đúng cho **mọi dạng** mới và đạt 100/100.

## Trang tổng quan Tiếng Anh
Cùng khung poster 1080px (`docs/05_THIET_KE.md`), thay công thức bằng: từ vựng chủ điểm (kèm tranh rõ chủ thể; theo docs/playbooks/TRANH_MINH_HOA.md), 3–5 mẫu câu hội thoại mẫu, mẹo nhớ, số trang sách; màu riêng cho từng chủ đề (không trùng 6 màu Toán, mở rộng bảng màu và ghi lại ở `05_THIET_KE.md`).

## Kế hoạch gốc và kết quả hiện tại
1. Chủ repo xác nhận kế hoạch/đã duyệt cây thư mục (`08`), rồi tham số hóa `build_all.py`/`gen_index.py`/`png.js` theo môn.
2. Làm **E1 (Unit 1)** trước làm mẫu: engine dạng mới + 6 đề + tổng quan, QA đầy đủ, **trình chủ repo xem**.
3. Chủ repo duyệt mẫu rồi mới làm các unit còn lại.
4. Cập nhật trang chủ gộp: Toán + Tiếng Anh.

## Mẫu Unit 1 đã thực hiện

Đã đọc từng trang in 10–15 (trang PDF 12–17), đối chiếu Wordlist 78–79, ghi ý chính ở `generator/english/u01/NOTES.md`. Có sáu đề: Khởi động; Từ vựng và hình ảnh; Mẫu câu và hội thoại; Đọc hiểu; Viết câu; Tổng hợp. Tổng 144 câu tự soạn, đúng khung 10/8/6. Hồ sơ dùng dữ liệu giả định chung để sinh câu hỏi/đáp án/lời giải; không lấy bài đọc hoặc tranh trong sách.

Nguồn: `generator/english/u01/content.py`. `gen_english.py` sinh wrapper, 6 JS đề, HTML tự chứa, tổng quan và trang chủ dùng chung thiết kế; build web tách assets như môn Toán. Không dựng `src/` riêng khi repo đã chốt giữ `generator/`.

Đã thêm engine chữ, nối, sắp từ, chọn theo hình, bài đọc. Sáu đề chính thức chưa tích hợp nghe/chấm nói; mẫu nghe riêng xem mục dưới. Khóa tiến độ là `mia5:en-u01-de1..6`; trang chủ/reset của Anh chỉ đọc/xóa khóa Anh. Chỉ có Unit 1 trên web, Starter/Review và Unit 2–10 vẫn chưa làm. Chủ repo đã xem mẫu và duyệt thay đủ sáu tranh theo mẫu cá heo ngày 30/10/2026; các unit tiếp theo chờ được giao. Luồng build và trang chủ gộp trong bước 1/4 của kế hoạch gốc đã hoàn tất.

## Mẫu nghe phân cấp (đã được giao làm thử ngày 30/10/2026)

Mẫu riêng 6 câu, mỗi cấp 2 câu: Trung bình một câu/thông tin trực tiếp; Khá hai câu/chọn thông tin; Giỏi đoạn 4 câu/kết hợp hai thông tin. Cùng giọng/tốc độ rõ cho mọi cấp (rate 0.9, nghe chậm 0.72), không tăng khó bằng đọc nhanh. Có nút chọn/thử giọng, dừng, nghe lại, xem lời nghe/nghĩa, chấm từng câu/cả mẫu. Hỗ trợ không bị trừ điểm. Chấm 8 ý; không nằm trong 24 câu/100 điểm và không làm đổi 6 đề cũ.

Giọng lấy từ Web Speech API, lọc tiếng Anh, chờ voiceschanged và có thông báo nếu thiếu giọng/lỗi/timeout. Không ghi âm/chấm nói, không sao chép audio sách. API trả giọng có sẵn trên thiết bị ([MDN getVoices](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis/getVoices)); tham số rate và các sự kiện theo [MDN SpeechSynthesisUtterance](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesisUtterance). Khả năng tự động kiểm tra hoạt động khác với nghe đánh giá chất lượng giọng; đợi chủ repo duyệt sau khi thử mẫu trước khi mở rộng.

## Sau khi duyệt mẫu: triển khai nghe toàn Unit 1

Chủ repo đã duyệt mẫu và giao áp dụng đủ 6 đề. Mỗi đề có 6 listen (2 mỗi cấp), giữ tổng 24 câu/100 điểm, khung 10/8/6. Hai cấp đầu chọn thông tin trực tiếp hoặc từ hai câu; cấp Giỏi nghe đoạn bốn câu và trả lời hai ý (chọn/điền). Nội dung các đề dùng dữ kiện phù hợp Unit 1, không tăng tốc độ để làm khó. Xem lời nghe trước nộp ghi đã dùng hỗ trợ, sau nộp tự mở. Giữ mẫu riêng để thử giọng. Chưa có chấm nói. Các ghi chú “mẫu chờ duyệt/chưa tích hợp” ở mục lịch sử phía trên mô tả giai đoạn trước triển khai này.
