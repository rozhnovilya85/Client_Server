# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

word_1 = "разработка"
word_2 = "администрирование"
word_3 = "protocol"
word_4 = "standard"
res_b = []
res_str = []
for var in [value for key, value in locals().items() if key.startswith('word_')]:
    var_b = var.encode('utf-8')
    print(type(var_b))
    print(var_b)
    res_b.append(var_b)

for i in res_b:
    var_str = i.decode('utf-8')
    res_str.append(var_str)

print(res_str)
