# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
list = []
while True:
    string = input("введите строку\n")
    if not string:
        break
    list.append(string+"\n")
# print(list)
with open("my_new_file.txt", "w+", encoding='utf-8') as my_file:
        my_file.writelines(list)
        # переношу указатель в начало
        my_file.seek(0)
        for line in my_file:
            print(line)



