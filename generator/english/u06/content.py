"""Original school-room exercises; verified textbook pages 44–49."""
from english.practice import mc,text,match,reorder,tf,based,picture as image,field,listen,assemble

CORE=['library','computer room','music room','art room']
MEANINGS=['thư viện','phòng máy tính','phòng âm nhạc','phòng mĩ thuật']
FLOORS=['ground','first','second','third']
TURNS=['left','right']
LABELS=dict(zip(CORE,MEANINGS))
def picture(room,width=320):return image('u06',room.replace(' ','-'),'Tranh phòng học: hãy quan sát đồ dùng để nhận biết.',width)
def school(index):
    return [dict(room=room,floor=FLOORS[(k+index)%4],turn=TURNS[(k+index)%2]) for k,room in enumerate(CORE)]
def location(r):return f"It is on the {r['floor']} floor."
def direction(r):return ('Go upstairs, go' if r['floor']!='ground' else 'Go')+f" along the corridor and turn {r['turn']}."
def card(rows):return 'School plan (start on the ground floor):\n'+'\n'.join(f"{r['room']}: {r['floor']} floor; turn {r['turn']}." for r in rows)
def passage(r):return f"This is our school. We have {'an' if r['room']=='art room' else 'a'} {r['room']}. The {r['room']} is on the {r['floor']} floor. {direction(r)}"
def facts(q,rows):return based(q,card(rows))

def warmup(rows):
    a,b,c,d=rows
    return [
      mc('Look at the picture. Choose the school room.',CORE,a['room'],f"Tranh có đồ dùng đặc trưng của {a['room']} ({LABELS[a['room']]}).",1,picture(a['room'])),
      match(list(zip(CORE,MEANINGS)),'Ghép tên phòng học với nghĩa tiếng Việt.'),
      text('Complete: the ___ floor. Use the word for “tầng trệt”.','ground','Ground floor là tầng trệt; không đổi thành first floor.'),
      mc('Which word means “thứ ba”?',FLOORS,'third','Third là thứ ba; tầng trệt dùng ground.'),
      text('Complete: Where ___ the library?','is','Where is the + tên phòng?'),
      reorder('It is on the first floor.','Dùng on the + từ chỉ tầng + floor.'),
      facts(mc('Where is the '+b['room']+'?',[f'on the {f} floor' for f in FLOORS],f"on the {b['floor']} floor",f"Thẻ ghi {b['room']}: {b['floor']} floor."),rows),
      mc('Choose the polite question.',['Could you tell me the way to the art room, please?','What colour is the art room?','How old is the art room?','What is your name?'],'Could you tell me the way to the art room, please?','Could you tell me the way to…? dùng để hỏi đường lịch sự.',2),
      match([('go upstairs','đi lên tầng trên'),('go downstairs','đi xuống tầng dưới'),('turn left','rẽ trái')],'Ghép chỉ dẫn với nghĩa.',2),
      text('Complete: Go along the ___.','corridor','Go along the corridor: đi dọc hành lang.',2),
      facts(text('Write the floor word for the '+c['room']+'.',c['floor'],f"Tìm {c['room']} trong thẻ: {c['floor']} floor.",2),rows),
      reorder('Go past the library and turn right.','Go past: đi qua; turn right: rẽ phải.',2),
      mc('Start on the third floor. The room is on the ground floor. Choose the direction.',['Go downstairs.','Go upstairs.','Stay on the third floor.','It is a book.'],'Go downstairs.','Từ tầng trên xuống tầng trệt: go downstairs.',2),
      text('Rewrite in full: Where’s the music room?','Where is the music room?','Where’s = Where is.',2),
      facts(text('Write a full sentence locating the '+d['room']+'. Start with “It”.',location(d),f"Dùng on the {d['floor']} floor.",3),rows),
      facts(tf([('The '+a['room']+' is on the '+a['floor']+' floor.',True),('The '+b['room']+' is on the '+a['floor']+' floor.',False)],'Hai phòng trong thẻ nằm ở hai tầng khác nhau.',3),rows),
      facts(text('You want the '+c['room']+'. Write only “left” or “right”.',c['turn'],f"Thẻ chỉ turn {c['turn']}.",3),rows),
      reorder('Could you tell me the way to the computer room, please?','Giữ cụm the way to the computer room, please.',3),
    ]

def vocabulary(rows):
    a,b,c,d=rows
    return [mc('Look at the picture. Which school room is it?',CORE,r['room'],f"Nhận biết {r['room']} qua đồ dùng, không đoán tầng từ tranh.",1,picture(r['room'])) for r in rows]+[
      text('Complete: l i b r a _ y. Write the whole word.','library','Library có chữ r trước y.'),
      text('Complete: c o m p u _ e r. Write the whole word.','computer','Computer có chữ t.'),
      match([('ground floor','tầng trệt'),('first floor','tầng thứ nhất phía trên tầng trệt'),('second floor','tầng thứ hai phía trên tầng trệt')],'Dùng cách gọi tầng của sách.'),
      mc('Choose the word for “thứ nhất”.',FLOORS,'first','First là thứ nhất.'),
      match([('left','trái'),('right','phải'),('corridor','hành lang')],'Ghép từ chỉ hướng và nơi đi.',2),
      text('Complete: Go ___ the library. Use the word for “đi qua”.','past','Go past the library: đi qua thư viện.',2),
      mc('Which phrase means “đi lên tầng trên”?',['go upstairs','go downstairs','turn left','turn right'],'go upstairs','Upstairs chỉ hướng đi lên.',2),
      text('Complete: Go ___ the corridor.','along','Go along the corridor.',2),
      reorder('Go downstairs and turn left.','Downstairs: xuống tầng; turn left: rẽ trái.',2),
      tf([('Upstairs and downstairs have stress on the second syllable here.',True),('Ground floor means third floor.',False)],'up-STAIRS, down-STAIRS nhấn âm sau; ground floor là tầng trệt.',3),
      facts(match([(r['room'],r['floor']+' floor') for r in rows],'Ghép từng phòng với đúng tầng theo thẻ.',3),rows),
      facts(text('Name the room on the '+a['floor']+' floor.',a['room'],f"Mỗi tầng có một phòng trong thẻ; đó là {a['room']}.",3),rows),
      facts(text('Write the turn for the '+d['room']+'.',d['turn'],f"Đọc turn {d['turn']} từ thẻ.",3),rows),
      reorder('Where is the music room?','Where is the + tên phòng?',3),
    ]

def dialogue(rows):
    a,b,c,d=rows
    return [
      mc('A: Where is the art room? B: ___.',['It is on the first floor.','I am ten.','I like pink.','She is friendly.'],'It is on the first floor.','Where hỏi vị trí của phòng.'),
      text('Complete: It is ___ the second floor.','on','On the + tầng + floor.'),
      reorder('Where is the computer room?','Where is the computer room?'),
      text('Complete: Could you tell me the ___ to the library, please?','way','The way to + nơi cần đến.'),
      mc('A: Thank you. B: ___.',['You are welcome.','Turn third.','I am a book.','On is school.'],'You are welcome.','You are welcome đáp lại lời cảm ơn.'),
      facts(text('A: Where is the '+a['room']+'? B: It is on the ___ floor.',a['floor'],f"{a['room']}: {a['floor']} floor."),rows),
      match([('Where is the library?','It is on the second floor.'),('Could you tell me the way, please?','Go upstairs and turn left.'),('Thank you.','You are welcome.')],'Ghép câu hỏi/đáp phù hợp.'),
      mc('Choose the question about location.',['Where is the music room?','What is your favourite food?','What nationality is she?','How old are you?'],'Where is the music room?','Where is…? hỏi ở đâu.'),
      facts(text('A: Do I turn left or right for the '+b['room']+'? Write one word.',b['turn'],f"Đọc hướng của {b['room']} trong thẻ.",2),rows),
      reorder('Could you tell me the way to the library, please?','Could you tell me the way to…?, có please.',2),
      text('Rewrite in full: It’s on the third floor.','It is on the third floor.','It’s = It is.',2),
      mc('A: I am on the ground floor. The room is on the second floor. B: ___.',['Go upstairs.','Go downstairs.','Go past the third floor downstairs.','The room is pink.'],'Go upstairs.','Tầng thứ hai cao hơn tầng trệt nên đi lên.',2),
      text('Complete: Go past the music room and ___ left.','turn','Turn left: rẽ trái.',2),
      facts(reorder(location(c),'Dùng đúng tầng đã cho trong thẻ.',2),rows),
      facts(text('Give the full location sentence for the '+d['room']+'. Begin “It”.',location(d),f"It is on the {d['floor']} floor.",3),rows),
      facts(match([(r['room'],r['floor']+' floor') for r in rows[:3]],'Ghép ba phòng với tầng theo thẻ.',3),rows),
      tf([('“Could you…” makes a request polite.',True),('“Where is…” asks for someone’s age.',False)],'Could you…? lịch sự; Where hỏi vị trí.',3),
      reorder('Go along the corridor and turn right.','Đi dọc hành lang rồi rẽ phải.',3),
    ]

def reading(rows):
    qs=[]
    for i,r in enumerate(rows):
        other=rows[(i+1)%4]
        qs.extend(based(q,passage(r)) for q in [
          mc('Which room is described?',CORE,r['room'],f"Bài đọc nêu {r['room']}.",3),
          text('Write only the floor word.',r['floor'],f"Phòng nằm ở {r['floor']} floor.",3),
          mc('Which way do you turn?',['left','right','upstairs','downstairs'],r['turn'],f"Chỉ dẫn có turn {r['turn']}.",3),
          tf([('The room is on the '+r['floor']+' floor.',True),('The room is on the '+other['floor']+' floor.',False)],'Đối chiếu tầng được nói trong bài, không dùng sơ đồ của đề khác.',3),
        ])
    qs += [facts(text('Which room is on the '+rows[0]['floor']+' floor and has a '+rows[0]['turn']+' turn?',rows[0]['room'],'Tìm phòng khớp cả tầng và hướng trong thẻ.',3),rows),
           facts(text('Locate the '+rows[3]['room']+' in a full sentence starting with “It”.',location(rows[3]),'Ghép on the + tầng đúng + floor.',3),rows)]
    return qs

def writing(rows):
    a,b,c,d=rows
    return [
      text('Complete: Where ___ the art room?','is','Where is…?'),
      text('Complete: It is on ___ first floor.','the','On the first floor.'),
      reorder('The library is on the ground floor.','Giữ the ground floor.'),
      text('Rewrite with spaces: Goalongthecorridor.','Go along the corridor.','Go / along / the / corridor.'),
      text('Complete: ___ you tell me the way, please?','Could','Could you…? là lời nhờ lịch sự.'),
      mc('Choose the correct sentence.',['It is on the third floor.','It is in third floor.','It on the third floor.','It is on floor the third.'],'It is on the third floor.','Dùng is on the + third + floor.'),
      reorder('Go upstairs and turn right.','Go upstairs, sau đó turn right.'),
      match([('go','upstairs'),('turn','left'),('on the','ground floor')],'Ghép thành cụm đúng.'),
      text('Rewrite in full: Where’s the library?','Where is the library?','Where’s = Where is.',2),
      text('Complete: The room is on the ___ floor. Use “thứ hai”.','second','Second là thứ hai phía trên tầng trệt.',2),
      reorder('Could you tell me the way to the music room, please?','The way to the music room.',2),
      facts(text('Write one word: the '+a['room']+' is on the ___ floor.',a['floor'],'Chọn tầng theo thẻ.',2),rows),
      facts(reorder(location(b),'Sắp xếp theo tầng trong thẻ.',2),rows),
      text('Complete: Go ___ the library and turn left. Use “qua”.','past','Go past the library.',2),
      facts(text('Write a full location sentence about the '+c['room']+'. Start with “It”.',location(c),'Dùng on the + tầng trong thẻ + floor.',3),rows),
      facts(text('Write the room on the '+d['floor']+' floor.',d['room'],'Tìm tên phòng theo tầng, viết đủ tên.',3),rows),
      reorder('Go downstairs, go past the library and turn left.','Giữ thứ tự chỉ dẫn: xuống → đi qua → rẽ trái.',3),
      text('Rewrite in full: It’s on the ground floor.','It is on the ground floor.','It’s = It is; ground floor là tầng trệt.',3),
    ]

def listening(index):
    a,b,c,d=school(index)
    return [
      listen('Listen and choose the room.',f"This is the {a['room']}.",[field('Room:',a['room'],CORE)]),
      listen('Listen and choose the floor.',location(b),[field('Floor:',b['floor'],FLOORS)]),
      listen('Listen. Which floor is the room on?',f"We have a {c['room']}. {location(c)}",[field('Floor:',c['floor'],FLOORS)]),
      listen('Listen and choose the turn.',f"Go along the corridor. Turn {d['turn']}.",[field('Turn:',d['turn'],TURNS)],2),
      listen('Listen and choose the room and floor.',passage(a),[field('Room:',a['room'],CORE),field('Floor:',a['floor'],FLOORS)],3),
      listen('Listen and write the floor word and turn.',passage(c),[field('Floor:',c['floor']),field('Turn:',c['turn'])],3),
    ]

def build_tests():
    import copy
    fns=[warmup,vocabulary,dialogue,reading,writing]
    result=[assemble(fn(school(i)),listening(i)) for i,fn in enumerate(fns)]
    sources=[fn(school(5)) for fn in fns]
    mixed=[copy.deepcopy(sources[i%5][i]) for i in range(18)]
    return result+[assemble(mixed,listening(5))]
