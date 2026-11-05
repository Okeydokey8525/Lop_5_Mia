"""Original cross-unit Review 2, verified pages 74–77 (Units 6–10)."""
from english.practice import mc,text as base_text,match,reorder,tf,based,field,listen,assemble
from english.u06.content import picture as room_picture
from english.u07.content import picture as school_picture
from english.u08.content import picture as object_picture
from english.u09.content import picture as place_picture
from english.u10.content import picture as trip_picture

CORE=['library','do projects','glue stick','aquarium']
PROFILES=[
 dict(name='An',room='library',floor='second',activity='doing projects',reason='useful',object='glue stick',position='beside the notebook',place='aquarium',past='watched the fish',destination='Hoan Kiem Lake',trip='walked around the lake',month='November'),
 dict(name='Linh',room='music room',floor='first',activity='reading books',reason='interesting',object='crayon',position='under the desk',place='campsite',past='played chess',destination='Ba Na Hills',trip='visited the old buildings',month='December'),
 dict(name='Minh',room='art room',floor='ground',activity='playing games',reason='fun',object='set square',position='in front of the pencil case',place='theatre',past='listened to music',destination='Suoi Tien Theme Park',trip='played games',month='November'),
 dict(name='Mai',room='computer room',floor='third',activity='solving maths problems',reason='useful',object='pencil sharpener',position='beside the book',place='campsite',past='danced around the campfire',destination='Bai Dinh Pagoda',trip='visited the old buildings',month='December'),
 dict(name='Nam',room='library',floor='first',activity='doing projects',reason='fun',object='crayon',position='under the chair',place='aquarium',past='watched the fish',destination='Ba Na Hills',trip='planted trees',month='September'),
 dict(name='Hoa',room='art room',floor='second',activity='reading books',reason='useful',object='glue stick',position='beside the book',place='theatre',past='listened to music',destination='Hoan Kiem Lake',trip='walked around the lake',month='October'),
]
ROOMS=['library','music room','art room','computer room'];FLOORS=['ground','first','second','third']
ACTIVITIES=['doing projects','reading books','playing games','solving maths problems']
REASONS=['useful','interesting','fun','good for group work']
PLACES=['aquarium','campsite','theatre','funfair']
DESTINATIONS=['Hoan Kiem Lake','Ba Na Hills','Suoi Tien Theme Park','Bai Dinh Pagoda']


def text(stem,answer,why,lesson=1,alternatives=()):
    variants=list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short=answer.replace('It is',"It's").replace('it is',"it's").replace('did not',"didn't").replace('were not',"weren't")
        if short!=answer:variants.append(short)
    return base_text(stem,answer,why,lesson,variants)


def picture(name,width=320):return {'library':room_picture,'do projects':school_picture,'glue stick':object_picture,'aquarium':place_picture,'plant trees':trip_picture}[name](name,width)
def school_card(p):return f"Name: {p['name']} · Room: {p['room']} · Floor: {p['floor']} · Likes: {p['activity']} · Reason: {p['reason']} · Owner: {p['name']} · Object: {p['object']} · Position: {p['position']}."
def trip_card(p):return f"Name: {p['name']} · Yesterday: {p['place']} · Yesterday’s activity: {p['past']} · School-trip destination: {p['destination']} · Trip time: last {p['month']} · Trip activity: {p['trip']}."
def school_passage(p):return f"I am {p['name']}. The {p['room']} is on the {p['floor']} floor. I like {p['activity']} because I think it is {p['reason']}. This is my {p['object']}. It is {p['position']}."
def trip_passage(p):return f"I am {p['name']}. Yesterday, my friends and I were at the {p['place']}. We {p['past']}. On our school trip last {p['month']}, we went to {p['destination']}. We {p['trip']}."
def tag(q,*units):q['sourceUnits']=list(units);return q
def shown(q,p,*units,trip=False):return tag(based(q,trip_card(p) if trip else school_card(p)),*units)


def written(index,kind):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    if kind==3:
        qs=[]
        for p in [a,b]:
            qs += [tag(based(q,school_passage(p)),u) for q,u in [
                (text('Write the pupil’s name.',p['name'],'Tên trong bài đọc.'),6),
                (mc('Which room is in this passage?',ROOMS,p['room'],'Đọc room.'),6),
                (text('Write the floor word only.',p['floor'],'Đọc tầng của đúng phòng.'),6),
                (text('Write the school activity in the -ing form.',p['activity'],'Đọc sở thích.',2),7),
                (text('Write the reason word only.',p['reason'],'Đọc lý do, không suy từ hoạt động.',2),7),
                (text('Write the object’s position phrase.',p['position'],'Đọc đúng vị trí đồ vật.',3),8)]]
        for p in [b,c]:
            qs += [tag(based(q,trip_passage(p)),*units) for q,units in [
                (text('Where was the group yesterday? Write the place only.',p['place'],'Phân biệt chuyến yesterday và school trip.',3),[9]),
                (text('Write the school-trip destination only.',p['destination'],'Địa điểm school trip, không phải yesterday.',3),[10]),
                (text('Write only the school-trip activity phrase.',p['trip'],'Hoạt động thuộc chuyến school trip.',3),[9,10])]]
        qs[0]=tag(based(tf([(f"The speaker is {a['name']}.",True),(f"The speaker is {b['name']}.",False)],'Đọc tên trong phần giới thiệu.'),school_passage(a)),6)
        qs[-1]=tag(based(mc('Which order matches the trip story?',[
            'planted trees → played games → walked around the lake',
            'played games → planted trees → walked around the lake',
            'walked around the lake → played games → planted trees',
            'planted trees → walked around the lake → played games'],
            'planted trees → played games → walked around the lake','Đọc First → Then → Finally, không sắp theo sở thích.',3),
            'On their school trip, the class planted trees first. Then they played games. Finally, they walked around the lake.'),10)
        return qs
    if kind==4:
        qs=[]
        for p in [a,b,c]:
            qs += [shown(text('Write the room’s location, starting with The.',f"The {p['room']} is on the {p['floor']} floor.",'On the + tầng + floor.'),p,6),
                shown(text('Write the owner reply: Whose object is this? Start with It.',f"It is {p['name']}’s.",'It is + tên’s.'),p,8),
                shown(text('Write one sentence about the activity, starting with I like.',f"I like {p['activity']}.",'Like + V-ing.',2),p,7),
                shown(text('Write one sentence about yesterday’s place, starting with We were.',f"We were at the {p['place']} yesterday.",'We were at…yesterday.',2),p,9,trip=True),
                shown(text('Write the school-trip destination and month in one sentence, starting with We went.',f"We went to {p['destination']} last {p['month']}.",'We went to…last + tháng.',3),p,10,trip=True),
                shown(text('Write one sentence for the school-trip activity, starting with We.',f"We {p['trip']}.",'Đúng hoạt động quá khứ của chuyến đi.',3),p,10,trip=True)]
        qs[0]=shown(reorder(f"The {a['room']} is on the {a['floor']} floor.",'Sắp câu theo thẻ phòng và tầng.'),a,6)
        owners=[a['name']]+[p['name'] for p in PROFILES if p['name']!=a['name']][:3]
        qs[1]=shown(mc('Choose the correct owner reply.',[f'It is {name}’s.' for name in owners],f"It is {a['name']}’s.",'Dùng tên chủ sở hữu + ’s.'),a,8)
        return qs
    if kind==2:return [
        shown(text('Where is the room? Start with It.',f"It is on the {a['floor']} floor.",'It is on the…floor.'),a,6),
        tag(text('Complete: What school activity does she ___?','like','Sau does dùng like.'),7),
        shown(text('Whose object is this? Start with It.',f"It is {b['name']}’s.",'Tên chủ sở hữu và ’s.'),b,8),
        tag(mc('Were you at the campsite yesterday?',['Yes, we were.','Yes, we did.','Yes, we do.','Yes, we was.'],'Yes, we were.','Were you…? → we were.'),9),
        tag(mc('Did they go to Ba Na Hills?',['Yes, they did.','Yes, they were.','Yes, they do.','Yes, they went.'],'Yes, they did.','Did they…? → they did.'),10),
        tag(reorder('Could you tell me the way to the art room, please?','Hỏi đường lịch sự.'),6),
        shown(text('Why do you like this activity? Start with Because I think.',f"Because I think it is {a['reason']}.",'Lý do của đúng người.',2),a,7),
        shown(text('Where is the object? Start with It.',f"It is {c['position']}.",'Đọc cả giới từ và vật làm mốc.',2),c,8),
        tag(text('Complete: No, we ___. Use the negative of were.','were not','Were not = weren’t.',2),9),
        tag(text('Complete: No, they ___. Use the negative of did.','did not','Did not = didn’t.',2),10),
        tag(text('Rewrite in full: It’s on the first floor.','It is on the first floor.','It’s = It is.',2),6),
        tag(match([('Where is the library?','On the second floor.'),('Whose crayon is this?','It is Mai’s.'),('What did they do?','They planted trees.')],'Ghép đúng loại câu hỏi.',2),6,8,10),
        shown(text('What did the group do yesterday? Start with We.',f"We {b['past']}.",'Chỉ dùng hoạt động yesterday.',2),b,9,trip=True),
        tag(tf([('After does, use like.',True),('After did, use went in the question.',False)],'Sau does/did dùng nguyên mẫu.',3),7,10),
        shown(text('Write the school-trip destination sentence with the month, starting with We went.',f"We went to {c['destination']} last {c['month']}.",'Đúng chuyến đi và thời gian.',3),c,10,trip=True),
        shown(text('Write one sentence about activity and reason, starting with I like and using because.',f"I like {b['activity']} because I think it is {b['reason']}.",'Đọc cả hoạt động và lý do trong thẻ.',3),b,7),
        tag(text('Rewrite in full: They didn’t go to the lake.','They did not go to the lake.','Sau did not giữ go.',3),10),
        shown(text('Write the owner reply and then the object’s position, both starting with It.',f"It is {a['name']}’s. It is {a['position']}.",'Tách rõ của ai và ở đâu.',3),a,8)]
    qs=[
        tag(mc('Which room is in the picture?',ROOMS,'library','Thư viện có sách và hoạt động đọc.',1,picture('library')),6),
        shown(text('Write the floor word only.',a['floor'],'Đọc Floor, không nhầm ground và first.'),a,6),
        shown(text('Write the school activity in the -ing form.',a['activity'],'Đọc Likes.'),a,7),
        shown(text('Whose object is this? Write the name only.',a['name'],'Đọc Owner.'),a,8),
        tag(match([('above','phía trên'),('useful','hữu ích'),('campsite','khu cắm trại')],'Ghép từ của ba Unit.'),7,8,9),
        tag(text('Complete: Did they ___ to Hoan Kiem Lake?','go','Sau did dùng go.'),10),
        shown(mc('Which place did the group visit yesterday?',PLACES,b['place'],'Chỉ đọc mục Yesterday.'),b,9,trip=True),
        shown(text('Write the school-trip month only, without last.',b['month'],'Đọc Trip time.'),b,10,trip=True),
        tag(text('Complete: She ___ reading books.','likes','She likes + V-ing.',2),7),
        tag(reorder('They are under the desk.','Số nhiều dùng They are.',2),8),
        shown(text('Write the object’s full position phrase.',c['position'],'Đọc vị trí từ đúng thẻ.',2),c,8),
        tag(mc('Choose the correct past phrase.',['planted trees','planting trees yesterday','did planted trees','were plant trees'],'planted trees','Câu kể quá khứ dùng planted.',2),10),
        tag(text('Complete: We ___ at the aquarium yesterday.','were','We were.',2),9),
        tag(tf([('Ground floor is below first floor in this book.',True),('Whose asks where a room is.',False)],'Đúng tầng và đúng loại câu hỏi.',3),6,8),
        shown(text('Write the room location sentence, starting with It.',f"It is on the {b['floor']} floor.",'On the + tầng + floor.',3),b,6),
        shown(text('Write one school-trip activity sentence, starting with We.',f"We {c['trip']}.",'Không lẫn với hoạt động yesterday.',3),c,10,trip=True),
        based(tag(match([(p['name'],p['destination']+' / '+p['month']) for p in [a,b,c]],'Ghép từng người với đúng nơi và tháng của school trip.',3),10),'\n'.join(trip_card(p) for p in [a,b,c])),
        shown(text('Write yesterday’s place then activity, starting each sentence with We.',f"We were at the {a['place']} yesterday. We {a['past']}.",'Kết hợp were và động từ quá khứ.',3),a,9,trip=True)]
    if kind==1:
        qs[:4]=[tag(mc('Choose the word or phrase for this picture.',CORE,k,'Tên phòng/đồ dùng/địa điểm/hoạt động phù hợp tranh.',1,picture(k)),[6,7,8,9][i]) for i,k in enumerate(CORE)]
        qs[8]=tag(text('Complete: They ___ trees last November. Use plant.','planted','Plant → planted.',2),10)
        qs[12]=tag(based(mc('Which holiday type is written on this card?',['winter holiday','beach holiday','sightseeing holiday','adventure holiday'],'winter holiday','Đáp án theo thẻ, phần mở rộng 76–77.',3),'Holiday type: winter holiday. Activity: skiing.'),9,10)
    return qs


def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    return [tag(listen('Listen and choose the floor.',f"The {a['room']} is on the {a['floor']} floor.",[field('Floor:',a['floor'],FLOORS)]),6),
        tag(listen('Listen and choose the school activity.',f"I like {b['activity']} because I think it is {b['reason']}.",[field('Activity:',b['activity'],ACTIVITIES)]),7),
        tag(listen('Listen and find the owner.',f"This is {c['name']}’s {c['object']}. It is {c['position']}.",[field('Owner:',c['name'],[p['name'] for p in PROFILES])],2),8),
        tag(listen('Listen and find yesterday’s place.',trip_passage(a),[field('Yesterday’s place:',a['place'],PLACES)],2),9),
        tag(listen('Listen for school-trip destination and month.',trip_passage(b),[field('Destination:',b['destination'],DESTINATIONS),field('Month:',b['month'],['September','October','November','December'])],3),9,10),
        tag(listen('Listen and write yesterday’s activity and school-trip activity.',trip_passage(c),[field('Yesterday’s activity:',c['past']),field('School-trip activity:',c['trip'])],3),9,10)]


def build_tests():
    return [assemble(written(i,i) if i<5 else [written(i,k%5)[k] for k in range(18)],listening(i)) for i in range(6)]
