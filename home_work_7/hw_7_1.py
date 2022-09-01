""""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора 
класса (метод __init__()), который должен принимать данные (список списков) 
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных 
в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в 
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
 двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
  новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
 первой строки первой матрицы складываем с первым элементом первой строки 
 второй матрицы и т.д.
"""""


class Matrix():

    def __init__(self, list_1, list_2, list_3):
        self.list_1 = list(list_1)
        self.list_2 = list(list_2)
        self.list_3 = list(list_3)

    def __str__(self):
        return ' '.join(map(str, self.list_1)) + '\n' + ' '.join(
            map(str, self.list_2)) + '\n' + ' '.join(
            map(str, self.list_3)) + '\n'

    def __add__(self, other):
        matrix_sum_l1 = []
        matrix_sum_l2 = []
        matrix_sum_l3 = []
        for i in range(len(self.list_1)):
            matrix_sum_l1.append(self.list_1[i] + other.list_1[i])
            matrix_sum_l2.append(self.list_2[i] + other.list_2[i])
            matrix_sum_l3.append(self.list_3[i] + other.list_3[i])
        return ' '.join(map(str, matrix_sum_l1)) + '\n' + ' '.join(
            map(str, matrix_sum_l2)) + '\n' + ' '.join(
            map(str, matrix_sum_l3)) + '\n'


a = Matrix([31, 32, 1], [37, 43, 1], [51, 86, 1])
b = Matrix([3, 5, 32], [2, 5, 6], [-1, 64, -8])
print(a)
print(b)
print(f'Сумма матриц:\n{a + b}')
