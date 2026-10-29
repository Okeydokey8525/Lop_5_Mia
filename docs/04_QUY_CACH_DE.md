# 04 — Quy cách mỗi đề

## Khung chung (Toán đang dùng; Tiếng Anh dùng cùng khung)
- **24 câu**: 10 Trung bình (`tb`, 3 điểm), 8 Khá (`kha`, 5 điểm), 6 Giỏi (`gioi`, 5 điểm). Tổng **100 điểm**. Thứ tự trong đề: tb → kha → gioi.
- `g4lib.write()` kiểm tra (assert) số câu và thứ tự mức độ; đề sai khung sẽ không ghi được.
- Xếp loại theo phần trăm: **Giỏi ≥ 80**, **Khá ≥ 60**, **Trung bình ≥ 40**, dưới 40: "Cần cố gắng thêm".
- Thời gian gợi ý: 40 phút (`minutes` trong `common/cdN.js`).
- Mỗi chủ đề: 1 trang tổng quan + **6 đề**: (1) *Khởi động* (tổng hợp, làm nóng), (2–5) bốn đề theo bối cảnh thực tế, (6) đề tổng hợp nhiều bước.
- Mỗi câu có `why`: lời giải ngắn, đúng, ghi phép tính; câu sai thường gặp có ghi chú lỗi hay mắc.

## Chất lượng câu hỏi
1. **Đa dạng dạng câu** trong một đề (trắc nghiệm, đúng/sai, điền, sắp xếp, có hình, có bảng), không lặp một mẫu 10 lần.
2. **Thực tế, gần gũi lớp 5**: lớp học, chợ, bếp, thể thao, du lịch, thiên nhiên. Tránh ngữ cảnh khó hiểu hay nhạy cảm.
3. Mức Giỏi: nhiều bước, có tìm số chưa biết, tiền, đổi đơn vị; vẫn phải **giải được trong chương trình lớp 5**.
4. Câu trắc nghiệm: 3 đáp án nhiễu đều phải có lý do sai hợp lý (sai đơn vị, quên chia 2, nhầm công thức...), không được hai đáp án cùng đúng.
5. Số liệu thực tế hợp lý (chiều cao người, giá tiền, tuổi...), không đặt số vô lý cho đẹp phép tính.
6. Không chép nguyên văn sách. Có thể bám dạng bài, nhưng số liệu và tình huống **tự soạn**.

## Văn phong (học sinh lớp 5)
- Câu ngắn, rõ ràng; không dùng từ Hán-Việt khó khi có từ thông thường.
- Không dùng ký hiệu em chưa học. Dấu phẩy thập phân kiểu Việt Nam (3,5).
- Lời giải thân thiện, không quở trách.

## Trang tổng quan
Mỗi chủ đề có một poster 1080px: tên chủ đề, các bài (kèm số trang SGK nếu có), công thức/ý chính, hình minh họa SVG, danh sách 6 đề. Chi tiết ở `docs/05_THIET_KE.md`.
