'''
    4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
    Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите
    в порядке их следования в исходном списке. Для выполнения задания обязательно
    используйте генератор.
'''
import random

def generator (my_list):
    for element in my_list:
        yield element

my_list = [random.randint(1, 10) for element in range(10)]
# print(f'Input list: {my_list}')


# print(set(my_list))
my_list = sorted(my_list)
print(my_list)

new_list = []
n = my_list[0]
temp = []
out_list = []

for i in range(0, len(my_list)):
    if n != my_list[i]:
       new_list.append(my_list[i])
       #print(f'n1 = {n}')
       # i += 1
       print(f'i = {my_list[i]}')
       n = my_list[i + 1]
    elif n == my_list[i]:
        print(f'i2 = {my_list[i]}')
       #new_list.append('-')
        n = my_list[i]
       #temp.append(my_list[i])
       #i += 1

        #print(f'n2 = {n}')

print(f'output {new_list}')
#print(f'output2 {temp}')


#print(temp)