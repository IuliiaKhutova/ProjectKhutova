# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

class Technic():
    def __init__(self,type,quantity):
        self.type = type
        self.quantity = quantity
class Warehouse():
    def __init__(self):
        self.technic_type = ""
        self.quantity = 0
        self.arrival_dict = {}
        self.tech =""
        self.operation =""
    def operate(self):
        while True:
            self.operation = input("введите тип операции: arrive или take. Для завершения введите stop\n")
            # вводим параметры техники, которые будем получать или отдавать
            if self.operation == "stop":
                break
            elif self.operation!= "arrive" and self.operation!="take":
                print("укажите верное название операции\n")
                continue
            elif self.operation == "arrive" or self.operation=="take":
                while True:
                    self.technic_type = input("введите тип техники\n")
                    if self.technic_type == "stop":
                        break
                    self.quantity = input("введите количество\n")
                    if self.technic_type == "printer":
                        product = Printer(input("принтер МФУ?\n"), input("введите скорость печати принтера\n"))
                    elif self.technic_type == "scaner":
                        product = Scaner(input("введите технологию сканирования\n"),
                                         input("поддерживается ли сканирование слайдов?\n"))
                    elif self.technic_type == "xerox":
                        product = Xerox(input("введите тип ксерокса\n"))
                    else:
                        print("укажите верное название товара\n")
                        continue
                    self.tech = str(product)  # преобразуем объект с его аттрибутами в строку
                    if self.operation == "arrive":
                        self.tech_arrival()
                    elif self.operation == "take":
                        self.tech_taken()
    def tech_arrival(self):
        if self.tech in self.arrival_dict.keys():
                self.arrival_dict[self.tech] = int(self.arrival_dict[self.tech])+int(self.quantity)
                #если среди ключей словаря такой уже есть, то увеличим количество
        else:  #добавляем новую технику и количество в словарь (на склад)
            self.arrival_dict.update({self.tech:self.quantity})
        return (f"текущий остаток на складе: {self.arrival_dict}")

    def tech_taken(self):
        if self.tech in self.arrival_dict.keys():
            if int(self.arrival_dict[self.tech]) >= int(self.quantity):
                self.arrival_dict[self.tech] = int(self.arrival_dict[self.tech]) - int(self.quantity)
            else:
                print(f"Не хватает для выдачи {int(self.quantity)-int(self.arrival_dict[self.tech])} штук")
            # если среди ключей словаря такой уже есть, то увеличим количество
        else:  # добавляем новую технику и количество в словарь (на склад)
            print("запрошенной техники нет в наличии на складе!")
        return (f"текущий остаток на складе: {self.arrival_dict}")

class Printer(Technic):
    def __init__(self,multifunction,print_speed):
        self.multifunction = multifunction
        self.print_speed = print_speed

    def __str__(self):
        return str(f"printer, возможности МФУ {self.multifunction}, Скорость печати {self.print_speed}")

class Scaner(Technic):
    def __init__(self,scan_technology,slide_scan):
        self.scan_technology = scan_technology
        self.slide_scan = slide_scan

    def __str__(self):
        return str(f"сканер, технология сканирования {self.scan_technology}, сканирование слайдов: {self.slide_scan}")

class Xerox(Technic):
    def __init__(self,type):
        self.type = type
    def __str__(self):
        return str(f"ксерокс, тип ксерокса {self.type}")

if __name__ =="__main__":
    warehouse = Warehouse()
    warehouse.operate()



