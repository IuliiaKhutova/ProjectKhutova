# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.
while True:
    try:
        a = float(input('введите делимое\n'))
        b = float(input('введите делитель\n'))
        break
    except ValueError:
        print("вводимые данные должны быть числом!")
        continue

def division(a,b):
    try:
        x = a / b
    except ZeroDivisionError:
        x = "делить на 0 нельзя!"
    return x

print(division(a,b))