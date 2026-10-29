from g4lib import *
import g4lib
from fractions import Fraction
PI=D('3.14')
def tri(a,h): return d(a)*d(h)/2
def trap(a,b,h): return (d(a)+d(b))*d(h)/2
def circ_d(dd): return PI*d(dd)
def circ_r(r): return PI*d(r)*2
def disc(r): return PI*d(r)*d(r)
def write5(num_,qs): g4lib.write(num_,qs,cd=5)
def write6(num_,qs): g4lib.write(num_,qs,cd=6)
def FR(pre,fr,post=None,reduced=True):
    fr=Fraction(fr); b={'pre':pre,'kind':'frac','ans':[fr.numerator,fr.denominator]}
    if reduced: b['reduced']=True
    if post: b['post']=post
    return b
def MX(pre,fr,post=None):
    fr=Fraction(fr); w=fr.numerator//fr.denominator; r=fr-w
    b={'pre':pre,'kind':'mixed','ans':[w,r.numerator,r.denominator]}
    if post: b['post']=post
    return b
def fs(fr):
    fr=Fraction(fr); return '{%d/%d}'%(fr.numerator,fr.denominator)
def ms(fr):
    fr=Fraction(fr); w=fr.numerator//fr.denominator; r=fr-w
    return '{%d %d/%d}'%(w,r.numerator,r.denominator) if r else str(w)
T='font-size="12" font-weight="700" fill="currentColor" font-family="inherit"'
def _w(svg,cap,w=240):
    return '<div class="fig"><figure>'+svg.replace('<svg ','<svg style="width:%dpx" '%w,1)+('<figcaption>%s</figcaption>'%cap if cap else '')+'</figure></div>'
def ra(x,y,dx=1,dy=-1,s=9):
    # dấu góc vuông tại (x,y), mở về hướng (dx,dy)
    return '<path d="M%d %d l%d %d l%d %d" fill="none" stroke="#e8741a" stroke-width="1.8"/>'%(x+dx*s,y,0,dy*s,-dx*s,0)
def fig_tri(kind,base,hh,cap=None,name='tam giác'):
    S='fill="var(--soft)" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"'
    D_='stroke="#e8741a" stroke-width="2" stroke-dasharray="5 4" fill="none"'
    if kind=='acute':
        shape=f'<polygon points="100,16 30,100 190,100" {S}/><line x1="100" y1="16" x2="100" y2="100" {D_}/>'+ra(100,100,1,-1)+ra(100,100,-1,-1)[:0]
        base_x=110; hx,hy,anc=106,62,'start'
    elif kind=='right':
        shape=f'<polygon points="30,16 30,100 190,100" {S}/>'+ra(30,100,1,-1)
        base_x=110; hx,hy,anc=24,62,'end'
        D_=''
    else:
        shape=f'<polygon points="40,16 90,100 190,100" {S}/><line x1="40" y1="16" x2="40" y2="100" {D_}/><line x1="40" y1="100" x2="90" y2="100" stroke="#e8741a" stroke-width="2" stroke-dasharray="5 4"/>'+ra(40,100,1,-1)
        base_x=140; hx,hy,anc=46,62,'start'
    svg=(f'<svg viewBox="0 0 230 124" role="img" aria-label="Hình {name}, đáy {base}, chiều cao {hh}">{shape}'
     f'<text x="{base_x}" y="118" text-anchor="middle" {T}>{base}</text><text x="{hx}" y="{hy}" text-anchor="{anc}" {T}>{hh}</text></svg>')
    return _w(svg,cap)
def fig_trap(a,b,hh,cap=None):
    S='fill="var(--soft)" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"'
    svg=(f'<svg viewBox="0 0 230 124" role="img" aria-label="Hình thang, đáy lớn {a}, đáy bé {b}, chiều cao {hh}">'
     f'<polygon points="70,22 150,22 200,100 20,100" {S}/><line x1="70" y1="22" x2="70" y2="100" stroke="#e8741a" stroke-width="2" stroke-dasharray="5 4"/>'+ra(70,100,1,-1)+
     f'<text x="110" y="14" text-anchor="middle" {T}>{b}</text><text x="110" y="118" text-anchor="middle" {T}>{a}</text><text x="76" y="64" text-anchor="start" {T}>{hh}</text></svg>')
    return _w(svg,cap)
def fig_circ(kind,label,cap=None):
    if kind=='r':
        line='<line x1="90" y1="62" x2="138" y2="62" stroke="#e8741a" stroke-width="2.4"/>'; lx=114
    else:
        line='<line x1="42" y1="62" x2="138" y2="62" stroke="#e8741a" stroke-width="2.4"/>'; lx=90
    svg=(f'<svg viewBox="0 0 180 124" role="img" aria-label="Hình tròn tâm O, {label}"><circle cx="90" cy="62" r="48" fill="var(--soft)" stroke="currentColor" stroke-width="2.4"/>{line}'
     f'<circle cx="90" cy="62" r="3" fill="currentColor"/><text x="86" y="80" text-anchor="end" {T}>O</text><text x="{lx}" y="55" text-anchor="middle" {T}>{label}</text></svg>')
    return _w(svg,cap,200)
def fig_house(w,hw,hr,cap=None):
    S='fill="var(--soft)" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"'
    svg=(f'<svg viewBox="0 0 250 150" role="img" aria-label="Hình ngôi nhà: tam giác ở trên, chữ nhật ở dưới. Đáy {w}, chiều cao tam giác {hr}, chiều cao hình chữ nhật {hw}">'
     f'<polygon points="125,10 40,60 210,60" {S}/><rect x="40" y="60" width="170" height="64" {S}/><line x1="125" y1="10" x2="125" y2="60" stroke="#e8741a" stroke-width="2" stroke-dasharray="5 4"/>'
     f'<text x="131" y="38" text-anchor="start" {T}>{hr}</text><text x="125" y="142" text-anchor="middle" {T}>{w}</text><text x="34" y="96" text-anchor="end" {T}>{hw}</text></svg>')
    return _w(svg,cap,250)
def fig_pond(L,Wd,r,cap=None):
    S='fill="var(--soft)" stroke="currentColor" stroke-width="2.4"'
    svg=(f'<svg viewBox="0 0 250 150" role="img" aria-label="Khu đất hình chữ nhật dài {L}, rộng {Wd}, có một ao tròn bán kính {r}">'
     f'<rect x="30" y="14" width="190" height="106" {S}/><circle cx="125" cy="67" r="34" fill="#b7dcf2" stroke="currentColor" stroke-width="2.4"/><line x1="125" y1="67" x2="159" y2="67" stroke="#e8741a" stroke-width="2.4"/>'
     f'<circle cx="125" cy="67" r="2.6" fill="currentColor"/><text x="143" y="61" text-anchor="middle" {T}>{r}</text><text x="125" y="140" text-anchor="middle" {T}>{L}</text><text x="24" y="70" text-anchor="end" {T}>{Wd}</text></svg>')
    return _w(svg,cap,250)
from decimal import ROUND_HALF_UP
def rnd(x,places=0):
    return d(x).quantize(D(1).scaleb(-places),rounding=ROUND_HALF_UP)
