def make_oneline(string):
    return string.replace('\n ', ' ').replace('\n', ' ').strip()

    # Проверяем наличие слов в списке, если есть - считаем среднюю длинну слова, если нет - возвращаем 0.
    if word_lengths:
        return sum(word_lengths) / len(word_lengths)
    else:
        return 0


def total_characters_and_word_count(txt):
    # Считаем общую длинну символов в тексте
    total_characters = len(txt)
    # Делим текст на слова с помощью пробелов
    words = txt.split()
    # Считаем количество слов в тексте
    word_count = len(words)
    # Возвращаем значения с количеством символов и количеством слов
    return total_characters, word_count

# Придумываем наш текст
DEMO = """
In the quiet town of Willowbrook, nestled amidst rolling hills, life unfolds at a leisurely pace.
The townsfolk know each other by name, and smiles are the currency of the day.
Willowbrook's main street is lined with charming shops, where the fragrant aroma of freshly baked bread mingles with the sound of laughter.
In the park, children's laughter fills the air as they chase butterflies, and elderly couples sit on weathered benches, reminiscing about days gone by.
As the seasons change, the town transforms into a kaleidoscope of colors.
Spring brings cherry blossoms, summer sees vibrant gardens in full bloom, autumn's leaves paint the streets with red and gold, and winter turns Willowbrook into a snow-covered wonderland.
In the heart of town stands a centuries-old oak tree, a symbol of resilience and unity.
It's a gathering spot for festivals and celebrations, and it bears witness to countless love stories.
Each year, the Willowbrook Fair brings the community together in a joyful frenzy of games and delicious treats.
In Willowbrook, time moves slowly, and the beauty of simplicity reigns supreme.
It's a place where people are more than neighbors; they are family.
And in the quiet town of Willowbrook, the world finds a gentle, welcoming embrace.
"""
#DEMO = make_oneline(DEMO)

print(DEMO) # Выводим текст на экран

total_characters, word_count = total_characters_and_word_count(DEMO)
print(f"Number of characters ==> {total_characters} characters") # Выводим общее количество символов из функции total_characters_and_word_count
print(f"Number of words ==> {word_count} words") # Выводим общее количество слов из функции total_characters_and_word_count

def symbols_count(txt):
    """Build mapping counting number of entries of each symbol.

    ...
    """
    syms = set(txt)
    res = dict()
    for sym in sorted(syms):
        res[sym] = txt.count(sym)
    return res
    # or
    # return {sym: txt.count(sym) for sym in sorted(set(txt))}


class Text:
    def __init__(self, obj=''):
        self.str = str(obj)
        self.oneline = make_oneline(self.str)

    def __repr__(self):
        lim = self.oneline[:16]
        ext = '...' if len(self.oneline) > 16 else ''
        return f'{type(self).__name__}({repr(lim)}{ext})'

    def __str__(self):
        return self.str

    def symbols_count(self):
        """... same as above ..."""
        return {sym: self.oneline.count(sym)
                for sym in sorted(set(self.oneline))}


