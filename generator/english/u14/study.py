"""Habits, complete weekly records and do/does practice."""
from english.u14.content import CORE,HABITS,ACTIVITIES,FREQUENCIES,picture
from english.study.author import word as w,question as q,choice as c,dialogue as d
from english.study.render import render_study as render


def data():
    words=[w('habits','healthy','khỏe mạnh','She wants to stay healthy.')]
    words += [w('habits',k,HABITS[k][1],'She '+HABITS[k][0]+'.',image=k) for k in CORE]
    words += [w('frequency',k,vn,'He '+ACTIVITIES[k]+'.') for k,vn in [('do yoga','tập yoga'),('play badminton','chơi cầu lông'),('drink orange juice','uống nước cam'),('eat vegetables','ăn rau')]]
    words += [w('frequency',k,vn,example) for k,vn,example in [('once a week','một lần mỗi tuần','He does yoga once a week.'),('twice a week','hai lần mỗi tuần','She plays badminton twice a week.'),('three times a week','ba lần mỗi tuần','He drinks orange juice three times a week.'),('every day','mỗi ngày','She eats vegetables every day.')]]
    words += [w('story',k,vn,example) for k,vn,example in [('regularly','đều đặn','He plays sports regularly.'),('every morning','mỗi buổi sáng','She does exercise every morning.'),('stay healthy','giữ sức khỏe','How does he stay healthy?')]]
    dialogs=[d('habits','Một thói quen','How does she stay healthy?','She eats healthy food.','Câu kể she dùng eats; câu hỏi does + stay.'),
        d('habits','Tập thể dục','How does he stay healthy?','He does morning exercise.','Do → does khi kể với he.'),
        d('frequency','Một buổi yoga','How often does he do yoga?','He does yoga once a week.','Sau does trong câu hỏi dùng do; câu kể dùng does.'),
        d('frequency','Hai buổi cầu lông','How often does she play badminton?','She plays badminton twice a week.','Câu hỏi play; câu kể plays.'),
        d('story','Nhớ động từ nguyên mẫu','Does she drink fresh juice?','Yes, she does. She drinks fresh juice.','Does + drink; She drinks.'),
        d('story','Đọc đủ tuần','How often does he play badminton?','Three times a week: on Monday, Wednesday and Friday.','Đếm ba buổi theo lịch giả định, không đoán từ tên hoạt động.')]
    exercises=[c('habits-listen','habits','Which habit is named?','eat healthy food','Nghe eat healthy food.',CORE,speech='To stay healthy, I eat healthy food.'),
        q('habits-does','habits','He ___ morning exercise. Use do.','does','He + does.'),
        q('habits-drinks','habits','She ___ fresh juice. Use drink.','drinks','She + drinks.'),
        q('habits-stay','habits','How does he ___ healthy?','stay','Does + stay nguyên mẫu.'),
        c('frequency-listen','frequency','How often does the speaker do yoga?','twice a week','Nghe twice a week.',FREQUENCIES,speech='I do yoga twice a week.'),
        q('frequency-base','frequency','How often does she ___ yoga?','do','Sau does dùng do, không dùng does.'),
        q('frequency-count','frequency','Complete seven-day record: one badminton session on Tuesday and one on Saturday, none on other days. Complete: ___ a week.','twice','Hai buổi trong tuần.'),
        q('frequency-times','frequency','Three ___ a week.','times','Three times a week.'),
        c('story-listen','story','How often does the speaker play badminton?','three times a week','Nghe đúng lịch của người nói.',FREQUENCIES,speech='I play badminton three times a week, on Monday, Wednesday and Friday.'),
        q('story-full','story','Rewrite in full: He doesn’t play sports.','He does not play sports.','Doesn’t = does not; giữ play.'),
        q('story-often','story','How ___ does she eat vegetables?','often','How often hỏi tần suất.'),
        q('story-sentence','story','Card: she / play badminton / twice a week. Write one sentence in this order.','She plays badminton twice a week.','She + plays; đúng tần suất.')]
    return dict(unit=14,key='mia5:learn:en-u14-v1',intro='Học cách nói thói quen, đọc lịch đủ tuần và hỏi tần suất. Nghe kèm bài, nghe chậm và ABC.',groups=[
        dict(id='habits',name='Thói quen hằng ngày',tip='How does he/she stay healthy? — He/She + động từ thêm s/es. Do → does; play → plays; drink → drinks; eat → eats.'),
        dict(id='frequency',name='Bao nhiêu lần mỗi tuần?',tip='How often does he/she + nguyên mẫu? Once / twice / three times a week; every day. Lịch trong bài đủ bảy ngày, mỗi ngày được ghi là một buổi. Đếm buổi, không đoán tần suất từ hoạt động.'),
        dict(id='story',name='Đọc và kể thói quen',tip='Câu hỏi does + do/play/drink/eat; câu kể he/she does/plays/drinks/eats. Regularly nghĩa đều đặn, không phải một con số cố định. Các lịch là giả định phục vụ học tiếng Anh; ABC là tên chữ cái, không phải phonics.')],words=words,dialogues=dialogs,exercises=exercises)


def render_study():return render(data(),picture)
