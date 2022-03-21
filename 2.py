"""
    Для списка реализовать обмен значений соседних элементов.
    Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
    и т. д. При нечётном количестве элементов последний сохранить
    на своём месте. Для заполнения списка элементов нужно использовать
    функцию input().
"""
s = input('Enter a string: ')
my_list = list(s)
element = 0

if (len(s) % 2 == 0):
    while element < len(my_list):
        '''
            Именованные параментры:
            temp -- временная переменная для перестановки
            element - индекс символа
        '''
        temp = my_list[element]
        my_list[element] = my_list[element + 1]
        my_list[element + 1] = temp
        element += 2
else:
    while element < (len(my_list) - 1):
        temp = my_list[element]
        my_list[element] = my_list[element + 1]
        my_list[element + 1] = temp
        element += 2
print(my_list)