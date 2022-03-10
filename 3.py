"""
    Реализовать функцию my_func(), которая принимает три
    позиционных аргумента и возвращает сумму наибольших
    двух аргументов.
"""
arg1 = input('Enter first number: ')
arg2 = input('Enter second number: ')
arg3 = input('Enter third number: ')

if (arg1.isdigit() == False) or (arg2.isdigit() == False) or (arg3.isdigit() == False):
    print('ERROR: enter an integer/float number.')  # проверка вводимых символов на число
else:                                               # изменение типа введенных строк
    arg1 = int(arg1)
    arg2 = int(arg2)
    arg3 = int(arg3)

    def my_func (arg1, arg2, arg3):

        """
        Функция возвращает сумму наибольших из принятых аргументов

        """
        if arg1 >= arg3 and arg2 >= arg3:
            return arg1 + arg2
        elif arg1 >= arg2 and arg3 >= arg2:
            return arg1 + arg3
        else:
            return arg2 + arg3

    print(f"result: {my_func(arg1, arg2, arg3)}")