# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на
# ноль. Проверьте его работу на данных, вводимых пользователем. При вводе нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class DivNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def div_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Нельзя делить на ноль")


print(DivNull.div_null(10, 0))
print(DivNull.div_null(10, 0.1))
