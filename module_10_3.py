# Домашнее задание по теме "Блокировки и обработка ошибок"
# выполнил Андрей Чекунов

import random
import threading
import time

class Bank:
    def __init__(self):
        self.lock = threading.Lock()
        #self.balance = random.randint(0,500)
        self.balance = 0

    def deposit(self):
        for i in range(100):
            x = random.randint(50,500)
            self.balance += x
            print(f'Пополнение: {x}. Баланс:{self.balance}')
            if (self.balance >= 500) and self.lock.locked() :
                self.lock.release()
                #print(f'Разблокировано')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            x = random.randint(50, 500)
            print(f'Запрос на {x}')
            if x <= self.balance:
                self.balance -= x
                print(f'Снятие: {x}. Баланс:{self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

    def run(self):
        pass

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
print(f'Начальный баланс:{bk.balance}')
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс:{bk.balance}')


