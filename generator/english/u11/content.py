"""Original family-trip practice, verified against volume two, printed pages 6-11."""
from english.practice import mc,text as base_text,match,reorder,tf,based,picture as image,field,listen,assemble

ACTIVITIES={
    'swim':('swam','bơi'),
    'take photos':('took photos','chụp ảnh'),
    'collect seashells':('collected seashells','nhặt vỏ sò'),
    'walk on the beach':('walked on the beach','đi dạo trên bãi biển'),
    'take a boat trip around the bay':('took a boat trip around the bay','đi thuyền quanh vịnh'),
    'buy souvenirs':('bought souvenirs','mua quà lưu niệm'),
    'eat seafood':('ate seafood','ăn hải sản'),
    'see some interesting places':('saw some interesting places','tham quan vài địa điểm thú vị'),
}
CORE=['collect seashells','take photos','buy souvenirs','take a boat trip around the bay']
IMAGE_NAMES=dict(zip(CORE,['collect-seashells','take-photos','buy-souvenirs','take-a-boat-trip']))
PAST=[v[0] for v in ACTIVITIES.values()]
PLACES=['Ha Long','Nha Trang','Sydney','Singapore']
TIMES=['last weekend','last summer','yesterday','last Sunday']
PROFILES=[
    dict(name='An',place='Ha Long',time='last weekend',activity='collect seashells',companion='my brother'),
    dict(name='Linh',place='Nha Trang',time='last summer',activity='take photos',companion='my father'),
    dict(name='Minh',place='Singapore',time='yesterday',activity='buy souvenirs',companion='my mother'),
    dict(name='Hoa',place='Ha Long',time='last Sunday',activity='take a boat trip around the bay',companion='my family'),
    dict(name='Nam',place='Sydney',time='last weekend',activity='see some interesting places',companion='my family'),
    dict(name='Mai',place='Nha Trang',time='last Sunday',activity='eat seafood',companion='my family'),
]


def text(stem,answer,why,lesson=1,alternatives=()):
    accepted=list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short=answer.replace('did not',"didn't")
        if short!=answer:accepted.append(short)
    return base_text(stem,answer,why,lesson,accepted)


def picture(activity,width=320):return image('u11',IMAGE_NAMES[activity],ACTIVITIES[activity][1],width)
def past(p):return ACTIVITIES[p['activity']][0]
def location(p):return f"My family went to {p['place']} {p['time']}."
def action(p):return f"I {past(p)} with {p['companion']}."
def card(p):return f"Speaker: {p['name']} · Family destination: {p['place']} · Time: {p['time']} · Speaker's activity: {past(p)} · With: {p['companion']}."
def passage(p):return f"My name is {p['name']}. "+location(p)+' '+action(p)+' It was a nice trip.'
def shown(q,p):return based(q,card(p))


def warmup():
    a,b,c=PROFILES[:3]
    return [
        mc('Look at the picture. Choose the activity.',CORE,CORE[0],'Bạn nhỏ đang nhặt vỏ sò.',1,picture(CORE[0])),
        match([('swim','swam'),('take','took'),('buy','bought')],'Swim → swam; take → took; buy → bought.'),
        text('Complete: Did you ___ photos?','take','Sau did dùng take nguyên mẫu.'),
        mc('Choose the past form of eat.',['ate','eat','eats','eating'],'ate','Eat → ate.',2),
        reorder('Did you collect seashells?','Did + you + nguyên mẫu?'),
        text('Did you swim? Yes, I ___.','did','Did you…? → Yes, I did.'),
        shown(mc('Where did this family go?',PLACES,a['place'],'Đọc địa điểm trong thẻ.'),a),
        text('Write the past form of see.','saw','See → saw.',2),
        shown(text('Write only the past activity phrase.',past(b),'Linh took photos.',2),b),
        reorder('What did your family do there?','Did…do, không dùng did…did.',2),
        text('Did you swim? No, I ___. Use the negative of did.','did not','Did not = didn’t.'),
        shown(tf([('The speaker bought souvenirs.',True),('The speaker ate seafood.',False)],'Đối chiếu hoạt động của Minh.',2),c),
        shown(text('Write only who An was with, using the words from the card.',a['companion'],'Thẻ ghi my brother.'),a),
        shown(text('Write the time phrase only.',b['time'],'Thẻ của Linh ghi last summer.',3),b),
        shown(text('Write a destination sentence starting with My family and including the time.',location(a),'Dùng went to + nơi + thời gian.',3),a),
        shown(text('Write the activity sentence starting with I and including who was with you.',action(c),'I bought souvenirs with my mother.',3),c),
        mc('Choose the correct question.',['Did you buy souvenirs?','Did you bought souvenirs?','Do you bought souvenirs?','Did you buys souvenirs?'],'Did you buy souvenirs?','Sau did dùng buy.',3),
        shown(text('Write the destination sentence, then the activity sentence, using My family and I.',location(b)+' '+action(b),'Lấy nơi, thời gian và người đi cùng từ cùng một thẻ.',3),b),
    ]


def vocabulary():return [
    *[mc('Look at the picture. Choose the activity.',CORE,k,'Tranh minh họa '+ACTIVITIES[k][1]+'.',1,picture(k)) for k in CORE],
    text('Complete: collect sea___. Write the missing part.','shells','Seashells: vỏ sò.'),
    match([('eat seafood','ate seafood'),('buy souvenirs','bought souvenirs'),('see some interesting places','saw some interesting places')],'Ghép cụm nguyên mẫu với quá khứ.',2),
    mc('Which phrase means “chụp ảnh”?',CORE,'take photos','Take photos: chụp ảnh.'),
    text('Write the past form of swim.','swam','Swim → swam.'),
    text('Complete: took a boat trip ___ the bay.','around','Around the bay: quanh vịnh.',2),
    text('Write the past form of collect.','collected','Collect → collected.'),
    match([('last weekend','cuối tuần vừa qua'),('last summer','mùa hè vừa qua'),('yesterday','hôm qua')],'Các mốc thời gian đã qua.',3),
    text('Complete: bought souve___. Write the whole word.','souvenirs','Souvenirs: quà lưu niệm.',2),
    reorder('We saw some interesting places.','Câu kể dùng saw.',2),
    tf([('After Did you, use take in a question.',True),('Bought is the base form of buy.',False)],'Did + take; buy là nguyên mẫu, bought là quá khứ.',2),
    shown(text('Write only the past activity phrase.',past(PROFILES[3]),'Took a boat trip around the bay.',3),PROFILES[3]),
    shown(text('Write only the companion phrase from the card.',PROFILES[1]['companion'],'My father, không phải my brother.',3),PROFILES[1]),
    based(match([(p['name'],p['place']+' / '+p['time']) for p in PROFILES[:3]],'Khớp đúng tên, nơi và thời gian.',3),'\n'.join(card(p) for p in PROFILES[:3])),
    reorder('When did your family go there?','When hỏi thời gian, không hỏi hoạt động.',3),
]


def dialogue():
    a,b,c=PROFILES[:3]
    return [
        mc('Did you swim? Choose a short yes answer.',['Yes, I did.','Yes, I do.','Yes, I was.','Yes, I swam.'],'Yes, I did.','Câu đáp ngắn của Did you… là Yes, I did.'),
        text('Complete: What ___ your family do there?','did','What did…do?',2),
        reorder('Did you take photos with your father?','Did + take nguyên mẫu.'),
        shown(mc('When did this family go there?',TIMES,a['time'],'Đọc thời gian từ thẻ.',3),a),
        text('Give a short negative answer in full form: Did you buy souvenirs?','No, I did not.','Câu đáp phủ định với did.'),
        text('Complete: We ___ seafood. Use eat.','ate','Eat → ate.',2),
        shown(text('Give the destination sentence with the time, starting with My family.',location(b),'Nha Trang / last summer.',2),b),
        shown(mc('What did the speaker do?',PAST[:4],past(a),'An collected seashells.'),a),
        reorder('When did you go to Singapore?','When did you go…?',3),
        text('Rewrite in full: I didn’t swim.','I did not swim.','Giữ swim sau did not.',2),
        text('Complete: What did they ___ in Ha Long?','do','Sau did dùng do.',2),
        match([('When did you go?','Last summer.'),('What did you do?','I took photos.'),('Did you swim?','No, I did not.')],'Phân biệt thời gian, hoạt động và câu có/không.',2),
        shown(text('Answer with the complete activity sentence starting with I.',action(c),'I bought souvenirs with my mother.',2),c),
        tf([('When asks about time.',True),('What did asks only about a place.',False)],'When: khi nào; What did…do: đã làm gì.',3),
        shown(text('Write the destination and activity sentences using My family and I.',location(a)+' '+action(a),'Không đổi my brother thành my father.',3),a),
        shown(text('Write the activity sentence starting with I.',action(PROFILES[4]),'See → saw.',3),PROFILES[4]),
        text('Rewrite in full: No, I didn’t.','No, I did not.','Didn’t = did not.',3),
        mc('Choose the correct past sentence.',['We took a boat trip.','We did took a boat trip.','We were take a boat trip.','We takes a boat trip yesterday.'],'We took a boat trip.','Câu kể dùng took.',3),
    ]


def reading():
    qs=[]
    for p in PROFILES[:4]:
        wrong=next(x for x in PROFILES if x['activity']!=p['activity'])
        qs.extend(based(q,passage(p)) for q in [
            text('Who is speaking? Write the name only.',p['name'],'Tên trong câu đầu.',3),
            mc('Where did the family go?',PLACES,p['place'],'Tìm nơi sau went to.',3),
            text('Write the time phrase only.',p['time'],'Thời gian chuyến đi trong bài.',3),
            tf([(f"The speaker {past(p)}.",True),(f"The speaker {past(wrong)}.",False)],'Đọc hoạt động, không đoán chỉ từ nơi đi.',3)])
    qs += [based(text('Whose family went to Ha Long last Sunday? Write the speaker’s name.','Hoa','Hai gia đình cùng đến Ha Long nhưng thời gian khác.',3),'\n'.join(card(p) for p in [PROFILES[0],PROFILES[3]])),
           based(mc('Choose the correct activity order.',['collected seashells → took photos → ate seafood','took photos → ate seafood → collected seashells','ate seafood → collected seashells → took photos','collected seashells → ate seafood → took photos'],'collected seashells → took photos → ate seafood','First → Then → Finally theo bài đọc.',3),'First, we collected seashells. Then, we took photos. Finally, we ate seafood.')]
    return qs


def writing():
    a,b,c=PROFILES[:3]
    return [
        text('Complete: Did you ___ souvenirs?','buy','Did + buy nguyên mẫu.'),
        reorder('I swam with my mother.','Swim → swam.'),
        text('Complete: We ___ a boat trip. Use take.','took','Take → took.',2),
        text('Complete: I ___ seashells. Use collect.','collected','Collect → collected.'),
        mc('Choose the correct question.',['Did you walk on the beach?','Did you walked on the beach?','Did you walking on the beach?','Did you walks on the beach?'],'Did you walk on the beach?','Did + walk.'),
        text('Write the past form of buy.','bought','Buy → bought.',2),
        match([('swim','swam'),('eat','ate'),('see','saw')],'Ghép dạng quá khứ.'),
        reorder('When did your family go there?','When hỏi thời gian.',3),
        text('Rewrite in full: We didn’t buy souvenirs.','We did not buy souvenirs.','Giữ buy sau did not.',2),
        text('Complete: I took photos ___ my father.','with','With: cùng với.'),
        shown(reorder(action(a),'Đúng hoạt động và người đi cùng theo thẻ.',2),a),
        reorder('What did your family do in Sydney?','Sau did dùng do.',2),
        text('Complete: My family went ___ Singapore.','to','Went to + nơi chốn.',2),
        text('Rewrite in full: I didn’t eat seafood.','I did not eat seafood.','Didn’t = did not; không đổi eat thành ate.',2),
        shown(text('Write the destination sentence and then the activity sentence, using My family and I.',location(b)+' '+action(b),'Giữ đúng last summer / my father.',3),b),
        shown(text('Write the destination sentence, starting with My family and including the time.',location(c),'Singapore / yesterday.',3),c),
        shown(text('Write the activity sentence starting with I.',action(PROFILES[3]),'I took a boat trip around the bay with my family.',3),PROFILES[3]),
        shown(text('Write both destination and activity sentences using My family and I.',location(PROFILES[5])+' '+action(PROFILES[5]),'Nha Trang / last Sunday / ate seafood.',3),PROFILES[5]),
    ]


def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    companions=['my brother','my father','my mother','my family']
    # Progress from one explicit fact to contrasting people/times and two fields.
    return [listen('Listen and choose the activity.',f"I {past(a)}.",[field('Activity:',past(a),[past(p) for p in PROFILES[:4]] if index<4 else PAST[4:])]),
        listen('Listen and choose who was with the speaker.',action(b),[field('With:',b['companion'],companions)]),
        listen('Listen and choose the time.',location(b)+' '+action(b),[field('Time:',b['time'],TIMES)],2),
        listen('Listen and choose the destination.',location(c)+' '+action(c),[field('Destination:',c['place'],PLACES)],2),
        listen('Listen and find both time and activity.',location(a)+' '+action(a),[field('Time:',a['time'],TIMES),field('Activity:',past(a),PAST)],3),
        listen('Listen carefully. Write only the Sunday activity and the companion phrase.',
               'On Saturday, I took photos with my father. On Sunday, I collected seashells with my brother.',
               [field('Sunday activity:','collected seashells'),field('With:','my brother')],3)]


def build_tests():
    import copy
    written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
    mixed=[copy.deepcopy(written[i%5][i]) for i in range(18)]
    return [assemble(qs,listening(i)) for i,qs in enumerate(written+[mixed])]
