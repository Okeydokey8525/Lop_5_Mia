"""Original review posters for the published units; no textbook passages."""
from gen_overview import gen_sheet,box


def sheet67(unit,content):
    from english.units import DETAILS
    details=DETAILS[unit['n']];colour=details['colour'];bg=details['bg']
    def lesson(n,title,pg,head,body):return dict(n=n,title=title,pg=pg,head=head,body=body,col=colour,bg=bg,dk='#702344')
    def pictures():return '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px">'+''.join('<figure style="margin:0;min-width:0">'+content.picture(w,280)+f'<figcaption style="font-weight:700;margin-top:8px">{w}</figcaption></figure>' for w in content.CORE)+'</div>'
    if unit['n']==6:
        lessons=[
          lesson(1,'Phòng nào, tầng nào?','44–45','Nhận biết phòng bằng đồ dùng, gọi đúng tên tầng.',lambda c:
            pictures()+box(bg,'<b>library</b> — thư viện · <b>computer room</b> — phòng máy tính<br><b>music room</b> — phòng âm nhạc · <b>art room</b> — phòng mĩ thuật')+
            box(bg,'<b>Where is the library?</b><br>It is <b>on the second floor</b>.<br><b>Where’s = Where is</b>; <b>It’s = It is</b>.')+
            box(bg,'<b>ground floor</b> — tầng trệt → <b>first floor</b> — tầng ngay trên tầng trệt → <b>second floor</b> → <b>third floor</b>.<br>Dùng cách gọi của sách; không coi ground floor và first floor là cùng một tầng.')),
          lesson(2,'Hỏi đường thật lịch sự','46–47','Đọc vị trí xuất phát rồi làm theo từng bước.',lambda c:
            box(bg,'<b>Could you tell me the way to the art room, please?</b><br>Go along the corridor and turn left.<br>Thank you. — You are welcome.')+
            box(bg,'<b>go upstairs</b> — đi lên tầng trên<br><b>go downstairs</b> — đi xuống tầng dưới<br><b>go along the corridor</b> — đi dọc hành lang<br><b>go past the library</b> — đi qua thư viện<br><b>turn left / right</b> — rẽ trái / phải')+
            box(bg,'<b>Mẹo:</b> tìm tầng trước, tìm hướng sau. Đi lên hay xuống phụ thuộc nơi bắt đầu. Các kế hoạch phòng trong đề là giả định và có thể khác nhau; luôn đọc thẻ của câu hiện tại.')),
          lesson(3,'Đọc kế hoạch và viết chỉ dẫn','48–49','Tách rõ tên phòng, tầng và hướng đi.',lambda c:
            box(bg,'<b>up-STAIRS</b>, <b>down-STAIRS</b>: nhấn âm sau.<br>Dùng <b>on the + tầng + floor</b>.')+
            box(bg,'<b>Thẻ tự soạn:</b> Start: ground floor · Room: art room · Floor: first · Turn: right.<br><b>Viết từ thẻ:</b> It is on the first floor. Go upstairs. Go along the corridor and turn right.')+
            box(bg,'<b>Tự kiểm tra:</b> đã có is chưa? Có on the chưa? Đúng tầng, trái/phải chưa? Nghe Giỏi cần tìm đủ hai ý; được nghe lại hoặc xem lời nghe.')),
        ];chips=['Phòng và tầng','Hỏi và chỉ đường','Đọc và viết'];intro='Khám phá từng góc nhỏ trong ngôi trường.'
    else:
        p=content.PROFILES[1]
        lessons=[
          lesson(1,'Hoạt động yêu thích ở trường','50–51','Hỏi does…like; trả lời He/She likes + V-ing.',lambda c:
            pictures()+box(bg,'<b>do projects → doing projects</b> — làm dự án<br><b>read books → reading books</b> — đọc sách<br><b>play games → playing games</b> — chơi trò chơi<br><b>solve maths problems → solving maths problems</b> — giải toán')+
            box(bg,'<b>What school activity does she like?</b><br>She <b>likes doing</b> projects.<br><b>Does he like reading books?</b> — Yes, he does. / No, he doesn’t.<br>Sau <b>does</b> dùng <b>like</b>; khi kể dùng <b>likes</b>.')),
          lesson(2,'Vì sao bạn ấy thích?','52–53','Why hỏi lý do; Because mở đầu lời giải thích.',lambda c:
            box(bg,'<b>Why does he like solving maths problems?</b><br>Because he <b>thinks it is useful</b>.')+
            box(bg,'<b>fun</b> — vui · <b>interesting</b> — thú vị<br><b>useful</b> — hữu ích · <b>good for group work</b> — tốt cho làm việc nhóm')+
            box(bg,'He/She <b>likes + V-ing</b> because he/she <b>thinks it is + lý do</b>.<br>Cùng một hoạt động, mỗi bạn có thể nêu lý do khác nhau. Đáp án theo thẻ/bài đọc, không có một lý do bắt buộc cho tất cả.')),
          lesson(3,'Đọc hồ sơ và viết sở thích','54–55','Khớp đúng người, hoạt động và lý do.',lambda c:
            box(bg,'<b>READ-ing</b>, <b>SOLV-ing</b>: nhấn âm đầu.<br><b>doesn’t = does not</b>; <b>it’s = it is</b>.')+
            box(bg,f"<b>Thẻ tự soạn:</b> {content.card(p)}<br><b>Viết từ thẻ:</b> {content.full_sentence(p)}")+
            box(bg,'<b>Tự kiểm tra:</b> he/she khớp thẻ chưa? Đã có likes + V-ing chưa? Đã thêm s ở thinks chưa? Nghe Giỏi lấy đủ hoạt động và lý do; không tăng độ khó bằng tốc độ.')),
        ];chips=['Hoạt động ở trường','Sở thích và lý do','Đọc và viết'];intro='Mỗi hoạt động là một niềm vui khám phá.'
    return gen_sheet(unit['n'],unit['name'].upper(),f"Unit {unit['n']} · Tiếng Anh 5 Global Success · Trang {unit['pages']}",colour,bg,lessons,chips,intro,'Ôn từ, đọc thẻ và luyện nghe ba cấp độ. Sáu đề giúp em tiến từng bước theo nhịp của mình.',f"Nội dung ôn tập tự soạn, bám Unit {unit['n']} · Global Success 5, tập một")


def sheet(unit,content):
    if unit['n'] in (6,7):return sheet67(unit,content)
    if unit['n'] in (4,5):return sheet45(unit,content)
    colour,bg,dk=('#AD4278','#FFE3F1','#702344') if unit['n']==2 else ('#AF4771','#FFE8F1','#702344')
    def lesson(n,title,pg,head,body):return dict(n=n,title=title,pg=pg,head=head,body=body,col=colour,bg=bg,dk=dk)
    def pictures(names):
        return '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px">'+''.join('<figure style="margin:0;min-width:0">'+content.picture(w,280)+f'<figcaption style="font-weight:700;margin-top:8px">{w}</figcaption></figure>' for w in names)+'</div>'
    if unit['n']==2:
        lessons=[
          lesson(1,'Ngôi nhà của em','16–17','Nhận biết loại nhà và trả lời câu hỏi có/không.',lambda c:
            box(bg,'<b>house</b> — ngôi nhà · <b>flat</b> — căn hộ · <b>building</b> — tòa nhà · <b>tower</b> — tòa tháp')+
            pictures(['house','flat','building','tower'])+
            box(bg,'<b>Do you live in this house?</b> — Yes, I do.<br><b>Do you live in that flat?</b> — No, I don’t.<br><b>This</b>: ở gần người nói; <b>that</b>: ở xa. Tower cũng là một loại building; flat là một căn hộ bên trong tòa nhà.')),
          lesson(2,'Địa chỉ và khoảng cách','18–19','Hỏi số nhà, tên đường; nói gần hay xa trường.',lambda c:
            box(bg,'<b>What is your address?</b> — It is 14 Queen Street.<br><b>I live at 14 Queen Street.</b><br><b>I live in a house.</b>')+
            box(bg,'<b>in + loại nhà</b>; <b>at + địa chỉ cụ thể</b>.<br>My home is <b>near</b> my school. — Nhà mình gần trường.<br>My home is <b>far from</b> my school. — Nhà mình xa trường.')+
            box(bg,'Các địa chỉ trong bộ đề đều giả định. Em không cần nhập địa chỉ thật của gia đình.')),
          lesson(3,'Số nhà, đọc và viết','20–21','Đọc số chính xác rồi tìm thông tin trong thẻ.',lambda c:
            box(bg,'<b>fif-TEEN</b> (15), <b>six-TEEN</b> (16): nhấn âm cuối.<br>Phân biệt <b>sixteen</b> (16) và <b>sixty</b> (60).')+
            box(bg,'<b>Thẻ tự soạn:</b> Name: Linh · Home: flat · Address: 26 Oxford Street · School: far from the home.<br><b>Viết từ thẻ:</b> I live in a flat. My address is 26 Oxford Street. My home is far from my school.')+
            box(bg,'<b>Mẹo:</b> gạch ý trong đầu: ai → loại nhà → số nhà → đường → gần/xa. Nghe Giỏi cần kết hợp hai thông tin, có thể nghe lại.')),
        ];chips=['Loại nhà','Địa chỉ và khoảng cách','Đọc và viết'];intro='Một ngôi nhà, một địa chỉ, một câu chuyện của em.';lead='Ôn từ chỉ nhà ở, cách hỏi địa chỉ và đọc thông tin. Sáu đề có nghe phân cấp để em luyện từng bước.'
    elif unit['n']==3:
        lessons=[
          lesson(1,'Quốc gia và quốc tịch','22–23','Tên nước khác với từ chỉ quốc tịch.',lambda c:
            box(bg,'<b>Australia → Australian</b> · nước Úc<br><b>Malaysia → Malaysian</b> · nước Malaysia<br><b>America → American</b> · nước Mỹ<br><b>Japan → Japanese</b> · nước Nhật Bản<br><b>Britain → British</b> · nước Anh (theo cách gọi trong sách)')+
            box(bg,'<b>Where is he from?</b> — He is from Australia.<br><b>What nationality is he?</b> — He is Australian.<br><b>What nationality is she?</b> — She is Japanese.')+
            box(bg,'<b>Nhớ:</b> from + tên nước; is + quốc tịch. Không đoán quốc tịch từ gương mặt hay ngoại hình.')),
          lesson(2,'Bạn ấy có tính cách gì?','24–25','Nhìn hành động và đọc ngữ cảnh trước khi chọn.',lambda c:
            pictures(['friendly','helpful','clever','active'])+
            box(bg,'<b>friendly</b> — thân thiện, chào đón bạn mới.<br><b>helpful</b> — hay giúp đỡ, giúp bạn nhặt sách.<br><b>clever</b> — thông minh, giải câu đố.<br><b>active</b> — năng động, tích cực vận động.')+
            box(bg,'<b>What is she like?</b> — She is friendly.<br><b>What is he like?</b> — He is helpful.<br>Câu này hỏi <b>tính cách</b>, không phải hỏi món đồ yêu thích.')),
          lesson(3,'Đọc hồ sơ và giới thiệu bạn','26–27','Tách rõ quốc tịch, ngoại hình và tính cách.',lambda c:
            box(bg,'<b>AC-tive</b>, <b>FRIEND-ly</b>: nhấn âm đầu.<br><b>nationality:</b> Japanese · <b>appearance:</b> long hair, big eyes · <b>personality:</b> helpful.')+
            box(bg,'<b>Hồ sơ tự soạn:</b> Yuki · Japan · Japanese · helpful · long hair · big eyes.<br><b>Viết từ thẻ:</b> This is Yuki. She is from Japan. She is Japanese. She is helpful. She has long hair and big eyes.')+
            box(bg,'<b>Tự kiểm tra:</b> He/She đã khớp thẻ chưa? Có is trước quốc tịch/tính cách chưa? Dùng has khi nói tóc và mắt. Nghe Giỏi tìm đủ hai ý.')),
        ];chips=['Quốc tịch','Tính cách','Giới thiệu bạn'];intro='Làm quen với bạn mới, hiểu thêm về thế giới.';lead='Ôn quốc tịch, tính cách và cách giới thiệu bạn. Đọc đúng thông tin, nghe từng bước và viết câu từ thẻ.'
    return gen_sheet(unit['n'],unit['name'].upper(),f"Unit {unit['n']} · Tiếng Anh 5 Global Success · Trang {unit['pages']}",colour,bg,lessons,chips,intro,lead,f"Nội dung ôn tập tự soạn, bám Unit {unit['n']} · Global Success 5, tập một")


def sheet45(unit,content):
    from english.units import DETAILS
    details=DETAILS[unit['n']];colour=details['colour'];bg=details['bg']
    def lesson(n,title,pg,head,body):return dict(n=n,title=title,pg=pg,head=head,body=body,col=colour,bg=bg,dk='#702344')
    def pictures(names):return '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px">'+''.join('<figure style="margin:0;min-width:0">'+content.picture(w,280)+f'<figcaption style="font-weight:700;margin-top:8px">{w}</figcaption></figure>' for w in names)+'</div>'
    if unit['n']==4:
        p=content.PROFILES[1]
        lessons=[
          lesson(1,'Điều em thích làm','28–29','Hỏi sở thích lúc rảnh; trả lời bằng like + V-ing.',lambda c:
            pictures(content.CORE)+
            box(bg,'<b>play the violin</b> — chơi đàn vi-ô-lông<br><b>surf the Internet</b> — lướt Internet<br><b>go for a walk</b> — đi dạo<br><b>water the flowers</b> — tưới hoa')+
            box(bg,'<b>What do you like doing in your free time?</b><br>I like <b>playing</b> the violin.<br><b>Nhớ:</b> sau like dùng V-ing: play → playing; go → going; water → watering.')),
          lesson(2,'Cuối tuần và tần suất','30–31','Hỏi hoạt động cuối tuần và nói thường làm đến mức nào.',lambda c:
            box(bg,'<b>What do you do at the weekend?</b><br>I <b>usually read</b> stories.<br>I <b>often ride</b> my bike.<br>I <b>sometimes surf</b> the Internet.')+
            box(bg,'<b>always</b> — luôn luôn → <b>usually</b> — thường thường → <b>often</b> — thường xuyên → <b>sometimes</b> — thỉnh thoảng → <b>rarely</b> — hiếm khi → <b>never</b> — không bao giờ')+
            box(bg,'<b>Vị trí:</b> I + từ chỉ tần suất + động từ.<br>I like <b>reading</b> stories. (sở thích)<br>I usually <b>read</b> stories. (thói quen)<br>Never nói việc không làm; không hiểu thành “luôn làm”.')),
          lesson(3,'Đọc lịch và viết câu','32–33','Khớp đúng người, hoạt động và tần suất.',lambda c:
            box(bg,'<b>AL-ways</b>, <b>SOME-times</b>: nhấn âm đầu.<br>He/She: likes, plays, waters, goes. I: like, play, water, go.')+
            box(bg,f"<b>Thẻ tự soạn:</b> {p['name']} · Likes: {content.ing(p['free'])} · Weekend: {p['weekend']} · Frequency: {p['frequency']}.<br><b>Viết từ thẻ:</b> {content.like(p)} {content.weekend(p)}")+
            box(bg,'<b>Mẹo đọc/nghe:</b> tìm ai → thích làm gì → cuối tuần làm gì → tần suất. Mức Giỏi kết hợp hai ý; được nghe lại hoặc xem lời nghe khi cần.')),
        ];chips=['Sở thích lúc rảnh','Cuối tuần','Đọc và viết'];intro='Lúc rảnh em thích làm gì?';lead='Nhận biết hoạt động, hỏi sở thích và kể về cuối tuần. Sáu đề có nghe chia ba mức để em luyện theo nhịp của mình.'
    else:
        p=content.PROFILES[0]
        lessons=[
          lesson(1,'Nghề em mơ ước','34–35','Nhận biết tên nghề và nói mong muốn tương lai.',lambda c:
            pictures(content.CORE)+
            box(bg,'<b>firefighter</b> — lính cứu hỏa · <b>reporter</b> — phóng viên<br><b>gardener</b> — người làm vườn · <b>writer</b> — nhà văn<br><b>doctor</b> — bác sĩ · <b>teacher</b> — giáo viên')+
            box(bg,'<b>What would you like to be in the future?</b><br>I would like to be <b>a writer</b>.<br><b>I’d = I would.</b> Dùng a trước tên nghề số ít trong những mẫu này.')),
          lesson(2,'Vì sao em chọn nghề đó?','36–37','Why hỏi lý do; Because mở đầu câu trả lời.',lambda c:
            box(bg,'<b>Why would you like to be a teacher?</b><br>Because I would like to <b>teach children</b>.')+
            box(bg,'<b>reporter → report the news</b> — đưa tin<br><b>gardener → grow flowers</b> — trồng hoa<br><b>writer → write stories</b> — viết truyện<br><b>teacher → teach children</b> — dạy trẻ em<br><b>doctor / firefighter → help people</b> — giúp mọi người')+
            box(bg,'<b>Hai mẫu cần phân biệt:</b><br>would like to <b>be a + nghề</b><br>would like to <b>+ việc muốn làm</b><br>Chọn lý do theo đúng hồ sơ, không chỉ đoán từ tên nghề.')),
          lesson(3,'Đọc hồ sơ và viết ước mơ','38–39','Ghép đúng tên, nghề và lý do của từng bạn.',lambda c:
            box(bg,'<b>TEA-cher</b>, <b>DEN-tist</b>: nhấn âm đầu.<br>Would you like to be a teacher? — <b>Yes, I would.</b>')+
            box(bg,f"<b>Thẻ tự soạn:</b> {p['name']} · Future job: {p['job']} · Reason: {content.reason(p)}.<br><b>Viết từ thẻ:</b> {content.job_sentence(p)} {content.because(p)}")+
            box(bg,'<b>Tự kiểm tra:</b> đã có would like to chưa? Có be a trước nghề chưa? Lý do có khớp thẻ không? I’d/He’d/She’d có thể viết đầy đủ thành I would/He would/She would.')),
        ];chips=['Nghề tương lai','Lý do lựa chọn','Đọc và viết'];intro='Ước mơ hôm nay, một bước tìm hiểu ngày mai.';lead='Làm quen tên nghề, nói ước mơ và giải thích lý do. Sáu đề gồm nghe, từ vựng, hội thoại, đọc và viết.'
    return gen_sheet(unit['n'],unit['name'].upper(),f"Unit {unit['n']} · Tiếng Anh 5 Global Success · Trang {unit['pages']}",colour,bg,lessons,chips,intro,lead,f"Nội dung ôn tập tự soạn, bám Unit {unit['n']} · Global Success 5, tập một")
