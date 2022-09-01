# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым для
# классов-наследников. Эти классы — конкретные типы оргтехники (принтер,
# сканер, ксерокс). В базовом классе определите параметры, общие для
# приведённых типов. В классах-наследниках реализуйте параметры, уникальные
# для каждого типа оргтехники.

class OfficeEq:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'


class Printer(OfficeEq):
    def __init__(self, name, price, quantity, print_speed):
        super().__init__(name, price, quantity)
        self.print_speed = print_speed

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity} ' \
               f' скорость печати {self.print_speed}'


class Scanner(OfficeEq):
    def __init__(self, name, price, quantity, scanning_speed):
        super().__init__(name, price, quantity)
        self.scanning_speed = scanning_speed

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity} ' \
               f'скорость сканирования {self.scanning_speed}'


class Copier(OfficeEq):
    def __init__(self, name, price, quantity, copy_speed):
        super().__init__(name, price, quantity)
        self.copy_speed = copy_speed

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity} ' \
               f'скорость копирования {self.copy_speed}'


p = Printer('hp', 1800, 5, 100)
s = Scanner('Canon', 12000, 3, 90)
c = Copier('Xerox', 7000, 2, 60)
print(p)
print(s)
print(c)
