"""Original story cards and language practice, printed pages 46-51."""
from english.practice import mc, text as base_text, match, reorder, tf, based, picture as image, field, listen, assemble
CORE = ['ant', 'grasshopper', 'tortoise', 'hare']
MEANINGS = ['con kiến', 'con châu chấu', 'con rùa cạn', 'con thỏ rừng']
CHARACTERS = CORE + ['fox', 'crow']
VERBS = ['cook', 'work', 'run', 'sing']
PAST = ['cooked', 'worked', 'ran', 'sang']
WAYS = ['well', 'hard', 'fast', 'beautifully']
PROFILES = [dict(name=n, pair=pair, character=ch, verb=v, past=p, way=w) for n, pair, ch, v, p, w in [('An', 'the ant and the grasshopper', 'ant', 'work', 'worked', 'hard'), ('Linh', 'the tortoise and the hare', 'hare', 'run', 'ran', 'fast'), ('Minh', 'the fox and the crow', 'crow', 'sing', 'sang', 'beautifully'), ('Hoa', 'Snow White and the seven dwarfs', 'Snow White', 'cook', 'cooked', 'well'), ('Nam', 'the ant and the grasshopper', 'grasshopper', 'sing', 'sang', 'beautifully'), ('Mai', 'the tortoise and the hare', 'tortoise', 'work', 'worked', 'hard')]]

def text(stem, answer, why, lesson=1, alternatives=()):
    accepted = list(alternatives)
    if 'full form' not in stem.lower() and 'rewrite in full' not in stem.lower():
        short = answer.replace('They are', "They're").replace('did not', "didn't")
        if short != answer:
            accepted.append(short)
    return base_text(stem, answer, why, lesson, accepted)

def picture(w, width=320):
    return image('u17', w, MEANINGS[CORE.index(w)], width)

def sentence(p):
    return 'He ' + p['past'] + ' ' + p['way'] + '.' if p['character'] != 'Snow White' else 'She cooked well.'

def character_name(p):
    return p['character'] if p['character'] == 'Snow White' else 'the ' + p['character']

def question(p):
    return 'How did ' + ('she' if p['character'] == 'Snow White' else 'he') + ' ' + p['verb'] + '?'

def card(p):
    return f"Original practice card: Reader: {p['name']} · Main characters: {p['pair']} · Focus character: {p['character']} · Pronoun: {('She' if p['character'] == 'Snow White' else 'He')} · Action: {p['verb']} · Past action: {p['past']} · Manner: {p['way']}. Answer from this card, not from another version of the story."

def passage(p):
    return f"{p['name']} is reading a story. The main characters are {p['pair']}. {p['name']} likes the {p['character']} best.".replace('the Snow White', 'Snow White') + f' The practice card says: {sentence(p)}'

def shown(q, p):
    return based(q, card(p))

def warmup():
    return [mc('Look at the picture. Choose the animal.', CORE, 'ant', 'Kiến có sáu chân và râu.', 1, picture('ant')), text('Complete: Who are the main ___ in the story?', 'characters', 'Main characters.'), match(list(zip(CORE, MEANINGS)), 'Phân biệt bốn con vật.'), shown(mc('Which character does the reader focus on?', CORE, 'hare', 'Focus character.'), PROFILES[1]), reorder('They are the fox and the crow.', 'They are + nhân vật.'), text('Complete: How ___ he work?', 'did', 'How did + nguyên mẫu.', 2), shown(text('Write only the manner word.', 'well', 'Manner trên thẻ.', 2), PROFILES[3]), text('Complete: He ___ fast. Use the past form of run.', 'ran', 'Run → ran.', 2), match([('cook', 'cooked'), ('work', 'worked'), ('sing', 'sang')], 'Động từ hiện tại/quá khứ.', 2), reorder('He worked hard.', 'Worked hard.', 2), shown(text('Write only the focus character.', 'crow', 'Theo thẻ Minh.', 2), PROFILES[2]), shown(tf([('The focus character is ant.', True), ('The manner word is fast.', False)], 'Đọc thẻ An.', 2), PROFILES[0]), text('Complete: How did she ___? Use cook.', 'cook', 'Did + cook, không cooked.', 2), shown(reorder(sentence(PROFILES[3]), 'She cooked well.', 2), PROFILES[3]), shown(text('Write the complete past sentence using the pronoun on the card.', sentence(PROFILES[2]), 'He sang beautifully.', 3), PROFILES[2]), shown(text('Write the complete How did question using the pronoun and action on the card.', question(PROFILES[1]), 'Did + run.', 3), PROFILES[1]), mc('Choose the correct question.', ['How did he sing?', 'How did he sang?', 'How he did sing?', 'How did sang he?'], 'How did he sing?', 'Did + sing.', 3), shown(text('Write the How did question, then the past answer. Use the pronoun on the card.', question(PROFILES[0]) + ' ' + sentence(PROFILES[0]), 'Work trong câu hỏi, worked trong câu kể.', 3), PROFILES[0])]

def vocabulary():
    return [*[mc('Look at the picture. Choose the animal.', CORE, k, 'Tranh: ' + MEANINGS[i], 1, picture(k)) for i, k in enumerate(CORE)], text('Complete: grass___. Write the whole animal word.', 'grasshopper', 'Grasshopper.'), match([('fox', 'con cáo'), ('crow', 'con quạ'), ('fairy tale', 'truyện cổ tích')], 'Từ trong Lesson 1.'), mc('Which word means nhân vật?', ['character', 'weather', 'jumper', 'season'], 'character', 'Character.'), text('Complete: tor___. Write the whole animal word.', 'tortoise', 'Tortoise là rùa cạn.'), match(list(zip(VERBS, PAST)), 'Run → ran, sing → sang.', 2), reorder('He sang beautifully.', 'Sang beautifully.', 2), text('Complete: He worked ___. Use chăm chỉ.', 'hard', 'Worked hard.', 2), text('Complete: She cooked ___. Use giỏi/tốt.', 'well', 'Cooked well.', 2), shown(text('Write only the past action word.', 'ran', 'Theo thẻ.', 2), PROFILES[1]), tf([('Ran is the past form of run.', True), ('Sang is the base form after did.', False)], 'Did + sing; câu kể sang.', 2), shown(text('Write only the manner word.', 'beautifully', 'Đọc đúng Manner.', 3), PROFILES[2]), reorder('Who are the main characters in the story?', 'Hỏi nhân vật.', 3), shown(text('Write a past sentence using the pronoun on the card.', sentence(PROFILES[0]), 'He worked hard.', 3), PROFILES[0]), text('Complete: I am reading a fairy ___.', 'tale', 'Fairy tale.', 3)]

def dialogue():
    return [mc('Choose the question about characters.', ['Who are the main characters in the story?', 'How is the weather?', 'What do you wear?', 'Where is the bag?'], 'Who are the main characters in the story?', 'Who hỏi nhân vật.'), text('Complete: How ___ he run?', 'did', 'Did.', 2), reorder('She cooked well.', 'Cooked well.', 2), shown(text('Write only the two main characters, in card order.', PROFILES[0]['pair'], 'The ant and the grasshopper.'), PROFILES[0]), text('Rewrite in full: They’re the fox and the crow.', 'They are the fox and the crow.', 'They’re = They are.'), text('Complete: He ___ beautifully. Use the past form of sing.', 'sang', 'Sing → sang.', 2), shown(text('Answer with a complete past sentence using the pronoun on the card.', sentence(PROFILES[1]), 'He ran fast.', 2), PROFILES[1]), shown(mc('Which manner word answers the How question?', WAYS, 'well', 'Theo thẻ Hoa.'), PROFILES[3]), reorder('How did he work?', 'Did + work.', 2), text('Rewrite in full: He didn’t run fast.', 'He did not run fast.', 'Did not + run.', 2), text('Complete: How did she ___? Use cook.', 'cook', 'Did + cook.', 2), match([('Who are the main characters?', 'They are the ant and the grasshopper.'), ('How did he run?', 'He ran fast.'), ('Do you like the story?', 'Yes, I do.')], 'Ghép theo chức năng câu hỏi.', 2), shown(text('Write the How did question using the card pronoun.', question(PROFILES[2]), 'How did he sing?', 2), PROFILES[2]), tf([('How did he work is a correct question pattern.', True), ('How did he worked is correct.', False)], 'Did + nguyên mẫu.', 3), shown(text('Write the question then answer, using the pronoun on the card.', question(PROFILES[3]) + ' ' + sentence(PROFILES[3]), 'Cook/cooked.', 3), PROFILES[3]), text('Rewrite in full: They’re the tortoise and the hare.', 'They are the tortoise and the hare.', 'They are.', 3), shown(text('Write the complete past sentence using the pronoun on the card.', sentence(PROFILES[4]), 'Cùng truyện nhưng tập trung nhân vật khác.', 3), PROFILES[4]), mc('Choose the correct sentence.', ['He ran fast.', 'He runned fast.', 'He did ran fast.', 'He running fast.'], 'He ran fast.', 'Run → ran.', 3)]

def reading():
    qs = []
    for p in PROFILES[:4]:
        qs.extend((based(q, passage(p)) for q in [text('Who is reading? Write the name only.', p['name'], 'Tên người đọc.', 3), mc('Which manner word is in the practice sentence?', WAYS, p['way'], 'Đọc practice card says.', 3), text('Write only the focus character.', p['character'], 'Reader likes…best.', 3), tf([(f"The past action is {p['past']}.", True), (f"The manner word is {WAYS[(WAYS.index(p['way']) + 1) % 4]}.", False)], 'Đối chiếu chính đoạn tự soạn.', 3)]))
    qs += [based(text('Both read about the ant and the grasshopper. Who focuses on the grasshopper? Write the name only.', 'Nam', 'Không suy nhân vật yêu thích từ tên truyện.', 3), '\n'.join((card(p) for p in [PROFILES[0], PROFILES[4]]))), based(text('Who reached the finish first? Write the animal only.', 'tortoise', 'Đọc kết thúc đoạn này.', 3), 'In this short original retelling, the hare ran fast but stopped to sleep. The tortoise kept walking and reached the finish first. The tortoise won the race.')]
    return qs

def writing():
    return [text('Complete: He ___ hard. Use work in the past.', 'worked', 'Worked.'), reorder('They are the ant and the grasshopper.', 'They are.'), text('Complete: How did he ___? Use run.', 'run', 'Did + run.'), text('Complete: She ___ well. Use cook in the past.', 'cooked', 'Cooked.', 2), mc('Choose the correct question.', ['How did he sing?', 'How did he sang?', 'How he did sang?', 'How does he sang?'], 'How did he sing?', 'Did + sing.', 2), text('Complete: main charac___. Write the whole plural word.', 'characters', 'Characters.'), match(list(zip(VERBS, PAST)), 'Bốn dạng quá khứ.', 2), reorder('He ran fast.', 'Ran fast.', 2), text('Rewrite in full: He didn’t sing.', 'He did not sing.', 'Did not + sing.', 2), text('Complete: He sang ___. Use hay/đẹp.', 'beautifully', 'Sang beautifully.', 2), shown(reorder(sentence(PROFILES[0]), 'Worked hard.', 2), PROFILES[0]), reorder('How did she cook?', 'Did + cook.', 2), text('Complete: She cooked ___. Use well.', 'well', 'Well.'), text('Rewrite in full: They’re the fox and the crow.', 'They are the fox and the crow.', 'They are.', 2), *[shown(text('Write the How did question, then the past answer using the card pronoun.', question(p) + ' ' + sentence(p), 'Did + nguyên mẫu; câu đáp dùng quá khứ.', 3), p) for p in PROFILES[:4]]]

def listening(index):
    a, b, c = [PROFILES[(index + k) % 6] for k in range(3)]
    return [listen('Listen and choose the character.', 'The focus character is ' + character_name(a) + '.', [field('Character:', a['character'], CHARACTERS + ['Snow White'])]), listen('Listen and choose the manner word.', sentence(b), [field('Manner:', b['way'], WAYS)], 2), listen('Listen and choose the past action.', sentence(a), [field('Past action:', a['past'], PAST)], 2), listen('Listen and choose the focus character.', f"The main characters are {c['pair']}. The focus character is {character_name(c)}.", [field('Focus character:', c['character'], CHARACTERS + ['Snow White'])], 2), listen('Listen. Find both character and manner.', f'The focus character is {character_name(a)}. ' + sentence(a), [field('Character:', a['character'], CHARACTERS + ['Snow White']), field('Manner:', a['way'], WAYS)], 3), listen('Listen. Write only Linh’s character and manner, not An’s.', 'An says: My focus character is the ant. He worked hard. Linh says: My focus character is the hare. He ran fast.', [field('Linh’s character:', 'hare'), field('Linh’s manner:', 'fast')], 3)]

def build_tests():
    import copy
    written = [warmup(), vocabulary(), dialogue(), reading(), writing()]
    mixed = [copy.deepcopy(written[i % 5][i]) for i in range(18)]
    return [assemble(qs, listening(i)) for i, qs in enumerate(written + [mixed])]
