"""Original Review 4: printed 70-73, exactly Units 16-20."""
from english.practice import mc, text as base_text, match, reorder, tf, based, listen, field, assemble
from english.u17.content import picture as animal_picture
from english.u18.content import picture as transport_picture
from english.u19.content import picture as place_picture
from english.u20.content import picture as summer_picture

CORE=['tortoise','bus','waterfall','go camping']
WEATHER=['cold and dry','hot and sunny','warm and rainy','cool and windy']
CLOTHES=['a jumper and trousers','a T-shirt and shorts','a blouse and jeans','a jacket and trousers']
ANIMALS=['tortoise','hare','ant','grasshopper']
PAST=['walked slowly','ran fast','worked hard','sang beautifully']
TRANSPORT=['by bus','by bicycle','by taxi','on foot']
PLACES=['the waterfall','the lake','the cave','the old town']
OPINIONS=['beautiful','peaceful','fantastic','interesting']
SUMMER=['go camping','join a music club','visit an eco-farm','practise swimming']
DISTANCE=['three kilometres','five kilometres','seven kilometres','nine kilometres']
PROFILES=[dict(name=n,weather=WEATHER[i%4],clothes=CLOTHES[i%4],animal=ANIMALS[i%4],past=PAST[i%4],transport=TRANSPORT[(i+1)%4],place=PLACES[i%4],opinion=OPINIONS[(i+1)%4],summer=SUMMER[(i+2)%4],distance=DISTANCE[i%4]) for i,n in enumerate(['An','Linh','Minh','Hoa','Nam','Mai'])]
SUMMER_PLACES=['Huong River','Phong Nha Cave','Phu Quoc Island','Dam Sen Aquarium']
for i,p in enumerate(PROFILES):p['summer_place']=SUMMER_PLACES[(i+1+i//4)%4]


def text(stem,answer,why,lesson=1,alternatives=()):
    accepted=list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        for a,b in [('They are',"They're"),('I am',"I'm"),('it is',"it's"),('did not',"didn't"),('cannot',"can't")]:
            if a in answer:accepted.append(answer.replace(a,b))
    if 'practise' in answer:accepted.append(answer.replace('practise','practice'))
    return base_text(stem,answer,why,lesson,accepted)


def picture(word,width=320):
    if word=='bus':return transport_picture('by bus',width)
    return {'tortoise':animal_picture,'waterfall':place_picture,'go camping':summer_picture}[word](word,width)
def tag(q,*units):q['sourceUnits']=list(units);return q


def card(p):
    return f"Fictional profile: {p['name']} · Weather on this card: {p['weather']} · Usual clothes in this weather: {p['clothes']} · Story character: {p['animal']} · Story action: {p['past']} · Place to visit: {p['place']} · Transport: {p['transport']} · Imaginary distance from home: {p['distance']} · Opinion: {p['opinion']} · Summer destination: {p['summer_place']} · Summer activity: {p['summer']}."


def passage(p):
    return f"My name is {p['name']}. In my weather diary, it is {p['weather']}. In this weather, I usually wear {p['clothes']}. In my little story, the {p['animal']} {p['past']}. I want to visit {p['place']}. I can get there {p['transport']}. On my imaginary map, it is {p['distance']} from my home to {p['place']}. I think it is {p['opinion']}. This summer, I am going to visit {p['summer_place']}. I am also going to {p['summer']} during the holidays."


def shown(q,p,*units):return tag(based(q,card(p)),*units)


def written(index,kind):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    if kind==3:
        result=[]
        for p in [a,b,c]:
            result += [tag(based(q,passage(p)),u) for q,u in [
                (text('Write the weather phrase only.',p['weather'],'Đọc diary, không suy khí hậu của cả nơi.'),16),
                (text('Write the main animal character only.',p['animal'],'Đọc my little story.'),17),
                (text('Write the full transport phrase, including by or on.',p['transport'],'By + phương tiện; on foot.',2),18),
                (text('Write the imaginary distance in words.',p['distance'],'Khoảng cách trong bản đồ giả định, không phải số liệu thực.',2),19),
                (text('Write only the summer activity phrase, after going to.',p['summer'],'Lấy dự định hè, không lấy hành động của nhân vật truyện.',3),20),
                (text('Write the place opinion adjective only.',p['opinion'],'Đúng ý kiến của người kể.',3),19)]]
        result[0]=tag(based(tf([(f"The diary says it is {a['weather']}.",True),(f"The diary says it is {b['weather']}.",False)],'Đọc thời tiết trong đúng nhật ký.'),passage(a)),16)
        result[1]=tag(based(mc('Who is the main animal character?',ANIMALS,a['animal'],'Lấy nhân vật trong truyện tự soạn.'),passage(a)),17)
        result[5]=tag(based(text('Write only the summer destination, not the place on the imaginary map.',a['summer_place'],'Tìm going to visit trong kế hoạch hè, không lấy want to visit.',3),passage(a)),20)
        return result
    if kind==4:
        result=[]
        for p in [a,b,c]:
            result += [shown(q,p,u) for q,u in [
                (text('Write the weather sentence, starting with It.',f"It is {p['weather']}.",'It is + thời tiết.'),16),
                (text('Write the story sentence, starting with The; use the past action.',f"The {p['animal']} {p['past']}.",'Câu kể quá khứ theo thẻ.'),17),
                (text('Write the transport reply, starting with You can get there.',f"You can get there {p['transport']}.",'Can + get; đúng by/on.',2),18),
                (text('Write the opinion sentence, starting with I think it.',f"I think it is {p['opinion']}.",'Một nơi dùng it is.',2),19),
                (text('Write the summer plan sentence, starting with I am going to.',f"I am going to {p['summer']}.",'Am going to + nguyên mẫu.',3),20),
                (text('Write the imaginary distance reply, starting with It is.',f"It is {p['distance']}.",'Chỉ viết câu trả lời khoảng cách, không thêm nơi.',3),19)]]
        result[0]=tag(reorder('What do you usually wear in winter?','Do + wear.'),16)
        result[1]=tag(mc('Choose the correct question about the past.',['How did the hare run?','How did the hare ran?','How does the hare ran?','How did the hare runs?'],'How did the hare run?','Did + run nguyên mẫu.'),17)
        result[5]=shown(text('Write the summer destination plan, starting with I am going to visit.',f"I am going to visit {a['summer_place']}.",'Nơi sẽ đến trong kế hoạch hè, không lấy nơi trên bản đồ.',3),a,20)
        return result
    if kind==2:
        return [
            tag(text('Complete: What do you usually ___ in summer?','wear','Do + wear.'),16),
            tag(text('Complete: How did the tortoise ___? Use walk.','walk','Did + walk.'),17),
            shown(text('Where do you want to visit? Start with I want to visit.',f"I want to visit {a['place']}.",'Want to visit + nơi.'),a,18),
            tag(mc('Which question asks about distance?',['How far is it?','How can I get there?','What is it like?','How did it run?'],'How far is it?','How far hỏi khoảng cách.'),19),
            shown(text('What are you going to do this summer? Start with I am going to.',f"I am going to {a['summer']}.",'Going to + hoạt động.'),a,20),
            tag(reorder('How can I get to the lake?','Can + get; get to + nơi.'),18),
            shown(text('How is the weather on this card? Start with It.',f"It is {b['weather']}.",'Đọc thời tiết của đúng thẻ.',2),b,16),
            shown(text('How did the animal act? Write only the past action phrase.',b['past'],'Lấy Story action, không lấy Summer activity.',2),b,17),
            tag(text('Rewrite in full: I’m going to go camping.','I am going to go camping.','I’m = I am.',2),20),
            tag(text('Complete: I think the waterfalls ___ beautiful.','are','Waterfalls số nhiều → are.',2),19),
            tag(text('Rewrite in full: I can’t get there by bus.','I cannot get there by bus.','Can’t = cannot; get nguyên mẫu.',2),18),
            tag(match([('How is the weather?','It is hot and sunny.'),('Who is the main character?','The tortoise.'),('How far is it?','Three kilometres.')],'Ghép đúng loại câu hỏi.',2),16,17,19),
            shown(text('Write the clothes reply, starting with I usually wear.',f"I usually wear {c['clothes']}.",'Theo thời tiết trong thẻ.',2),c,16),
            tag(tf([('After did, use a base verb.',True),('Use by foot for walking.',False)],'Did + nguyên mẫu; on foot.',3),17,18),
            tag(text('Rewrite in full: They’re going to visit an eco-farm.','They are going to visit an eco-farm.','They’re = They are.',3),20),
            shown(text('Write transport then opinion as two sentences: start with You can get there, then I think it.',f"You can get there {b['transport']}. I think it is {b['opinion']}.",'Đúng phương tiện và ý kiến của cùng thẻ.',3),b,18,19),
            shown(text('Write the story sentence, starting with The.',f"The {c['animal']} {c['past']}.",'Đọc đúng nhân vật và hành động quá khứ.',3),c,17),
            shown(text('Where are you going to visit this summer? Start with I am going to visit.',f"I am going to visit {c['summer_place']}.",'Lấy Summer destination, không lấy Place to visit hoặc hoạt động.',3),c,20)]
    result=[
        tag(mc('Choose the word for the animal in the picture.',ANIMALS,'tortoise','Rùa cạn trong tranh.',1,picture('tortoise')),17),
        shown(text('Write only the weather phrase.',a['weather'],'Đọc Weather.'),a,16),
        shown(text('Write only the place to visit, including the.',a['place'],'Đọc Place to visit.'),a,18),
        shown(text('Write only the opinion adjective.',a['opinion'],'Opinion khác thời tiết.'),a,19),
        shown(text('Write only the summer activity phrase.',a['summer'],'Đọc Summer activity.'),a,20),
        tag(match([('windy','có gió'),('walked slowly','đã đi chậm'),('on foot','đi bộ')],'Ghép từ ôn ba Unit.'),16,17,18),
        tag(text('Complete: How did the hare ___? Use run.','run','Did + run.'),17),
        tag(text('Complete: She is going to ___ a music club.','join','Going to + join.'),20),
        shown(text('Write the full transport phrase.',b['transport'],'Giữ by/on.',2),b,18),
        tag(reorder('I think it is fantastic.','Một nơi dùng it is.',2),19),
        shown(text('Write only the usual clothes phrase.',b['clothes'],'Theo thẻ, không suy ra mọi mùa giống nhau.',2),b,16),
        tag(text('Complete: We can get there ___ foot.','on','On foot, không by foot.',2),18),
        shown(text('Write the distance in words.',c['distance'],'Khoảng cách giả định.',2),c,19),
        tag(tf([('This summer can introduce a new plan.',True),('Last summer always means a future plan.',False)],'Phân biệt việc đã qua với kế hoạch mới.',3),17,20),
        shown(text('Write the story sentence, starting with The.',f"The {c['animal']} {c['past']}.",'Dùng quá khứ theo truyện.',3),c,17),
        shown(text('Write the plan sentence, starting with I am going to.',f"I am going to {b['summer']}.",'Đúng chủ ngữ và nguyên mẫu.',3),b,20),
        shown(text('Write the opinion sentence, starting with I think it.',f"I think it is {a['opinion']}.",'Ý kiến theo người, không có đáp án cảm nhận duy nhất.',3),a,19),
        shown(text('Write weather then clothes: start with It, then I usually wear.',f"It is {c['weather']}. I usually wear {c['clothes']}.",'Tìm đủ hai thông tin.',3),c,16)]
    if kind==1:
        result[:4]=[tag(mc('Choose the phrase for this picture.',CORE,k,'Nhận ra đúng chủ thể, không đoán địa danh.',1,picture(k)),u) for k,u in zip(CORE,[17,18,19,20])]
        result[12]=tag(based(mc('Extension: Which story type is on the card?',['adventure story','mystery story','history story','spooky story'],'mystery story','Đọc nhãn thể loại trong thẻ, không cần biết tác phẩm ngoài bài.',2),'Original reading card: Title: The Missing Red Kite. Type: mystery story. Two friends look for clues to find their kite.'),17)
    return result


def listening(index):
    a,b,c=[PROFILES[(index+k)%6] for k in range(3)]
    return [
        tag(listen('Listen and choose the weather.',f"In my weather diary, it is {a['weather']}.",[field('Weather:',a['weather'],WEATHER)]),16),
        tag(listen('Listen and choose the main character.',f"In my story, the {b['animal']} {b['past']}.",[field('Character:',b['animal'],ANIMALS)]),17),
        tag(listen('Listen and find the transport.',f"I want to visit {c['place']}. I can get there {c['transport']}.",[field('Transport:',c['transport'],TRANSPORT)],2),18),
        tag(listen('Listen for the opinion, not the weather.',f"It is {a['weather']} today. I think {a['place']} is {a['opinion']}.",[field('Opinion:',a['opinion'],OPINIONS)],2),16,19),
        tag(listen('Listen for imaginary distance and summer activity.',f"On my imaginary map, it is {b['distance']} from my home to {b['place']}. This summer, I am going to {b['summer']}.",[field('Distance:',b['distance'],DISTANCE),field('Summer activity:',b['summer'],SUMMER)],3),19,20),
        tag(listen('Listen and write the story action, then the new summer activity.',f"In my story, the {c['animal']} {c['past']}. This summer, I am going to {c['summer']}.",[field('Story action:',c['past']),field('Summer activity:',c['summer'])],3),17,20)]


def build_tests():return [assemble(written(i,i) if i<5 else [written(i,k%5)[k] for k in range(18)],listening(i)) for i in range(6)]
