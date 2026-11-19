"""Special days review sheet; original menus, no copied textbook passages."""
from gen_overview import gen_sheet,box


def sheet(unit,content):
    col='#A63C70';bg='#FFE4F0'
    def lesson(i,title,pg,head,body):return dict(n=i,title=title,pg=pg,head=head,body=body,col=col,bg=bg,dk='#702344')
    pictures='<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px">'+''.join('<figure style="margin:0;min-width:0">'+content.picture(w,280)+f'<figcaption style="font-weight:700;margin-top:8px">{w}</figcaption></figure>' for w in content.CORE)+'</div>'
    lessons=[lesson(1,'Ngày đặc biệt, em sẽ làm gì?','18–19','What will you do…? — We’ll + nguyên mẫu.',lambda c:
        box(bg,'<b>What will you do on Children’s Day?</b> — We’ll dance.<br><b>What will you do on Teachers’ Day?</b> — We’ll sing.<br><b>On Sports Day</b> — We’ll play badminton.<br><b>At Mid-Autumn Festival</b> — We’ll have a party.')+
        box(bg,'<b>Children’s Day</b>: ngày Thiếu nhi · <b>Teachers’ Day</b>: ngày Nhà giáo<br><b>Sports Day</b>: ngày Thể thao · <b>Mid-Autumn Festival</b>: Tết Trung thu.<br>Sách dùng <b>on</b> với ba tên ngày; <b>at</b> với Mid-Autumn Festival. Đọc thẻ để biết kế hoạch, không đoán hoạt động chỉ từ tên ngày.')),
        lesson(2,'Thực đơn cho bữa tiệc','20–21','Food: đồ ăn · Drinks: đồ uống.',lambda c:
            pictures+box(bg,'<b>What food will you have at the party?</b> — We’ll have pizza and burgers.<br><b>What drinks will you have at the party?</b> — We’ll have apple juice and water.')+
            box(bg,'<b>milk tea</b> — trà sữa · <b>apple juice</b> — nước ép táo<br><b>lemonade</b> — nước chanh · <b>water</b> — nước.<br>Will + <b>have</b>, không dùng will has. Các món trong bài phục vụ học từ, không phải thực đơn bắt buộc.')),
        lesson(3,'Đọc lời mời và viết kế hoạch','22–23','Tìm đúng ngày, nơi, hoạt động và thực đơn.',lambda c:
            box(bg,'<b>Will you come to my birthday party?</b> — Yes, I will.<br><b>We’ll = We will · They’ll = They will.</b><br>Nhấn từ mang thông tin như <b>FOOD / DRINKS</b>, <b>HAVE</b>, <b>PARTY</b>; nghe và đọc cả cụm.')+
            box(bg,'<b>Thẻ tự soạn:</b> An · Children’s Day · dance · pizza · apple juice.<br><b>Viết:</b> We will dance on Children’s Day. We will have pizza and apple juice.')+
            box(bg,'<b>Tự kiểm tra:</b> câu hỏi cần hoạt động, đồ ăn hay đồ uống? Will + nguyên mẫu? Đúng on/at? Đọc đúng thực đơn Sunday, không lấy nhầm Saturday.<br>Bài viết tự động có yêu cầu thứ tự cụ thể; em vẫn có thể tự nói thêm với người thân.'))]
    return gen_sheet(13,'OUR SPECIAL DAYS','Unit 13 · Global Success 5 · Tập hai · Trang 18–23',col,bg,lessons,['Ngày và hoạt động','Food / drinks','Nghe, đọc và viết'],'Cùng lên kế hoạch cho một ngày vui.','Học từ, nghe và đánh vần; thử sáu đề rồi xem lại bài của em.','Nội dung tự soạn, bám Unit 13 · Global Success 5, tập hai')
