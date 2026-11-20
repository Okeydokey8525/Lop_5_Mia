"""Original Review 3: printed 36-39, exactly Units 11-15."""
from english.practice import mc, text as base_text, match, reorder, tf, based, listen, field, assemble
from english.u11.content import picture as trip_picture
from english.u12.content import picture as tet_picture
from english.u13.content import picture as food_picture
from english.u14.content import picture as habit_picture

CORE = ['take photos', 'decorate the house', 'pizza', 'do morning exercise']
PAST = ['took photos', 'collected seashells', 'bought souvenirs', 'took a boat trip']
TET = ['decorate the house', 'do the shopping', 'make spring rolls', 'buy peach blossoms']
FOOD = ['pizza', 'burgers', 'chips', 'salads']
DRINK = ['apple juice', 'milk tea', 'lemonade', 'orange juice']
HABIT = ['plays sports', 'does morning exercise', 'drinks fresh juice', 'eats healthy food']
FREQ = ['once a week', 'twice a week', 'three times a week', 'every day']
ISSUE = ['headache', 'toothache', 'sore throat', 'stomach ache']
PROFILES = [dict(name=n, past=PAST[i % 4], tet=TET[(i+1) % 4], food=FOOD[i % 4], drink=DRINK[(i+1) % 4], habit=HABIT[i % 4], freq=FREQ[i % 4], issue=ISSUE[i % 4], advice=['have a rest', 'go to the dentist', 'drink warm water', 'go to the doctor'][i % 4]) for i,n in enumerate(['An','Linh','Minh','Hoa','Nam','Mai'])]
TET_PLACES=['a flower festival','a fireworks show','a New Year party','my grandparents’ house']
PARTY_ACTIVITIES=['sing','dance','play badminton','have a party']
for i,p in enumerate(PROFILES):
    p.update(tet_place=TET_PLACES[(i+i//4)%4],party_activity=PARTY_ACTIVITIES[(i+1+i//4)%4])


def text(stem, answer, why, lesson=1, alternatives=()):
    accepted = list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        for a,b in [('I will', "I'll"), ('We will', "We'll"), ('will not', "won't"), ('did not', "didn't"), ('should not', "shouldn't")]:
            if a in answer: accepted.append(answer.replace(a,b))
    if answer == 'twice a week': accepted.append('two times a week')
    if answer == 'once a week': accepted.append('one time a week')
    if answer == 'stomach ache': accepted.append('stomachache')
    return base_text(stem, answer, why, lesson, accepted)


def picture(word,width=320):
    return {'take photos':trip_picture,'decorate the house':tet_picture,'pizza':food_picture,'do morning exercise':habit_picture}[word](word,width)


def tag(q,*units):
    q['sourceUnits'] = list(units)
    return q


def card(p):
    return f"Fictional profile: {p['name']} · Last family trip: {p['past']} · Tet plan: {p['tet']} · Tet place: {p['tet_place']} · Special-day activity: {p['party_activity']} · Party food: {p['food']} · Party drink: {p['drink']} · Habit: {p['habit']} · Frequency: {p['freq']} · Health role-play: {p['issue']} · Advice line: {p['advice']}."


def passage(p):
    return f"My name is {p['name']}. On my last family trip, I {p['past']}. At Tet, I will {p['tet']}. I will go to {p['tet_place']}. On our special day next week, we will {p['party_activity']}. At our party, we will have {p['food']} and {p['drink']}. My brother {p['habit']} {p['freq']}. In our English role-play, I say, 'I have a {p['issue']}.' My partner says, 'You should {p['advice']}.'"


def shown(q,p,*units): return tag(based(q,card(p)),*units)


def written(index,kind):
    a,b,c = [PROFILES[(index+k)%6] for k in range(3)]
    if kind == 3:
        result = []
        for p in [a,b,c]:
            result += [tag(based(q,passage(p)),u) for q,u in [
                (text('Write only the last family-trip activity phrase.',p['past'],'Đọc last family trip, không lấy kế hoạch Tết.'),11),
                (text('Write only the Tet plan activity phrase.',p['tet'],'At Tet, I will + hoạt động.'),12),
                (text('Write the party food, then the drink, joined by and.',p['food']+' and '+p['drink'],'Đúng đồ ăn và đồ uống của cùng người.',2),13),
                (text('How often does the brother do the habit? Write the frequency phrase.',p['freq'],'Đọc tần suất của anh/em trai, không phải lời thoại.',2),14),
                (text('Write only the health problem in the role-play.',p['issue'],'Đọc lời thoại I have a…; đây là bài Anh giả định.',3),15),
                (text('Write the partner’s advice sentence, starting with You.',f"You should {p['advice']}.",'Theo lời thoại đã cho, không suy lời khuyên từ triệu chứng.',3),15)]]
        result[0] = tag(based(tf([(f"The speaker is {a['name']}.",True),(f"The speaker is {b['name']}.",False)],'Đọc người kể trong bài.'),passage(a)),11)
        result[1] = tag(based(mc('Which activity is the Tet plan?',TET,a['tet'],'Lấy dự định Tết trong bài đọc.'),passage(a)),12)
        result[7] = tag(based(text('Write only the place the speaker will go to at Tet.',b['tet_place'],'Đọc nơi đến dịp Tết, không lấy hoạt động.'),passage(b)),12)
        return result
    if kind == 4:
        result=[]
        for p in [a,b,c]:
            result += [shown(q,p,u) for q,u in [
                (text('Write the last-trip activity sentence, starting with I.',f"I {p['past']}.",'Câu kể quá khứ, không thêm did trước động từ quá khứ.'),11),
                (text('Write the Tet plan sentence, starting with I will.',f"I will {p['tet']}.",'Will + nguyên mẫu.'),12),
                (text('Write the party menu sentence: start with We will have; food before drink.',f"We will have {p['food']} and {p['drink']}.",'Đúng hai món và đúng thứ tự.',2),13),
                (text('Write the brother’s habit and frequency, starting with He.',f"He {p['habit']} {p['freq']}.",'He + động từ thêm s/es + tần suất.',2),14),
                (text('Write the role-play health problem, starting with I have.',f"I have a {p['issue']}.",'I have a…; không tự chẩn đoán.',3),15),
                (text('Write the advice line, starting with You should.',f"You should {p['advice']}.",'Should + nguyên mẫu; đúng lời thoại trong thẻ.',3),15)]]
        result[0]=tag(reorder('Did you take photos on the trip?','Did + take, không took.'),11)
        result[1]=tag(mc('Choose the correct future sentence.',['I will decorate the house.','I will decorates the house.','I will decorated the house.','I will decorating the house.'],'I will decorate the house.','Will + nguyên mẫu.'),12)
        result[7]=shown(text('Write the Tet destination sentence, starting with I will go to.',f"I will go to {b['tet_place']}.",'Will go to + nơi đến.'),b,12)
        result[8]=shown(text('Write the special-day activity sentence, starting with We will.',f"We will {b['party_activity']}.",'Will + hoạt động, không trả lời bằng món ăn.',2),b,13)
        return result
    if kind == 2:
        return [
            tag(mc('Did you collect seashells?',['Yes, I did.','Yes, I will.','Yes, I do.','Yes, I was.'],'Yes, I did.','Did you…? → I did.'),11),
            shown(text('Where will you go at Tet? Start with I will go to.',f"I will go to {a['tet_place']}.",'Where hỏi nơi sẽ đến.'),a,12),
            shown(text('What drink will you have? Start with We will have.',f"We will have {a['drink']}.",'What drink hỏi đồ uống.'),a,13),
            tag(text('Complete: How often ___ he play sports?','does','He dùng does.'),14),
            tag(mc('Which question asks about a health problem?',['What is the matter?','Where will you go?','What food will you have?','When did you go?'],'What is the matter?','What is the matter? hỏi vấn đề trong lời thoại.'),15),
            tag(reorder('Where will you go at Tet?','Where hỏi nơi, will + go.'),12),
            shown(text('Write the last-trip reply, starting with I.',f"I {a['past']}.",'Kể việc đã làm.',2),a,11),
            shown(text('How does the brother stay healthy? Write only his habit phrase.',b['habit'],'Lấy Habit, không lấy Frequency.',2),b,14),
            tag(text('Rewrite in full: I won’t buy peach blossoms.','I will not buy peach blossoms.','Won’t = will not.',2),12),
            tag(text('Complete: What food will you ___ at the party?','have','Will + have, không has.',2),13),
            tag(text('Rewrite in full: I didn’t take photos.','I did not take photos.','Didn’t = did not; giữ take nguyên mẫu.',2),11),
            tag(match([('Did you buy souvenirs?','Yes, I did.'),('How often does he play sports?','Twice a week.'),('What is the matter?','I have a headache.')],'Ghép đúng loại câu hỏi.',2),11,14,15),
            shown(text('Write the advice line, starting with You.',f"You should {c['advice']}.",'Theo lời thoại trong thẻ.',2),c,15),
            tag(tf([('After will, use a base verb.',True),('After does in a question, use plays.',False)],'Will + nguyên mẫu; does…play.',3),12,14),
            tag(text('Rewrite in full: You shouldn’t watch too much TV.','You should not watch too much TV.','Shouldn’t = should not; watch nguyên mẫu.',3),15),
            shown(text('Write food and drink in one sentence: start with We will have; food first.',f"We will have {b['food']} and {b['drink']}.",'Không lẫn món của người khác.',3),b,13),
            shown(text('Write the brother’s habit and frequency, starting with He.',f"He {c['habit']} {c['freq']}.",'Động từ thêm s/es và tần suất theo thẻ.',3),c,14),
            tag(text('Complete: What ___ your family do last weekend?','did','Last weekend đã qua; What did…do?',3),11)]
    result=[
        tag(mc('Choose the activity in the picture.',CORE,CORE[0],'Chụp ảnh, không phải kế hoạch suy ra từ ảnh.',1,picture(CORE[0])),11),
        shown(text('Write only the Tet plan activity phrase.',a['tet'],'Đọc Tet plan.'),a,12),
        shown(text('Write only the party food.',a['food'],'Food khác drink.'),a,13),
        shown(text('Write only the brother’s frequency phrase.',a['freq'],'Frequency nói bao nhiêu lần.'),a,14),
        shown(text('Write only the role-play health problem.',a['issue'],'Đọc Health role-play.'),a,15),
        tag(match([('took photos','đã chụp ảnh'),('will buy','sẽ mua'),('twice a week','hai lần mỗi tuần')],'Ghép nghĩa theo mốc thời gian.'),11,12,14),
        tag(text('Complete: Did you ___ souvenirs?','buy','Did + buy.'),11),
        tag(text('Complete: She ___ sports every day. Use play.','plays','She plays sports.'),14),
        shown(text('What will the group do on the special day? Write only the activity phrase.',b['party_activity'],'What…do hỏi hoạt động; không lấy đồ ăn hoặc đồ uống.',2),b,13),
        tag(reorder('You should have a rest.','Should + have, không has.',2),15),
        shown(mc('Where will this pupil go at Tet?',TET_PLACES,b['tet_place'],'Đọc Tet place, không lấy Tet plan.',2),b,12),
        tag(text('Complete: He ___ morning exercise. Use do.','does','He does morning exercise.',2),14),
        shown(text('Write only the last-trip activity phrase.',c['past'],'Đã qua, không lấy kế hoạch.',2),c,11),
        tag(tf([('Will you…? asks about the future.',True),('Did you…? asks about next week.',False)],'Phân biệt will và did.',3),11,12),
        shown(text('Write the menu sentence, starting with We will have; food first.',f"We will have {c['food']} and {c['drink']}.",'Ghép đúng hai mục trong thẻ.',3),c,13),
        shown(text('Write the role-play advice, starting with You.',f"You should {b['advice']}.",'Theo lời thoại, không suy ra một cách chữa bệnh.',3),b,15),
        shown(text('Write the brother’s habit and frequency, starting with He.',f"He {a['habit']} {a['freq']}.",'Đúng habit và frequency.',3),a,14),
        shown(text('Write last-trip then Tet plan as two sentences, both starting with I.',f"I {c['past']}. I will {c['tet']}.",'Quá khứ trước, dự định sau.',3),c,11,12)]
    if kind == 1:
        result[:4]=[tag(mc('Choose the phrase for this picture.',CORE,k,'Nhận ra chủ thể trong tranh.',1,picture(k)),u) for k,u in zip(CORE,[11,12,13,14])]
        result[12]=tag(based(mc('Extension: Which food group is milk in?',['dairy','grains','protein','fruit and vegetables'],'dairy','Theo bảng học từ của Extension trang 38–39.',2),'Extension word card: milk → dairy; rice → grains; fish → protein; carrot → fruit and vegetables.'),14)
    return result


def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    return [
        tag(listen('Listen and choose the last-trip activity.',f"On my last family trip, I {a['past']}.",[field('Activity:',a['past'],PAST)]),11),
        tag(listen('Listen and choose the Tet plan.',f"At Tet, I will {b['tet']}.",[field('Plan:',b['tet'],TET)]),12),
        tag(listen('Listen and choose the party drink.',f"At our party, we will have {c['food']} and {c['drink']}.",[field('Drink:',c['drink'],DRINK)],2),13),
        tag(listen('Listen for the brother’s frequency.',f"My brother {a['habit']} {a['freq']}.",[field('Frequency:',a['freq'],FREQ)],2),14),
        tag(listen('Listen and find the role-play problem and advice.',f"In our English role-play, {b['name']} says, I have a {b['issue']}. The partner says, You should {b['advice']}.",[field('Problem:',b['issue'],ISSUE),field('Advice phrase:',b['advice'])],3),15),
        tag(listen('Listen and write the past activity, then the Tet plan.',f"Last weekend, I {c['past']}. At Tet, I will {c['tet']}.",[field('Past activity:',c['past']),field('Tet plan:',c['tet'])],3),11,12)]


def build_tests():
    return [assemble(written(i,i) if i<5 else [written(i,k%5)[k] for k in range(18)],listening(i)) for i in range(6)]
