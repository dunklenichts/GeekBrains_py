"""
    Программа запрашивает у пользователя строку чисел,
    разделённых пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить
    ввод чисел, разделённых пробелом и снова нажать Enter.
    Сумма вновь введённых чисел будет добавляться к уже
    подсчитанной сумме.
    Но если вместо числа вводится специальный символ, выполнение
    программы завершается. Если специальный символ введён после
    нескольких чисел, то вначале нужно добавить сумму этих чисел
    к полученной ранее сумме и после этого завершить программу.
"""
def summ():
    ext = False
    res_sum = 0
    res_sum2 = 0
    while ext == False:
        str_num = input('Enter numbers or Q to quit programm: ').split()
        for element in range(len(str_num)):
            if (str_num[element] == 'Q') or (str_num[element] == 'q'):
                ext == True
                break
            else:
                res_sum = res_sum + int(str_num[element])
        res_sum2 = res_sum + res_sum2
    print(res_sum2)