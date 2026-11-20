"""Independent exact checks against emitted text, including physical cube-net folding."""
import json,re
from fractions import Fraction as F
from pathlib import Path
from audit_math_volume2 import numbers,answers,equal,volume
ROOT=Path(__file__).resolve().parents[1]


def fold(cells):
    cells=set(cells);orientation={next(iter(cells)):((1,0,0),(0,1,0),(0,0,1))};todo=list(orientation)
    neg=lambda v:tuple(-x for x in v)
    while todo:
        x,y=todo.pop();u,v,n=orientation[x,y]
        for dx,dy,basis in [(1,0,(neg(n),v,u)),(-1,0,(n,v,neg(u))),(0,1,(u,neg(n),v)),(0,-1,(u,n,neg(v)))]:
            other=(x+dx,y+dy)
            if other not in cells:continue
            if other in orientation:
                if orientation[other]!=basis:return False
            else:orientation[other]=basis;todo.append(other)
    return len(orientation)==6 and len({basis[2] for basis in orientation.values()})==6


def audit9(q):
    assert q[0]['opts'][q[0]['answer']]=='hình trụ'
    nets=re.findall(r'data-cube-net="([^"]+)"',q[1]['fig'])
    valid=[fold([tuple(map(int,p.split(','))) for p in net.split(';')]) for net in nets]
    assert len(valid)==4 and sum(valid)==1 and valid[q[1]['answer']],valid
    a,b,h=numbers(q[2]['stem']);equal(answers(q[2]),[2*(a+b)*h]);equal(answers(q[3]),[2*(a*b+a*h+b*h)])
    c,=numbers(q[4]['stem']);assert numbers(q[4]['opts'][q[4]['answer']])[0]==4*c*c
    c,=numbers(q[5]['stem']);equal(answers(q[5]),[6*c*c])
    a,b,h=numbers(q[6]['stem']);equal(answers(q[6]),[a*b*h])
    c,=numbers(q[7]['stem']);equal(answers(q[7]),[c**3])
    for blank in q[8]['blanks']:
        a,b=volume(blank['pre']),volume(blank['post']);assert blank['ans']==('>' if a>b else '<' if a<b else '=')
    assert [x['a'] for x in q[9]['items']]==[True,False,True]
    a,b,h=numbers(q[10]['stem']);equal(answers(q[10]),[2*(a+b)*h,2*(a+b)*h+a*b])
    c,=numbers(q[11]['stem']);equal(answers(q[11]),[5*c*c])
    a,b,h=numbers(q[12]['stem']);equal(answers(q[12]),[100*a,100*a*b*h])
    a,b,low,high=numbers(q[13]['stem']);equal(answers(q[13]),[high-low,a*b*(high-low)])
    vs=list(map(volume,q[14]['items']));assert all(a<b for a,b in zip(vs,vs[1:]))
    a,b,h,c=numbers(q[15]['stem']);assert all(v%c==0 for v in [a,b,h]);equal(answers(q[15]),[(a//c)*(b//c),(a//c)*(b//c)*(h//c)])
    assert [x['a'] for x in q[16]['items']]==[True,False,True]
    v,a,b=numbers(q[17]['stem']);equal(answers(q[17]),[v/(a*b)])
    a,b,h,opening,rate=numbers(q[18]['stem']);area=2*(a+b)*h-opening;equal(answers(q[18]),[area,area*rate])
    a,b,h,c=numbers(q[19]['stem']);assert c<=min(a,b,h);equal(answers(q[19]),[c**3,a*b*h-c**3])
    c,=numbers(q[20]['stem']);equal(answers(q[20]),[2*c**3,2*((2*c)*c+(2*c)*c+c*c)])
    v,area=numbers(q[21]['stem']);equal(answers(q[21]),[v/area])
    total,c,a,b,h=numbers(q[22]['stem']);assert total==a*b*h;equal(answers(q[22]),[a*c,total*c**3])
    c,pct,*_=numbers(q[23]['stem']);equal(answers(q[23]),[c**3,c**3*(100-pct)/100])


def normalized(q,total):
    equal(answers(q),divmod(total,60));assert 0<=answers(q)[1]<60


def audit10(q):
    hh,mm=numbers(q[0]['blanks'][0]['pre']);equal(answers(q[0]),[hh*60+mm])
    expected={'tuần':7,'ngày':24,'giờ':60,'thế kỉ':100,'năm':12,'phút':60}
    key=next(k for k in expected if 'Một '+k+' có' in q[1]['stem']);assert numbers(q[1]['opts'][q[1]['answer']])[0]==expected[key]
    a,b,c,*_=numbers(q[2]['stem']);normalized(q[2],a*60+b+c)
    a,b,c,d,*_=numbers(q[3]['stem']);normalized(q[3],a*60+b-c*60-d)
    a,b,c,*_=numbers(q[4]['stem']);normalized(q[4],(a*60+b)*c)
    a,b,c,*_=numbers(q[5]['stem']);normalized(q[5],(a*60+b)/c)
    s,t=numbers(q[6]['stem']);equal(answers(q[6]),[s/t])
    v,t=numbers(q[7]['stem']);equal(answers(q[7]),[v*t])
    s,v=numbers(q[8]['stem']);equal(answers(q[8]),[s/v])
    assert [x['a'] for x in q[9]['items']]==[False,True,True,True]
    km,=numbers(q[10]['blanks'][0]['pre']);equal(answers(q[10]),[km*1000/3600])
    s,t=numbers(q[11]['stem']);v=s/t;rounded=F((v*10+F(1,2))//1,10);equal(answers(q[11]),[rounded])
    hh,mm,dh,dm,rest,*_=numbers(q[12]['stem']);normalized(q[12],(hh*60+mm+dh*60+dm+rest)%1440)
    h1,m1,h2,m2,rest,s=numbers(q[13]['stem']);running=(h2-h1)*60+m2-m1-rest;equal(answers(q[13]),[running,s*60/running])
    factors={'giờ':3600,'phút':60,'giây':1}
    vals=[numbers(v)[0]*factors[v.rsplit(' ',1)[-1]] for v in q[14]['items']];assert all(a<b for a,b in zip(vals,vals[1:]))
    sa,va,sb,vb=numbers(q[15]['stem']);assert q[15]['opts'][q[15]['answer']]==('Đường A' if sa/va<sb/vb else 'Đường B')
    count,total,*_=numbers(q[16]['stem']);normalized(q[16],total/count)
    assert [x['a'] for x in q[17]['items']]==[True,False,True]
    s,va,vb=numbers(q[18]['stem']);equal(answers(q[18]),[s/va*60,s/vb*60,(s/va+s/vb)*60])
    hour,s1,v1,rest,s2,v2=numbers(q[19]['stem']);total=(s1/v1+s2/v2)*60+rest;equal(answers(q[19]),[total,*divmod(hour*60+total,60)])
    train,tunnel,v=numbers(q[20]['stem']);equal(answers(q[20]),[train+tunnel,(train+tunnel)/v])
    d1,t1,d2,t2=numbers(q[21]['stem']);equal(answers(q[21]),[d1+d2,(d1+d2)/(t1+t2)])
    minutes,v1,v2=numbers(q[22]['stem']);equal(answers(q[22]),[minutes*60*v1,minutes*60*v2,minutes*60*(v1+v2)])
    hh,mm,travel,rest,*_=numbers(q[23]['stem']);assert 0<=mm<60;normalized(q[23],(hh*60+mm+travel+rest)%1440)


def main():
    total=0
    for cd,audit,lessons in [(9,audit9,set(range(49,56))),(10,audit10,set(range(56,63)))]:
        seen=[]
        for i in range(1,7):
            text=(ROOT/f'generator/tests/cd{cd}/de0{i}.js').read_text(encoding='utf-8')
            q=json.loads(text.split(f'return MK{cd}(',1)[1].rsplit(');',1)[0])
            assert len(q)==24 and {x['lesson'] for x in q}==lessons
            assert {x['type'] for x in q}=={'fill','mc','tf','order'} and all(x['why'] for x in q)
            assert q not in seen;seen.append(q)
            try:audit(q)
            except Exception as err:raise AssertionError(f'cd{cd} de{i}: {err}') from err
            total+=len(q)
    print(f'Math 9–10 PASS: {total} independently solved questions, 12 exams, physical cube-net folding, units, time and rounding.')

if __name__=='__main__':main()
