"""Places and past outings; pronunciation and practice are not formal scores."""
from english.u09.content import PLACES, ACTIVITIES, PAST, picture
from english.study.author import word as w,question as q,choice as c,dialogue as d
from english.study.render import render_study as render


def data():
    words=[w('places',name,vn,'We were at the '+name+' yesterday.',image=name) for name,vn in PLACES.items()]
    words += [w('places',name,vn,'I was at the '+name+' yesterday.') for name,vn in [('cinema','rạp chiếu phim'),('bakery','tiệm bánh')]]
    words += [w('activities',past,vn+' (đã làm)','We '+past+' yesterday.') for _,(past,vn) in ACTIVITIES.items()]
    words += [w('past',name,vn,example) for name,vn,example in [
        ('yesterday','hôm qua','We played chess yesterday.'),('last Saturday','thứ Bảy vừa qua','I was at the theatre last Saturday.'),
        ('last Sunday','Chủ nhật vừa qua','We were at the campsite last Sunday.'),
        ('was','đã ở/là (với I, he, she, it)','I was at the aquarium yesterday.'),('were','đã ở/là (với you, we, they)','We were at the funfair yesterday.')]]
    dialogues=[
        d('places','Nhóm đã ở đâu?','Were you at the aquarium yesterday?','Yes, we were.','Were you…? — Yes, we were.'),
        d('places','Trả lời không','Were you at the funfair last Saturday?','No, we were not. We were at the theatre.','Weren’t = were not.'),
        d('activities','Ngắm cá','What did you do at the aquarium?','We watched the fish.','Hỏi did…do, trả lời watched.'),
        d('activities','Cắm trại','What did you do at the campsite?','We danced around the campfire.','Dance → danced; đây là hoạt động của nhân vật, không phải hoạt động bắt buộc ở campsite.'),
        d('past','Một người kể','Where were you yesterday?','I was at the theatre. I listened to music.','Câu hỏi you dùng were; trả lời I dùng was.'),
        d('past','Nhóm kể lại','What did you do last Sunday?','We played chess.','What did you do…? — We + động từ quá khứ.'),
    ]
    picture_q=c('place-listen','places','Choose the place you hear.','aquarium','Tìm bể kính lớn có cá.',list(PLACES),speech='aquarium')
    picture_q.update(kind='picture',instruction='Nghe tên địa điểm rồi chọn tranh.')
    exercises=[picture_q,
        q('place-spell','places','c a m p _ i t e — Write the whole word.','campsite','Campsite có chữ s trước i.'),
        c('place-theatre','places','Which place has a stage for a live play?','theatre','Theatre là nhà hát, có sân khấu trình diễn.',list(PLACES)),
        c('place-bakery','places','Which place means “tiệm bánh”?','bakery','Bakery là tiệm bánh.',['cinema','bakery','aquarium','campsite']),
        q('activity-watched','activities','We ___ the fish yesterday. Use watch.','watched','Watch → watched, không dùng watching.'),
        q('activity-danced','activities','Write the past form of dance.','danced','Dance có e, thêm d.'),
        c('activity-listen','activities','What did the group do?','played chess','Lời nghe nói We played chess.',PAST,speech='We played chess at the campsite.'),
        q('activity-to','activities','We listened ___ music.','to','Listen to music; giữ to khi dùng listened.'),
        q('past-was','past','I ___ at the theatre yesterday.','was','I dùng was; we/you/they dùng were.'),
        q('past-were','past','We ___ at the campsite last Sunday.','were','We were.'),
        q('past-did','past','What did you ___ there?','do','Sau did dùng động từ nguyên mẫu do.'),
        q('past-negative','past','Were you at the funfair? No, we ___.','were not','No, we were not. Cũng viết weren’t.',alternatives=['weren’t']),
    ]
    return dict(unit=9,key='mia5:learn:en-u09-v1',intro='Kể chuyến đi đã qua: em đã ở đâu và đã làm gì? Nghe, đọc theo rồi tự thử nhớ.',groups=[
        dict(id='places',name='Địa điểm',tip='Were you at the…yesterday? — Yes, we were./No, we weren’t. CI-ne-ma, BA-ke-ry nhấn âm đầu. Theatre khác cinema: nhà hát có trình diễn, cinema chiếu phim.'),
        dict(id='activities',name='Việc đã làm',tip='Listen → listened; watch → watched; dance → danced; play → played. What did you do there? — We + động từ quá khứ. Không thêm were trước played/listened.'),
        dict(id='past',name='Kể chuyện đã qua',tip='I/he/she/it was; you/we/they were. Sau did dùng nguyên mẫu: What did you do? Yesterday, last Saturday, last Sunday là thời gian đã qua. Weren’t = were not.')],words=words,dialogues=dialogues,exercises=exercises)


def render_study():return render(data(),picture)
