# Домашнее задание по теме "Декораторы"
# выполнил Андрей Чекунов

def is_prime(func):
    def wrapper(a,b,c):
        result = func(a,b,c)
        k = 0
        for i in range(2, result//2+1):
            if result % i == 0:
                k += 1
        if k == 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(a:int, b:int, c:int)->int:
    return a+b+c

result = sum_three(2, 3, 6)
print(result)