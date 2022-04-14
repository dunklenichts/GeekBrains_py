'''
    1. Создать программный файл в текстовом формате, записать в
    него построчно данные, вводимые пользователем. Об окончании
    ввода данных будет свидетельствовать пустая строка.
'''

try:
    with open("my_file.txt", "w+", encoding="utf-8") as f_obj:  # перезаписываем содержимое файла или создаем его
        while True:
            input_str = input('Enter text: ')
            f_obj.write(input_str + ' ')
            if input_str == '':
                break
    with open("my_file.txt", "r", encoding="utf-8") as f_obj:   # открываем файл на чтение
        for line in f_obj:
            print(line)
except IOError:
    print('ERROR')