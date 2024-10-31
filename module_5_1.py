# Домашняя работа по уроку "Атрибуты и методы объекта"
# Выполнил Андрей Чекунов
'''
Задача "Developer - не только разработчик":
Реализуйте класс House, объекты которого будут создаваться следующим образом:
House('ЖК Эльбрус', 30)
Объект этого класса должен обладать следующими атрибутами:
self.name - имя, self.number_of_floors - кол-во этажей
Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
Пункты задачи:
Создайте класс House.
Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
Создайте объект класса House с произвольным названием и количеством этажей.
Вызовите метод go_to у этого объекта с произвольным числом.

Пример результата выполнения программы:
Исходные данные:
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
Вывод на консоль:
1
2
3
4
5
"Такого этажа не существует"
'''

class House():
    def __init__(self, name, floors):
        self.name = name                    # Название ЖК
        self.number_of_floors = floors      # Количество этажей
        self.current_floor = 0              # указывает на каком этаже находится лифт, по умолчанию на нулевом

    def go_to(self, new_floor):
        # перемещает лифт на этаж new_floor
        if 0 <= new_floor <= self.number_of_floors :
            directions = new_floor - self.current_floor
            while directions != 0:
                if directions > 0:
                    self.current_floor += 1
                    print(f'{self.name} <---> {self.current_floor}')
                    directions -= 1
                else:
                    self.current_floor -= 1
                    print(f'{self.name} <---> {self.current_floor}')
                    directions += 1

        else:
            print(f'{self.name} ---> Такого этажа не существует')

    def where_is_elevator(self):
        # выводит на каком этаже находится лифт
        print(f'{self.name} - лифт на этаже {self.current_floor}')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.where_is_elevator()
h2.where_is_elevator()
h1.go_to(5)
h2.go_to(10)

h1.where_is_elevator()
h1.go_to(17)
h2.go_to(1)

h1.go_to(9)
h2.go_to(0)

h1.go_to(0)
h2.go_to(2)

h1.where_is_elevator()
h2.where_is_elevator()