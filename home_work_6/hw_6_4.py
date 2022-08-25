"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные
атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_l(self):
        return f'{self.name} повернула налево'

    def turn_r(self):
        return f'{self.name} повернула направо'

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} равна {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Превышение скорости автомобилем {self.name}'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Превышение скорости автомобилем {self.name}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский автомобиль'
        else:
            return f'{self.name} не полицейский автомобиль'


auto1 = SportCar(300, 'желтый', 'ferrari', False)
auto2 = TownCar(70, 'желтый', 'mazda', False)
auto3 = WorkCar(50, 'желтый', 'gaz', False)
auto4 = PoliceCar(60, 'бело-голубой', 'bmw', True)

print(auto1.go())
print(auto2.stop())
print(auto3.turn_l())
print(auto4.turn_r())
print(auto1.show_speed())
print(auto2.show_speed())
print(auto3.show_speed())
print(auto4.police())
