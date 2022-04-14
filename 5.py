'''
    5. Создать (программно) текстовый файл, записать в него
    программно набор чисел, разделённых пробелами. Программа
    должна подсчитывать сумму чисел в файле и выводить её на экран.
'''
from functools import reduce
my_list = []

def summ_func (a, b):
    return a + b

with open("my_file5.txt", "w+") as f_obj:
        try:
            i = input("Enter numbers split ' ': ")
            f_obj.writelines(i)
            my_list = i.split()
            n = int(my_list[0])
            for element in range(1, len(my_list)):
                output = reduce(summ_func, [int(n), int(my_list[element])])
                n = output
            print(f'output = {output}')
        except ValueError:
            print('Enter integer numbs.')
        except NameError:
            print(n)