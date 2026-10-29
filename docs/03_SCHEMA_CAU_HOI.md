# 03 — Schema câu hỏi (engine hiện tại)

Mỗi đề là mảng 24 câu truyền vào `MKn([...])`. Trường chung: `level` (`tb`|`kha`|`gioi`), `lesson` (số bài, tra trong `lessons` của `common/cdN.js`), `type`, `stem`, `why` (lời giải), `fig` (HTML/SVG tùy chọn).

## Bốn dạng câu hiện có
| `type` | Trường riêng | Ghi chú |
|---|---|---|
| `mc` | `opts` (đúng 4, không trùng), `answer` (chỉ số 0–3) | Trắc nghiệm |
| `tf` | `items: [{t:'câu', a:true/false}, ...]` | Đúng/Sai nhiều ý; tạo bằng `tf(lv,ls,stem,[(text,True/False),...],why)` |
| `fill` | `blanks: [...]` | Điền nhiều ô, mỗi ô có `pre`, `kind`, `ans`, `post` |
| `order` | `items`, `sep` (`<` hoặc `>`) | Sắp xếp số; engine so sánh số nên `items` phải là số hợp lệ |

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

## Mở rộng cho Tiếng Anh (chưa có, cần làm)
Engine chưa có: ô điền chữ (so khớp chuỗi), nối cặp, sắp xếp từ thành câu, chọn tranh, câu nghe. Xem `docs/09_TIENG_ANH.md`. Khi thêm dạng mới: thêm vào `engine.js`, thêm `audit.js` và `tall.js` hỗ trợ dạng đó (tự điền đáp án đúng), **không làm hỏng các dạng cũ** (chạy lại QA 36 đề Toán).
