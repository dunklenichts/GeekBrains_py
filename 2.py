'''
    2. Реализовать класс Road (дорога).
    - определить атрибуты: length (длина), width (ширина);
    - значения атрибутов должны передаваться при создании
      экземпляра класса;
    - атрибуты сделать защищёнными;
    - определить метод расчёта массы асфальта, необходимого
      для покрытия всей дороги;
    - использовать формулу: длина*ширина*масса асфальта для
      покрытия одного кв. метра дороги асфальтом, толщиной
      в 1 см*число см толщины полотна;
    - проверить работу метода.
'''
class Road():
    def __init__(self, road_lenght, road_width, thickness):
        self._road_lenght = road_lenght
        self._road_width = road_width
        self.thickness = thickness

    '''
        Именованные переменные:
        road_lenght -- длина дороги
        road_width -- ее ширина
        thickness -- толщина полотна
    '''
    # вычисляем массу асфальта
    def mass_calc(self):
        a = self._road_width * self._road_lenght * 25 * self.thickness
        return a

c = Road(20, 5000, 5)
print(f"{(c.mass_calc()/1000):.0f} т")