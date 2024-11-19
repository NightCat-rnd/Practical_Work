# Домашнее задание по теме "Множественное наследование"
# выполнил Андрей Чекунов
from random import randrange
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self,speed):
        self._cords = [0,0,0]
        self.speed = speed
    def move(self,dx,dy,dz):
        if (self.speed * dz) < 0 :
            print(f"It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed
    def get_cords(self):
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER < 5 :
            print("Sorry, i'm peaceful")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    def __init__(self, speed):
        self.beak = True
        super().__init__(speed)
    def lay_eggs(self):
        print(f'Here are(is) {randrange(1,4)} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def __init__(self,speed):
        super().__init__(speed)
    def dive_in(self,dz):
        self._cords[2] -= abs(dz * int(self.speed / 2))

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    def __init__(self,speed):
        super().__init__(speed)

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    def __init__(self,speed):
        #print(Duckbill.mro())
        self.sound = "Click-click-click"
        super().__init__(speed)
    def speak(self):
        print(f'{self.sound}')

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
''' 
Вывод на консоль:
True
True
Click-click-click
Be careful, i'm attacking you 0_0
X: 10 Y: 20 Z: 30
X: 10 Y: 20 Z: 0
Here are(is) 3 eggs for you # Число может быть другим (1-4)
'''
