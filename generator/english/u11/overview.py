"""Original Unit 11 overview, volume two pages 6-11."""
from gen_overview import gen_sheet,box


def sheet(unit,content):
    col='#A63C70';bg='#FFE4F0'
    def lesson(i,title,pg,head,body):return dict(n=i,title=title,pg=pg,head=head,body=body,col=col,bg=bg,dk='#702344')
    pictures='<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px">'+''.join('<figure style="margin:0;min-width:0">'+content.picture(w,280)+f'<figcaption style="font-weight:700;margin-top:8px">{w}</figcaption></figure>' for w in content.CORE)+'</div>'
    lessons=[lesson(1,'Em đã làm gì cùng gia đình?','6–7','Did + nguyên mẫu; câu kể dùng quá khứ.',lambda c:
        pictures+box(bg,'<b>Did you swim?</b> — Yes, I did. / No, I didn’t.<br><b>I swam with my mother.</b><br>Did you <b>take</b> photos? — I <b>took</b> photos with my father.')+
        box(bg,'<b>collect seashells → collected seashells</b>: nhặt vỏ sò<br><b>walk on the beach → walked on the beach</b>: đi dạo trên bãi biển.<br>Không dùng did + swam/took trong câu hỏi.')),
        lesson(2,'Chuyến đi có gì đáng nhớ?','8–9','Hỏi hoạt động và thời gian của chuyến đi.',lambda c:
            box(bg,'<b>What did your family do there?</b><br>We <b>took a boat trip around the bay</b>.<br><b>When did your family go there?</b> — We went there last summer.')+
            box(bg,'buy souvenirs → <b>bought souvenirs</b><br>eat seafood → <b>ate seafood</b><br>see some interesting places → <b>saw some interesting places</b>.<br>With my father/brother/family: cùng bố/anh hoặc em trai/gia đình.')+
            box(bg,'Các thẻ chuyến đi là giả định. Cùng một nơi có thể có nhiều hoạt động; luôn tìm đúng thẻ, không đoán theo địa danh.')),
        lesson(3,'Nghe theo cụm, đọc và kể lại','10–11','Tìm đúng ngày, hoạt động và người đi cùng.',lambda c:
            box(bg,'<b>Nhịp câu hỏi:</b> nhấn các từ mang thông tin như When, go, London hoặc What, do, Finland. Đọc theo cụm, không đọc tên từng chữ cái như khi đánh vần.')+
            box(bg,'<b>Thẻ tự soạn:</b> Nha Trang · last summer · took photos · with my father.<br><b>Viết:</b> My family went to Nha Trang last summer. I took photos with my father.')+
            box(bg,'<b>Tự kiểm tra:</b> câu hỏi đã có did + nguyên mẫu? Câu kể đã đổi quá khứ? Đúng người, ngày và hoạt động chưa?<br>Nghe Giỏi có thể hỏi riêng Sunday sau khi kể cả Saturday; em được nghe lại.'))]
    return gen_sheet(11,'FAMILY TIME','Unit 11 · Global Success 5 · Tập hai · Trang 6–11',col,bg,lessons,['Did you…?','Gia đình đã làm gì?','Nghe, đọc và kể'],'Cùng gia đình, gom những kỷ niệm nhỏ.','Học từ, nghe và đánh vần; thử sáu đề rồi xem lại bài của em.','Nội dung tự soạn, bám Unit 11 · Global Success 5, tập hai')
