# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

i = 0
while i < 1:
    try:
        x = int(input("введите число x\n"))
        y = int(input("введите число y\n"))
        i += 1
    except ValueError:
        print("ОШИБКА! В поле можно указать только число")
        continue

def my_func(x,y):
    return x**y

def my_func_complex(x,y):
    i=y
    result=1
    while i:
        result = result*x
        i=i-1
    return result

print(my_func(x,y),my_func_complex(x,y))
