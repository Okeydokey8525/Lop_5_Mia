"""Original summer-plan exercises, volume two printed pages 64-69."""
from english.practice import mc, text as base_text, match, reorder, tf, based, picture as image, field, listen, assemble

CORE = ['join a music club', 'go camping', 'visit an eco-farm', 'practise swimming']
MEANINGS = ['tham gia câu lạc bộ âm nhạc', 'đi cắm trại', 'tham quan trang trại sinh thái', 'luyện bơi']
PLACES = ['Huong River', 'Phong Nha Cave', 'Phu Quoc Island', 'Dam Sen Aquarium']
PROFILES = [dict(name=n, pronoun=s, place=p, activity=a, past=old) for n, s, p, a, old in [
    ('An', 'He', PLACES[0], CORE[0], 'grew vegetables'),
    ('Linh', 'She', PLACES[1], CORE[1], 'joined a music club'),
    ('Minh', 'He', PLACES[2], CORE[3], 'went camping'),
    ('Hoa', 'She', PLACES[3], CORE[2], 'practised swimming'),
    ('Nam', 'He', PLACES[1], CORE[0], 'went camping'),
    ('Mai', 'She', PLACES[0], CORE[2], 'joined a music club'),
]]


def text(stem, answer, why, lesson=1, alternatives=()):
    accepted = list(alternatives)
    if 'practise' in answer:
        accepted.append(answer.replace('practise', 'practice'))
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short = answer.replace('We are', "We're").replace('They are', "They're")
        if short != answer:
            accepted.append(short)
    return base_text(stem, answer, why, lesson, accepted)


def picture(w, width=320):
    return image('u20', w.replace(' ', '-'), MEANINGS[CORE.index(w)], width)


def destination(p):
    return 'I am going to visit ' + p['place'] + '.'


def activity(p):
    return 'I am going to ' + p['activity'] + '.'


def card(p):
    return f"Original summer plan card: Name: {p['name']} · Pronoun: {p['pronoun']} · This summer: visit {p['place']}; {p['activity']} · Last summer: {p['past']}."


def passage(p):
    return f"My name is {p['name']}. Last summer, I {p['past']} with my cousins. This summer, {destination(p)[0].lower() + destination(p)[1:]} My family is going to travel by bus. {activity(p)} I am also going to learn a new language with my friends. We are going to take photos during our holiday. I am excited about our plans."


def shown(q, p):
    return based(q, card(p))


def warmup():
    return [
        mc('Look at the picture. Choose the summer activity.', CORE, CORE[1], 'Lều và đồ cắm trại: go camping.', 2, picture(CORE[1])),
        text('Complete: I ___ going to visit Huong River.', 'am', 'I am going to + động từ.'),
        match(list(zip(PLACES, ['sông Hương', 'động Phong Nha', 'đảo Phú Quốc', 'thủy cung Đầm Sen'])), 'Tên địa điểm trong Lesson 1.'),
        shown(mc('Where is An going to visit this summer?', PLACES, PLACES[0], 'Đọc nơi đến của An.'), PROFILES[0]),
        reorder('Where are you going to visit this summer?', 'Where hỏi nơi sẽ tham quan.'),
        text('Complete: What are you going to ___ this summer?', 'do', 'What…do hỏi hoạt động.', 2),
        shown(text('Write Linh’s activity phrase only.', CORE[1], 'Theo kế hoạch mùa hè này của Linh.', 2), PROFILES[1]),
        text('Complete: I am going ___ practise swimming.', 'to', 'Going to + nguyên mẫu.', 2),
        match(list(zip(CORE, MEANINGS)), 'Nhớ cả cụm hoạt động.', 2),
        reorder('I am going to join a music club.', 'Am going to join.', 2),
        text('Complete: Hoa ___ going to visit an eco-farm.', 'is', 'Hoa dùng is.', 2),
        shown(tf([('Minh is going to practise swimming this summer.', True), ('Minh went camping this summer.', False)], 'Kế hoạch this summer khác việc đã làm last summer.', 3), PROFILES[2]),
        text('Complete: We ___ going to take photos.', 'are', 'We are going to.'),
        shown(reorder(destination(PROFILES[3]), 'Visit + tên nơi, không visit to.', 1), PROFILES[3]),
        shown(text('Answer as An in full form, starting with I am: Where are you going to visit this summer?', destination(PROFILES[0]), 'Lấy nơi đến trong thẻ An.', 3), PROFILES[0]),
        shown(text('Answer as Hoa in full form, starting with I am: What are you going to do this summer?', activity(PROFILES[3]), 'Giữ an trước eco-farm.', 3), PROFILES[3]),
        mc('Choose the correct plan sentence.', ['She is going to go camping.', 'She are going to go camping.', 'She is going to went camping.', 'She is going go camping.'], 'She is going to go camping.', 'She is + going to + go.', 3),
        shown(text('Write two sentences as Linh in full form. Give destination first, then activity. Start each with I am.', destination(PROFILES[1]) + ' ' + activity(PROFILES[1]), 'Cả hai thông tin phải cùng thẻ Linh.', 3), PROFILES[1]),
    ]


def vocabulary():
    return [
        *[mc('Look at the picture. Choose the activity.', CORE, k, 'Tranh: ' + MEANINGS[i], 2, picture(k)) for i, k in enumerate(CORE)],
        text('Complete: I am going to join a music ___.', 'club', 'A music club: câu lạc bộ âm nhạc.', 2),
        match([('river', 'sông'), ('island', 'đảo'), ('aquarium', 'thủy cung')], 'Các loại địa điểm.'),
        text('Complete: I am going to visit ___ eco-farm. Choose a or an.', 'an', 'Eco bắt đầu bằng âm nguyên âm.', 2),
        text('Complete: I am going to ___ camping. Use the base form of went.', 'go', 'Going to + go, không went.', 2),
        match([('this summer', 'mùa hè này'), ('last summer', 'mùa hè năm ngoái'), ('next week', 'tuần tới')], 'Tìm mốc thời gian trước khi chọn câu.'),
        reorder('I am going to practise swimming.', 'Practise + swimming.', 2),
        text('Complete: I am going to grow ___ on an eco-farm. Use the plural of vegetable.', 'vegetables', 'Grow vegetables: trồng rau.', 2),
        text('Complete: I am going to learn a new ___. It means ngôn ngữ.', 'language', 'Learn a new language.', 3),
        shown(text('Write the place name only for Nam’s plan this summer.', PLACES[1], 'Đọc đúng thẻ Nam.'), PROFILES[4]),
        tf([('Visit an aquarium is a plan about a place to visit.', True), ('Last summer means mùa hè này.', False)], 'Place và mốc thời gian.'),
        shown(text('Write Mai’s activity sentence in full form, starting with I am.', activity(PROFILES[5]), 'Không lấy hoạt động của An dù cùng Huong River.', 3), PROFILES[5]),
        reorder('Where are you going to visit this summer?', 'Where + are you going to visit.', 3),
        text('Complete in full form: They ___ to take photos. Use be + going.', 'are going', 'They are going, không they is going.', 3),
        text('Rewrite in full: I’m going to join a music club.', 'I am going to join a music club.', 'I’m = I am.', 3),
    ]


def dialogue():
    return [
        mc('Which question asks about a place to visit this summer?', ['Where are you going to visit this summer?', 'What did you do last summer?', 'How far is it from here?', 'What are you going to do this summer?'], 'Where are you going to visit this summer?', 'Where hỏi nơi.'),
        text('Complete: Where ___ you going to visit this summer?', 'are', 'Are you going to.'),
        reorder('I am going to visit Phong Nha Cave.', 'Visit + địa điểm.'),
        shown(mc('What is Linh going to do this summer?', CORE, CORE[1], 'Linh: go camping.', 2), PROFILES[1]),
        text('Rewrite in full: She’s going to practise swimming.', 'She is going to practise swimming.', 'She’s = She is.', 2),
        text('Complete: What is he going to ___ this summer?', 'do', 'What…do hỏi hoạt động.', 2),
        shown(text('Answer as An in full form, starting with I am. Give the activity only.', activity(PROFILES[0]), 'An sẽ join a music club.', 2), PROFILES[0]),
        shown(mc('Which place is Hoa going to visit?', PLACES, PLACES[3], 'Theo thẻ Hoa.'), PROFILES[3]),
        reorder('What are you going to do this summer?', 'Are you, không you are trong câu hỏi.', 2),
        text('Rewrite in full: We’re going to visit Huong River.', 'We are going to visit Huong River.', 'We’re = We are.'),
        text('Complete: Nam is going to ___ a music club. Use join, joins or joined.', 'join', 'Sau going to dùng nguyên mẫu.', 2),
        match([('Where are you going to visit?', 'I am going to visit Huong River.'), ('What are you going to do?', 'I am going to go camping.'), ('What did you do last summer?', 'I grew vegetables.')], 'Phân biệt nơi, việc dự định và việc đã qua.', 3),
        shown(text('Answer as Minh in full form, starting with I am. Give the activity only.', activity(PROFILES[2]), 'Practise swimming.', 2), PROFILES[2]),
        tf([('Are you going to is the correct direct question order.', True), ('Is they going to is the correct question form.', False)], 'Are you/they, is he/she.', 3),
        shown(text('Write destination then activity as Hoa, in two full-form sentences starting with I am.', destination(PROFILES[3]) + ' ' + activity(PROFILES[3]), 'Cùng người, đúng nơi và hoạt động.', 3), PROFILES[3]),
        text('Rewrite in full: They’re going to go camping.', 'They are going to go camping.', 'They’re = They are.', 3),
        shown(text('Give Nam’s activity sentence, starting with He is, in full form.', 'He is going to join a music club.', 'Nam dùng he is, không lấy kế hoạch Linh.', 3), PROFILES[4]),
        mc('Choose the correct question.', ['Where is she going to visit this summer?', 'Where are she going to visit this summer?', 'Where she is going to visit this summer?', 'Where is she going visit this summer?'], 'Where is she going to visit this summer?', 'Is she going to visit.', 3),
    ]


def reading():
    qs = []
    for p in PROFILES[:4]:
        qs.extend(based(q, passage(p)) for q in [
            text('Who is speaking? Write the name only.', p['name'], 'Tên ở đầu đoạn.', 3),
            mc('Where is the speaker going to visit this summer?', PLACES, p['place'], 'Tìm going to visit.', 3),
            text('Besides learning a language and taking photos, what is the speaker going to do this summer? Write the activity phrase only.', p['activity'], 'Tìm kế hoạch sau câu nói về phương tiện; không lấy việc hè năm ngoái.', 3),
            tf([('The family is going to travel by bus.', True), ('The speaker is going to learn a new language alone.', False)], 'By bus; with friends, không alone.', 3),
        ])
    qs += [
        based(text('Both plan to visit Phong Nha Cave. Who is going to join a music club? Write the name only.', 'Nam', 'Linh sẽ cắm trại, Nam sẽ tham gia câu lạc bộ.', 3), '\n'.join(card(p) for p in [PROFILES[1], PROFILES[4]])),
        based(text('Write only what Minh did last summer, using the past activity phrase.', 'went camping', 'Last summer: went camping; this summer: practise swimming.', 3), passage(PROFILES[2])),
    ]
    return qs


def writing():
    return [
        text('Complete: I ___ going to visit an aquarium.', 'am', 'I am.'),
        reorder('We are going to visit Phu Quoc Island.', 'We are going to visit.'),
        text('Complete: She ___ going to go camping.', 'is', 'She is.', 2),
        text('Complete: They ___ going to practise swimming.', 'are', 'They are.', 2),
        mc('Choose the correct sentence.', ['I am going to visit Huong River.', 'I going to visit Huong River.', 'I am going visit Huong River.', 'I am going to visiting Huong River.'], 'I am going to visit Huong River.', 'Am going to + visit.'),
        text('Complete: I am going to ___ a music club. Use the base form of joined.', 'join', 'Going to join.', 2),
        match([('I', 'am going to'), ('she', 'is going to'), ('we', 'are going to')], 'Chọn đúng dạng be.'),
        reorder('What are you going to do this summer?', 'Đảo are trước you.', 2),
        text('Rewrite in full: He’s going to visit an eco-farm.', 'He is going to visit an eco-farm.', 'He is.', 2),
        text('Complete: I am going to practise ___. Use swim with -ing.', 'swimming', 'Gấp đôi m: swimming.', 2),
        shown(reorder(destination(PROFILES[2]), 'Visit, không visit to.', 2), PROFILES[2]),
        reorder('Where are you going to visit this summer?', 'Wh thường xuống giọng.', 3),
        text('Complete: I am going to visit ___ eco-farm. Use a or an.', 'an', 'An eco-farm.', 2),
        text('Rewrite in full: We’re going to grow vegetables.', 'We are going to grow vegetables.', 'We are.', 3),
        *[shown(text('Write two full-form sentences as this speaker. Destination first, then activity; start each with I am.', destination(p) + ' ' + activity(p), 'Đúng am going to, visit + nơi, hoạt động theo cùng thẻ.', 3), p) for p in PROFILES[:4]],
    ]


def listening(index):
    a, b, c = [PROFILES[(index + k) % 6] for k in range(3)]
    return [
        listen('Listen and choose the place.', a['place'], [field('Place:', a['place'], PLACES)]),
        listen('Listen and choose the activity.', b['activity'], [field('Activity:', b['activity'], CORE)], 2),
        listen('Listen. Where is the speaker going to visit this summer?', 'Where are you going to visit this summer? ' + destination(a), [field('Place:', a['place'], PLACES)]),
        listen('Listen. What is the speaker going to do this summer?', 'What are you going to do this summer? ' + activity(c), [field('Activity:', c['activity'], CORE)], 2),
        listen('Listen and find the destination and activity for this summer.', 'My name is ' + b['name'] + '. This summer, ' + destination(b) + ' ' + activity(b), [field('Place:', b['place'], PLACES), field('Activity:', b['activity'])], 3),
        listen('Listen. Write only Minh’s plans for this summer, not last summer.', 'My name is Minh. Last summer, I went camping. This summer, I am going to visit Phu Quoc Island. I am going to practise swimming.', [field('Place this summer:', PLACES[2]), field('Activity this summer:', CORE[3], alternatives=['practice swimming'])], 3),
    ]


def build_tests():
    import copy
    written = [warmup(), vocabulary(), dialogue(), reading(), writing()]
    mixed = [copy.deepcopy(written[i % 5][i]) for i in range(18)]
    return [assemble(qs, listening(i)) for i, qs in enumerate(written + [mixed])]
