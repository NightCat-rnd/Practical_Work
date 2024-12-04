# Домашнее задание по теме "Введение в функциональное программирование"
# выполнил Андрей Чекунов

def apply_all_func(int_list:list, *functions)->dict:
    result = {}
    for item in functions:
        result[item.__name__] = item(int_list)
    return result
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))