"""Embed checked-in audio for portable HTML; web build extracts the same bytes."""
import base64
import json
from pathlib import Path

HERE=Path(__file__).parent


def markup(unit,texts):
    folder=HERE/unit/'audio'
    manifest=json.loads((folder/'manifest.json').read_text(encoding='utf-8'))
    files={c['text']:c['file'] for c in manifest['clips']}
    clips={}
    for text in sorted(set(texts)):
        if text not in files:raise ValueError(f'Missing recorded text: {text}')
        clips[text]='data:audio/wav;base64,'+base64.b64encode((folder/files[text]).read_bytes()).decode('ascii')
    payload=json.dumps(dict(voice=manifest['voice'],clips=clips),ensure_ascii=False).replace('</',r'<\/')
    return '<script type="application/json" id="mia-audio-data">'+payload+'</script><script>'+(HERE/'recorded.js').read_text(encoding='utf-8')+'</script>'


def study_texts(config):
    texts=['Hello! Let us listen and learn English.']+list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for w in config['words']:texts.extend([w['word'],w['example']])
    for d in config['dialogues']:texts.extend([d['a'],d['a']+' '+d['b']])
    texts.extend(q['speech'] for q in config['exercises'] if q.get('speech'))
    return texts


def quiz_texts(questions):return ['Hello! Let’s listen and learn English.']+[q['speech'] for q in questions if q['type']=='listen']
