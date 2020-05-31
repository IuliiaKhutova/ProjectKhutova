# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
list = []
i=0
while i < 3:
    try:
       el = float(input("введите число\n"))
       list.append(el)
       i+=1
    except ValueError:
        print("ОШИБКА! В поле можно указать только число")
        continue
def my_func(*args):
    my_sum = sum(list) - min(list)
    return(my_sum)
print(my_func(*list))