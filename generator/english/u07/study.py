"""Learning companion for verified Unit 7 pages 50–55."""
from english.u07.content import ACTIVITIES, picture
from english.study.render import render_study as render


def word(group,name,meaning,example,**extra):return dict(id=name.replace(' ','-'),word=name,group=group,meaning=meaning,example=example,**extra)
def question(id,group,title,prompt,answer,hint,kind='text',instruction='Viết câu trả lời tiếng Anh.',**extra):return dict(id=id,group=group,title=title,prompt=prompt,answer=answer,hint=hint,kind=kind,instruction=instruction,**extra)


def data():
    words=[word('activities',base,vn,'We '+base+' at school.',image=base) for base,(_,vn) in ACTIVITIES.items()]
    words += [word('likes',ing,vn+' (dạng V-ing)','She likes '+ing+'.',image=base) for base,(ing,vn) in ACTIVITIES.items()]
    words += [word('reasons',name,meaning,'He thinks it is '+name+'.',image=image) for name,meaning,image in [
        ('fun','vui','play games'),('interesting','thú vị','read books'),('useful','hữu ích','solve maths problems'),('good for group work','tốt cho làm việc nhóm','do projects')]]
    dialogues=[
        dict(group='activities',title='Bạn ấy thích hoạt động nào?',a='What school activity does he like?',b='He likes reading books.',meaning='Bạn ấy thích hoạt động nào ở trường? — Bạn ấy thích đọc sách.'),
        dict(group='activities',title='Hỏi về bạn nữ',a='What school activity does she like?',b='She likes doing projects.',meaning='She likes doing projects: bạn ấy thích làm dự án.'),
        dict(group='likes',title='Trả lời có',a='Does she like solving maths problems?',b='Yes, she does.',meaning='Bạn ấy thích giải toán phải không? — Đúng vậy.'),
        dict(group='likes',title='Trả lời không rồi nói sở thích',a='Does he like playing games?',b='No, he does not. He likes reading books.',meaning='Bạn ấy không thích chơi trò chơi; bạn ấy thích đọc sách. Doesn’t = does not.'),
        dict(group='reasons',title='Vì sao bạn ấy thích?',a='Why does she like doing projects?',b='Because she thinks it is good for group work.',meaning='Bạn ấy thích làm dự án vì nghĩ hoạt động này tốt cho làm việc nhóm.'),
        dict(group='reasons',title='Vì sao bạn ấy không thích?',a='Why does he not like solving maths problems?',b='Because he thinks they are not interesting.',meaning='Trong ví dụ này bạn ấy không thấy các bài toán thú vị. Đây là ý kiến của nhân vật, không là nhận xét chung về môn Toán.'),
    ]
    q=question
    exercises=[
        q('activity-picture','activities','Listen and choose the picture.','', 'do-projects','Các bạn đang cùng làm một dự án.',kind='picture',options=list(ACTIVITIES.keys()),speech='do projects',instruction='Nghe hoạt động rồi chọn tranh.'),
        q('activity-spell','activities','Complete the word.','p r o j e _ t s','projects','Projects có chữ c sau e.',instruction='Viết cả từ tiếng Anh.'),
        q('activity-read','activities','Choose the activity.','Which phrase means “đọc sách”?','read books','Read books là đọc sách.',kind='choice',options=list(ACTIVITIES),instruction='Chọn cụm từ đúng.'),
        q('activity-solve','activities','Complete the phrase.','solve maths ___','problems','Solve maths problems là giải các bài toán.',instruction='Điền từ còn thiếu.'),
        q('likes-reading','likes','Complete the sentence.','He likes ___ books.','reading','Sau likes dùng V-ing: reading.',instruction='Điền dạng V-ing của read.'),
        q('likes-question','likes','Complete the question.','What school activity does she ___?','like','Sau does dùng like, không thêm s.',instruction='Điền một từ còn thiếu.'),
        q('likes-listen','likes','Listen and choose.','Which activity does she like?','solving maths problems','Lời nghe nói She likes solving maths problems.',kind='choice',options=[v[0] for v in ACTIVITIES.values()],speech='She likes solving maths problems.',instruction='Nghe rồi chọn hoạt động đúng.'),
        q('likes-negative','likes','Complete the short answer.','Does he like playing games? No, he ___.','does not','No, he does not. Cũng có thể viết doesn’t.',alternatives=['doesn’t'],instruction='Điền does not hoặc dạng viết tắt.'),
        q('reason-listen','reasons','Listen for the reason.','Why does he like reading books?','interesting','Lời nghe nói he thinks it is interesting.',kind='choice',options=['fun','interesting','useful','good for group work'],speech='He likes reading books because he thinks it is interesting.',instruction='Nghe rồi chọn lý do của nhân vật.'),
        q('reason-group','reasons','Complete the reason.','It is good ___ group work.','for','Good for group work là tốt cho làm việc nhóm.',instruction='Điền một từ còn thiếu.'),
        q('reason-thinks','reasons','Complete the reply.','Because she ___ it is fun.','thinks','She thinks, thêm s ở thinks.',instruction='Điền dạng đúng của think.'),
        q('reason-full','reasons','Write a complete reason.','Why does he like solving maths problems? Card: useful.','Because he thinks it is useful.','Because he thinks it is useful.',alternatives=['Because he thinks it’s useful.'],instruction='Viết câu bắt đầu bằng Because, dùng he và lý do trong thẻ.'),
    ]
    # Picture choices use stable word IDs, while each image depicts the base action.
    exercises[0]['options']=[w.replace(' ','-') for w in exercises[0]['options']]
    return dict(unit=7,key='mia5:learn:en-u07-v1',intro='Hoạt động yêu thích ở trường, likes + V-ing và lý do: học từng nhóm, nghe rồi thử nói.',groups=[
        dict(id='activities',name='Hoạt động',tip='Do projects, read books, play games, solve maths problems. Nhớ theo cả cụm, không chỉ từng từ rời.'),
        dict(id='likes',name='Likes + V-ing',tip='He/She likes + V-ing. Trong câu hỏi does…like, like không thêm s. READ-ing và SOLV-ing nhấn âm đầu. Does not = doesn’t.'),
        dict(id='reasons',name='Lý do',tip='Why hỏi lý do; Because mở đầu câu trả lời. He/She thinks it is… Một hoạt động có thể có nhiều lý do tùy người; đọc đúng thẻ hoặc lời nghe.'),
    ],words=words,dialogues=dialogues,exercises=exercises)


def render_study():return render(data(),picture)
