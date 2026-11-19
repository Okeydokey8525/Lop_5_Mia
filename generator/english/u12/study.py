"""Tet vocabulary and future plans, with independently saved practice."""
from english.u12.content import CORE,ACTIVITIES,PLACES,picture
from english.study.author import word as w,question as q,choice as c,dialogue as d
from english.study.render import render_study as render


def data():
    words=[w('prepare',k,ACTIVITIES[k],'I will '+k+' for Tet.',image=k) for k in CORE]
    words += [w('prepare',k,vn,ex) for k,vn,ex in [('make banh chung','gói/làm bánh chưng','My mother will make banh chung.'),('buy roses','mua hoa hồng','I will not buy roses.')]]
    words += [w('places',k,vn,'I will go to '+k+' at Tet.') for k,vn in zip(PLACES,['nhà ông bà của tôi','buổi trình diễn pháo hoa','tiệc năm mới','lễ hội hoa'])]
    words += [w('plans',k,vn,ex) for k,vn,ex in [('will','sẽ','We will decorate the house.'),('will not','sẽ không','I will not make banh chung.'),('at Tet','vào dịp Tết','We will visit our grandparents at Tet.'),('for Tet','để đón Tết','I will do the shopping for Tet.')]]
    dialogs=[d('prepare','Cùng trang trí','Will you decorate the house for Tet?','Yes, I will. I will decorate it with flowers.','Will + nguyên mẫu; đáp Yes, I will.'),
        d('prepare','Chọn việc khác','Will you make banh chung?','No, I will not. I will make spring rolls.','Phủ định việc đầu, rồi nói việc sẽ làm.'),
        d('places','Thăm ông bà','Where will you go at Tet?','I will go to my grandparents’ house.','Where hỏi nơi đến.'),
        d('places','Xem pháo hoa','Will you go to a flower festival?','No, I will not. I will go to a fireworks show.','Hai sự kiện khác nhau; nghe cả câu phủ định.'),
        d('plans','Đi mua sắm','What will you do for Tet?','I will do the shopping with my father.','Will + do; with là cùng với.'),
        d('plans','Kế hoạch gia đình','Where will your family go at Tet?','We will go to a New Year party.','Will không đổi theo chủ ngữ.')]
    exercises=[c('prepare-listen','prepare','What will the speaker do?','decorate the house','Nghe decorate the house.',CORE,speech='I will decorate the house for Tet.'),
        q('prepare-buy','prepare','She will ___ roses. Use buy.','buy','Sau will dùng buy, không thêm s.'),
        q('prepare-spring','prepare','I will make ___ rolls.','spring','Spring rolls là nem/cuốn chả giò.'),
        q('prepare-full','prepare','Rewrite in full: I won’t buy roses.','I will not buy roses.','Won’t = will not.',exactForm=True),
        c('places-listen','places','Where will the speaker go?',PLACES[1],'A fireworks show.',PLACES,speech='I will go to a fireworks show at Tet.'),
        q('places-where','places','___ will you go at Tet?','Where','Where hỏi nơi đến.'),
        q('places-to','places','I will go ___ a flower festival.','to','Go to.'),
        q('places-grandparents','places','Complete: my grandparents’ ___.','house','Nhà của ông bà.'),
        c('plans-listen','plans','Which activity will the speaker NOT do?','buy roses','Nghe will not buy roses.',['buy roses','do the shopping','make spring rolls','decorate the house'],speech='I will not buy roses. I will do the shopping.'),
        q('plans-negative','plans','Will you buy roses? No, I ___.','will not','Will not = won’t.',alternatives=['won’t']),
        q('plans-go','plans','Where will she ___ at Tet? Use go.','go','Will + go.'),
        q('plans-sentence','plans','Card: I / do the shopping / for Tet. Write one full-form sentence in this order.','I will do the shopping for Tet.','I will + nguyên mẫu.',exactForm=True)]
    return dict(unit=12,key='mia5:learn:en-u12-v1',intro='Chuẩn bị và lên kế hoạch đón Tết. Có âm thanh kèm bài, nghe chậm và đánh vần.',groups=[
        dict(id='prepare',name='Chuẩn bị đón Tết',tip='Will you + nguyên mẫu? — Yes, I will. / No, I won’t. Will not = won’t. Không dùng will buys hoặc will makes.'),
        dict(id='places',name='Em sẽ đi đâu?',tip='Where will you go at Tet? — I’ll go to + nơi/sự kiện. Phân biệt flower festival với fireworks show. My grandparents’ house là nhà ông bà.'),
        dict(id='plans',name='Nói kế hoạch của em',tip='For Tet: để chuẩn bị đón Tết; at Tet: vào dịp Tết. Nghe theo cụm và chú ý will/won’t. ABC đọc tên chữ cái, khác cách phát âm cả từ. Kế hoạch trong bài là giả định, không bắt buộc mọi gia đình giống nhau.')],words=words,dialogues=dialogs,exercises=exercises)


def render_study():return render(data(),picture)
