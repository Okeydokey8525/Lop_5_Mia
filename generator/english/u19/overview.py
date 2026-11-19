"""Unit 19 overview grounded in printed pages 58-63."""
from gen_overview import gen_sheet, box


def sheet(unit, content):
    col, bg = '#A63C70', '#FFE4F0'
    pictures = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px">' + ''.join('<figure style="margin:0;min-width:0">' + content.picture(w, 280) + f'<figcaption style="font-weight:700;margin-top:8px">{w}</figcaption></figure>' for w in content.CORE) + '</div>'

    def lesson(n, title, pg, head, body):
        return dict(n=n, title=title, pg=pg, head=head, body=body, col=col, bg=bg, dk='#702344')

    lessons = [
        lesson(1, 'Em nghĩ gì về địa điểm?', '58–59', 'What do you think of…?', lambda c: pictures + box(bg, '<b>I think it is peaceful / exciting / beautiful / fantastic.</b><br>Peaceful: yên bình · exciting: thú vị, sôi động · beautiful: đẹp · fantastic: tuyệt vời.<br><b>Ban Gioc Waterfall</b>: Thác Bản Giốc · <b>Hoi An Old Town</b>: Phố cổ Hội An · <b>Sydney Opera House</b>: Nhà hát Opera Sydney.') + box(bg, '<b>What do you think of Petronas Twin Towers?</b><br><b>I think they are fantastic.</b> Towers là số nhiều → they are; một nơi như the lake → it is.<br>Tranh chỉ loại địa điểm. Cảm nhận có thể khác nhau; đọc đúng ý kiến người trong thẻ.')),
        lesson(2, 'Hỏi khoảng cách', '60–61', 'How far is it from…to…?', lambda c: box(bg, '<b>How far is it from the school to the lake?</b><br><b>It is about four kilometres.</b><br>From: từ · to: đến · about: khoảng · one kilometre / four kilometres.<br>Ví dụ trên là giả định để luyện Anh, không phải khoảng cách địa lý thực.') + box(bg, '<b>Cùng tuyến: school → museum → lake.</b><br>School → museum: 3 km; museum → lake: 4 km. Tổng quãng đường <b>theo tuyến qua museum</b>: 7 km.<br>Không cộng những chặng rời nhau; phân biệt How far (khoảng cách) với How can (cách đi).')),
        lesson(3, 'Ngữ điệu, đọc và viết kỳ nghỉ', '62–63', 'Câu hỏi Wh thường xuống giọng ↘', lambda c: box(bg, '<b>What do you think of the lake? ↘</b><br><b>How far is it from here to the lake? ↘</b><br>Khi đọc, tìm: nơi đến, cách đi, hoạt động, đồ ăn và nơi ở. Sách có bài đọc về Sentosa Island; bài luyện ở đây được tự soạn.') + box(bg, '<b>Thử nói hoặc viết kỳ nghỉ mơ ước khoảng 40 từ:</b><br>Em muốn đến đâu? Nơi ấy ở đâu? Cách quê em bao xa? Đi bằng gì? Em nghĩ nơi ấy thế nào? Em làm gì ở đó?<br>Đề tự chấm dùng thẻ có dữ kiện và câu có mở đầu/thứ tự rõ. Bài viết tự do nên nhờ người lớn đọc cùng; website chưa chấm nói hoặc chấm bài luận tự do.')),
    ]
    return gen_sheet(19, 'PLACES OF INTEREST', 'Unit 19 · Global Success 5 · Tập hai · Trang 58–63', col, bg, lessons, ['Địa điểm và cảm nhận', 'Hỏi khoảng cách', 'Đọc và viết kỳ nghỉ'], 'Mỗi nơi thú vị mở thêm một điều em biết.', 'Học từ, nghe chậm, ABC và hội thoại; sáu đề theo ba cấp độ.', 'Nội dung tự soạn, bám Unit 19 · Global Success 5, tập hai')
