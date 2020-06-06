# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).

# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).

class Cell:
    # это количество ячеек в клетке, как я поняла
    def __init__(self,cell_quantity:int):
        self.cell_quantity = cell_quantity
    def __add__(self, other):
        # Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
        return self.cell_quantity+other.cell_quantity

    def __sub__(self, other):
        # Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
        # иначе выводить соответствующее сообщение.
        if self.cell_quantity-other.cell_quantity >0:
            return self.cell_quantity-other.cell_quantity
        else:
            print("разность меньше 0")
    def __mul__(self, other):
        # Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
        return self.cell_quantity*other.cell_quantity
    def __truediv__(self, other):
        # Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
        # В методе деления должно осуществляться округление значения до целого числа.
        return round(self.cell_quantity/other.cell_quantity,0)

    def make_order(self, quantity_in_row:int):
        # В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
        # Данный метод позволяет организовать ячейки по рядам.
        # Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
        # Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
        string = ""
        for i in range(int(self.cell_quantity // quantity_in_row)):
            string = string+ f'{"*" * quantity_in_row}\\n'
        string = string+ f'{"*" * (self.cell_quantity % quantity_in_row)}'
        return string

if __name__ =="__main__":
    cell=Cell(100)
    cell1=Cell(52)
    print(cell/cell1)
    print(cell + cell1)
    print(cell * cell1)
    print(cell-cell1)
    print(cell.make_order(33))
