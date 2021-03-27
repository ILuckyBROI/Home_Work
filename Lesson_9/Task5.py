# Реализовать класс Stationery (канцелярская принадлежность):
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    def __init__(self, title='Рисуем закрытыми глазами!'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки! {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Начало рисования, ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Начало рисования, ножкой {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Начало рисования, маркером {self.title}')


stat = Stationery()
stat.draw()
pen = Pen('Кисти')
pen.draw()
pencil = Pencil('Кэтбер')
pencil.draw()
marker = Handle('ВипВип')
marker.draw()
