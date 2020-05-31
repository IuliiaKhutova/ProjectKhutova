# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open("les5-5.txt", "w", encoding="utf-8") as my_file:
    my_file.write("6 5 7 8 9 1")

with open("les5-5.txt", "r", encoding="utf-8") as my_file:
    content = (my_file.read()).split()
    print(content)
    sum=0
    for el in content:
        sum = sum+float(el)
    print(sum)


