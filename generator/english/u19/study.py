"""Opinions, places of interest, and distances; companion practice for Unit 19."""
from english.u19.content import CORE, MEANINGS, PLACES, OPINIONS, picture
from english.study.author import word as w, question as q, choice as c, dialogue as d
from english.study.render import render_study as render


def data():
    words = [w('places', k, v, 'I want to visit the ' + k + '.', image=k) for k, v in zip(CORE, MEANINGS)]
    words += [w('places', k, v, e) for k, v, e in [
        (PLACES[0], 'Thác Bản Giốc', 'What do you think of Ban Gioc Waterfall?'),
        (PLACES[1], 'Phố cổ Hội An', 'What do you think of Hoi An Old Town?'),
        (PLACES[2], 'Nhà hát Opera Sydney', 'I think Sydney Opera House is beautiful.'),
        (PLACES[3], 'Tháp đôi Petronas', 'I think Petronas Twin Towers are fantastic.'),
    ]]
    words += [w('opinions', k, v, e) for k, v, e in [
        ('peaceful', 'yên bình', 'I think the lake is peaceful.'),
        ('exciting', 'thú vị, sôi động', 'I think the old town is exciting.'),
        ('beautiful', 'đẹp', 'I think the waterfall is beautiful.'),
        ('fantastic', 'tuyệt vời', 'I think the towers are fantastic.'),
        ('think', 'nghĩ, cho rằng', 'What do you think of the lake?'),
        ('interesting', 'thú vị', 'There are interesting things to see and do.'),
    ]]
    words += [w('distance', k, v, e) for k, v, e in [
        ('far', 'xa', 'How far is it from here to the lake?'),
        ('near', 'gần', 'The park is near my home.'),
        ('about', 'khoảng', 'It is about four kilometres.'),
        ('kilometre', 'ki lô mét', 'It is about one kilometre.'),
        ('hundred', 'một trăm', 'The card says one hundred kilometres.'),
        ('distance', 'khoảng cách', 'How far asks about distance.'),
    ]]
    dialogs = [
        d('places', 'Hỏi cảm nhận về thác', 'What do you think of Ban Gioc Waterfall?', 'I think it is peaceful.', 'It chỉ một địa điểm; đây là một ý kiến mẫu.'),
        d('places', 'Tháp đôi dùng they', 'What do you think of Petronas Twin Towers?', 'I think they are fantastic.', 'Towers số nhiều → they are, không they is.'),
        d('opinions', 'Em nghĩ thế nào?', 'What do you think of Hoi An Old Town?', 'I think it is exciting.', 'What do you think of…? I think it is… Không suy một cảm nhận duy nhất từ tranh.'),
        d('opinions', 'Hai người có thể nghĩ khác', 'I think the lake is peaceful. What do you think of it?', 'I think it is beautiful.', 'Hai ý kiến đều có thể hợp lý; đề chấm theo người nói được giao.'),
        d('distance', 'Hỏi khoảng cách', 'How far is it from here to the lake?', 'It is about four kilometres.', 'Dữ kiện giả định để luyện Anh; from điểm đi to điểm đến; one kilometre nhưng four kilometres.'),
        d('distance', 'Ngữ điệu câu hỏi Wh', 'How far is it from the school to the park?', 'It is about seven kilometres.', 'Câu hỏi Wh như What do you think of…?/How far is it…? thường xuống giọng. Khoảng cách ví dụ là giả định.'),
    ]
    exercises = [
        c('place-listen', 'places', 'Which type of place is heard?', 'waterfall', 'Nghe waterfall.', CORE, speech='I want to visit the waterfall.'),
        q('place-cave', 'places', 'Complete: ca___. Write the whole word meaning hang động.', 'cave', 'Cave.'),
        q('place-plural', 'places', 'I think Petronas Twin Towers ___ fantastic.', 'are', 'Towers số nhiều → are.'),
        q('place-of', 'places', 'What do you think ___ Hoi An Old Town?', 'of', 'Think of + nơi chốn.'),
        c('opinion-listen', 'opinions', 'Which opinion does Nam give?', 'peaceful', 'Chỉ lấy ý kiến Nam.', OPINIONS, speech='Linh thinks the lake is exciting. Nam thinks it is peaceful.'),
        q('opinion-do', 'opinions', 'What ___ you think of the cave?', 'do', 'Do you think.'),
        q('opinion-full', 'opinions', 'Rewrite in full: I think it’s beautiful.', 'I think it is beautiful.', 'It’s = it is.'),
        q('opinion-sentence', 'opinions', 'Card: it / peaceful. Write in full form starting with I think.', 'I think it is peaceful.', 'I think it is + tính từ.'),
        c('distance-listen', 'distance', 'How far is the lake from Nam’s imaginary school?', 'six kilometres', 'Chỉ lấy khoảng cách của Nam.', ['four kilometres', 'six kilometres', 'seven kilometres', 'nine kilometres'], speech='These distances are imaginary. Linh says seven kilometres. Nam says six kilometres.'),
        q('distance-to', 'distance', 'How far is it from here ___ the lake?', 'to', 'From…to…'),
        q('distance-singular', 'distance', 'It is about one ___. Use the singular of kilometres.', 'kilometre', 'One kilometre.'),
        q('distance-route', 'distance', 'Imaginary route: school → museum → lake. The first leg is three kilometres and the second is four. Write the total distance phrase along this route in words.', 'seven kilometres', 'Cùng tuyến qua museum: 3 + 4 = 7.', alternatives=['7 kilometres', '7 km']),
    ]
    return dict(unit=19, key='mia5:learn:en-u19-v1', intro='Học địa điểm, nêu cảm nhận và hỏi khoảng cách: nghe thường/chậm, ABC, hội thoại và bài luyện tự lưu.', groups=[
        dict(id='places', name='Những nơi thú vị', tip='Tranh minh họa loại địa điểm, không nhận diện tên riêng. Ban Gioc Waterfall, Hoi An Old Town, Sydney Opera House dùng it is; Petronas Twin Towers dùng they are.'),
        dict(id='opinions', name='Em nghĩ thế nào?', tip='What do you think of…? I think it is/they are… Ý kiến có thể khác nhau; đọc đúng người nói. Câu hỏi Wh thường xuống giọng. ABC là tên chữ cái, không phải phonics.'),
        dict(id='distance', name='Hỏi khoảng cách', tip='How far is it from…to…? It is about…kilometres. One kilometre; từ hai trở lên dùng kilometres. Khoảng cách tự soạn là giả định. Khi cộng chặng, chỉ cộng các chặng đã nêu trên cùng tuyến.'),
    ], words=words, dialogues=dialogs, exercises=exercises)


def render_study():
    return render(data(), picture)
