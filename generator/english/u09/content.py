"""Original past outings and activities, verified textbook pages 62–67."""
from english.practice import mc,text as base_text,match,reorder,tf,based,picture as image,field,listen,assemble

PLACES={'theatre':'nhà hát','aquarium':'thủy cung','campsite':'khu cắm trại','funfair':'hội chợ vui chơi'}
CORE=list(PLACES)
ACTIVITIES={'listen to music':('listened to music','nghe nhạc'),'watch the fish':('watched the fish','ngắm cá'),'dance around the campfire':('danced around the campfire','nhảy múa quanh lửa trại'),'play chess':('played chess','chơi cờ vua')}
PAST=[v[0] for v in ACTIVITIES.values()]
PROFILES=[
 dict(name='An',subject='We',place='theatre',activity='listen to music',day='yesterday'),
 dict(name='Linh',subject='We',place='aquarium',activity='watch the fish',day='last Saturday'),
 dict(name='Minh',subject='We',place='campsite',activity='dance around the campfire',day='last Sunday'),
 dict(name='Mai',subject='We',place='campsite',activity='play chess',day='yesterday'),
 dict(name='Nam',subject='I',place='theatre',activity='listen to music',day='last Saturday'),
 dict(name='Hoa',subject='I',place='aquarium',activity='watch the fish',day='last Sunday'),
]


def text(stem,answer,why,lesson=1,alternatives=()):
    variants=list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short=answer.replace('were not',"weren't").replace('was not',"wasn't").replace('did not',"didn't")
        if short!=answer:variants.append(short)
    return base_text(stem,answer,why,lesson,variants)


def picture(place,width=320):return image('u09',place,PLACES[place],width)
def past(p):return ACTIVITIES[p['activity']][0]
def be(p):return 'was' if p['subject']=='I' else 'were'
def where(p):return f"{p['subject']} {be(p)} at the {p['place']} {p['day']}."
def action(p):return f"{p['subject']} {past(p)}."
def card(p):return f"Speaker: {p['name']} · Subject: {p['subject']} · Place: {p['place']} · Time: {p['day']} · Activity: {past(p)}."
def passage(p):return f"My name is {p['name']}. "+('I was with my friends. ' if p['subject']=='We' else '')+where(p)+' '+action(p)
def shown(q,p):return based(q,card(p))


def warmup():
    a,b,c,d=PROFILES[:4]
    return [
        mc('Look at the picture. Choose the place.',CORE,'aquarium','Thủy cung có bể kính lớn để xem cá.',1,picture('aquarium')),
        match(list(PLACES.items())[:3],'Ghép ba địa điểm với nghĩa.'),
        text('Complete: We ___ at the campsite yesterday.','were','We dùng were ở quá khứ.'),
        mc('Choose the past form of play.',['played','play','plays','playing'],'played','Play → played.'),
        reorder('I was at the theatre yesterday.','I was + at the + nơi chốn.'),
        text('Complete: What ___ you do yesterday?','did','Hỏi việc đã làm dùng did.'),
        mc('Which word refers to the past?',['yesterday','tomorrow','next week','next year'],'yesterday','Yesterday: hôm qua.'),
        shown(mc('Where was this group?',CORE,a['place'],'Theo thẻ, nhóm ở theatre.',2),a),
        match([(k,v[0]) for k,v in list(ACTIVITIES.items())[:3]],'Listen → listened, watch → watched, dance → danced.',2),
        text('Complete: Were you at the aquarium? Yes, we ___.','were','Yes, we were.',2),
        shown(text('Write only the past activity phrase.',past(b),'Watched the fish.',2),b),
        reorder('We danced around the campfire.','Dance → danced trong câu quá khứ.',2),
        text('Complete: No, we ___ at the funfair. Write the full form of the negative of were.','were not','Were not là dạng phủ định đầy đủ.',2),
        shown(tf([('The group danced around the campfire.',True),('The group watched the fish.',False)],'Đọc đúng hoạt động trong thẻ.',2),c),
        shown(text('Write the full location sentence using the subject and time in the card.',where(d),'We were at the campsite yesterday.',3),d),
        shown(text('Write the activity sentence using the subject in the card.',action(a),'We listened to music.',3),a),
        mc('Choose the correct question.',['What did you do yesterday?','What did you played yesterday?','What do you did yesterday?','What were you do yesterday?'],'What did you do yesterday?','Sau did dùng do nguyên mẫu.',3),
        shown(text('Write the location sentence and then the activity sentence.',where(c)+' '+action(c),'Dùng were, đúng ngày và danced.',3),c),
    ]


def vocabulary():return [
    *[mc('Look at the picture. Choose the place.',CORE,k,'Tranh minh họa '+v+'.',1,picture(k)) for k,v in PLACES.items()],
    text('Complete: c a m p _ i t e. Write the whole word.','campsite','Campsite có chữ s trước i.'),
    text('Write the past form of watch.','watched','Watch → watched.'),
    match([(k,v[0]) for k,v in list(ACTIVITIES.items())[:3]],'Ghép động từ với dạng quá khứ.'),
    mc('Which phrase means “chơi cờ vua”?',list(ACTIVITIES),'play chess','Play chess là chơi cờ vua.'),
    mc('Choose the past phrase for dance around the campfire.',PAST,'danced around the campfire','Dance đã có e, thêm d.',2),
    text('Complete: listened ___ music.','to','Listen to music; giữ to khi đổi quá khứ.',2),
    match([('yesterday','hôm qua'),('last Saturday','thứ Bảy vừa qua'),('last Sunday','Chủ nhật vừa qua')],'Các mốc thời gian trong quá khứ.',2),
    text('Write the past form of listen.','listened','Listen → listened.',2),
    reorder('They were at the funfair yesterday.','They were + địa điểm + thời gian.',2),
    tf([('Cinema has first-syllable stress.',True),('Bakery has second-syllable stress.',False)],'CI-ne-ma, BA-ke-ry: nhấn âm đầu.',3),
    shown(text('Write the place only.',PROFILES[2]['place'],'Thẻ ghi campsite.',3),PROFILES[2]),
    shown(text('Write the past activity phrase.',past(PROFILES[3]),'Played chess.',3),PROFILES[3]),
    based(match([(p['name'],past(p)) for p in PROFILES[:3]],'Ghép từng người với hoạt động trong thẻ.',3),'\n'.join(card(p) for p in PROFILES[:3])),
    reorder('What did you do at the campsite?','Did + chủ ngữ + do.',3),
]


def dialogue():
    a,b,c,d=PROFILES[:4]
    return [
        mc('A: Were you at the theatre yesterday? B: ___.',['Yes, we were.','Yes, we are.','Yes, we did.','Yes, we was.'],'Yes, we were.','Were you…? → Yes, we were.'),
        text('Complete: Where ___ you yesterday?','were','Where were you yesterday?'),
        reorder('What did you do there?','What + did + you + do + there?'),
        shown(mc('What did the group do?',PAST,past(b),'Thẻ ghi watched the fish.'),b),
        text('Complete: I ___ at the aquarium last Sunday.','was','I dùng was.'),
        text('Complete: Were you at the funfair? No, we ___.','were not','No, we were not. Cũng dùng weren’t.'),
        shown(text('Give the location sentence with the subject and time in the card.',where(a),'We were at the theatre yesterday.',2),a),
        shown(mc('When was the group at the campsite?',['yesterday','last Saturday','last Sunday','last summer'],c['day'],'Thẻ của Minh ghi last Sunday.',2),c),
        reorder('Were you at the campsite last Saturday?','Were + you + at the + địa điểm?',2),
        text('Rewrite in full: We weren’t at the aquarium.','We were not at the aquarium.','Weren’t = were not.',2),
        text('Complete: What did you ___ there?','do','Sau did, dùng do nguyên mẫu.',2),
        match([('Where were you yesterday?','We were at the campsite.'),('What did you do there?','We played chess.'),('Were you at the theatre?','No, we were not.')],'Ghép hỏi nơi chốn, hoạt động và có/không.',2),
        shown(text('Give the activity sentence using the card subject.',action(d),'We played chess.',2),d),
        tf([('Were you…? asks about a past state or place.',True),('What did you do…? needs a present-tense activity answer here.',False)],'Kể hoạt động đã làm dùng động từ quá khứ.',2),
        shown(text('Write both the location and activity sentences from the card.',where(b)+' '+action(b),'Giữ We were, last Saturday và watched.',3),b),
        shown(text('Give the location sentence using I and the time in the card.',where(PROFILES[4]),'I was at the theatre last Saturday.',3),PROFILES[4]),
        text('Rewrite in full: I wasn’t at the campsite.','I was not at the campsite.','Wasn’t = was not.',3),
        mc('Choose the correct past activity sentence.',['We listened to music.','We listen music yesterday.','We were listened to music.','We did listened to music.'],'We listened to music.','Câu khẳng định dùng listened, không thêm were/did.',3),
    ]


def reading():
    qs=[]
    for i,p in enumerate(PROFILES[:4]):
        other=PROFILES[(i+1)%4]
        qs.extend(based(item,passage(p)) for item in [
            text('Write the speaker’s name.',p['name'],'Tên trong phần My name is.',3),
            mc('Where was the group?',CORE,p['place'],'Tìm địa điểm sau at the.',3),
            text('Write only the past activity phrase.',past(p),'Hoạt động: '+past(p)+'.',3),
            tf([(f"The group {past(p)}.",True),(f"The group {past(other)}.",False)],'Đọc chính hoạt động của nhóm, không suy từ địa điểm.',3),
        ])
    qs += [based(text('Who was at the campsite and played chess? Write the speaker’s name.','Mai','Minh và Mai cùng campsite nhưng hoạt động khác nhau.',3),'\n'.join(card(p) for p in [PROFILES[2],PROFILES[3]])),
           based(text('Who was at the aquarium last Sunday? Write the speaker’s name.','Hoa','Linh và Hoa cùng aquarium nhưng ngày khác nhau.',3),'\n'.join(card(p) for p in [PROFILES[1],PROFILES[5]]))]
    return qs


def writing():
    a,b,c,d=PROFILES[:4]
    return [
        text('Complete: We ___ at the theatre yesterday.','were','We were.'),
        reorder('I was at the campsite last Sunday.','I was, không dùng I were.'),
        text('Complete: What ___ you do there?','did','What did you do there?'),
        text('Complete: We ___ chess yesterday. Use play.','played','Play → played.'),
        mc('Choose the correct sentence.',['We watched the fish.','We watch the fish yesterday.','We were watch the fish.','We did watched the fish.'],'We watched the fish.','Câu khẳng định dùng watched.'),
        text('Write the past form of dance.','danced','Dance đã có e, thêm d.'),
        match([('I','was'),('we','were'),('play yesterday','played')],'I was; we were; play → played.'),
        reorder('Were you at the funfair yesterday?','Were you at…?'),
        text('Rewrite in full: We weren’t at the theatre.','We were not at the theatre.','Weren’t = were not.',2),
        text('Complete: I ___ to music yesterday. Use listen.','listened','Listen → listened.',2),
        shown(reorder(action(c),'Đổi dance thành danced theo thẻ.',2),c),
        reorder('What did you do last Saturday?','Sau did dùng do.',2),
        text('Complete: We danced ___ the campfire.','around','Dance around the campfire.',2),
        text('Rewrite in full: I wasn’t at the aquarium.','I was not at the aquarium.','Wasn’t = was not.',2),
        shown(text('Write the location and then activity sentence using the card subject.',where(a)+' '+action(a),'We were… We listened…',3),a),
        shown(text('Write the full location sentence including time.',where(b),'We were at the aquarium last Saturday.',3),b),
        shown(text('Write the activity sentence using the card subject.',action(d),'We played chess.',3),d),
        shown(text('Write the location and then activity sentence using I.',where(PROFILES[5])+' '+action(PROFILES[5]),'I was… I watched…',3),PROFILES[5]),
    ]


def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    days=['yesterday','last Saturday','last Sunday','last summer']
    return [
        listen('Listen and choose the place.',where(a),[field('Place:',a['place'],CORE)]),
        listen('Listen and choose the activity.',action(b),[field('Activity:',past(b),PAST)],2),
        listen('Listen. When was the outing?',passage(b),[field('Time:',b['day'],days)]),
        listen('Listen. Where was the speaker or group?',passage(c),[field('Place:',c['place'],CORE)],2),
        listen('Listen and choose the place and activity.',passage(a),[field('Place:',a['place'],CORE),field('Activity:',past(a),PAST)],3),
        listen('Listen and write the time and past activity phrase.',passage(c),[field('Time:',c['day']),field('Activity:',past(c))],3),
    ]


def build_tests():
    import copy
    written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
    mixed=[copy.deepcopy(written[i%5][i]) for i in range(18)]
    return [assemble(qs,listening(i)) for i,qs in enumerate(written+[mixed])]
