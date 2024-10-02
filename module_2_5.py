# Домашняя работа по уроку "Функции в Python.Функция с параметром"
# Выполнил Андрей Чекунов

def get_matrix(n, m, value):
    matrix = [0]*n            # делаем список из n элементов заполненных 0
    for i in range(n):           # каждый эл-т списка заменяем ссылкой на одномерный список из m элементов с value
        matrix[i] = [value]*m
    return matrix

def get_matrix1(n,m,value):
    matrix = []     # делаем пустой список
    for i in range(n):  # n раз добавляем список из m значений value
        matrix.append([value]*m)
    return matrix

result1 = get_matrix(2,2,10)
result2 = get_matrix(3,5,42)
result3 = get_matrix(4,2,13)
print(result1)
print(result2)
print(result3)

print('--------------')
result1 = get_matrix1(2,2,10)
result2 = get_matrix1(3,5,42)
result3 = get_matrix1(4,2,13)
print(result1)
print(result2)
print(result3)