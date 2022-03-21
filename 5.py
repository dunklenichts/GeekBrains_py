'''
    Реализовать структуру «Рейтинг», представляющую собой набор
    натуральных чисел, который не возрастает. У пользователя нужно
    запрашивать новый элемент рейтинга. Если в рейтинге существуют
    элементы с одинаковыми значениями, то новый элемент с тем же
    значением должен разместиться после них.
'''

my_list = [7, 5, 3, 3, 2]
print(f'Current rating: {my_list}')
new_rang = input('Enter a number: ')

if (new_rang.isdigit() == False):
    print('Enter an integer number')
else:
    '''
        Именованные параметры:
        new_rang -- ранг, который вводит пользователь
        list_rang -- список рангов
    '''
    new_rang = int(new_rang)
    for element in range(len(my_list)):
        if my_list[element] == new_rang:
            my_list.insert(element + 1, new_rang)
            break
        else:
            my_list.append(new_rang)
            break
    my_list.sort(reverse=True)
    print(f'Your new rating: {my_list}')