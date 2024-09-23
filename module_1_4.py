# Практическое задание по уроку - Организация программ и методы строк.
# Выполнил Андрей Чекунов

my_string = input('Введите строку: ')
print(f'Вы ввели {len(my_string)} символов.')
print(f'Строка в верхнем регистре: {str.upper(my_string)}')
print(f'Строка в нижнем регистре: {str.lower(my_string)}')
print(f'Строка без пробелов: {str.replace(my_string,' ', '')}')
print(f'Первый элемент строки: {my_string[0]}')
print(f'Последний элемент строки: {my_string[-1]}')
