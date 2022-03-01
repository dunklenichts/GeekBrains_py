# 1. Поработайте с переменными, создайте несколько, выведите на экран. 
#    Запросите у пользователя некоторые числа и строки и сохраните в переменные, 
#    затем выведите на экран.

name = input('Enter your name: ')
print(f'Hello, {name}')
number = input('Enter a number: ')
number = int(number)
if number:
    print(f'Your number is {number}')
else:
    print('Enter a number')
