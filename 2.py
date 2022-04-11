'''
    2. Создайте собственный класс-исключение, обрабатывающий ситуацию
    деления на ноль. Проверьте его работу на данных, вводимых пользователем.
    При вводе нуля в качестве делителя программа должна корректно обработать
    эту ситуацию и не завершиться с ошибкой.
'''

class Exception:
    '''
        Именованные переменные:
        divisor -- делимое
        dividend -- делитель
    '''
    def __init__(self, divisor, dividend):
        self.divisor = divisor
        self.dividend = dividend

    @staticmethod
    def null_exception (divisor, dividend):
        try:
            return divisor / dividend
        except:
            return f'ERROR'

mc = Exception(1, 2)
# пример работы с правильными параментрами
print(f'{Exception.null_exception(1, 3):.2}')
print(f'{Exception.null_exception(1, -3):.2}')
print(f'{Exception.null_exception(1, 0.2):.2}')

# пример работы с делением на 0
print(Exception.null_exception(100, 0))
print(mc.null_exception(100, 0))