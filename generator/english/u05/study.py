"""Original future-job companion; choices and reasons are fictional."""
from english.u05.content import JOBS, CORE, picture
from english.study.author import word as w, question as q, choice as c, dialogue as d
from english.study.render import render_study as render


def data():
    words=[w('jobs',job,values[0],'I would like to be a '+job+'.',**({'image':job} if job in CORE else {})) for job,values in JOBS.items()]
    words += [w('dreams',name,vn,example) for name,vn,example in [
        ('would like','muốn (cách nói lịch sự)','I would like to be a writer.'),('future','tương lai','I would like to be a teacher in the future.'),
        ('be a reporter','trở thành phóng viên','She would like to be a reporter.'),('be a gardener','trở thành người làm vườn','He would like to be a gardener.')]]
    words += [w('reasons',name,vn,'I would like to '+name+'.',**({'image':job} if job in CORE else {})) for name,vn,job in [
        ('help people','giúp đỡ mọi người','firefighter'),('report the news','đưa tin','reporter'),('grow flowers','trồng hoa','gardener'),
        ('write stories','viết truyện','writer'),('teach children','dạy trẻ em','teacher')]]
    dialogues=[
        d('jobs','Nhận biết nghề','Is she a firefighter?','Yes, she is a firefighter.','Nghề nghiệp không phụ thuộc giới tính.'),
        d('jobs','Nghề của nhân vật','Is he a reporter?','No, he is a writer.','Reporter: phóng viên; writer: nhà văn.'),
        d('dreams','Ước mơ','What would you like to be in the future?','I would like to be a gardener.','Bạn muốn làm nghề gì trong tương lai? — Người làm vườn.'),
        d('dreams','Trả lời ngắn','Would you like to be a teacher?','Yes, I would.','I’d = I would trong mẫu ước mơ nghề nghiệp.'),
        d('reasons','Vì sao thích viết?','Why would you like to be a writer?','Because I would like to write stories.','Đây là lý do của nhân vật, không phải lý do duy nhất để chọn nghề.'),
        d('reasons','Vì sao muốn làm giáo viên?','Why would you like to be a teacher?','Because I would like to teach children.','Because mở đầu câu nêu lý do.'),
    ]
    exercises=[
        c('job-listen','jobs','Which job does the speaker want?','reporter','Lời nghe nói reporter.',list(JOBS),speech='I would like to be a reporter.'),
        q('job-spell','jobs','w r i _ e r — Write the whole word.','writer','Writer có chữ t trước e.'),
        c('job-garden','jobs','Which job means “người làm vườn”?','gardener','Gardener là người làm vườn.',list(JOBS)),
        q('job-article','jobs','I would like to be ___ doctor.','a','Dùng a trước doctor.'),
        q('dream-be','dreams','I would like to ___ a firefighter.','be','Would like to be + a + nghề.'),
        q('dream-question','dreams','What ___ you like to be in the future?','would','What would you like to be…?'),
        q('dream-full-form','dreams','In this job sentence, write the full form of I’d.','I would','Yêu cầu dạng đầy đủ: I would.'),
        q('dream-full','dreams','Card: She / writer. Start with She would and include in the future.','She would like to be a writer in the future.','She would like to be a writer in the future.'),
        c('reason-listen','reasons','Why would the speaker like to be a gardener?','grow flowers','Lời nghe nói grow flowers.',list(dict.fromkeys(v[1] for v in JOBS.values())),speech='I would like to be a gardener because I would like to grow flowers.'),
        q('reason-because','reasons','___ I would like to help people.','Because','Because dùng để mở đầu lý do.'),
        q('reason-teach','reasons','I would like to ___ children.','teach','Teach children là dạy trẻ em.'),
        q('reason-full','reasons','Why would you like to be a writer? Card: write stories. Start with Because.','Because I would like to write stories.','Because I would like to write stories.',alternatives=['Because I’d like to write stories.']),
    ]
    return dict(unit=5,key='mia5:learn:en-u05-v1',intro='Khám phá nghề nghiệp, nói ước mơ và lý do theo thẻ nhân vật. Em có thể có ước mơ khác.',groups=[
        dict(id='jobs',name='Nghề nghiệp',tip='A firefighter/reporter/gardener/writer/doctor/teacher. TEA-cher nhấn âm đầu. Dent-ist (nha sĩ) cũng nhấn âm đầu; không đoán nghề theo giới tính.'),
        dict(id='dreams',name='Ước mơ',tip='What would you like to be in the future? — I would like to be a… I’d/He’d/She’d = I would/He would/She would trong ngữ cảnh này. Nếu bài yêu cầu dạng đầy đủ thì viết đầy đủ.'),
        dict(id='reasons',name='Lý do',tip='Why…? — Because I would like to + động từ nguyên mẫu. Report the news, grow flowers, write stories, teach children, help people. Nhiều nghề có thể giúp mọi người.')],words=words,dialogues=dialogues,exercises=exercises)


def render_study():return render(data(),picture)
