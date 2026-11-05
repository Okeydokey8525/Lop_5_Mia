"""Original recap posters for the classroom and past-outing units."""
from gen_overview import gen_sheet,box
from english.units import DETAILS


def sheet89(unit,content):
    n=unit['n'];details=DETAILS[n];colour=details['colour'];bg=details['bg']
    def lesson(i,title,pg,head,body):return dict(n=i,title=title,pg=pg,head=head,body=body,col=colour,bg=bg,dk='#702344')
    def pictures():return '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px">'+''.join('<figure style="margin:0;min-width:0">'+content.picture(w,280)+f'<figcaption style="font-weight:700;margin-top:8px">{w}</figcaption></figure>' for w in content.CORE)+'</div>'
    if n==8:
        p=content.PROFILES[2]
        lessons=[
            lesson(1,'Đồ dùng ở đâu?','56–57','Hỏi vị trí, phân biệt một và nhiều đồ dùng.',lambda c:
                box(bg,'<b>Where are the pencils?</b><br>They are <b>beside the book</b>.<br><b>Where is the crayon?</b><br>It is <b>under the desk</b>.')+
                box(bg,'<b>beside</b> — bên cạnh · <b>under</b> — bên dưới<br><b>above</b> — phía trên · <b>in front of</b> — phía trước<br>Luôn đọc cả giới từ và vật làm mốc. Không suy vị trí từ tranh đồ vật đơn lẻ.')+
                box(bg,'Một vật: <b>It is</b>…; nhiều vật: <b>They are</b>…<br><b>They’re = They are</b>; <b>It’s = It is</b>.')),
            lesson(2,'Đồ dùng của ai?','58–59','Hỏi chủ sở hữu bằng Whose, trả lời bằng tên + ’s.',lambda c:
                pictures()+box(bg,'<b>glue stick</b> — hồ dán dạng thỏi<br><b>crayon</b> — bút sáp màu<br><b>set square</b> — ê-ke<br><b>pencil sharpener</b> — gọt bút chì')+
                box(bg,'<b>Whose glue stick is this?</b> — It is An’s.<br><b>Is this your crayon?</b> — No, it isn’t. It’s Linh’s.<br><b>Whose</b> hỏi của ai; <b>Where</b> hỏi ở đâu.')),
            lesson(3,'Đọc góc học tập và viết','60–61','Khớp đúng chủ sở hữu, đồ dùng và vị trí.',lambda c:
                box(bg,'<b>a-BOVE</b>, <b>be-SIDE</b>: nhấn âm sau.<br>glue stick → <b>glue sticks</b>; set square → <b>set squares</b>; pencil sharpener → <b>pencil sharpeners</b>.')+
                box(bg,f"<b>Thẻ tự soạn:</b> {content.card(p)}<br><b>Viết từ thẻ:</b> This is Minh’s set square. It is in front of the pencil case.")+
                box(bg,'<b>Tự kiểm tra:</b> chủ sở hữu đúng chưa? Có ’s chưa? Đã chọn is/are theo số lượng chưa? Giới từ và vật làm mốc có khớp thẻ không?')),
        ];chips=['Vị trí đồ dùng','Của ai?','Góc học tập'];intro='Mỗi đồ dùng đều có một chỗ và một người bạn.'
    else:
        p=content.PROFILES[1]
        lessons=[
            lesson(1,'Chúng mình đã ở đâu?','62–63','Hỏi địa điểm trong quá khứ với Were you…?',lambda c:
                pictures()+box(bg,'<b>theatre</b> — nhà hát · <b>aquarium</b> — thủy cung<br><b>campsite</b> — khu cắm trại · <b>funfair</b> — hội chợ vui chơi')+
                box(bg,'<b>Were you at the aquarium yesterday?</b><br>Yes, we were. / No, we weren’t.<br><b>Where were you yesterday?</b> — I was at the theatre.<br><b>I/he/she/it was</b>; <b>you/we/they were</b>.')),
            lesson(2,'Đã làm gì ở đó?','64–65','Câu hỏi dùng did + nguyên mẫu, trả lời bằng động từ quá khứ.',lambda c:
                box(bg,'<b>What did you do there?</b> — We watched the fish.<br><b>listen to music → listened to music</b><br><b>watch the fish → watched the fish</b><br><b>dance around the campfire → danced around the campfire</b><br><b>play chess → played chess</b>')+
                box(bg,'Sau <b>did</b> dùng <b>do</b>, không dùng did played.<br>Câu kể: <b>We played chess.</b> Không thêm were trước played.<br>Hoạt động theo thẻ nhân vật, không suy chỉ từ địa điểm.')),
            lesson(3,'Đọc và kể chuyến đi','66–67','Tìm đủ ai, nơi nào, khi nào và việc đã làm.',lambda c:
                box(bg,'<b>CI-ne-ma</b>, <b>BA-ke-ry</b>: nhấn âm đầu.<br><b>yesterday</b> — hôm qua; <b>last Saturday/Sunday</b> — thứ Bảy/Chủ nhật vừa qua.<br><b>weren’t = were not</b>; <b>wasn’t = was not</b>.')+
                box(bg,f"<b>Thẻ tự soạn:</b> {content.card(p)}<br><b>Viết từ thẻ:</b> {content.where(p)} {content.action(p)}")+
                box(bg,'<b>Tự kiểm tra:</b> I was hay we were? Có đúng ngày không? Động từ câu kể đã đổi sang quá khứ chưa? Cấp Giỏi kết hợp hai ý, không đọc nhanh hơn.')),
        ];chips=['Địa điểm đã đến','Việc đã làm','Kể chuyện đã qua'];intro='Một chuyến đi, những điều em muốn kể.'
    return gen_sheet(n,unit['name'].upper(),f"Unit {n} · Tiếng Anh 5 Global Success · Trang {unit['pages']}",colour,bg,lessons,chips,intro,'Ôn tập tự soạn theo sách, sáu đề có nghe phân cấp. Mở trang học từ để nghe, đánh vần và luyện từng nhóm nhỏ.',f"Nội dung ôn tập tự soạn, bám Unit {n} · Global Success 5, tập một")
