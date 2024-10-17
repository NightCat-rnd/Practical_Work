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
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    ret = 0
    for arg in args:
        if isinstance(arg, list):
            for item in arg:
                ret += calculate_structure_sum(item)
        elif isinstance(arg, tuple):
            for item in arg:
                ret += calculate_structure_sum(item)
        elif isinstance(arg, set):
            for item in arg:
                ret += calculate_structure_sum(item)
        elif isinstance(arg,dict):
            for k,v in arg.items():
                ret += calculate_structure_sum(k)
                ret += calculate_structure_sum(v)
        elif isinstance(arg, int):
            ret += arg
        elif isinstance(arg, str):
            ret += len(arg)
    return ret

result = calculate_structure_sum(data_structure)
print(result)
result = calculate_structure_sum(data_structure,data_structure1,data_structure,data_structure,data_structure1)
print(result)

