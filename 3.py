'''
    3. Реализовать базовый класс Worker (работник).
    - определить атрибуты: name, surname, position (должность), income (доход);
    - последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
      элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
    - создать класс Position (должность) на базе класса Worker;
    - в классе Position реализовать методы получения полного имени сотрудника
      (get_full_name) и дохода с учётом премии (get_total_income);
    - проверить работу примера на реальных данных: создать экземпляры класса Position,
      передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''

class Worker():
    def __init__ (self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
'''
    Именованные переменные:
    name -- имя сотруднка
    surname -- его фамилия
    position -- занимаемая должность
    wage -- оклад
    bonus -- премия
'''
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    # получаем полное имя сотрудника
    def get_full_name (self):
        return self.name + ' ' + self.surname
    # выводим его оклад и премию как словарь
    def get_total_income (self):
        self._income = {"wage": self.wage, "bonus": self.bonus}
        return self._income

output = Position('Ivan', 'Ivanov', 'engineer', 100, 100)
print(f"Employee name's: {output.get_full_name()}\nHis income is {output.get_total_income()}")