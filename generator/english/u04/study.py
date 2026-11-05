"""Original companion for verified Unit 4 likes and weekend routines."""
from english.u04.content import ACTIVITIES, CORE, FREQUENCIES, picture
from english.study.author import word as w, question as q, choice as c, dialogue as d
from english.study.render import render_study as render


def data():
    words=[w('activities',a,ACTIVITIES[a][2],'I '+a+' at the weekend.',**({'image':a} if a in CORE else {})) for a in ACTIVITIES]
    words += [w('likes',ACTIVITIES[a][0],ACTIVITIES[a][2]+' (dạng V-ing)','I like '+ACTIVITIES[a][0]+'.',image=a) for a in CORE]
    words += [w('weekend',name,vn,'I '+name+' read stories at the weekend.') for name,vn in FREQUENCIES.items()]
    dialogues=[
        d('activities','Hoạt động cuối tuần','What do you do at the weekend?','I read stories and listen to music.','Bạn làm gì cuối tuần? — Đọc truyện và nghe nhạc.'),
        d('activities','Tưới hoa','Do you water the flowers at the weekend?','Yes, I do.','Bạn có tưới hoa cuối tuần không? — Có.'),
        d('likes','Sở thích lúc rảnh','What do you like doing in your free time?','I like playing the violin.','Sau like dùng V-ing trong mẫu của Unit này.'),
        d('likes','Sở thích của bạn','What does she like doing in her free time?','She likes going for a walk.','Câu khẳng định She likes; câu hỏi does she like.'),
        d('weekend','Tần suất','What do you do at the weekend?','I usually water the flowers.','Usually đứng trước động từ thường water.'),
        d('weekend','Không bao giờ','Do you surf the Internet at the weekend?','No, I do not. I never surf the Internet at the weekend.','Never nghĩa là không bao giờ; không thêm don’t vào câu I never surf…'),
    ]
    exercises=[
        c('activity-listen','activities','Which activity do you hear?','water the flowers','Water the flowers là tưới hoa.',CORE,speech='I water the flowers at the weekend.'),
        q('activity-spell','activities','v i o _ i n — Write the whole word.','violin','Violin có chữ l sau o.'),
        c('activity-read','activities','Which phrase means “đọc truyện”?','read stories','Read stories là đọc truyện.',list(ACTIVITIES)),
        q('activity-internet','activities','surf the ___','Internet','Viết Internet.'),
        q('likes-water','likes','I like ___ the flowers. Use water.','watering','Water → watering sau like.'),
        q('likes-question','likes','What do you like ___ in your free time?','doing','What do you like doing…?'),
        c('likes-listen','likes','What does the speaker like doing?','going for a walk','Lời nghe nói I like going for a walk.',[ACTIVITIES[a][0] for a in CORE],speech='I like going for a walk in my free time.'),
        q('likes-third','likes','She ___ playing the violin. Use like.','likes','She likes; thêm s trong câu khẳng định.'),
        c('weekend-never','weekend','Which word means “không bao giờ”?','never','Never nghĩa là không bao giờ.',list(FREQUENCIES)),
        c('weekend-listen','weekend','How often does the speaker read stories?','sometimes','Lời nghe nói sometimes.',list(FREQUENCIES),speech='I sometimes read stories at the weekend.'),
        q('weekend-third','weekend','She usually ___ the flowers. Use water.','waters','She waters; trạng từ usually không thay đổi quy tắc thêm s.'),
        q('weekend-full','weekend','Card: I / always / read stories / at the weekend. Write one sentence.','I always read stories at the weekend.','I + always + read stories + at the weekend.'),
    ]
    return dict(unit=4,key='mia5:learn:en-u04-v1',intro='Học hoạt động lúc rảnh, nói điều em thích và thói quen cuối tuần.',groups=[
        dict(id='activities',name='Hoạt động',tip='Nhớ cả cụm: play the violin, surf the Internet, go for a walk, water the flowers. I ride my bike; với she có thể nói she rides a bike.'),
        dict(id='likes',name='Like + V-ing',tip='What do you like doing in your free time? — I like + V-ing. He/She likes; sau does dùng like. Go → going, play → playing.'),
        dict(id='weekend',name='Cuối tuần và tần suất',tip='Always → usually → often → sometimes → rarely → never: từ thường xuyên nhất đến không bao giờ; không gán phần trăm cố định. AL-ways, SOME-times nhấn âm đầu. I usually water; she usually waters.')],words=words,dialogues=dialogues,exercises=exercises)


def render_study():return render(data(),picture)
