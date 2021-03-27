# Реализуйте базовый класс Car:
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, name, color, speed, is_polise=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_polise = is_polise
        print(f'Машина: {self.name}(цвет {self.color}) машина полицеская - {self.is_polise}')

    def go(self):
        print(f'{self.name} : Машина поехала!')

    def stop(self):
        print(f'{self.name} : Машина остановилась!')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"направо" if direction == 0 else "налево"}.')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed} км/ч.'


class TownCar(Car):
    def show_speed(self):
        return f'{self.name}:Скорость автомобиля: {self.speed} км/ч. Обнаружен шумахер!' \
            if self.speed > 60 else f'{self.name}: Скорость автомобиля {self.speed} км/ч.'


class SportCar(Car):
    ''' Auto '''


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed} км/ч. Умерь пыл водила!' \
            if self.speed > 40 else f'{self.name}: Скорость автомобиля {self.speed} км/ч.'


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_polise=True):
        super().__init__(name, color, speed, is_polise)


tocar = TownCar('Семерка', 'бордовая', 58)
tocar.go()
tocar.turn(1)
print(tocar.show_speed())
tocar.turn(1)
tocar.stop()
print()

spocar = SportCar('Мерс', 'серый', 228)
spocar.go()
print(spocar.show_speed())
spocar.turn(1)
spocar.stop()
print()

worcar = WorkCar('Трактор', 'жёлтый', 44)
worcar.go()
print(worcar.show_speed())
worcar.turn(0)
worcar.stop()
print()

polcar = PoliceCar('Пазик', 'бело-синий', 67)
polcar.go()
polcar.turn(1)
print(polcar.show_speed())
polcar.turn(1)
polcar.turn(0)
polcar.turn(1)
polcar.stop()
print()
