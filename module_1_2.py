# Практическое задание по теме "Переменные".
# Выполнил Андрей Чекунов

number_of_homework = 12
number_of_hours = 1.5
course_name = 'Python'
time_spent = number_of_hours / number_of_homework
# различные способы вывода
# конкатенация
print('Курс: ' + course_name + ', всего задач: ' + str(number_of_homework) +
        ', среднее время выполнения: ' + str(time_spent) + ' часа.')
# %-форматирование
print('Курс: %s, всего задач: %d, среднее время выподнения: %0.3f часа.'
      % (course_name, number_of_homework, time_spent))
# метод .format
print('Курс: {}, всего задач: {}, среднее время выполнения: {} часа.'.format(course_name,
        number_of_homework, time_spent))
# f-строка
print(f'Курс: {course_name}, всего задач: {number_of_homework}, среднее время выполнения: '
      f'{time_spent} часа.')