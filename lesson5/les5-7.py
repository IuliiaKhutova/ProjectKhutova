# 7. Создать (не программно) текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

import json
sum_profit = 0
count=0
dict = {}
dict_avg = {}

with open("les5-7", "r", encoding="utf-8") as my_file:
    for line in my_file.readlines():
        profit = float(line.split()[2])-float(line.split()[3])
        if profit >= 0:
            print(f'прибыль компании {line.split()[0]} составила {profit} рублей')
            sum_profit = sum_profit + profit
            count=count+1
        else:
            print(f'убыток компании {line.split()[0]} составила {profit} рублей')
        profit_avg = (sum_profit/(count)).__round__(2)
        dict[line.split()[0]] = profit
    dict_avg["average_profit"] = profit_avg
    print(f'средняя прибыль по всем безубыточным компаниям составила {profit_avg} рублей')
print(dict,dict_avg)

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
dict_list = [dict,dict_avg]
with open("dict.json","w",encoding="utf-8") as my_dict:
    json.dump(dict_list,my_dict,ensure_ascii=False)
