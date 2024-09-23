# Практическое задание по уроку - Строки и индексация строк
# Выполнил Андрей Чекунов

example = 'Топинамбур'
print(example[0])
print(example[-1])
strLen = len(example)    # длина строки, вводим переменную, что бы дважды не вызывать метод в print
print(example[strLen//2:strLen])
# print(example[len(example)//2:len(example)])   # но можно и так
print(example[::-1])
print(example[1::2])