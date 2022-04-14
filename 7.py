'''
    7. Создать вручную и заполнить несколькими строками текстовый
    файл, в котором каждая строка будет содержать данные о фирме:
    название, форма собственности, выручка, издержки.
    Необходимо построчно прочитать файл, вычислить прибыль каждой
    компании, а также среднюю прибыль. Если фирма получила убытки,
    в расчёт средней прибыли её не включать.
    Далее реализовать список. Он должен содержать словарь с фирмами и
    их прибылями, а также словарь со средней прибылью. Если фирма
    получила убытки, также добавить её в словарь (со значением убытков).
'''
import json
bonus = {}
count = 0
temp = 0
avr_dict = {}

with open("my_file7.txt", 'r', encoding="utf-8") as f_obj:
    for word in f_obj:
        name, firm_type, income, costs = word.split()
        if (int(income) - int(costs)) >= 0:
            bonus[name] = int(income) - int(costs)
            temp += (int(income) - int(costs))
            count += 1
        else:
            bonus[f'losses of {name}'] = int(income) - int(costs)
    avr_dict['average profit'] = temp / count
    bonus.update(avr_dict)
    print(f'profit: {bonus}')
    # print(f'average profit: {avr_dict}')

with open("my_file7.json", 'w+', encoding="utf-8") as f_obj:
    json.dump(bonus, f_obj)
    bonus_json = json.dumps(bonus)
    print(f'json type: {bonus_json}')
