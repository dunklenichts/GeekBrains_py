'''
    3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
    Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
    соответствующий количеству ячеек клетки (целое число). В классе должны быть
    реализованы методы перегрузки арифметических операторов: сложение (__add__()),
    вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные
    методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
    умножение и целочисленное (с округлением до целого) деление клеток,
    соответственно.
'''

class  Cell():
    def __init__(self, cell_amount):
        self.cell_amount = cell_amount
        # if cell_amount.isdigit == True:
        #     print ('')
        # else:
        #     print('Error')

    def __str__(self):
        return self.cell_amount * '*'

    def __add__(self, other):
        return Cell(self.cell_amount + other.cell_amount)

    def __sub__(self, other):
        if (self.cell_amount - other.cell_amount) < 0:
            print ('Error')
        else:
            return Cell(self.cell_amount - other.cell_amount)

    def __mul__(self, other):
        return Cell(self.cell_amount * other.cell_amount)

    def __truediv__(self, other):
        return Cell(self.cell_amount // other.cell_amount)

    def make_order(self, other):
        output_str = ''
        for element in range(self.cell_amount // other):
            output_str += '*' * other + "\\n"
        return output_str

cell = Cell(7)
cell_2 = Cell(2)

print(f'Sum: {cell + cell_2}')
print(f'Sub: {cell - cell_2}')
print(f'Mul: {cell * cell_2}')
print(f"Div: {cell / cell_2}")

print(cell.make_order(7))