"""Unit 20 overview grounded in printed pages 64-69."""
from gen_overview import gen_sheet, box


def sheet(unit, content):
    col, bg = '#A63C70', '#FFE4F0'
    pictures = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px">' + ''.join('<figure style="margin:0;min-width:0">' + content.picture(w, 280) + f'<figcaption style="font-weight:700;margin-top:8px">{w}</figcaption></figure>' for w in content.CORE) + '</div>'

    def lesson(n, title, pg, head, body):
        return dict(n=n, title=title, pg=pg, head=head, body=body, col=col, bg=bg, dk='#702344')

    lessons = [
        lesson(1, 'Em sẽ tham quan đâu?', '64–65', 'Where are you going to visit this summer?', lambda c: box(bg, '<b>I am going to visit Huong River.</b><br>Huong River: sông Hương · Phong Nha Cave: động Phong Nha · Phu Quoc Island: đảo Phú Quốc · Dam Sen Aquarium: thủy cung Đầm Sen.<br><b>Where</b> hỏi nơi. <b>Visit + địa điểm</b>, không visit to. Kế hoạch trong thẻ là tự soạn, không phải lịch trình du lịch thực.') + box(bg, '<b>I am going to visit an aquarium.</b><br><b>She is going to visit an island.</b><br><b>We are going to visit Phong Nha Cave.</b><br>I am · he/she is · you/we/they are + going to + động từ nguyên mẫu. I’m = I am; We’re = We are.')),
        lesson(2, 'Em sẽ làm gì?', '66–67', 'What are you going to do this summer?', lambda c: pictures + box(bg, '<b>I am going to join a music club.</b><br>Go camping: đi cắm trại · visit an eco-farm: tham quan trang trại sinh thái · practise swimming: luyện bơi.<br>Giữ cả cụm: <b>join a music club</b>, <b>an eco-farm</b>, <b>practise swimming</b>. Sau going to không thêm -s hoặc dùng quá khứ: she is going to <b>join</b>, không joins/joined.') + box(bg, '<b>Where…visit?</b> → nơi đến.<br><b>What…do?</b> → hoạt động.<br>Ví dụ: I am going to visit an eco-farm. I am going to grow vegetables there. Một nơi có thể có nhiều hoạt động; đọc đúng người và kế hoạch trong thẻ.')),
        lesson(3, 'Ngữ điệu, đọc và viết kỳ nghỉ', '68–69', 'Câu hỏi Wh thường xuống giọng ↘', lambda c: box(bg, '<b>Where are you going to visit this summer? ↘</b><br><b>What are you going to do this summer? ↘</b><br>Khi đọc, đánh dấu <b>last summer</b> (đã qua) và <b>this summer</b> (kế hoạch trong bài).<br>Last summer, I went camping. This summer, I am going to join a music club.<br>Tìm đúng người, nơi, hoạt động chính và việc làm thêm; không chuyển việc năm ngoái thành dự định năm nay.') + box(bg, '<b>Thử nói hoặc viết khoảng 40 từ về kỳ nghỉ hè:</b><br>Em/chúng em sẽ đến đâu? Sẽ làm gì ở đó? Sau chuyến đi em dự định học hoặc tham gia việc gì?<br>Vẽ poster kế hoạch và nói với người thân. Đề tự chấm dùng dữ kiện và mở đầu/thứ tự rõ; bài viết tự do nhờ người lớn đọc cùng. Website có mẫu nghe/đánh vần, chưa ghi âm hoặc chấm bài nói/bài luận.')),
    ]
    return gen_sheet(20, 'OUR SUMMER HOLIDAYS', 'Unit 20 · Global Success 5 · Tập hai · Trang 64–69', col, bg, lessons, ['Nơi sẽ tham quan', 'Hoạt động mùa hè', 'Đọc và viết kế hoạch'], 'Mùa hè mới, em có bao điều muốn khám phá.', 'Học từ, nghe chậm, ABC và hội thoại; sáu đề theo ba cấp độ.', 'Nội dung tự soạn, bám Unit 20 · Global Success 5, tập hai')
