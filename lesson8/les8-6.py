
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Validation(Exception):
    def __init__(self,text):
        self.text = text
    @staticmethod
    def validate(digit):
        if not digit.isdigit():
            raise Validation("ошибка ввода. необходимо ввести число!")

class Technic():
    def __init__(self,type,quantity):
        self.type = type
        self.quantity = quantity
class Warehouse():
    def __init__(self):
        self.technic_type=""
        self.quantity=0
        self.arrival_dict ={}
        self.department_dict = {}
        self.tech=""
        self.operation=""
        self.depart=""
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
                    try:
                        Validation.validate(self.quantity)
                    except Validation as error:
                        print(error)
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
                        self.depart = input("укажите подразделение-получатель\n")
                        self.dep = str(product)+str(self.depart)
                        self.tech_taken()
    def tech_arrival(self):
        if self.tech in self.arrival_dict.keys():
                self.arrival_dict[self.tech] = int(self.arrival_dict[self.tech])+int(self.quantity)
                #если среди ключей словаря такой уже есть, то увеличим количество
        else:  #добавляем новую технику и количество в словарь (на склад)
            self.arrival_dict.update({self.tech:self.quantity})
        return print(f"текущий остаток на складе: {self.arrival_dict}")

    def tech_taken(self):

        if self.tech in self.arrival_dict.keys():
            if int(self.arrival_dict[self.tech]) >= int(self.quantity):
                self.arrival_dict[self.tech] = int(self.arrival_dict[self.tech]) - int(self.quantity)
            else:
                print(f"Не хватает для выдачи {int(self.quantity)-int(self.arrival_dict[self.tech])} штук")
        else:
            print("запрошенной техники нет в наличии на складе!")
        # добавляем новый словарь для учета в подразделении
        if self.dep in self.department_dict.keys():
            self.department_dict[self.dep] = int(self.department_dict[self.dep])+int(self.quantity)
        else:
            self.department_dict.update({self.dep: self.quantity})
        return print(f"текущий остаток на складе: {self.arrival_dict},хранится в подразделениях: {self.department_dict}")

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



