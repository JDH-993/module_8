class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.is_valid_vin(__vin)
        self.is_valid_numbers(__numbers)

    def is_valid_vin(self, vin_number):
        if type(vin_number) == float:
            raise IncorrectVinNumber("Некорректный тип vin номер")
        elif 1000000 > vin_number or vin_number > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        else:
            return True

    def  is_valid_numbers(self, numbers):
        if type(numbers) != str:
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        else:
            return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message= message
    pass

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
    pass

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



