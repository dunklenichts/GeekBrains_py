'''
    3. Создать текстовый файл (не программно). Построчно записать
    фамилии сотрудников и величину их окладов (не менее 10 строк).
    Определить, кто из сотрудников имеет оклад менее 20 тысяч,
    вывести фамилии этих сотрудников. Выполнить подсчёт средней
    величины дохода сотрудников.
'''
with open("my_file3.txt", "r", encoding="utf-8") as f_obj:
    content = f_obj.read().split('\n')
    print(f'{content}\n')

with open("my_file3.txt", "r", encoding="utf-8") as f_obj:
    my_list = f_obj.read().split('\n')
    new_list = []

    for word in my_list:
        word = word.split()
        if int(word[1]) < 20000:
            new_list.append(word[0])
    print(f'These employees have salary less than 20 000: {new_list}')