"""Solve numeric constraints from emitted question text, independently of generators."""
import json
import re
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def numbers(text):
    return [F(s.replace('\u00a0','').replace(' ','').replace(',','.'))
            for s in re.findall(r'\d+(?:[ \u00a0]\d{3})*(?:,\d+)?',text)]


def answers(q):
    return [F(str(b['ans'])) if b['kind']=='num' else F(*b['ans'])
            for b in q['blanks'] if b['kind'] in ('num','frac')]


def equal(actual, expected):
    assert actual == list(map(F,expected)), (actual,expected)


def audit7(qs):
    # Inverse checks against the numbers actually shown to the pupil.
    a,b=numbers(qs[0]['stem'])
    equal(answers(qs[0]),[a/b])
    equal(answers(qs[1]),[b/a,a/(a+b)])
    p,total=numbers(qs[3]['stem']); result,=answers(qs[3]); assert result*100==p*total
    _,scale,length=numbers(qs[5]['stem']); result,=answers(qs[5]); assert result*100==length*scale
    for k,kind in [(6,'sum'),(7,'difference'),(12,'sum'),(13,'difference')]:
        value,num,den=numbers(qs[k]['stem']); x,y=answers(qs[k])
        assert (x+y if kind=='sum' else y-x)==value
        assert (x/y if k!=13 else y/x)==num/den
    x,y=numbers(qs[9]['stem']); equal(answers(qs[9]),[x*y])
    total,part=numbers(qs[10]['stem']); x,y=answers(qs[10]); assert x+y==100 and x*total==part*100
    length,_,scale=numbers(qs[11]['stem']); equal(answers(qs[11]),[length*100/scale])
    price,p=numbers(qs[14]['stem']); discount,paid=answers(qs[14]); assert discount+paid==price and discount*100==price*p
    for blank in qs[15]['blanks']:
        ns=numbers(blank['pre']); expected=ns[0]+ns[1] if '+' in blank['pre'] else ns[0]*ns[1]
        assert F(str(blank['ans']))==expected
    total,num,den,used=numbers(qs[18]['stem']); x,left=answers(qs[18]); assert x-left==used and x*(num+den)==total*num
    diff,num,den,price=numbers(qs[19]['stem']); sold,revenue=answers(qs[19]); assert sold*(den-num)==diff*den and revenue==sold*price
    _,scale,leg1,leg2=numbers(qs[20]['stem']); length,real=answers(qs[20]); assert length==leg1+leg2 and real*100==length*scale
    p,threshold,price,count=numbers(qs[21]['stem']); raw,paid=answers(qs[21]); assert raw==price*count
    assert paid==(raw*(100-p)/100 if count>=threshold else raw)
    total,p,fee=numbers(qs[22]['stem']); reserve,left=answers(qs[22]); assert reserve*100==total*p and left+reserve+fee==total
    plan,done=numbers(qs[23]['stem']); achieved,excess=answers(qs[23]); assert achieved*plan==done*100 and excess+100==achieved
    # Definition/key questions and truth values are checked separately from arithmetic.
    assert qs[2]['opts'][qs[2]['answer']]==str(int(numbers(qs[2]['stem'])[0]))+'%'
    assert qs[4]['opts'][qs[4]['answer']].endswith('cm ngoài thực tế')
    correct=qs[8]['opts'][qs[8]['answer']]
    key=re.search(r'phím (.*?) dùng',qs[8]['stem'])[1]
    assert correct=={'CE':'xóa số vừa nhập','OFF':'tắt máy','=':'hiện kết quả','ON/C':'bật máy hoặc xóa toàn bộ phép tính'}[key]
    assert [it['a'] for it in qs[17]['items']]==[True,False,True,False]


UNITS={'m³':F(1000000),'dm³':F(1000),'cm³':F(1)}


def volume(text):
    match=re.fullmatch(r'([\d,\s\u00a0]+)\s*(cm³|dm³|m³)',text.strip())
    assert match,text
    return numbers(match[1])[0]*UNITS[match[2]]


def audit8(qs):
    assert qs[0]['opts'][qs[0]['answer']]=='hình lập phương cạnh 1 cm'
    assert qs[3]['opts'][qs[3]['answer']]=='1 000 dm³'
    assert qs[9]['opts'][qs[9]['answer']]=='m³'
    for k in [1,18]:
        # One front rectangle is exactly one visible cube; top/side polygons are not cubes.
        count=qs[k]['fig'].count('<rect ')
        assert answers(qs[k])[0]==count
        if k==18:
            added=numbers(qs[k]['stem'])[-1]
            assert answers(qs[k])[1]==count+added
    for k in [2,4,5]:
        blank=qs[k]['blanks'][0]
        assert volume(blank['pre'].removesuffix('=').strip())==F(str(blank['ans']))*UNITS[blank['post']]
    assert [it['a'] for it in qs[6]['items']]==[True,True,False]
    for k in [7,12]:
        for blank in qs[k]['blanks']:
            left,right=volume(blank['pre']),volume(blank['post'])
            assert blank['ans']==('>' if left>right else '<' if left<right else '=')
    for blank in qs[8]['blanks']:
        left,right=re.split(r' [+−] ',blank['pre'].removesuffix(' ='))
        expected=volume(left)+volume(right) if ' + ' in blank['pre'] else volume(left)-volume(right)
        assert F(str(blank['ans']))*UNITS[blank['post']]==expected
    for blank in qs[10]['blanks']:
        ns=numbers(blank['pre']); expected=ns[0]*1000+ns[1]
        assert F(str(blank['ans']))*UNITS[blank['post']]==expected
    vals=list(map(volume,qs[11]['items'])); assert all(x<y for x,y in zip(vals,vals[1:]))
    layers,per=numbers(qs[13]['stem']); equal(answers(qs[13]),[layers*per])
    initial,removed,*_=numbers(qs[14]['stem']); remain,each=answers(qs[14]); assert remain==initial-removed and 2*each==remain and each.denominator==1
    bottles,each,*_=numbers(qs[15]['stem']); dm,cm=answers(qs[15]); assert dm==bottles*each and dm*1000==cm
    assert [it['a'] for it in qs[16]['items']]==[True,False,True,True]
    cells=re.findall(r'<td>(.*?)</td>',qs[17]['fig']); equal(answers(qs[17]),[(volume(cells[0])+volume(cells[1]))/1000000])
    water,capacity,*_=numbers(qs[19]['stem']); cm,cups=answers(qs[19]); assert water*1000==cm and cups*capacity==cm and cups.denominator==1
    total,pct=numbers(qs[20]['stem']); free_pct,free,dm=answers(qs[20]); assert free_pct+pct==100 and free*100==total*free_pct and free*1000==dm
    limit,rate1,_,rate2,used=numbers(qs[21]['stem']); first,total=answers(qs[21]); assert first==limit*rate1 and total-first==(used-limit)*rate2
    months,total=numbers(qs[22]['stem']); avg,dm=answers(qs[22]); assert avg*months==total and dm==avg*1000
    layers,per,unit,removed=numbers(qs[23]['stem']); initial,remain=answers(qs[23]); assert initial==layers*per and remain==(initial-removed)*1000 and unit==1


def main():
    checked=0
    for cd,audit,lessons in [(7,audit7,set(range(36,45))),(8,audit8,set(range(45,49)))]:
        previous=[]
        for i in range(1,7):
            text=(ROOT/f'generator/tests/cd{cd}/de0{i}.js').read_text(encoding='utf-8')
            qs=json.loads(text.split(f'return MK{cd}(',1)[1].rsplit(');',1)[0])
            assert len(qs)==24 and {q['lesson'] for q in qs}==lessons
            assert {q['type'] for q in qs}=={'fill','mc','tf','order'}
            assert all(q['why'] for q in qs)
            assert qs not in previous; previous.append(qs)
            try:
                audit(qs)
            except (AssertionError,ValueError) as err:
                raise AssertionError(f'cd{cd} de{i}: {err}') from err
            checked+=len(qs)
    print(f'Math volume 2 content PASS: {checked} questions, 12 exams, exact independent constraints; lessons, diagrams and counts checked.')


if __name__=='__main__':
    main()
