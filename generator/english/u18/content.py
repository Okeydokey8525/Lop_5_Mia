"""Original transport and destination practice, volume two pages 52-57."""
from english.practice import mc, text as base_text, match, reorder, tf, based, picture as image, field, listen, assemble
CORE = ['by bus', 'by bicycle', 'by taxi', 'on foot']
MEANINGS = ['bằng xe buýt', 'bằng xe đạp', 'bằng taxi', 'đi bộ']
IMAGE_NAMES = dict(zip(CORE, ['bus', 'bicycle', 'taxi', 'on-foot']))
PLACES = ['Ha Noi Opera House', 'Dragon Bridge', 'Ngo Mon Square', 'Ho Chi Minh City Museum']
PROFILES = [dict(name=n, place=p, mode=m) for n, p, m in [('An', PLACES[0], CORE[0]), ('Linh', PLACES[1], CORE[1]), ('Minh', PLACES[2], CORE[2]), ('Hoa', PLACES[3], CORE[3]), ('Nam', PLACES[1], CORE[0]), ('Mai', PLACES[0], CORE[3])]]

def text(stem, answer, why, lesson=1, alternatives=()):
    accepted = list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short = answer.replace('cannot', "can't").replace('We will', "We'll")
        if short != answer:
            accepted.append(short)
    return base_text(stem, answer, why, lesson, accepted)

def picture(w, width=320):
    return image('u18', IMAGE_NAMES[w], MEANINGS[CORE.index(w)], width)

def visit(p):
    return 'I want to visit ' + p['place'] + '.'

def route(p):
    return 'You can get there ' + p['mode'] + '.'

def card(p):
    return f"Fictional English practice card: Traveller: {p['name']} · Destination: {p['place']} · Transport: {p['mode']}. Use this card, not a real route map."

def passage(p):
    return f"Hello! I am {p['name']}. I want to visit {p['place']}. I ask a friend how to get there. My friend says: You can get there {p['mode']}. I say: Thank you so much!"

def shown(q, p):
    return based(q, card(p))

def warmup():
    return [mc('Look at the picture. Choose the way to travel.', CORE, 'by bus', 'Xe buýt.', 1, picture('by bus')), text('Complete: Where do you want to ___?', 'visit', 'Want to visit.'), match(list(zip(CORE, MEANINGS)), 'By + phương tiện; on foot.'), shown(mc('Which destination is on the card?', PLACES, PLACES[0], 'Đọc Destination.'), PROFILES[0]), reorder('I want to visit Dragon Bridge.', 'Want to + visit.'), text('Complete: How ___ I get to Dragon Bridge?', 'can', 'How can I get to…?', 2), shown(text('Write only the transport phrase.', 'by bicycle', 'Theo thẻ Linh.', 2), PROFILES[1]), text('Complete: You can ___ there by taxi. Use get.', 'get', 'Can + nguyên mẫu.', 2), match([('museum', 'bảo tàng'), ('pagoda', 'chùa'), ('aquarium', 'thủy cung')], 'Từ chỉ nơi đến.'), reorder('You can get there on foot.', 'On foot, không by foot.', 2), shown(text('Write only the destination.', PLACES[2], 'Ngo Mon Square.', 2), PROFILES[2]), shown(tf([('Hoa wants to visit Ho Chi Minh City Museum.', True), ('Her card says by taxi.', False)], 'Theo đúng thẻ Hoa.', 2), PROFILES[3]), text('Complete: You can get there ___ bus.', 'by', 'By bus.', 2), shown(reorder(visit(PROFILES[1]), 'Đúng địa danh trên thẻ.', 2), PROFILES[1]), shown(text('Write a complete destination sentence starting with I want.', visit(PROFILES[2]), 'I want to visit + địa danh.', 3), PROFILES[2]), shown(text('Write a complete travel answer starting with You can.', route(PROFILES[3]), 'You can get there on foot.', 3), PROFILES[3]), mc('Choose the correct question.', ['How can I get to Dragon Bridge?', 'How can I gets to Dragon Bridge?', 'How I can get to Dragon Bridge?', 'How can I to get Dragon Bridge?'], 'How can I get to Dragon Bridge?', 'Can + I + get.', 3), shown(text('Write destination then travel answer. Start with I want and You can.', visit(PROFILES[0]) + ' ' + route(PROFILES[0]), 'Lấy đủ hai trường của cùng người.', 3), PROFILES[0])]

def vocabulary():
    return [*[mc('Look at the picture. Choose the way to travel.', CORE, k, 'Tranh: ' + MEANINGS[i], 1, picture(k)) for i, k in enumerate(CORE)], text('Complete: bi___. Write the whole vehicle word.', 'bicycle', 'Bicycle.'), match([('bridge', 'cầu'), ('square', 'quảng trường'), ('bus stop', 'điểm dừng xe buýt')], 'Từ trong Unit18.'), mc('Which phrase means đi bộ?', CORE, 'on foot', 'On foot.'), text('Complete: You can go by ___. Use tàu hỏa.', 'train', 'By train trong bài đọc.', 3), match([('boat', 'thuyền'), ('ferry', 'phà'), ('island', 'đảo')], 'Phương tiện và nơi đến trong phần đọc/luyện.', 3), reorder('I want to visit Ngo Mon Square.', 'Visit không có to sau nó.'), text('Complete: You can get there ___ foot.', 'on', 'On foot.', 2), text('Complete: I want to ___ the museum.', 'visit', 'Want to visit.', 2), shown(text('Write only the transport phrase.', 'by taxi', 'Theo thẻ Minh.', 2), PROFILES[2]), tf([('By bicycle names a way to travel.', True), ('On foot means by taxi.', False)], 'Phân biệt phương tiện.', 2), shown(text('Write only the destination.', PLACES[3], 'Giữ đủ tên nơi đến.', 3), PROFILES[3]), reorder('How can I get to the aquarium?', 'Get to + nơi đến.', 3), shown(text('Write the complete travel answer starting with You can.', route(PROFILES[4]), 'Cùng Dragon Bridge nhưng thẻ Nam đi bus.', 3), PROFILES[4]), text('Complete: Excuse me! I am ___. Use bị lạc.', 'lost', 'I am lost.', 3)]

def dialogue():
    return [mc('Choose the question asking about a destination.', ['Where do you want to visit?', 'What do you wear?', 'Who is the main character?', 'How did he run?'], 'Where do you want to visit?', 'Where hỏi nơi muốn đến.'), text('Complete: How ___ I get there?', 'can', 'Can I.', 2), reorder('You can get there by bus.', 'Can + get.', 2), shown(mc('Choose the transport phrase on the card.', CORE, 'by bicycle', 'Đọc thẻ Linh.', 2), PROFILES[1]), text('Rewrite in full: I can’t get there by bus.', 'I cannot get there by bus.', 'Can’t = cannot.'), text('Complete: I want ___ visit Dragon Bridge.', 'to', 'Want to + visit.'), shown(text('Give the destination sentence starting with I want.', visit(PROFILES[0]), 'Đọc thẻ An.'), PROFILES[0]), shown(mc('Where does Hoa want to visit?', PLACES, PLACES[3], 'Theo thẻ Hoa.'), PROFILES[3]), reorder('How can I get to Ngo Mon Square?', 'Get to + nơi đến.', 2), text('Rewrite in full: It’s far from here.', 'It is far from here.', 'It’s = It is.', 2), text('Complete: You can ___ there on foot. Use get.', 'get', 'Can + get.', 2), match([('Where do you want to visit?', 'I want to visit Dragon Bridge.'), ('How can I get there?', 'You can get there by bicycle.'), ('Thank you so much!', 'You are welcome.')], 'Ghép theo chức năng lời nói.', 2), shown(text('Write the complete travel answer starting with You can.', route(PROFILES[2]), 'Theo thẻ Minh.', 2), PROFILES[2]), tf([('Can I get is a correct question pattern.', True), ('Can I gets is correct.', False)], 'Sau can dùng get.', 3), shown(text('Write destination then travel answer, starting with I want and You can.', visit(PROFILES[3]) + ' ' + route(PROFILES[3]), 'On foot theo thẻ.', 3), PROFILES[3]), text('Rewrite in full: We’ll get there by train.', 'We will get there by train.', 'We’ll = We will.', 3), shown(text('Write the complete travel answer starting with You can.', route(PROFILES[5]), 'Cùng địa danh với An nhưng khác cách đi.', 3), PROFILES[5]), mc('Choose the correct sentence.', ['You can get there on foot.', 'You can gets there on foot.', 'You can to get there on foot.', 'You can get there by foot.'], 'You can get there on foot.', 'Can + get; on foot.', 3)]

def reading():
    qs = []
    for p in PROFILES[:4]:
        qs.extend((based(q, passage(p)) for q in [text('Who is speaking? Write the name only.', p['name'], 'Tên người nói.', 3), mc('Which destination is named?', PLACES, p['place'], 'Đọc I want to visit…', 3), text('Write only the transport phrase.', p['mode'], 'You can get there…', 3), tf([(f"The way to travel is {p['mode']}.", True), (f"The way to travel is {CORE[(CORE.index(p['mode']) + 1) % 4]}.", False)], 'Theo đoạn, không đoán đường đi thật.', 3)]))
    qs += [based(text('Both want to visit Dragon Bridge. Who travels by bus? Write the name only.', 'Nam', 'Linh và Nam có cùng nơi đến nhưng khác phương tiện.', 3), '\n'.join((card(p) for p in [PROFILES[1], PROFILES[4]]))), based(text('Which transport takes the group to the island? Write the vehicle word only.', 'ferry', 'Chặng cuối đi ferry, không phải bus.', 3), 'An original fictional morning plan: First, we visit the museum by bus. Next, we walk to the lake. Finally, we go to the island by ferry. We stay together with an adult.')]
    return qs

def writing():
    return [text('Complete: I want ___ visit the museum.', 'to', 'Want to visit.'), reorder('You can get there by taxi.', 'Can + get.'), text('Complete: How can I ___ there?', 'get', 'Can + get.'), text('Complete: You can go ___ foot.', 'on', 'On foot.', 2), mc('Choose the correct destination sentence.', ['I want to visit Dragon Bridge.', 'I want visit Dragon Bridge.', 'I want to visit to Dragon Bridge.', 'I wants to visit Dragon Bridge.'], 'I want to visit Dragon Bridge.', 'Want to visit + nơi đến.', 2), text('Complete: Where do you want to ___?', 'visit', 'Visit.'), match(list(zip(CORE, MEANINGS)), 'Giới từ đúng với cách đi.'), reorder('How can I get to the museum?', 'Get to + museum.', 2), text('Rewrite in full: I can’t get there on foot.', 'I cannot get there on foot.', 'Cannot.', 2), text('Complete: You can get there ___ bicycle.', 'by', 'By bicycle.', 2), shown(reorder(route(PROFILES[3]), 'On foot.', 2), PROFILES[3]), reorder('Is it far from here?', 'Câu hỏi Yes/No lên giọng.', 2), text('Complete: Thank you so ___.', 'much', 'Thank you so much.'), text('Rewrite in full: It’s not far from here.', 'It is not far from here.', 'It is not.', 2), *[shown(text('Write destination then travel answer. Start with I want and You can.', visit(p) + ' ' + route(p), 'Giữ đúng nơi và phương tiện trên thẻ.', 3), p) for p in PROFILES[:4]]]

def listening(index):
    a, b, c = [PROFILES[(index + k) % 6] for k in range(3)]
    return [listen('Listen and choose the transport phrase.', route(a), [field('Transport:', a['mode'], CORE)], 2), listen('Listen and choose the destination.', visit(b), [field('Destination:', b['place'], PLACES)]), listen('Listen. Which transport phrase is used?', visit(a) + ' ' + route(a), [field('Transport:', a['mode'], CORE)], 2), listen('Listen. Which destination is named?', visit(c) + ' ' + route(c), [field('Destination:', c['place'], PLACES)], 2), listen('Listen and find both destination and transport.', visit(b) + ' ' + route(b), [field('Destination:', b['place'], PLACES), field('Transport:', b['mode'], CORE)], 3), listen('Listen. Write only Nam’s destination and transport, not Linh’s.', 'Linh says: I want to visit Dragon Bridge. I can get there by bicycle. Nam says: I want to visit Dragon Bridge. I can get there by bus.', [field('Nam’s destination:', 'Dragon Bridge'), field('Nam’s transport:', 'by bus')], 3)]

def build_tests():
    import copy
    written = [warmup(), vocabulary(), dialogue(), reading(), writing()]
    mixed = [copy.deepcopy(written[i % 5][i]) for i in range(18)]
    return [assemble(qs, listening(i)) for i, qs in enumerate(written + [mixed])]
