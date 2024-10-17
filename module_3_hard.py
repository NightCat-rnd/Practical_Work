# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Выполнил Андрей Чекунов
'''
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

вопрос:"А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"

Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

'''

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

data_structure1 = [
  [1, 2, 3],
#  {'a': 4, 'b': 5},
#  (6, {'cube': 7, 'drum': 8}),
  "Hello",
#  ((), [{(2, 'Urban', ('Urban2', 35))}]),
    34
]
num = 0
sum = 0
def calculate_structure_sum(*args):
    global num
    global sum
    print('Entry',num)
    num += 1
#    sum = 0
    for arg in args:
        print(type(arg))
        if isinstance(arg, list):
            print('List',arg)
            for item in arg:
                calculate_structure_sum(item)
        elif isinstance(arg, tuple):
            for item in arg:
                calculate_structure_sum(item)
            print('Tuple',arg)
        elif isinstance(arg, set):
            for item in arg:
                calculate_structure_sum(item)
            print('Set',arg)
        elif isinstance(arg,dict):
            for k,v in arg.items():
                calculate_structure_sum(k)
                calculate_structure_sum(v)
                print(f'key={k}, value={v}')

        elif isinstance(arg, int):
           print('Int',arg)
           sum += arg
        elif isinstance(arg, str):
            print('String',arg)
            sum += len(arg)
    print('Sum = ',sum)


calculate_structure_sum(data_structure)
#calculate_structure_sum(data_structure1)
