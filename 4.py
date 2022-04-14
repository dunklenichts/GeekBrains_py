'''
    4. Создать (не программно) текстовый файл со следующим содержимым:
            One — 1
            Two — 2
            Three — 3
            Four — 4
    Напишите программу, открывающую файл на чтение и считывающую
    построчно данные. При этом английские числительные должны заменяться
    на русские. Новый блок строк должен записываться в новый текстовый
    файл.
'''
rus_words = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []

with open("my_file4.txt", "r", encoding="utf-8") as f_obj:
    # content = f_obj.read().split('\n')
    for word in f_obj:
        word = word.split(' ', 1)
        my_list.append(rus_words[word[0]] + '' + word[1])
    print(my_list)

with open ("my_file4_new.txt", "w+", encoding="utf-8") as f_obj:
    f_obj.writelines(my_list)