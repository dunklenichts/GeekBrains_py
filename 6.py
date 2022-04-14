'''
    6. Сформировать (не программно) текстовый файл. В нём каждая
    строка должна описывать учебный предмет и наличие лекционных,
    практических и лабораторных занятий по предмету. Сюда должно
    входить и количество занятий. Необязательно, чтобы для каждого
    предмета были все типы занятий.
    Сформировать словарь, содержащий название предмета и общее
    количество занятий по нему. Вывести его на экран.
'''
import re

dict = {}
lesson_hours = 0
with open("my_file6.txt", "r", encoding="utf-8") as f_obj:
    for word in f_obj:
        lesson, lecture, practice, labs = re.split(',|:', word)
        # print(f'lesson = {lesson}')
        # print(f'lectures = {lecture}')
        # print(f'practice = {practice}')
        # print(f'labs = {labs}')
        dict['lesson'] = lesson
        dict['lectures'] = int(lecture)
    print(dict)




        # lesson, lecture, amount = re.split(":|,|-", word)
        # print(f'{lesson}, {lecture}')
        # print(f'l = {lesson}')
        # print(f'lec = {lecture}')