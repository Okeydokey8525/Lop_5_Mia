"""Original place descriptions and distances, volume two printed pages 58-63."""
from english.practice import mc, text as base_text, match, reorder, tf, based, picture as image, field, listen, assemble

CORE = ['waterfall', 'lake', 'cave', 'old town']
MEANINGS = ['thác nước', 'hồ', 'hang động', 'phố cổ']
PLACES = ['Ban Gioc Waterfall', 'Hoi An Old Town', 'Sydney Opera House', 'Petronas Twin Towers']
OPINIONS = ['peaceful', 'exciting', 'beautiful', 'fantastic']
PROFILES = [dict(name=n, place=p, opinion=o, distance=k, plural=plural) for n, p, o, k, plural in [
    ('An', PLACES[0], 'peaceful', 'four', False),
    ('Linh', PLACES[1], 'exciting', 'seven', False),
    ('Minh', PLACES[2], 'beautiful', 'nine', False),
    ('Hoa', PLACES[3], 'fantastic', 'twelve', True),
    ('Nam', PLACES[1], 'peaceful', 'six', False),
    ('Mai', PLACES[0], 'beautiful', 'eight', False),
]]


def text(stem, answer, why, lesson=1, alternatives=()):
    accepted = list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short = answer.replace('I think it is', "I think it's").replace('I think they are', "I think they're").replace('They are', "They're")
        if short != answer:
            accepted.append(short)
    return base_text(stem, answer, why, lesson, accepted)


def picture(w, width=320):
    return image('u19', w.replace(' ', '-'), MEANINGS[CORE.index(w)], width)


def opinion(p):
    return 'I think ' + ('they are ' if p['plural'] else 'it is ') + p['opinion'] + '.'


def distance(p):
    return 'It is about ' + p['distance'] + ' kilometres.'


def card(p):
    return f"Imaginary English practice card, not real geography: Speaker: {p['name']} · Place: {p['place']} · Speaker's opinion: {p['opinion']} · Distance from this speaker's imaginary school to the place: about {p['distance']} kilometres."


def passage(p):
    return f"An imaginary holiday plan for English practice: My name is {p['name']}. I want to visit {p['place']}. {opinion(p)} It is about {p['distance']} kilometres from my imaginary school. I can get there by bus. I want to take photos there. These distances are made up for this exercise."


def shown(q, p):
    return based(q, card(p))


def warmup():
    return [
        mc('Look at the picture. Choose the type of place.', CORE, 'waterfall', 'Nước đổ từ trên cao: thác nước.', 1, picture('waterfall')),
        text('Complete: What do you think ___ Hoi An Old Town?', 'of', 'Think of + nơi chốn.'),
        match(list(zip(OPINIONS, ['yên bình', 'thú vị, sôi động', 'đẹp', 'tuyệt vời'])), 'Từ nêu cảm nhận.'),
        shown(mc('Which opinion does An give?', OPINIONS, 'peaceful', 'Theo ý kiến của An, không đoán từ ảnh.'), PROFILES[0]),
        reorder('What do you think of Ban Gioc Waterfall?', 'What do you think of…?'),
        text('Complete: How ___ is it from here to the lake?', 'far', 'How far hỏi khoảng cách.', 2),
        shown(text('Write the distance phrase only, using words: ___ kilometres.', 'seven kilometres', 'Theo thẻ Linh.', 2, ['7 kilometres', '7 km']), PROFILES[1]),
        text('Complete: It is ___ four kilometres.', 'about', 'About: khoảng.', 2),
        match(list(zip(CORE, MEANINGS)), 'Loại địa điểm, không phải tên riêng.'),
        reorder('How far is it from here to the lake?', 'From nơi đi to nơi đến.', 2),
        shown(text('Complete the answer: I think it is ___.', 'beautiful', 'Theo ý kiến Minh.', 2), PROFILES[2]),
        shown(tf([('Hoa thinks Petronas Twin Towers are fantastic.', True), ('Hoa gives the opinion peaceful.', False)], 'Đọc đúng người và cảm nhận.', 2), PROFILES[3]),
        text('Complete: I think they ___ fantastic.', 'are', 'They are, không they is.'),
        shown(reorder(opinion(PROFILES[1]), 'It chỉ một địa điểm.'), PROFILES[1]),
        shown(text('Write the opinion sentence in full form, starting with I think.', opinion(PROFILES[3]), 'Twin Towers dùng they are.', 3), PROFILES[3]),
        shown(text('Write the distance answer in words and full form, starting with It is.', distance(PROFILES[0]), 'It is about four kilometres.', 3), PROFILES[0]),
        mc('Choose the correct distance question.', ['How far is it from the school to the lake?', 'How far it is from the school to the lake?', 'How far are it from the school to the lake?', 'How far is it to the school from?'], 'How far is it from the school to the lake?', 'How far is it from…to…?', 3),
        shown(text('Write opinion then distance, in words and full form. Start with I think and It is.', opinion(PROFILES[1]) + ' ' + distance(PROFILES[1]), 'Lấy đủ hai thông tin của cùng người.', 3), PROFILES[1]),
    ]


def vocabulary():
    return [
        *[mc('Look at the picture. Choose the type of place.', CORE, k, 'Tranh: ' + MEANINGS[i], 1, picture(k)) for i, k in enumerate(CORE)],
        text('Complete: peace___. Write the whole word meaning yên bình.', 'peaceful', 'Peaceful.'),
        match([('beautiful', 'đẹp'), ('exciting', 'thú vị, sôi động'), ('fantastic', 'tuyệt vời')], 'Cảm nhận có thể khác nhau giữa hai người.'),
        mc('Which word means khoảng?', ['about', 'from', 'near', 'far'], 'about', 'About + số chỉ khoảng cách.', 2),
        text('Complete: It is about one ___. Use the singular distance unit.', 'kilometre', 'One kilometre, không one kilometres.', 2),
        match([('near', 'gần'), ('far', 'xa'), ('a hundred', 'một trăm')], 'Từ và số trong bài khoảng cách.', 2),
        reorder('I think it is peaceful.', 'Think + it is + tính từ.'),
        text('Complete: It is about four ___. Use the plural of kilometre.', 'kilometres', 'Số lớn hơn một dùng kilometres.', 2),
        text('Complete: How far is it ___ our school to the park?', 'from', 'From…to…', 2),
        shown(text('Write the speaker’s opinion word only.', 'fantastic', 'Hoa nghĩ fantastic.', 2), PROFILES[3]),
        tf([('What do you think of asks for an opinion.', True), ('How far asks for a favourite food.', False)], 'Phân biệt cảm nhận và khoảng cách.', 2),
        shown(text('Write the opinion in full form, starting with I think.', opinion(PROFILES[4]), 'Nam và Linh cùng nơi nhưng khác ý kiến.', 3), PROFILES[4]),
        reorder('How far is it from here to the old town?', 'Giữ đúng hai đầu from/to.', 3),
        shown(text('Write the distance answer in words and full form, starting with It is.', distance(PROFILES[5]), 'Mai và An cùng nơi nhưng khác điểm xuất phát giả định.', 3), PROFILES[5]),
        text('Complete in full form: Petronas Twin Towers are fantastic. I think ___ fantastic.', 'they are', 'Danh từ số nhiều → they are.', 3),
    ]


def dialogue():
    return [
        mc('Choose the question asking for an opinion.', ['What do you think of Hoi An Old Town?', 'How far is it from here?', 'How can I get there?', 'When did you go there?'], 'What do you think of Hoi An Old Town?', 'What do you think of…?'),
        text('Complete: How ___ is it from here to the museum?', 'far', 'How far.', 2),
        reorder('It is about twelve kilometres.', 'About + khoảng cách.', 2),
        shown(mc('Choose Linh’s opinion.', OPINIONS, 'exciting', 'Theo Linh.'), PROFILES[1]),
        text('Rewrite in full: They’re fantastic.', 'They are fantastic.', 'They’re = They are.'),
        text('Complete: What ___ you think of the lake?', 'do', 'What do you think…?'),
        shown(text('Give the opinion in full form, starting with I think.', opinion(PROFILES[0]), 'Dùng ý kiến An.'), PROFILES[0]),
        shown(mc('Which place does Hoa describe?', PLACES, PLACES[3], 'Theo thẻ Hoa.'), PROFILES[3]),
        reorder('How far is it from here to Hoi An Old Town?', 'Is it, from…to…', 2),
        text('Rewrite in full: It’s about nine kilometres.', 'It is about nine kilometres.', 'It’s = It is.', 2),
        text('Complete: I think Petronas Twin Towers ___ beautiful.', 'are', 'Towers là số nhiều.', 2),
        match([('What do you think of the lake?', 'I think it is peaceful.'), ('How far is it from here to the lake?', 'It is about four kilometres.'), ('How can I get there?', 'You can get there by bus.')], 'Ghép đúng loại thông tin hỏi.', 2),
        shown(text('Write the distance answer in words and full form, starting with It is.', distance(PROFILES[2]), 'Dữ kiện giả định Minh.', 2), PROFILES[2]),
        tf([('How far is it is the correct word order.', True), ('How far it is is the correct direct question order.', False)], 'Câu hỏi trực tiếp đảo is it.', 3),
        shown(text('Write opinion then distance, in words and full form. Start with I think and It is.', opinion(PROFILES[3]) + ' ' + distance(PROFILES[3]), 'They are cho Twin Towers.', 3), PROFILES[3]),
        text('Rewrite in full: I think it’s beautiful.', 'I think it is beautiful.', 'It’s = it is.', 3),
        shown(text('Write Nam’s opinion in full form, starting with I think.', opinion(PROFILES[4]), 'Không lấy ý kiến Linh.', 3), PROFILES[4]),
        mc('Choose the correct sentence.', ['I think they are fantastic.', 'I think they is fantastic.', 'I think it are fantastic.', 'I thinks they are fantastic.'], 'I think they are fantastic.', 'I think; they are.', 3),
    ]


def reading():
    qs = []
    for p in PROFILES[:4]:
        qs.extend(based(q, passage(p)) for q in [
            text('Who is speaking? Write the name only.', p['name'], 'Tên trong đoạn.', 3),
            mc('Which opinion is given?', OPINIONS, p['opinion'], 'Đọc I think…', 3),
            text('How far is it from the speaker’s imaginary school? Write the distance phrase only.', p['distance'] + ' kilometres', 'Lấy khoảng cách trong đoạn, không tra bản đồ thật.', 3),
            tf([('The speaker can get there by bus.', True), ('The speaker wants to buy a new bicycle there.', False)], 'Chỉ chọn thông tin đã nêu.', 3),
        ])
    qs += [
        based(text('Both describe Hoi An Old Town. Who thinks it is peaceful? Write the name only.', 'Nam', 'Hai người có thể nêu ý kiến khác nhau.', 3), '\n'.join(card(p) for p in [PROFILES[1], PROFILES[4]])),
        based(text('Along this route, how far is it from the school to the lake via the museum? Write the total distance phrase in words.', 'seven kilometres', 'Cộng hai chặng cùng tuyến: 3 + 4 = 7, không phải khoảng cách đường chim bay.', 3, ['7 kilometres', '7 km']), 'Imaginary route for English practice: school → museum → lake. Along this route, school to museum is about three kilometres, and museum to lake is about four kilometres. There is no extra leg. Add these two legs to find the distance along this route.'),
    ]
    return qs


def writing():
    return [
        text('Complete: What do you think ___ the cave?', 'of', 'Think of.'),
        reorder('I think it is beautiful.', 'I think + it is.'),
        text('Complete: How far ___ it from here to the park?', 'is', 'How far is it…?', 2),
        text('Complete: It is ___ six kilometres.', 'about', 'About: khoảng.', 2),
        mc('Choose the correct question.', ['What do you think of Hoi An Old Town?', 'What does you think of Hoi An Old Town?', 'What do you thinks of Hoi An Old Town?', 'What you think of Hoi An Old Town?'], 'What do you think of Hoi An Old Town?', 'Do you think, không thinks.'),
        text('Complete: I think Petronas Twin Towers ___ fantastic.', 'are', 'Towers số nhiều.'),
        match(list(zip(OPINIONS, ['yên bình', 'thú vị, sôi động', 'đẹp', 'tuyệt vời'])), 'Dùng tính từ phù hợp dữ kiện.'),
        reorder('How far is it from the school to the museum?', 'Câu hỏi khoảng cách.', 2),
        text('Rewrite in full: It’s about four kilometres.', 'It is about four kilometres.', 'It is.', 2),
        text('Complete: How far is it from here ___ the lake?', 'to', 'From…to…', 2),
        shown(reorder(opinion(PROFILES[3]), 'Số nhiều: they are.', 2), PROFILES[3]),
        reorder('What do you think of the old town?', 'Câu hỏi Wh thường xuống giọng.', 3),
        text('Complete: It is about one ___. Use the singular of kilometres.', 'kilometre', 'One kilometre.', 2),
        text('Rewrite in full: They’re beautiful.', 'They are beautiful.', 'They are.', 2),
        *[shown(text('Write opinion then distance, in words and full form. Start with I think and It is.', opinion(p) + ' ' + distance(p), 'Dùng cùng thẻ; đúng it/they và số kilometre.', 3), p) for p in PROFILES[:4]],
    ]


def listening(index):
    a, b, c = [PROFILES[(index + k) % 6] for k in range(3)]
    return [
        listen('Listen and choose the opinion.', opinion(a), [field('Opinion:', a['opinion'], OPINIONS)]),
        listen('Listen and choose the distance phrase.', distance(b), [field('Distance:', b['distance'] + ' kilometres', ['four kilometres', 'seven kilometres', 'nine kilometres', 'twelve kilometres', 'six kilometres', 'eight kilometres'])], 2),
        listen('Listen. Which opinion is given?', 'What do you think of ' + a['place'] + '? ' + opinion(a), [field('Opinion:', a['opinion'], OPINIONS)]),
        listen('Listen. How far is it from the imaginary school to the place?', 'How far is it from my imaginary school to ' + c['place'] + '? ' + distance(c), [field('Distance:', c['distance'] + ' kilometres', ['four kilometres', 'seven kilometres', 'nine kilometres', 'twelve kilometres', 'six kilometres', 'eight kilometres'])], 2),
        listen('Listen and find both the opinion and distance in this imaginary plan.', b['place'] + '. ' + opinion(b) + ' ' + distance(b), [field('Opinion:', b['opinion'], OPINIONS), field('Distance:', b['distance'] + ' kilometres')], 3),
        listen('Listen. Write only Nam’s opinion and distance, not Linh’s.', 'These distances are imaginary. Linh says: Hoi An Old Town is exciting. It is about seven kilometres from my school. Nam says: Hoi An Old Town is peaceful. It is about six kilometres from my school.', [field('Nam’s opinion:', 'peaceful'), field('Nam’s distance:', 'six kilometres', alternatives=['6 kilometres', '6 km'])], 3),
    ]


def build_tests():
    import copy
    written = [warmup(), vocabulary(), dialogue(), reading(), writing()]
    mixed = [copy.deepcopy(written[i % 5][i]) for i in range(18)]
    return [assemble(qs, listening(i)) for i, qs in enumerate(written + [mixed])]
