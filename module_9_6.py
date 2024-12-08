# Домашнее задание по теме "Генераторы"
# выполнил Андрей Чекунов

def all_variants(text:str):
    n = 1
    while n <= len(text):
        for i in range(len(text)):
            stop = i + n
            if stop > len(text):
                continue
            #res = text[i:stop:]
            yield text[i:stop:]
        n += 1

a = all_variants("abcdef")
for i in a:
    print(i)