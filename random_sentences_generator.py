import random

def get_random_word(words: list) -> str:
    return random.choice(words)

def get_color() -> str:
    global color_calls
    color_calls += 1
    if color_calls == 1:
        return '[91m'
    elif color_calls == 2:
        return '[92m'
    else: #elif color_calls == 3:
        color_calls = 0
        return '[96m'

def get_random_sentence(color_: str, current_count = 1, total_count = 1) -> str:
    global current_names
    global current_places
    global current_verbs
    global current_nouns
    global current_adverbs
    global current_details
    name = get_random_word(current_names)
    current_names.remove(name)
    place = get_random_word(current_places)
    current_places.remove(place)
    verb = get_random_word(current_verbs)
    current_verbs.remove(verb)
    noun = get_random_word(current_nouns)
    current_nouns.remove(noun)
    adverb = get_random_word(current_adverbs)
    current_adverbs.remove(adverb)
    detail = get_random_word(current_details)
    current_details.remove(detail)
    if current_count == total_count:
        current_names = names.copy()
        current_places = places.copy()
        current_verbs = verbs.copy()
        current_nouns = nouns.copy()
        current_adverbs = adverbs.copy()
        current_details = details.copy()
    return f'\033{color_}{name} from {place} {verb} {noun} {adverb} {detail}\033[00m'

def get_count_suffix(count_: int) -> str:
    count_as_string_ = str(count_)
    if count_as_string_.endswith('1') and not count_as_string_.endswith('11'):
        return 'st'
    elif count_as_string_.endswith('2') and not count_as_string_.endswith('12'):
        return 'nd'
    elif count_as_string_.endswith('3') and not count_as_string_.endswith('13'):
        return 'rd'
    else:
        return 'th'

names = ['Simon', 'Joanne', 'George', 'Ann', 'Michael', 'Nicole']
places = ['Boston', 'New Castle', 'Marseille', 'Naples', 'San Diego', 'Osaka']
verbs = ['represents', 'duplicates', 'avoids', 'discovers', 'hides', 'excavates']
nouns = ['the bag', 'the treasure', 'the traffic jam', 'the sandwich', 'the spaceship', 'the sun']
adverbs = ['quickly', 'suddenly', 'masterfully', 'courageously', 'secretly', 'blissfully']
details = ['at school.', 'at sunrise.', 'at noon.', 'at work.', 'in the mountain.', 'in the park.']

current_names = names.copy()
current_places = places.copy()
current_verbs = verbs.copy()
current_nouns = nouns.copy()
current_adverbs = adverbs.copy()
current_details = details.copy()

game_start = True
expected_count = 1
color_calls = 0

while True:
    if expected_count == 0:
        print('Thanks for playing!')
        break
    if game_start:
        print(f'Hello, this is your 1st random sentence:')
        game_start = False
        color = get_color()
        print(get_random_sentence(color))
        expected_count = input(f'\nType a number: 0, 1, 2 or 3 to generate next that number of fully unique random sentences: ')
        while not (expected_count.isdigit() and int(expected_count) in [0, 1, 2, 3]):
            expected_count = input(f'Type a number: 0, 1, 2 or 3 to generate next that number of fully unique random sentences: ')
        expected_count = int(expected_count)
    else:
        if expected_count == 1:
            print(f'1st of {expected_count}:')
            color = get_color()
            print(get_random_sentence(color))
            expected_count = input(f'\nType a number: 0, 1, 2 or 3 to generate next that number of fully unique random sentences: ')
            while not (expected_count.isdigit() and int(expected_count) in [0, 1, 2, 3]):
                expected_count = input(f'Type a number: 0, 1, 2 or 3 to generate next that number of fully unique random sentences: ')
            expected_count = int(expected_count)
        elif expected_count > 1:
            color = get_color()
            for i in range(1, expected_count + 1):
                print(f'{i}{get_count_suffix(i)} of {expected_count}:')
                print(get_random_sentence(color, i, expected_count))
            expected_count = input(f'\nType a number: 0, 1, 2 or 3 to generate next that number of fully unique random sentences: ')
            while not (expected_count.isdigit() and int(expected_count) in [0, 1, 2, 3]):
                expected_count = input(f'Type a number: 0, 1, 2 or 3 to generate next that number of fully unique random sentences: ')
            expected_count = int(expected_count)