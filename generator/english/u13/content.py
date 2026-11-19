"""Original special-day plans and menus, printed pages 18-23, volume two."""
from english.practice import mc,text as base_text,match,reorder,tf,based,picture as image,field,listen,assemble

CORE=['pizza','burgers','milk tea','apple juice']
MEANINGS=['bánh pizza','bánh mì kẹp thịt','trà sữa','nước ép táo']
IMAGE_NAMES=dict(zip(CORE,['pizza','burgers','milk-tea','apple-juice']))
FOODS=['pizza','burgers','chicken and rice','fish and chips']
DRINKS=['apple juice','milk tea','lemonade','water']
EVENTS=["Children’s Day","Teachers’ Day",'Sports Day','Mid-Autumn Festival']
ACTIVITIES=['dance','sing','play badminton','have a party']
PROFILES=[
    dict(name='An',event=EVENTS[0],prep='on',activity='dance',food='pizza',drink='apple juice',day='Sunday',place='my home'),
    dict(name='Linh',event=EVENTS[1],prep='on',activity='sing',food='burgers',drink='milk tea',day='Monday',place='our classroom'),
    dict(name='Minh',event=EVENTS[2],prep='on',activity='play badminton',food='chicken and rice',drink='water',day='Saturday',place='our school'),
    dict(name='Hoa',event=EVENTS[3],prep='at',activity='have a party',food='fish and chips',drink='lemonade',day='Friday',place='my home'),
    dict(name='Nam',event=EVENTS[0],prep='on',activity='sing',food='burgers',drink='water',day='Saturday',place='our classroom'),
    dict(name='Mai',event=EVENTS[1],prep='on',activity='dance',food='pizza',drink='lemonade',day='Sunday',place='our school')]


def text(stem,answer,why,lesson=1,alternatives=()):
    accepted=list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short=answer.replace('will not',"won't").replace('We will',"We'll").replace('They will',"They'll").replace('I will',"I'll")
        if short!=answer:accepted.append(short)
    return base_text(stem,answer,why,lesson,accepted)


def picture(word,width=320):return image('u13',IMAGE_NAMES[word],MEANINGS[CORE.index(word)],width)
def action(p):return f"We will {p['activity']} {p['prep']} {p['event']}."
def menu(p):return f"We will have {p['food']} and {p['drink']}."
def card(p):return f"Speaker: {p['name']} · Event: {p['event']} · Activity: {p['activity']} · Food: {p['food']} · Drink: {p['drink']} · Day: {p['day']} · Place: {p['place']}."
def passage(p):return f"My name is {p['name']}. Our party will be on {p['day']} at {p['place']}. "+action(p)+' '+menu(p)
def shown(q,p):return based(q,card(p))


def warmup():
    a,b,c=PROFILES[:3]
    return [mc('Look at the picture. Choose the word.',CORE,'pizza','Pizza có đế tròn và topping.',2,picture('pizza')),
        text('Complete: What will you ___ on Children’s Day?','do','What will you do?'),
        match([('dance','nhảy/múa'),('sing','hát'),('play badminton','chơi cầu lông')],'Ghép hoạt động.'),
        mc('Choose a drink.',['pizza','burgers','apple juice','fish and chips'],'apple juice','Apple juice là nước ép táo; ba đáp án còn lại là đồ ăn.',2),
        reorder('We will sing on Teachers’ Day.','Will + sing.'),
        text('Complete: We will ___ a party.','have','Have a party.'),
        shown(mc('What food will they have?',FOODS,b['food'],'Tìm mục Food.',2),b),
        text('Complete: What ___ will you have? Ask about beverages.','drinks','Drinks hỏi đồ uống.',2),
        shown(text('Write only the activity phrase.',c['activity'],'Play badminton.'),c),
        reorder('What drinks will you have at the party?','Drinks đứng trước will.',2),
        shown(text('Write only the drink phrase.',a['drink'],'Apple juice.',2),a),
        tf([('We will have pizza names food.',True),('Milk tea is an activity.',False)],'Tách food, drinks và activities.',2),
        text('Complete: ___ Sports Day, we will play badminton.','On','On + tên ngày.',1),
        shown(text('Write only the day of the party.',b['day'],'Monday.',3),b),
        shown(text('Write the complete activity sentence starting with We will.',action(a),'Dùng on Children’s Day.',3),a),
        shown(text('Write one menu sentence starting with We will have: food first, then drink.',menu(b),'Burgers trước milk tea.',3),b),
        mc('Choose the correct question.',['What food will you have?','What food will you has?','What food you will have?','What food will you having?'],'What food will you have?','Will + you + have.',3),
        shown(text('Write activity, then menu. Start both sentences with We will; food before drink.',action(c)+' '+menu(c),'Dữ kiện cùng một thẻ.',3),c)]


def vocabulary():return [
    *[mc('Look at the picture. Choose the word.',CORE,k,'Tranh: '+MEANINGS[CORE.index(k)]+'.',2,picture(k)) for k in CORE],
    text('Complete: apple ___.','juice','Apple juice: nước ép táo.',2),
    match([('pizza','food'),('milk tea','drink'),('dance','activity')],'Ba nhóm nghĩa.',2),
    mc('Which phrase means “bánh mì kẹp thịt”?',CORE,'burgers','Burgers.',2),
    text('Complete: milk ___.','tea','Milk tea: trà sữa.',2),
    text('Complete: play bad___. Write the whole word.','badminton','Badminton: cầu lông.'),
    reorder('We will have burgers and apple juice.','Food trước drink.',2),
    match([(EVENTS[0],'ngày Thiếu nhi'),(EVENTS[1],'ngày Nhà giáo'),(EVENTS[2],'ngày Thể thao')],'Các ngày trong bài.',1),
    text('Complete: Mid-Autumn ___.','Festival','Tết Trung thu.',1),
    shown(text('Write only the food phrase.',PROFILES[3]['food'],'Fish and chips là đồ ăn.',2),PROFILES[3]),
    tf([('Lemonade is a drink.',True),('Burgers is the name of a drink.',False)],'Đọc đúng nhóm.',2),
    shown(text('Write only the drink phrase.',PROFILES[2]['drink'],'Water, không lấy chicken and rice.',3),PROFILES[2]),
    shown(text('Write only the activity phrase.',PROFILES[3]['activity'],'Have a party.',3),PROFILES[3]),
    based(match([(p['name'],p['food']+' / '+p['drink']) for p in PROFILES[:3]],'Đối chiếu cả món và đồ uống.',3),'\n'.join(card(p) for p in PROFILES[:3])),
    reorder('What food will they have at the party?','What food hỏi đồ ăn.',3)]


def dialogue():
    a,b,c=PROFILES[:3]
    return [mc('What will you do on Sports Day? Choose a sport activity answer.',['We will play badminton.','We will have apple juice.','On Saturday.','At our school.'],'We will play badminton.','Câu yêu cầu hoạt động thể thao: play badminton.'),
        text('Complete: What food ___ you have at the party?','will','What food will you have?',2),
        reorder('What will you do on Children’s Day?','Will + you + do.'),
        shown(mc('What drinks will they have?',DRINKS,b['drink'],'Tìm mục Drink.',2),b),
        text('Rewrite in full: We’ll have pizza.','We will have pizza.','We’ll = We will.',2),
        text('Complete: We will ___ on Teachers’ Day. Use sing.','sing','Không thêm s.'),
        shown(text('Answer with the complete activity sentence, starting with We will.',action(a),'On Children’s Day.'),a),
        shown(mc('What food will they have?',FOODS,c['food'],'Chicken and rice.',2),c),
        reorder('Will you come to my birthday party?','Will đứng trước you.',2),
        text('Rewrite in full: They’ll dance.','They will dance.','They’ll = They will.'),
        text('Complete: We will have a party ___ Mid-Autumn Festival.','at','Sách dùng at Mid-Autumn Festival.'),
        match([('What food will you have?','Pizza.'),('What drinks will you have?','Apple juice.'),('What will you do?','Dance.')],'Phân biệt food/drinks/do.',2),
        shown(text('Write one menu sentence with food first, then drink, starting with We will have.',menu(c),'Giữ chicken and rice trước water.',2),c),
        tf([('What drinks asks about beverages.',True),('What will you do asks only about food.',False)],'Nhận đúng loại câu hỏi.',3),
        shown(text('Write activity, then menu, starting each sentence with We will; food before drink.',action(b)+' '+menu(b),'Đúng on Teachers’ Day.',3),b),
        text('Give a short negative answer in full form: Will you dance?','No, I will not.','Will not = won’t.',3),
        shown(text('Write the activity sentence starting with We will.',action(PROFILES[3]),'At Mid-Autumn Festival.',3),PROFILES[3]),
        mc('Choose the correct sentence.',['They will have milk tea.','They will has milk tea.','They wills have milk tea.','They will having milk tea.'],'They will have milk tea.','Will + have.',3)]


def reading():
    qs=[]
    for p in PROFILES[:4]:
        qs.extend(based(q,passage(p)) for q in [text('Who is speaking? Write the name only.',p['name'],'Tên ở câu đầu.',3),
            mc('What drink will they have?',DRINKS,p['drink'],'Không lấy đồ ăn.',3),
            text('Write only the day of the party.',p['day'],'Ngày sau on.',3),
            tf([(f"They will {p['activity']}.",True),(f"They will have {DRINKS[(DRINKS.index(p['drink'])+1)%4]}.",False)],'Theo kế hoạch trong bài.',3)])
    qs += [based(text('Who plans to sing on Children’s Day? Write the name only.','Nam','An và Nam cùng ngày lễ nhưng khác hoạt động.',3),'\n'.join(card(p) for p in [PROFILES[0],PROFILES[4]])),
        based(mc('Choose the order of activities.',['sing → play games → dance','dance → sing → play games','play games → dance → sing','sing → dance → play games'],'sing → play games → dance','First → Then → Finally.',3),'At our class party, we will sing first. Then, we will play games. Finally, we will dance.')]
    return qs


def writing():
    a,b,c=PROFILES[:3]
    return [text('Complete: We will ___ pizza.','have','Will + have.',2),reorder('We will dance on Children’s Day.','On + Children’s Day.'),
        text('Complete: She will ___ at the party. Use sing.','sing','Will + nguyên mẫu.'),text('Complete: apple ___.','juice','Nước ép táo.',2),
        mc('Choose the correct question.',['What drinks will they have?','What drinks they will have?','What drinks will they has?','What drinks will they having?'],'What drinks will they have?','Will + they + have.',2),
        text('Complete: ___ will you do on Sports Day?','What','What will you do?'),
        match([("We’ll",'We will'),("They’ll",'They will'),("I’ll",'I will')],'Dạng rút gọn với will.'),
        reorder('We will have a party at Mid-Autumn Festival.','At Mid-Autumn Festival.',2),
        text('Rewrite in full: We’ll have milk tea.','We will have milk tea.','Giữ nguyên đồ uống.',2),
        text('Complete: We will sing ___ Teachers’ Day.','on','On Teachers’ Day.'),
        shown(reorder(menu(a),'Food trước drink.',2),a),reorder('What food will you have at the party?','Food đứng trước will.',2),
        text('Complete: They will play ___. Use the sport cầu lông.','badminton','Play badminton.'),
        text('Rewrite in full: They’ll play games.','They will play games.','They’ll = They will.',2),
        shown(text('Write activity, then menu. Start both with We will; food before drink.',action(b)+' '+menu(b),'Khớp tất cả dữ kiện.',3),b),
        shown(text('Write one menu sentence starting with We will have, with food before drink.',menu(c),'Chicken and rice / water.',3),c),
        shown(text('Write the activity sentence starting with We will.',action(PROFILES[3]),'Dùng at.',3),PROFILES[3]),
        shown(text('Write activity, then menu. Start both with We will; food before drink.',action(PROFILES[4])+' '+menu(PROFILES[4]),'Không lấy kế hoạch của An.',3),PROFILES[4])]


def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    return [listen('Listen and choose the food.',f"We will have {a['food']}.",[field('Food:',a['food'],FOODS)],2),
        listen('Listen and choose the activity.',action(b),[field('Activity:',b['activity'],ACTIVITIES)]),
        listen('Listen and choose the drink.',f"We will have {b['food']} and {b['drink']} at our party.",[field('Drink:',b['drink'],DRINKS)],2),
        listen('Listen and choose the day of the party.',f"Our party will be on {c['day']}. "+action(c),[field('Day:',c['day'],['Sunday','Monday','Saturday','Friday'])],3),
        listen('Listen. Choose both food and drink.',action(a)+' '+menu(a),[field('Food:',a['food'],FOODS),field('Drink:',a['drink'],DRINKS)],3),
        listen('Listen. Write only the Sunday menu, not the Saturday menu.',
            'On Saturday, we will have burgers and water. On Sunday, we will have pizza and apple juice.',
            [field('Sunday food:','pizza'),field('Sunday drink:','apple juice')],3)]


def build_tests():
    import copy
    written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
    mixed=[copy.deepcopy(written[i%5][i]) for i in range(18)]
    return [assemble(qs,listening(i)) for i,qs in enumerate(written+[mixed])]
