"""Listening questions derived from shared facts, six per version-2 exam."""
import re
from english.u01.content import PROFILES, picture

def make_listening(index):
    pupils=PROFILES+[dict(name='Nam',cls='5E',place='city',colour='blue',sport='swimming',food='pizza',animal='a dolphin'),dict(name='Hoa',cls='5G',place='countryside',colour='pink',sport='football',food='a sandwich',animal='a panda')]
    a=pupils[index];b=pupils[(index+1)%6];c=pupils[(index+2)%6]
    def field(label,answer,options=None):
        return dict(label=label,answer=answer,options=options,alternatives=[])
    def make(level,stem,transcript,fields,lesson=2,fig=None):
        q=dict(type='listen',level=level,lesson=lesson,stem=stem,speech=re.sub(r'Class 5([A-Z])',r'Class five \1',transcript),transcript=transcript,fields=fields,
               why='Thông tin trong lời nghe: '+ '; '.join(f['label']+' '+f['answer'] for f in fields)+'.')
        if fig:q['fig']=fig
        return q
    # Focus shifts by exam; answers always use the same facts as the speech.
    first=[('name','name','My name is '+a['name']+'.',['An','Linh','Minh','Mai','Nam','Hoa']),('place','home','I live in the '+a['place']+'.',['city','countryside']),('cls','class','I am in Class '+a['cls']+'.',[p['cls'] for p in pupils]),('animal','favourite animal','My favourite animal is '+a['animal']+'.',['a dolphin','a panda']),('colour','favourite colour','My favourite colour is '+a['colour']+'.',['pink','blue','green','red']),('food','favourite food','My favourite food is '+a['food']+'.',['pizza','a sandwich','fish and chips'])][index]
    key,label,line,options=first
    return [
      make('tb','Listen and choose the '+label+'.',line,[field(label,a[key],options)],1 if index<3 else 2),
      make('tb','Listen and choose the place to live.','I live in the '+b['place']+'.',[field('Home:',b['place'],['city','countryside'])],1, '<div style="display:flex;flex-wrap:wrap;gap:12px">'+picture('city',220)+picture('countryside',220)+'</div>'),
      make('kha','What is '+b['name']+'’s favourite sport?','My name is '+b['name']+'. My favourite sport is '+b['sport']+'.',[field('Sport:',b['sport'],['table tennis','swimming','football','basketball'])]),
      make('kha','Listen and choose the favourite '+('food' if index%2 else 'colour')+'.','My name is '+c['name']+'. My favourite '+('food is '+c['food'] if index%2 else 'colour is '+c['colour'])+'.',[field('Food:' if index%2 else 'Colour:',c['food'] if index%2 else c['colour'],['pizza','a sandwich','fish and chips'] if index%2 else ['pink','blue','green','red'])]),
      make('gioi','Listen to '+a['name']+'. Choose the home and favourite animal.','My name is '+a['name']+'. I am in Class '+a['cls']+'. I live in the '+a['place']+'. My favourite animal is '+a['animal']+'.',[field('Home:',a['place'],['city','countryside']),field('Animal:',a['animal'],['a dolphin','a panda'])],3),
      make('gioi','Listen to '+c['name']+'. Write the favourite colour and sport.','My name is '+c['name']+'. I live in the '+c['place']+'. My favourite colour is '+c['colour']+'. My favourite sport is '+c['sport']+'.',[field('Colour:',c['colour']),field('Sport:',c['sport'])],3),
    ]
