# Домашняя работа по уроку "Модули и пакеты"
# Выполнил Андрей Чекунов
from math import inf
def divide(first, second):
    if second != 0:
        return first/second
    elif first > 0 :
        return inf      # Положительная бесконечность
    else:
        return -inf     # Отрицательная бесконечность

def main():
    result3 = divide(49, 7)
    result4 = divide(15, 0)
    result5 = divide(-45,0)
    print(result3)
    print(result4)
    print(result5)

if __name__ == '__main__':
    main()