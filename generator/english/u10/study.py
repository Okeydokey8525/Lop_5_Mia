"""School trip learning companion with examples from fictional class cards."""
from english.u10.content import PLACES,ACTIVITIES,CORE,PAST,MONTHS,picture
from english.study.author import word as w,question as q,choice as c,dialogue as d
from english.study.render import render_study as render


def data():
    meanings=['Bà Nà Hills','Hồ Hoàn Kiếm','Khu du lịch Suối Tiên','Chùa Bái Đính']
    words=[w('places',name,vn,'They went to '+name+'.') for name,vn in zip(PLACES,meanings)]
    words += [w('activities',name,vn,'They '+past+'.',image=name) for name,(past,vn) in ACTIVITIES.items()]
    words += [w('activities',past,vn+' (đã làm)','They '+past+' on the trip.',image=name) for name,(past,vn) in ACTIVITIES.items()]
    words += [w('months',name,'tháng '+str(i+9),'They went to Hoan Kiem Lake last '+name+'.') for i,name in enumerate(MONTHS)]
    dialogs=[d('places','Hỏi đã đến đâu','Did they go to Ba Na Hills?','Yes, they did.','Sau Did dùng go; câu đáp Yes, they did.'),
        d('places','Trả lời không','Did they go to Bai Dinh Pagoda?','No, they did not. They went to Hoan Kiem Lake.','Didn’t = did not; câu kể dùng went to.'),
        d('activities','Làm gì ở đó?','What did they do there?','They visited the old buildings.','Hỏi did…do; kể visited.'),
        d('activities','Trồng cây','Did they plant trees?','Yes, they did. They planted trees.','Sau did dùng plant, câu kể dùng planted.'),
        d('months','Chuyến đi tháng 11','Where did they go last November?','They went to Ba Na Hills.','No-VEM-ber nhấn âm thứ hai.'),
        d('months','Chuyến đi tháng 12','What did they do last December?','They walked around the lake.','De-CEM-ber nhấn âm thứ hai. Các ví dụ là chuyến đi giả định.'),]
    exercises=[c('place-listen','places','Where did the class go?','Hoan Kiem Lake','Lời nghe nói Hoan Kiem Lake.',PLACES,speech='They went to Hoan Kiem Lake.'),
        q('place-go','places','Did they ___ to Ba Na Hills?','go','Sau did dùng go.'),
        q('place-went','places','They ___ to Bai Dinh Pagoda. Use go.','went','Go → went trong câu kể quá khứ.'),
        q('place-negative','places','Did they go to the lake? No, they ___.','did not','Did not = didn’t.',alternatives=['didn’t']),
        c('activity-listen','activities','What did they do?','planted trees','Lời nghe nói planted trees.',PAST,speech='They planted trees on the trip.'),
        q('activity-visited','activities','They ___ the old buildings. Use visit.','visited','Visit → visited.'),
        q('activity-question','activities','What did they ___ there?','do','Sau did dùng do, không dùng did.'),
        q('activity-full','activities','Card: walk around the lake. Write a past sentence starting with They.','They walked around the lake.','They walked around the lake.'),
        c('month-listen','months','When was the trip?','November','Lời nghe nói last November.',MONTHS,speech='They went to Ba Na Hills last November.'),
        q('month-after','months','Which month comes after November?','December','December theo sau November.'),
        q('month-spell','months','D e c e m _ e r — Write the whole word.','December','December có chữ b trước e.'),
        q('month-full','months','Card: Hoan Kiem Lake / last December. Start with They went.','They went to Hoan Kiem Lake last December.','They went to + nơi + last + tháng.')]
    return dict(unit=10,key='mia5:learn:en-u10-v1',intro='Hỏi và kể chuyến đi: nơi đến, việc đã làm và tháng của chuyến đi.',groups=[
        dict(id='places',name='Chuyến đi đâu?',tip='Did they go…? — Yes, they did./No, they didn’t. Câu kể: They went to… Tên riêng địa danh theo sách; giọng máy có thể đọc tên Việt chưa tự nhiên.'),
        dict(id='activities',name='Đã làm gì?',tip='What did they do there? — They + động từ quá khứ. Visit → visited, plant → planted, play → played, walk → walked. Tranh là cảnh hoạt động chung, không phải ảnh địa danh thật.'),
        dict(id='months',name='Tháng của chuyến đi',tip='No-VEM-ber, De-CEM-ber nhấn âm thứ hai. Last November/December: tháng 11/12 vừa qua. Đọc đúng tháng của từng thẻ, không suy từ địa điểm.')],words=words,dialogues=dialogs,exercises=exercises)


def render_study():return render(data(),picture)
