"""Review 2 combines school, classroom and two distinct past outings."""
from english.study.author import word as w,question as q,choice as c,dialogue as d
from english.study.render import render_study as render
from english.r02.content import picture


def data():
    words=[w('school',name,vn,example,**({'image':img} if img else {})) for name,vn,example,img in [
        ('library','thư viện','The library is on the second floor.','library'),('second floor','tầng thứ hai phía trên tầng trệt','The art room is on the second floor.',None),
        ('doing projects','làm dự án (V-ing)','She likes doing projects.','do projects'),('interesting','thú vị','She thinks it is interesting.',None)]]
    words += [w('classroom',name,vn,example,**({'image':img} if img else {})) for name,vn,example,img in [
        ('glue stick','hồ dán dạng thỏi','This is An’s glue stick.','glue stick'),('crayon','bút sáp màu','Whose crayon is this?',None),
        ('beside','bên cạnh','The pencils are beside the book.',None),('whose','của ai','Whose glue stick is this?',None)]]
    words += [w('trips',name,vn,example,**({'image':img} if img else {})) for name,vn,example,img in [
        ('aquarium','thủy cung','We were at the aquarium yesterday.','aquarium'),('listened to music','đã nghe nhạc','We listened to music yesterday.',None),
        ('went','đã đi (quá khứ của go)','They went to Ba Na Hills last November.',None),('planted trees','đã trồng cây','They planted trees on the trip.','plant trees'),
        ('winter holiday','kỳ nghỉ mùa đông','This is a plan for a winter holiday.',None),('sightseeing holiday','kỳ nghỉ tham quan','This is a plan for a sightseeing holiday.',None)]]
    dialogs=[d('school','Hỏi phòng học','Where is the library?','It is on the second floor.','Ground floor ở dưới first floor, không coi hai tầng là một.'),
        d('school','Hoạt động và lý do','What school activity does she like?','She likes doing projects because she thinks it is useful.','Sau does dùng like; khi kể dùng likes + V-ing.'),
        d('classroom','Của ai?','Whose glue stick is this?','It is An’s.','Whose hỏi chủ sở hữu.'),
        d('classroom','Ở đâu?','Where are the crayons?','They are under the desk.','Where are…? — They are… với số nhiều.'),
        d('trips','Hôm qua','Were you at the aquarium yesterday?','Yes, we were. We watched the fish.','Kể nơi bằng were, kể hoạt động bằng watched.'),
        d('trips','Chuyến đi của trường','Did they go to Ba Na Hills last November?','Yes, they did. They visited the old buildings.','Sau Did dùng go; câu kể có went/visited.')]
    exercises=[q('school-on','school','The library is ___ the second floor.','on','On the + tầng + floor.'),
        q('school-like','school','What school activity does she ___?','like','Sau does dùng like.'),
        c('school-listen','school','Why does she like reading books?','interesting','Lời nghe nói interesting.',['interesting','useful','fun','good for group work'],speech='She likes reading books because she thinks it is interesting.'),
        q('school-first','school','ground floor → ___ → second floor','first floor','First floor ở ngay trên ground floor.'),
        q('class-whose','classroom','___ set square is this?','Whose','Whose hỏi của ai.'),
        q('class-owner','classroom','Card: owner Mai. It is ___. Write the possessive name.','Mai’s','Cần dấu sở hữu ’s, không chỉ tên.'),
        c('class-listen','classroom','Where are the crayons?','under the desk','Lời nghe nói under the desk.',['under the desk','beside the book','above the window','in front of the clock'],speech='The crayons are under the desk.'),
        q('class-are','classroom','The pencils ___ beside the notebook.','are','Số nhiều dùng are.'),
        q('trip-were','trips','We ___ at the theatre yesterday.','were','We were.'),
        q('trip-go','trips','Did they ___ to Hoan Kiem Lake?','go','Sau did dùng go.'),
        c('trip-listen','trips','Which activity happened on the school trip?','planted trees','Yesterday là ngắm cá, school trip mới trồng cây.',['watched the fish','planted trees','played chess','listened to music'],speech='Yesterday, we watched the fish at the aquarium. On our school trip, we planted trees.'),
        c('trip-extension','trips','Card: Holiday type = winter holiday. Which type is written?','winter holiday','Đọc loại kỳ nghỉ theo thẻ, phần mở rộng 76–77.',['winter holiday','beach holiday','sightseeing holiday','adventure holiday'])]
    return dict(unit='R2',label='Review 2',overview='TongQuan_Review2.html',key='mia5:learn:en-r02-v1',intro='Ôn kết hợp Units 6–10: trường lớp, sở thích, đồ dùng và những chuyến đi đã qua.',groups=[
        dict(id='school',name='Trường và hoạt động',tip='Where is…? — On the…floor. Does…like? — He/She likes… Why…? — Because… Đọc đúng phòng, hoạt động và lý do.'),
        dict(id='classroom',name='Vị trí và chủ sở hữu',tip='Where hỏi ở đâu, Whose hỏi của ai. It’s = It is; tên’s chỉ sở hữu. Một vật It is; nhiều vật They are.'),
        dict(id='trips',name='Kể chuyến đi',tip='Yesterday và school trip có thể là hai chuyến khác nhau. Sau did dùng go/do; câu kể dùng went/played/planted. Các loại holiday ở phần mở rộng đọc theo thẻ, không đoán mọi hoạt động chỉ thuộc một loại.')],words=words,dialogues=dialogs,exercises=exercises)


def render_study():return render(data(),picture)
