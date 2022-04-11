'''
    1. Реализовать класс «Дата», функция-конструктор которого должна
     принимать дату в виде строки формата «день-месяц-год». В рамках
     реализовать два метода. Первый, с декоратором @classmethod. Он
     должен извлекать число, месяц, год и преобразовывать их тип к
     типу «Число». Второй, с декоратором @staticmethod, должен проводить
     валидацию числа, месяца и года (например, месяц — от 1 до 12).
     Проверить работу полученной структуры на реальных данных.
'''


class Data:
    def __init__(self, str_data):
        self.str_data = str(str_data)

    @classmethod
    def changed_str(cls, day_month_year):
        new_list = []
        count = 0
        while count < 3:
            for i in day_month_year.split():
                if i != '-':
                    new_list.append(i)
                    # подсчитываем количество знаков '-'. Если их
                    # будет < 2 или > 2, то выводим ошибку. Т.к.
                    # стандарт ввода dd-mm-yy
                if i == '-':
                    count += 1
            if (count > 2) or (count < 2):
                print('Enter valid data dd-mm-yy.')
                break
            else:
                return int(new_list[0]), int(new_list[1]), int(new_list[2])

    @staticmethod
    def correct_data(day, month, year):
        # проверяем диапазон значений дня
        if (day <= 0) or (day > 31):
            return f'Enter a correct day.'
        # проверяем диапазон значений месяца
        elif (month < 1) or (month > 12):
            return f'Enter a correct month.'
        # проверяем правильность введенного года - 2022
        elif year != 2022:
            return f'Enter a correct year.'
        # отдельная проверка на февраль
        elif (month == 2) and (day > 28):
            return f'Fab has only 28 days.'
        # отдельная проверка на месяцы с 30 днями
        elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
            return f'This month has only 30 days.'
        else:
            return ''

    def __str__(self):
        return f'Текущая дата {Data.changed_str(self.str_data)}'

'''
    Именованные переменные:
    today -- правильный вид даты dd-mm-yy
    today_incorrect -- введенно больше знаков '-'
'''
today = Data('13 - 11 - 2022')
today_incorrect = Data('13 - 12 - 1 - 2022')
print(f"first output: {today}")
print(f'second output: {today_incorrect} \n')

# проверка на правильность введенных данных
print(Data.correct_data(31, 11, 2022))
print(today.correct_data(31, -12, 2022))
print(f"{today.correct_data(31, 0, 2022)} \n")

# проверка декоратора @classmethod
print(Data.changed_str('31 - 12 - 2010'))
print(today.changed_str('31 - 12 - 2022'))