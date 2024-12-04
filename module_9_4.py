# Домашнее задание по теме "Создание функций на лету"
# выполнил Андрей Чекунов

# 1
first =  'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x,y: x==y, first, second)))
#Результатом должен быть список совпадения букв в той же позиции:
#[False, True, True, False, False, False, False, False, True, False, False, False, False, False]
#Где True - совпало, False - не совпало.

#2
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i)+'\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#3
from random import choice
class MysticBall:
    words = []
    def __init__(self,*words):
        for i in words:
            self.words.append(i)
    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
