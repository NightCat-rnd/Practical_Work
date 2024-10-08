# Дополнительное практическое задание по модулю: "Базовые структуры данных."
# Выполнил: Андрей Чекунов

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # исходный список с оценками
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # исходное множество студентов
# по условию список оценок отсортирован по алфавиту списка студентов
# множество студентов не отсортировано
# считаем что количество студентов совпадает со списком оценок, так по условию:) не усложняем себе жизнь
print('Исходный список с оценками',grades)
print('Исходное множество студентов',students)
list_students = list(students)  # преобразуем множество студентов в список
#print('Список студентов преобразованный из множества ',list_students)
sorted_list_students = sorted(list_students) # Сортируем список с фамилиями методом sorted(), с созданием нового списка студентов
# можно было использовать метод sort(), но он применяется к текущему списку, т.е. меняет исходный список
# на самом деле нам без разницы, можно и так и так
#print('Сортированный список студентов',sorted_list_students)
# делаем список среднего балла
# интересно как это делать, если чисто теоретически циклы и условия мы еще не учили:)
# может быть повторить вручную с каждым элементом списка, но это долго
# поэтому сделаю как могу через циклы
quantity_of_grades = len(grades)
quantity_of_students = len(sorted_list_students)
if quantity_of_grades != quantity_of_students :
    print('Количество студентов и количество оценок не совпадает')
average_grades = [0]*quantity_of_grades # создаем  список для средних оценок из нулевых элементов по количеству студентов
i=0
for item in grades :
    average_grades[i] = round(sum(item) / len(item),2) # вычисляем среднее и округляем до сотых, что бы красиво было
    i += 1
#print('Список со средними оценками: ',average_grades)
# Упаковываем сортированный список студентов и средние оценки в словарь
student_grades = dict(zip(sorted_list_students,average_grades))
print('Итоговый словарь студентов со средними оценками',)
print(student_grades)
print('-----------------')
print('Студент: средняя оценка')   # так выглядит привлекательнее
for key,value in student_grades.items():
    print(f'{key}: {value}')
