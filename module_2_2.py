# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
# Выполнил Андрей Чекунов
first, second, third = map(int, input('Введите (через пробел) 3 числа: ').split())
if first == second and second == third :
    print ('Три числа одинаковые')
elif first == second or first == third or second == third :
    print('Два числа одинаковые')
else:
    print('Одинаковых чисел нет')
