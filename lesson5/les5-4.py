# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


def my_prog(file_name,new_file_name):
    rus_list = ["Один", "Два", "Три", "Четыре"]
    rus_list_final = []
    i=0
    with open(file_name,"r",encoding="utf-8") as my_file:
        for line in my_file:
            new_line = line.split("—")
            new_line[0] = rus_list[i]
            i+=1
            final_line = " -".join(new_line)
            rus_list_final.append(final_line)
    with open(new_file_name,"w",encoding="utf-8") as my_new_file:
        my_new_file.writelines(rus_list_final)

my_prog("file5-4","new_file")



