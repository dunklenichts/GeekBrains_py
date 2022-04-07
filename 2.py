'''
    2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь определённое
    название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
    одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут
    быть обычные числа: V и H, соответственно.

    Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом
    уроке знания: реализовать абстрактные классы для основных классов проекта, проверить
    на практике работу декоратора @property.
'''

class Clothes():

    def __init__(self, coat, height):
        self.coat = coat
        self.height = height

    @property
    def full_textil(self):
        return f'{(self.coat / 6.5 + 0.5) + (2 * self.height + 0.3)}'

    def __str__(self):
        return f'{(self.coat / 6.5 + 0.5) + (2 * self.height + 0.3):.2}'

class Coat(Clothes):
    def __init__(self, coat, height):
        super().__init__(coat, height)

    def __str__(self):
        return f"{(self.coat / 6.5 + 0.5):.2}"

class Costume(Clothes):
    def __init__(self, coat, height):
        super().__init__(coat, height)

    def __str__(self):
        return f"{(2 * self.height + 0.3):.2}"

mc = Clothes(2, 4)
print(f"Full amount of textil for both of clothes: {mc}")

coat = Coat(1, 2)
print(f"Full amount of textil for coat: {coat}")

costume = Costume(3, 4)
print(f"Full amount of textil for costume: {costume}")