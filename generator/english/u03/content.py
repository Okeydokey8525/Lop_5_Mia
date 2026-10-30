"""Original nationalities and personality practice, verified against pages 22–27."""
from english.practice import TESTS, mc, text, match, reorder, tf, based, picture as image, field, listen, assemble

COUNTRIES={'Australia':'Australian','Malaysia':'Malaysian','America':'American','Japan':'Japanese','Britain':'British'}
TRAITS={'friendly':'thân thiện','helpful':'hay giúp đỡ','clever':'thông minh','active':'năng động'}
PROFILES=[
 dict(name='Alex',pronoun='He',country='Australia',trait='active',hair='short',eyes='big'),
 dict(name='Yuki',pronoun='She',country='Japan',trait='helpful',hair='long',eyes='big'),
 dict(name='Adam',pronoun='He',country='Malaysia',trait='clever',hair='short',eyes='big'),
 dict(name='Lucy',pronoun='She',country='America',trait='friendly',hair='long',eyes='big'),
 dict(name='Tom',pronoun='He',country='Britain',trait='helpful',hair='short',eyes='big'),
 dict(name='Grace',pronoun='She',country='Australia',trait='active',hair='long',eyes='big'),
]


def nationality(p):return COUNTRIES[p['country']]
def card(p):return f"Name: {p['name']}\nPronoun: {p['pronoun'].lower()}\nCountry: {p['country']}\nNationality: {nationality(p)}\nPersonality: {p['trait']}\nHair: {p['hair']}\nEyes: {p['eyes']}"
def passage(p):return f"This is my friend {p['name']}. {p['pronoun']} is from {p['country']}. {p['pronoun']} is {nationality(p)}. {p['pronoun']} is {p['trait']}. {p['pronoun']} has {p['hair']} hair and {p['eyes']} eyes."
def picture(name,width=320):return image('u03',name,{'friendly':'Các bạn chào đón một bạn mới','helpful':'Bạn nhỏ giúp nhặt sách bị rơi','clever':'Bạn nhỏ giải câu đố xếp hình','active':'Bạn nhỏ chơi bóng rổ'}[name],width)
def nat_options():return list(COUNTRIES.values())[:4]
def nat_answer(p):return p['pronoun']+' is '+nationality(p)+'.'
def trait_answer(p):return p['pronoun']+' is '+p['trait']+'.'


def warmup():
 return [
 mc('Which word means “quốc tịch”?',['nationality','address','food','sport'],'nationality','Nationality nghĩa là quốc tịch.'),
 mc('A pupil is from Japan. The pupil is ___.',nat_options(),COUNTRIES['Japan'],'Japan là nước Nhật; quốc tịch là Japanese.'),
 text('Complete: Austra _ ian. Write the whole word.',COUNTRIES['Australia'],'Australia → Australian.'),
 mc('She is from Malaysia. She is ___.',nat_options(),COUNTRIES['Malaysia'],'Malaysia → Malaysian.'),
 match(list(COUNTRIES.items())[:3],'Australia → Australian; Malaysia → Malaysian; America → American.'),
 text('Complete: What nationality ___ he?','is','What nationality is he?'),
 mc('Which word means “thân thiện”?',list(TRAITS),'friendly','Friendly nghĩa là thân thiện.',2),
 reorder('He is American.','He is + quốc tịch.'),
 mc('A: What is she like? B: ___.',['She is helpful.','She is from Japan.','Her name is Yuki.','She is Japanese.'],'She is helpful.','What is she like? hỏi tính cách.',2),
 text('Complete: He is from ___. He is Australian.','Australia','Australian là quốc tịch của người Australia.'),
 match(list(TRAITS.items())[:3],'Friendly: thân thiện; helpful: hay giúp đỡ; clever: thông minh.',2),
 reorder('What nationality is she?','What nationality is she? hỏi quốc tịch.'),
 tf([('Active describes personality.',True),('Japanese is a type of home.',False)],'Active nói tính cách; Japanese là quốc tịch.',2),
 text('Write the full form of “She’s”.','She is','She’s = She is.',2),
 based(text('Write a full sentence about Alex’s nationality. Start with “He”.',nat_answer(PROFILES[0]),f"Alex: {nationality(PROFILES[0])}.",3),card(PROFILES[0])),
 based(tf([('Yuki is Japanese.',True),('Yuki is active.',False)],f"Yuki: {nationality(PROFILES[1])}; {PROFILES[1]['trait']}.",3),card(PROFILES[1])),
 based(text('What is Lucy like? Write a full sentence starting with “She”.',trait_answer(PROFILES[3]),f"Lucy: {PROFILES[3]['trait']}.",3),card(PROFILES[3])),
 mc('Which question asks about personality?',['What is he like?','What nationality is he?','Where is he from?','What is his name?'],'What is he like?','What is he like? hỏi tính cách, không hỏi quốc tịch.',3),
 ]


def vocabulary():
 qs=[]
 scenes=[('friendly','The pupils smile and welcome a new friend.'),('helpful','The girl helps a classmate pick up dropped books.'),('clever','The pupil solves the shape puzzle correctly.'),('active','The girl runs and plays basketball.')]
 for word,context in scenes:
  qs.append(mc(context+' Choose the matching word.',list(TRAITS),word,f"Ngữ cảnh minh họa {word}: {TRAITS[word]}.",2,picture(word)))
 qs += [
 text('Complete: J a p a n _ s e. Write the whole word.','Japanese','Japanese viết có e trước s.'),
 match([('Australia','nước Úc'),('Japan','nước Nhật Bản'),('Malaysia','nước Malaysia')],'Ghép tên nước với nghĩa tiếng Việt.'),
 mc('Which word means “người Mỹ / có quốc tịch Mỹ”?',nat_options(),'American','American là quốc tịch Mỹ.'),
 text('Complete: h e l p _ u l. Write the whole word.','helpful','Helpful có chữ f.',2),
 match([('Britain','British'),('America','American'),('Japan','Japanese')],'Britain → British; America → American; Japan → Japanese.'),
 tf([('Friendly means “thân thiện”.',True),('Clever means “địa chỉ”.',False)],'Clever nghĩa là thông minh; address mới là địa chỉ.',2),
 text('Complete: She is from Malaysia. She is ___.','Malaysian','Malaysia → Malaysian.'),
 reorder('He is from Australia.','From + tên nước.'),
 mc('Which pair is correct?',['Japan – Japanese','Japan – Australian','Malaysia – American','Australia – British'],'Japan – Japanese','Nước Nhật: Japan; quốc tịch: Japanese.'),
 match([('nationality','Japanese'),('personality','helpful'),('appearance','long hair')],'Phân biệt quốc tịch, tính cách và ngoại hình.',3),
 text('Write the full form: He’s clever.','He is clever.','He’s = He is.',3),
 based(text('Write Lucy’s country.',PROFILES[3]['country'],f"Lucy đến từ {PROFILES[3]['country']}.",3),card(PROFILES[3])),
 tf([('“Long hair” describes appearance.',True),('“Helpful” describes nationality.',False)],'Long hair nói ngoại hình; helpful nói tính cách.',3),
 based(text('Write a sentence about Adam’s personality. Start with “He”.',trait_answer(PROFILES[2]),f"Adam: {PROFILES[2]['trait']}.",3),card(PROFILES[2])),
 ];return qs


def dialogue():
 return [
 mc('A: What nationality is he? B: ___.',['He is Australian.','He is active.','He has short hair.','His name is Alex.'],'He is Australian.','Câu hỏi hỏi quốc tịch.'),
 text('Complete: What nationality is ___? She is Japanese.','she','Câu trả lời She tương ứng câu hỏi she.'),
 reorder('She is Malaysian.','She is + quốc tịch.'),
 mc('A: What is he like? B: ___.',['He is clever.','He is Malaysian.','He is from Malaysia.','His name is Adam.'],'He is clever.','What is he like? hỏi tính cách.',2),
 text('Complete: What is she ___? She is friendly.','like','Câu hỏi tính cách: What is she like?',2),
 match([('Where is she from?','She is from Japan.'),('What nationality is she?','She is Japanese.'),('What is she like?','She is helpful.')],'Phân biệt quê quán, quốc tịch và tính cách.'),
 text('Complete: He ___ American.','is','He đi với is.'),
 reorder('What is he like?','What is he like? hỏi tính cách.',2),
 based(mc('Which question matches “She is American.”?',['What nationality is she?','What is she like?','What is her name?','What is her favourite food?'],'What nationality is she?','American là quốc tịch.'),card(PROFILES[3])),
 text('Rewrite in full: What’s she like?','What is she like?','What’s = What is.',2),
 based(text('Answer “Where is Tom from?” Start with “He”.',f"He is from {PROFILES[4]['country']}.",f"Tom: {PROFILES[4]['country']}.",2),card(PROFILES[4])),
 based(reorder(trait_answer(PROFILES[1]),'Dùng tính cách trong thẻ Yuki.',2),card(PROFILES[1])),
 tf([('“What’s he like?” asks about personality.',True),('“What nationality is he?” asks about his favourite food.',False)],'Personality: tính cách; nationality: quốc tịch.',2),
 based(text('Answer “What nationality is Grace?” Start with “She”.',nat_answer(PROFILES[5]),f"Grace: {nationality(PROFILES[5])}.",2),card(PROFILES[5])),
 based(text('Write a full answer about Adam’s personality. Start with “He”.',trait_answer(PROFILES[2]),f"Adam: {PROFILES[2]['trait']}.",3),card(PROFILES[2])),
 based(match([('Name',PROFILES[1]['name']),('Nationality',nationality(PROFILES[1])),('Personality',PROFILES[1]['trait'])],'Ghép ba thông tin từ thẻ Yuki.',3),card(PROFILES[1])),
 mc('Choose the correct question.',['What nationality is she?','What nationality she is?','What is nationality she?','What nationality are she?'],'What nationality is she?','Thứ tự What nationality + is + she?',3),
 text('Rewrite in full: She’s friendly and helpful.','She is friendly and helpful.','She’s = She is; giữ cả hai tính cách.',3),
 ]


def reading():
 qs=[]
 for p in PROFILES[:2]:
  qs.extend(based(q,passage(p)) for q in [
   text('Write the friend’s name.',p['name'],f"Bài đọc giới thiệu {p['name']}.",3),
   mc('What nationality is '+p['name']+'?',nat_options(),nationality(p),f"Bài đọc ghi {nationality(p)}.",3),
   text('Write the country.',p['country'],f"From {p['country']}.",3),
   mc('Which word describes the personality?',list(TRAITS),p['trait'],f"Bài đọc ghi {p['trait']}.",3),
  ])
 for p in PROFILES[2:4]:
  qs.extend(based(q,passage(p)) for q in [
   match([('Name',p['name']),('Nationality',nationality(p)),('Personality',p['trait'])],'Đọc và ghép ba thông tin đúng.',3),
   tf([(p['name']+' has '+p['hair']+' hair.',True),(p['name']+' is Japanese.',False)],f"{p['name']}: {p['hair']} hair; {nationality(p)}.",3),
   text('Complete using the passage: '+p['pronoun']+' is ___. Write the personality word.',p['trait'],f"Tính cách: {p['trait']}.",3),
  ])
 cards='\n\n'.join(card(p) for p in PROFILES)
 def find(**facts):
  rows=[p for p in PROFILES if all(p[k]==v for k,v in facts.items())];assert len(rows)==1;return rows[0]['name']
 qs.extend(based(q,cards) for q in [
  text('Who is Australian and has long hair? Write the name.',find(country='Australia',hair='long'),'Grace khớp cả Australia và long hair.',3),
  text('Who is helpful and from Britain? Write the name.',find(trait='helpful',country='Britain'),'Tom khớp cả helpful và Britain.',3),
  tf([('Alex and Grace are both Australian.',all(nationality(p)=='Australian' for p in [PROFILES[0],PROFILES[5]])),('Yuki and Tom are both Japanese.',all(nationality(p)=='Japanese' for p in [PROFILES[1],PROFILES[4]]))],'Alex/Grace đều Australian; Tom là British, Yuki là Japanese.',3),
  text('Write a full sentence about Lucy’s nationality and personality. Start with “She is”, nationality first.',f"She is {nationality(PROFILES[3])} and {PROFILES[3]['trait']}.",'Lucy: American và friendly.',3),
 ]);return qs


def writing():
 p=PROFILES[1]
 return [
 text('Complete: She ___ Japanese.','is','She đi với is.'),
 reorder('He is from Malaysia.','From + tên nước.'),
 text('Complete: What ___ is she? She is American.','nationality','American là quốc tịch.'),
 reorder('She is friendly.','She is + tính cách.',2),
 text('Complete: He is ___ Australia.','from','Dùng from trước tên nước.'),
 mc('Choose the correct sentence.',['He is helpful.','He are helpful.','He helpful is.','He am helpful.'],'He is helpful.','He is + tính cách.',2),
 text('Complete: What is he ___? He is active.','like','What is he like? hỏi tính cách.',2),
 match([('He','is clever.'),('I','am Japanese.'),('She has','long hair.')],'He is; I am; She has.',2),
 text('Rewrite in full: He’s Australian.','He is Australian.','He’s = He is.'),
 reorder('What nationality is he?','What nationality is he?'),
 text('Complete: She has long ___.','hair','Long hair: tóc dài.',3),
 based(reorder(nat_answer(p),'Dùng quốc tịch từ thẻ.',2),card(p)),
 text('Rewrite with spaces: Sheishelpful.','She is helpful.','Tách She / is / helpful.',2),
 mc('Which sentence uses a nationality?',['She is American.','She is friendly.','She has long hair.','She is active.'],'She is American.','American là quốc tịch.'),
 based(text('Write Yuki’s country sentence. Start with “She is from”.',f"She is from {p['country']}.",f"Country: {p['country']}.",3),card(p)),
 based(text('Write Yuki’s nationality sentence. Start with “She”.',nat_answer(p),f"Nationality: {nationality(p)}.",3),card(p)),
 based(text('Write Yuki’s personality sentence. Start with “She”.',trait_answer(p),f"Personality: {p['trait']}.",3),card(p)),
 based(text('Write Yuki’s appearance sentence. Start with “She has” and include hair and eyes, hair first.',f"She has {p['hair']} hair and {p['eyes']} eyes.",f"Hair: {p['hair']}; Eyes: {p['eyes']}.",3),card(p)),
 ]


def listening(index):
 a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
 return [
 listen('Listen and choose the nationality.',nat_answer(a),[field('Nationality:',nationality(a),list(COUNTRIES.values()))]),
 listen('Listen and choose the personality.',trait_answer(b),[field('Personality:',b['trait'],list(TRAITS))],2),
 listen('Listen. Where is '+b['name']+' from?',f"This is {b['name']}. {b['pronoun']} is from {b['country']}.",[field('Country:',b['country'],list(COUNTRIES))]),
 listen('Listen. What is '+c['name']+' like?',f"This is {c['name']}. {trait_answer(c)}",[field('Personality:',c['trait'],list(TRAITS))],2),
 listen('Listen and choose the nationality and personality.',f"This is my friend {a['name']}. {a['pronoun']} is from {a['country']}. {nat_answer(a)} {trait_answer(a)}",[field('Nationality:',nationality(a),list(COUNTRIES.values())),field('Personality:',a['trait'],list(TRAITS))],3),
 listen('Listen and write the nationality and personality.',f"This is {c['name']}. {c['pronoun']} is from {c['country']}. {nat_answer(c)} {trait_answer(c)}",[field('Nationality:',nationality(c)),field('Personality:',c['trait'])],3),
 ]


def build_tests():
 written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
 mixed=[written[1][0],written[0][1],written[4][2],written[2][5],written[1][3],written[4][1],written[2][3],written[1][5],
        written[4][8],written[0][10],written[1][11],written[2][10],written[3][12],written[4][11],
        written[3][14],written[3][15],written[4][17],written[3][16]]
 import copy
 return [assemble(copy.deepcopy(qs),listening(i)) for i,qs in enumerate(written+[mixed])]
