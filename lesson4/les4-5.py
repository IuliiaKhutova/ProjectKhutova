# 5. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
#     Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при
# достижении числа 10 завершаем цикл. Во втором также необходимо
# предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle

def iter():
    while True:
        try:
            start = int(input("введите первое число последовательности\n"))
            stop = int(input("введите последнее число последовательности\n"))
            break
        except ValueError:
            print("введите целое число")
    for el in count(start):
        print(el)
        if el == stop:
            break

iter()

list = [43, "dgdg" ,342, 3432, 8]
def cycle_list():
    y=0
    for i in cycle(list):
        print(i)
        if y == 10:
            break
        y +=1

cycle_list()
