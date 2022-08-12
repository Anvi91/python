# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    num_list = [arg_1, arg_2, arg_3]
    num_list.sort(reverse=True)
    print(f'Сумма двух наибольших : {num_list[0] + num_list[1]}')


try:
    a = float(input('Введите аргумент 1: '))
    b = float(input('Введите аргумент 2: '))
    c = float(input('Введите аргумент 3: '))
except ValueError:
    print(f'Введено не число')
    sys.exit()

my_func(a, b, c)
