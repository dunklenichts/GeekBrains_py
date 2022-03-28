'''
    4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
    Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите
    в порядке их следования в исходном списке. Для выполнения задания обязательно
    используйте генератор.
'''
import random

my_list = [random.randint(1, 10) for element in range(10)]
print(f'Input list: {my_list}')

# print(my_list)
# my_list = sorted(my_list)
# print(my_list)

new_list = []

for i in my_list:
    if my_list.count(i) == 1:
        new_list.append(i)

print(f'Output list: {new_list}')
