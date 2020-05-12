#1 вывод переменных числовых и текстовых на экран
name = input('введите пожалуйста имя\n')
city = input('введите город проживания\n')
weight = input('введите свой вес\n')
age = input('введите возраст\n')
print('Hello',name,'твой вес:', weight,'уезжай обратно в город:', city,'и неважно, что тебе всего',age)
#2 перевод в часы мин и секунды
while True:
    timesec = input('введите время в секундах\n')
    if timesec.isdigit():
        timesec=int(timesec)
        break
    else:
        print('введите число!')
hours = int(timesec/60)
minutes = int((timesec-hours*60)/60)
seconds = timesec-hours*60-minutes*60*60
print(('Точное время: {} часов {} минут {} секунд').format(hours,minutes,seconds))
#3 сумма чисел n, nn, nnn
while True:
    digit = input('введите произвольное число\n')
    if digit.isdigit():
        break
    else:
        print('введите число!')
digit_sum = int(digit)+int(digit+digit)+int(digit+digit+digit)
print(digit_sum)
#4 самая большая цифра в числе
while True:
    positive_digit = input('введите целое положительное число\n')
    if positive_digit.isdigit() and int(positive_digit)>0:
        break
    else:
        print('число должно быть целым и положительным!')
i=len(positive_digit)-1
list=[]
while i>=0:
    digit = positive_digit[i]
    list.append(digit)
    i-=1
i=len(positive_digit)-1
probably_max = list[i]
while i>=0:
    if list[i - 1]>probably_max:
        probably_max = list[i - 1]
        i -= 1
    else:
        i -= 1
        continue
print(probably_max)
#5 рентабельность фирмы
while True:
    revenue = input('введите доход фирмы\n')
    costs = input('введите издержки фирмы\n')
    if revenue.isdigit() and costs.isdigit():
        revenue = float(revenue)
        costs = float(costs)
        break
    else:
        print('Введите число!')
if revenue > costs:
    profit = revenue-costs
    profit_margin = profit /revenue*100
    print('Успех! Фирма в прибыли! Прибыль составила {} руб.'.format(profit))
    while True:
        staff_quantity = input('введите численность сотрудников\n')
        if staff_quantity.isdigit() and int(staff_quantity)>0:
            staff_quantity = int (staff_quantity)
            profit_per_unit = profit / staff_quantity
            print('Рентабельность фирмы: {} руб., прибыль на человека составила {} руб.'.format(profit_margin,profit_per_unit))
            break
        else:
            print('введите целое число!')
else:
        loss = costs - revenue
        print('Печаль...У фирмы убытки! Убыток составил {} руб.'.format(loss))
#6 Задача про спортсмена
while True:
    distance = input('Сколько км Вы пробежали в 1-й день?\n')
    max_distance = input('Какого результата в км хотите достигнуть?\n')
    if distance.isdigit() and max_distance.isdigit():
        distance = float(distance)
        max_distance = float(max_distance)
        break
    else:
        print('введите число!')
day = 1
while distance < max_distance:
    distance = distance*1.1
    day +=1
distance = int(distance)
print('На {}-й день спортсмен достиг результата — не менее {} км'.format(day, max_distance))