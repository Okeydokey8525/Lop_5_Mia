"""Original home/address practice from verified Unit 2 scope."""
from english.practice import TESTS, mc, text, match, reorder, tf, based, picture as image, field, listen, assemble

HOMES=['house','flat','building','tower']
MEANINGS=['ngôi nhà','căn hộ','tòa nhà','tòa tháp']
PROFILES=[
 dict(name='An',home='house',number='14',street='Queen Street',near=True),
 dict(name='Linh',home='flat',number='26',street='Oxford Street',near=False),
 dict(name='Minh',home='tower',number='18',street='King Street',near=True),
 dict(name='Mai',home='building',number='32',street='London Street',near=False),
 dict(name='Nam',home='house',number='16',street='King Street',near=False),
 dict(name='Hoa',home='flat',number='19',street='Queen Street',near=True),
]


def address(p):return p['number']+' '+p['street']
def card(p):return f"Name: {p['name']}\nHome: {p['home']}\nAddress: {address(p)}\nSchool: {'near' if p['near'] else 'far from'} the home"
def passage(p):return f"Hello! My name is {p['name']}. I live in a {p['home']}. My address is {address(p)}. My home is {'near' if p['near'] else 'far from'} my school."
def picture(name,width=320):return image('u02',name,dict(zip(HOMES,MEANINGS))[name],width)
def reply(p):return 'Yes, I do.' if p['near'] else 'No, I do not.'


def warmup():
 return [
 mc('Which word means “ngôi nhà”?',HOMES,'house','House nghĩa là ngôi nhà.'),
 text('Complete: f l _ t. Write the whole word.','flat','Căn hộ là flat.'),
 mc('Do you ___ in this house?',['live','lives','living','is'],'live','Do you đi với động từ live.'),
 text('Complete: Yes, I ___.','do','Trả lời Do you…? bằng Yes, I do.'),
 match(list(zip(HOMES[:3],MEANINGS[:3])),'House: ngôi nhà; flat: căn hộ; building: tòa nhà.'),
 mc('Which word means “địa chỉ”?',['address','animal','colour','sport'],'address','Address nghĩa là địa chỉ.',2),
 tf([('A flat is a home.',True),('Street means “màu sắc”.',False)],'Flat là căn hộ; street là đường phố.',2),
 reorder('I live in a house.','I live in + a house.'),
 mc('What is your ___? It is 14 Queen Street.',['address','name','class','food'],'address','Số nhà và tên đường trả lời câu hỏi về address.',2),
 text('Complete: I live ___ 26 Oxford Street.','at','Dùng at trước địa chỉ cụ thể.',2),
 based(text('An is speaking. Write the house number only.',PROFILES[0]['number'],f"Địa chỉ ghi {address(PROFILES[0])}.",2),card(PROFILES[0])),
 reorder('Do you live in that flat?','Do you live in + that flat?'),
 based(tf([('Linh lives in a flat.',True),('Linh lives in Queen Street.',False)],f"Linh: flat; {address(PROFILES[1])}.",3),passage(PROFILES[1])),
 text('Write the full form of “don’t”.','do not','Don’t là dạng rút gọn của do not.'),
 based(text('Minh is speaking. Answer “What is your address?”. Start with “It”.',f"It is {address(PROFILES[2])}.",f"Thẻ của Minh ghi {address(PROFILES[2])}.",3),card(PROFILES[2])),
 based(match([(p['name'],address(p)) for p in PROFILES[:3]],'Ghép tên và địa chỉ từ đúng thẻ của từng bạn.',3),'\n\n'.join(card(p) for p in PROFILES[:3])),
 mc('Choose the correct address sentence.',['I live at 14 Queen Street.','I live on a house.','I live at a flat.','I live in at Queen Street.'],'I live at 14 Queen Street.','Dùng at trước số nhà và tên đường.',3),
 based(text('Mai is speaking. Write a sentence about the home. Start with “I live”.',f"I live in a {PROFILES[3]['home']}.",f"Home trong thẻ là {PROFILES[3]['home']}.",3),card(PROFILES[3])),
 ]


def vocabulary():
 qs=[mc('Look at the picture. Which word means a home with its own roof and garden?',['house','street','address','school'],'house','Ngôi nhà riêng có mái và vườn: house.',1,picture('house')),
 mc('Look inside the building. Which word means one home inside it?',['flat','street','colour','food'],'flat','Một căn hộ bên trong tòa nhà: flat.',1,picture('flat')),
 mc('Choose the word for the whole block of homes shown.',['building','street','sport','animal'],'building','Hình cho thấy toàn bộ tòa nhà: building.',1,picture('building')),
 mc('Choose the word for the very tall home shown.',['tower','street','food','class'],'tower','Tòa tháp cao là tower; tower cũng là một loại building.',1,picture('tower')),
 text('Complete: a d d r _ s s. Write the whole word.','address','Address viết có hai chữ d và hai chữ s.',2),
 match([('near','gần'),('far','xa'),('street','đường phố')],'Near = gần; far = xa; street = đường phố.',2),
 mc('Which word is a number?',['sixteen','flat','house','address'],'sixteen','Sixteen là số mười sáu.',3),
 text('Write 15 in English.','fifteen','15 viết là fifteen.',3),
 mc('Which word means 16?',['sixteen','sixty','six','sixty-six'],'sixteen','Sixteen là 16; sixty là 60.',3),
 text('Write the number for “eighteen”.','18','Eighteen = 18.',3),
 match([('fifteen','15'),('sixteen','16'),('nineteen','19')],'Ghép đúng số teen.',3),
 tf([('An address can include a house number.',True),('A street is a favourite animal.',False)],'Địa chỉ có thể gồm số nhà; street không phải con vật.',2),
 reorder('My home is near my school.','Near nói khoảng cách gần.',2),
 text('Complete: My home is far ___ my school.','from','Cụm đúng là far from.',2),
 based(text('Write the street name, including “Street”.',PROFILES[4]['street'],f"Thẻ của Nam ghi {address(PROFILES[4])}.",3),card(PROFILES[4])),
 based(tf([('Hoa’s house number is 19.',True),('Hoa’s home is far from school.',False)],f"Hoa: {address(PROFILES[5])}; near school.",3),card(PROFILES[5])),
 reorder('What is your address?','What is your address? hỏi địa chỉ.',3),
 text('Write the full form: It’s 16 King Street.','It is 16 King Street.','It’s = It is; giữ nguyên địa chỉ.',3),
 ];return qs


def dialogue():
 return [
 mc('A: Do you live in this house? B: Yes, ___.',['I do','I is','I am','I live'],'I do','Yes, I do. trả lời Do you…?'),
 text('A: Do you live in that flat? B: No, I ___.','do not','Câu trả lời phủ định dùng do not.',alternatives=["don't"]),
 mc('Which question asks about an address?',['What is your address?','What is your name?','What is your favourite sport?','What colour is it?'],'What is your address?','Address là địa chỉ.',2),
 reorder('Do you live in this building?','Do you live in + this building?'),
 text('Complete: What is ___ address?','your','Hỏi địa chỉ của bạn: your address.',2),
 mc('A: What is your address? B: ___.',['It is 18 King Street.','It is pink.','I am An.','It is football.'],'It is 18 King Street.','Đáp lại bằng số nhà và tên đường.',2),
 match([('Do you live in this flat?','Yes, I do.'),('What is your address?','It is 32 London Street.'),('What is your name?','My name is Mai.')],'Ghép đúng câu hỏi có/không, địa chỉ và tên.',2),
 text('The house is close to you. Complete: Do you live in ___ house?','this','This chỉ vật ở gần người nói.'),
 text('The tower is far from you. Complete: Do you live in ___ tower?','that','That chỉ vật ở xa người nói.'),
 reorder('No, I do not live in that tower.','No, I do not + live in that tower.'),
 based(text('An is speaking. Answer “Do you live near your school?” Use a short answer.',reply(PROFILES[0]),'Thẻ ghi near nên trả lời Yes, I do.',2),card(PROFILES[0])),
 based(mc('Linh is speaking. Which reply agrees with the card?',['I live in a flat.','I live in a house.','I live in a tower.','I live near my school.'],'I live in a flat.','Home: flat; School: far from the home.',2),card(PROFILES[1])),
 text('Rewrite in full: What’s your address?','What is your address?','What’s = What is.',2),
 based(reorder('It is '+address(PROFILES[3])+'.','Dùng địa chỉ trên thẻ.',2),card(PROFILES[3])),
 based(text('Nam is speaking. Answer “Do you live near your school?” Use a short answer.',reply(PROFILES[4]),'Thẻ ghi far from nên trả lời No, I do not.',3),card(PROFILES[4])),
 based(text('Hoa is speaking. Answer “Where do you live?” Start with “I live at”.',f"I live at {address(PROFILES[5])}.",f"Địa chỉ: {address(PROFILES[5])}.",3),card(PROFILES[5])),
 mc('Choose the correct question.',['Do you live in this flat?','Does you live in this flat?','Do you lives in this flat?','Is you live in this flat?'],'Do you live in this flat?','Do you + live + in…?',3),
 tf([('“What’s your address?” asks for a name only.',False),('“No, I don’t.” can answer “Do you live in that house?”.',True)],'Address hỏi địa chỉ; No, I don’t là câu trả lời phủ định phù hợp.',3),
 ]


def reading():
 qs=[]
 for p in PROFILES[:2]:
  other=PROFILES[2]
  qs.extend(based(q,passage(p)) for q in [
   mc('Which home does '+p['name']+' live in?',HOMES,p['home'],f"Bài đọc ghi a {p['home']}.",3),
   text('Write the house number only.',p['number'],f"Địa chỉ: {address(p)}.",3),
   text('Write the street name, including “Street”.',p['street'],f"Đường là {p['street']}.",3),
   tf([(p['name']+' lives in a '+p['home']+'.',True),(p['name']+' lives at '+address(other)+'.',False)],f"Đọc đúng loại nhà {p['home']} và địa chỉ {address(p)}.",3),
  ])
 for p in PROFILES[2:4]:
  qs.extend(based(q,passage(p)) for q in [
   match([('Name',p['name']),('Home',p['home']),('Address',address(p))],'Ghép thông tin từ đúng bài đọc.',3),
   mc('Is the home near the school?',['Yes, it is.','No, it is not.','It is pink.','It is a sport.'],'Yes, it is.' if p['near'] else 'No, it is not.',f"Bài đọc ghi {'near' if p['near'] else 'far from'} my school.",3),
   text(p['name']+' is speaking. Complete: My address is ___.',address(p),f"Địa chỉ là {address(p)}.",3),
  ])
 cards='\n\n'.join(card(p) for p in PROFILES)
 def find(**facts):
  result=[p for p in PROFILES if all(p[k]==v for k,v in facts.items())];assert len(result)==1;return result[0]['name']
 qs.extend(based(q,cards) for q in [
  text('Who lives in a flat near school? Write the name.',find(home='flat',near=True),'Tìm đồng thời Home: flat và School: near; đó là Hoa.',3),
  text('Who lives in King Street far from school? Write the name.',find(street='King Street',near=False),'Nam sống ở King Street và xa trường.',3),
  tf([('An and Hoa both live in Queen Street.',all(p['street']=='Queen Street' for p in [PROFILES[0],PROFILES[5]])),('Minh and Nam both live near school.',all(p['near'] for p in [PROFILES[2],PROFILES[4]]))],'An/Hoa: Queen Street. Minh gần trường, Nam xa trường.',3),
  text('Mai is speaking. Write the full address sentence starting with “I live at”.',f"I live at {address(PROFILES[3])}.",f"Thẻ Mai ghi {address(PROFILES[3])}.",3),
 ]);return qs


def writing():
 p=PROFILES[4]
 return [
 text('Complete: I ___ in a house.','live','Chủ ngữ I dùng live.'),
 reorder('I live in a flat.','I live in a flat.'),
 text('Complete: Do ___ live in this house?','you','Câu hỏi Do you live…?'),
 text('Complete: No, I do ___.','not','Phủ định: do not.'),
 reorder('Yes, I do.','Yes, I do. là câu trả lời ngắn.'),
 text('Complete: My ___ is 18 King Street.','address','Địa chỉ: My address is…',2),
 mc('Choose the correct sentence.',['It is 14 Queen Street.','It 14 Queen Street is.','Is it Street Queen 14.','It are 14 Queen Street.'],'It is 14 Queen Street.','It is + số nhà + tên đường.',2),
 reorder('What is your address?','What is your address?',2),
 text('Rewrite in full: I don’t live in that tower.','I do not live in that tower.','Don’t = do not.'),
 text('Complete: I live ___ a building.','in','In + loại nhà.'),
 reorder('My home is far from my school.','Far from: xa.',2),
 text('Rewrite with spaces: Iliveat16KingStreet.','I live at 16 King Street.','Tách từ, giữ đúng địa chỉ.',2),
 match([('I live in','a house.'),('I live at','16 King Street.'),('My home is near','my school.')],'In + loại nhà; at + địa chỉ; near + địa điểm.',2),
 based(text('Complete the address: It is ___.',address(p),f"Địa chỉ Nam là {address(p)}.",2),card(p)),
 based(text('Nam is speaking. Write a sentence about the type of home. Start with “I live”.',f"I live in a {p['home']}.",f"Home: {p['home']}.",3),card(p)),
 based(text('Nam is speaking. Write the address sentence. Start with “My address”.',f"My address is {address(p)}.",f"Address: {address(p)}.",3),card(p)),
 based(reorder('My home is far from my school.','Thẻ ghi far from the home.',3),card(p)),
 based(text('Nam is speaking. Answer “Do you live near school?” with a short answer.',reply(p),'Nam sống xa trường nên trả lời No, I do not.',3),card(p)),
 ]


def listening(index):
 a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
 return [
 listen('Listen and choose the type of home.',f"I live in a {a['home']}.",[field('Home:',a['home'],HOMES)]),
 listen('Listen and choose the house number.',f"My house number is {b['number']}.",[field('Number:',b['number'],['14','26','18','32','16','19'])],2),
 listen('Listen. Which street does '+b['name']+' live in?',f"My name is {b['name']}. I live at {address(b)}.",[field('Street:',b['street'],['Queen Street','Oxford Street','King Street','London Street'])],2),
 listen('Listen. Is the home near or far from school?',f"My name is {c['name']}. My home is {'near' if c['near'] else 'far from'} my school.",[field('School:', 'near' if c['near'] else 'far from',['near','far from'])],2),
 listen('Listen and choose the home and street.',passage(a),[field('Home:',a['home'],HOMES),field('Street:',a['street'],['Queen Street','Oxford Street','King Street','London Street'])],3),
 listen('Listen and write the house number and type of home.',passage(c),[field('Number:',c['number']),field('Home:',c['home'])],3),
 ]


def build_tests():
 written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
 # Synthesis selects different tasks in the same level bands, with no repeated task within the exam.
 mixed=[written[1][0],written[2][1],written[4][5],written[0][4],written[1][6],written[4][1],written[2][2],written[0][6],
        written[2][8],written[4][10],written[0][10],written[1][11],written[3][12],written[4][12],
        written[3][14],written[3][15],written[4][15],written[3][16]]
 import copy
 return [assemble(copy.deepcopy(qs),listening(i)) for i,qs in enumerate(written+[mixed])]
