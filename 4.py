# 4. Пользователь вводит целое положительное число. 
#    Найдите самую большую цифру в числе. 
#     Для решения используйте цикл while и арифметические операции.

n = input('Enter a number')
if n.isdigit() == False:
    print('Enter an integer number')
elif n.isdigit():
        n = int(n)
        max = n % 10
        n = n // 10
        while n > 0:
            # print(f"max first = {max}")
            # print(f"n1 = {n}, elif = {n%10}")
            if ((n % 10) >= max):
                max = n % 10
                n = n // 10
                # print(f"max = {max}")
            elif ((n % 10) < max):
                n = n // 10
                # print(f"n = {n}")
            else:
                break
        print(f"The highest number is {max}")
