# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма).
#
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC,abstractmethod
class ClothesAbstract(ABC):
    def __init__(self):
       pass
    @abstractmethod
    def ClothConsumption(self) -> int:
        pass


class Coat(ClothesAbstract):
    def __init__(self,size):
        self.__size = size

    def ClothConsumption(self):
        cloth_cons = round(self.__size / 6.5 + 0.5)
        return cloth_cons
        pass
    @property
    def size(self):
        return self.__size

class Suit(ClothesAbstract):
    def __init__(self, height):
        self.__height = height

    def ClothConsumption(self):
        cloth_cons = round(2 * self.__height + 0.3)
        return cloth_cons

    @property
    def height(self):
        return self.__height

if __name__ == "__main__":

    suit = Suit(100)
    print(suit.ClothConsumption())
    coat = Coat(200)
    print(coat.ClothConsumption())
    print(coat.size)
    print(suit.height)
    # общий подсчет
    print(suit.ClothConsumption()+coat.ClothConsumption())