'''
    Пользователь вводит строку из нескольких слов, разделённых пробелами.
    Вывести каждое слово с новой строки. Строки нужно пронумеровать.
    Если слово длинное, выводить только первые 10 букв в слове.
'''

input_string = input('Enter a string: ')
count = 0
word_list = input_string.split(' ')

for element in range(len(input_string.split(' '))):
    '''
        Именованные параметры:
        count -- количество слов
        word_list -- список отдельных слов, разделенных пробелом
        input_string -- исходная строка
    '''
    word_list = input_string.split()
    count += 1
    if len(str(word_list)) <= 10:
        print(f'{count}. {word_list[element]}')
    else:
        print(f'{count}. {word_list[element][:10]}')