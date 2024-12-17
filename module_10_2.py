# Домашнее задание по теме "Потоки на классах"
# выполнил Андрей Чекунов

import threading
import time

class Knight(threading.Thread):

    def __init__(self, name:str, power:int, enemy=100, war_day=0, delay=1):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = enemy
        self.war_day = war_day
        self.delay = delay

    def war(self):
        while True:
            time.sleep(self.delay)
            if self.enemy <= 0 :
                print(f'{self.name} одержал победу спустя {self.war_day} дней (дня)')
                break
            else:
                self.enemy -= self.power
                self.war_day += 1
                print(f'{self.name} сражается {self.war_day}..., осталось {self.enemy} воинов')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.war()



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')