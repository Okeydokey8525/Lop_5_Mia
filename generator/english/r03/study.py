"""Review 3: past/future, health role-play, clearly labelled food extension."""
from english.study.author import word as w, question as q, choice as c, dialogue as d
from english.study.render import render_study as render
from english.r03.content import picture


def data():
    rows={
        'plans':[
            ('took photos','đã chụp ảnh','I took photos on my family trip.','take photos'),
            ('collected seashells','đã nhặt vỏ sò','We collected seashells last weekend.',None),
            ('decorate the house','trang trí nhà','I will decorate the house at Tet.','decorate the house'),
            ('make spring rolls','làm nem/cuốn chả giò','We will make spring rolls at Tet.',None),
            ('pizza','bánh pizza','We will have pizza at our party.','pizza'),
            ('apple juice','nước ép táo','We will have apple juice at our party.',None),
            ('last weekend','cuối tuần vừa qua','Last weekend, I bought souvenirs.',None),
            ('next week','tuần tới','We will have a party next week.',None)],
        'health':[
            ('do morning exercise','tập thể dục buổi sáng','He does morning exercise every day.','do morning exercise'),
            ('twice a week','hai lần mỗi tuần','She plays sports twice a week.',None),
            ('headache','đau đầu','In the role-play, I have a headache.',None),
            ('toothache','đau răng','In the role-play, I have a toothache.',None),
            ('have a rest','nghỉ ngơi','The advice line is: You should have a rest.',None),
            ('should not','không nên','The advice line is: You should not watch too much TV.',None)],
        'extension':[
            ('dairy','nhóm sữa và sản phẩm từ sữa','Milk is in the dairy group.',None),
            ('grains','nhóm ngũ cốc','Rice is in the grains group.',None),
            ('protein','nhóm thực phẩm giàu đạm','Fish is in the protein group on our word card.',None),
            ('fruit and vegetables','nhóm trái cây và rau','Carrot is in the fruit and vegetables group.',None)]}
    words=[w(g,n,v,e,**({'image':img} if img else {})) for g,rs in rows.items() for n,v,e,img in rs]
    dialogs=[
        d('plans','Việc đã qua','Did you take photos on the family trip?','Yes, I did. I took photos with my sister.','Did + take; câu kể dùng took.'),
        d('plans','Kế hoạch Tết','Will you decorate the house at Tet?','Yes, I will. I will make spring rolls, too.','Will + nguyên mẫu; không dùng will decorated.'),
        d('health','Tần suất','How often does she play sports?','She plays sports twice a week.','Does…play trong câu hỏi, plays trong câu kể.'),
        d('health','Lời thoại quan tâm','What is the matter?','I have a headache.','Luyện câu hỏi và lời đáp trong bài Anh; không dùng để tự chẩn đoán.'),
        d('extension','Mở rộng: nhóm sữa','Which food group is milk in?','It is in the dairy group.','Extension trang 38–39: gọi tên nhóm theo bảng học từ.'),
        d('extension','Mở rộng: ngũ cốc','Which food group is rice in?','It is in the grains group.','Đây là phân nhóm thực phẩm theo hoạt động trong sách, không phải thực đơn bắt buộc.')]
    exercises=[
        q('past-base','plans','Did you ___ photos? Use take, took or takes.','take','Did + take nguyên mẫu.'),
        q('future-base','plans','We will ___ spring rolls. Use make.','make','Will + make.'),
        c('menu-listen','plans','Which drink will they have?','apple juice','Nghe đồ uống, không chọn pizza.',['apple juice','milk tea','lemonade','orange juice'],speech='At our party next week, we will have pizza and apple juice.'),
        q('past-took','plans','Last weekend, I ___ photos. Use take in the past.','took','Take → took.'),
        q('habit-does','health','He ___ morning exercise. Use do.','does','He does morning exercise.'),
        q('frequency-base','health','How often does she ___ sports? Use play.','play','Sau does dùng play.'),
        c('health-listen','health','Which problem is in the role-play?','headache','Đọc/nghe lời thoại giả định.',['headache','toothache','sore throat','stomach ache'],speech='In our English role-play, Mai says, I have a headache. Her partner says, You should have a rest.'),
        q('advice-base','health','You should ___ a rest. Use have.','have','Should + nguyên mẫu.'),
        c('dairy-word','extension','Extension card: milk → dairy. Which group is milk in?','dairy','Theo thẻ nhóm thực phẩm.',['dairy','grains','protein','fruit and vegetables']),
        q('grains-word','extension','Extension word card: rice → grains. Write the group.','grains','Rice thuộc grains trong bảng.'),
        c('food-listen','extension','Extension: Which food is heard?','fish','Nghe fish; nhóm protein theo bảng học từ.',['fish','milk','rice','carrot'],speech='On our food word card, fish is in the protein group.'),
        q('vegetables-word','extension','Complete the group name: fruit and ___.','vegetables','Fruit and vegetables.')]
    return dict(unit='R3',label='Review 3',overview='TongQuan_Review3.html',key='mia5:learn:en-r03-v1',intro='Ôn Units 11–15: nghe thường/chậm, ABC, hội thoại và bài luyện tự lưu. Nhóm thực phẩm là phần Extension riêng.',groups=[
        dict(id='plans',name='Chuyến đi và kế hoạch',tip='Last weekend: did + nguyên mẫu / câu kể quá khứ. At Tet, next week: will + nguyên mẫu. Food hỏi đồ ăn, drinks hỏi đồ uống.'),
        dict(id='health',name='Thói quen và lời thoại',tip='He does / she plays; How often does…? Should + nguyên mẫu. Theo thẻ hội thoại, không suy triệu chứng thành lời khuyên duy nhất.'),
        dict(id='extension',name='Mở rộng: nhóm thực phẩm',tip='Extension trang 38–39: dairy, grains, protein, fruit and vegetables. Học tên nhóm, chọn từ theo thẻ; thử viết bữa sáng của em với người thân. ABC là tên chữ cái; website chưa chấm phát âm.')],words=words,dialogues=dialogs,exercises=exercises)


def render_study():return render(data(),picture)
