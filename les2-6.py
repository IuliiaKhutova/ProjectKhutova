# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
products_dict={}
product_list=[]
num=1
while True:
    product_name = input("введите наименование товара\n")
    if not product_name:
        break
    else:
        while True:
            product_price = input("введите цену товара\n")
            if product_price.isdigit() and int(product_price) >0:
                product_price = int(product_price)
                break
        while True:
            product_quant = input("введите количество товара\n")
            if product_quant.isdigit() and int(product_quant) >0:
                product_quant = int(product_quant)
                break
        product_pce = input("введите единицу измерения\n")
        products_dict.update({"название":product_name,"цена":product_price,"количество":product_quant, "ед.изм":product_pce})
        product_list_el = (num, products_dict) #в цикле, пока пользователь вводит данные получаем элементы будущего списка и нумеруем
        product_list.append(product_list_el)  #добавляем каждый элемент в список
        num = num +1
        products_dict = {} #очищаем словарь, куда добавляли введенные значения (мы и так его записали в список), иначе будут затерты данные при след.подходе
print(product_list)
dict_no_num = []
numbers, dict_no_num = zip(*product_list)   #разложим список на элементы, чтобы убрать нумерацию.
temp_list = []   #в данный список буду помещать значения из каждого словаря
for dict_el in dict_no_num:
    values_list = list(dict_el.values())  #список значений по каждому имеющемуся словарю
    keys_list = list(dict_el.keys()) #список ключей для будущего итогового аналит.словаря
    temp_list.append(values_list) #временный список значений по всем словарям, которые потом нужно зипануть
values_zipped = list(zip(*temp_list))  #транспонируем список значений, чтобы они были сгруппированы
#теперь нужно добавить все в один словарь
analytics_dict_fi = dict(zip(keys_list,values_zipped))
print(analytics_dict_fi)






