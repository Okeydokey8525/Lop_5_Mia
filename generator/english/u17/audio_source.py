"""Explicit audio authoring step; ordinary builds use checked-in WAV clips."""
import hashlib
import json
from pathlib import Path
from english.u17.content import build_tests
from english.u17.study import data
from english.recorded import study_texts, quiz_texts

def main():
    texts = study_texts(data())
    for questions in build_tests():
        texts.extend(quiz_texts(questions))
    clips = [dict(text=t, file=hashlib.sha256(t.encode()).hexdigest()[:20] + '.wav') for t in sorted(set(texts))]
    folder = Path(__file__).parent / 'audio'
    folder.mkdir(exist_ok=True)
    manifest = dict(voice='Microsoft Zira Desktop', language='en-US', rate=-1, format='PCM 22050 Hz 16-bit mono', clips=clips)
    (folder / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(f'Unit 17 audio source: {len(clips)} distinct clips')
if __name__ == '__main__':
    main()
