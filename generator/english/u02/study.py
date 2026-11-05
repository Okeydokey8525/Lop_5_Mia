"""Original learning companion within verified Unit 2 pages 16–21."""
from english.u02.content import HOMES, MEANINGS, picture
from english.study.author import word as w, question as q, choice as c, dialogue as d
from english.study.render import render_study as render


def data():
    words=[w('homes',name,vn,'I live in a '+name+'.',image=name) for name,vn in zip(HOMES,MEANINGS)]
    words += [w('address',name,vn,example) for name,vn,example in [
        ('address','địa chỉ','My address is 14 Queen Street.'),('street','đường phố','I live at 14 Queen Street.'),
        ('fifteen','mười lăm','My house number is fifteen.'),('sixteen','mười sáu','My house number is sixteen.'),('sixty','sáu mươi','My house number is sixty.')]]
    words += [w('distance',name,vn,example) for name,vn,example in [
        ('near','gần','My home is near my school.'),('far from','xa','My home is far from my school.'),
        ('kilometre','ki-lô-mét','My home is one kilometre from my school.')]]
    dialogues=[
        d('homes','Nói loại nhà','Do you live in a house?','Yes, I do.','Bạn sống trong một ngôi nhà phải không? — Đúng vậy.'),
        d('homes','Trả lời không','Do you live in a tower?','No, I do not. I live in a flat.','Bạn không sống trong tháp; bạn sống trong một căn hộ.'),
        d('address','Địa chỉ giả định','What is your address?','It is 14 Queen Street.','Đây là địa chỉ tưởng tượng để luyện, không cần nhập địa chỉ thật.'),
        d('address','Nghe số nhà','Is your house number sixteen?','Yes, it is sixteen, not sixty.','Sixteen là 16, sixty là 60.'),
        d('distance','Nhà gần trường','Is your home near your school?','Yes, it is. My home is near my school.','Nhà của nhân vật ở gần trường.'),
        d('distance','Nhà xa trường','Is your home near your school?','No, it is not. My home is far from my school.','Nhà của nhân vật ở xa trường.'),
    ]
    exercises=[
        c('home-listen','homes','Which home do you hear?','flat','Flat là một căn hộ bên trong tòa nhà.',HOMES,speech='I live in a flat.'),
        q('home-spell','homes','h o u _ e — Write the whole word.','house','House viết có chữ s trước e.'),
        q('home-question','homes','Do you ___ in this house?','live','Sau Do you dùng live.'),
        q('home-reply','homes','Do you live in that flat? Yes, I ___.','do','Yes, I do.'),
        q('address-spell','address','a d d r _ s s — Write the whole word.','address','Address có hai chữ d và hai chữ s.'),
        q('address-at','address','I live ___ 14 Queen Street.','at','At đứng trước địa chỉ cụ thể.'),
        c('address-listen','address','What is the house number?','16','Sixteen là 16; sixty là 60.',['15','16','60','6'],speech='My address is sixteen King Street.'),
        q('address-full','address','Card: 26 Oxford Street. What is your address? Start with It is.','It is 26 Oxford Street.','Viết It is + địa chỉ trong thẻ.'),
        c('distance-listen','distance','Is the home near or far from school?','near','Lời nghe nói near my school.',['near','far from'],speech='My home is near my school.'),
        q('distance-from','distance','My home is far ___ my school.','from','Dùng cụm far from.'),
        c('distance-unit','distance','Which word means “ki-lô-mét”?','kilometre','Kilometre là đơn vị khoảng cách.',['street','kilometre','address','flat']),
        q('distance-in','distance','I live ___ a house.','in','In + loại nhà; at + địa chỉ cụ thể.'),
    ]
    return dict(unit=2,key='mia5:learn:en-u02-v1',intro='Học nhà ở, địa chỉ tưởng tượng và khoảng cách. Không nhập địa chỉ thật của em.',
        groups=[dict(id='homes',name='Nhà ở',tip='Do you live in this/that…? — Yes, I do./No, I don’t. This là này, that là kia; cần ngữ cảnh gần/xa. Tower cũng là một loại building, không phân biệt hai từ chỉ bằng tranh.'),
                dict(id='address',name='Địa chỉ và số',tip='I live in + loại nhà; I live at + số nhà và tên đường. Fif-TEEN, six-TEEN nhấn âm sau; SIX-ty nhấn âm đầu. Giọng máy có thể thay đổi trọng âm theo câu.'),
                dict(id='distance',name='Gần và xa',tip='Near = gần; far from = xa. One kilometre, two kilometres. Các địa chỉ đều giả định.')],
        words=words,dialogues=dialogues,exercises=exercises)


def render_study():return render(data(),picture)
