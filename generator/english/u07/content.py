"""Original school-activity exercises; verified textbook pages 50–55."""
from english.practice import mc,text as base_text,match,reorder,tf,based,picture as image,field,listen,assemble

ACTIVITIES={
 'do projects':('doing projects','làm dự án'),
 'read books':('reading books','đọc sách'),
 'play games':('playing games','chơi trò chơi'),
 'solve maths problems':('solving maths problems','giải các bài toán'),
}
CORE=list(ACTIVITIES)
GERUNDS=[v[0] for v in ACTIVITIES.values()]
REASONS=['fun','interesting','useful','good for group work']
PROFILES=[
 dict(name='An',pronoun='He',activity='read books',reason='interesting'),
 dict(name='Linh',pronoun='She',activity='do projects',reason='good for group work'),
 dict(name='Minh',pronoun='He',activity='solve maths problems',reason='useful'),
 dict(name='Mai',pronoun='She',activity='play games',reason='fun'),
 dict(name='Nam',pronoun='He',activity='do projects',reason='fun'),
 dict(name='Hoa',pronoun='She',activity='read books',reason='useful'),
]
def text(stem,answer,why,lesson=1,alternatives=()):
    variants=list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short=answer.replace('it is',"it's").replace('does not',"doesn't")
        if short!=answer:variants.append(short)
    return base_text(stem,answer,why,lesson,variants)
def picture(activity,width=320):return image('u07',activity.replace(' ','-'),'Tranh hoạt động ở trường: quan sát việc các bạn đang làm.',width)
def gerund(p):return ACTIVITIES[p['activity']][0]
def sentence(p):return f"{p['pronoun']} likes {gerund(p)}."
def because(p):return f"Because {p['pronoun'].lower()} thinks it is {p['reason']}."
def full_sentence(p):return f"{p['pronoun']} likes {gerund(p)} because {p['pronoun'].lower()} thinks it is {p['reason']}."
def card(p):return f"Name: {p['name']} ({p['pronoun'].lower()}) · School activity: {gerund(p)} · Reason: {p['reason']}."
def passage(p):return f"This is {p['name']}. {sentence(p)} {p['pronoun']} thinks it is {p['reason']}. {p['pronoun']} likes this school activity."
def shown(q,p):return based(q,card(p))

def warmup():
    a,b,c,d=PROFILES[:4]
    return [
      mc('Look at the picture. Choose the school activity.',CORE,'do projects','Các bạn đang cùng làm một dự án.',1,picture('do projects')),
      match([(k,v[1]) for k,v in ACTIVITIES.items()],'Ghép hoạt động ở trường với nghĩa.'),
      text('Complete: He ___ reading books.','likes','He/She dùng likes khi kể sở thích.'),
      mc('Choose the form after “likes”.',['reading books','read books','reads books','readed books'],'reading books','Likes + V-ing: reading books.'),
      reorder('She likes playing games.','She + likes + playing games.'),
      text('Complete: What school activity ___ he like?','does','Does đi với he/she trong câu hỏi; like giữ nguyên.'),
      mc('Which word asks for a reason?',['Why','Where','Who','When'],'Why','Why hỏi vì sao.',2),
      shown(mc('Which activity does '+a['name']+' like?',GERUNDS,gerund(a),f"Thẻ ghi {gerund(a)}."),a),
      match([('fun','vui'),('interesting','thú vị'),('useful','hữu ích')],'Ghép từ nêu lý do.',2),
      text('Complete: Because she ___ it is fun.','thinks','She thinks; thêm s với she.',2),
      shown(text('Why does '+b['name']+' like this activity? Write only the reason phrase.',b['reason'],f"Linh chọn lý do {b['reason']}.",2),b),
      reorder('He likes solving maths problems.','Solve → solving; giữ maths problems.',2),
      text('Complete: It is good for group ___.','work','Good for group work: tốt cho làm việc nhóm.',2),
      shown(tf([(c['name']+' likes '+gerund(c)+'.',True),(c['name']+' likes '+gerund(d)+'.',False)],'Đối chiếu đúng hoạt động trong thẻ.',2),c),
      shown(text('Write a full sentence about '+d['name']+'’s activity. Start with “She”.',sentence(d),'She likes + playing games.',3),d),
      shown(text('Answer “Why?” Start with “Because”.',because(a),'He thinks it is interesting.',3),a),
      mc('Choose the correct question.',['What school activity does she like?','What school activity does she likes?','What school activity do she like?','What school activity she likes?'],'What school activity does she like?','Sau does dùng like, không thêm s.',3),
      shown(text('Write one sentence with the activity and reason. Start with “He” and include “because”.',full_sentence(c),'He likes… because he thinks it is useful.',3),c),
    ]

def vocabulary():return [
    *[mc('Look at the picture. Choose the activity.',CORE,k,f"Tranh minh họa {v[1]}.",1,picture(k)) for k,v in ACTIVITIES.items()],
    text('Complete: p r o j e _ t s. Write the whole word.','projects','Projects có chữ c sau e.'),
    text('Complete: u s e f _ l. Write the whole word.','useful','Useful có chữ u trước l.'),
    match([('do','projects'),('read','books'),('solve','maths problems')],'Ghép đúng cụm động từ.'),
    mc('Which phrase means “chơi trò chơi”?',CORE,'play games','Play games là chơi trò chơi.'),
    match([(k,v[0]) for k,v in ACTIVITIES.items()],'Ghép dạng nguyên mẫu với V-ing.',2),
    mc('Which reason means “thú vị”?',REASONS,'interesting','Interesting nghĩa là thú vị.',2),
    text('Complete: good ___ group work.','for','Good for + group work.',2),
    text('Complete: solve maths ___.','problems','Solve maths problems: giải các bài toán.',2),
    reorder('She likes doing projects.','Do → doing sau likes.',2),
    tf([('Reading and solving have first-syllable stress here.',True),('Useful means “vô ích”.',False)],'READ-ing, SOLV-ing nhấn âm đầu; useful nghĩa là hữu ích.',3),
    shown(text('Write the complete activity phrase for Linh.',gerund(PROFILES[1]),'Thẻ ghi doing projects.',3),PROFILES[1]),
    shown(text('Write the reason phrase for Nam.',PROFILES[4]['reason'],'Dùng lý do của Nam trong thẻ, không suy từ thẻ Linh.',3),PROFILES[4]),
    based(match([(p['name'],p['reason']) for p in PROFILES[:3]],'Ghép mỗi bạn với lý do từ ba thẻ.',3),'\n\n'.join(card(p) for p in PROFILES[:3])),
    reorder('Because she thinks it is good for group work.','Because + she thinks + it is + lý do.',3),
]

def dialogue():
    a,b,c,d=PROFILES[:4]
    return [
      mc('A: What school activity does he like? B: ___.',['He likes reading books.','He is on the first floor.','He is ten.','He lives in a flat.'],'He likes reading books.','Trả lời sở thích bằng He likes + V-ing.'),
      text('Complete: What school activity does she ___?','like','Sau does dùng like nguyên dạng.'),
      reorder('What school activity does he like?','What school activity + does + he + like?'),
      mc('A: Why does she like playing games? B: ___.',['Because she thinks it is fun.','It is on the third floor.','She is Japanese.','She has long hair.'],'Because she thinks it is fun.','Why hỏi lý do; dùng Because…'),
      text('Complete: ___ he like reading books?','Does','Does he like…?'),
      text('Complete: Does she like doing projects? Yes, she ___.','does','Does she…? → Yes, she does.'),
      text('Complete: Does he like playing games? No, he ___.','does not','No, he does not; cũng có thể viết doesn’t.'),
      shown(mc('Why does '+c['name']+' like this activity?',REASONS,c['reason'],'Đọc lý do của Minh trong thẻ.'),c),
      shown(text('Write the reply about '+b['name']+'’s activity. Begin “She”.',sentence(b),'She likes doing projects.',2),b),
      reorder('Why does he like solving maths problems?','Sau does dùng like.',2),
      text('Rewrite in full: Because she thinks it’s interesting.','Because she thinks it is interesting.','It’s = it is.',2),
      match([('What school activity does he like?','He likes reading books.'),('Why does he like it?','Because he thinks it is useful.'),('Does he like doing projects?','Yes, he does.')],'Ghép đúng câu hỏi hoạt động, lý do và có/không.',2),
      shown(text('Mai is the subject. Give the full reason starting with “Because”.',because(d),'Mai: she; fun.',2),d),
      tf([('“What school activity…?” asks about an activity.',True),('“Why…?” asks which floor a room is on.',False)],'What school activity hỏi hoạt động; Why hỏi lý do.',2),
      shown(text('Write one activity sentence and one reason sentence, starting with “He” and then “Because”.',sentence(a)+' '+because(a),'He likes reading books. Because he thinks it is interesting.',3),a),
      shown(text('Write a single sentence with “because”, starting with “She”.',full_sentence(b),'Giữ likes doing và she thinks.',3),b),
      text('Rewrite in full: He doesn’t like playing games.','He does not like playing games.','Doesn’t = does not; like không thêm s.',3),
      mc('Choose the correct reason sentence.',['Because he thinks it is useful.','Because he think it is useful.','Because he thinks is useful.','Because does he thinks useful.'],'Because he thinks it is useful.','He thinks + it is + useful.',3),
    ]

def reading():
    qs=[]
    for i,p in enumerate(PROFILES[:4]):
        other=PROFILES[(i+1)%4]
        qs.extend(based(q,passage(p)) for q in [
          text('Write the pupil’s name.',p['name'],f"Bài đọc giới thiệu {p['name']}.",3),
          mc('Which school activity does the pupil like?',GERUNDS,gerund(p),f"Sở thích: {gerund(p)}.",3),
          text('Write only the reason phrase.',p['reason'],f"Lý do trong bài: {p['reason']}.",3),
          tf([(p['name']+' likes '+gerund(p)+'.',True),(p['name']+' thinks it is '+other['reason']+'.',False)],'Đọc cả hoạt động và lý do, không suy đoán theo sở thích của mình.',3),
        ])
    qs += [based(text('Who likes doing projects because it is fun? Write the name.','Nam','Nam và Linh cùng doing projects nhưng lý do khác nhau.',3),'\n\n'.join(card(p) for p in [PROFILES[1],PROFILES[4]])),
           based(text('Who likes reading books because it is useful? Write the name.','Hoa','Hoa và An cùng reading books nhưng lý do khác nhau.',3),'\n\n'.join(card(p) for p in [PROFILES[0],PROFILES[5]]))]
    return qs

def writing():
    a,b,c,d=PROFILES[:4]
    return [
      text('Complete: She ___ doing projects.','likes','She likes + V-ing.'),
      reorder('He likes reading books.','He + likes + reading books.'),
      text('Complete: What school activity ___ she like?','does','Does với she.'),
      text('Complete: He likes ___ games.','playing','Play → playing sau likes.'),
      mc('Choose the correct sentence.',['She likes solving maths problems.','She like solve maths problems.','She likes solve maths problems.','She does likes solving maths problems.'],'She likes solving maths problems.','She likes + solving maths problems.'),
      text('Complete: ___ he thinks it is fun.','Because','Because mở đầu lời giải thích.'),
      match([('do','doing'),('read','reading'),('solve','solving')],'Ghép đúng dạng V-ing.'),
      reorder('Does she like playing games?','Does + she + like + playing games?'),
      text('Rewrite in full: She doesn’t like reading books.','She does not like reading books.','Doesn’t = does not.',2),
      text('Complete: Because he ___ it is useful.','thinks','He thinks, thêm s.',2),
      shown(reorder(sentence(b),'Theo hoạt động trong thẻ Linh.',2),b),
      reorder('Why does she like doing projects?','Why + does + she + like…?',2),
      text('Complete: It is good for ___ work.','group','Good for group work.',2),
      text('Rewrite in full: Because he thinks it’s fun.','Because he thinks it is fun.','It’s = it is.',2),
      shown(text('Write a single sentence about Minh with the activity and “because”. Begin “He”.',full_sentence(c),'He likes solving maths problems because he thinks it is useful.',3),c),
      shown(text('Write a single sentence about Mai with “because”. Begin “She”.',full_sentence(d),'She likes playing games because she thinks it is fun.',3),d),
      shown(text('Give the reason for An starting with “Because”.',because(a),'Because he thinks it is interesting.',3),a),
      shown(text('Write a full activity sentence about Hoa, starting with “She”.',sentence(PROFILES[5]),'She likes reading books.',3),PROFILES[5]),
    ]

def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    return [
      listen('Listen and choose the activity.',sentence(a),[field('Activity:',gerund(a),GERUNDS)]),
      listen('Listen and choose the reason.',because(b),[field('Reason:',b['reason'],REASONS)],2),
      listen('Listen. Which activity does '+b['name']+' like?',f"This is {b['name']}. {sentence(b)}",[field('Activity:',gerund(b),GERUNDS)]),
      listen('Listen. Why does '+c['name']+' like this activity?',sentence(c)+' '+because(c),[field('Reason:',c['reason'],REASONS)],2),
      listen('Listen and choose the activity and reason.',passage(a),[field('Activity:',gerund(a),GERUNDS),field('Reason:',a['reason'],REASONS)],3),
      listen('Listen and write the activity and reason.',passage(c),[field('Activity:',gerund(c)),field('Reason:',c['reason'])],3),
    ]

def build_tests():
    import copy
    written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
    mixed=[copy.deepcopy(written[i%5][i]) for i in range(18)]
    return [assemble(qs,listening(i)) for i,qs in enumerate(written+[mixed])]
