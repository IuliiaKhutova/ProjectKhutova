# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar.
#
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self,speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f"Машина {self.name} поехала")
    def stop(self):
        print(f"Машина {self.name} остановилась")
    def turn(self,direction):
        print(f"Машина {self.name} повернула в {direction}")
    def show_speed(self,speed):
        print(f'внимание! на спидометре машины {self.name}: {speed} км')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed>60:
            print(f'скорость машины {self.name} превышена на {self.speed-60} км')
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    # print("Это спортивная машина {self.name}")
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            print(f'скорость машины {self.name} превышена на {self.speed - 40} км')
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)
    # print("Это полицейская машина {self.name}")

police = PoliceCar(60, "черная", "Ауди")
police.go()
work =WorkCar(90, "синяя", "BMW", False)
work.stop()
work.show_speed()
sport = SportCar(160, "синяя", "BMW", False)
sport.turn("лево")
town = TownCar(88, "красный", "Мини", False)
town.show_speed()

