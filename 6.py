'''
    6. Реализовать два небольших скрипта:
        6.1. итератор, генерирующий целые числа, начиная с указанного;
        6.2. итератор, повторяющий элементы некоторого списка, определённого
             заранее. Подсказка: используйте функцию count() и cycle() модуля
             itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным.
             Предусмотрите условие его завершения. #### Например, в первом задании выводим
             целые числа, начиная с 3. При достижении числа 10 — завершаем цикл. Вторым
             пунктом необходимо предусмотреть условие, при котором повторение элементов
             списка прекратится.
'''

import itertools

a = input('Enter a start number: ')

'''
    Именованные переменные:
    a -- начало генераторации чисел
    my_list -- исходный список чисел
    counter -- счетчик для окончания цикла count
    new_list -- список для второй части задачи
'''
if a.isdigit() == False:
    print('Enter an integer number.')
else:
    a = int(a)
    my_list = []
    counter = 0
    for element in itertools.count(a):
        counter += 1
        my_list.append(element)
        if counter == 10: break
    print(f'6.1. Output list: {my_list}')

new_list = []
for element in itertools.cycle(my_list):
    new_list.append(element)
    if element == a * 2: break
print(f'6.2. Output list: {new_list}')