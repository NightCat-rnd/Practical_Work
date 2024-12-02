# Домашнее задание по теме "Создание исключений"
# выполнил Андрей Чекунов
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if Car.__is_valid_vin(vin):
            self.__vin = vin
        if Car.__is_valid_numbers(numbers):
            self.__numbers = numbers
    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber(f'Не корректный тип vin - {vin_number}')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber(f'Не верный диапазон для vin - {vin_number}')
        return True
    def __is_valid_numbers(numbers):
        if not isinstance(numbers,str):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров - {numbers}')
        if len(numbers) != 6:
            raise IncorrectCarNumbers(f'Неверная длина номера - {numbers}')
        return  True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')