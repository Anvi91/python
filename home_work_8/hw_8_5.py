# 5. Продолжить работу над первым заданием. Разработайте методы, которые
# отвечают за приём оргтехники на склад и передачу в определённое
# подразделение компании. Для хранения данных о наименовании и количестве
# единиц оргтехники, а также других данных, можно использовать любую
# подходящую структуру (например, словарь).


class OfficeEq:

    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_wh = []
        self.new_eq = {'Наименование': self.name, 'Цена': self.price,
                       'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def arriv_comp(self):
        in_name = input(f'Введите наименование ')
        in_quantity = input(f'Введите количество ')
        in_price = input(f'Введите цену ')
        new_eq = {'Наименование': in_name, 'Цена': in_price,
                  'Количество': in_quantity}

        self.new_eq.update(new_eq)
        self.my_wh.append(self.new_eq)

        return print(f'Текущий список -\n {self.my_wh}')


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
p.arriv_comp()