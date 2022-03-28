'''
    2. Представлен список чисел. Необходимо вывести элементы исходного списка,
    значения которых больше предыдущего элемента.
'''
import random

my_list = [random.randint(0, 15) for i in range(15)] # создание списка из сгенерированных чисел
print(f'Input list: {my_list}')                      # вывод исходного списка чисел
output_list = []

'''
   Именованные переменные:
   my_list -- список с исходными сгенерированными числами
   output_list -- список с итоговыми числами
'''

for element in range(1, len(my_list)):
    if my_list[element] > my_list[element - 1]:
        output_list.append(my_list[element])

print(f'Output list: {output_list}')