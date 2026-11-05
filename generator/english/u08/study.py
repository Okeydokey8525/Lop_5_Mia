"""Classroom words, positions and ownership with isolated saved practice."""
from english.u08.content import OBJECTS, CORE, POSITIONS, picture
from english.study.author import word as w,question as q,choice as c,dialogue as d
from english.study.render import render_study as render


def data():
    words=[w('objects',name,vn,'This is a '+name+'.',image=name) for name,(_,vn) in OBJECTS.items()]
    words += [w('objects',plural,vn+' (số nhiều)','These are '+plural+'.') for _,(plural,vn) in OBJECTS.items()]
    words += [w('positions',name,vn,example) for name,vn,example in [
        ('beside','bên cạnh','The pencils are beside the book.'),('under','bên dưới','The erasers are under the desk.'),
        ('above','phía trên','The pictures are above the window.'),('in front of','phía trước','The pens are in front of the clock.')]]
    words += [w('ownership',name,vn,example) for name,vn,example in [
        ('whose','của ai','Whose glue stick is this?'),('this','đây, này (một vật ở gần)','This is a set square.'),('your','của bạn','Is this your crayon?')]]
    dialogues=[
        d('objects','Một đồ dùng','What is this?','It is a glue stick.','Một đồ dùng: It is a…'),
        d('objects','Nhiều đồ dùng','What are these?','They are crayons.','Nhiều đồ dùng: They are…'),
        d('positions','Hỏi vị trí','Where are the pencils?','They are beside the book.','Where are…? — They are… khi hỏi nhiều đồ dùng.'),
        d('positions','Hỏi một đồ vật','Where is the set square?','It is under the desk.','Where is…? — It is… khi hỏi một đồ dùng.'),
        d('ownership','Hỏi của ai','Whose pencil sharpener is this?','It is An’s.','An’s = của An; dấu ’s sau tên thể hiện sở hữu.'),
        d('ownership','Trả lại đồ dùng','Is this your crayon?','No, it is not. It is Linh’s.','Đây không phải bút sáp của người trả lời; đó là của Linh.'),
    ]
    picture_q=c('object-listen','objects','Choose the object you hear.','set-square','Ê-ke có hình tam giác vuông.',[name.replace(' ','-') for name in CORE],speech='set square')
    picture_q.update(kind='picture',instruction='Nghe rồi chọn tranh đồ dùng.')
    exercises=[picture_q,
        q('object-spell','objects','c r a _ o n — Write the whole word.','crayon','Crayon có chữ y.'),
        q('object-plural','objects','Write the plural of glue stick.','glue sticks','Thêm s vào stick.'),
        q('object-are','objects','These ___ pencil sharpeners.','are','These dùng với số nhiều, theo sau là are.'),
        c('position-listen','positions','Where are the crayons?','under','Lời nghe nói under the desk.',list(POSITIONS),speech='The crayons are under the desk.'),
        q('position-of','positions','The pens are in front ___ the clock.','of','Cụm in front of.'),
        c('position-above','positions','Which word means “phía trên”?','above','Above là phía trên.',list(POSITIONS)),
        q('position-full','positions','Card: pencils / beside the book. Start with They.','They are beside the book.','They are beside the book.',alternatives=['They’re beside the book.']),
        q('owner-whose','ownership','___ crayon is this?','Whose','Hỏi của ai dùng Whose.'),
        c('owner-listen','ownership','Who owns the glue stick?','Linh','Lời nghe nói Linh’s glue stick.',['An','Linh','Minh','Mai'],speech='This is Linh’s glue stick.'),
        q('owner-mark','ownership','Card: owner An. It is ___. Write the possessive name.','An’s','Tên An + ’s: An’s.'),
        q('owner-full','ownership','Card: owner Mai. Whose set square is this? Start with It.','It is Mai’s.','It is Mai’s.',alternatives=['It’s Mai’s.']),
    ]
    return dict(unit=8,key='mia5:learn:en-u08-v1',intro='Đồ dùng ở đâu và của ai? Nghe tên đồ dùng, thử nhớ vị trí rồi luyện hỏi đáp.',groups=[
        dict(id='objects',name='Đồ dùng',tip='Một vật: a crayon / It is… Nhiều vật: crayons / They are… Thêm s vào từ cuối: glue sticks, set squares, pencil sharpeners. Tranh từ đơn minh họa một đồ dùng.'),
        dict(id='positions',name='Vị trí',tip='a-BOVE, be-SIDE nhấn âm thứ hai. Above: phía trên; under: bên dưới; beside: bên cạnh; in front of: phía trước. Đọc cả vật làm mốc, không chỉ giới từ.'),
        dict(id='ownership',name='Của ai?',tip='Whose…is this? — It is + tên’s. Where hỏi vị trí; Whose hỏi chủ sở hữu. It’s = It is, nhưng An’s nghĩa là của An trong câu It’s An’s.')],words=words,dialogues=dialogues,exercises=exercises)


def render_study():return render(data(),picture)
