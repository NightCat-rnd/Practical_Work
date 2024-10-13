# Самостоятельная работа по уроку "Рекурсия"
# Выполнил Андрей Чекунов
'''
1)перевод числа в строку
2)сохранить в переменную первую цифру.
3)при условии что длинна числа больше 1 умножаем первое на рекурсию.
4) при условии что первое число неравно 0 возвращаем первое число.
5) воыращаем единицу
'''

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif first:
        return first
    else:
        return 1


result = get_multiplied_digits(40203)
print(result)
