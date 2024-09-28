# Домашняя работа по уроку "Стиль кода часть II. Цикл While."
# Выполнил Андрей Чекунов

my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_my_list = len(my_list)  # длина списка
i = 0 # index для перемещения по списку
while i < len_my_list :
    if my_list[i] == 0 :
        i +=1
        continue
    elif my_list[i] < 0 :
        print('Окончание перебора списка, встретился элемент меньше нуля')
        break
    else:
        print(my_list[i])
        i += 1
if i == len_my_list :
    print('Список перебран')

