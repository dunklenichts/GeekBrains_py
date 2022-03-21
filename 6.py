"""
    Реализовать функцию int_func(), принимающую слова из маленьких
    латинских букв и возвращающую их же, но с прописной первой буквой.
    Например, print(int_func(‘text’)) -> Text.
"""
def int_func(text):
    new_txt = list(text)
    new_txt[0] = new_txt[0].upper()
    return ''.join(new_txt)

s = input("Enter a string: ")
print(f'Output: {int_func(s)}')