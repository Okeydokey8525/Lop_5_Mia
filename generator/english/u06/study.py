"""Full Unit 6 learning companion; safely inherit the approved pilot's marks."""
from english.u06.content import CORE, MEANINGS, picture
from english.study.render import render_study as render


def word(group,name,meaning,example,**extra):
    return dict(id=name.replace(' ','-'),word=name,group=group,meaning=meaning,example=example,**extra)


def question(id,group,title,prompt,answer,hint,kind='text',instruction='Viết câu trả lời tiếng Anh.',**extra):
    return dict(id=id,group=group,title=title,prompt=prompt,answer=answer,hint=hint,kind=kind,instruction=instruction,**extra)


def data():
    words=[word('rooms',r,m,f'This is the {r}.',image=r) for r,m in zip(CORE,MEANINGS)]
    words += [word('floors',f+' floor',m,f'The {room} is on the {f} floor.',floor=f) for f,m,room in [
        ('ground','tầng trệt','art room'),('first','tầng thứ nhất phía trên tầng trệt','computer room'),('second','tầng thứ hai phía trên tầng trệt','library'),('third','tầng thứ ba phía trên tầng trệt','music room')]]
    words += [word('directions',name,meaning,example,direction=True) for name,meaning,example in [
        ('go upstairs','đi lên tầng trên','Go upstairs to the music room.'),
        ('go downstairs','đi xuống tầng dưới','Go downstairs to the art room.'),
        ('go along the corridor','đi dọc hành lang','Go along the corridor and turn left.'),
        ('go past the library','đi qua thư viện','Go past the library and turn right.'),
        ('turn left','rẽ trái','Go along the corridor and turn left.'),
        ('turn right','rẽ phải','Go past the music room and turn right.'),
    ]]
    dialogues=[
        dict(group='rooms',title='Tìm thư viện',a='Where is the library?',b='It is on the second floor.',meaning='Thư viện ở đâu? — Ở tầng thứ hai phía trên tầng trệt.'),
        dict(group='rooms',title='Tìm phòng mĩ thuật',a='Where is the art room?',b='It is on the ground floor.',meaning='Phòng mĩ thuật ở tầng trệt. Where’s và Where is có cùng nghĩa.'),
        dict(group='floors',title='Phòng máy tính ở tầng nào?',a='Where is the computer room?',b='It is on the first floor.',meaning='Phòng máy tính ở tầng ngay phía trên tầng trệt.'),
        dict(group='floors',title='Tầng thứ ba',a='Where is the music room?',b='It is on the third floor.',meaning='Trong ví dụ này, phòng âm nhạc ở tầng thứ ba phía trên tầng trệt.'),
        dict(group='directions',title='Hỏi đường lịch sự',a='Could you tell me the way to the art room, please?',b='Go along the corridor and turn left.',meaning='Bạn chỉ đường đến phòng mĩ thuật giúp mình nhé? — Đi dọc hành lang rồi rẽ trái.'),
        dict(group='directions',title='Đi xuống từ tầng trên',a='Could you tell me the way to the library, please?',b='Go downstairs and turn right.',meaning='Ví dụ: em đang ở tầng thứ nhất, thư viện ở tầng trệt. Đi xuống tầng dưới rồi rẽ phải.'),
        dict(group='directions',title='Cảm ơn và đáp lại',a='Thank you.',b='You are welcome.',meaning='Cảm ơn bạn. — Không có gì.'),
    ]
    q=question
    exercises=[
        q('room','rooms','Listen and choose the picture.','', 'library','Tìm tranh có kệ sách và các bạn đang đọc.',kind='picture',instruction='Nghe tên phòng rồi chọn tranh. Có thể mở lời nghe nếu cần.',speech='library',options=[r.replace(' ','-') for r in CORE]),
        q('spelling','rooms','Complete the word.','c o m p u _ e r','computer','Viết cả từ computer, có chữ t sau u.',instruction='Viết cả từ tiếng Anh, không chỉ chữ còn thiếu.'),
        q('room-music','rooms','Choose the room.','Which room means “phòng âm nhạc”?','music room','Music room là phòng âm nhạc.',kind='choice',options=CORE,instruction='Chọn tên phòng tương ứng.'),
        q('room-art','rooms','Choose the room.','Which room means “phòng mĩ thuật”?','art room','Art room là phòng mĩ thuật.',kind='choice',options=CORE,instruction='Chọn tên phòng tương ứng.'),
        q('floor-listen','floors','Listen and find the floor.','Which floor is the library on?','second floor','Lời nghe nói on the second floor.',kind='choice',options=['ground floor','first floor','second floor','third floor'],speech='The library is on the second floor.',instruction='Nghe rồi chọn tầng đúng.'),
        q('sentence','floors','Complete the reply.','It is ___ the first floor.','on','Dùng on the + tầng + floor.',instruction='Điền một từ còn thiếu.'),
        q('floor-above','floors','Read the floor order.','ground floor → ___ → second floor','first floor','First floor nằm ngay phía trên ground floor.',kind='choice',options=['third floor','ground floor','first floor','second floor'],instruction='Chọn tầng nằm ngay phía trên tầng trệt.'),
        q('floor-full','floors','Write the full reply.','Where is the music room? Card: third floor.','It is on the third floor.','Viết It is on the third floor.',alternatives=['It’s on the third floor.'],instruction='Viết một câu trả lời bắt đầu bằng It is hoặc It’s.'),
        q('route-up','directions','Listen and choose.','Which direction do you hear?','go upstairs','Go upstairs nghĩa là đi lên tầng trên.',kind='choice',options=['go downstairs','turn left','go upstairs','turn right'],speech='Go upstairs.',instruction='Nghe rồi chọn chỉ dẫn đúng.'),
        q('route-past','directions','Complete the direction.','Go ___ the library.','past','Go past là đi qua một nơi.',instruction='Điền từ mang nghĩa “qua”.'),
        q('route-right','directions','Listen for the turn.','Go along the corridor and turn ___.','right','Lời nghe nói turn right.',kind='choice',options=['left','right','upstairs','downstairs'],speech='Go along the corridor and turn right.',instruction='Nghe rồi chọn hướng rẽ.'),
        q('route-left','directions','Write the missing word.','Go downstairs and turn ___.','left','Turn left nghĩa là rẽ trái.',instruction='Điền từ để câu có nghĩa “Đi xuống tầng dưới rồi rẽ trái”.'),
    ]
    return dict(unit=6,key='mia5:learn:en-u06-v1',legacyKey='mia5:learn:en-u06-preview-v1',legacyWords=[r.replace(' ','-') for r in CORE],intro='Phòng học, tầng và chỉ đường: chọn từng nhóm nhỏ để nghe, đọc theo rồi thử nhớ.',groups=[
        dict(id='rooms',name='Phòng học',tip='Where is/Where’s the…? — It is/It’s on the…floor. Computer nhấn âm thứ hai: com-PU-ter.'),
        dict(id='floors',name='Các tầng',tip='Ground floor là tầng trệt; first floor là tầng ngay phía trên. Không dùng hai tên này cho cùng một tầng. Vị trí dùng on the + tầng + floor.'),
        dict(id='directions',name='Chỉ đường',tip='up-STAIRS và down-STAIRS nhấn âm sau. Đi lên/xuống phụ thuộc nơi bắt đầu. Could you tell me the way to…please? là cách hỏi lịch sự.'),
    ],words=words,dialogues=dialogues,exercises=exercises)


def render_study():return render(data(),picture)
