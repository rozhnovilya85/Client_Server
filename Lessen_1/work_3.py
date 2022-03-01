# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.

word_1 = "attribute"
word_2 = "класс"
word_3 = "функция"
word_4 = "type"

for var in [value for key, value in locals().items() if key.startswith('word_')]:
    try:
        var_b = bytes(var,'ascii')
        print(var_b)
        print(type(var_b))
    except UnicodeEncodeError:
        print(f'Слово "{var}" невозможно записать в виде байтовой строки')
