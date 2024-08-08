import re

CYRILLIC_TO_LATIN = {
    'а': 'a', 'А': 'A',
    'б': 'b', 'Б': 'B',
    'в': 'v', 'В': 'V',
    'г': 'g', 'Г': 'G',
    'д': 'd', 'Д': 'D',
    'е': 'e', 'Е': 'E',
    'ё': 'yo', 'Ё': 'Yo',
    'ж': 'j', 'Ж': 'J',
    'з': 'z', 'З': 'Z',
    'и': 'i', 'И': 'I',
    'й': 'y', 'Й': 'Y',
    'к': 'k', 'К': 'K',
    'л': 'l', 'Л': 'L',
    'м': 'm', 'М': 'M',
    'н': 'n', 'Н': 'N',
    'о': 'o', 'О': 'O',
    'п': 'p', 'П': 'P',
    'р': 'r', 'Р': 'R',
    'с': 's', 'С': 'S',
    'т': 't', 'Т': 'T',
    'у': 'u', 'У': 'U',
    'ф': 'f', 'Ф': 'F',
    'х': 'x', 'Х': 'X',
    'ц': 's', 'Ц': 'S',
    'ч': 'ch', 'Ч': 'Ch',
    'ш': 'sh', 'Ш': 'Sh',
    'ъ': 'ʼ', 'Ъ': 'ʼ',
    'ь': '', 'Ь': '',
    'э': 'e', 'Э': 'E',
    'ю': 'yu', 'Ю': 'Yu',
    'я': 'ya', 'Я': 'Ya',
    'ў': 'oʻ', 'Ў': 'Oʻ',
    'қ': 'q', 'Қ': 'Q',
    'ғ': 'gʻ', 'Ғ': 'Gʻ',
    'ҳ': 'h', 'Ҳ': 'H',
}
CYRILLIC_VOWELS = (
    'а', 'А', 'е', 'Е', 'ё', 'Ё', 'и', 'И', 'о', 'О', 'у', 'У', 'э', 'Э',
    'ю', 'Ю', 'я', 'Я', 'ў', 'Ў'
)


def to_latin(text):
    beginning_rules = {
        'ц': 's', 'Ц': 'S',
        'е': 'ye', 'Е': 'Ye'
    }
    after_vowel_rules = {
        'ц': 'ts', 'Ц': 'Ts',
        'е': 'ye', 'Е': 'Ye'
    }

    text = re.sub(
        r'(сент|окт)([яЯ])(бр)',
        lambda x: '%s%s%s' % (x.group(1),
                              'a' if x.group(2) == 'я' else 'A', x.group(3)),
        text,
        flags=re.IGNORECASE | re.U
    )

    text = re.sub(
        r'\b(%s)' % '|'.join(beginning_rules.keys()),
        lambda x: beginning_rules[x.group(1)],
        text,
        flags=re.U
    )

    text = re.sub(
        r'(%s)(%s)' % ('|'.join(CYRILLIC_VOWELS),
                       '|'.join(after_vowel_rules.keys())),
        lambda x: '%s%s' % (x.group(1), after_vowel_rules[x.group(2)]),
        text,
        flags=re.U
    )

    text = re.sub(
        r'(%s)' % '|'.join(CYRILLIC_TO_LATIN.keys()),
        lambda x: CYRILLIC_TO_LATIN[x.group(1)],
        text,
        flags=re.U
    )

    return text
