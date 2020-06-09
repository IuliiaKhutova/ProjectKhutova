# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Technic():
    def __init__(self,weight,price,color):
        self.weight = weight
        self.color = color
        self.price = price

class Warehouse():
    def __init__(self):
        pass

class Printer(Technic):
    def __init__(self,multifunction,print_speed):
        self.multifunction = multifunction
        self.print_speed = print_speed

class Scaner(Technic):
    def __init__(self,scan_technology,slide_scan):
        self.scan_technology = scan_technology
        self.slide_scan = slide_scan

class Xerox(Technic):
    def __init__(self,type):
        self.type = type
