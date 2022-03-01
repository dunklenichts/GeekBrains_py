# 2. Пользователь вводит время в секундах. 
#    Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. 
#    Используйте форматирование строк.

time = int(input('Enter time in seconds: '))
if time < 0:
    print('ERROR')
else:
    minutes = time // 60
    hours = minutes // 60
    minutes = minutes % 60
    seconds = time - hours * 3600 - minutes * 60
    print(f"{hours} hrs {minutes} min {seconds} sec")
