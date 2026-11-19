"""Original health-language review sheet, not medical guidance."""
from gen_overview import gen_sheet,box


def sheet(unit,content):
    col='#A63C70';bg='#FFE4F0'
    def lesson(i,title,pg,head,body):return dict(n=i,title=title,pg=pg,head=head,body=body,col=col,bg=bg,dk='#702344')
    pictures='<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px">'+''.join('<figure style="margin:0;min-width:0">'+content.picture(w,280)+f'<figcaption style="font-weight:700;margin-top:8px">{w}</figcaption></figure>' for w in content.CORE)+'</div>'
    lessons=[lesson(1,'Nói khi không khỏe','30–31','What’s the matter? — I have a…',lambda c:
        pictures+box(bg,'<b>What’s the matter? = What is the matter?</b><br>I have a <b>toothache / headache / sore throat / stomach ache</b>.<br><b>I do not feel well.</b> — Mình cảm thấy không khỏe.')+
        box(bg,'<b>I have</b> nhưng <b>He/She has</b>: She has a sore throat.<br>Tranh giúp học từ và nhận biết vị trí; không dùng để chẩn đoán người thật. Khi không khỏe, em báo người lớn.')),
        lesson(2,'Lời thoại với should','32–33','What should I do? — You should + nguyên mẫu.',lambda c:
            box(bg,'<b>What should I do?</b><br>Thẻ hội thoại giao sẵn: <b>go to the dentist</b>.<br><b>You should go to the dentist.</b><br><b>Thanks for your advice.</b> — You are welcome.')+
            box(bg,'<b>have a rest</b> — nghỉ ngơi · <b>drink warm water</b> — uống nước ấm<br><b>go to the doctor</b> — đến bác sĩ<br><b>take some medicine</b> — dùng thuốc · <b>rinse your mouth with salt water</b> — súc miệng bằng nước muối.<br>Đây là các cụm từ trong bài tiếng Anh. Em không tự dùng thuốc; bài không có tên thuốc, liều hay công thức pha.')+
            box(bg,'Sau <b>should</b> dùng <b>go / have / drink</b> với mọi chủ ngữ. Không dùng should goes, should has hoặc should to go. Đọc đúng dòng được giao trong thẻ, không tự chọn cách chữa.')),
        lesson(3,'Quan tâm, đọc và viết hội thoại','34–35','Should not = shouldn’t; giữ nguyên động từ.',lambda c:
            box(bg,'<b>WHAT’s the MATTER?</b> · <b>WHAT should I DO?</b><br>Nhấn từ mang thông tin, đọc cả cụm. <b>don’t = do not</b>; <b>shouldn’t = should not</b>.')+
            box(bg,'<b>Thẻ đóng vai tự soạn:</b> An · headache · positive line: have a rest · negative line: watch too much TV.<br><b>Viết theo thẻ:</b> I have a headache. You should have a rest. You should not watch too much TV.')+
            box(bg,'<b>Tự kiểm tra:</b> I have / he has đúng chưa? Should + nguyên mẫu? Có giữ not của dòng phủ định? Đúng người trong hội thoại?<br>Bài nghe Giỏi tách hai người và hai thông tin; em được nghe lại.'))]
    return gen_sheet(15,'OUR HEALTH','Unit 15 · Global Success 5 · Tập hai · Trang 30–35',col,bg,lessons,['What’s the matter?','Should / shouldn’t','Hỏi thăm và đáp lời'],'Biết nói cảm giác, biết quan tâm đến bạn.','Học từ, nghe và đánh vần; luyện hội thoại tiếng Anh qua sáu đề tự soạn.','Nội dung tự soạn, bám Unit 15 · Global Success 5, tập hai')
