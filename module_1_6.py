# Практическое задание по уроку - Словари и множества
# Выполнил Андрей Чекунов

my_dict = {'Nata':1996, 'Alex':1998, 'Den':2000, 'Lera':2001}   # создаем словарь
print('Мой словарь:',my_dict)  # выводим словарь
mess='Такой ключ отсутствует'    # сообщение при отсутвующем ключе для метода get()
print('Значение ключа "Lera"',my_dict.get('Lera',mess))  # выводим значение ключа 'Lera'
print('Значение ключа "Sasha"',my_dict.get('Sasha',mess))  # выводим значение ключа 'Sasha', или сообщение об отсутствии такого ключа
# print(my_dict('Sasha')) # если написать так, то при отсутствующем ключе будет сообщение об ошибке
print("Добавим ключи - Ruslan, Olga, Oleg")
my_dict['Ruslan']=1999   # добавляем ключ и значение, при обращении к несуществующему ключу он добавляется
my_dict.update({'Olga':1998, 'Oleg':1999}) # добавляем ключи через .update (или изменяем существующие)
print('Мой словарь:',my_dict)  # выводим словарь
deleted_ = my_dict.popitem()  # удалим последнюю пару с возвратом удаленной пары и выведем ее
print('Удаленая пара:',deleted_)
print('Мой словарь:',my_dict)  # выводим словарь
print('Удалим Nata методом del')
del my_dict['Nata']
print('Мой словарь:',my_dict)  # выводим словарь
print('Удалим Den методом pop()')
deleted_ = my_dict.pop('Den')   # метод возвращает удаляемое значение
print('Удаленное значение',deleted_)
print('Мой словарь:',my_dict)  # выводим словарь
print('------------------------\n\n')

my_set = set({1, 100, 333, 'Nata', 'Alisa', 1999, 5, 1,333, 4.5, (0,1,2,3), (0,1,2,3), (0,1,2)})
print("Создаем множество из {1, 100, 333, 'Nata', 'Alisa', 1999, 5, 1,333, 4.5, (0,1,2,3), (0,1,2,3), (0,1,2)}")
print('Множество:',my_set)
print("Добавим в множество элементы - 9.9, 'Cat', 999")
my_set.add(9.9) # добавление одного элемента
my_set.update({'Cat',999}) # добавление нескольких элементов
print('Множество:',my_set)
print('Удалим 999')
my_set.discard(999)
#my_set.remove(999) # при отстутствующем элементе создает ошибку
print('Множество:',my_set)

print('-----------------\n')
print('Создадим frozenset')
my_fset = frozenset({1, 100, 333, 'Nata', 'Alisa', 1999, 5, 1,333, 4.5, (0,1,2,3), (0,1,2,3), (0,1,2)})
print(my_fset)
#my_fset.add(200)
#print(my_fset)
#my_fset.remove(1)
#print(my_fset)
print('Это неизменяемое множество')

