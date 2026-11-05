"""Original school-trip practice from visually verified pages 68–73."""
from english.practice import mc,text as base_text,match,reorder,tf,based,picture as image,field,listen,assemble

PLACES=['Ba Na Hills','Hoan Kiem Lake','Suoi Tien Theme Park','Bai Dinh Pagoda']
ACTIVITIES={'visit the old buildings':('visited the old buildings','tham quan những tòa nhà cổ'),'plant trees':('planted trees','trồng cây'),'play games':('played games','chơi trò chơi'),'walk around the lake':('walked around the lake','đi bộ quanh hồ')}
CORE=list(ACTIVITIES)
PAST=[v[0] for v in ACTIVITIES.values()]
MONTHS=['September','October','November','December']
PROFILES=[
 dict(name='An',place=PLACES[0],activity=CORE[0],month='November'),
 dict(name='Linh',place=PLACES[1],activity=CORE[3],month='December'),
 dict(name='Minh',place=PLACES[2],activity=CORE[2],month='November'),
 dict(name='Mai',place=PLACES[3],activity=CORE[0],month='December'),
 dict(name='Nam',place=PLACES[0],activity=CORE[1],month='September'),
 dict(name='Hoa',place=PLACES[1],activity=CORE[3],month='October'),
]


def text(stem,answer,why,lesson=1,alternatives=()):
    variants=list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short=answer.replace('did not',"didn't")
        if short!=answer:variants.append(short)
    return base_text(stem,answer,why,lesson,variants)


def picture(activity,width=320):return image('u10',activity.replace(' ','-'),ACTIVITIES[activity][1],width)
def past(p):return ACTIVITIES[p['activity']][0]
def where(p):return 'They went to '+p['place']+' last '+p['month']+'.'
def action(p):return 'They '+past(p)+'.'
def card(p):return f"Class: {p['name']}'s class · Place: {p['place']} · Time: last {p['month']} · Activity: {past(p)}."
def passage(p):return f"This is {p['name']}'s class. "+where(p)+' '+action(p)+' They enjoyed the trip.'
def shown(q,p):return based(q,card(p))


def warmup():
    a,b,c,d=PROFILES[:4]
    return [
        mc('Look at the picture. Choose the activity.',CORE,CORE[1],'Các bạn đang trồng cây.',1,picture(CORE[1])),
        match([(k,v[0]) for k,v in list(ACTIVITIES.items())[:3]],'Visit → visited; plant → planted; play → played.'),
        text('Complete: Did they ___ to Ba Na Hills?','go','Sau did dùng go, không dùng went.'),
        mc('Choose the past form of go.',['went','go','goes','going'],'went','Go → went.'),
        reorder('They went to Hoan Kiem Lake.','They went to + địa điểm.'),
        text('Complete: Did they go there? Yes, they ___.','did','Yes, they did.'),
        mc('Which month comes after November?',MONTHS,'December','November là tháng 11; December là tháng 12.',3),
        shown(mc('Where did this class go?',PLACES,a['place'],'Địa điểm của lớp An trong thẻ.'),a),
        match([('November','tháng mười một'),('December','tháng mười hai'),('September','tháng chín')],'Ghép tháng với nghĩa.',3),
        text('Complete: They ___ trees. Use plant.','planted','Plant → planted.',2),
        shown(text('Write only the past activity phrase.',past(b),'Theo thẻ: walked around the lake.',2),b),
        reorder('What did they do there?','What did + they + do + there?',2),
        text('Complete: No, they ___. Use the negative of did.','did not','Did not = didn’t.'),
        shown(tf([('The class played games.',True),('The class planted trees.',False)],'Đối chiếu hoạt động trong thẻ.',2),c),
        shown(text('Write the location sentence, starting with They and including the month.',where(d),'They went to Bai Dinh Pagoda last December.',3),d),
        shown(text('Write the activity sentence, starting with They.',action(a),'They visited the old buildings.',3),a),
        mc('Choose the correct question.',['Did they go to Ba Na Hills?','Did they went to Ba Na Hills?','Do they went to Ba Na Hills?','Did they goes to Ba Na Hills?'],'Did they go to Ba Na Hills?','Did + chủ ngữ + go nguyên mẫu.',3),
        shown(text('Write the location sentence and then the activity sentence.',where(c)+' '+action(c),'Viết đủ nơi, tháng và hoạt động theo thẻ.',3),c),
    ]


def vocabulary():return [
    *[mc('Look at the picture. Choose the activity.',CORE,k,'Tranh minh họa '+v[1]+'.',1,picture(k)) for k,v in ACTIVITIES.items()],
    text('Complete: v i s i _ e d. Write the whole word.','visited','Visited có chữ t trước e.'),
    text('Write the past form of walk.','walked','Walk → walked.'),
    match([(k,v[0]) for k,v in list(ACTIVITIES.items())[1:]],'Ghép đúng cụm quá khứ.'),
    mc('Which phrase means “trồng cây”?',CORE,'plant trees','Plant trees: trồng cây.'),
    mc('Which word is the past form of go?',['went','goes','going','go'],'went','Dạng quá khứ là went.',2),
    text('Complete: visit the old ___.','buildings','Giữ số nhiều buildings.',2),
    match([('last November','tháng 11 vừa qua'),('last December','tháng 12 vừa qua'),('last weekend','cuối tuần vừa qua')],'Ghép cụm thời gian đã qua.',3),
    text('Complete: walked ___ the lake.','around','Walk around the lake.',2),
    reorder('They planted trees last November.','Động từ quá khứ và tháng đã qua.',3),
    tf([('November has second-syllable stress.',True),('December has first-syllable stress.',False)],'No-VEM-ber và De-CEM-ber nhấn âm thứ hai.',3),
    shown(text('Write the destination only.',PROFILES[2]['place'],'Tên trong thẻ: Suoi Tien Theme Park.',3),PROFILES[2]),
    shown(text('Write the month only, without last.',PROFILES[3]['month'],'Thẻ ghi last December.',3),PROFILES[3]),
    based(match([(p['name'],p['place']) for p in PROFILES[:3]],'Ghép lớp của từng bạn với địa điểm trong thẻ.',3),'\n'.join(card(p) for p in PROFILES[:3])),
    reorder('What did they do on the trip?','Sau did dùng do, không dùng did.',3),
]


def dialogue():
    a,b,c,d=PROFILES[:4]
    return [
        mc('A: Did they go to Bai Dinh Pagoda? B: ___.',['Yes, they did.','Yes, they do.','Yes, they were.','Yes, they went.'],'Yes, they did.','Did they…? → Yes, they did.'),
        text('Complete: What ___ they do there?','did','Hỏi việc đã làm bằng did.'),
        reorder('Where did they go last November?','Where did they go…?',3),
        shown(mc('What did this class do?',PAST,past(b),'Theo thẻ lớp Linh.'),b),
        text('Complete: Did they go to the lake? No, they ___.','did not','No, they did not; cũng viết didn’t.'),
        text('Complete: They ___ to Ba Na Hills. Use go.','went','Câu kể quá khứ: went.'),
        shown(text('Give the location sentence including the month.',where(a),'Dùng They went to và tháng trong thẻ.',2),a),
        shown(mc('Which month was the trip?',MONTHS,c['month'],'Lớp Minh đi tháng November.',3),c),
        reorder('Did they visit the old buildings?','Sau did dùng visit nguyên mẫu.',2),
        text('Rewrite in full: They didn’t go to the lake.','They did not go to the lake.','Didn’t = did not.',2),
        text('Complete: What did they ___ there?','do','Did…do, không dùng did…did.',2),
        match([('Where did they go?','They went to Ba Na Hills.'),('What did they do?','They planted trees.'),('Did they play games?','Yes, they did.')],'Ghép câu hỏi nơi, việc làm, có/không.',2),
        shown(text('Give the activity sentence, starting with They.',action(d),'Theo thẻ: visited the old buildings.',2),d),
        tf([('Did they go…? asks about a past trip.',True),('After did, use went in this question.',False)],'Sau did dùng go nguyên mẫu.',2),
        shown(text('Write both location and activity sentences from the card.',where(b)+' '+action(b),'Giữ last December và walked.',3),b),
        shown(text('Give the location sentence with the month.',where(PROFILES[4]),'Lớp Nam đi last September.',3),PROFILES[4]),
        text('Rewrite in full: No, they didn’t.','No, they did not.','Didn’t = did not.',3),
        mc('Choose the correct past sentence.',['They visited the old buildings.','They did visited the old buildings.','They were visit the old buildings.','They visits the old buildings yesterday.'],'They visited the old buildings.','Câu kể dùng visited, không thêm did/were.',3),
    ]


def reading():
    qs=[]
    for p in PROFILES[:4]:
        wrong=next(x for x in PROFILES if x['activity']!=p['activity'])
        qs.extend(based(item,passage(p)) for item in [
            text('Whose class is the passage about? Write the pupil’s name.',p['name'],'Tìm tên trong câu đầu.',3),
            mc('Where did the class go?',PLACES,p['place'],'Đọc địa điểm sau went to.',3),
            text('Write only the past activity phrase.',past(p),'Hoạt động theo bài đọc.',3),
            tf([(f"The class {past(p)}.",True),(f"The class {past(wrong)}.",False)],'Đọc hoạt động, không suy chỉ từ nơi đi.',3),
        ])
    qs += [based(text('Which class planted trees? Write the pupil’s name.','Nam','An và Nam cùng Ba Na Hills nhưng hoạt động khác.',3),'\n'.join(card(p) for p in [PROFILES[0],PROFILES[4]])),
           based(text('Which class went to Hoan Kiem Lake last October? Write the pupil’s name.','Hoa','Linh và Hoa cùng nơi nhưng khác tháng.',3),'\n'.join(card(p) for p in [PROFILES[1],PROFILES[5]]))]
    return qs


def writing():
    a,b,c,d=PROFILES[:4]
    return [
        text('Complete: Did they ___ to Ba Na Hills?','go','Did…go.'),
        reorder('They went to Hoan Kiem Lake.','Câu kể dùng went to.'),
        text('Complete: What did they ___ there?','do','Sau did dùng do.'),
        text('Complete: They ___ trees. Use plant.','planted','Plant → planted.'),
        mc('Choose the correct question.',['Did they play games?','Did they played games?','Did they playing games?','Did they plays games?'],'Did they play games?','Did + play nguyên mẫu.'),
        text('Write the past form of visit.','visited','Visit → visited.'),
        match([('go','went'),('walk','walked'),('plant','planted')],'Ghép nguyên mẫu và quá khứ.'),
        reorder('Did they go to Suoi Tien Theme Park?','Did they go…?'),
        text('Rewrite in full: They didn’t visit the old buildings.','They did not visit the old buildings.','Giữ visit sau did not.',2),
        text('Complete: They walked around the ___ .','lake','Walk around the lake.',2),
        shown(reorder(action(c),'Đúng hoạt động theo thẻ.',2),c),
        reorder('Where did they go last December?','Where did they go…?',3),
        text('Complete: They went ___ Bai Dinh Pagoda.','to','Went to + tên nơi.',2),
        text('Rewrite in full: They didn’t play games.','They did not play games.','Didn’t = did not; giữ play sau did not.',2),
        shown(text('Write location and then activity, both starting with They.',where(a)+' '+action(a),'Lấy nơi, tháng, hoạt động cùng thẻ.',3),a),
        shown(text('Write the location sentence including the month.',where(b),'Hoan Kiem Lake last December.',3),b),
        shown(text('Write the activity sentence starting with They.',action(d),'They visited the old buildings.',3),d),
        shown(text('Write the location and activity sentences.',where(PROFILES[5])+' '+action(PROFILES[5]),'Lớp Hoa đi Hoan Kiem Lake tháng October.',3),PROFILES[5]),
    ]


def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    return [listen('Listen and choose the destination.',where(a),[field('Destination:',a['place'],PLACES)]),
        listen('Listen and choose the activity.',action(b),[field('Activity:',past(b),PAST)],2),
        listen('Listen and find the month.',passage(b),[field('Month:',b['month'],MONTHS)],3),
        listen('Listen and find the destination.',passage(c),[field('Destination:',c['place'],PLACES)],2),
        listen('Listen and choose destination and activity.',passage(a),[field('Destination:',a['place'],PLACES),field('Activity:',past(a),PAST)],3),
        listen('Listen and write month and activity.',passage(c),[field('Month:',c['month']),field('Activity:',past(c))],3)]


def build_tests():
    import copy
    written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
    mixed=[copy.deepcopy(written[i%5][i]) for i in range(18)]
    return [assemble(qs,listening(i)) for i,qs in enumerate(written+[mixed])]
