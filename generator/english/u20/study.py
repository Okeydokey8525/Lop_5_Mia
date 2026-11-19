"""Summer plans: words, dialogues and independent saved practice."""
from english.u20.content import CORE, MEANINGS, PLACES, picture
from english.study.author import word as w, question as q, choice as c, dialogue as d
from english.study.render import render_study as render


def data():
    words = [w('activities', k, v, 'I am going to ' + k + '.', image=k) for k, v in zip(CORE, MEANINGS)]
    words += [w('activities', k, v, e) for k, v, e in [
        ('grow vegetables', 'trồng rau', 'We are going to grow vegetables on an eco-farm.'),
        ('learn a new language', 'học một ngôn ngữ mới', 'I am going to learn a new language with my friends.'),
    ]]
    words += [w('places', k, v, e) for k, v, e in [
        ('river', 'sông', 'I am going to visit the river.'),
        ('cave', 'hang động', 'We are going to visit a cave.'),
        ('island', 'đảo', 'They are going to visit an island.'),
        ('aquarium', 'thủy cung', 'She is going to visit an aquarium.'),
        (PLACES[0], 'sông Hương', 'I am going to visit Huong River.'),
        (PLACES[1], 'động Phong Nha', 'We are going to visit Phong Nha Cave.'),
        (PLACES[2], 'đảo Phú Quốc', 'He is going to visit Phu Quoc Island.'),
        (PLACES[3], 'thủy cung Đầm Sen', 'They are going to visit Dam Sen Aquarium.'),
    ]]
    words += [w('plans', k, v, e) for k, v, e in [
        ('summer holidays', 'kỳ nghỉ hè', 'Our summer holidays start next week.'),
        ('plan', 'kế hoạch', 'This is my summer plan.'),
        ('this summer', 'mùa hè này', 'I am going to go camping this summer.'),
        ('last summer', 'mùa hè năm ngoái', 'Last summer, I grew vegetables.'),
        ('next week', 'tuần tới', 'We are going to visit the aquarium next week.'),
        ('learn', 'học', 'I am going to learn to play the guitar.'),
    ]]
    dialogs = [
        d('activities', 'Hoạt động mùa hè', 'What are you going to do this summer?', 'I am going to join a music club.', 'What…do hỏi hoạt động; am going to + nguyên mẫu join.'),
        d('activities', 'Luyện bơi', 'What is Hoa going to do this summer?', 'She is going to practise swimming.', 'She is; practise + swimming. Đây là mẫu luyện Anh, không phải hướng dẫn tự tập bơi.'),
        d('places', 'Nơi sẽ tham quan', 'Where are you going to visit this summer?', 'I am going to visit Huong River.', 'Where hỏi nơi. Visit + địa điểm, không visit to.'),
        d('places', 'Đi cùng nhau', 'Where are they going to visit this summer?', 'They are going to visit Phong Nha Cave.', 'They are going to visit; giữ đúng tên riêng.'),
        d('plans', 'Năm ngoái và năm nay', 'What did you do last summer?', 'I went camping. This summer, I am going to visit an eco-farm.', 'Last summer: đã qua → went; this summer: dự định → am going to visit.'),
        d('plans', 'Kế hoạch của chúng mình', 'What are we going to do this summer?', 'We are going to learn a new language.', 'We are going to. Câu hỏi Wh thường xuống giọng; ABC là tên chữ cái, không phải phonics.'),
    ]
    exercises = [
        c('activity-listen', 'activities', 'Which summer activity is heard?', CORE[1], 'Nghe go camping.', CORE, speech='I am going to go camping this summer.'),
        q('activity-base', 'activities', 'She is going to ___ a music club. Use join, joins or joined.', 'join', 'Going to + nguyên mẫu join.'),
        q('activity-swim', 'activities', 'I am going to practise ___. Use swim with -ing.', 'swimming', 'Swim → swimming, gấp đôi m.'),
        q('activity-an', 'activities', 'I am going to visit ___ eco-farm. Use a or an.', 'an', 'An eco-farm.'),
        c('place-listen', 'places', 'Where is Nam going to visit?', PLACES[1], 'Lấy nơi của Nam, không nơi của Mai.', PLACES, speech='Mai is going to visit Huong River. Nam is going to visit Phong Nha Cave.'),
        q('place-where', 'places', '___ are you going to visit this summer? Ask about a place.', 'Where', 'Where hỏi nơi; What…do hỏi hoạt động.'),
        q('place-full', 'places', 'Rewrite in full: I’m going to visit Huong River.', 'I am going to visit Huong River.', 'I’m = I am.'),
        q('place-base', 'places', 'We are going to ___ an aquarium. Use visit, visits or visiting.', 'visit', 'Going to + visit, không visiting.'),
        c('plan-listen', 'plans', 'What is Minh going to do this summer?', CORE[3], 'Lấy this summer, không last summer.', CORE, speech='Last summer, Minh went camping. This summer, he is going to practise swimming.'),
        q('plan-am', 'plans', 'I ___ going to learn a new language.', 'am', 'I am going to.'),
        q('plan-are', 'plans', 'They ___ going to go camping.', 'are', 'They are going to.'),
        q('plan-past', 'plans', 'Card: Last summer: went camping. This summer: practise swimming. Write the past activity phrase only.', 'went camping', 'Last summer là mùa hè năm ngoái, không phải dự định mới.'),
    ]
    return dict(unit=20, key='mia5:learn:en-u20-v1', intro='Lên kế hoạch nghỉ hè: nơi sẽ tham quan, việc sẽ làm, nghe thường/chậm, ABC và bài luyện tự lưu.', groups=[
        dict(id='activities', name='Mùa hè em làm gì?', tip='What are you going to do this summer? I am going to… Dùng động từ nguyên mẫu sau going to: join, go, visit, practise. Tranh minh họa hoạt động; không đoán dự định của một người chỉ từ tranh.'),
        dict(id='places', name='Em sẽ tham quan đâu?', tip='Where are you going to visit this summer? I am going to visit… Visit + địa điểm. Tên riêng lấy từ Lesson 1, trang 64–65.'),
        dict(id='plans', name='Kể kế hoạch của em', tip='I am / he, she is / we, they are going to + nguyên mẫu. Phân biệt last summer đã qua với this summer trong kế hoạch. ABC là đánh vần bằng tên chữ cái; nghe câu mẫu rồi thử nói, website chưa ghi âm hoặc chấm phát âm.'),
    ], words=words, dialogues=dialogs, exercises=exercises)


def render_study():
    return render(data(), picture)
