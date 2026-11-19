"""Original weather and clothing exercises; volume two, pages 40-45."""
from english.practice import mc, text, match, reorder, tf, based, picture as image, field, listen, assemble
CORE = ['a blouse', 'trousers', 'jeans', 'a jumper']
IMAGE_NAMES = dict(zip(CORE, ['blouse', 'trousers', 'jeans', 'jumper']))
MEANINGS = ['áo kiểu', 'quần dài', 'quần bò', 'áo len chui đầu']
SEASONS = ['spring', 'summer', 'autumn', 'winter']
WEATHER = ['warm and rainy', 'hot and sunny', 'cool and cloudy', 'cold and dry']
PROFILES = [dict(name=n, place=p, season=s, weather=w, clothes=c) for n, p, s, w, c in [('An', 'Ha Noi', 'spring', 'warm and rainy', 'a blouse'), ('Linh', 'Ha Noi', 'summer', 'hot and sunny', 'trousers'), ('Minh', 'Tokyo', 'autumn', 'cool and cloudy', 'jeans'), ('Hoa', 'London', 'winter', 'cold and dry', 'a jumper'), ('Nam', 'Ha Noi', 'winter', 'cold and dry', 'jeans'), ('Mai', 'Tokyo', 'spring', 'warm and rainy', 'a jumper')]]

def picture(w, width=320):
    return image('u16', IMAGE_NAMES[w], MEANINGS[CORE.index(w)], width)

def weather(p):
    return 'It is ' + p['weather'] + '.'

def outfit(p):
    return 'I wear ' + p['clothes'] + '.'

def card(p):
    return f"Fictional practice card: {p['name']} · Place: {p['place']} · Season: {p['season']} · Weather: {p['weather']} · Usual clothes: {p['clothes']}. These are the conditions and choice on this card, not a forecast or a rule for everyone."

def passage(p):
    return f"My name is {p['name']}. I am in {p['place']}. It is {p['season']} here. The weather is {p['weather']}. I usually wear {p['clothes']}. I like this season."

def shown(q, p):
    return based(q, card(p))

def warmup():
    return [mc('Look at the picture. Choose the clothes.', CORE, 'a blouse', 'Áo kiểu.', 1, picture('a blouse')), text('Complete: How is the ___ in Ha Noi?', 'weather', 'How is the weather?'), match(list(zip(SEASONS, ['mùa xuân', 'mùa hè', 'mùa thu', 'mùa đông'])), 'Ghép bốn mùa.'), shown(mc('What season is on the card?', SEASONS, 'spring', 'Đọc Season.'), PROFILES[0]), reorder('It is hot and sunny.', 'It is + tính từ.'), text('Complete: I ___ jeans. Use wear.', 'wear', 'I wear.'), shown(text('Write the weather only.', 'hot and sunny', 'Đọc Weather.'), PROFILES[1]), text('Complete: What do you usually ___ in winter?', 'wear', 'Do + wear.', 2), match([('rainy', 'có mưa'), ('cloudy', 'có mây'), ('dry', 'khô')], 'Từ chỉ thời tiết.'), reorder('I wear a jumper in winter.', 'In + mùa.', 2), shown(text('Write only the usual clothes.', 'jeans', 'Theo thẻ Minh.', 2), PROFILES[2]), shown(tf([('The place is London.', True), ('The season is summer.', False)], 'Đọc thẻ, không đoán từ thành phố.', 2), PROFILES[3]), text('Complete: It ___ cool and cloudy.', 'is', 'It is.'), shown(reorder(outfit(PROFILES[0]), 'I wear a blouse.', 2), PROFILES[0]), shown(text('Write a weather sentence in full form starting with It.', weather(PROFILES[3]), 'It is cold and dry.', 3), PROFILES[3]), shown(text('Write a clothes sentence starting with I wear.', outfit(PROFILES[2]), 'I wear jeans.', 3), PROFILES[2]), mc('Choose the correct question.', ['What do you usually wear in autumn?', 'What do you usually wears in autumn?', 'What you usually wear in autumn?', 'What do usually you wear in autumn?'], 'What do you usually wear in autumn?', 'Do + you + wear.', 3), shown(text('Write weather, then clothes. Start with It and I.', weather(PROFILES[0]) + ' ' + outfit(PROFILES[0]), 'Lấy cả hai trường trên thẻ.', 3), PROFILES[0])]

def vocabulary():
    return [*[mc('Look at the picture. Choose the clothes.', CORE, k, 'Tranh: ' + MEANINGS[i], 1, picture(k)) for i, k in enumerate(CORE)], match(list(zip(SEASONS, ['mùa xuân', 'mùa hè', 'mùa thu', 'mùa đông'])), 'Bốn mùa.'), text('Complete: win___. Write the whole season.', 'winter', 'Winter.'), mc('Which word means ẩm?', ['humid', 'dry', 'snowy', 'windy'], 'humid', 'Humid.'), text('Complete: sun___. Write the whole weather word.', 'sunny', 'Sunny.'), match([('dry season', 'mùa khô'), ('rainy season', 'mùa mưa'), ('snowy', 'có tuyết')], 'Hai mùa trong phần đọc, không suy rằng mọi nơi đều có bốn mùa.', 3), reorder('It is warm in spring.', 'In spring.'), text('Complete: I wear a ___ in winter. Use áo len chui đầu.', 'jumper', 'A jumper.', 2), text('Complete: I wear ___. Use quần bò.', 'jeans', 'Jeans dạng số nhiều.', 2), tf([('A blouse is a kind of clothing.', True), ('Humid means dry.', False)], 'Phân biệt loại từ.', 2), shown(text('Write only the weather phrase.', PROFILES[2]['weather'], 'Cool and cloudy.', 2), PROFILES[2]), based(text('How many seasons does this note name? Write one number.', '2', 'Dry và rainy là hai mùa.', 3), 'This note describes two seasons in the south of Viet Nam: the dry season and the rainy season.'), reorder('I wear trousers in summer.', 'Không thêm a trước trousers.', 3), text('Complete: How is the weather ___ winter?', 'in', 'In + mùa.', 3), shown(text('Write the clothes sentence starting with I.', outfit(PROFILES[3]), 'I wear a jumper.', 3), PROFILES[3])]

def dialogue():
    return [mc('Choose the weather question.', ['How is the weather in Ha Noi?', 'What do you wear?', 'Who is she?', 'Where is my book?'], 'How is the weather in Ha Noi?', 'Hỏi thời tiết.'), text('Complete: How ___ the weather in spring?', 'is', 'How is.'), reorder('What do you usually wear in winter?', 'Do + wear.', 2), shown(mc('Choose the weather answer.', [weather(p) for p in PROFILES[:4]], weather(PROFILES[1]), 'Theo thẻ.', 2), PROFILES[1]), text('Rewrite in full: It’s cold and dry.', 'It is cold and dry.', 'It’s = It is.'), text('Complete: What ___ you usually wear?', 'do', 'Do you.'), shown(text('Answer the clothes question. Start with I.', outfit(PROFILES[0]), 'I wear a blouse.'), PROFILES[0]), shown(mc('Which clothes are on the card?', CORE, 'a jumper', 'Theo thẻ Hoa.'), PROFILES[3]), reorder('How is the weather in autumn?', 'In autumn.', 2), text('Rewrite in full: It’s hot and sunny.', 'It is hot and sunny.', 'Full form giữ is.', 2), text('Complete: I ___ a blouse. Use wear.', 'wear', 'I wear.', 2), match([('How is the weather?', 'It is cool and cloudy.'), ('What do you wear?', 'I wear jeans.'), ('What season is it?', 'It is autumn.')], 'Ghép đúng câu hỏi.', 2), shown(text('Give a weather sentence in full form.', weather(PROFILES[2]), 'It is cool and cloudy.', 2), PROFILES[2]), tf([('Do you wear is a correct question pattern.', True), ('Do you wears is correct.', False)], 'Do + nguyên mẫu.', 3), shown(text('Write weather then clothes, in full form.', weather(PROFILES[1]) + ' ' + outfit(PROFILES[1]), 'Hai câu theo thẻ.', 3), PROFILES[1]), reorder('I usually wear jeans in autumn.', 'Usually trước wear.', 3), shown(text('Write one clothes sentence starting with I.', outfit(PROFILES[4]), 'Không mặc định winter chỉ có jumper.', 3), PROFILES[4]), text('Complete: It is cold ___ dry.', 'and', 'And nối hai tính từ.', 3)]

def reading():
    qs = []
    for p in PROFILES[:4]:
        qs.extend((based(q, passage(p)) for q in [text('Who is speaking? Write the name only.', p['name'], 'Tên người kể.', 3), mc('Which season is named?', SEASONS, p['season'], 'Đọc It is…here.', 3), text('Write only the usual clothes.', p['clothes'], 'I usually wear…', 3), tf([(f"The weather is {p['weather']}.", True), (f"The speaker wears {CORE[(CORE.index(p['clothes']) + 1) % 4]}.", False)], 'Đối chiếu bài đọc.', 3)]))
    qs += [based(text('Both cards say winter. Who wears jeans? Write the name only.', 'Nam', 'Cùng mùa, khác lựa chọn trang phục.', 3), '\n'.join((card(p) for p in [PROFILES[3], PROFILES[4]]))), based(text('Name the two seasons in the order given. Use and between them.', 'the dry season and the rainy season', 'Theo thứ tự trong ghi chú.', 3), 'In this note about the south of Viet Nam, the two seasons are the dry season and the rainy season.')]
    return qs

def writing():
    return [text('Complete: It ___ hot.', 'is', 'It is.'), reorder('I wear jeans.', 'I wear.'), text('Complete: What do you usually ___?', 'wear', 'Do + wear.'), text('Complete: It is warm ___ rainy.', 'and', 'And.', 2), mc('Choose the correct sentence.', ['I wear trousers.', 'I wears trousers.', 'I wear a trousers.', 'I wearing trousers.'], 'I wear trousers.', 'I wear; trousers số nhiều.', 2), text('Complete: How is the ___?', 'weather', 'Weather.'), match([('spring', 'warm'), ('summer', 'hot'), ('winter', 'cold')], 'Cặp từ của Lesson 1, không dùng như dự báo thật.'), reorder('It is cool in autumn.', 'In autumn.', 2), text('Rewrite in full: It’s warm and rainy.', 'It is warm and rainy.', 'It’s = It is.', 2), text('Complete: I wear a ___. Use áo kiểu.', 'blouse', 'A blouse.', 2), shown(reorder(outfit(PROFILES[3]), 'I wear a jumper.', 2), PROFILES[3]), reorder('What do you wear in spring?', 'Do you wear.', 2), text('Complete: I wear ___ in autumn. Use quần bò.', 'jeans', 'Jeans.'), text('Rewrite in full: It’s cool and cloudy.', 'It is cool and cloudy.', 'Giữ is.', 2), *[shown(text('Write weather then clothes. Start with It and I, in full form.', weather(p) + ' ' + outfit(p), 'Hai thông tin đúng thẻ.', 3), p) for p in PROFILES[:4]]]

def listening(index):
    a, b, c = [PROFILES[(index + k) % 6] for k in range(3)]
    return [listen('Listen and choose the season.', 'It is ' + a['season'] + '.', [field('Season:', a['season'], SEASONS)]), listen('Listen and choose the clothes.', outfit(b), [field('Clothes:', b['clothes'], CORE)], 2), listen('Listen and choose the weather.', f"It is {a['season']}. " + weather(a), [field('Weather:', a['weather'], WEATHER)], 2), listen('Listen and choose the season.', f"In {c['season']}, I usually wear {c['clothes']}.", [field('Season:', c['season'], SEASONS)], 2), listen('Listen. Find both season and clothes.', f"It is {b['season']}. " + outfit(b), [field('Season:', b['season'], SEASONS), field('Clothes:', b['clothes'], CORE)], 3), listen('Listen. Write only Nam’s season and clothes, not Hoa’s.', 'Hoa says: It is winter. I wear a jumper. Nam says: It is winter. I wear jeans.', [field('Nam’s season:', 'winter'), field('Nam’s clothes:', 'jeans')], 3)]

def build_tests():
    import copy
    written = [warmup(), vocabulary(), dialogue(), reading(), writing()]
    mixed = [copy.deepcopy(written[i % 5][i]) for i in range(18)]
    return [assemble(qs, listening(i)) for i, qs in enumerate(written + [mixed])]
