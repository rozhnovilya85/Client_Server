# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
# «сокет», «декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того,
# что перед нами файл в неизвестной кодировке.
# Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.

from chardet import detect

word_1 = "сетевое программирование"
word_2 = "сокет"
word_3 = "декоратор"




with open('test.txt', 'w') as f:
    for var in [value for key, value in locals().items() if key.startswith('word_')]:
        f.write(f'{var}\n')
f.close()

with open('test.txt', 'rb') as f:
    content = f.read()
encod = detect(content)['encoding']
print(encod)

with open('test.txt', 'r', encoding=encod) as f:
    content = f.read()
print(content)