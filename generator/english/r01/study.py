"""Review 1 vocabulary and original combined-pattern practice."""
from english.study.author import word as w,question as q,choice as c,dialogue as d
from english.study.render import render_study as render
from english.u01.content import picture as p1
from english.u02.content import picture as p2
from english.u03.content import picture as p3
from english.u04.content import picture as p4
from english.u05.content import picture as p5


def picture(name,width=320):return {'dolphin':p1,'pink':p1,'friendly':p3,'house':p2,'flat':p2,'water the flowers':p4,'play the violin':p4,'writer':p5}[name](name,width)


def data():
    words=[w('people',name,vn,example,**({'image':img} if img else {})) for name,vn,example,img in [
        ('dolphin','cá heo','My favourite animal is a dolphin.','dolphin'),('pink','màu hồng','My favourite colour is pink.','pink'),
        ('Australian','quốc tịch Úc','My friend is Australian.',None),('friendly','thân thiện','My friend is friendly.','friendly')]]
    words += [w('homes',name,vn,example,**({'image':img} if img else {})) for name,vn,example,img in [
        ('house','ngôi nhà','I live in a house.','house'),('flat','căn hộ','I live in a flat.','flat'),
        ('address','địa chỉ','My address is 21 Rose Street.',None),('near','gần','My home is near my school.',None)]]
    words += [w('dreams',name,vn,example,**({'image':img} if img else {})) for name,vn,example,img in [
        ('watering the flowers','tưới hoa (V-ing)','I like watering the flowers.','water the flowers'),
        ('playing the violin','chơi đàn vi-ô-lông (V-ing)','I like playing the violin.','play the violin'),
        ('writer','nhà văn','I would like to be a writer.','writer'),('report the news','đưa tin','I would like to report the news.',None),
        ('actor','diễn viên','An actor can work at a theatre.',None),('put out fires','dập lửa','Firefighters put out fires.',None)]]
    dialogs=[d('people','Giới thiệu bản thân','Can you tell me about yourself?','I am An. I am in Grade 5.','Tên và lớp là thông tin giả định để luyện.'),
        d('people','Tính cách và quốc tịch','What is your friend like?','She is helpful. She is Japanese.','Câu đầu nói tính cách; câu sau nói quốc tịch.'),
        d('homes','Địa chỉ giả định','What is your address?','It is 21 Rose Street.','Không cần nhập địa chỉ thật của em.'),
        d('homes','Loại nhà','Do you live in a flat?','No, I do not. I live in a house.','In + loại nhà, at + địa chỉ cụ thể.'),
        d('dreams','Sở thích và ước mơ','What do you like doing?','I like playing the violin. I would like to be a teacher.','Sở thích và nghề mơ ước có thể khác nhau.'),
        d('dreams','Nghề và lý do','Why would you like to be a reporter?','Because I would like to report the news.','Because nêu lý do, would like to + nguyên mẫu.')]
    exercises=[c('person-nationality','people','She is from Japan. She is ___.','Japanese','Japan → Japanese.',['Japanese','Australian','Malaysian','American']),
        q('person-is','people','He ___ helpful.','is','He is + tính cách.'),
        c('person-listen','people','What is the favourite animal?','dolphin','Lời nghe nói dolphin.',['dolphin','tiger','rabbit','elephant'],speech='My favourite animal is a dolphin.'),
        q('person-full','people','Card: An / Grade 5. Start with I am and write two sentences.','I am An. I am in Grade 5.','Viết đủ tên và lớp.',alternatives=['I’m An. I’m in Grade 5.']),
        q('home-at','homes','I live ___ 21 Rose Street.','at','At + số nhà và đường.'),
        q('home-in','homes','I live ___ a flat.','in','In + loại nhà.'),
        c('home-listen','homes','What is the address?','36 Green Street','Đọc đúng địa chỉ lời nghe.',['21 Rose Street','36 Green Street','18 Lake Street','42 Hill Street'],speech='My address is thirty-six Green Street.'),
        q('home-full','homes','Card: house. Answer with a full sentence starting with I live.','I live in a house.','I live in a house.'),
        q('dream-ing','dreams','I like ___ the flowers. Use water.','watering','Sau like dùng V-ing.'),
        q('dream-be','dreams','I would like to ___ a writer.','be','Would like to be + a + nghề.'),
        c('dream-listen','dreams','Why would the speaker like to be a reporter?','report the news','Lời nghe nói report the news.',['report the news','write stories','grow flowers','teach children'],speech='I would like to be a reporter because I would like to report the news.'),
        q('dream-reason','dreams','Card: writer / write stories. Start with Because I would.','Because I would like to write stories.','Đúng lý do của thẻ.',alternatives=['Because I’d like to write stories.'])]
    return dict(unit='R1',label='Review 1',overview='TongQuan_Review1.html',key='mia5:learn:en-r01-v1',intro='Ôn kết hợp Units 1–5: bản thân, nhà ở, bạn bè, sở thích và nghề nghiệp.',groups=[
        dict(id='people',name='Bản thân và bạn bè',tip='Favourite colour/animal khác nationality và personality. From Japan → Japanese; What is he/she like? hỏi tính cách.'),
        dict(id='homes',name='Nhà ở và địa chỉ',tip='Dùng địa chỉ giả định. In a house/flat; at + số nhà và tên đường. Do you…? — Yes, I do./No, I don’t.'),
        dict(id='dreams',name='Sở thích và ước mơ',tip='Like + V-ing; would like to be a + nghề; Because I would like to + động từ. Actor/theatre và put out fires có trong mở rộng trang 42–43.')],words=words,dialogues=dialogs,exercises=exercises)


def render_study():return render(data(),picture)
