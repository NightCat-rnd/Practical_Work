# Домашнее задание по теме  "Зачем нужно наследование"
# Выполнил Андрей Чекунов

class Animal:

    def __init__(self, name:str):
        self.name = name
        self.alive = True
        self.fed = False
    def __str__(self):
        return 'Animal'
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    edible = False
    def __init__(self,name:str):
        self.name = name
    def __str__(self):
        return 'Plant'

class Mammal(Animal):
    def __str__(self):
        return 'Mammal'

class Predator(Animal):
    def __str__(self):
        return 'Predator'

class Flower(Plant):
    def __str__(self):
        return 'Flower'

class Fruit(Plant):
    edible = True
    def __str__(self):
        return 'Fruit'

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

'''
Вывод на консоль:
Волк с Уолл-Стрит
Цветик семицветик
True
False
Волк с Уолл-Стрит не стал есть Цветик семицветик
Хатико съел Заводной апельсин
False
True
'''