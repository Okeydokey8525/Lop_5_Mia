"""Special-day activities, menus and constrained original writing."""
from english.u13.content import CORE,MEANINGS,EVENTS,FOODS,DRINKS,picture
from english.study.author import word as w,question as q,choice as c,dialogue as d
from english.study.render import render_study as render


def data():
    words=[w('days',k,vn,ex) for k,vn,ex in [(EVENTS[0],'ngày Thiếu nhi','We will dance on Children’s Day.'),(EVENTS[1],'ngày Nhà giáo','We will sing on Teachers’ Day.'),(EVENTS[2],'ngày Thể thao','We will play badminton on Sports Day.'),(EVENTS[3],'Tết Trung thu','We will have a party at Mid-Autumn Festival.')]]
    words += [w('menu',k,vn,'We will have '+k+'.',image=k) for k,vn in zip(CORE,MEANINGS)]
    words += [w('menu',k,vn,'We will have '+k+'.') for k,vn in [('lemonade','nước chanh'),('water','nước')]]
    words += [w('party',k,vn,ex) for k,vn,ex in [('dance','nhảy/múa','We will dance at the party.'),('sing','hát','They will sing at our party.'),('play badminton','chơi cầu lông','We will play badminton on Sports Day.'),('have a party','tổ chức/dự tiệc','We will have a party on Sunday.'),('food','đồ ăn','What food will you have?'),('drinks','đồ uống','What drinks will you have?')]]
    dialogs=[d('days','Ngày Thiếu nhi','What will you do on Children’s Day?','We will dance and sing.','What will…do hỏi hoạt động.'),
        d('days','Trung thu','What will you do at Mid-Autumn Festival?','We will have a party.','At Mid-Autumn Festival; on Children’s Day.'),
        d('menu','Đồ ăn','What food will you have at the party?','We will have pizza and burgers.','Food là đồ ăn; sau will dùng have.'),
        d('menu','Đồ uống','What drinks will you have at the party?','We will have apple juice and water.','Drinks là đồ uống.'),
        d('party','Lời mời','Will you come to my birthday party on Sunday?','Yes, I will. Thank you.','Will you…? đáp Yes, I will.'),
        d('party','Ngày Thể thao','What will they do on Sports Day?','They will play badminton.','Will không đổi theo they; dùng play nguyên mẫu.')]
    exercises=[c('days-listen','days','What will they do?','dance','Nghe dance.',['dance','sing','play badminton','have a party'],speech='We will dance on Children’s Day.'),
        q('days-on','days','We will sing ___ Teachers’ Day.','on','On + tên ngày.'),
        q('days-at','days','We will have a party ___ Mid-Autumn Festival.','at','Sách dùng at Mid-Autumn Festival.'),
        q('days-do','days','What will you ___ on Sports Day?','do','What will you do?'),
        c('menu-listen','menu','What drink will they have?','apple juice','Nghe apple juice.',DRINKS,speech='We will have burgers and apple juice.'),
        q('menu-have','menu','We will ___ pizza. Use have.','have','Will + have, không phải has.'),
        q('menu-tea','menu','Complete: milk ___.','tea','Milk tea.'),
        q('menu-drinks','menu','What ___ will you have? We will have water.','drinks','Water là đồ uống.'),
        c('party-listen','party','When will the party be?','Sunday','Nghe Sunday.',['Monday','Friday','Saturday','Sunday'],speech='Our party will be on Sunday. We will sing and dance.'),
        q('party-full','party','Rewrite in full: We’ll have pizza.','We will have pizza.','We’ll = We will.',exactForm=True),
        q('party-play','party','They will ___ badminton.','play','Will + play.'),
        q('party-sentence','party','Card: we / have / burgers / and / apple juice. Write one full-form future sentence in this order.','We will have burgers and apple juice.','We will have + food + and + drink.',exactForm=True)]
    return dict(unit=13,key='mia5:learn:en-u13-v1',intro='Lên kế hoạch cho ngày đặc biệt: làm gì, ăn gì và uống gì. Nghe kèm bài và luyện nói theo lượt.',groups=[
        dict(id='days',name='Ngày đặc biệt',tip='What will you do on…? — We’ll + nguyên mẫu. Dùng on Children’s Day / Teachers’ Day / Sports Day; at Mid-Autumn Festival theo mẫu sách.'),
        dict(id='menu',name='Thực đơn của lớp',tip='What food/drinks will you have at the party? — We’ll have… Food: pizza, burgers; drinks: milk tea, apple juice. Đây là học tên đồ ăn, không phải gợi ý khẩu phần.'),
        dict(id='party',name='Lời mời và kế hoạch',tip='Will you come…? — Yes, I will. We’ll = We will; They’ll = They will. Đọc nhấn food/drinks và have/party theo cụm; ABC là tên từng chữ cái. Các thẻ tiệc là giả định, cần đọc đúng ngày và thực đơn.')],words=words,dialogues=dialogs,exercises=exercises)


def render_study():return render(data(),picture)
