'''
    3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
    Решите задание в одну строку.
'''

my_list = [element for element in range(20, 241) if element % 20 == 0 or element % 21 == 0]
print(my_list)