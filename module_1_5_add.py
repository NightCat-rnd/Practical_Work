# Практическое задание по уроку - Неизменяемые и изменяемые объекты. Кортежи
# Выполнил Андрей Чекунов
import sys # для использования getsizeof

immutable_var = (1,2,3,4,5,'dog','cat',5.2,[1,2,3])

# можно кортеж преобразовать в список, и его изменить
# после чего удалить кортеж, а потом преобразовать список в кортеж со старым именем
# таким образом мы получим другой(измененный) кортеж с прежним именем
#
print('кортеж')
print(immutable_var)
sizeof_old_tuple = sys.getsizeof(immutable_var)
temp_list = list(immutable_var)
print('преобразовали в список')
print(type(temp_list))
print(temp_list)
temp_list[0:5] = 10,20,30,40,50
print('изменили список temp_list')
print(temp_list)
print('ID кортежа до удаления')
print(id(immutable_var))
id_old = id(immutable_var)
del immutable_var
immutable_var = tuple(temp_list)
sizeof_new_tuple = sys.getsizeof(immutable_var)
print('удалили кортеж и создали заново из списка')
print('ID нового кортежа с тем же идентификатором и его содержимое')
print(id(immutable_var))
id_new = id(immutable_var)
print(immutable_var)
print('сравниваем ID кортежей, до удаления и вновь созданного')
if id_old == id_new:
    print('ID кортежей идентичны')
else:
    print('ID кортежей НЕ идентичны')
print('выводим размеры старого и нового кортежа ')
print('Old - '+str(sizeof_old_tuple))
print('New - '+str(sizeof_new_tuple))
#  очень интересно работает виртуальная машина Питона, надо разбираться что там внутри происходит :)

# повторяем все то же самое, но вместе с изменением списка, добавляем в него еще элементы
# проверяем, что произойдет если изменим количество элементов в списке и затем преобразуем в кортеж
print('------------------\n\n\n')
print('кортеж')
print(immutable_var)
sizeof_old_tuple = sys.getsizeof(immutable_var)
temp_list = list(immutable_var)
print('преобразовали в список')
print(type(temp_list))
print(temp_list)
temp_list[0:5] = 10,20,30,40,50
print('изменили список temp_list')
print(temp_list)
print('добавили в список элементы')
temp_list.append('New_element')
temp_list.insert(-2,123.456)
print(temp_list)
print('ID кортежа до удаления')
print(id(immutable_var))
id_old = id(immutable_var)
del immutable_var
immutable_var = tuple(temp_list)
sizeof_new_tuple = sys.getsizeof(immutable_var)
print('удалили кортеж и создали заново из списка')
print('ID нового кортежа с тем же идентификатором и его содержимое')
print(id(immutable_var))
id_new = id(immutable_var)
print(immutable_var)
print('сравниваем ID кортежей, до удаления и вновь созданного')
if id_old == id_new:
    print('ID кортежей идентичны')
else:
    print('ID кортежей НЕ идентичны')
print('выводим размеры старого и нового кортежа ')
print('Old - '+str(sizeof_old_tuple))
print('New - '+str(sizeof_new_tuple))
#  очень интересно работает виртуальная машина Питона, надо разбираться что там внутри происходит :)