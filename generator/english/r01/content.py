"""Original cross-unit Review 1, verified printed pages 40–43 (Units 1–5)."""
from english.practice import mc,text,match,reorder,tf,based,field,listen,assemble
from english.u01.content import picture as first_picture
from english.u02.content import picture as home_picture
from english.u03.content import picture as trait_picture
from english.u04.content import picture as activity_picture
from english.u05.content import picture as job_picture

COUNTRIES={'Australia':'Australian','Japan':'Japanese','Malaysia':'Malaysian','America':'American'}
JOBS={'writer':'write stories','reporter':'report the news','gardener':'grow flowers','teacher':'teach children'}
CORE=['dolphin','house','friendly','writer']
PROFILES=[
 dict(name='An',country='Australia',home='house',address='21 Rose Street',colour='pink',trait='friendly',free='playing the violin',job='writer'),
 dict(name='Linh',country='Japan',home='flat',address='36 Green Street',colour='blue',trait='helpful',free='watering the flowers',job='gardener'),
 dict(name='Minh',country='Malaysia',home='house',address='18 Lake Street',colour='red',trait='clever',free='surfing the Internet',job='reporter'),
 dict(name='Mai',country='America',home='flat',address='42 Hill Street',colour='yellow',trait='active',free='going for a walk',job='teacher'),
 dict(name='Nam',country='Japan',home='house',address='15 Green Street',colour='pink',trait='active',free='watering the flowers',job='writer'),
 dict(name='Hoa',country='Australia',home='flat',address='60 Rose Street',colour='blue',trait='friendly',free='playing the violin',job='reporter'),
]


def picture(name,width=320):
    fn={'dolphin':first_picture,'house':home_picture,'friendly':trait_picture,'writer':job_picture}[name]
    return fn(name,width)


def nationality(p):return COUNTRIES[p['country']]
def reason(p):return JOBS[p['job']]
def card(p):return f"Name: {p['name']} · Grade: 5 · Country: {p['country']} · Home: {p['home']} · Address: {p['address']} · Colour: {p['colour']} · Personality: {p['trait']} · Free time: {p['free']} · Future job: {p['job']} · Reason: {reason(p)}."
def passage(p):return f"I am {p['name']}. I am in Grade 5. I am {nationality(p)}. I live in a {p['home']} at {p['address']}. My favourite colour is {p['colour']}. I am {p['trait']}. I like {p['free']}. I would like to be a {p['job']} because I would like to {reason(p)}."
def tag(q,*units):q['sourceUnits']=list(units);return q
def shown(q,p,*units):return tag(based(q,card(p)),*units)


def written(index,kind):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    if kind==3:
        result=[]
        for p in [a,b,c]:
            result.extend(tag(based(q,passage(p)),u) for q,u in [
                (text('Write the speaker’s name.',p['name'],'Đọc tên trong bài.',1),1),
                (text('Write the nationality, not the country.',nationality(p),'Quốc tịch lấy từ tên nước.',1),3),
                (text('Write the full address.',p['address'],'Địa chỉ giả định từ bài đọc.',1),2),
                (text('Write the free-time activity in the -ing form.',p['free'],'Sau like là cụm V-ing.',2),4),
                (mc('What would the speaker like to be?',list(JOBS),p['job'],'Tìm would like to be.',2),5),
                (tf([(f"The speaker likes {p['free']}.",True),(f"The speaker would like to {JOBS[next(j for j in JOBS if j!=p['job'])]}.",False)],'Đọc cả sở thích và lý do nghề nghiệp.',3),5)])
        return result
    if kind==4:
        qs=[]
        for p in [a,b,c]:
            qs += [shown(text('Write one sentence: name. Start with I am.',f"I am {p['name']}.",'I am + tên.',1),p,1),
                   shown(text('Write one sentence: address. Start with I live at.',f"I live at {p['address']}.",'At + địa chỉ cụ thể.',1),p,2),
                   shown(text('Write one sentence: nationality. Start with I am.',f"I am {nationality(p)}.",'I am + quốc tịch.',1),p,3),
                   shown(text('Write one sentence: free time. Start with I like.',f"I like {p['free']}.",'Like + V-ing.',2),p,4),
                   shown(text('Write one sentence: future job. Start with I would.',f"I would like to be a {p['job']}.",'Would like to be a + nghề.',2),p,5),
                   shown(text('Answer Why? Start with Because I would.',f"Because I would like to {reason(p)}.",'Because + I would like to + việc làm.',3),p,5)]
        qs[0]=shown(reorder(f"I am {a['name']}.",'Sắp câu giới thiệu theo đúng tên.'),a,1)
        qs[2]=shown(mc('Choose the correct nationality sentence.',['I am '+v+'.' for v in COUNTRIES.values()],'I am '+nationality(a)+'.','Đọc tên nước và chọn đúng quốc tịch.'),a,3)
        return qs
    if kind==2:return [
        shown(mc('Can you tell me your name?',[f"I am {p['name']}." for p in PROFILES[:4]],f"I am {a['name']}.",'Đọc tên trong thẻ.'),a,1) if index<4 else shown(text('Can you tell me your name? Start with I am.',f"I am {a['name']}.",'Dùng tên của thẻ.'),a,1),
        shown(text('What is your address? Start with It is.',f"It is {a['address']}.",'It is + địa chỉ.'),a,2),
        tag(reorder('Do you live in a flat?','Do you live in…?'),2),
        shown(text('What nationality are you? Start with I am.',f'I am {nationality(b)}.','Phân biệt tên nước và quốc tịch.'),b,3),
        shown(text('What are you like? Start with I am.',f"I am {a['trait']}.",'Hỏi tính cách, không hỏi sở thích.'),a,3),
        shown(text('What do you like doing? Start with I like.',f"I like {b['free']}.",'Sau like dùng V-ing.'),b,4),
        tag(mc('Which question asks about a future job?',['What would you like to be?','What is your address?','What nationality is he?','What is she like?'],'What would you like to be?','Would like to be hỏi ước mơ.'),5),
        shown(text('Why would you like this job? Start with Because.',f'Because I would like to {reason(c)}.','Lý do nghề nghiệp trong thẻ.'),c,5),
        tag(text('Complete: Do you live in a house? Yes, I ___.','do','Yes, I do.',2),2),
        tag(reorder('What do you like doing in your free time?','What do you like doing…?',2),4),
        tag(text('Rewrite in full: I’d like to be a writer.','I would like to be a writer.','I’d = I would trong ngữ cảnh này.',2),5),
        tag(match([('Where do you live?','In a flat.'),('What is he like?','He is helpful.'),('What is your favourite animal?','It is a dolphin.')],'Ghép đúng chủ đề hỏi.',2),1,2,3),
        shown(text('Answer about colour, starting with It is.',f"It is {c['colour']}.",'Đúng màu trong thẻ.',2),c,1),
        tag(tf([('What is she like? asks about personality.',True),('What nationality is she? asks for an address.',False)],'Phân biệt tính cách, quốc tịch và địa chỉ.',3),2,3),
        shown(text('Write two sentences: home then address. Start each with I live.',f"I live in a {a['home']}. I live at {a['address']}.",'In + loại nhà; at + địa chỉ.',3),a,2),
        shown(text('Write two sentences: free time then future job. Start with I like and then I would.',f"I like {b['free']}. I would like to be a {b['job']}.",'Giữ V-ing và would like to be.',3),b,4,5),
        tag(text('Rewrite in full: He’s Japanese.','He is Japanese.','He’s = He is.',3),3),
        shown(text('Write one sentence about the future job and reason. Start with I would and use because.',f"I would like to be a {c['job']} because I would like to {reason(c)}.",'Kết hợp đúng nghề và lý do trong cùng thẻ.',3),c,5)]
    qs=[
        tag(mc('Choose the animal in the picture.',['dolphin','house','writer','flat'],'dolphin','Dolphin là cá heo.',1,picture('dolphin')),1),
        shown(text('Write the nationality only.',nationality(a),'Dùng quốc tịch tương ứng tên nước.'),a,3),
        shown(mc('Which home is in this card?',['house','flat','tower','building'],a['home'],'Đọc Home.'),a,2),
        shown(text('Write the favourite colour only.',a['colour'],'Đọc Colour.'),a,1),
        tag(match([('house','ngôi nhà'),('helpful','hay giúp đỡ'),('writer','nhà văn')],'Ghép từ của các Unit khác nhau.'),2,3,5),
        tag(text('Complete: I live ___ 21 Rose Street.','at','At + địa chỉ cụ thể.'),2),
        shown(text('Write the free-time phrase in the -ing form.',b['free'],'Đọc Free time trong thẻ.'),b,4),
        shown(mc('Which future job is in the card?',list(JOBS),c['job'],'Đọc Future job.'),c,5),
        tag(text('Complete: She ___ helpful.','is','She is + tính cách.',2),3),
        tag(reorder('I like watering the flowers.','Like + V-ing.',2),4),
        shown(text('Write only the job reason phrase.',reason(c),'Lý do từ đúng thẻ.',2),c,5),
        tag(mc('What do you do at the weekend?',['I usually read stories.','I am Japanese.','It is 21 Rose Street.','I am ten.'],'I usually read stories.','Đáp hoạt động cuối tuần.',2),4),
        tag(text('Complete: I would like to ___ a teacher.','be','Would like to be + nghề.',2),5),
        tag(tf([('Australian is a nationality.',True),('Friendly is a nationality.',False)],'Phân biệt quốc tịch và tính cách.',3),3),
        shown(text('Write a complete nationality sentence, starting with I am.',f'I am {nationality(b)}.','Đúng quốc tịch của thẻ.',3),b,3),
        shown(text('Write a full address sentence starting with My address is.',f"My address is {c['address']}.",'My address is + địa chỉ giả định.',3),c,2),
        based(tag(match([(p['name'],p['address']) for p in [a,b,c]],'Ghép mỗi bạn với đúng địa chỉ giả định.',3),1,2),'\n'.join(card(p) for p in [a,b,c])),
        shown(text('Write the full job sentence, starting with I would.',f"I would like to be a {a['job']}.",'Dùng đúng nghề trong thẻ.',3),a,5)]
    if kind==1:
        qs[:4]=[tag(mc('Choose the word for this picture.',CORE,k,'Đọc đúng chủ thể; friendly có hành động chào bạn mới.',1,picture(k)),[1,2,3,5][i]) for i,k in enumerate(CORE)]
        qs[8]=tag(text('Complete: I like ___ the violin. Use play.','playing','Play → playing sau like.',2),4)
        qs[9]=tag(mc('An actor performs plays. Which workplace matches this description?',['theatre','hospital','garden','school'],'theatre','Actor và theatre có trong phần mở rộng trang 42–43.',3),5)
        qs[12]=tag(text('Complete the firefighter’s action: put out ___.','fires','Put out fires: dập lửa, phần mở rộng trang 42–43.',3),5)
    return qs


def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    return [tag(listen('Listen and choose the favourite colour.',f"My favourite colour is {a['colour']}.",[field('Colour:',a['colour'],['pink','blue','red','yellow'])]),1),
        tag(listen('Listen and choose the home.',f"I live in a {b['home']} at {b['address']}.",[field('Home:',b['home'],['house','flat','building','tower'])]),2),
        tag(listen('Listen and choose the personality.',f"My friend is {c['trait']}.",[field('Personality:',c['trait'],['friendly','helpful','clever','active'])],2),3),
        tag(listen('Listen and choose the free-time activity.',f"I like {a['free']} in my free time.",[field('Activity:',a['free'],[p['free'] for p in PROFILES[:4]])],2),4),
        tag(listen('Listen for the future job and reason.',f"I am {b['name']}. I would like to be a {b['job']} because I would like to {reason(b)}.",[field('Job:',b['job'],list(JOBS)),field('Reason:',reason(b),list(JOBS.values()))],3),5),
        tag(listen('Listen and write nationality and address.',f"I am {c['name']}. I am {nationality(c)}. I live at {c['address']}.",[field('Nationality:',nationality(c)),field('Address:',c['address'])],3),2,3)]


def build_tests():
    tests=[]
    for i in range(6):
        qs=written(i,i) if i<5 else [written(i,k%5)[k] for k in range(18)]
        tests.append(assemble(qs,listening(i)))
    return tests
