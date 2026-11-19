"""Original habit and weekly-record review sheet."""
from gen_overview import gen_sheet,box


def sheet(unit,content):
    col='#A63C70';bg='#FFE4F0'
    def lesson(i,title,pg,head,body):return dict(n=i,title=title,pg=pg,head=head,body=body,col=col,bg=bg,dk='#702344')
    pictures='<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px">'+''.join('<figure style="margin:0;min-width:0">'+content.picture(w,280)+f'<figcaption style="font-weight:700;margin-top:8px">{w}</figcaption></figure>' for w in content.CORE)+'</div>'
    lessons=[lesson(1,'Em giữ sức khỏe thế nào?','24–25','How does he/she stay healthy? — He/She…',lambda c:
        pictures+box(bg,'<b>How does she stay healthy?</b> — She <b>eats</b> healthy food.<br><b>How does he stay healthy?</b> — He <b>does</b> morning exercise.')+
        box(bg,'<b>do → does · play → plays · drink → drinks · eat → eats.</b><br>Hỏi với does thì dùng động từ nguyên mẫu: <b>does she eat</b>, không dùng does she eats.')),
        lesson(2,'Bao nhiêu lần mỗi tuần?','26–27','How often does he/she + nguyên mẫu?',lambda c:
            box(bg,'<b>How often does she play badminton?</b><br>She <b>plays badminton twice a week</b>.<br><b>How often does he do yoga?</b> — He does yoga once a week.')+
            box(bg,'<b>once a week</b> — một lần mỗi tuần<br><b>twice a week</b> — hai lần mỗi tuần<br><b>three times a week</b> — ba lần mỗi tuần<br><b>every day</b> — mỗi ngày. <b>Regularly</b> là đều đặn, không có số lần cố định.')+
            box(bg,'<b>Lịch giả định đủ bảy ngày:</b> một buổi cầu lông vào Tuesday, một buổi vào Saturday, không có buổi vào ngày khác.<br>Hai buổi → <b>twice a week</b>. Cùng một hoạt động có thể có lịch khác nhau.')),
        lesson(3,'Đọc lịch và viết thói quen','28–29','Đúng động từ, đúng người, đúng số buổi.',lambda c:
            box(bg,'<b>Does she EAT HEALTHY FOOD?</b><br>Nhấn từ mang thông tin và đọc theo cụm. <b>doesn’t = does not</b>; sau does not dùng nguyên mẫu.')+
            box(bg,'<b>Thẻ tự soạn:</b> Linh · She · play sports · badminton on Tuesday and Thursday only, one session each day.<br><b>Viết:</b> She plays sports. She plays badminton twice a week.')+
            box(bg,'<b>Tự kiểm tra:</b> he/she đã thêm s/es ở câu kể? Sau does còn giữ nguyên mẫu? Lịch đã ghi đủ tuần? <b>How</b> hỏi cách/thói quen; <b>How often</b> hỏi tần suất.<br>Lịch trong bài phục vụ học tiếng Anh, không phải lịch tập bắt buộc cho trẻ.'))]
    return gen_sheet(14,'STAYING HEALTHY','Unit 14 · Global Success 5 · Tập hai · Trang 24–29',col,bg,lessons,['How does…?','How often…?','Đọc lịch tuần'],'Mỗi thói quen nhỏ, một câu chuyện để kể.','Học từ, nghe và đánh vần; đọc lịch rồi thử sáu đề theo nhịp của em.','Nội dung tự soạn, bám Unit 14 · Global Success 5, tập hai')
