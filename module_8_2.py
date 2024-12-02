# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"
# выполнил Андрей Чекунов

def personal_sum(numbers)->tuple:
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
    return result, incorrect_data
def calculate_average(numbers):
    try:
        summ, incorrect_data = personal_sum(numbers)
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None
    correct_data = len(numbers) - incorrect_data
    try:
        average = summ / correct_data
    except ZeroDivisionError:
        #print('Количество данных равно 0')
        return 0
    return average


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать