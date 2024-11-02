# Домашняя работа по уроку "Перегрузка операторов"
# Выполнил Андрей Чекунов
'''
Задача "Нужно больше этажей":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".

Необходимо дополнить класс House следующими специальными методами:
__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и
возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении
участвует кол-во этажей.
__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат
его вызова).
Остальные методы арифметических операторов, где self - x, other - y:

Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики
перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
isinstance(other, int) - other указывает на объект типа int.
isinstance(other, House) - other указывает на объект типа House.

Пример результата выполнения программы:
Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
False
Название: ЖК Эльбрус, кол-во этажей: 20
True
Название: ЖК Эльбрус, кол-во этажей: 30
Название: ЖК Акация, кол-во этажей: 30
False
True
False
True
False
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
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__