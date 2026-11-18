"""Family-trip learning companion; all examples are original."""
from english.u11.content import ACTIVITIES,CORE,PAST,picture
from english.study.author import word as w,question as q,choice as c,dialogue as d
from english.study.render import render_study as render


def data():
    words=[w('beach',k,ACTIVITIES[k][1],'I '+ACTIVITIES[k][0]+' with my family.',**({'image':k} if k in CORE else {})) for k in list(ACTIVITIES)[:4]]
    words += [w('trip',k,ACTIVITIES[k][1],'We '+ACTIVITIES[k][0]+'.',**({'image':k} if k in CORE else {})) for k in list(ACTIVITIES)[4:]]
    words += [w('story',past,vn,example) for past,vn,example in [
        ('swam','đã bơi','I swam with my mother.'),('took photos','đã chụp ảnh','I took photos with my father.'),
        ('bought souvenirs','đã mua quà lưu niệm','We bought souvenirs last summer.'),('ate seafood','đã ăn hải sản','We ate seafood last weekend.'),
        ('last weekend','cuối tuần vừa qua','We took a boat trip last weekend.'),('last summer','mùa hè vừa qua','We saw some interesting places last summer.'),
        ('yesterday','hôm qua','I collected seashells yesterday.'),('on Saturday','vào thứ Bảy','I walked on the beach on Saturday.')]]
    dialogs=[d('beach','Hỏi đã bơi chưa','Did you swim?','Yes, I did. I swam with my mother.','Sau did dùng swim; câu kể dùng swam.'),
        d('beach','Chưa chụp ảnh','Did you take photos?','No, I did not. I collected seashells.','Did not + take; collected là quá khứ của collect.'),
        d('trip','Đi thuyền','What did your family do there?','We took a boat trip around the bay.','Hỏi did…do; trả lời took.'),
        d('trip','Mua quà','Did you buy souvenirs?','Yes, I did. I bought souvenirs with my father.','Buy → bought; with là cùng với.'),
        d('story','Khi nào?','When did your family go there?','We went there last summer.','When hỏi thời gian; last summer là mùa hè vừa qua.'),
        d('story','Kể ngày Chủ nhật','What did you do on Sunday?','I took photos with my brother.','Tách đúng ngày, hoạt động và người đi cùng.')]
    exercises=[c('beach-listen','beach','What did the speaker do?','collected seashells','Lời nghe nói collected seashells.',PAST[:4],speech='I collected seashells with my brother.'),
        q('beach-take','beach','Did you ___ photos?','take','Sau did dùng take.'),
        q('beach-swam','beach','I ___ with my mother. Use swim.','swam','Swim → swam.'),
        q('beach-negative','beach','Did you swim? No, I ___.','did not','Did not = didn’t.',alternatives=['didn’t']),
        c('trip-listen','trip','What did the family do?','took a boat trip around the bay','Lời nghe nói took a boat trip around the bay.',PAST[4:],speech='We took a boat trip around the bay.'),
        q('trip-bought','trip','We ___ souvenirs. Use buy.','bought','Buy → bought.'),
        q('trip-do','trip','What did your family ___ there?','do','Sau did dùng do.'),
        q('trip-ate','trip','We ___ seafood. Use eat.','ate','Eat → ate.'),
        c('story-listen','story','When did the family go there?','last summer','Lời nghe nói last summer.',['last weekend','last summer','yesterday','last Sunday'],speech='My family went there last summer.'),
        q('story-full','story','Rewrite in full: I didn’t swim.','I did not swim.','Didn’t = did not; giữ swim.'),
        q('story-saw','story','We ___ some interesting places. Use see.','saw','See → saw.'),
        q('story-sentence','story','Card: take photos / with my father / yesterday. Write one past sentence starting with I, in this order.','I took photos with my father yesterday.','Take → took; giữ đúng người và thời gian.')]
    return dict(unit=11,key='mia5:learn:en-u11-v1',intro='Kể chuyến đi cùng gia đình: đã làm gì, với ai và khi nào. Có âm thanh đi kèm để thử nghe trên máy của em.',groups=[
        dict(id='beach',name='Cùng nhau ở bãi biển',tip='Did you + nguyên mẫu? — Yes, I did./No, I didn’t. Câu kể: swim → swam, take → took, collect → collected, walk → walked.'),
        dict(id='trip',name='Gia đình đã làm gì?',tip='What did your family do…? — We + quá khứ. Take → took; buy → bought; eat → ate; see → saw. Tranh là cảnh hoạt động chung, không phải ảnh địa danh thật.'),
        dict(id='story',name='Kể lại chuyến đi',tip='When hỏi thời gian. Last weekend / last summer / yesterday là thời gian đã qua. Nghe và đọc theo cụm; ABC là tên chữ cái, không phải cách phát âm cả từ.')],words=words,dialogues=dialogs,exercises=exercises)


def render_study():return render(data(),picture)
