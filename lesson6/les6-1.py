# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами
# должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
from time import sleep
class TrafficLight:

    def __init__(self,__color):
        self.color = __color
    def change_color(self,newcolor):
        self.color = newcolor
        print(self.color)
    def running(self,max_count):
        count=1
        while count<=max_count:
            sleep(7)
            self.change_color("yellow")
            sleep(2)
            self.change_color("green")
            sleep(7)
            self.change_color("red")
            count+=1

Traffic = TrafficLight("red")
Traffic.running(2)



