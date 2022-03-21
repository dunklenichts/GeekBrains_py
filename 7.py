"""
    Продолжить работу над заданием. В программу должна попадать
    строка из слов, разделённых пробелом. Каждое слово состоит
    из латинских букв в нижнем регистре. Нужно сделать вывод
    исходной строки, но каждое слово должно начинаться с заглавной
    буквы. Используйте написанную ранее функцию int_func().
"""

def int_func(text):
    new_txt = list(text)
    new_txt[0] = new_txt[0].upper()
    return ''.join(new_txt)

def int_func2(text2):
    result = []
    word_list = text2.split(' ')
    for word in word_list:
        result.append(int_func(word))
    return ' '.join(result)

s = input("Enter a string: ")
print(f"{int_func2(s)}")