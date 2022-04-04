'''
    5. Реализовать формирование списка, используя функцию range() и возможности генератора.
    В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить
    результат вычисления произведения всех элементов списка.
'''
from functools import reduce

'''
    Функция, отвечающая за умножение
'''

def mult_func (a, b):
    return a * b

my_list = [element for element in range(100, 1001) if element % 2 == 0]
print(f'Input list: {my_list}')

'''
    Именованные переменные:
    my_list -- список с четными числами от 100 до 1000
    n -- результат умножения первых двух чисел списка
    mult_output -- итоговое число
'''

n = my_list[0]
for element in range(1, len(my_list)):
    mult_output = reduce(mult_func, [n, element])
    n = mult_output

print(f'List multiplication is {mult_output}')