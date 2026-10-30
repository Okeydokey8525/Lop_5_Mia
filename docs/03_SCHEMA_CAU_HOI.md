# 03 — Schema câu hỏi (engine hiện tại)

Mỗi đề là mảng 24 câu truyền vào `MKn([...])`. Trường chung: `level` (`tb`|`kha`|`gioi`), `lesson` (số bài, tra trong `lessons` của `common/cdN.js`), `type`, `stem`, `why` (lời giải), `fig` (HTML/SVG tùy chọn).

## Bốn dạng câu hiện có
| `type` | Trường riêng | Ghi chú |
|---|---|---|
| `mc` | `opts` (đúng 4, không trùng), `answer` (chỉ số 0–3) | Trắc nghiệm |
| `tf` | `items: [{t:'câu', a:true/false}, ...]` | Đúng/Sai nhiều ý; tạo bằng `tf(lv,ls,stem,[(text,True/False),...],why)` |
| `fill` | `blanks: [...]` | Điền nhiều ô, mỗi ô có `pre`, `kind`, `ans`, `post` |
| `order` | `items`, `sep` (`<` hoặc `>`) | Sắp xếp theo thứ tự đáp án khai báo trong `items`; có thể là số, số đo, phép tính hoặc nhãn theo bảng |

### Các `kind` của ô điền (`fill`)
- `num`: số (`ans` kiểu số thực). Với `decimal:true`, nhập `,` hoặc `.` đều được, dung sai 1e-9.
- `frac`: phân số `ans=[tử,mẫu]`. `reduced:true` bắt buộc tối giản, mặc định chấp nhận phân số bằng nhau.
- `mixed`: hỗn số `ans=[phần nguyên, tử, mẫu]`.
- `sel`: chọn trong `opts` (`>`, `<`, `=`), `ans` là ký hiệu đúng.

## Phân số trong chữ
`{a/b}` và `{w a/b}` (hỗn số) vẽ thành phân số; dùng được trong `stem`, `opts`, `pre`, `post`, `items`.

## Số kiểu Việt Nam
Dùng `n(x)` trong `g4lib.py`: dấu phẩy thập phân, nhóm nghìn bằng khoảng trắng không ngắt. Không tự định dạng số bằng tay.

## Hình vẽ
`fig` là HTML với `<div class="fig"><figure><svg ...>...</svg><figcaption>...</figcaption></figure></div>`. Màu dùng biến của chủ đề (`var(--soft)`, `currentColor`) và màu nhấn `#e8741a`. Thư viện `fig_tri`, `fig_trap`, `fig_circ`, `fig_house`, `fig_pond` trong `g5lib.py`; `H.angles/table/rect/numline` trong `engine.js`.

## Các dạng Tiếng Anh đã có

| `type` | Trường | Cách chấm |
|---|---|---|
| `text` | `answers: string[]`, `exactForm: boolean` | Một ô chữ, so với danh sách đáp án sau chuẩn hóa |
| `match` | `pairs: [{left,right}]` | Ô chọn ở mỗi dòng; phương án đảo thứ tự; điểm theo tỷ lệ cặp đúng |
| `reorder` | `items` theo thứ tự đúng | Bấm từng từ; chấm thứ tự từ, không dùng so sánh số |
| `pic` | `fig` SVG tự vẽ, `opts`, `answer` | Chấm như `mc` |

`passage` là hồ sơ/bài đọc tự soạn, có thể đi kèm mọi dạng. Các câu liên tiếp dùng chung bài đọc trong cùng mức độ chỉ hiển thị bài một lần; các câu sau có liên kết xem lại đúng bài. QA đối chiếu bài hiển thị/tham chiếu với dữ liệu từng câu.

Ô chữ chuẩn hóa NFKC, hoa/thường, nháy cong/thẳng, khoảng trắng và dấu kết câu; chấp nhận colour/color và favourite/favorite. Các dạng I'm/I am, It's/It is, What's/What is, My name's/My name is và don't/do not tương đương, **trừ khi** câu đặt `exactForm:true` để yêu cầu viết dạng đầy đủ. Không bỏ qua từ thừa hoặc sửa chính tả theo suy đoán.

`lesson` của Anh dùng 1/2/3 theo ba phần đã đọc; wrapper đặt `meta.subject='en'`, `lessonLabel='Phần'`. Câu nghe chưa triển khai. Sau khi sửa engine phải chạy lại cả Toán và Anh.

## Kiểm tra dạng sắp xếp

Engine so sánh thứ tự chỉ số, không tự tính giá trị của chuỗi. `items` phải được khai báo theo đáp án đúng; thứ tự hiển thị được xáo trước khi làm. `generator/audit_order.js` tính độc lập giá trị số, phân số, số đo, phép tính và diện tích/chu vi của các mẫu đang dùng; câu sắp tên học sinh được đối chiếu bảng chiều cao. Mẫu chưa được hỗ trợ phải báo lỗi để bổ sung validator, không tự bỏ qua.

## listen — câu nghe trong Unit 1 phiên bản 2

`type: 'listen'`, `speech` (lời đọc), `transcript` (lời nghe hiển thị), `fields: [{label, answer, options: [...]/null, alternatives: [...]}]`. Có thể có fig minh họa. Mỗi field được chấm một phần bằng nhau của điểm câu; ví dụ 1/2 ý của câu 5 điểm = 2,5 điểm. Cùng dữ kiện sinh lời nghe và đáp án, không gõ hai nguồn độc lập. Lớp 5A có thể đọc thành “Class five A” nhưng transcript vẫn là “Class 5A”.

Engine dùng speech.js chỉ khi có câu listen. Lời nghe ẩn trước nộp, mở thủ công ghi supportUsed; sau nộp tự mở. Replay sau nộp được phép, các ô trả lời khóa. Làm lại reset hỗ trợ và giải phóng speech controller cũ. ID đề Anh đổi hậu tố -v2; bản cũ giữ trong localStorage và không được cộng vào thống kê bản mới.

## Nhập phân số/hỗn số

Tử, mẫu và phần nguyên chỉ nhận toàn bộ chuỗi chữ số sau khi trim; tử/phần nguyên không âm, mẫu lớn hơn 0. Từ chối phần thập phân, dấu phẩy, ký tự dư, số mũ và số vượt Number.MAX_SAFE_INTEGER. Ô phần nguyên để trống vẫn hiểu là 0 theo quy ước cũ. So sánh chéo bằng BigInt để không mất chính xác ở tích lớn; điều kiện tối giản/đúng dạng vẫn giữ nguyên. Không đổi quy ước ô số thập phân hoặc định dạng số nguyên thông thường của dạng num.
