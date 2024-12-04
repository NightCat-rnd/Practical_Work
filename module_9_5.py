# Домашнее задание по теме "Итераторы"
# выполнил Андрей Чекунов

class StepValueError(ValueError):
    pass
class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError
        else:
            self.start = start
            self.stop = stop
            self.step = step
            self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        res = self.pointer
        if self.step < 0 :
            if self.pointer < self.stop:
                raise StopIteration()
            else:
                self.pointer += self.step
                return res
        else:
            if self.pointer > self.stop:
                raise StopIteration()
            else:
                self.pointer += self.step
                return res

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)
iter6 = Iterator(10,5,-1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
'''
Шаг указан неверно
-5 -4 -3 -2 -1 0 1
6 8 10 12 14
5 4 3 2 1

'''