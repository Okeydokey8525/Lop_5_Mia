"""Original free-time practice derived from the verified scope on pages 28–33."""
from english.practice import mc,text,match,reorder,tf,based,picture as image,field,listen,assemble

ACTIVITIES={
 'play the violin':('playing the violin','plays the violin','chơi đàn vi-ô-lông'),
 'surf the Internet':('surfing the Internet','surfs the Internet','lướt Internet'),
 'go for a walk':('going for a walk','goes for a walk','đi dạo'),
 'water the flowers':('watering the flowers','waters the flowers','tưới hoa'),
 'read stories':('reading stories','reads stories','đọc truyện'),
 'ride my bike':('riding my bike','rides a bike','đạp xe'),
 'listen to music':('listening to music','listens to music','nghe nhạc'),
}
CORE=list(ACTIVITIES)[:4]
FREQUENCIES={'always':'luôn luôn','usually':'thường thường','often':'thường xuyên','sometimes':'thỉnh thoảng','rarely':'hiếm khi','never':'không bao giờ'}
PROFILES=[
 dict(name='An',pronoun='He',free='play the violin',weekend='read stories',frequency='always'),
 dict(name='Linh',pronoun='She',free='go for a walk',weekend='water the flowers',frequency='usually'),
 dict(name='Minh',pronoun='He',free='surf the Internet',weekend='ride my bike',frequency='often'),
 dict(name='Mai',pronoun='She',free='water the flowers',weekend='surf the Internet',frequency='sometimes'),
 dict(name='Nam',pronoun='He',free='go for a walk',weekend='listen to music',frequency='rarely'),
 dict(name='Hoa',pronoun='She',free='play the violin',weekend='go for a walk',frequency='never'),
]

def ing(action):return ACTIVITIES[action][0]
def like(p):return 'I like '+ing(p['free'])+' in my free time.'
def weekend(p):return 'I '+p['frequency']+' '+p['weekend']+' at the weekend.'
def third_weekend(p):return p['pronoun']+' '+p['frequency']+' '+ACTIVITIES[p['weekend']][1]+' at the weekend.'
def card(p):return f"Name: {p['name']}\nPronoun: {p['pronoun'].lower()}\nLikes: {ing(p['free'])}\nWeekend activity: {p['weekend']}\nFrequency: {p['frequency']}"
def passage(p):return f"My name is {p['name']}. I am in Grade 5. {like(p)} {weekend(p)}"
def picture(name,width=320):return image('u04',name.lower().replace(' ','-'),ACTIVITIES[name][2],width)
def options():return [ing(a) for a in CORE]

def warmup():return [
 mc('Which phrase means “chơi đàn vi-ô-lông”?',CORE,CORE[0],'Play the violin là chơi đàn vi-ô-lông.'),
 text('Complete: I like ___ the flowers. Use “water”.','watering','Sau like dùng dạng V-ing: watering.'),
 mc('What do you like ___ in your free time?',['doing','do','does','did'],'doing','Mẫu hỏi sở thích: What do you like doing…?'),
 reorder('I like going for a walk.','Like + going for a walk.'),
 match([(a,ACTIVITIES[a][2]) for a in CORE[:3]],'Ghép nghĩa: chơi đàn, lướt Internet và đi dạo.'),
 text('Complete the phrase for “lướt Internet”: surf the ___.','Internet','Cụm đúng là surf the Internet.'),
 mc('Which word means “luôn luôn”?',list(FREQUENCIES)[:4],'always','Always nghĩa là luôn luôn.',2),
 tf([('Watering the flowers is an activity.',True),('Never means “luôn luôn”.',False)],'Tưới hoa là hoạt động; never nghĩa là không bao giờ.',2),
 text('Complete: What do you do ___ the weekend?','at','Cụm theo sách: at the weekend.',2),
 reorder('I usually read stories at the weekend.','Usually đứng trước read.',2),
 mc('Choose the correct sentence.',['I like playing the violin.','I like play the violin.','I likes playing the violin.','I like plays the violin.'],'I like playing the violin.','I like + playing; I không đi với likes.'),
 based(text('Write the frequency word on Linh’s card.',PROFILES[1]['frequency'],f"Thẻ ghi Frequency: {PROFILES[1]['frequency']}.",2),card(PROFILES[1])),
 based(tf([('Minh likes surfing the Internet.',True),('Minh never rides a bike at the weekend.',False)],f"Minh thích {ing(PROFILES[2]['free'])}; tần suất cuối tuần là {PROFILES[2]['frequency']}.",3),passage(PROFILES[2])),
 match([('always','luôn luôn'),('rarely','hiếm khi'),('never','không bao giờ')],'Phân biệt ba mức tần suất.',2),
 based(text('Mai is speaking. Write the full free-time sentence, including “in my free time”.',like(PROFILES[3]),f"Likes: {ing(PROFILES[3]['free'])}; dùng I like…",3),card(PROFILES[3])),
 based(text('An is speaking. Write the full weekend sentence, including frequency.',weekend(PROFILES[0]),f"Always + {PROFILES[0]['weekend']} at the weekend.",3),card(PROFILES[0])),
 based(match([(p['name'],p['frequency']) for p in PROFILES[:3]],'Đối chiếu dòng Frequency của từng thẻ.',3),'\n\n'.join(card(p) for p in PROFILES[:3])),
 mc('Which question asks about a weekend routine?',['What do you do at the weekend?','What is your address?','What nationality is she?','What is your name?'],'What do you do at the weekend?','At the weekend xác định hoạt động cuối tuần.',3),
]

def vocabulary():
 qs=[mc('Look at the picture. Choose the activity.',CORE,a,f"Tranh minh họa {a}: {ACTIVITIES[a][2]}.",1,picture(a)) for a in CORE]
 return qs+[
 text('Write the -ing form of “play”.','playing','Play + ing = playing.'),
 text('Write the -ing form of “go”.','going','Go + ing = going.'),
 match([('read stories','đọc truyện'),('ride my bike','đạp xe'),('listen to music','nghe nhạc')],'Ghép đúng các hoạt động cuối tuần.',2),
 mc('Which phrase means “tưới hoa”?',CORE,'water the flowers','Water the flowers nghĩa là tưới hoa.'),
 match(list(FREQUENCIES.items())[:4],'Ghép từ chỉ tần suất với nghĩa.',2),
 mc('Which word means “hiếm khi”?',['always','never','rarely','usually'],'rarely','Rarely nghĩa là hiếm khi.',2),
 text('Complete: go for ___ walk.','a','Cụm đúng là go for a walk.'),
 text('Complete: play ___ violin.','the','Dùng the trước violin trong mẫu đã học.'),
 tf([('Usually comes before often in the frequency scale.',True),('Never means the same as always.',False)],'Thang trong sách: always, usually, often, sometimes, rarely, never.',2),
 reorder('I sometimes surf the Internet.','Sometimes đứng trước động từ surf.',2),
 based(text('Which activity does Nam rarely do at the weekend? Write the base phrase.',PROFILES[4]['weekend'],f"Thẻ Nam: {PROFILES[4]['frequency']} {PROFILES[4]['weekend']}.",3),card(PROFILES[4])),
 based(text('What does Hoa never do at the weekend? Write the base phrase.',PROFILES[5]['weekend'],f"Thẻ Hoa: never {PROFILES[5]['weekend']}.",3),card(PROFILES[5])),
 mc('Which phrase correctly follows “I like”?',['going for a walk','go for a walk','goes for a walk','went for a walk'],'going for a walk','Sau I like dùng going.',3),
 based(reorder(weekend(PROFILES[1]),'Sắp câu theo đúng tần suất và hoạt động của Linh.',3),card(PROFILES[1])),
 ]

def dialogue():return [
 mc('A: What do you like doing in your free time? B: ___.',['I like playing the violin.','My address is 14 Queen Street.','I am Japanese.','My name is An.'],'I like playing the violin.','Hỏi sở thích lúc rảnh, trả lời I like + V-ing.'),
 text('Complete: I ___ going for a walk in my free time.','like','I like + going.'),
 reorder('What do you like doing in your free time?','What do you like doing + in your free time?'),
 mc('A: What do you do at the weekend? B: ___.',['I often read stories.','I am in Grade 5.','It is a dolphin.','My name is Mai.'],'I often read stories.','Often read stories là hoạt động và tần suất cuối tuần.',2),
 text('Complete: What do you ___ at the weekend?','do','What do you do…? hỏi hoạt động.',2),
 match([('What do you like doing?','I like playing the violin.'),('What do you do at the weekend?','I usually read stories.'),('Do you like going for a walk?','Yes, I do.')],'Ghép câu hỏi sở thích, thói quen và câu có/không.'),
 text('Complete: Do you like ___ the flowers? Use “water”.','watering','Do you like + V-ing.'),
 mc('A: Do you like surfing the Internet? B: Yes, ___.',['I do','I does','I am','I is'],'I do','Do you…? → Yes, I do.'),
 based(text('An is speaking. Answer with the frequency word only.',PROFILES[0]['frequency'],'Thẻ An ghi always.',2),card(PROFILES[0])),
 based(text('Linh is speaking. Complete: I like ___.',ing(PROFILES[1]['free']),f"Likes: {ing(PROFILES[1]['free'])}."),card(PROFILES[1])),
 reorder('Do you like playing the violin?','Do you like + playing the violin?'),
 based(mc('Minh is speaking. Choose the reply about the weekend.',[weekend(PROFILES[2]),weekend(PROFILES[0]),weekend(PROFILES[1]),weekend(PROFILES[3])],weekend(PROFILES[2]),f"Minh: {PROFILES[2]['frequency']} {PROFILES[2]['weekend']}.",2),card(PROFILES[2])),
 text('Complete: What ___ your brother like doing?','does','Your brother là ngôi thứ ba số ít; dùng does.'),
 text('Complete: She ___ going for a walk. Use “like”.','likes','She đi với likes.'),
 based(text('Write one full sentence about Mai’s weekend. Start with “She”.',third_weekend(PROFILES[3]),'She + sometimes + surfs the Internet at the weekend.',3),card(PROFILES[3])),
 based(text('Hoa is speaking. Give a full answer about the weekend.',weekend(PROFILES[5]),'Hoa: never go for a walk at the weekend.',3),card(PROFILES[5])),
 tf([('“What do you like doing?” asks about a favourite activity.',True),('“What do you do at the weekend?” asks for an address.',False)],'Phân biệt câu hỏi sở thích/thói quen với địa chỉ.',3),
 based(text('Nam is speaking. Answer about free time; include “in my free time”.',like(PROFILES[4]),f"Nam thích {ing(PROFILES[4]['free'])}.",3),card(PROFILES[4])),
]

def reading():
 qs=[]
 for p in PROFILES[:2]:
  qs.extend(based(q,passage(p)) for q in [
   text('Write the pupil’s name.',p['name'],f"Bài đọc ghi tên {p['name']}.",3),
   mc('What does '+p['name']+' like doing?',options(),ing(p['free']),f"Bài đọc: {like(p)}",3),
   text('Write the weekend frequency word.',p['frequency'],f"Tần suất: {p['frequency']}.",3),
   text('Write the weekend activity as a base phrase.',p['weekend'],f"Hoạt động: {p['weekend']}.",3),
  ])
 for p in PROFILES[2:4]:
  qs.extend(based(q,passage(p)) for q in [
   match([('Name',p['name']),('Likes',ing(p['free'])),('Frequency',p['frequency'])],'Ghép đúng dữ kiện trong đoạn đọc.',3),
   tf([(p['name']+' likes '+ing(p['free'])+'.',True),(p['name']+' always reads stories at the weekend.',False)],f"{like(p)} {weekend(p)}",3),
   text('Complete the weekend sentence: I '+p['frequency']+' ___ at the weekend.',p['weekend'],f"Thẻ ghi {p['weekend']}.",3),
  ])
 cards='\n\n'.join(card(p) for p in PROFILES)
 def find(**facts):
  rows=[p['name'] for p in PROFILES if all(p[k]==v for k,v in facts.items())];assert len(rows)==1;return rows[0]
 qs.extend(based(q,cards) for q in [
  text('Who likes playing the violin and always reads stories? Write the name.',find(free='play the violin',frequency='always'),'An khớp cả Likes: playing the violin và Frequency: always.',3),
  text('Who likes going for a walk and rarely listens to music? Write the name.',find(free='go for a walk',frequency='rarely'),'Nam khớp cả sở thích và thói quen cuối tuần.',3),
  tf([('An and Hoa both like playing the violin.',all(p['free']=='play the violin' for p in [PROFILES[0],PROFILES[5]])),('Linh and Mai both usually water the flowers.',all(p['weekend']=='water the flowers' and p['frequency']=='usually' for p in [PROFILES[1],PROFILES[3]]))],'An/Hoa cùng thích đàn; Mai sometimes surf the Internet, không usually water the flowers.',3),
  text('Linh is speaking. Write the full weekend sentence.',weekend(PROFILES[1]),f"Dùng {PROFILES[1]['frequency']} + {PROFILES[1]['weekend']}.",3),
 ]);return qs

def writing():return [
 text('Complete: I like ___ the violin. Use “play”.','playing','Like + V-ing.'),
 reorder('I like watering the flowers.','I like + watering the flowers.'),
 text('Complete: I often ___ stories. Use “read”.','read','I + often + động từ nguyên dạng.',2),
 reorder('I always listen to music.','Always đứng trước listen.',2),
 mc('Choose the correct sentence.',['I usually water the flowers.','I water usually the flowers.','I usually waters the flowers.','I usually watering the flowers.'],'I usually water the flowers.','I + usually + water.',2),
 text('Complete: I like going ___ a walk.','for','Go for a walk.'),
 match([('play','the violin'),('surf','the Internet'),('water','the flowers')],'Ghép ba cụm hoạt động.'),
 text('Write the -ing form of “surf”.','surfing','Surf + ing = surfing.'),
 text('Rewrite with spaces: IoftensurftheInternet.','I often surf the Internet.','Tách từ theo đúng mẫu.',2),
 reorder('What do you do at the weekend?','Hỏi hoạt động cuối tuần.',2),
 text('Complete: He ___ the flowers. Use “water”.','waters','He + waters.'),
 text('Complete: She ___ for a walk. Use “go”.','goes','She + goes.'),
 based(text('An is speaking. Complete: I like ___.',ing(PROFILES[0]['free']),'Likes: playing the violin.'),card(PROFILES[0])),
 based(reorder(weekend(PROFILES[3]),'Sắp theo thẻ Mai.',2),card(PROFILES[3])),
 based(text('Write one full sentence about Linh’s weekend. Start with “She”.',third_weekend(PROFILES[1]),'She + usually + waters the flowers at the weekend.',3),card(PROFILES[1])),
 based(text('Nam is speaking. Write the full free-time sentence, including “in my free time”.',like(PROFILES[4]),'Likes: going for a walk.',3),card(PROFILES[4])),
 based(text('Write one full sentence about Hoa’s weekend. Start with “She”.',third_weekend(PROFILES[5]),'She + never + goes for a walk at the weekend.',3),card(PROFILES[5])),
 based(text('Mai is speaking. Write the full weekend sentence.',weekend(PROFILES[3]),'I + sometimes + surf the Internet at the weekend.',3),card(PROFILES[3])),
]

def listening(index):
 a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
 return [
 listen('Listen and choose the free-time activity.',like(a),[field('Likes:',ing(a['free']),options())]),
 listen('Listen and choose the frequency word.',weekend(b),[field('Frequency:',b['frequency'],list(FREQUENCIES))],2),
 listen('Listen. What does '+b['name']+' like doing?',f"My name is {b['name']}. {like(b)}",[field('Likes:',ing(b['free']),options())]),
 listen('Listen and choose the weekend activity mentioned.',f"My name is {c['name']}. {weekend(c)}",[field('Activity:',c['weekend'],[p['weekend'] for p in PROFILES])],2),
 listen('Listen and choose the activity and frequency.',passage(a),[field('Likes:',ing(a['free']),options()),field('Frequency:',a['frequency'],list(FREQUENCIES))],3),
 listen('Listen and write the free-time activity and weekend frequency.',passage(c),[field('Likes:',ing(c['free'])),field('Frequency:',c['frequency'])],3),
 ]

def build_tests():
 import copy
 written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
 mixed=[written[1][0],written[4][0],written[0][4],written[2][3],written[1][3],written[4][6],written[1][6],written[0][6],written[2][8],written[4][9],written[3][10],written[1][12],written[2][12],written[4][11],written[3][14],written[3][15],written[4][16],written[3][16]]
 return [assemble(copy.deepcopy(qs),listening(i)) for i,qs in enumerate(written+[mixed])]
