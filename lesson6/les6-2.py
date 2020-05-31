# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться
# при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    def __init__(self,_length,_width):
        self.length = _length
        self.width = _width

class Asphalt(Road):
    def __init__(self,asp_weight_unit,thickness,*args):
        self.asp_weight_unit = asp_weight_unit
        self.thickness = thickness
        super().__init__(*args)

    def asp_weight_calc(self):
        asphalt_weight = self.length*self.width*self.asp_weight_unit*self.thickness
        print(asphalt_weight)

asp = Asphalt(25,5, 20,5000)
asp.asp_weight_calc()



