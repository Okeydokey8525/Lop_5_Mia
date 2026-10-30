"""Original Unit 1 practice, based on verified scope in NOTES.md."""
import html
import base64
from pathlib import Path

TESTS = [
    ('KhoiDong', 'Khởi động', 'Làm quen từ vựng, tên, lớp và nơi sống.'),
    ('TuVungVaHinhAnh', 'Từ vựng và hình ảnh', 'Nhận biết từ qua hình tự vẽ, ghép nghĩa và viết từ.'),
    ('MauCauVaHoiThoai', 'Mẫu câu và hội thoại', 'Chọn lời đáp phù hợp và hoàn thành hội thoại.'),
    ('DocHieu', 'Đọc hiểu', 'Đọc các hồ sơ tự soạn và tìm đúng thông tin.'),
    ('VietCau', 'Viết câu', 'Điền từ, sửa câu và sắp xếp từ theo gợi ý rõ ràng.'),
    ('TongHop', 'Tổng hợp', 'Kết hợp từ vựng, hội thoại, đọc và viết trong Unit 1.'),
]
PROFILES = [
    dict(name='An', cls='5A', place='city', colour='pink', sport='table tennis', food='a sandwich', animal='a dolphin'),
    dict(name='Linh', cls='5D', place='countryside', colour='blue', sport='swimming', food='pizza', animal='a panda'),
    dict(name='Minh', cls='5C', place='city', colour='green', sport='football', food='fish and chips', animal='a dolphin'),
    dict(name='Mai', cls='5B', place='countryside', colour='red', sport='basketball', food='a sandwich', animal='a panda'),
]


def q(kind, stem, why, lesson=2, **fields):
    return dict(type=kind, stem=stem, why=why, lesson=lesson, **fields)


def mc(stem, options, answer, why, lesson=2, fig=None):
    assert len(options)==4 and len(set(options))==4 and answer in options
    result=q('pic' if fig else 'mc', stem, why, lesson, opts=options, answer=options.index(answer))
    if fig: result['fig']=fig
    return result


def text(stem, answer, why, lesson=2, alternatives=()):
    return q('text', stem, why, lesson, answers=[answer, *alternatives],
             exactForm='full form' in stem.lower() or 'rewrite in full' in stem.lower())


def reorder(sentence, why, lesson=1):
    return q('reorder', 'Put the words in order.', why, lesson, items=sentence.split())


def match(pairs, why, lesson=2):
    assert len({b for a,b in pairs})==len(pairs)
    return q('match', 'Match each item with the correct answer.', why, lesson,
             pairs=[dict(left=a,right=b) for a,b in pairs])


def tf(items, why, lesson=2):
    return q('tf', 'Read and choose True (Đúng) or False (Sai).', why, lesson,
             items=[dict(t=s,a=a) for s,a in items])


def profile(p):
    return (f"Hello! My name is {p['name']}. I am in Class {p['cls']}. I live in the {p['place']}. "
            f"My favourite colour is {p['colour']}. My favourite sport is {p['sport']}. "
            f"My favourite food is {p['food']}. My favourite animal is {p['animal']}.")


def card(p):
    return '\n'.join([f"Name: {p['name']}",f"Class: {p['cls']}",f"Home: {p['place']}",
                      f"Colour: {p['colour']}",f"Sport: {p['sport']}",f"Food: {p['food']}",f"Animal: {p['animal']}"])


def based(question, passage):
    question['passage']=passage
    return question


def picture(kind, width=320):
    # Embed for standalone HTML; web build extracts the same bytes to shared assets.
    name=kind.replace(' ','-')
    image=Path(__file__).parent/'images'/f'{name}.webp'
    src='data:image/webp;base64,'+base64.b64encode(image.read_bytes()).decode('ascii')
    labels={'pink':'Mảng màu hồng','sandwich':'Bánh mì kẹp','table tennis':'Bàn, lưới, vợt và bóng bàn','city':'Đường phố và các tòa nhà trong thành phố','countryside':'Ngôi nhà giữa cánh đồng quê','dolphin':'Con cá heo'}
    return (f'<div class="fig en-figure"><img src="{src}" alt="{html.escape(labels[kind])}" '
            f'width="768" height="512" style="width:{width}px;max-width:100%;height:auto;display:block;border-radius:12px" decoding="async"></div>')


def warmup():
    return [
      mc('Which word means “lớp học”?',['class','colour','food','sport'],'class','Class nghĩa là lớp học.',1),
      mc('Choose the word for this colour.',['blue','pink','green','red'],'pink','Mảng màu là màu hồng: pink.',fig=picture('pink')),
      text('Complete the word: c _ t y. Write the whole word.','city','Từ đúng là city: thành phố.',1),
      mc("I am ___ Class 5A.",['on','at','in','to'],'in','Dùng in trước Class: in Class 5A.',1),
      mc('I live in the ___. Choose the word for this picture.',['class','food','sport','countryside'],'countryside','Hình là đồng quê: countryside.',1,picture('countryside')),
      text('Complete with the word for “tên”: My ___ is An.','name','My name is… dùng để nói tên.',1),
      match([('city','thành phố'),('countryside','nông thôn'),('class','lớp học')],'Ghép nghĩa: city = thành phố; countryside = nông thôn; class = lớp học.',1),
      mc('Which one is a sport?',['pink','a dolphin','table tennis','a sandwich'],'table tennis','Table tennis là môn bóng bàn.'),
      tf([('Pink is a colour.',True),('A sandwich is a sport.',False)],'Pink là màu sắc; sandwich là đồ ăn.'),
      reorder('I live in the city.','Câu giới thiệu nơi sống: I live in the city.'),
      mc('A: What is your favourite animal? B: ___.',["It's pink.","It's a dolphin.","I'm in Class 5B.","It's table tennis."],"It's a dolphin.",'Câu hỏi hỏi con vật; a dolphin là cá heo.'),
      text('Complete the question: What is your favourite ___? It is pink.','colour','Pink là màu, nên hỏi favourite colour.',alternatives=['color']),
      match([('favourite sport','table tennis'),('favourite colour','pink'),('favourite animal','a dolphin'),('favourite food','a sandwich')],'Ghép đúng nhóm: môn thể thao, màu sắc, con vật và đồ ăn.'),
      reorder('My favourite food is a sandwich.','My favourite food is… giới thiệu đồ ăn yêu thích.',2),
      text('Write the full form of “I’m”.','I am','I’m là dạng rút gọn của I am.',1),
      tf([('“I live in the city.” tells us a place.',True),('“I am in Class 5A.” tells us a favourite food.',False)],'City nói nơi sống; Class 5A nói lớp học.',1),
      based(mc('Which class is An in?',['5B','5C','5D','5A'],'5A','Hồ sơ ghi Class: 5A.',1),card(PROFILES[0])),
      based(text('Write An’s favourite sport.','table tennis','Hồ sơ ghi Sport: table tennis.'),card(PROFILES[0])),
      based(tf([('Linh lives in the countryside.',True),('Linh’s favourite colour is pink.',False)],'Hồ sơ của Linh: countryside, blue.',3),card(PROFILES[1])),
      based(text('Complete a sentence about yourself using this card: My name is ___.','Mai','Thẻ ghi tên Mai.',1),card(PROFILES[3])),
      reorder('Can you tell me about yourself?','Thứ tự câu hỏi là Can you tell me about yourself?',1),
      mc('Choose the correct sentence.',['I live in city the.','I lives in the city.','I live in the city.','I living in the city.'],'I live in the city.','Chủ ngữ I đi với live; cụm nơi sống là in the city.',1),
      based(match([('Name',PROFILES[2]['name']),('Class',PROFILES[2]['cls']),('Home',PROFILES[2]['place'])],'Dựa vào đúng ba dòng Name, Class, Home của thẻ.',3),card(PROFILES[2])),
      based(text('Write a full sentence about the favourite colour. Start with “My”.','My favourite colour is red.','Thẻ ghi Colour: red; ghép mẫu My favourite colour is…',3,alternatives=['My favorite color is red.']),card(PROFILES[3])),
    ]


def vocabulary():
    qs=[]
    for word,opts in [('city',['city','class','pink','food']),('dolphin',['table tennis','sandwich','dolphin','pink']),('table tennis',['football','basketball','swimming','table tennis']),('sandwich',['a sandwich','a dolphin','pink','a class'])]:
      answer='a sandwich' if word=='sandwich' else word
      qs.append(mc('Look at the picture. Choose the matching word.',opts,answer,f'Hình tự vẽ minh họa {word}.',1 if word=='city' else 2,picture(word)))
    qs += [
      text('Complete: p _ n k. Write the whole word.','pink','Pink có bốn chữ cái: p-i-n-k.'),
      text('Complete: d o l _ h i n. Write the whole word.','dolphin','Chữ còn thiếu là p: dolphin.'),
      mc('Which word is a place to live?',['sandwich','pink','countryside','tennis'],'countryside','Countryside nghĩa là nông thôn.',1),
      match([('pink','màu hồng'),('dolphin','cá heo'),('sandwich','bánh mì kẹp')],'Ghép đúng nghĩa của từng từ.'),
      tf([('Table tennis is a sport.',True),('A dolphin is a colour.',False)],'Table tennis là môn thể thao; dolphin là con vật.'),
      mc('Which word completes “favourite ___”? Answer: a sandwich.',['class','food','colour','animal'],'food','Sandwich thuộc nhóm đồ ăn: food.'),
      text('Write the two-word name of the sport shown.', 'table tennis','Đây là môn bóng bàn: table tennis.'),
      text('Which word is missing? sand _ ich. Write the whole word.','sandwich','Sandwich viết có w: s-a-n-d-w-i-c-h.'),
      match([('sport','swimming'),('colour','blue'),('food','pizza'),('animal','a panda')],'Swimming là môn thể thao; blue là màu; pizza là đồ ăn; panda là con vật.'),
      reorder('My favourite animal is a dolphin.','Dùng a trước dolphin khi nói một con cá heo.',2),
      mc('Which pair contains only sports?',['pink and blue','table tennis and swimming','pizza and a sandwich','a panda and a dolphin'],'table tennis and swimming','Cả table tennis và swimming đều là môn thể thao.'),
      tf([('City and countryside are places to live.',True),('Class and colour mean the same thing.',False)],'Class là lớp học; colour là màu sắc.',1),
      text('Which syllable is stressed in “tennis”? Write “first” (âm đầu) or “second” (âm thứ hai).','first','Tennis nhấn âm đầu; phần phát âm của Lesson 3.',3),
      text('Which syllable is stressed in “dolphin”? Write “first” (âm đầu) or “second” (âm thứ hai).','first','Dolphin nhấn âm đầu theo Lesson 3.',3),
      based(mc('Which thing in the card is a food?',['red','basketball','a sandwich','a panda'],'a sandwich','Thẻ ghi Food: a sandwich.',3),card(PROFILES[3])),
      based(text('Find the animal in this card. Write the complete phrase.','a panda','Thẻ ghi Animal: a panda.',3),card(PROFILES[1])),
      match([('I live in the…','countryside.'),('I am in…','Class 5B.'),('My favourite colour is…','pink.'),('My favourite food is…','a sandwich.')],'Chọn phần cuối theo đúng nơi sống, lớp, màu và đồ ăn.',3),
      mc('Choose the correct spelling.',['countrysied','countrysid','countryside','countrisyde'],'countryside','Từ đúng là countryside; xem lại thứ tự chữ cái.',1),
      based(text('Complete using the card: My favourite ___ is green.','colour','Green nằm ở mục Colour.',3,alternatives=['color']),card(PROFILES[2])),
      reorder('My favourite sport is table tennis.','Table tennis là cụm hai từ chỉ môn bóng bàn.',3),
    ]
    qs[10]['fig']=picture('table tennis')
    return qs


def dialogue():
    return [
      mc('A: Hello! My name is Mai. B: ___.',['Hello! I’m An.','It is pink.','A sandwich.','Table tennis.'],'Hello! I’m An.','Lời chào và giới thiệu tên phù hợp với lời của Mai.',1),
      text('A: My name ___ Linh.','is','My name đi với is.',1),
      mc('A: Can you tell me about yourself? B: ___.',['Pink is a colour.','I’m in Class 5D.','It’s a dolphin.','It’s pizza.'],'I’m in Class 5D.','Giới thiệu lớp là thông tin về bản thân.',1),
      reorder('I am in Class 5B.','Dùng I am in Class + tên lớp.',1),
      match([('What is your name?','My name is Mai.'),('What is your favourite food?','It is pizza.'),('Where do you live?','I live in the city.')],'Ghép câu hỏi về tên, đồ ăn và nơi sống với lời đáp đúng.',1),
      text('A: I live ___ the countryside.','in','Nói nơi sống dùng live in.',1),
      mc('A: What’s your favourite colour? B: ___.',['I am in Class 5A.','It’s a sandwich.','It’s pink.','I live in the city.'],'It’s pink.','Pink trả lời câu hỏi về màu sắc.'),
      mc('A: What’s your favourite sport? B: ___.',['It’s a panda.','It’s green.','My name is An.','It’s swimming.'],'It’s swimming.','Swimming là môn thể thao.'),
      tf([('“It is a dolphin.” can answer a question about a favourite animal.',True),('“It is blue.” answers a question about a favourite food.',False)],'Dolphin là con vật; blue là màu sắc.'),
      text('Ask about the other speaker. Complete with “my” or “your”: A: What is ___ favourite food? B: It is a sandwich.','your','Khi hỏi về người đối diện, dùng your.'),
      reorder('What is your favourite colour?','Mẫu hỏi: What is your favourite + nhóm điều yêu thích?',2),
      mc('A: What is your favourite animal? B: ___.',['My favourite animal is a panda.','My favourite animal are a panda.','My favourite animal am a panda.','My favourite animal in a panda.'],'My favourite animal is a panda.','Dùng is trong mẫu My favourite animal is…'),
      text('Write the full form of “What’s”.','What is','What’s là dạng rút gọn của What is.'),
      text('Write the full form of “It’s”.','It is','It’s là dạng rút gọn của It is.'),
      based(mc('An is speaking. Choose the answer about the favourite food.',['It’s pizza.','It’s a sandwich.','It’s fish and chips.','It’s pink.'],'It’s a sandwich.','Thẻ của An ghi Food: a sandwich.'),card(PROFILES[0])),
      match([('What’s your favourite colour?','It’s blue.'),('What’s your favourite animal?','It’s a dolphin.'),('What’s your favourite sport?','It’s football.')],'Blue là màu; dolphin là con vật; football là môn thể thao.'),
      reorder('My name is Minh.','Câu giới thiệu tên: My name is Minh.',1),
      based(text('Linh is speaking: I am in Class ___.',PROFILES[1]['cls'],f"Thẻ ghi Class: {PROFILES[1]['cls']}.",1),card(PROFILES[1])),
      based(text('Mai is speaking. Write a complete answer to “Where do you live?”.','I live in the countryside.','Thẻ của Mai ghi Home: countryside.',3),card(PROFILES[3])),
      based(mc('Minh is speaking. Which question matches “It is green.”?',['What is your name?','What’s your favourite food?','What’s your favourite colour?','What’s your favourite animal?'],'What’s your favourite colour?','Green nằm ở mục Colour trong thẻ.',3),card(PROFILES[2])),
      tf([('“My name’s Mai.” and “My name is Mai.” have the same meaning.',True),('“I’m in Class 5A.” and “I live in the city.” give the same information.',False)],'Hai cách nói tên tương đương; lớp học và nơi sống là hai thông tin khác nhau.',3),
      based(match([('My name is…',PROFILES[2]['name']+'.'),('My favourite food is…',PROFILES[2]['food']+'.'),('My favourite colour is…',PROFILES[2]['colour']+'.')],'Dựa vào tên, đồ ăn và màu trong thẻ của Minh.',3),card(PROFILES[2])),
      reorder('Can you tell me about yourself?','Can you + tell me + about yourself?',3),
      based(text('An is speaking. Write a full answer about the favourite animal. Start with “My”.','My favourite animal is a dolphin.','Thẻ ghi Animal: a dolphin; dùng mẫu My favourite animal is…',3),card(PROFILES[0])),
    ]


def reading_block(p):
    other=next(x for x in PROFILES if x['place']!=p['place'])
    return [based(question,profile(p)) for question in [
      mc('What is the pupil’s name?',[x['name'] for x in PROFILES],p['name'],f"Bài đọc giới thiệu tên {p['name']}.",3),
      text('Which class is the pupil in? Write only the class code.',p['cls'],f"Thông tin lớp là Class {p['cls']}.",3),
      mc('Which place is in the profile?',['the city','the countryside','a zoo','a sports centre'],'the '+p['place'],f"Hồ sơ ghi I live in the {p['place']}.",3),
      tf([(f"The favourite colour is {p['colour']}.",True),(f"The pupil lives in the {other['place']}.",False)],f"Hồ sơ ghi màu {p['colour']} và nơi sống {p['place']}.",3),
      text('Write the favourite sport.',p['sport'],f"Môn thể thao trong hồ sơ là {p['sport']}.",3),
      match([('Colour',p['colour']),('Food',p['food']),('Animal',p['animal'])],f"Ghép từ hồ sơ: {p['colour']}; {p['food']}; {p['animal']}.",3),
      reorder('My favourite colour is '+p['colour']+'.','Dùng đúng màu đã cho trong bài đọc.',3),
      mc('Which sentence agrees with the profile?',[
        f"My favourite food is {p['food']}.",f"My favourite food is {other['food']}.",f"My favourite food is {p['colour']}.",f"My favourite food is {p['sport']}."],f"My favourite food is {p['food']}.",f"Food trong hồ sơ là {p['food']}.",3),
    ]]


def writing():
    p=PROFILES[3]
    return [
      text('Complete: I ___ in Class 5A.','am','I đi với am.',1),
      reorder('My name is Linh.','My name is + tên.',1),
      text('Complete: I live in ___ city.','the','Cụm đã học là in the city.',1),
      mc('Choose the correct sentence.',['I am Class in 5A.','I am in Class 5A.','I in am Class 5A.','I Class 5A am in.'],'I am in Class 5A.','Thứ tự đúng là I am in Class 5A.',1),
      reorder('I live in the countryside.','Nói nơi sống: I live in the countryside.',1),
      text('Complete: My favourite colour ___ pink.','is','Dùng is để nối với màu yêu thích.'),
      match([('I','am in Class 5A.'),('My name','is An.'),('I live','in the city.')],'Ghép phần đầu và cuối đúng cấu trúc.',1),
      text('Write the missing word: My favourite ___ is a dolphin.','animal','Dolphin là con vật nên dùng animal.'),
      reorder('My favourite sport is swimming.','My favourite sport is + tên môn thể thao.',2),
      text('Complete: What is your favourite ___? It is a sandwich.','food','Sandwich là đồ ăn.'),
      mc('Choose the correct word: ___ name is Mai.',['I','My','Me','Am'],'My','Cụm đúng là My name.',1),
      reorder('What is your favourite food?','What is your favourite food?',2),
      text('Rewrite with spaces: Iliveinthecity.','I live in the city.','Tách thành I / live / in / the / city.',1),
      reorder('My favourite colour is blue.','Mẫu câu có is trước màu.',2),
      text('Rewrite in full: I’m in Class 5C.','I am in Class 5C.','I’m tương đương I am.',1),
      mc('Which sentence is correct?',['My favourite sport is table tennis.','My favourite sport table tennis is.','My favourite is sport table tennis.','My sport favourite is table tennis.'],'My favourite sport is table tennis.','Cụm favourite sport đi cùng nhau, rồi đến is.'),
      reorder('It is a sandwich.','Dùng a trước danh từ số ít sandwich.',2),
      match([('favourite animal','is a dolphin.'),('in','Class 5D.'),('live in the','countryside.')],'Nối các cụm từ theo mẫu câu đã học.',2),
      based(text('Write one full sentence for the name on this card. Start with “My”.',f"My name is {p['name']}.",f"Tên trên thẻ là {p['name']}.",3),card(p)),
      based(text('Write one full sentence for the class on this card. Start with “I”.',f"I am in Class {p['cls']}.",f"Lớp trên thẻ là {p['cls']}.",3),card(p)),
      based(reorder('My favourite food is a sandwich.','Thẻ ghi đồ ăn là a sandwich.',3),card(p)),
      based(text('Write one full sentence for the home on this card. Start with “I”.',f"I live in the {p['place']}.",f"Nơi sống trên thẻ là {p['place']}.",3),card(p)),
      based(text('Write one full sentence for the colour. Start with “My”.',f"My favourite colour is {p['colour']}.",f"Màu trên thẻ là {p['colour']}.",3,alternatives=[f"My favorite color is {p['colour']}."]),card(p)),
      based(reorder('My favourite animal is a panda.','Thẻ ghi con vật yêu thích là a panda.',3),card(p)),
    ]


def mixed():
    p=PROFILES[1]
    return [
      mc('Look at the picture. Choose the correct word.',['class','city','countryside','colour'],'city','Các tòa nhà minh họa city.',1,picture('city')),
      text('Complete: I am ___ Class 5D.','in','Dùng in trước Class.',1),
      mc('Which one is an animal?',['a sandwich','a dolphin','pink','table tennis'],'a dolphin','Dolphin là cá heo.'),
      reorder('My name is Mai.','Giới thiệu tên: My name is Mai.',1),
      match([('colour','green'),('sport','football'),('food','fish and chips')],'Ghép đúng ba nhóm từ vựng.'),
      text('Complete the spelling: c l a _ s. Write the whole word.','class','Class có hai chữ s ở cuối.',1),
      tf([('A panda is an animal.',True),('Swimming is a food.',False)],'Panda là con vật; swimming là môn thể thao.'),
      mc('Choose the matching phrase.',['a dolphin','a sandwich','a class','a city'],'a sandwich','Hình minh họa bánh mì kẹp: a sandwich.',2,picture('sandwich')),
      text('A: What is your favourite colour? B: It ___ pink.','is','It đi với is.'),
      mc('Which word means “nông thôn”?',['city','class','countryside','sport'],'countryside','Countryside nghĩa là nông thôn.',1),
      based(text('Which class is Linh in?',p['cls'],f"Thẻ ghi lớp {p['cls']}.",3),card(p)),
      based(tf([(f"Linh lives in the {p['place']}.",True),('Linh’s favourite sport is football.',False)],f"Linh sống ở {p['place']} và thích {p['sport']}.",3),profile(p)),
      reorder('What is your favourite animal?','Hỏi con vật yêu thích: What is your favourite animal?',2),
      match([('What is your name?','My name is Minh.'),('What is your favourite sport?','It is basketball.'),('What is your favourite colour?','It is red.')],'Ghép câu hỏi với loại thông tin tương ứng.'),
      text('Write the full form: My name’s An.','My name is An.','My name’s là My name is.',1),
      mc('Choose the correct reply to “Can you tell me about yourself?”.',['I’m in Class 5B.','It is a food.','It is a colour.','A dolphin is an animal.'],'I’m in Class 5B.','Lớp học là thông tin để giới thiệu bản thân.',1),
      based(mc('What is Linh’s favourite colour?',['red','pink','blue','green'],p['colour'],f"Bài đọc ghi màu {p['colour']}.",3),profile(p)),
      based(text('Write Linh’s favourite food.',p['food'],f"Đồ ăn trong hồ sơ là {p['food']}.",3),profile(p)),
      based(match([('Home',p['place']),('Sport',p['sport']),('Animal',p['animal'])],'Đọc đúng nơi sống, môn thể thao và con vật trong hồ sơ.',3),profile(p)),
      based(text('Linh is speaking. Write a full sentence about the favourite sport. Start with “My”.',f"My favourite sport is {p['sport']}.",f"Sport là {p['sport']}; dùng My favourite sport is…",3),card(p)),
      reorder('I live in the countryside.','Sắp xếp theo mẫu I live in the + nơi sống.',3),
      mc('Which question asks about a favourite food?',['What is your name?','What is your favourite food?','Where do you live?','Can you tell me about yourself?'],'What is your favourite food?','Từ food xác định câu hỏi về đồ ăn.',3),
      tf([('“It’s blue.” and “It is blue.” mean the same thing.',True),('“My favourite animal is a dolphin.” tells us a class.',False)],'It’s tương đương It is; dolphin là con vật, không phải lớp.',3),
      based(text('Minh is speaking. Write the full sentence about the home. Start with “I”.','I live in the city.','Thẻ của Minh ghi nơi sống là city.',3),card(PROFILES[2])),
    ]


def build_tests():
    reading=sum([reading_block(p) for p in PROFILES[:3]],[])[:18]
    passage='\n\n'.join(card(p) for p in PROFILES[:3])
    def find(**facts):
        pupils=[p['name'] for p in PROFILES[:3] if all(p[key]==value for key,value in facts.items())]
        assert len(pupils)==1
        return pupils[0]
    choices=['An','Linh','Minh','An and Linh']
    for question in [
      mc('Who lives in the city and likes football?',choices,find(place='city',sport='football'),'Đối chiếu hai mục Home và Sport: Minh sống ở city và thích football.',3),
      mc('Who is in Class 5D and likes pizza?',choices,find(cls='5D',food='pizza'),'Đối chiếu Class và Food: Linh học lớp 5D và thích pizza.',3),
      match([(p['name'],p['food']) for p in PROFILES[:3]],'Ghép từng bạn với đúng dòng Food trong thẻ của bạn đó.',3),
      tf([('An and Minh live in the city.',all(p['place']=='city' for p in [PROFILES[0],PROFILES[2]])),('An’s favourite colour is pink, and Linh’s favourite colour is pink.',all(p['colour']=='pink' for p in PROFILES[:2]))],'An và Minh đều ghi city. An thích pink, Linh thích blue nên ý thứ hai sai.',3),
      text('Who lives in the city? This pupil’s favourite colour is green. Write the name.',find(place='city',colour='green'),'Cần khớp cả Home: city và Colour: green, đó là Minh.',3),
      text('An is speaking. Write a full sentence about the favourite food. Start with “My”.',f"My favourite food is {PROFILES[0]['food']}.",'Chọn đúng thẻ của An, đọc Food rồi viết theo mẫu My favourite food is…',3),
    ]:reading.append(based(question,passage))
    tests=[warmup(),vocabulary(),dialogue(),reading,writing(),mixed()]
    from english.u01.exam_listening import make_listening
    for test_index,questions in enumerate(tests):
        for position,question in zip([0,1,10,13,20,23],make_listening(test_index)):
            questions[position]=question
        assert len(questions)==24,len(questions)
        for i,question in enumerate(questions):
            question['level']='tb' if i<10 else 'kha' if i<18 else 'gioi'
    return tests
