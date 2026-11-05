"""Original classroom/location/ownership exercises, verified pages 56–61."""
from english.practice import mc,text as base_text,match,reorder,tf,based,picture as image,field,listen,assemble

OBJECTS={'glue stick':('glue sticks','hồ dán dạng thỏi'),'crayon':('crayons','bút sáp màu'),'set square':('set squares','ê-ke'),'pencil sharpener':('pencil sharpeners','gọt bút chì')}
CORE=list(OBJECTS)
POSITIONS={'beside':'bên cạnh','under':'bên dưới','above':'phía trên','in front of':'phía trước'}
PROFILES=[
 dict(owner='An',item='glue stick',position='beside',reference='notebook'),
 dict(owner='Linh',item='crayon',position='under',reference='desk'),
 dict(owner='Minh',item='set square',position='in front of',reference='pencil case'),
 dict(owner='Mai',item='pencil sharpener',position='beside',reference='book'),
 dict(owner='Nam',item='crayon',position='above',reference='bookcase'),
 dict(owner='Hoa',item='glue stick',position='under',reference='chair'),
]


def text(stem,answer,why,lesson=1,alternatives=()):
    variants=list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short=answer.replace('They are',"They're").replace('they are',"they're").replace('It is',"It's")
        if short!=answer:variants.append(short)
    return base_text(stem,answer,why,lesson,variants)


def picture(name,width=320):return image('u08',name.replace(' ','-'),OBJECTS[name][1],width)
def location(p):return p['position']+' the '+p['reference']
def own(p):return p['owner']+"'s"
def owner_reply(p):return 'It is '+own(p)+'.'
def location_reply(p):return 'It is '+location(p)+'.'
def plural_reply(p):return 'They are '+location(p)+'.'
def card(p):return f"Owner: {p['owner']} · One object: {p['item']} · Position: {location(p)}."
def passage(p):return f"This is {p['owner']}'s {p['item']}. {location_reply(p)} {p['owner']} has a tidy study corner."
def shown(q,p):return based(q,card(p))


def warmup():
    a,b,c,d=PROFILES[:4]
    return [
        mc('Look at the picture. Choose the classroom object.',CORE,'glue stick','Đây là hồ dán dạng thỏi.',1,picture('glue stick')),
        match([(k,v[1]) for k,v in OBJECTS.items()],'Ghép bốn đồ dùng với nghĩa.'),
        text('Complete: Where ___ the crayons?','are','Crayons số nhiều dùng are.'),
        mc('Choose the plural of set square.',['set squares','set square','sets square','set squaring'],'set squares','Thêm s vào square.'),
        reorder('They are under the desk.','They are + vị trí.'),
        text('Complete the whole word: c r a _ o n.','crayon','Crayon có chữ y sau a.'),
        mc('Which word asks who owns an object?',['Whose','Where','When','Why'],'Whose','Whose hỏi của ai.',2),
        shown(mc('Whose glue stick is this?',[own(p) for p in PROFILES[:4]],own(a),'Owner trong thẻ là An.',2),a),
        match(list(POSITIONS.items())[:3],'Beside: bên cạnh; under: bên dưới; above: phía trên.'),
        text('Complete: They are in front ___ the clock.','of','Cụm in front of.',2),
        shown(text('Write only the position phrase, including the reference object.',location(b),'Dùng under the desk từ thẻ.',2),b),
        reorder('Whose set square is this?','Whose + đồ vật số ít + is this?',2),
        text('Complete: It ___ Linh’s.','is','It is Linh’s.',2),
        shown(tf([('The set square is in front of the pencil case.',True),('The set square is under the desk.',False)],'Đọc đúng vị trí trong thẻ.',2),c),
        shown(text('Answer “Whose pencil sharpener is this?” Start with It.',owner_reply(d),'Chủ sở hữu là Mai.',3),d),
        shown(text('Answer “Where is the glue stick?” Start with It.',location_reply(a),'It is beside the notebook.',3),a),
        mc('Choose the correct plural question.',['Where are the pencils?','Where is the pencils?','Whose are this pencil?','Where the pencils are?'],'Where are the pencils?','Where are the + danh từ số nhiều?',3),
        shown(text('Write the full ownership sentence. Start with This is.',f"This is {own(c)} {c['item']}.",'Dùng tên + apostrophe s và đúng đồ vật.',3),c),
    ]


def vocabulary():return [
    *[mc('Look at the picture. Choose the object.',CORE,k,'Tranh minh họa '+v[1]+'.',1,picture(k)) for k,v in OBJECTS.items()],
    text('Complete: s h a r p _ n e r. Write the whole word.','sharpener','Sharpener có e trước n.'),
    text('Write the plural of crayon.','crayons','Crayon → crayons.'),
    match([(k,v[0]) for k,v in list(OBJECTS.items())[:3]],'Ghép dạng số ít và số nhiều.'),
    mc('Which phrase means “phía trước”?',list(POSITIONS),'in front of','In front of: phía trước.'),
    mc('Which word means “bên cạnh”?',list(POSITIONS),'beside','Beside: bên cạnh.',2),
    text('Complete: a ___ stick.','glue','Glue stick là hồ dán dạng thỏi.',2),
    match([('above','phía trên'),('under','bên dưới'),('in front of','phía trước')],'Đối chiếu đúng giới từ.',2),
    text('Write the plural of pencil sharpener.','pencil sharpeners','Chỉ thêm s vào sharpener.',2),
    reorder('The pictures are above the window.','Pictures số nhiều dùng are.',2),
    tf([('Above has second-syllable stress.',True),('Beside means “bên dưới”.',False)],'a-BOVE, be-SIDE nhấn âm sau; beside là bên cạnh.',3),
    shown(text('Write the classroom object only.',PROFILES[2]['item'],'Thẻ ghi set square.',3),PROFILES[2]),
    shown(text('Write the reference object only, without the.',PROFILES[3]['reference'],'Vật làm mốc là book.',3),PROFILES[3]),
    based(match([(p['owner'],location(p)) for p in PROFILES[:3]],'Ghép tên với vị trí đồ dùng từ đúng thẻ.',3),'\n'.join(card(p) for p in PROFILES[:3])),
    reorder('Whose pencil sharpener is this?','Whose + pencil sharpener + is this?',3),
]


def dialogue():
    a,b,c,d=PROFILES[:4]
    return [
        mc('A: Where are the pencils? B: ___.',['They are beside the book.','It is An’s.','He is ten.','I am fine.'],'They are beside the book.','Hỏi vị trí số nhiều dùng They are…'),
        text('Complete: Whose crayon ___ this?','is','Một crayon dùng is.'),
        reorder('Where are the pencil sharpeners?','Where are + đồ vật số nhiều?'),
        shown(mc('Whose pencil sharpener is this?',[owner_reply(p) for p in PROFILES[:4]],owner_reply(d),'Theo chủ sở hữu Mai.'),d),
        text('Complete: Are they under the desk? Yes, they ___.','are','Yes, they are.'),
        text('Complete: Are they beside the book? No, they ___.','are not','No, they are not.',alternatives=['aren’t']),
        shown(text('Answer “Where is the crayon?” Start with It.',location_reply(b),'It is under the desk.',2),b),
        shown(mc('Whose set square is this?',[own(p) for p in PROFILES[:4]],own(c),'Thẻ ghi Minh.',2),c),
        reorder('Is this your glue stick?','Is this your + đồ vật?',2),
        text('Rewrite in full: They’re above the window.','They are above the window.','They’re = They are.',2),
        text('Rewrite in full: It’s Mai’s.','It is Mai’s.','It’s = It is; Mai’s chỉ sở hữu.',2),
        match([('Whose crayon is this?','It is Linh’s.'),('Where are the pencils?','They are beside the book.'),('Is this your glue stick?','Yes, it is.')],'Phân biệt câu hỏi chủ sở hữu, vị trí và có/không.',2),
        shown(text('Answer with the owner, starting with It.',owner_reply(a),'It is An’s.',2),a),
        tf([('Whose asks about ownership.',True),('Where asks who owns an object.',False)],'Whose: của ai; Where: ở đâu.',2),
        shown(text('Write the owner reply and location reply, both starting with It.',owner_reply(d)+' '+location_reply(d),'Viết đủ It is Mai’s. It is beside the book.',3),d),
        based(text('Where are the crayons? Start with They.','They are under the desk.','They are under the desk.',3),'Objects: crayons (plural). Position: under the desk.'),
        text('Rewrite in full: They aren’t beside the clock.','They are not beside the clock.','Aren’t = are not.',3),
        mc('Choose the correct ownership question.',['Whose glue stick is this?','Who glue stick is this?','Whose glue stick are this?','Where glue stick this is?'],'Whose glue stick is this?','Whose + danh từ số ít + is this?',3),
    ]


def reading():
    qs=[]
    for p in PROFILES[:4]:
        other=next(x for x in PROFILES if x['position']!=p['position'])
        qs.extend(based(item,passage(p)) for item in [
            text('Write the owner’s name.',p['owner'],'Tìm tên đứng trước dấu sở hữu.',3),
            mc('Which object belongs to this pupil?',CORE,p['item'],'Đọc tên đồ dùng trong bài.',3),
            text('Write only the position phrase, including the reference object.',location(p),'Vị trí là '+location(p)+'.',3),
            tf([(f"The {p['item']} is {location(p)}.",True),(f"The {p['item']} is {location(other)}.",False)],'Đọc cả giới từ và vật làm mốc.',3),
        ])
    qs += [based(text('Whose crayon is above the bookcase? Write the name.','Nam','Linh và Nam đều có crayon nhưng vị trí khác nhau.',3),'\n'.join(card(p) for p in [PROFILES[1],PROFILES[4]])),
           based(text('Whose glue stick is under the chair? Write the name.','Hoa','An và Hoa đều có glue stick; đọc đúng vị trí.',3),'\n'.join(card(p) for p in [PROFILES[0],PROFILES[5]]))]
    return qs


def writing():
    a,b,c,d=PROFILES[:4]
    return [
        text('Complete: Where ___ the erasers?','are','Erasers số nhiều dùng are.'),
        reorder('They are in front of the clock.','They are + in front of + vật làm mốc.'),
        text('Complete: ___ glue stick is this?','Whose','Hỏi chủ sở hữu dùng Whose.'),
        text('Complete: It ___ An’s.','is','It is + tên sở hữu.'),
        mc('Choose the correct sentence.',['The pencils are beside the book.','The pencils is beside the book.','The pencils are beside of the book.','The pencils beside the book are.'],'The pencils are beside the book.','Số nhiều dùng are; beside không có of.'),
        text('Write the plural of set square.','set squares','Thêm s vào square.'),
        match([('one crayon','it is'),('two crayons','they are'),('An owns it','An’s')],'Phân biệt số lượng và sở hữu.'),
        reorder('Whose crayon is this?','Whose + crayon + is this?'),
        text('Rewrite in full: They’re under the chair.','They are under the chair.','They’re = They are.',2),
        text('Complete: The pictures are ___ the window. Use the word meaning “phía trên”.','above','Above nghĩa là phía trên.',2),
        shown(reorder(location_reply(c),'Theo vị trí set square trong thẻ.',2),c),
        reorder('Is this your pencil sharpener?','Is this your + đồ vật?',2),
        text('Complete: in ___ of the desk.','front','In front of là phía trước.',2),
        text('Rewrite in full: It’s Linh’s crayon.','It is Linh’s crayon.','It’s = It is; giữ Linh’s.',2),
        shown(text('Write one sentence starting with This is and naming the owner and object.',f"This is {own(a)} {a['item']}.",'This is An’s glue stick.',3),a),
        shown(text('Write the location sentence starting with It.',location_reply(d),'It is beside the book.',3),d),
        based(text('Where are the pencils? Start with They.','They are beside the notebook.','They are beside the notebook.',3),'Objects: pencils (plural). Position: beside the notebook.'),
        shown(text('Answer Whose crayon is this? Start with It.',owner_reply(b),'It is Linh’s.',3),b),
    ]


def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    refs=['notebook','desk','pencil case','book','bookcase','chair']
    return [
        listen('Listen and choose the object.',f"This is a {a['item']}.",[field('Object:',a['item'],CORE)]),
        listen('Listen and choose the position.',location_reply(b),[field('Position:',b['position'],list(POSITIONS))],2),
        listen('Listen. Whose object is this?',passage(b),[field('Owner:',b['owner'],[p['owner'] for p in PROFILES])]),
        listen('Listen and find the reference object.',passage(c),[field('Reference object:',c['reference'],refs)],2),
        listen('Listen and choose owner and position.',passage(a),[field('Owner:',a['owner'],[p['owner'] for p in PROFILES]),field('Position:',a['position'],list(POSITIONS))],3),
        listen('Listen and write object and position phrase.',passage(c),[field('Object:',c['item']),field('Position phrase:',location(c))],3),
    ]


def build_tests():
    import copy
    written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
    mixed=[copy.deepcopy(written[i%5][i]) for i in range(18)]
    return [assemble(qs,listening(i)) for i,qs in enumerate(written+[mixed])]
