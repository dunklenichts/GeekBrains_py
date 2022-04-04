'''
    5. Реализовать класс Stationery (канцелярская принадлежность).
    - определить в нём атрибут title (название) и метод draw (отрисовка).
      Метод выводит сообщение «Запуск отрисовки»;
    - создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    - в каждом классе реализовать переопределение метода draw.
      Для каждого класса метод должен выводить уникальное сообщение;
    - создать экземпляры классов и проверить, что выведет описанный метод для каждого
      экземпляра.
'''

class Stationery():
    def __init__(self, title):
        self.title = title
    # общий метод для отрисовки
    def draw(self):
        print('Drawing started')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    # переопределение метода
    def draw(self):
        return f"You're drawing with {self.title}"

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    # переопределение метода
    def draw(self):
        return f"You're drawing with {self.title}"

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    # переопределение метода
    def draw(self):
        return f"You're drawing with {self.title}"

# создание экземпляров класса
a = Pen('pen')
b = Pencil('pencil')
c = Handle('handle')
# проверка методов
print(a.draw())
print(b.draw())
print(c.draw())