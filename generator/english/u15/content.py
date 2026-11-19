"""Original English role-play: health phrases and should, printed pages 30-35."""
from english.practice import mc,text as base_text,match,reorder,tf,based,picture as image,field,listen,assemble

CORE=['toothache','headache','sore throat','stomach ache']
MEANINGS=['đau răng','đau đầu','đau họng','đau bụng']
IMAGE_NAMES=dict(zip(CORE,['toothache','headache','sore-throat','stomach-ache']))
ADVICE=['go to the dentist','have a rest','drink warm water','go to the doctor']
AVOID=['watch too much TV','drink cold water','eat ice cream very often']
PROFILES=[
    dict(name='An',pronoun='He',issue='headache',advice='have a rest',avoid=AVOID[0]),
    dict(name='Linh',pronoun='She',issue='toothache',advice='go to the dentist',avoid=AVOID[2]),
    dict(name='Minh',pronoun='He',issue='sore throat',advice='go to the doctor',avoid=AVOID[1]),
    dict(name='Hoa',pronoun='She',issue='stomach ache',advice='go to the doctor',avoid=AVOID[1]),
    dict(name='Nam',pronoun='He',issue='headache',advice='go to the doctor',avoid=AVOID[0]),
    dict(name='Mai',pronoun='She',issue='sore throat',advice='drink warm water',avoid=AVOID[1])]


def text(stem,answer,why,lesson=1,alternatives=()):
    accepted=list(alternatives)
    if 'stomach ache' in answer:accepted.append(answer.replace('stomach ache','stomachache'))
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short=answer.replace('should not',"shouldn't").replace('What is',"What's").replace('I do not',"I don't").replace('I am',"I'm")
        if short!=answer:accepted.append(short)
    return base_text(stem,answer,why,lesson,accepted)


def picture(word,width=320):return image('u15',IMAGE_NAMES[word],MEANINGS[CORE.index(word)],width)
def symptom(p):return f"I have a {p['issue']}."
def reported(p):return f"{p['pronoun']} has a {p['issue']}."
def advice(p):return f"You should {p['advice']}."
def negative(p):return f"You should not {p['avoid']}."
def card(p):return f"Fictional English role-play · Speaker: {p['name']} · Pronoun: {p['pronoun']} · Health phrase: {p['issue']} · Positive line to practise: {p['advice']} · Negative line to practise: {p['avoid']}. Use these lines for the language task; do not choose a treatment yourself."
def passage(p):return f"In our English role-play, {p['name']} says, ‘{symptom(p)}’ A partner reads the card and says, ‘{advice(p)} {negative(p)}’ {p['name']} says, ‘Thanks for your advice.’"
def shown(q,p):return based(q,card(p))


def warmup():
    a,b,c=PROFILES[:3]
    return [mc('Look at the illustration. Choose the health phrase.',CORE,'toothache','Tranh chỉ vị trí đau ở răng.',1,picture('toothache')),
        text('Complete: What is the ___?','matter','What is the matter?'),
        match([('toothache','đau răng'),('headache','đau đầu'),('sore throat','đau họng')],'Ghép từ, không chẩn đoán người thật.'),
        mc('Choose the correct first-person sentence.',['I have a headache.','I has a headache.','I am a headache.','I have headache a.'],'I have a headache.','I have a + vấn đề sức khỏe.'),
        reorder('What is the matter?','What’s = What is.'),
        text('Complete: I have a sore ___.','throat','Sore throat.'),
        shown(mc('Which positive line is on the role-play card?',ADVICE,b['advice'],'Lấy đúng dòng Positive line.',2),b),
        text('Complete: You ___ have a rest. Use the word nên.','should','Should + nguyên mẫu.',2),
        shown(text('Write only the health phrase.',c['issue'],'Sore throat.'),c),
        reorder('Thanks for your advice.','Cảm ơn lời khuyên.',2),
        text('Complete: He ___ a toothache. Use have.','has','He/she has; I have.'),
        shown(tf([('The speaker’s phrase is headache.',True),('The positive line says go to the dentist.',False)],'Theo thẻ An, không tự đoán lời khuyên.',2),a),
        shown(text('Write only the positive verb phrase from the card.',b['advice'],'Go to the dentist.',2),b),
        text('Complete: You should ___ warm water. Use drink.','drink','Should + drink.',2),
        shown(text('Write the complete symptom sentence, starting with I.',symptom(a),'I have a headache.',3),a),
        shown(text('Write the positive line as one sentence starting with You should.',advice(c),'Theo thẻ của Minh.',3),c),
        mc('Choose the correct negative sentence.',['You should not watch too much TV.','You should not watches too much TV.','You not should watch too much TV.','You should does not watch too much TV.'],'You should not watch too much TV.','Should not + nguyên mẫu.',3),
        shown(text('Write symptom, then positive line. Start the sentences with I and You should.',symptom(b)+' '+advice(b),'Dùng đúng health phrase và positive line.',3),b)]


def vocabulary():return [
    *[mc('Look at the illustration. Choose the health phrase.',CORE,k,'Tranh: '+MEANINGS[CORE.index(k)]+'.',1,picture(k)) for k in CORE],
    text('Complete: tooth___. Write the whole word.','toothache','Toothache viết liền.'),
    match([('go to the dentist','đến nha sĩ'),('have a rest','nghỉ ngơi'),('drink warm water','uống nước ấm')],'Các cụm từ trong bài học.',2),
    mc('Which phrase means “đau bụng”?',CORE,'stomach ache','Stomach ache.'),
    text('Complete: sore ___.','throat','Sore throat: đau họng.'),
    text('Complete: Thanks for your ___.','advice','Advice là lời khuyên.',2),
    reorder('You should go to the doctor.','Should + go.',2),
    match([('should','nên'),('should not','không nên'),('dentist','nha sĩ')],'Nhận nghĩa của từ/cụm.',2),
    text('Complete: have a ___. Use the word meaning sự nghỉ ngơi.','rest','Have a rest.',2),
    shown(text('Write only the negative verb phrase from the card.',PROFILES[1]['avoid'],'Eat ice cream very often.',2),PROFILES[1]),
    tf([('Take some medicine means dùng thuốc in Vietnamese.',True),('After should, use has with he.',False)],'Nhớ nghĩa cụm từ; sau should dùng have nguyên mẫu.',2),
    shown(text('Write only the health phrase.',PROFILES[3]['issue'],'Stomach ache.',3),PROFILES[3]),
    shown(text('Write only the positive verb phrase.',PROFILES[5]['advice'],'Drink warm water theo đúng thẻ.',3),PROFILES[5]),
    based(match([(p['name'],p['issue']+' / '+p['advice']) for p in PROFILES[:3]],'Đọc cả hai trường trên thẻ.',3),'\n'.join(card(p) for p in PROFILES[:3])),
    reorder('I do not feel well.','I don’t = I do not.',3)]


def dialogue():
    a,b,c=PROFILES[:3]
    return [mc('What is the matter? Choose the sentence that names a health problem.',['I have a sore throat.','Thanks for your advice.','You should have a rest.','On Sunday.'],'I have a sore throat.','I have a… nêu vấn đề sức khỏe.'),
        text('Complete: What ___ I do? Use the word nên.','should','What should I do?',2),
        reorder('You should have a rest.','Should + have.'),
        shown(mc('Which positive line is on the card?',ADVICE,b['advice'],'Không suy từ bệnh, đọc thẻ.',2),b),
        text('Rewrite in full: I don’t feel well.','I do not feel well.','Don’t = do not.'),
        text('Complete: She ___ a headache. Use have.','has','She has.'),
        shown(text('Say the health phrase in a complete sentence starting with I.',symptom(a),'I have a headache.'),a),
        shown(mc('What health phrase does the speaker practise?',CORE,c['issue'],'Minh: sore throat.'),c),
        reorder('What should I do?','Hỏi lời khuyên.',2),
        text('Rewrite in full: You shouldn’t watch too much TV.','You should not watch too much TV.','Shouldn’t = should not.',2),
        text('Complete: You should ___ to the dentist.','go','Should + go.',2),
        match([('What is the matter?','I have a toothache.'),('What should I do?','You should go to the dentist.'),('Thanks for your advice.','You are welcome.')],'Khớp câu hỏi và chức năng câu đáp.',2),
        shown(text('Give the positive line starting with You should.',advice(c),'Theo thẻ, không tự chọn thuốc.',2),c),
        tf([('Should not gives a negative line.',True),('After should, use goes with he.',False)],'Should + go với mọi chủ ngữ.',3),
        shown(text('Write positive, then negative line in full form. Start both with You should.',advice(a)+' '+negative(a),'Giữ nguyên động từ sau should/not.',3),a),
        text('Rewrite in full: What’s the matter?','What is the matter?','What’s = What is.',3),
        shown(text('Give the negative line in full form starting with You should not.',negative(b),'Lấy dòng Negative line.',3),b),
        mc('Choose the correct sentence.',['He should have a rest.','He should has a rest.','He should having a rest.','He should to have a rest.'],'He should have a rest.','Should + have.',3)]


def reading():
    qs=[]
    for p in PROFILES[:4]:
        wrong=CORE[(CORE.index(p['issue'])+1)%4]
        qs.extend(based(q,passage(p)) for q in [text('Who speaks first? Write the name only.',p['name'],'Tên trước says đầu tiên.',3),
            mc('Which positive line does the partner read?',ADVICE,p['advice'],'Lấy từ hội thoại, không đoán cách chữa.',3),
            text('Write only the health phrase used by the speaker.',p['issue'],'Đọc câu I have a…',3),
            tf([(f"The speaker uses the phrase {p['issue']}.",True),(f"The speaker uses the phrase {wrong}.",False)],'Đối chiếu nguyên hội thoại.',3)])
    qs += [based(text('Who has the headache card with the positive line go to the doctor? Write the name only.','Nam','An và Nam cùng health phrase nhưng khác positive line.',3),'\n'.join(card(p) for p in [PROFILES[0],PROFILES[4]])),
        based(mc('What does the partner say last?',['You are welcome.','I have a headache.','What is the matter?','Thanks for your advice.'],'You are welcome.','Đọc đúng lượt nói cuối.',3),'A: What is the matter? B: I have a headache. A: You should have a rest. B: Thanks for your advice. A: You are welcome.')]
    return qs


def writing():
    a,b,c=PROFILES[:3]
    return [text('Complete: I ___ a toothache. Use have.','have','I have.'),reorder('She has a sore throat.','She has.'),
        text('Complete: He ___ a headache. Use have.','has','He has.'),text('Complete: You should ___ a rest.','have','Should + have.',2),
        mc('Choose the correct question.',['What should I do?','What should I does?','What I should do?','What should do I?'],'What should I do?','Should + I + do.',2),
        text('Complete: What is the ___?','matter','What is the matter?'),
        match([('I','have'),('She','has'),('You should','have a rest')],'Phân biệt have/has và should + have.'),
        reorder('You should drink warm water.','Should + drink.',2),
        text('Rewrite in full: You shouldn’t drink cold water.','You should not drink cold water.','Should not + drink.',2),
        text('Complete: Thanks ___ your advice.','for','Thanks for.',2),
        shown(reorder(advice(b),'Dòng positive trên thẻ.',2),b),reorder('I do not feel very well.','Do not feel.',2),
        text('Complete: go to the ___. Use nha sĩ.','dentist','Dentist.'),
        text('Rewrite in full: What’s the matter?','What is the matter?','What’s = What is.',2),
        shown(text('Write symptom, then positive line, starting with I and You should.',symptom(c)+' '+advice(c),'Theo thẻ Minh.',3),c),
        shown(text('Write the third-person health sentence starting with He.',reported(a),'He has a headache.',3),a),
        shown(text('Write the negative line in full form starting with You should not.',negative(PROFILES[5]),'Should not + drink.',3),PROFILES[5]),
        shown(text('Write symptom, then positive line starting with I and You should.',symptom(PROFILES[3])+' '+advice(PROFILES[3]),'Đúng health phrase và dòng được giao.',3),PROFILES[3])]


def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    return [listen('Listen and choose the health phrase.',symptom(a),[field('Health phrase:',a['issue'],CORE)]),
        listen('Listen and choose the positive verb phrase.',advice(b),[field('Positive line:',b['advice'],ADVICE)],2),
        listen('Listen. Which negative verb phrase is used?',symptom(b)+' '+negative(b),[field('Negative line:',b['avoid'],AVOID)],2),
        listen('Listen and choose the speaker’s health phrase.',f"{c['name']} says: "+symptom(c)+' '+advice(c),[field('Health phrase:',c['issue'],CORE)],2),
        listen('Listen. Find both the health phrase and the positive verb phrase.',symptom(a)+' '+advice(a),[field('Health phrase:',a['issue'],CORE),field('Positive line:',a['advice'],ADVICE)],3),
        listen('Listen. Write only Linh’s health phrase and positive verb phrase, not An’s.',
            'An says: I have a headache. His partner says: You should have a rest. Linh says: I have a toothache. Her partner says: You should go to the dentist.',
            [field('Linh’s health phrase:','toothache'),field('Linh’s positive line:','go to the dentist')],3)]


def build_tests():
    import copy
    written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
    mixed=[copy.deepcopy(written[i%5][i]) for i in range(18)]
    return [assemble(qs,listening(i)) for i,qs in enumerate(written+[mixed])]
