"""Tet review sheet; original examples and illustrations."""
from gen_overview import gen_sheet,box


def sheet(unit,content):
    col='#A63C70';bg='#FFE4F0'
    def lesson(i,title,pg,head,body):return dict(n=i,title=title,pg=pg,head=head,body=body,col=col,bg=bg,dk='#702344')
    pictures='<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px">'+''.join('<figure style="margin:0;min-width:0">'+content.picture(w,280)+f'<figcaption style="font-weight:700;margin-top:8px">{w}</figcaption></figure>' for w in content.CORE)+'</div>'
    lessons=[lesson(1,'Cùng chuẩn bị đón Tết','12–13','Will you + nguyên mẫu? — Yes, I will. / No, I won’t.',lambda c:
        pictures+box(bg,'<b>Will you decorate the house for Tet?</b> — Yes, I will.<br><b>Will you make banh chung?</b> — No, I won’t. I’ll make spring rolls.')+
        box(bg,'<b>do the shopping</b> — đi mua sắm<br><b>buy a branch of peach blossoms</b> — mua một cành hoa đào<br><b>buy roses</b> — mua hoa hồng. Hoa hồng khác hoa đào.<br>Sau will dùng <b>buy / make / do</b>, không thêm s hoặc đổi quá khứ.')),
        lesson(2,'Tết này em sẽ đi đâu?','14–15','Where hỏi nơi đến; trả lời I’ll go to…',lambda c:
            box(bg,'<b>Where will you go at Tet?</b><br>I’ll go to <b>my grandparents’ house</b>.<br>I’ll go to <b>a fireworks show</b>.')+
            box(bg,'<b>a New Year party</b> — tiệc năm mới<br><b>a flower festival</b> — lễ hội hoa<br><b>a fireworks show</b> — buổi trình diễn pháo hoa.<br><b>For Tet</b>: để chuẩn bị đón Tết; <b>at Tet</b>: vào dịp Tết.')+
            box(bg,'Nghe cả câu: “I won’t buy roses. I’ll buy peach blossoms.” Việc không làm và việc sẽ làm là hai ý khác nhau. Kế hoạch từng gia đình có thể khác nhau.')),
        lesson(3,'Nghe theo cụm, đọc kế hoạch','16–17','Will / won’t; đọc đúng người và hoạt động.',lambda c:
            box(bg,'<b>I’ll = I will · We’ll = We will · won’t = will not.</b><br>Nhấn từ mang thông tin: <b>DO</b> the <b>SHOPPING</b> for <b>TET</b>; đọc theo cụm, không tách từng chữ như khi ABC.')+
            box(bg,'<b>Thẻ tự soạn:</b> Linh · do the shopping · a fireworks show · with my father.<br><b>Viết:</b> I will do the shopping for Tet. I will go to a fireworks show at Tet.')+
            box(bg,'<b>Tự kiểm tra:</b> will + nguyên mẫu? Will not đúng chỗ? Where đã trả lời bằng nơi? Đúng người trong thẻ?<br>Nghe Giỏi cần hai ý và phân biệt hai người; em được nghe lại.'))]
    return gen_sheet(12,'OUR TET HOLIDAY','Unit 12 · Global Success 5 · Tập hai · Trang 12–17',col,bg,lessons,['Will you…?','Where will you go…?','Kế hoạch đón Tết'],'Đón Tết với những kế hoạch nhỏ.','Học từ, nghe và đánh vần; thử sáu đề rồi xem lại bài của em.','Nội dung tự soạn, bám Unit 12 · Global Success 5, tập hai')
