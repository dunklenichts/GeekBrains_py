'''
    4. Реализуйте базовый класс Car.
    - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
      А также методы: go, stop, turn(direction), которые должны сообщать, что машина
      поехала, остановилась, повернула (куда);
    - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    - добавьте в базовый класс метод show_speed, который должен показывать текущую
      скорость автомобиля;
    - для классов TownCar и WorkCar переопределите метод show_speed. При значении
      скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
      превышении скорости.
    - Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
      к атрибутам, выведите результат. Вызовите методы и покажите результат.
'''
class Car():
    def __init__(self, name, color, speed, is_police):
        self.color = color
        self.name = name
        self.speed = speed
        self.is_police = is_police

    # методы, отображающие характер движения машины
    def car_go(self):
        return 'went'
    def car_stop(self):
        return 'stopped'
    def car_TurnLeft(self):
        return 'turned left'
    def car_TurnRight(self):
        return 'turned right'
    def car_TurnBack(self):
        return 'turned back'

    # метод для отображения скорости движения машины
    def show_speed(self):
        return f'speed is {self.speed}'

class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    # если скорость городской машины > 60, то выводится сообщение
    # о превышении скорости в черте города
    def show_speed(self):
        if self.speed > 60:
            return f'Overspeed {self.speed} for town'
        else:
            return f'Speed is {self.speed}'

class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    # если скорость городской машины > 40, то выводится сообщение
    # о превышении скорости для рабочей машины
    def show_speed(self):
        if self.speed > 40:
            return f'Overspeed {self.speed} for work car'
        else:
            return f'Speed is {self.speed}'

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    # метод, показывающий принадлежность машины к полиции
    def police_car(self):
        if self.is_police == True:
            print(f"{self.name} is a police car")
        else:
            print(f"{self.name} isn't a police car")

# проверка работы методов на вывод информации о машинах и их скорости
a = TownCar('nissan', 'black', 60, False)
print(f"\ntown car name: {a.name}, color: {a.color}, speed: {a.speed}is police: {a.is_police}")
print(a.show_speed())

b = SportCar('Audi', 'black', 100, False)
print(f"\nsport car name: {b.name}, color: {b.color}, speed: {b.speed}, is police: {b.is_police}")
print(b.show_speed())

c = WorkCar('mercedez', 'white', 41, False)
print(f"\nwork car name: {c.name}, color: {c.color}, speed: {c.speed}, is police: {c.is_police}")
print(c.show_speed())

d = PoliceCar('audi', 'white', 60, True)
print(f"\npolice car name: {d.name}, color: {d.color}, speed: {d.speed}, is police: {d.is_police}")
print(d.show_speed())

# проверка методов характера движения машины
print('\nDestination test:')
print(f"{a.name} {a.car_TurnLeft()} then {a.car_TurnRight()} and finally {a.car_stop()}")
print(f"{b.name} {a.car_TurnRight()} then {a.car_stop()} and finally {a.car_go()}")
print(f"{c.name} {a.car_TurnBack()} then {a.car_go()} and finally {a.car_TurnLeft()}")

# проверка полицейских машин
print('\nPolice test')
print(f"{a.color} {a.name} belongs to police dpt: {a.is_police}")
print(f"{c.color} {c.name} belongs to police dpt: {c.is_police}")
print(f"{d.color} {d.name} belongs to police dpt: {d.is_police}")