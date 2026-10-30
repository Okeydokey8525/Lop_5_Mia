"""Original review posters for Units 2 and 3; no textbook passages."""
from gen_overview import gen_sheet,box


def sheet(unit,content):
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
    else:
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
