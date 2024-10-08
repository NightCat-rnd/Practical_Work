# Практическое задание по уроку - Неизменяемые и изменяемые объекты. Кортежи
# Выполнил Андрей Чекунов
import sys # для использования getsizeof

immutable_var = (1,2,3,4,5,'dog','cat',5.2,[1,2,3])
#print(type(immutable_var))
print(immutable_var)
# immutable_var[2] = 33 такая конструкция не работает, т.к. данные в кортеже неизменяемые
immutable_var[8][1] = 33 # это работает, т.к. мы меняем данные в списке, который находится в кортеже, т.е. формально кортеж остается неизменным
print(immutable_var)

mutable_list = [1,2,3,4,5,'dog','chery']
print(mutable_list)
mutable_list[1:3] = 20,30
print(mutable_list)


# ------формально выполнение задания здесь завершено--------------------------

# нельзя изменить содержимое кортежа поэлементно,
# но можно тупо переназначить кортеж!!!
# но, судя по ID это будут разные объекты
print('\n')
new_tuple = (1,2,3,4,5,6,7,8,9,0)
print('кортеж',new_tuple)
print('ID = ',id(new_tuple))
new_tuple = (10,20,30,40,50,60,70,80,90,00,'переназначение кортежа')
print('Переназначанный кортеж',new_tuple)
print('ID = ',id(new_tuple))
# т.е. это разные объекты

print('------------------\n')
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
