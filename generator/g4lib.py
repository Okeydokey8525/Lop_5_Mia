# Thư viện tạo đề Chủ đề 4: đáp án luôn được TÍNH từ số liệu của đề
import json, pathlib
from decimal import Decimal as D, getcontext
getcontext().prec=50
NB=' '
def d(x): return x if isinstance(x,D) else D(str(x))
def n(x):
    """Số -> chuỗi kiểu Việt Nam: dấu phẩy thập phân, cách nhóm nghìn bằng khoảng trắng không ngắt."""
    x=d(x)
    s=format(x.normalize(),'f')
    if '.' in s: i,f=s.split('.')
    else: i,f=s,''
    neg=i.startswith('-'); i=i.lstrip('-')
    i=f"{int(i):,}".replace(',',NB)
    return ('−' if neg else '')+i+(','+f if f else '')
def num(x):
    return float(d(x))
def B(pre,ans,post=None):
    b={'pre':pre,'kind':'num','ans':num(ans)}
    if post: b['post']=post
    return b
def SEL(pre,ans,post):
    return {'pre':pre,'kind':'sel','opts':['>','<','='],'ans':ans,'post':post}
def cmp(a,b):
    a,b=d(a),d(b); return '>' if a>b else '<' if a<b else '='
def mc(lv,ls,stem,opts,ans,why,fig=None):
    assert len(opts)==4 and len(set(opts))==4,(stem,opts)
    q={'level':lv,'lesson':ls,'type':'mc','stem':stem,'opts':opts,'answer':ans,'why':why}
    if fig: q['fig']=fig
    return q
def fill(lv,ls,stem,blanks,why,fig=None):
    q={'level':lv,'lesson':ls,'type':'fill','stem':stem,'blanks':blanks,'why':why}
    if fig: q['fig']=fig
    return q
def tf(lv,ls,stem,items,why):
    return {'level':lv,'lesson':ls,'type':'tf','stem':stem,'items':[{'t':t,'a':a} for t,a in items],'why':why}
def order(lv,ls,stem,items,sep,why):
    return {'level':lv,'lesson':ls,'type':'order','stem':stem,'items':items,'sep':sep,'why':why}
def write(num_,qs,cd=4):
    from collections import Counter
    c=Counter(q['level'] for q in qs)
    assert c['tb']==10 and c['kha']==8 and c['gioi']==6 and len(qs)==24,c
    assert [q['level'] for q in qs]==['tb']*10+['kha']*8+['gioi']*6
    out=pathlib.Path(__file__).parent/'tests'/f'cd{cd}'; out.mkdir(parents=True,exist_ok=True)
    js='window.TEST_FN=function(H){\nreturn MK%d([\n'%cd+',\n'.join(json.dumps(q,ensure_ascii=False) for q in qs)+'\n]);};\n'
    (out/f'de0{num_}.js').write_text(js)
    print('wrote de0%d'%num_,len(js))
