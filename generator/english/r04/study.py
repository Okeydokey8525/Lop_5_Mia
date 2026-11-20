"""Review 4: mixed recall and a separate story-genre extension."""
from english.study.author import word as w, question as q, choice as c, dialogue as d
from english.study.render import render_study as render
from english.r04.content import picture


def data():
    rows={
        'stories':[
            ('windy','có gió','It is cool and windy in my weather diary.',None),
            ('jumper','áo len chui đầu','I usually wear a jumper in cold weather.',None),
            ('tortoise','rùa cạn','The tortoise walked slowly.','tortoise'),
            ('hare','thỏ rừng','The hare ran fast.',None),
            ('walked slowly','đã đi chậm','In my little story, the tortoise walked slowly.',None),
            ('ran fast','đã chạy nhanh','In my little story, the hare ran fast.',None)],
        'journeys':[
            ('bus','xe buýt','You can get there by bus.','bus'),
            ('on foot','đi bộ','You can get there on foot.',None),
            ('waterfall','thác nước','I think the waterfall is beautiful.','waterfall'),
            ('kilometres','ki-lô-mét','On my imaginary map, it is five kilometres away.',None),
            ('peaceful','yên bình','I think the lake is peaceful.',None),
            ('go camping','đi cắm trại','I am going to go camping this summer.','go camping'),
            ('join a music club','tham gia câu lạc bộ âm nhạc','She is going to join a music club.',None),
            ('practise swimming','luyện bơi','We are going to practise swimming.',None)],
        'extension':[
            ('adventure story','truyện phiêu lưu','The card says this is an adventure story.',None),
            ('mystery story','truyện bí ẩn, trinh thám','The card says this is a mystery story.',None),
            ('history story','truyện lịch sử','The card says this is a history story.',None),
            ('spooky story','truyện có yếu tố ma quái','The card says this is a spooky story.',None)]}
    words=[w(g,n,v,e,**({'image':img} if img else {})) for g,rs in rows.items() for n,v,e,img in rs]
    dialogs=[
        d('stories','Thời tiết và trang phục','What do you usually wear in cold weather?','I usually wear a jumper and trousers.','Theo thẻ thời tiết, không coi mọi nơi cùng mùa đều giống nhau.'),
        d('stories','Nhân vật đã làm gì?','How did the tortoise walk?','It walked slowly.','Did + walk trong câu hỏi; walked trong câu kể.'),
        d('journeys','Phương tiện và khoảng cách','How can I get to the lake?','You can get there by bus. On this imaginary map, it is five kilometres away.','Can + get; by bus / on foot. Khoảng cách là dữ kiện giả định.'),
        d('journeys','Kế hoạch mùa hè','What are you going to do this summer?','I am going to join a music club.','I am / she is / they are going to + nguyên mẫu.'),
        d('extension','Mở rộng: thể loại','What type of story is it?','The card says it is a mystery story.','Thể loại đọc từ thẻ, không bắt trẻ biết tác phẩm ngoài bài.'),
        d('extension','Mở rộng: nói sở thích','What type of stories do you like?','I like adventure stories because I think they are exciting.','Sở thích và lý do theo từng người; không ép một lý do cho mọi truyện.')]
    exercises=[
        q('story-base','stories','How did the hare ___? Use run, ran or runs.','run','Did + run.'),
        q('story-past','stories','The tortoise ___ slowly. Use walk in the past.','walked','Walk → walked.'),
        c('weather-listen','stories','What is the weather in the diary?','cool and windy','Nghe đúng hai đặc điểm.',['cool and windy','cold and dry','hot and sunny','warm and rainy'],speech='In my weather diary, it is cool and windy.'),
        q('clothes-base','stories','What do you usually ___? Use wear.','wear','Do + wear.'),
        q('transport-on','journeys','You can get there ___ foot.','on','On foot, không by foot.'),
        q('plan-are','journeys','They ___ going to go camping.','are','They are going to.'),
        c('journey-listen','journeys','How can the speaker get there?','by bus','Nghe by bus.',['by bus','by taxi','by bicycle','on foot'],speech='I want to visit the waterfall. I can get there by bus.'),
        q('place-plural','journeys','I think the waterfalls ___ beautiful.','are','Waterfalls số nhiều.'),
        c('genre-card','extension','Extension card: Type = mystery story. Choose the type.','mystery story','Đọc nhãn trong thẻ.',['adventure story','mystery story','history story','spooky story']),
        q('genre-an','extension','It is ___ adventure story. Use a or an.','an','An adventure story.'),
        c('genre-listen','extension','Extension: Which type is on the card?','history story','Nghe nhãn thể loại theo thẻ.',['adventure story','mystery story','history story','spooky story'],speech='The reading card says this is a history story.'),
        q('genre-plural','extension','I like adventure ___. Use story in the plural.','stories','Story → stories sau I like với nghĩa thích thể loại.')]
    return dict(unit='R4',label='Review 4',overview='TongQuan_Review4.html',key='mia5:learn:en-r04-v1',intro='Ôn Units 16–20: thời tiết, truyện, nơi đến, phương tiện và dự định hè. Nghe, ABC và bài luyện tự lưu; thể loại truyện ở Extension riêng.',groups=[
        dict(id='stories',name='Thời tiết và truyện',tip='Do…wear? Did…run? Câu hỏi dùng nguyên mẫu; câu kể quá khứ dùng walked/ran. Mỗi truyện tự soạn có đủ dữ kiện.'),
        dict(id='journeys',name='Chuyến đi và mùa hè',tip='Want to visit + nơi; can get there by bus / on foot; How far + khoảng cách; I think it is…; am/is/are going to + hoạt động.'),
        dict(id='extension',name='Mở rộng: thể loại truyện',tip='Extension trang 72–73: adventure, mystery, history, spooky story. History story giữ đúng từ trong sách. Thử giới thiệu truyện em thích với người thân; website chưa chấm lời nói hoặc bài viết tự do.')],words=words,dialogues=dialogs,exercises=exercises)


def render_study():return render(data(),picture)
