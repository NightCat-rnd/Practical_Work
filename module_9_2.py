# Домашнее задание по теме "Списковые, словарные сборки"
# выполнил Андрей Чекунов
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(x) for x in first_strings if len(x) >= 5]
second_result = [(first_strings[x],second_strings[y]) for x in range(len(first_strings)) \
                  for y in range(len(second_strings)) if len(first_strings[x])==len(second_strings[y])]
third_result = {i:len(i) for i in (first_strings+second_strings) if not len(i)%2}

print(first_result)
print(second_result)
print(third_result)
'''
Вывод на консоль:
[10, 8, 8]
[('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
{'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
'''