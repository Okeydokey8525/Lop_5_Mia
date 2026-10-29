# 09 — Đặc tả Tiếng Anh 5 (Global Success, Sách học sinh tập 1)

Sách của chủ repo: `C:\LeDucLuong\Mia\SHS Tiếng anh 5 Global Success - Tập 1.pdf` (83 trang, bản **scan ảnh**, không có lớp chữ; nhà xuất bản Giáo dục Việt Nam & Macmillan Education). File này **không** nằm trong repo. Tập 2 chưa có.

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
3. Ghi vào `src/tieng-anh/uNN/NOTES.md` (không chứa nguyên văn đoạn dài của sách): từ vựng, mẫu câu, chủ điểm, số trang. Chỉ ghi ý và từ khóa.

## Khung đề (giống Toán)
- Mỗi đề 24 câu = 10 `tb` (3đ) + 8 `kha` (5đ) + 6 `gioi` (5đ) = 100 điểm; xếp loại như `docs/04_QUY_CACH_DE.md`.
- 6 đề/chủ đề: Khởi động (từ vựng cơ bản của unit), 4 đề theo kỹ năng/bối cảnh (ví dụ: Từ vựng và hình ảnh; Mẫu câu và hội thoại; Đọc hiểu; Ngữ pháp và viết câu), 1 đề tổng hợp.
- Giao diện, bài hướng dẫn, nút, kết quả: **bằng tiếng Việt**; nội dung câu hỏi: tiếng Anh, có chú thích tiếng Việt khi cần.
- Mục tiêu theo sách: nghe, nói, đọc, viết. Trên web chỉ làm tốt đọc, viết (điền, sắp xếp, chọn), và nghe nếu kiểm chứng được giọng đọc.

## Dạng câu hỏi mới cần thêm vào engine
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
Cùng khung poster 1080px (`docs/05_THIET_KE.md`), thay công thức bằng: từ vựng chủ điểm (kèm hình SVG tự vẽ), 3–5 mẫu câu hội thoại mẫu, mẹo nhớ, số trang sách; màu riêng cho từng chủ đề (không trùng 6 màu Toán, mở rộng bảng màu và ghi lại ở `05_THIET_KE.md`).

## Việc cần làm (thứ tự)
1. Chủ repo xác nhận kế hoạch/đã duyệt cây thư mục (`08`), rồi tham số hóa `build_all.py`/`gen_index.py`/`png.js` theo môn.
2. Làm **E1 (Unit 1)** trước làm mẫu: engine dạng mới + 6 đề + tổng quan, QA đầy đủ, **trình chủ repo xem**.
3. Chủ repo duyệt mẫu rồi mới làm các unit còn lại.
4. Cập nhật trang chủ gộp: Toán + Tiếng Anh.
