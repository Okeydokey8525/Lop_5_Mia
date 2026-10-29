import pathlib, json, sys
sys.path.insert(0,'.')
from cfg import *
W=pathlib.Path(__file__).parent
OUT=W/'out'/ROOT
css=(W/'engine.css').read_text(encoding='utf-8'); eng=(W/'engine.js').read_text(encoding='utf-8'); fonts=(W/'fonts.css').read_text(encoding='utf-8')
def page(title, data_js, extra, mk_js):
    return f'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<style>{fonts}</style>
<style>
{css}
</style></head><body>
<div class="page"><div id="app"></div></div>
<div class="bar" id="bar" data-mode="run"><div class="bar-in"></div></div>
<script>
{mk_js}
{data_js}
window.TEST_EXTRA={json.dumps(extra,ensure_ascii=False)};
{eng}
</script></body></html>'''
count=0
for cd in CDS:
    d=OUT/cd['dir']; d.mkdir(parents=True,exist_ok=True)
    mk=(W/'common'/f"{cd['mk']}.js").read_text(encoding='utf-8')
    for i,(slug,name,theme) in enumerate(cd['tests'],1):
        src=W/'tests'/f"cd{cd['n']}"/f"de{i:02d}.js"
        if not src.exists(): continue
        fn=f"De{i}_{slug}.html"
        nxt=f"De{i+1}_{cd['tests'][i][0]}.html" if i<len(cd['tests']) else None
        prv=f"De{i-1}_{cd['tests'][i-2][0]}.html" if i>1 else None
        extra={'id':f"cd{cd['n']}-de{i}",'title':f"Đề {i} · {name}",'theme':theme,'home':'../index.html','next':nxt,'prev':prv}
        extra={k:v for k,v in extra.items() if v}
        html=page(f"Toán 5 · Chủ đề {cd['n']} · Đề {i} · {name}", src.read_text(encoding='utf-8'), extra, mk)
        (d/fn).write_text(html,encoding='utf-8',newline='\n'); count+=1
print('built',count)
