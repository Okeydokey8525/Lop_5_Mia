"""Original future-job practice based on verified pages 34–39."""
from english.practice import mc,text,match,reorder,tf,based,picture as image,field,listen,assemble

JOBS={
 'firefighter':('lính cứu hỏa','help people'),
 'reporter':('phóng viên','report the news'),
 'gardener':('người làm vườn','grow flowers'),
 'writer':('nhà văn','write stories'),
 'doctor':('bác sĩ','help people'),
 'teacher':('giáo viên','teach children'),
}
CORE=list(JOBS)[:4]
PROFILES=[
 dict(name='An',pronoun='He',job='writer'),dict(name='Linh',pronoun='She',job='firefighter'),
 dict(name='Minh',pronoun='He',job='gardener'),dict(name='Mai',pronoun='She',job='reporter'),
 dict(name='Nam',pronoun='He',job='teacher'),dict(name='Hoa',pronoun='She',job='doctor'),
]
REASONS=list(dict.fromkeys(reason for meaning,reason in JOBS.values()))
def reason(p):return JOBS[p['job']][1]
def job_sentence(p):return 'I would like to be a '+p['job']+' in the future.'
def because(p):return 'Because I would like to '+reason(p)+'.'
def third_job(p):return p['pronoun']+' would like to be a '+p['job']+' in the future.'
def card(p):return f"Name: {p['name']}\nPronoun: {p['pronoun'].lower()}\nFuture job: {p['job']}\nReason: {reason(p)}"
def passage(p):return f"My name is {p['name']}. I am in Grade 5. {job_sentence(p)} I would like to {reason(p)}."
def picture(name,width=320):return image('u05',name,JOBS[name][0],width)
def job_options(answer):
 return [answer]+[j for j in JOBS if j!=answer][:3]

def warmup():return [
 mc('Which word means “nhà văn”?',CORE,'writer','Writer nghĩa là nhà văn.'),
 text('Complete: I would like to ___ a doctor.','be','Would like to be + a + nghề.'),
 mc('What ___ you like to be in the future?',['would','is','are','am'],'would','Mẫu hỏi ước mơ dùng would.'),
 reorder('I would like to be a reporter.','I would like to be + a reporter.'),
 match([(j,JOBS[j][0]) for j in CORE[:3]],'Firefighter: lính cứu hỏa; reporter: phóng viên; gardener: người làm vườn.'),
 text('Complete: I would like to be ___ writer.','a','A trước danh từ nghề nghiệp số ít writer.'),
 mc('Which phrase means “dạy trẻ em”?',['teach children','grow flowers','write stories','report the news'],'teach children','Teach children nghĩa là dạy trẻ em.',2),
 tf([('A reporter can report the news.',True),('A gardener means “nhà văn”.',False)],'Reporter đưa tin; gardener là người làm vườn.',2),
 mc('Which word asks for a reason?',['Why','Where','Who','What'],'Why','Why hỏi lý do.',2),
 text('Complete: ___ I would like to help people.','Because','Because mở đầu câu trả lời nêu lý do.',2),
 match([(j,JOBS[j][1]) for j in CORE[1:]],'Reporter → report the news; gardener → grow flowers; writer → write stories.',2),
 text('Write the full form of “I’d”.','I would','Trong mẫu nghề nghiệp, I’d = I would.'),
 based(text('Write Linh’s future job.',PROFILES[1]['job'],f"Thẻ ghi Future job: {PROFILES[1]['job']}.",2),card(PROFILES[1])),
 reorder('Why would you like to be a teacher?','Why + would you like to be + a teacher?',2),
 based(text('An is speaking. Write the full future-job sentence, including “in the future”.',job_sentence(PROFILES[0]),f"Future job: {PROFILES[0]['job']}.",3),card(PROFILES[0])),
 based(text('Mai is speaking. Answer “Why?” Start with “Because”.',because(PROFILES[3]),f"Reason: {reason(PROFILES[3])}.",3),card(PROFILES[3])),
 based(tf([('Minh would like to be a gardener.',True),('Minh would like to write stories.',False)],f"Minh: {PROFILES[2]['job']}; {reason(PROFILES[2])}.",3),card(PROFILES[2])),
 mc('Choose the correct future-job question.',['What would you like to be in the future?','What you would like to be in the future?','What would you like be in the future?','What would you likes to be in the future?'],'What would you like to be in the future?','What + would + you + like to be…?',3),
]

def vocabulary():
 qs=[mc('Look at the picture. Choose the job.',CORE,j,f"Tranh minh họa nghề {j}: {JOBS[j][0]}.",1,picture(j)) for j in CORE]
 return qs+[
 text('Complete: r e p o r _ e r. Write the whole word.','reporter','Reporter có chữ t sau r.'),
 text('Complete: w r i _ e r. Write the whole word.','writer','Writer có chữ t.'),
 match([('doctor','bác sĩ'),('teacher','giáo viên'),('firefighter','lính cứu hỏa')],'Ghép tên nghề với nghĩa.'),
 mc('Which job means “người làm vườn”?',CORE,'gardener','Gardener là người làm vườn.'),
 match([('report the news','đưa tin'),('grow flowers','trồng hoa'),('write stories','viết truyện')],'Ghép các việc làm tương ứng.',2),
 mc('Which phrase means “giúp đỡ mọi người”?',['help people','teach children','write stories','grow flowers'],'help people','Help people nghĩa là giúp mọi người.',2),
 text('Complete: report the ___.','news','Cụm đúng là report the news.',2),
 text('Complete: grow ___. Use the word for “hoa”.','flowers','Grow flowers là trồng hoa.',2),
 tf([('Teacher and dentist have first-syllable stress in this lesson.',True),('Writer means “phóng viên”.',False)],'TEA-cher và DEN-tist nhấn âm đầu; writer là nhà văn.',3),
 reorder('I would like to write stories.','Would like to + write stories.',2),
 based(text('Hoa is speaking. Write the full reason starting with “Because”.',because(PROFILES[5]),f"Reason: {reason(PROFILES[5])}.",3),card(PROFILES[5])),
 based(text('Write Nam’s job.',PROFILES[4]['job'],f"Nam muốn làm {PROFILES[4]['job']}.",3),card(PROFILES[4])),
 match([(j,JOBS[j][1]) for j in CORE],'Ghép bốn nghề với việc làm/lý do trong bộ từ của bài.',3),
 based(reorder(job_sentence(PROFILES[2]),'Dùng nghề trong thẻ Minh.',3),card(PROFILES[2])),
 ]

def dialogue():return [
 mc('A: What would you like to be in the future? B: ___.',['I would like to be a writer.','I live in a house.','I am Japanese.','It is pink.'],'I would like to be a writer.','Trả lời bằng I would like to be + nghề.'),
 text('Complete: I would ___ to be a gardener.','like','Would like to be là cụm diễn tả mong muốn.'),
 reorder('What would you like to be?','What would you like to be?'),
 mc('A: Why would you like to be a teacher? B: ___.',['Because I would like to teach children.','I am in Grade 5.','My name is An.','It is a dolphin.'],'Because I would like to teach children.','Why hỏi lý do; dùng Because…',2),
 text('Complete: Why would you like to ___ a reporter?','be','Would like to be + a reporter.',2),
 match([('What would you like to be?','I would like to be a gardener.'),('Why would you like to be a gardener?','Because I would like to grow flowers.'),('Would you like to be a teacher?','Yes, I would.')],'Ghép câu hỏi nghề, lý do và có/không.',2),
 text('Complete: Would you like to be a writer? Yes, I ___.','would','Would you…? → Yes, I would.'),
 mc('Which question asks for a reason?',['Why would you like to be a doctor?','What would you like to be?','What is your name?','Where do you live?'],'Why would you like to be a doctor?','Why hỏi lý do.',2),
 text('Rewrite in full: I’d like to be a reporter.','I would like to be a reporter.','I’d = I would.'),
 based(text('Linh is speaking. Complete: I would like to be a ___.',PROFILES[1]['job'],f"Linh: {PROFILES[1]['job']}.",2),card(PROFILES[1])),
 based(mc('Minh is speaking. Choose the reason in the card.',REASONS[:4],reason(PROFILES[2]),f"Reason: {reason(PROFILES[2])}.",2),card(PROFILES[2])),
 reorder('Because I would like to report the news.','Because + I would like to + report the news.',2),
 text('Rewrite in full: She’d like to be a teacher.','She would like to be a teacher.','She’d = She would trong mẫu đã học.',2),
 tf([('“Because…” can introduce a reason.',True),('“What would you like to be?” asks for a street address.',False)],'Because nêu lý do; would like to be hỏi nghề mong muốn.',2),
 based(text('Write a full sentence about Mai’s future job. Start with “She” and include “in the future”.',third_job(PROFILES[3]),f"Mai: {PROFILES[3]['job']}.",3),card(PROFILES[3])),
 based(text('Hoa is speaking. Give the reason starting with “Because”.',because(PROFILES[5]),f"Reason: {reason(PROFILES[5])}.",3),card(PROFILES[5])),
 based(match([(p['name'],p['job']) for p in PROFILES[:3]],'Ghép tên với nghề từ ba thẻ.',3),'\n\n'.join(card(p) for p in PROFILES[:3])),
 text('Rewrite in full: He’d like to write stories.','He would like to write stories.','He’d = He would.',3),
]

def reading():
 qs=[]
 for p in PROFILES[:2]:
  qs.extend(based(q,passage(p)) for q in [
   text('Write the pupil’s name.',p['name'],f"Bài đọc ghi {p['name']}.",3),
   mc('What would '+p['name']+' like to be?',job_options(p['job']),p['job'],f"Future job: {p['job']}.",3),
   text('Write the reason as a base phrase.',reason(p),f"Bài đọc nói muốn {reason(p)}.",3),
   tf([(p['name']+' would like to be a '+p['job']+'.',True),(p['name']+' would like to be a gardener.',False)],f"Nghề trong bài là {p['job']}.",3),
  ])
 for p in PROFILES[2:4]:
  qs.extend(based(q,passage(p)) for q in [
   match([('Name',p['name']),('Job',p['job']),('Reason',reason(p))],'Ghép thông tin từ bài đọc.',3),
   text(p['name']+' is speaking. Complete: I would like to ___. Write the reason.',reason(p),f"Reason: {reason(p)}.",3),
   mc('Choose the sentence that agrees with the passage.',[job_sentence(p)]+[job_sentence(other) for other in PROFILES[:2]]+['I would like to be a doctor.'],job_sentence(p),f"Bài đọc chọn nghề {p['job']}.",3),
  ])
 cards='\n\n'.join(card(p) for p in PROFILES)
 def find(**facts):
  rows=[p['name'] for p in PROFILES if all(p[k]==v for k,v in facts.items())];assert len(rows)==1;return rows[0]
 qs.extend(based(q,cards) for q in [
  text('Who would like to be a doctor and help people? Write the name.',find(job='doctor'),'Hoa khớp cả nghề doctor và lý do help people.',3),
  text('Who would like to be a reporter and report the news? Write the name.',find(job='reporter'),'Mai: reporter; report the news.',3),
  tf([('Linh and Hoa both want to help people.',all(reason(p)=='help people' for p in [PROFILES[1],PROFILES[5]])),('An and Nam both want to write stories.',all(reason(p)=='write stories' for p in [PROFILES[0],PROFILES[4]]))],'Linh/Hoa cùng help people; Nam teach children, An write stories.',3),
  text('Nam is speaking. Write the full reason starting with “Because”.',because(PROFILES[4]),'Nam muốn teach children.',3),
 ]);return qs

def writing():return [
 text('Complete: I ___ like to be a teacher.','would','I would like to be…'),
 reorder('I would like to be a firefighter.','Would like to be + a firefighter.'),
 text('Complete: I would like ___ grow flowers.','to','Would like to + động từ.',2),
 mc('Choose the correct sentence.',['I would like to be a writer.','I would like be a writer.','I would to like be a writer.','I would likes to be a writer.'],'I would like to be a writer.','Giữ đúng cụm would like to be.'),
 reorder('Why would you like to be a gardener?','Why + would you like to be + nghề?',2),
 text('Complete: Because I would like to ___ children.','teach','Teach children: dạy trẻ em.',2),
 match([('be a','reporter'),('report the','news'),('write','stories')],'Ghép đúng các cụm trong bài.',2),
 text('Complete: I would like to be a ___. Use the word for “bác sĩ”.','doctor','Doctor là bác sĩ.'),
 text('Rewrite in full: I’d like to grow flowers.','I would like to grow flowers.','I’d = I would.',2),
 reorder('Because I would like to help people.','Because + I would like to + lý do.',2),
 text('Rewrite with spaces: Iwouldliketobeawriter.','I would like to be a writer.','Tách I / would / like / to / be / a / writer.'),
 based(text('An is speaking. Complete: I would like to ___. Write the reason.',reason(PROFILES[0]),'Reason: write stories.',2),card(PROFILES[0])),
 text('Write the full form of “He’d” in “He’d like to be a teacher”.','He would','Trong mẫu này, He’d = He would.',2),
 based(reorder(job_sentence(PROFILES[3]),'Dùng nghề trong thẻ Mai.',2),card(PROFILES[3])),
 based(text('Linh is speaking. Write the full job sentence, including “in the future”.',job_sentence(PROFILES[1]),'Linh muốn làm firefighter.',3),card(PROFILES[1])),
 based(text('Write one sentence about Nam’s future job. Start with “He” and include “in the future”.',third_job(PROFILES[4]),'He would like to be a teacher in the future.',3),card(PROFILES[4])),
 based(text('Mai is speaking. Write the full reason starting with “Because”.',because(PROFILES[3]),'Reason: report the news.',3),card(PROFILES[3])),
 based(text('Write one sentence about Hoa’s future job. Start with “She” and include “in the future”.',third_job(PROFILES[5]),'She would like to be a doctor in the future.',3),card(PROFILES[5])),
]

def listening(index):
 a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
 return [
 listen('Listen and choose the future job.',job_sentence(a),[field('Job:',a['job'],list(JOBS))]),
 listen('Listen and choose the reason.',f"I would like to {reason(b)}.",[field('Reason:',reason(b),REASONS)],2),
 listen('Listen. What would '+b['name']+' like to be?',f"My name is {b['name']}. {job_sentence(b)}",[field('Job:',b['job'],list(JOBS))]),
 listen('Listen. Why would '+c['name']+' like to do this job?',f"I would like to be a {c['job']}. {because(c)}",[field('Reason:',reason(c),REASONS)],2),
 listen('Listen and choose the job and reason.',passage(a),[field('Job:',a['job'],list(JOBS)),field('Reason:',reason(a),REASONS)],3),
 listen('Listen and write the job and reason.',passage(c),[field('Job:',c['job']),field('Reason:',reason(c))],3),
 ]

def build_tests():
 import copy
 written=[warmup(),vocabulary(),dialogue(),reading(),writing()]
 mixed=[written[1][0],written[4][0],written[0][4],written[2][3],written[1][2],written[4][6],written[1][6],written[0][7],written[2][8],written[0][10],written[3][10],written[1][12],written[2][12],written[4][11],written[3][14],written[3][15],written[4][16],written[3][16]]
 return [assemble(copy.deepcopy(qs),listening(i)) for i,qs in enumerate(written+[mixed])]
