# 2. Каждое из слов «class», «function», «method» записать в байтовом типе.
# Сделать это необходимо в автоматическом, а не ручном режиме, с помощью добавления литеры b к текстовому значению,
# (т.е. ни в коем случае не используя методы encode, decode или функцию bytes) и определить тип,
# содержимое и длину соответствующих переменных.

word_1 = "class"
word_2 = "function"
word_3 = "method"

for var in [value for key, value in locals().items() if key.startswith('word_')]:
    word_b = eval(f"b'{var}'")
    print(word_b)
    print(type(word_b))
    print(len(word_b))