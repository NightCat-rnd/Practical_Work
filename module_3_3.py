# Домашняя работа по уроку "Дополнительное практическое задание по модулю: "Распаковка позиционных параметров"
# Выполнил Андрей Чекунов
def print_params(a = 1, b = 'строка', c = True):
    print(f'a = {a}, b = {b}, c = {c}')
    print(f'Type(a) = {type(a)}, Type(b) = {type(b)}, Type(c) = {type(c)}')
    print()

print_params()
print_params(a=99)
print_params(c = [1,2,3,4,5,6,7,8,9,0], b='Hello', a='Привет')

values_list = [23, 'Hello World!', False]
print_params(values_list)
print_params(*values_list)
values_list1 = ['4', 54, 'end']
print_params(*values_list1)

values_dict = {'a':1, 'b':2, 'c':3}
print_params(values_dict)
print_params(*values_dict)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
print_params(45, *values_list_2)
print_params(*values_list_2, values_list[1])

