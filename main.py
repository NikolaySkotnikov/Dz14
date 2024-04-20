# Задание 1.
# К уже реализованному классу «Дробь» добавьте статический
# метод, который при вызове возвращает количество
# созданных объектов класса «Дробь».

def gcd(i, j):
    if j == 0:
        return i
    return gcd(j, i % j)


class Fraction:

    count = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1


    def sum(self, other):
        new_numerator = (self.numerator * other.denominator + self.denominator * other.numerator)
        new_denominator = self.denominator * other.denominator
        common_part = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator/common_part, new_denominator/common_part)

    def subtract(self, other):
        new_numerator = (self.numerator * other.denominator - self.denominator * other.numerator)
        new_denominator = self.denominator * other.denominator
        common_part = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator/common_part, new_denominator/common_part)

    def multiply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        common_part = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator/common_part, new_denominator/common_part)

    def divide(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        common_part = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator/common_part, new_denominator/common_part)

    def __str__(self):
        return f'{int(self.numerator)}/{int(self.denominator)}'

    @staticmethod
    def get_count():
        return print(f'Создано объектов класса Дробь: {Fraction.count}')

a = Fraction(2, 5)
b = Fraction(3, 4)
c = Fraction(36, 51)
Fraction.get_count()

# Задание 2.
# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт
# и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температуры и
# возвращать это значение с помощью статического метода.

class DegreeConverter:

    count = 0

    @staticmethod
    def celsius_to_fahrenheit(temp_celsius):
        DegreeConverter.count += 1
        return print(f'{temp_celsius} градусов Цельсия равно {int((temp_celsius * 9/5) + 32)} градусов Фаренгейта.')

    @staticmethod
    def fahrenheit_to_celsius(temp_fahrenheit):
        DegreeConverter.count += 1
        return print(f'{temp_fahrenheit} градусов Фаренгейта равно {int((temp_fahrenheit - 32) * 9/5)} градусов Цельсия.')

    @staticmethod
    def get_count():
        return print(f'Подсчётов температур: {DegreeConverter.count}')

DegreeConverter.celsius_to_fahrenheit(12)
DegreeConverter.fahrenheit_to_celsius(35)
DegreeConverter.get_count()

# Задание 3.
# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.

class LengthConverter:

    @staticmethod
    def meter_to_inch(meter):
        return print(f'{meter} метров равно {round(meter * 39.37, 2)} дюймов.')

    @staticmethod
    def meter_to_foot(meter):
        return print(f'{meter} метров равно {round(meter * 3.281, 2)} футов.')

    @staticmethod
    def meter_to_yard(meter):
        return print(f'{meter} метров равно {round(meter * 1.094, 2)} ярдов.')

    @staticmethod
    def inch_to_meter(inch):
        return print(f'{inch} дюймов равно {round(inch / 39.37, 2)} метров.')

    @staticmethod
    def foot_to_meter(foot):
        return print(f'{foot} футов равно {round(foot / 3.281, 2)} метров.')

    @staticmethod
    def yard_to_meter(yard):
        return print(f'{yard} ярдов равно {round(yard / 1.094, 2)} метров.')

LengthConverter.meter_to_foot(10)
LengthConverter.meter_to_yard(100)
LengthConverter.meter_to_inch(50)
LengthConverter.inch_to_meter(10)
LengthConverter.foot_to_meter(25)
LengthConverter.yard_to_meter(68)
