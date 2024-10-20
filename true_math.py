# Домашняя работа по уроку "Модули и пакеты"
# Выполнил Андрей Чекунов
from math import inf,nan
def divide(first, second):
    if second == 0 and first > 0 :
        return inf      # Положительная бесконечность
    elif second == 0 and first < 0 :
        return -inf     # Отрицательная бесконечность
    elif first == 0 and second == 0:
        return nan      # 0/0 неопределенность согласно https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BD%D0%B0_%D0%BD%D0%BE%D0%BB%D1%8C
    else:
       return first / second


def main():
    result3 = divide(49, 7)
    result4 = divide(15, 0)
    result5 = divide(-45,0)
    result6 = divide(0,0)
    result7 = divide(0,34)
    print(result3)
    print(result4)
    print(result5)
    print(result6)
    print(result7)
if __name__ == '__main__':
    main()