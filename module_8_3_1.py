# Код с использованием декоратора @staticmethod

"""
Класс Car должен обладать следующими свойствами:
Атрибут объекта model - название автомобиля (строка).
Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True,
если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Атрибут __numbers - номера автомобиля (строка).
Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True,
если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение,
которое будет выводиться при выбрасывании исключения.

Работа методов __is_valid_vin и __is_valid_numbers:
__is_valid_vin
Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число.
(тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
Возвращает True, если исключения не были выброшены.
__is_valid_numbers
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана не строка.
(тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
переданная строка должна состоять ровно из 6 символов.
Возвращает True, если исключения не были выброшены.

ВАЖНО!
Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта
(в __init__ при объявлении атрибутов __vin и __numbers).
"""
# Создадим класс "Car", с помощью метода "__init__" определим атрибуты (model, __vin, __numbers) объекта.
class Car:
    def __init__(self, model, __vin, __numbers):
        # создадим атрибут объекта "model" - название автомобиля (строка).
        self.model = model
        # создадим атрибут объекта "__vin" - vin номер автомобиля (целое число).
        self.__vin = __vin
        self.__is_valid_vin(__vin)
        # создадим атрибут объекта "__numbers" - номер автомобиля (строка).
        self.__numbers = __numbers
        self.__is_valid_numbers(__numbers)

    @staticmethod
    # создадим метод "__is_valid_vin", который принимает один атрибут "vin_number".
    def __is_valid_vin(vin_number):
        # создадим условие, где будем проверять атрибут "vin_number" методом "isinstance" принадлежность
        # к числовому(int) типу, если условие не выполняется, будем с помощью ключевого слова "raise" передавать
        # исключение с сообщением.
        if not (isinstance(vin_number, int)):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        # создадим условие, где будем проверять количество передаваемых символов в атрибут "vin_number" в диапазоне,
        # если условие не выполняется, будем с помощью ключевого слова "raise" передавать исключение с сообщением.
        if not (9999999 >= vin_number and vin_number >= 1000000):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        # если исключение не выполнено, вернем(return) "True".
        return True

    @staticmethod
    # создадим метод "__is_valid_numbers", который принимает один атрибут "numbers".
    def __is_valid_numbers(numbers):
        # создадим условие, где будем проверять атрибут "numbers" методом "isinstance" принадлежность к
        # строковому(str) типу, если условие не выполняется, будем с помощью ключевого слова "raise" передавать
        # исключение с сообщением.
        if not (isinstance(numbers, str)):
            raise IncorrectCarNumbers('Некорректный тип данных для номера')
        # создадим условие, где будем проверять длину передаваемых значений в атрибут "numbers" функцией "len",
        # если условие не выполняется, будем с помощью ключевого слова "raise" передавать исключение с сообщением.
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        # если исключение не выполнено, вернем (return) "True".
        return True

# Создадим класс исключений "IncorrectVinNumber", который наследуется от базового класса "Exception".
class IncorrectVinNumber(Exception):
    # создадим метод "__init__"(конструктор), который принимает один атрибут "message".
    def __init__(self, message):
        # создадим атрибут объекта "message" - сообщение.
        self.message = message

# Создадим класс исключений "IncorrectVinNumber", который наследуется от базового класса "Exception".
class IncorrectCarNumbers(Exception):
    # создадим метод "__init__"(конструктор), который принимает один атрибут "message".
    def __init__(self, message):
        # создадим атрибут объекта "message" - сообщение.
        self.message = message

# создадим конструкцию "try/except", в блоке "try" вызовем класс "Car" куда передадим значения атрибутов и сохраним в
# переменную "first".
try:
    first = Car('Model1', 1000000, 'f123dj')
# в блоке "except" перехватываем исключение "IncorrectVinNumber", сохраняя его в переменной "exc".
except IncorrectVinNumber as exc:
    # выводим на печать содержимое атрибута "exc.message".
    print(exc.message)
# в блоке "except" перехватываем исключение "IncorrectCarNumbers", сохраняя его в переменной "exc".
except IncorrectCarNumbers as exc:
    # выводим на печать содержимое атрибута "exc.message".
    print(exc.message)
# если в блоке "try" не произошло ошибок(исключений) выполняется блок "else", и выводим на печать сообщение,
# и значение переменной "first" с атрибутом "model".
else:
    print(f'{first.model} успешно создан')

# создадим конструкцию "try/except", в блоке "try" вызовем класс "Car" куда передадим значения атрибутов и сохраним в
# переменную "second".
try:
    second = Car('Model2', 300, 'т001тр')
# в блоке "except" перехватываем исключение "IncorrectVinNumber", сохраняя его в переменной "exc".
except IncorrectVinNumber as exc:
    # выводим на печать содержимое атрибута "exc.message".
    print(exc.message)
# в блоке "except" перехватываем исключение "IncorrectCarNumbers", сохраняя его в переменной "exc".
except IncorrectCarNumbers as exc:
    # выводим на печать содержимое атрибута "exc.message".
    print(exc.message)
# если в блоке "try" не произошло ошибок(исключений) выполняется блок "else", и выводим на печать сообщение,
# и значение переменной "second" с атрибутом "model".
else:
    print(f'{second.model} успешно создан')

# создадим конструкцию "try/except", в блоке "try" вызовем класс "Car" куда передадим значения атрибутов и сохраним в
# переменную "third".
try:
    third = Car('Model3', 2020202, 'нет номера')
# в блоке "except" перехватываем исключение "IncorrectVinNumber", сохраняя его в переменной "exc".
except IncorrectVinNumber as exc:
  # выводим на печать содержимое атрибута "exc.message".
    print(exc.message)
# в блоке "except" перехватываем исключение "IncorrectCarNumbers", сохраняя его в переменной "exc".
except IncorrectCarNumbers as exc:
    # выводим на печать содержимое атрибута "exc.message".
    print(exc.message)
# если в блоке "try" не произошло ошибок(исключений) выполняется блок "else", и выводим на печать сообщение,
# и значение переменной "third" с атрибутом "model".
else:
    print(f'{third.model} успешно создан')


# Model1 успешно создан
# Неверный диапазон для vin номера
# Неверная длина номера