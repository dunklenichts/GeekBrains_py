'''
    1. Создать класс TrafficLight (светофор).
    - определить у него один атрибут color (цвет) и метод running (запуск);
    - атрибут реализовать как приватный;
    - в рамках метода реализовать переключение светофора в режимы:
      красный, жёлтый, зелёный;
    - продолжительность первого состояния (красный) составляет
      7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
    - переключение между режимами должно осуществляться только в указанном
      порядке (красный, жёлтый, зелёный);
    - проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
from time import sleep

class TrafficLight:
    __traffic_color = ['red', 'yellow', 'green']

    def traffic_running(self):
        element = 0
        while element <= 2:
            print(f"Traffic light color's {TrafficLight.__traffic_color[element]}")
            if element == 0:    # красный
                sleep(7)
            if element == 1:    # желтый
                sleep(2)
            if element == 2:    # зеленый
                sleep(10)
            element += 1

a = TrafficLight()
a.traffic_running()
