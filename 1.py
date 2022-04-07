'''
    1. Реализовать класс Matrix (матрица). Обеспечить перегрузку
    конструктора класса (метод __init__()), который должен принимать
    данные (список списков) для формирования матрицы.

    Следующий шаг — реализовать перегрузку метода __str__() для вывода
    матрицы в привычном виде.

    Далее реализовать перегрузку метода __add__() для реализации
    операции сложения двух объектов класса Matrix (двух матриц).
    Результатом сложения должна быть новая матрица.
'''

class Matrix():
    def __init__(self, param_1):
        self.param_1 = param_1

    def __str__(self):
        for i in self.param_1:
            print(i)
        return ''

    def __add__(self, other):
        for i in range(len(self.param_1)):
            for j in range(len(other.param_1)):
                self.param_1[i][j] = self.param_1[i][j] + other.param_1[i][j]
        return Matrix.__str__(self)

mc = Matrix([[1, 2, 3], [4, 5, 6]])
mc_2 = Matrix([[2, 3, 4], [5, 6, 7]])
print(mc)
print(mc + mc_2)