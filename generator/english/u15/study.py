"""Health vocabulary and scripted advice, not medical assessment."""
from english.u15.content import CORE,MEANINGS,ADVICE,picture
from english.study.author import word as w,question as q,choice as c,dialogue as d
from english.study.render import render_study as render


def data():
    words=[w('health',k,vn,'I have a '+k+'.',image=k) for k,vn in zip(CORE,MEANINGS)]
    words += [w('advice',k,vn,example) for k,vn,example in [('go to the dentist','đến nha sĩ','In the role-play, the partner says: You should go to the dentist.'),('have a rest','nghỉ ngơi','In the role-play, the partner says: You should have a rest.'),('drink warm water','uống nước ấm','Our card says: You should drink warm water.'),('go to the doctor','đến bác sĩ','Our card says: You should go to the doctor.'),('take some medicine','uống/dùng thuốc','Take some medicine is a phrase in our English lesson. Ask an adult for help.'),('rinse your mouth with salt water','súc miệng bằng nước muối','We read the phrase rinse your mouth with salt water in our English lesson.')]]
    words += [w('talk',k,vn,example) for k,vn,example in [('should','nên','What should I do?'),('should not','không nên','The card says: You should not watch too much TV.'),('advice','lời khuyên','Thanks for your advice.'),('I do not feel well','mình cảm thấy không khỏe','I do not feel well. I will tell an adult.'),('What is the matter','có chuyện gì/vấn đề gì vậy','What is the matter?'),('Thanks for your advice','cảm ơn lời khuyên của bạn','Thanks for your advice. You are welcome.')]]
    dialogs=[d('health','Hỏi thăm','What is the matter?','I have a headache.','I have a + vấn đề sức khỏe; không dùng I am a headache.'),
        d('health','Nói cảm giác','Are you OK?','I do not feel well. I have a sore throat.','Do not feel well = không cảm thấy khỏe.'),
        d('advice','Đọc thẻ nha sĩ','What should I do?','Our role-play card says: You should go to the dentist.','Should + go nguyên mẫu; đọc đúng thẻ, không tự chọn cách chữa.'),
        d('advice','Đọc thẻ nghỉ ngơi','What does our role-play card say?','You should have a rest.','Sau should dùng have, không dùng has.'),
        d('talk','Cảm ơn','Thanks for your advice.','You are welcome.','Đáp lời cảm ơn lịch sự.'),
        d('talk','Câu phủ định trong bài','What is the negative line on our card?','You should not watch too much TV.','Should not = shouldn’t; giữ watch nguyên mẫu.')]
    exercises=[c('health-listen','health','Which health phrase is used?','sore throat','Nghe sore throat.',CORE,speech='I have a sore throat.'),
        q('health-have','health','I ___ a headache. Use have.','have','I have; he/she has.'),
        q('health-has','health','She ___ a toothache. Use have.','has','She has.'),
        q('health-throat','health','I have a sore ___.','throat','Sore throat.'),
        c('advice-listen','advice','Which positive line is on the card?','go to the dentist','Nghe câu trong thẻ.',ADVICE,speech='Our role-play card says: You should go to the dentist.'),
        q('advice-base','advice','You should ___ a rest. Use have.','have','Should + have, không dùng has.'),
        q('advice-go','advice','She should ___ to the doctor.','go','Should + go.'),
        q('advice-warm','advice','Our English card says: drink ___ water. Use ấm.','warm','Warm water, không tự suy cách chữa.'),
        c('talk-listen','talk','Which negative verb phrase is used?','watch too much TV','Nghe should not watch too much TV.',['watch too much TV','drink cold water','eat ice cream very often'],speech='The negative line on the card is: You should not watch too much TV.'),
        q('talk-full','talk','Rewrite in full: You shouldn’t watch too much TV.','You should not watch too much TV.','Shouldn’t = should not.'),
        q('talk-thanks','talk','Thanks for your ___.','advice','Advice: lời khuyên.'),
        q('talk-sentence','talk','Card: I / have / a headache. Write one complete sentence in this order.','I have a headache.','I have a + health phrase.')]
    return dict(unit=15,key='mia5:learn:en-u15-v1',intro='Học từ để nói khi không khỏe và luyện hội thoại hỏi thăm. Đây là bài tiếng Anh; khi không khỏe, báo người lớn và không tự dùng thuốc.',groups=[
        dict(id='health',name='Nói khi không khỏe',tip='What’s the matter? = What is the matter? — I have a…; He/She has a… Tranh giúp nhận biết từ và vị trí, không dùng để chẩn đoán người thật.'),
        dict(id='advice',name='Lời thoại với should',tip='What should I do? — You should + nguyên mẫu. Thẻ trong bài giao sẵn lời thoại, không yêu cầu tự chọn cách chữa. Take some medicine và rinse… là cụm từ của sách; không có tên thuốc, liều hay công thức pha.'),
        dict(id='talk',name='Quan tâm và đáp lời',tip='Shouldn’t = should not; What’s = What is; don’t = do not. Thanks for your advice. — You are welcome. Nhấn WHAT / MATTER hoặc WHAT / DO trong câu hỏi, đọc cả cụm; ABC đọc tên chữ cái.')],words=words,dialogues=dialogs,exercises=exercises)


def render_study():return render(data(),picture)
