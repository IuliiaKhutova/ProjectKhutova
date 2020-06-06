# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv
script_name, production, rate, bonus = argv

def salary(production, rate, bonus):
    salary = float(production)*float(rate)+float(bonus)
    return salary

print(salary(production, rate, bonus))