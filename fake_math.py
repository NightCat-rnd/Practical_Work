# Домашняя работа по уроку "Модули и пакеты"
# Выполнил Андрей Чекунов

def divide(first, second):
    if second != 0 :
        return first / second
    else:
        return 'Error: division by zero'

def main():
    result1 = divide(69, 3)
    result2 = divide(3, 0)
    print(result1)
    print(result2)

if __name__ == '__main__':
    main()