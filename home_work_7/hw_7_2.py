""""2. Реализовать проект расчёта суммарного расхода ткани на производство 
одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь 
определённое название. К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и 
 рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: 
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих 
методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на 
этом уроке знания: реализовать абстрактные классы для основных классов проекта,
 проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def consumption_c(self):
        return f'Абстракция'

    @abstractmethod
    def consumption_j(self):
        return f'Абстракция'

    @property
    def consumption_all(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cons_c = self.width / 6.5 + 0.5

    def consumption_c(self):
        return f'Площадь на пальто {self.width / 6.5 + 0.5}'

    def consumption_j(self):
        return f'Абстракция'

    def __str__(self):
        return f'Площадь на пальто {self.cons_c}'


class Jacket(Clothes):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cons_j = self.height * 2 + 0.3

    def consumption_j(self):
        return f'Площадь на костюм {self.height * 2 + 0.3}'

    def consumption_c(self):
        return f'Абстракция'

    def __str__(self):
        return f'Площадь на костюм {self.cons_j}'


coat = Coat(3, 4)
jacket = Jacket(3, 4)

print(coat.consumption_c())
print(jacket.consumption_j())
print(jacket.consumption_all)
