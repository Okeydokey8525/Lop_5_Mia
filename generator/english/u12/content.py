"""Original Tet plans; volume two, printed pages 12-17."""
from english.practice import mc,text as base_text,match,reorder,tf,based,picture as image,field,listen,assemble

ACTIVITIES={'decorate the house':'trang trí nhà','do the shopping':'đi mua sắm','make spring rolls':'làm nem/cuốn chả giò','buy a branch of peach blossoms':'mua một cành hoa đào'}
CORE=list(ACTIVITIES)
IMAGE_NAMES=dict(zip(CORE,['decorate-the-house','do-the-shopping','make-spring-rolls','buy-peach-blossoms']))
PLACES=["my grandparents’ house",'a fireworks show','a New Year party','a flower festival']
PROFILES=[
    dict(name='An',activity=CORE[0],no='do the shopping',place=PLACES[0],with_='my mother'),
    dict(name='Linh',activity=CORE[1],no='buy roses',place=PLACES[1],with_='my father'),
    dict(name='Minh',activity=CORE[2],no='make banh chung',place=PLACES[2],with_='my family'),
    dict(name='Hoa',activity=CORE[3],no='buy roses',place=PLACES[3],with_='my brother'),
    dict(name='Nam',activity=CORE[1],no='make spring rolls',place=PLACES[0],with_='my father'),
    dict(name='Mai',activity=CORE[0],no='make banh chung',place=PLACES[1],with_='my family')]


def text(stem,answer,why,lesson=1,alternatives=()):
    accepted=list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short=answer.replace('will not',"won't").replace('I will',"I'll").replace('We will',"We'll")
        if short!=answer:accepted.append(short)
    return base_text(stem,answer,why,lesson,accepted)


def picture(activity,width=320):return image('u12',IMAGE_NAMES[activity],ACTIVITIES[activity],width)
def action(p):return f"I will {p['activity']} for Tet."
def destination(p):return f"I will go to {p['place']} at Tet."
def card(p):return f"Speaker: {p['name']} · For Tet: {p['activity']} · Will NOT: {p['no']} · At Tet, go to: {p['place']} · With: {p['with_']}."
def passage(p):return f"My name is {p['name']}. "+action(p)+f" I will not {p['no']}. "+destination(p)+f" I will go with {p['with_']}."
def shown(q,p):return based(q,card(p))


def warmup():
    a,b,c=PROFILES[:3]
    return [mc('Look at the picture. Choose the activity.',CORE,CORE[0],'Bạn nhỏ đang trang trí nhà.',1,picture(CORE[0])),
        text('Complete: Will you ___ the house for Tet?','decorate','Will + nguyên mẫu.'),
        match([('do the shopping','đi mua sắm'),('make spring rolls','làm nem/cuốn chả giò'),('buy roses','mua hoa hồng')],'Nhớ cụm động từ.'),
        mc('Will you do the shopping? Choose a short yes answer.',['Yes, I will.','Yes, I do.','Yes, I did.','Yes, I am.'],'Yes, I will.','Hỏi will, đáp will.'),
        reorder('Will you make spring rolls for Tet?','Đưa will lên trước you.'),
        text('Complete: No, I ___. Use the negative of will.','will not','Will not = won’t.'),
        shown(mc('Where will the speaker go at Tet?',PLACES,a['place'],'Đọc nơi đến trong thẻ.',2),a),
        text('Complete: I will ___ to a flower festival.','go','Sau will dùng go.',2),
        shown(text('Write only the activity phrase for Tet.',b['activity'],'Thẻ ghi do the shopping.'),b),
        reorder('Where will you go at Tet?','Where hỏi nơi chốn.',2),
        shown(text('Write only the activity the speaker will NOT do.',c['no'],'Đọc Will NOT, không lấy kế hoạch sẽ làm.',2),c),
        tf([('Will is followed by a base verb.',True),('Won’t means will.',False)],'Won’t = will not.'),
        shown(text('Write only the companion phrase from the card.',a['with_'],'My mother.',2),a),
        text('Complete: I will go ___ a New Year party.','to','Go to + nơi/sự kiện.',2),
        shown(text('Write one sentence starting with I will and ending with for Tet.',action(a),'Đúng hoạt động và thời gian.',3),a),
        shown(text('Write the destination sentence, starting with I will and ending with at Tet.',destination(c),'I will go to + nơi + at Tet.',3),c),
        mc('Choose the correct question.',['Will she buy flowers?','Will she buys flowers?','Does she will buy flowers?','Will she buying flowers?'],'Will she buy flowers?','Will + she + buy.',3),
        shown(text('Write two sentences: activity for Tet, then destination at Tet. Start each with I will.',action(b)+' '+destination(b),'Không đổi thứ tự hai câu.',3),b)]


def vocabulary():return [
    *[mc('Look at the picture. Choose the activity.',CORE,k,'Tranh: '+ACTIVITIES[k]+'.',1,picture(k)) for k in CORE],
    text('Complete: do the shop___. Write the whole word.','shopping','Shopping có pp.'),
    match([('a fireworks show','buổi trình diễn pháo hoa'),('a flower festival','lễ hội hoa'),('a New Year party','tiệc năm mới')],'Ba sự kiện khác nhau.',2),
    mc('Which phrase means “làm nem/cuốn chả giò”?',CORE,CORE[2],'Make spring rolls.'),
    text('Complete: a branch of peach ___.','blossoms','Peach blossoms: hoa đào.'),
    text('Complete: ___ the house. Use a verb meaning trang trí.','decorate','Decorate the house.'),
    reorder('I will buy a branch of peach blossoms.','Will buy, không dùng will bought.'),
    match([('roses','hoa hồng'),('peach blossoms','hoa đào'),('spring rolls','nem/cuốn chả giò')],'Hoa đào khác hoa hồng.',2),
    text('Complete: make ___ rolls.','spring','Spring rolls là một cụm.'),
    shown(text('Write only the destination phrase from the card.',PROFILES[3]['place'],'A flower festival.',2),PROFILES[3]),
    tf([('A fireworks show is a place/event to go to.',True),('Do the shopping means make spring rolls.',False)],'Phân biệt nơi đến với việc chuẩn bị.',2),
    shown(text('Write the full activity phrase, not just buy.',CORE[3],'Giữ a branch of peach blossoms.',3),PROFILES[3]),
    shown(text('Write only the companion phrase.',PROFILES[4]['with_'],'My father, không phải my mother.',3),PROFILES[4]),
    based(match([(p['name'],p['place']+' / '+p['with_']) for p in PROFILES[:3]],'Khớp cả nơi và người đi cùng.',3),'\n'.join(card(p) for p in PROFILES[:3])),
    reorder('My grandparents will decorate the house.','Will dùng như nhau với chủ ngữ số nhiều.',3)]


def dialogue():
    a,b,c=PROFILES[:3]
    return [mc('Will you decorate the house? Choose a short yes answer.',['Yes, I will.','Yes, I do.','Yes, I was.','Yes, I did.'],'Yes, I will.','Đáp theo will.'),
        text('Complete: ___ will you go at Tet? Ask about a place.','Where','Where hỏi nơi đến.',2),
        reorder('Will you do the shopping for Tet?','Will + you + do.'),
        shown(mc('Where will the speaker go?',PLACES,b['place'],'Linh sẽ đến buổi pháo hoa.',2),b),
        text('Give a short negative answer in full form: Will you buy roses?','No, I will not.','Won’t = will not.'),
        text('Complete: I will ___ spring rolls.','make','Will + make.'),
        shown(text('Answer with one destination sentence, starting with I will and ending with at Tet.',destination(a),'Đúng nơi đến.',2),a),
        shown(mc('What will the speaker do for Tet?',CORE,c['activity'],'Minh làm spring rolls.'),c),
        reorder('Where will your family go at Tet?','Will đứng trước your family.',2),
        text('Rewrite in full: I won’t buy roses.','I will not buy roses.','Will not + buy.'),
        text('Complete: Will she ___ flowers? Use buy.','buy','Không thêm s sau will.'),
        match([('Will you make spring rolls?','Yes, I will.'),('Where will you go?','To a flower festival.'),('What will you buy?','A branch of peach blossoms.')],'Phân biệt câu có/không, nơi và đồ mua.',2),
        shown(text('Write a negative sentence starting with I will not, using the Will NOT phrase.',f"I will not {a['no']}.",'Không thay bằng việc sẽ làm.',2),a),
        tf([('Where will you go asks about a place.',True),('No, I won’t is a positive answer.',False)],'Won’t là phủ định.',3),
        shown(text('Write activity for Tet, then destination at Tet. Start each sentence with I will.',action(c)+' '+destination(c),'Lấy hai ý cùng thẻ.',3),c),
        text('Rewrite in full: We’ll do the shopping.','We will do the shopping.','We’ll = We will.',3),
        shown(text('Write a complete negative sentence starting with I will not.',f"I will not {b['no']}.",'Linh không mua hoa hồng.',3),b),
        mc('Choose the correct negative sentence.',['She will not make banh chung.','She will not makes banh chung.','She not will make banh chung.','She will does not make banh chung.'],'She will not make banh chung.','Will not + make.',3)]


def reading():
    qs=[]
    for p in PROFILES[:4]:
        qs.extend(based(q,passage(p)) for q in [text('Who is speaking? Write the name only.',p['name'],'Tên ở câu đầu.',3),
            mc('Where will the speaker go at Tet?',PLACES,p['place'],'Tìm go to.',3),
            text('Write only the activity the speaker will NOT do.',p['no'],'Đọc câu phủ định.',3),
            tf([(f"The speaker will {p['activity']} for Tet.",True),(f"The speaker will {p['no']}.",False)],'Đối chiếu will và will not.',3)])
    qs += [based(text('Who will go to their grandparents’ house with their father? Write the name.','Nam','An và Nam cùng nơi nhưng khác người đi cùng.',3),'\n'.join(card(p) for p in [PROFILES[0],PROFILES[4]])),
        based(mc('Choose the correct order.',['do the shopping → make spring rolls → decorate the house','make spring rolls → do the shopping → decorate the house','decorate the house → make spring rolls → do the shopping','do the shopping → decorate the house → make spring rolls'],'do the shopping → make spring rolls → decorate the house','First → Then → Finally.',3),'First, we will do the shopping. Then, we will make spring rolls. Finally, we will decorate the house.')]
    return qs


def writing():
    a,b,c=PROFILES[:3]
    return [text('Complete: Will you ___ the house?','decorate','Decorate sau will.'),reorder('I will make spring rolls for Tet.','Will + make.'),
        text('Complete: She will ___ roses. Use buy.','buy','Không thêm s.'),text('Complete: We will ___ the shopping.','do','Do the shopping.'),
        mc('Choose the correct sentence.',['He will go to a flower festival.','He will goes to a flower festival.','He wills go to a flower festival.','He will went to a flower festival.'],'He will go to a flower festival.','Will + go.',2),
        text('Complete: Where ___ you go at Tet? Use the future helper.','will','Where will you go?',2),
        match([("I’ll",'I will'),("won’t",'will not'),("We’ll",'We will')],'Nhớ ba dạng rút gọn.'),
        reorder('Will your father buy peach blossoms?','Will + chủ ngữ + buy.',2),
        text('Rewrite in full: I won’t make banh chung.','I will not make banh chung.','Will not + make.'),
        text('Complete: I will go ___ my grandparents’ house.','to','Go to.',2),
        shown(reorder(action(c),'Đúng hoạt động theo thẻ.',2),c),reorder('We will go to a New Year party.','Will go to.',2),
        text('Complete: We will go to a fireworks show ___ Tet.','at','At Tet.',2),
        text('Rewrite in full: I’ll do the shopping.','I will do the shopping.','I’ll = I will.',2),
        shown(text('Write activity for Tet, then destination at Tet. Start each sentence with I will.',action(a)+' '+destination(a),'Giữ thứ tự và địa điểm.',3),a),
        shown(text('Write one negative sentence starting with I will not.',f"I will not {b['no']}.",'Dùng mục Will NOT.',3),b),
        shown(text('Write the destination sentence, starting with I will and ending with at Tet.',destination(PROFILES[3]),'A flower festival.',3),PROFILES[3]),
        shown(text('Write activity for Tet, then destination at Tet. Start each sentence with I will.',action(PROFILES[4])+' '+destination(PROFILES[4]),'Không lấy dữ kiện của An.',3),PROFILES[4])]


def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    return [listen('Listen and choose the activity.',action(a),[field('Activity:',a['activity'],CORE)]),
        listen('Listen and choose the place.',destination(b),[field('Place:',b['place'],PLACES)],2),
        listen('Listen. Which activity will the speaker NOT do?',f"I will not {b['no']}. "+action(b),[field('Will NOT:',b['no'],list(dict.fromkeys([b['no'],'buy roses','make banh chung','do the shopping'])))],2),
        listen('Listen and choose the companion.',destination(c)+f" I will go with {c['with_']}.",[field('With:',c['with_'],['my mother','my father','my family','my brother'])],2),
        listen('Listen. Find both activity and place.',action(a)+' '+destination(a),[field('Activity:',a['activity'],CORE),field('Place:',a['place'],PLACES)],3),
        listen('Listen. Write only Mai’s activity and place, not Nam’s.',
            'Nam will do the shopping and go to a flower festival. Mai will decorate the house and go to a fireworks show.',
            [field('Mai’s activity:','decorate the house'),field('Mai’s place:','a fireworks show')],3)]


def build_tests():
    import copy
    written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
    mixed=[copy.deepcopy(written[i%5][i]) for i in range(18)]
    return [assemble(qs,listening(i)) for i,qs in enumerate(written+[mixed])]
