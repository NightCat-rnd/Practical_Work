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
global_a = 'Global A'
def test_function():
    global global_a
    global_a += ' test_function'
    test_a = ' Test_Function'
    def inner_function():
        nonlocal test_a
        global global_a
        str_ = "Я в области видимости функции test_function"
        print(str_)
        test_a += ' inner_function'
        global_a += test_a
        print(locals())
    inner_function()
    print(locals())


for i in range(3):
    print('Iteration:',i)
    test_function()
    print(global_a)
#inner_function()
