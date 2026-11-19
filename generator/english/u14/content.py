"""Original habit and weekly-frequency practice, volume two pages 24-29."""
from english.practice import mc,text as base_text,match,reorder,tf,based,picture as image,field,listen,assemble

HABITS={'do morning exercise':('does morning exercise','tập thể dục buổi sáng'),'play sports':('plays sports','chơi thể thao'),'drink fresh juice':('drinks fresh juice','uống nước ép tươi'),'eat healthy food':('eats healthy food','ăn thức ăn tốt cho sức khỏe')}
CORE=list(HABITS)
IMAGE_NAMES=dict(zip(CORE,['do-morning-exercise','play-sports','drink-fresh-juice','eat-healthy-food']))
ACTIVITIES={'do yoga':'does yoga','play badminton':'plays badminton','drink orange juice':'drinks orange juice','eat vegetables':'eats vegetables'}
FREQUENCIES=['once a week','twice a week','three times a week','every day']
WEEK=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
PROFILES=[
    dict(name='An',pronoun='He',habit=CORE[0],activity='do yoga',days=['Monday']),
    dict(name='Linh',pronoun='She',habit=CORE[1],activity='play badminton',days=['Tuesday','Thursday']),
    dict(name='Minh',pronoun='He',habit=CORE[2],activity='drink orange juice',days=['Monday','Wednesday','Friday']),
    dict(name='Hoa',pronoun='She',habit=CORE[3],activity='eat vegetables',days=WEEK[:]),
    dict(name='Nam',pronoun='He',habit=CORE[0],activity='do yoga',days=['Tuesday','Thursday']),
    dict(name='Mai',pronoun='She',habit=CORE[1],activity='play badminton',days=['Monday','Wednesday','Friday'])]


def text(stem,answer,why,lesson=1,alternatives=()):
    accepted=list(alternatives)
    for source,variant in [('once a week','one time a week'),('twice a week','two times a week'),('three times a week','3 times a week'),('every day','daily')]:
        if source in answer:accepted.append(answer.replace(source,variant))
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short=answer.replace('does not',"doesn't").replace('do not',"don't").replace('He is',"He's").replace('She is',"She's")
        if short!=answer:accepted.append(short)
    return base_text(stem,answer,why,lesson,accepted)


def picture(activity,width=320):return image('u14',IMAGE_NAMES[activity],HABITS[activity][1],width)
def frequency(p):return {1:'once a week',2:'twice a week',3:'three times a week',7:'every day'}[len(p['days'])]
def habit_sentence(p):return f"{p['pronoun']} {HABITS[p['habit']][0]}."
def routine(p):return f"{p['pronoun']} {ACTIVITIES[p['activity']]} {frequency(p)}."
def card(p):return f"Name: {p['name']} · Pronoun: {p['pronoun']} · Habit: {p['habit']} · Tracked activity: {p['activity']} · Complete seven-day record, one session on each listed day: {', '.join(p['days'])}. No sessions on other days."
def passage(p):return f"This is {p['name']}. "+habit_sentence(p)+f" In this complete weekly record, {p['pronoun'].lower()} {ACTIVITIES[p['activity']]} on "+' and '.join(p['days'])+'. There are no sessions on other days.'
def shown(q,p):return based(q,card(p))


def warmup():
    a,b,c=PROFILES[:3]
    return [mc('Look at the picture. Choose the habit.',CORE,CORE[0],'Bạn nhỏ đang tập thể dục buổi sáng.',1,picture(CORE[0])),
        text('Complete: How ___ he stay healthy?','does','He dùng does trong câu hỏi.'),
        match([('do','does'),('play','plays'),('drink','drinks')],'He/she: does, plays, drinks.'),
        mc('Choose the correct habit sentence.',['She eats healthy food.','She eat healthy food.','She does eats healthy food.','She eating healthy food.'],'She eats healthy food.','Câu kể với she dùng eats.'),
        reorder('How does she stay healthy?','Sau does dùng stay nguyên mẫu.'),
        text('Complete: He ___ morning exercise. Use do.','does','Do → does với he.'),
        shown(mc('How often does An do yoga?',FREQUENCIES,frequency(a),'Một buổi trong tuần → once a week.',2),a),
        text('Complete: How ___ does she play badminton?','often','How often hỏi tần suất.',2),
        shown(text('Write only the tracked activity phrase.',b['activity'],'Play badminton.',2),b),
        reorder('He drinks fresh juice.','He dùng drinks.'),
        text('Complete: How often does he ___ yoga?','do','Sau does dùng do, không dùng does.',2),
        shown(tf([('The record has three orange-juice sessions.',True),('The record has a session on Sunday.',False)],'Minh có Monday, Wednesday, Friday.',2),c),
        shown(text('Write only the frequency phrase.',frequency(b),'Hai buổi → twice a week.',2),b),
        text('Complete: She plays badminton twice a ___.','week','Twice a week: hai lần mỗi tuần.',2),
        shown(text('Write the complete tracked-activity sentence, starting with He.',routine(a),'He does yoga once a week.',3),a),
        shown(text('Write the complete tracked-activity sentence, starting with She.',routine(b),'She plays badminton twice a week.',3),b),
        mc('Choose the correct question.',['How often does she eat vegetables?','How often does she eats vegetables?','How often do she eats vegetables?','How often she does eat vegetables?'],'How often does she eat vegetables?','Does + she + eat.',3),
        shown(text('Write two sentences: habit, then tracked activity with frequency. Start both with He.',habit_sentence(c)+' '+routine(c),'Phân biệt habit và tracked activity.',3),c)]


def vocabulary():return [
    *[mc('Look at the picture. Choose the habit.',CORE,k,'Tranh: '+HABITS[k][1]+'.',1,picture(k)) for k in CORE],
    text('Complete: fresh ___. Use the word meaning nước ép.','juice','Fresh juice.'),
    match([('once a week','một lần mỗi tuần'),('twice a week','hai lần mỗi tuần'),('three times a week','ba lần mỗi tuần')],'Không gán phần trăm cho các cụm tần suất.',2),
    mc('Which phrase means “ăn thức ăn tốt cho sức khỏe”?',CORE,CORE[3],'Eat healthy food.'),
    text('Complete: do morning exer___. Write the whole word.','exercise','Morning exercise.'),
    text('Complete: play bad___. Write the whole word.','badminton','Play badminton.',2),
    reorder('She does yoga once a week.','She does, không phải she do.',2),
    match([('do yoga','tập yoga'),('eat vegetables','ăn rau'),('drink orange juice','uống nước cam')],'Nhớ cụm động từ.',2),
    text('Complete: every ___. Use the word ngày.','day','Every day là hai từ.',2),
    shown(text('Write only the frequency phrase.',frequency(PROFILES[3]),'Đủ bảy ngày → every day.',2),PROFILES[3]),
    tf([('Twice means two times.',True),('Once a week means every day.',False)],'Once khác every day.',2),
    shown(text('Write only the tracked activity phrase.',PROFILES[2]['activity'],'Drink orange juice.',3),PROFILES[2]),
    shown(text('Write only the frequency phrase.',frequency(PROFILES[4]),'Cùng yoga nhưng Nam có hai buổi.',3),PROFILES[4]),
    based(match([(p['name'],p['activity']+' / '+frequency(p)) for p in PROFILES[:3]],'Khớp hoạt động và số buổi.',3),'\n'.join(card(p) for p in PROFILES[:3])),
    reorder('He eats vegetables every day.','Every day, không phải once a week.',3)]


def dialogue():
    a,b,c=PROFILES[:3]
    return [mc('How does she stay healthy? Choose a habit answer.',['She eats healthy food.','Twice a week.','On Monday.','At school.'],'She eats healthy food.','How…stay healthy hỏi cách/thói quen, không chỉ hỏi tần suất.'),
        text('Complete: How often ___ he do yoga?','does','He dùng does.',2),
        reorder('How often does she play badminton?','Does + play nguyên mẫu.',2),
        shown(mc('How often does An do yoga?',FREQUENCIES,frequency(a),'Một buổi đã ghi.',2),a),
        text('Rewrite in full: He doesn’t play sports.','He does not play sports.','Does not + play.'),
        text('Complete: She ___ fresh juice. Use drink.','drinks','She dùng drinks.'),
        shown(text('Give the complete tracked-activity sentence starting with She.',routine(b),'Có plays và twice a week.',2),b),
        shown(mc('How often does Minh drink orange juice?',FREQUENCIES,frequency(c),'Ba buổi trong tuần.',2),c),
        reorder('Does he eat healthy food?','Does + eat nguyên mẫu.'),
        text('Give a short negative answer in full form: Does she do yoga?','No, she does not.','Doesn’t = does not.'),
        text('Complete: How does she ___ healthy?','stay','Sau does dùng stay.'),
        match([('How does she stay healthy?','She plays sports.'),('How often does she play?','Twice a week.'),('Does she do yoga?','Yes, she does.')],'Nhận đúng loại câu hỏi.',2),
        shown(text('Give the habit sentence starting with He.',habit_sentence(a),'Does morning exercise.',2),a),
        tf([('How often asks about frequency.',True),('After does in a question, use plays.',False)],'Sau does dùng play.',3),
        shown(text('Write habit, then tracked activity with frequency. Start both with She.',habit_sentence(b)+' '+routine(b),'Đọc cả hai mục trong thẻ.',3),b),
        text('Rewrite in full: She doesn’t eat vegetables.','She does not eat vegetables.','Giữ eat nguyên mẫu.',3),
        shown(text('Write the tracked-activity sentence starting with He.',routine(PROFILES[4]),'Nam có hai buổi, khác An.',3),PROFILES[4]),
        mc('Choose the correct sentence.',['He plays sports regularly.','He play sports regularly.','He does plays sports regularly.','He playing sports regularly.'],'He plays sports regularly.','He + plays.',3)]


def reading():
    qs=[]
    for p in PROFILES[:4]:
        qs.extend(based(q,passage(p)) for q in [text('Who is the record about? Write the name only.',p['name'],'Tên trong câu đầu.',3),
            mc('How often is the tracked activity recorded?',FREQUENCIES,frequency(p),'Đếm buổi trong đủ bảy ngày, không đoán theo hoạt động.',3),
            text('Write only the tracked activity phrase, in base form.',p['activity'],'Lấy do/play/drink/eat nguyên mẫu.',3),
            tf([(f"The record includes {p['days'][0]}.",True),(f"There are {len(p['days'])+1} sessions in the complete weekly record.",False)],'Một buổi mỗi ngày đã ghi, không có buổi ở ngày khác.',3)])
    qs += [based(text('Who does yoga twice a week? Write the name only.','Nam','An và Nam cùng yoga, khác số buổi.',3),'\n'.join(card(p) for p in [PROFILES[0],PROFILES[4]])),
        based(mc('How often does Lan play badminton in this complete weekly record?',FREQUENCIES,'twice a week','Tuesday và Saturday là hai buổi.',3),'Lan plays badminton once on Tuesday and once on Saturday. She does not play on the other five days.')]
    return qs


def writing():
    a,b,c=PROFILES[:3]
    return [text('Complete: How does he ___ healthy?','stay','Does + stay.'),reorder('She drinks fresh juice.','She + drinks.'),
        text('Complete: He ___ sports. Use play.','plays','He + plays.'),text('Complete: She ___ morning exercise. Use do.','does','Do → does.'),
        mc('Choose the correct question.',['Does she eat vegetables?','Does she eats vegetables?','Do she eats vegetables?','She does eat vegetables?'],'Does she eat vegetables?','Does + she + eat.'),
        text('Complete: How often does she ___ badminton?','play','Play sau does.',2),
        match([('do','does'),('eat','eats'),('drink','drinks')],'Dạng câu kể he/she.'),
        reorder('He does yoga twice a week.','Twice a week.',2),
        text('Rewrite in full: He doesn’t drink orange juice.','He does not drink orange juice.','Does not + drink.',2),
        text('Complete: three ___ a week.','times','Three times a week.',2),
        shown(reorder(routine(b),'Đúng hoạt động và tần suất.',2),b),reorder('How often does he eat vegetables?','Does + eat.',2),
        text('Complete: She eats healthy ___.','food','Healthy food.'),
        text('Rewrite in full: She doesn’t do yoga.','She does not do yoga.','Does not + do.',2),
        shown(text('Write habit, then tracked activity with frequency. Start each sentence with He.',habit_sentence(a)+' '+routine(a),'Does morning exercise / does yoga once a week.',3),a),
        shown(text('Write the tracked-activity sentence starting with He.',routine(c),'Drinks orange juice three times a week.',3),c),
        shown(text('Write the tracked-activity sentence starting with She.',routine(PROFILES[3]),'Eats vegetables every day.',3),PROFILES[3]),
        shown(text('Write habit, then tracked activity with frequency. Start both with She.',habit_sentence(PROFILES[5])+' '+routine(PROFILES[5]),'Mai khác tần suất với Linh.',3),PROFILES[5])]


def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    return [listen('Listen and choose the habit phrase in base form.',f"To stay healthy, I {a['habit']}.",[field('Habit:',a['habit'],CORE)]),
        listen('Listen and choose the frequency.',f"I {b['activity']} {frequency(b)}.",[field('Frequency:',frequency(b),FREQUENCIES)],2),
        listen('Listen. Choose the weekly activity in base form.',f"This is {b['name']}. I {b['activity']} {frequency(b)}.",[field('Activity:',b['activity'],list(ACTIVITIES))],2),
        listen('Listen. Choose the frequency, not the activity.',f"{c['name']} says: I {c['activity']} {frequency(c)}.",[field('Frequency:',frequency(c),FREQUENCIES)],2),
        listen('Listen. Find both activity and frequency.',f"{a['name']} says: I {a['activity']} {frequency(a)}.",[field('Activity:',a['activity'],list(ACTIVITIES)),field('Frequency:',frequency(a),FREQUENCIES)],3),
        listen('Listen. Write only Mai’s activity and frequency, not Nam’s.',
            'Nam says: I do yoga once a week. Mai says: I play badminton three times a week.',
            [field('Mai’s activity:','play badminton'),field('Mai’s frequency:','three times a week')],3)]


def build_tests():
    import copy
    written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
    mixed=[copy.deepcopy(written[i%5][i]) for i in range(18)]
    return [assemble(qs,listening(i)) for i,qs in enumerate(written+[mixed])]
