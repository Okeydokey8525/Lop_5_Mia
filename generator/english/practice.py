"""Small shared authoring helpers; answers and feedback use the same lesson facts."""
import base64
import html
from pathlib import Path
from english.u01.content import mc as original_mc, text as original_text, match, reorder, tf, based, TESTS


def mc(stem, options, answer, why, lesson=1, fig=None):
    # Vary answer positions deterministically without separating answer from data.
    shift=sum(map(ord,stem)) % len(options)
    options=options[shift:]+options[:shift]
    return original_mc(stem,options,answer,why,lesson,fig)


def text(stem, answer, why, lesson=1, alternatives=()):
    accepted=list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short=answer
        for full,contracted in [('He is',"He's"),('She is',"She's"),('It is',"It's"),('I am',"I'm"),('What is',"What's"),('do not',"don't"),('I would',"I'd"),('He would',"He'd"),('She would',"She'd")]:
            short=short.replace(full,contracted)
        if short!=answer:accepted.append(short)
    return original_text(stem,answer,why,lesson,accepted)


def picture(unit, name, label, width=320):
    source=Path(__file__).parent/unit/'images'/f'{name}.webp'
    src='data:image/webp;base64,'+base64.b64encode(source.read_bytes()).decode('ascii')
    return f'<div class="fig en-figure"><img src="{src}" alt="{html.escape(label)}" width="768" height="512" style="width:{width}px;max-width:100%;height:auto;display:block;border-radius:12px" decoding="async"></div>'


def field(label, answer, options=None, alternatives=()):
    return dict(label=label,answer=answer,options=options,alternatives=list(alternatives))


def listen(stem, transcript, fields, lesson=1, speech=None):
    return dict(type='listen',lesson=lesson,stem=stem,transcript=transcript,speech=speech or transcript,
                fields=fields,why='Thông tin trong lời nghe: '+'; '.join(f['label']+' '+f['answer'] for f in fields)+'.')


def assemble(written, listening):
    assert len(written)==18 and len(listening)==6
    result=list(written)
    for position,question in zip([0,1,10,13,20,23],listening):result.insert(position,question)
    for i,question in enumerate(result):question['level']='tb' if i<10 else 'kha' if i<18 else 'gioi'
    assert [sum(q['type']=='listen' and q['level']==level for q in result) for level in ['tb','kha','gioi']]==[2,2,2]
    return result
