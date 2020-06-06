# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

newlist=list()
while True:
    list_el = input('Вводите последовательно элементы списка, нажимая Enter.\n Чтобы закончить не вводите ничего и нажмите Enter\n')
    if not list_el:
        break
    else:
        newlist.append(list_el)
print(newlist)
quant = len(newlist)
i=0
while i <= quant-2:
    newlist[(i)], newlist[(i +1)] = newlist[(i +1)], newlist[(i)]
    i=i+2
print(newlist)







