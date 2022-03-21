'''
    Пользователь вводит месяц в виде целого числа от 1 до 12.
    Сообщить, к какому времени года относится месяц
    (зима, весна, лето, осень). Напишите решения через
    list и dict.
'''

season_number = input('Enter a season number: ')

if (season_number.isdigit() == False):
    print('Enter an integer number.')
elif (int(season_number) <= 0) or (int(season_number) > 12):
    print("There's no such month")
else:
    '''
        Именованные параментры:
        season_number -- номер месяца, который вводит пользователь
        season_list -- вывод соответствующего сезона через list
        season_dict -- вывод соответствующего сезона через dict
    '''
    season_number = int(season_number)
    seasons_list = ['winter', 'spring', 'summer', 'fall']
    seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'fall'}
    if season_number == 12 or season_number == 1 or season_number == 2:
        print(f'This is {seasons_list[0]}, according to list')
        print(f'This is {seasons_dict.get(1)}, according to dict')
    elif season_number == 3 or season_number == 4 or season_number == 5:
        print(f'This is {seasons_list[1]}, according to list')
        print(f'This is {seasons_dict.get(2)}, according to dict')
    elif season_number == 6 or season_number == 7 or season_number == 7:
        print(f'This is {seasons_list[2]}, according to list')
        print(f'This is {seasons_dict.get(3)}, according to dict')
    else:
        print(f'This is {seasons_list[3]}, according to list')
        print(f'This is {seasons_dict.get(4)}, according to dict')