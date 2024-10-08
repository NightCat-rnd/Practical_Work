# Домашняя работа по уроку "Дополнительное практическое задание по модулю: "Пространство имён"
# Выполнил Андрей Чекунов
'''
Вам необходимо написать 3 функции:
Функция count_calls подсчитывающая вызовы остальных функций.
Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
строку в нижнем регистре.
Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

Пример выполняемого кода:
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
Вывод на консоль:
(8, 'CAPYBARA', 'capybara')
(10, 'ARMAGEDDON', 'armageddon')
True
False
4
'''
calls = 0                                   # глобальная переменная подсчета вызовов функций

def count_calls():
    global calls
    calls += 1                                # при каждом вызове фенкции переменная увеличивается на 1


def string_info(string_in):
    count_calls()
    len_string = len(string_in)
    string_upp = string_in.upper()
    string_low = string_in.lower()
    tuple_return = (len_string, string_upp, string_low)
    return tuple_return


def is_contains(string_in, list_in):
    count_calls()
    string_lower = string_in.lower()
    new_list_lower = [x.lower() for x in list_in]
    if string_lower not in new_list_lower:
        return False
    else:
        return True


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['Ban','BaNaN','UrBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
