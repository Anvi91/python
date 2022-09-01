# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два
# метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с
# декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Data:
    def __init__(self, my_date):
        self.my_date = str(my_date)

    @classmethod
    def extract(cls, my_date):
        my_date_ex = []

        for i in my_date.split():
            if i != '-': my_date_ex.append(i)

        return int(my_date_ex[0]), int(my_date_ex[1]), int(my_date_ex[2])

    @staticmethod
    def validate(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Проверка пройдена'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.my_date)}'


a = Data('1 - 9 - 2022')
print(a)
print(Data.validate(1, 9, 2022))
print(Data.extract('1 - 9 - 2022'))

