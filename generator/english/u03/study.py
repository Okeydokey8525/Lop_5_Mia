"""Original companion for countries, personality and a friend's profile."""
from english.u03.content import COUNTRIES, TRAITS, picture
from english.study.author import word as w, question as q, choice as c, dialogue as d
from english.study.render import render_study as render


def data():
    names={'Australia':'Úc','Malaysia':'Malaysia','America':'Mỹ','Japan':'Nhật Bản','Britain':'Anh (Britain)'}
    words=[]
    for country,nationality in COUNTRIES.items():
        words += [w('nationality',country,names[country],'My friend is from '+country+'.'),
                  w('nationality',nationality,'quốc tịch: '+names[country],'My friend is '+nationality+'.')]
    words += [w('personality',name,vn,'My friend is '+name+'.',image=name) for name,vn in TRAITS.items()]
    words += [w('profile',name,vn,example) for name,vn,example in [
        ('long hair','tóc dài','She has long hair.'),('short hair','tóc ngắn','He has short hair.'),
        ('big eyes','mắt to','She has big eyes.'),('friend','người bạn','This is my friend.')]]
    dialogues=[
        d('nationality','Quê quán','Where is she from?','She is from Japan.','From + tên nước: bạn ấy đến từ Nhật Bản.'),
        d('nationality','Quốc tịch','What nationality is he?','He is Australian.','Quốc gia Australia; quốc tịch Australian. Không đoán từ khuôn mặt.'),
        d('personality','Tính cách','What is she like?','She is friendly and helpful.','Bạn ấy có tính cách thế nào? — Thân thiện và hay giúp đỡ.'),
        d('personality','Năng động','What is he like?','He is active. He likes playing basketball.','Active nói năng động; hành động chỉ minh họa nghĩa, không kết luận tính cách từ ngoại hình.'),
        d('profile','Giới thiệu bạn','Who is this?','This is my friend Mai. She has long hair and big eyes.','Dùng has với tóc, mắt; không dùng is long hair.'),
        d('profile','Lớp của bạn','What grade is she in?','She is in Grade 5.','Bạn ấy học lớp 5.'),
    ]
    exercises=[
        c('nationality-japan','nationality','She is from Japan. She is ___.','Japanese','Japan → Japanese.',list(COUNTRIES.values())),
        q('nationality-country','nationality','He is Australian. He is from ___.','Australia','Tên nước là Australia.'),
        c('nationality-listen','nationality','What nationality is the friend?','Malaysian','Lời nghe nói from Malaysia.',list(COUNTRIES.values()),speech='My friend is from Malaysia.'),
        q('nationality-is','nationality','What nationality ___ she?','is','What nationality is she?'),
        c('personality-help','personality','Mai helps her friend pick up dropped books. Which word matches this action?','helpful','Helpful: hay giúp đỡ.',list(TRAITS)),
        q('personality-spell','personality','f r i e n d _ y — Write the whole word.','friendly','Friendly có chữ l trước y.'),
        c('personality-listen','personality','What is he like?','active','Lời nghe nói He is active.',list(TRAITS),speech='He is active. He likes running and playing basketball.'),
        c('personality-question','personality','Which answer tells us about personality?','She is clever.','What is she like? hỏi tính cách.',['She is Japanese.','She is clever.','She has long hair.','She is from Japan.']),
        q('profile-has','profile','She ___ long hair.','has','She has + tóc/mắt.'),
        q('profile-is','profile','He ___ friendly.','is','He is + tính cách.'),
        c('profile-listen','profile','Which detail does the speaker describe?','short hair','Lời nghe nói He has short hair.',['long hair','short hair','big eyes','Grade 5'],speech='This is my friend. He has short hair.'),
        q('profile-full','profile','Card: Mai / helpful. Write a full sentence starting with She.','She is helpful.','She is helpful.',alternatives=['She’s helpful.']),
    ]
    return dict(unit=3,key='mia5:learn:en-u03-v1',intro='Ghép tên nước với quốc tịch, nói tính cách và giới thiệu bạn. Không đoán quốc tịch từ ngoại hình.',groups=[
        dict(id='nationality',name='Nước và quốc tịch',tip='Where is…from? hỏi tên nước. What nationality is…? hỏi quốc tịch. Britain/British theo phạm vi sách. Nghe theo từng cặp Australia/Australian, Japan/Japanese.'),
        dict(id='personality',name='Tính cách',tip='What is he/she like? hỏi tính cách, không hỏi sở thích. AC-tive và FRIEND-ly nhấn âm đầu. Tranh minh họa hành động; không suy tính cách từ quốc tịch.'),
        dict(id='profile',name='Giới thiệu bạn',tip='He/She is + tính cách hoặc quốc tịch. He/She has + tóc hoặc mắt. She’s = She is; không thay She has bằng She’s trong các câu này.')],words=words,dialogues=dialogues,exercises=exercises)


def render_study():return render(data(),picture)
