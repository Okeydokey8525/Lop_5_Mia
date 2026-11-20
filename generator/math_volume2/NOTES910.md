# Toán tập hai — Chủ đề 9–10

## Nguồn và đối chiếu

- PDF đầy đủ chủ repo gửi: `C:\LeDucLuong\Mia\tai_lieu\sach\SGK - Toán 5 - Tập 2 - Chương tình mới.pdf`, 138 trang, 20 723 145 byte.
- SHA256 chính xác: `08d50c2dc5e338789a073700a4ba9b7d5e7b03db42e4225959f3f2be9c7baeaf`.
- Kết nối tri thức với cuộc sống, Hà Huy Khoái/Lê Anh Vinh, tái bản lần thứ hai. PDF đầy đủ: trang PDF = trang in + 1. Đã xem bìa/tác giả/mục lục và đối chiếu trang in 40, 63, 64, 86.
- Đã đọc riêng từng trang in 40–63 từ PDF 70 trang nhận trước đó (trang PDF 42–65). Đã đọc riêng từng trang 64–86 qua [bản đọc của NXB](https://taphuan.nxbgd.vn/tap-huan/doc-sach/sgk-toan-5-tap-hai.4714103431); đối chiếu đúng bộ sách với PDF đầy đủ. Không tuyên bố đã xem lại toàn bộ 138 trang.
- Ảnh render, bản manifest nguồn trang 64–86, ảnh đối chiếu và HTML tra cứu nằm ngoài repo trong `C:\LeDucLuong\Mia\luu_tru\math-volume2-planning\`. Không đưa PDF, scan hoặc tranh SGK lên repo.
- Bài 49–55, trang 40–63: hình khai triển; diện tích hộp/lập phương; thể tích hộp/lập phương; thực hành và luyện tập chung.
- Bài 56–62, trang 64–86: đơn vị thời gian; cộng/trừ/nhân/chia; vận tốc; quãng đường và thời gian; thực hành và luyện tập chung. Tên và trang đầu từng bài ở `topics910.py`.

## Nội dung và ranh giới

- Mỗi chủ đề 6 đề × 24 câu, 10/8/6 câu ba mức, 100 điểm; đủ bảy bài và bốn dạng câu trong từng đề. Cùng bộ dạng bài với dữ kiện thay đổi, không phải 288 dạng toán khác nhau. Ví dụ, sơ đồ và câu hỏi tự soạn.
- Chủ đề 9: hình khai triển lập phương/trụ; S xung quanh/toàn phần; hộp không nắp; thể tích; đổi đơn vị; xếp hộp phải vừa từng chiều; mặt tiếp xúc; vật chìm hoàn toàn/không hút nước/nước không tràn; bảo toàn lượng nước. Không dạy công thức diện tích/thể tích hình trụ.
- Chủ đề 10: đổi theo 60; mượn/nhớ; ngày hôm sau; chọn đơn vị vận tốc; làm tròn một chữ số thập phân theo đề; tách lúc chạy/nghỉ; từng chặng và vận tốc trung bình từ tổng quãng đường/thời gian. Hai người gặp sau thời gian cho sẵn: tính riêng mỗi quãng đường, không đòi công thức chuyển động tương đối ngoài phạm vi.
- Các số đo thực hành/bảng giá/đường đi là giả định. Hoạt động đo ở tổng quan dành cho người lớn hỗ trợ; không chấm như thể trẻ đã thực hành thật.
- Đáp án sinh bằng Decimal; audit độc lập bằng Fraction từ văn bản đã xuất, không gọi hàm giải của generator. Kiểm hình khai triển bằng gấp 3D và sáu pháp tuyến phân biệt.

## Nguồn và kiểm tra

- `topics910.py`, `overviews910.py`: nguồn mới; `gen_math_volume2.py` sinh thêm wrapper và tests9/10. Registry cfg, bộ tổng quan và build chung giữ kiến trúc cũ. ID `cd9-deN`, `cd10-deN`; không đổi ID cũ hoặc schema lưu bài.
- `python tools/audit_math910.py`; `node tools/qa_math910.js` và `--webkit`; `node tools/qa_persistence.js --math=9,10`. Cổng 7–8 vẫn chạy riêng, toàn bộ audit/order và QA chung tiếp tục chạy.
- Giữ hình SVG có kích thước riêng/max-width 100%; phải xem nét/chữ ở điện thoại, kiểm cả hình khai triển và nhãn cạnh, không chỉ kiểm tràn ngang.
- Bàn giao và trạng thái local/CI/live: `docs/breakdowns/2026-11-20_TOAN_CHUDE9_CHUDE10.md`. Bản đầy đủ đã có; chủ đề 11–12 chưa được giao trong đợt này.
