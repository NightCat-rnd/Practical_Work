# Домашняя работа по уроку "Различие атрибутов класса и экземпляра"
# Выполнил Андрей Чекунов
'''
Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам
класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.

Пример результата выполнения программы:
Пример выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

Вывод на консоль:
['ЖК Эльбрус']
['ЖК Эльбрус', 'ЖК Акация']
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Акация снесён, но он останется в истории
ЖК Матрёшки снесён, но он останется в истории
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Эльбрус снесён, но он останется в истории
'''

class House():
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name                    # Название ЖК
        self.number_of_floors = floors      # Количество этажей
        self.current_floor = 0              # указывает на каком этаже находится лифт, по умолчанию на нулевом

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


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

    # __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=)
    def __lt__(self, other):        # (<)
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print('Операция не определена')
            return None

    def __le__(self, other):        # (<=)
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('Операция не определена')
            return None

    def __gt__(self, other):        # (>)
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print('Операция не определена')
            return None

    def __ge__(self, other):        # (>=)
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('Операция не определена')
            return None

    def __ne__(self, other):        # (!=)
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print('Операция не определена')
            return None

    def __eq__(self, other):   # (==)
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print('Операция не определена')
            return None

    def __add__(self, other):  # (self+other)
        if isinstance(self, House) and isinstance(other, int):                      # other -> int
            return House(self.name, self.number_of_floors + other)
        elif isinstance(self, House) and isinstance(other, House):                  # other -> House()
            return House(self.name, self.number_of_floors + other.number_of_floors)
        else:
            print('Операция не возможна')
            return False

    def __radd__(self, other):      # (other+self)
        if isinstance(self, House) and isinstance(other, int):                      # other -> int
            return House(self.name, self.number_of_floors + other)
        elif isinstance(self, House) and isinstance(other, House):                  # other -> House()
            return House(self.name, self.number_of_floors + other.number_of_floors)
        else:
            print('Операция не возможна')
            return False

    def __iadd__(self, other):      # (+=)
        if isinstance(self, House) and isinstance(other, int):  # other -> int
            return House(self.name, self.number_of_floors + other)
        elif isinstance(self, House) and isinstance(other, House):  # other -> House()
            return House(self.name, self.number_of_floors + other.number_of_floors)
        else:
            print('Операция не возможна')
            return False
    def __sub__(self, other):       # (-)
        if isinstance(self, House) and isinstance(other, int):  # other -> int
            return House(self.name, self.number_of_floors - other)
        elif isinstance(self, House) and isinstance(other, House):  # other -> House()
            return House(self.name, self.number_of_floors - other.number_of_floors)
        else:
            print('Операция не возможна')
            return False
    def __isub__(self, other):       # (-=)
        if isinstance(self, House) and isinstance(other, int):  # other -> int
            return House(self.name, self.number_of_floors - other)
        elif isinstance(self, House) and isinstance(other, House):  # other -> House()
            return House(self.name, self.number_of_floors - other.number_of_floors)
        else:
            print('Операция не возможна')
            return False
    def __mul__(self, other):       # (*)
        if isinstance(self, House) and isinstance(other, int):                      # other -> int
            return House(self.name, self.number_of_floors * other)
        elif isinstance(self, House) and isinstance(other, House):                  # other -> House()
            return House(self.name, self.number_of_floors * other.number_of_floors)
        else:
            print('Операция не возможна')
            return False

    def __imul__(self, other):       # (*=)
        if isinstance(self, House) and isinstance(other, int):                      # other -> int
            return House(self.name, self.number_of_floors * other)
        elif isinstance(self, House) and isinstance(other, House):                  # other -> House()
            return House(self.name, self.number_of_floors * other.number_of_floors)
        else:
            print('Операция не возможна')
            return False

    def __truediv__(self, other):       # (/)
        if isinstance(self, House) and isinstance(other, int):                      # other -> int
            return House(self.name, self.number_of_floors / other)
        elif isinstance(self, House) and isinstance(other, House):                  # other -> House()
            return House(self.name, self.number_of_floors / other.number_of_floors)
        else:
            print('Операция не возможна')
            return False
    def __itruediv__(self, other):       # (/=)
        if isinstance(self, House) and isinstance(other, int):                      # other -> int
            return House(self.name, self.number_of_floors / other)
        elif isinstance(self, House) and isinstance(other, House):                  # other -> House()
            return House(self.name, self.number_of_floors / other.number_of_floors)
        else:
            print('Операция не возможна')
            return False


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
