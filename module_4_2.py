# Домашнее задание по уроку "Пространство имен"
# выполнил Андрей Чекунов
'''
Ваша задача:
1. Создайте новую функцию test_function
2. Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать значение
    "Я в области видимости функции test_function"
3. Вызовите функцию inner_function внутри функции test_function
4. Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
'''
def test_function():
    def inner_function():
        str_ = "Я в области видимости функции test_function"
        print(str_)
    inner_function()

test_function()
#inner_function() #невозможно вызвать, т.к. вне test_function() такой функции нет
