'''
    7. Реализовать генератор с помощью функции с ключевым словом yield,
    создающим очередное значение. При вызове функции должен создаваться
    объект-генератор. Функция вызывается следующим образом: for el in fact(n).
    Она отвечает за получение факториала числа. В цикле нужно выводить только
    первые n чисел, начиная с 1! и до n!.
'''

from math import factorial

def fact(n):
    yield factorial(n)

n = input('Enter a number: ')
if n.isdigit() == False:
    print('Enter an integer number for the factorial.')
else:
    n = int(n)
    for el in fact(n):
        print(el)