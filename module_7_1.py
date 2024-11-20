# Домашнее задание по теме "Режимы открытия файлов"
# выполнил Андрей Чекунов
import os
class Product:
    def __init__(self, name:str, weight:(int,float), category:str):
        self.name = name
        self.weight = weight
        self. category = category
    def __str__(self)->str:
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'product.txt'
    def get_products(self)->str:
        if os.path.isfile(self.__file_name):
            file = open(self.__file_name, "r")
            file_contents = file.read()
            file.close()
            return file_contents
        else:
            print(f'Файл "{self.__file_name}" не существует')
            return None

    def add(self, *products:Product):
        if os.path.exists(self.__file_name):
            file = open(self.__file_name, "r+")
            lines = file.readlines()
            first_word = []
            for line in lines:
                first_word.append(line.strip().split(',')[0])
            for arg in products:
                if arg.name in first_word:
                    print(f'Продукт {arg.name} уже есть в магазине')
                else:
                    file.write(f'{arg.name}, {arg.weight}, {arg.category}\n')
            file.close()
        else:
            file = open(self.__file_name, "a")
            for arg in products:
                file.write(f'{arg.name}, {arg.weight}, {arg.category}\n')
            file.close()

#Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
#print(p1)
p2 = Product('Spaghetti', 3.4, 'Groceries')
print(p2)
p3 = Product('Potato', 5.5, 'Vegetables')
#print(p3) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
#p4 = Product('Apple', 70, 'Vegetables')
#s1.add(p3,p4)
#print(s1.get_products())

'''
Вывод на консоль:
Первый запуск:
Spaghetti, 3.4, Groceries
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables
Второй запуск:
Spaghetti, 3.4, Groceries
Продукт Potato, 50.5, Vegetables уже есть в магазине
Продукт Spaghetti, 3.4, Groceries уже есть в магазине
Продукт Potato, 5.5, Vegetables уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables
'''