# Домашняя работа по уроку "Атрибуты и методы объекта"
# Выполнил Андрей Чекунов
'''
Задача "Магические здания":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".

Необходимо дополнить класс House следующими специальными методами:
__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

Пример результата выполнения программы:
Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
10
20
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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
