"""Original posters for Unit 10 and the two textbook reviews."""
from gen_overview import gen_sheet,box
from english.units import DETAILS,label


def sheet_final(unit,content):
    n=unit['n'];d=DETAILS[n];col=d['colour'];bg=d['bg']
    def lesson(i,title,pg,head,body):return dict(n=i,title=title,pg=pg,head=head,body=body,col=col,bg=bg,dk='#702344')
    def pictures():return '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px">'+''.join('<figure style="margin:0;min-width:0">'+content.picture(w,280)+f'<figcaption style="font-weight:700;margin-top:8px">{w}</figcaption></figure>' for w in content.CORE)+'</div>'
    if n==10:
        lessons=[lesson(1,'Đã đi đến đâu?','68–69','Did + go trong câu hỏi, went trong câu kể.',lambda c:
            box(bg,'<b>Did they go to Ba Na Hills?</b><br>Yes, they did. / No, they didn’t.<br><b>Where did they go?</b> — They went to Hoan Kiem Lake.')+
            box(bg,'<b>Ba Na Hills</b> · <b>Hoan Kiem Lake</b><br><b>Suoi Tien Theme Park</b> · <b>Bai Dinh Pagoda</b><br>Tên địa điểm theo sách. Đọc nơi đến trong thẻ, không đoán từ tranh hoạt động.')),
            lesson(2,'Đã làm gì ở đó?','70–71','What did they do there? — They + động từ quá khứ.',lambda c:
                pictures()+box(bg,'visit the old buildings → <b>visited the old buildings</b><br>plant trees → <b>planted trees</b><br>play games → <b>played games</b><br>walk around the lake → <b>walked around the lake</b>')+
                box(bg,'Tranh minh họa hoạt động chung, không phải ảnh địa danh. Trong câu kể không thêm did trước visited/planted. Sau did trong câu hỏi dùng visit/plant nguyên mẫu.')),
            lesson(3,'Tháng, đọc và kể chuyến đi','72–73','Tìm đủ lớp của ai, nơi, tháng và hoạt động.',lambda c:
                box(bg,'<b>No-VEM-ber</b>, <b>De-CEM-ber</b>: nhấn âm thứ hai.<br><b>last November</b>: tháng 11 vừa qua; <b>last December</b>: tháng 12 vừa qua.')+
                box(bg,'<b>Thẻ tự soạn:</b> Class: Linh’s class · Place: Hoan Kiem Lake · Month: December · Activity: walked around the lake.<br><b>Viết:</b> They went to Hoan Kiem Lake last December. They walked around the lake.')+
                box(bg,'<b>Tự kiểm tra:</b> did + go/do hay câu kể went? Đã đổi động từ quá khứ chưa? Tháng có đúng thẻ không? Các chuyến đi là giả định.'))]
        chips=['Nơi đã đến','Việc đã làm','Đọc và viết'];intro='Một chuyến đi, nhiều điều để kể.';title='OUR SCHOOL TRIP';num=10
    elif n=='R1':
        lessons=[lesson(1,'Bản thân, nhà ở và bạn bè','40–41','Ôn Unit 1–3, khớp đúng loại thông tin.',lambda c:
            pictures()+box(bg,'<b>Can you tell me about yourself?</b> — I am An. I am in Grade 5.<br><b>What is your address?</b> — It is 21 Rose Street.<br><b>What nationality is she?</b> — She is Japanese.<br><b>What is she like?</b> — She is helpful.')+
            box(bg,'<b>In</b> a house/flat; <b>at</b> + địa chỉ cụ thể.<br>Favourite colour/animal khác quốc tịch và tính cách. Địa chỉ trong đề là giả định, không cần địa chỉ thật của em.')),
            lesson(2,'Sở thích và nghề nghiệp','40–43','Ôn Unit 4–5 và từ trong phần mở rộng.',lambda c:
                box(bg,'<b>What do you like doing?</b> — I like playing the violin.<br><b>What would you like to be?</b> — I would like to be a writer.<br><b>Why?</b> — Because I would like to write stories.')+
                box(bg,'Like + <b>V-ing</b>; would like to <b>be a + nghề</b>; would like to <b>+ nguyên mẫu</b>.<br>Writer/write stories; reporter/report the news; gardener/grow flowers; teacher/teach children.')+
                box(bg,'<b>Mở rộng trang 42–43:</b> actor — diễn viên; theatre — nhà hát; firefighter — lính cứu hỏa; put out fires — dập lửa. Nghề và sở thích không suy theo giới tính.')),
            lesson(3,'Đọc hồ sơ và viết tổng hợp','41–43','Đọc nhiều thông tin nhưng không lẫn người.',lambda c:
                box(bg,'<b>Hồ sơ tự soạn:</b> An · Australian · house · 21 Rose Street · friendly · likes playing the violin · future job writer · reason write stories.')+
                box(bg,'<b>Viết:</b> I am An. I am Australian. I live in a house at 21 Rose Street. I like playing the violin. I would like to be a writer because I would like to write stories.')+
                box(bg,'<b>Tự kiểm tra:</b> tên và quốc tịch đúng chưa? In/at đúng chưa? Like + V-ing chưa? Nghề và lý do có cùng hồ sơ không? Đoạn viết mở dùng mẫu tham khảo, không coi chỉ một cách diễn đạt là đúng.'))]
        chips=['Unit 1–3','Unit 4–5','Đọc và viết'];intro='Ghép những điều đã học thành câu chuyện của em.';title='ÔN TẬP UNIT 1–5';num=1
    else:
        lessons=[lesson(1,'Trường lớp và hoạt động','74–75','Ôn Unit 6–8: đúng tầng, đúng sở thích, đúng chủ sở hữu.',lambda c:
            pictures()+box(bg,'<b>Where is the library?</b> — It is on the second floor.<br><b>What school activity does she like?</b> — She likes doing projects.<br><b>Why?</b> — Because she thinks it is useful.')+
            box(bg,'<b>Whose glue stick is this?</b> — It is An’s.<br><b>Where are the crayons?</b> — They are under the desk.<br>Where hỏi vị trí, Whose hỏi của ai. Ground floor khác first floor.')),
            lesson(2,'Hai chuyến đi đã qua','74–75','Ôn Unit 9–10, tách yesterday khỏi school trip.',lambda c:
                box(bg,'<b>Yesterday:</b> We were at the aquarium. We watched the fish.<br><b>School trip:</b> We went to Ba Na Hills last November. We visited the old buildings.')+
                box(bg,'<b>Were you…?</b> — Yes, we were. / No, we weren’t.<br><b>Did they go…?</b> — Yes, they did. / No, they didn’t.<br><b>What did they do?</b> — They planted trees.')+
                box(bg,'Sau did dùng go/do/play nguyên mẫu. Câu kể dùng went/played/planted. Bài đọc có thể kể hai chuyến khác nhau; gắn mỗi hoạt động với đúng thời gian.')),
            lesson(3,'Sắp xếp thông tin và kể lại','75–77','Đọc thứ tự trước/sau và loại kỳ nghỉ theo thẻ.',lambda c:
                box(bg,'<b>Thẻ tự soạn:</b> Morning: planted trees · Afternoon: played games · Trip: last November.<br><b>Viết:</b> In the morning, we planted trees. In the afternoon, we played games.')+
                box(bg,'<b>Phần mở rộng:</b> adventure holiday — nghỉ trải nghiệm; beach holiday — nghỉ ở biển; sightseeing holiday — nghỉ tham quan; winter holiday — nghỉ mùa đông.<br>Một hoạt động có thể xuất hiện trong nhiều loại kỳ nghỉ. Khi chấm, đọc đúng kế hoạch/thẻ của câu.')+
                box(bg,'<b>Tự kiểm tra:</b> đang nói chuyến nào? Địa điểm, tháng và hoạt động có khớp nhau không? Was/were và dạng quá khứ đúng chưa?'))]
        chips=['Unit 6–8','Unit 9–10','Đọc và viết'];intro='Nhìn lại lớp học và những chuyến đi đáng nhớ.';title='ÔN TẬP UNIT 6–10';num=2
    result=gen_sheet(num,title,f"{label(unit)} · Tiếng Anh 5 Global Success · Trang {unit['pages']}",col,bg,lessons,chips,intro,'Sáu đề tự soạn, nghe ba cấp và trang học từ/phát âm để ôn theo nhịp của em.',f"Nội dung tự soạn, bám {label(unit)} · Global Success 5, tập một")
    if unit.get('kind')=='review':result=result.replace('>Chủ đề</span>','>Review</span>',1)
    return result
