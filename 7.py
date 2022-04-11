'''
    7. Реализовать проект «Операции с комплексными числами».
    Создайте класс «Комплексное число». Реализуйте перегрузку
    методов сложения и умножения комплексных чисел. Проверьте
    работу проекта. Для этого создаёте экземпляры класса
    (комплексные числа), выполните сложение и умножение созданных
    экземпляров. Проверьте корректность полученного результата.
'''
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Add = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Mul = {self.a * other.a - self.b * other.b} + {self.a * other.b + other.a * self.b} * i'

    def __str__(self):
        return f'{self.a} + {self.b} * i'

a = ComplexNumber(1, 2)
b = ComplexNumber(3, 4)
print(a)
print(b)
print(a + b)
print(a * b)