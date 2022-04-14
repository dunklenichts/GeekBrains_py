'''
    2. Создать текстовый файл (не программно), сохранить в нём
    несколько строк, выполнить подсчёт строк и слов в каждой строке.
'''

count = 0
word_count = 0
with open("my_file2.txt", "r", encoding="utf-8") as f_obj:
    print(f_obj.read())

with open("my_file2.txt", "r", encoding="utf-8") as f_obj:
    for line in enumerate(f_obj.readlines()):
        count += 1
    print(f'Emount of strokes: {count}')

with open("my_file2.txt", "r", encoding="utf-8") as f_obj:
    content = f_obj.readlines()
    for word in range(len(content)):
        print(f'Amount of {word + 1} str is {len(content[word]) - 1}')