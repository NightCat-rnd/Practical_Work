# Домашнее задание по теме "Генераторные сборки"
# выполнил Андрей Чекунов

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = ( abs(len(x)-len(y)) for x,y, in zip(first,second) if len(x) != len(y) )
second_result = (len(first[x]) == len(second[y]) for x in range(len(first)) for y in range(len(second)) if x==y)
third_result = (len(first[x]) == len(second[x]) for x in range(len(first)))

print(list(first_result))
print(list(second_result))
print(list(third_result))

#Вывод в консоль:
#[1, 2]
#[False, False, True]