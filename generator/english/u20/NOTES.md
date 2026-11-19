# Unit 20 — Our summer holidays

## Verified source

Read all six pages of the local Global Success 5 student book, volume two: printed **64–69**, PDF **66–71** (79-page PDF). Source remains outside the public repository at `../tai_lieu/sach/05-sgk-tieng-anh-5-global-success-tap-hai_268202616.pdf`; SHA-256 `65e57b1193689e5a66f0ad9ce754388c6332d772c7d892c8f7b40660072713f9`. Page renders remain outside the repo under `../luu_tru/english-volume2-planning/unit20-66.png` through `unit20-71.png`.

- Lesson 1, 64–65: **Where are you going to visit this summer? / I’m going to visit…** Huong River, Phong Nha Cave, Phu Quoc Island, Dam Sen Aquarium. Generic place words support remembering names; pictures never require guessing a named landmark.
- Lesson 2, 66–67: **What are you going to do this summer? / I’m going to…** Join a music club, go camping, visit an eco-farm, practise swimming. The page also introduces learning to play an instrument and growing vegetables.
- Lesson 3, 68–69: falling intonation for Wh questions, reading that contrasts last summer with plans this summer, writing about summer in about 40 words, and a summer-holiday poster project. Language learning is present in the reading. Readings, dialogues and listening tracks here are independently authored; no book scans, song/chant lyrics, reading passages or publisher audio are copied.

## Authoring decisions

Six exams × 24 questions: 10/8/6 questions by level, 100 points. Each includes two listening questions per level. Beginner listening identifies short place/activity phrases; intermediate listening answers a full question; advanced listening extracts two details or distinguishes past actions from future plans.

Keep **I am / he, she is / you, we, they are going to + base verb**, visit + place (no visit to), join a music club, an eco-farm, practise swimming. Full-form tasks require expanded forms; ordinary tasks accept relevant contractions. British `practise` follows the book; text responses also accept American `practice` where appropriate. Past actions are only a contrast scaffold, not a replacement for the Unit’s future-plan focus.

Profiles are original fictional plans. Repeated destinations with different people/activities prevent matching by place alone. Reading questions distinguish the main activity, extra language-learning plan, transport, and last-summer action. Autograded writing specifies the speaker, sentence order and opening; free writing and the poster project remain guided activities for adult feedback. The site does not record or grade speaking or open essays.

Content review caught lowercasing the initial `I` when joining a generated sentence after `This summer,`. Keep the English pronoun `I` capitalized even inside a sentence. Do not apply generic initial-letter lowercasing to complete English phrases; successful scoring QA alone does not catch this language error.

## Study, artwork and audio

`study.py`: 20 words/phrases, three groups (activities/places/plans), six dialogues, 12 practice tasks with separate saved progress. Stable new keys: `en-u20-deN-v1`, `mia5:learn:en-u20-v1`. Existing units’ keys remain unchanged.

Four original activity illustrations: `join-a-music-club`, `go-camping`, `visit-an-eco-farm`, `practise-swimming`. Built-in ImageGen; full prompts and retained-original paths in `images/PROMPTS.md`. The images show observable activities, not a person’s future intention. Check source artwork plus actual quiz, reader, poster and study renderings before acceptance.

95 checked-in WAV clips: words, examples, dialogues, A–Z letter names and quiz listening. Authoring uses Microsoft Zira Desktop/en-US, rate -1, PCM 22050 Hz/16-bit/mono; normal builds use those files without installing voices. To recreate intentionally: run `python -m english.u20.audio_source` from `generator/`, then `powershell -NoProfile -File tools/generate_english_audio.ps1 -Unit u20` from the root. ABC is letter-name spelling, not phonics. Browser playback does not establish human pronunciation quality or actual iPad acceptance.

## Verification

Run the full build/audit/link/browser/responsive suite plus Unit 20 exam, persistence, study and real-audio gates. Specific assertions cover full forms, am/is/are, base verbs after going to and last/this summer separation. See `docs/breakdowns/2026-11-19_UNIT20.md` for local/CI/live evidence and remaining limitations.
