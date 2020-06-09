# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
import os
file_path = os.path.join(os.path.dirname(__file__), 'file5-3')


import json
list_surname = []
list_salary = []
list = []
while True:
    surname = input("введите Фамилию\n")
    if not surname:
        print("до свидания!")
        break
    try:
        salary = float(input("введите оклад\n"))
    except ValueError:
        print("Оклад должен быть числом!")
    list_surname.append(surname)
    list_salary.append(salary)
    complex_list = dict(zip(list_surname,list_salary))

empolees_file = open(file_path, "w", encoding="utf-8")
with open("mu_file.json", "w"):
    json.dump(complex_list,empolees_file,sort_keys = True,indent=0,ensure_ascii=False)

# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
income = 0
for key, val in complex_list.items():
    if val < 20000:
        print(f"у сотрудника {key} оклад меньше 20 000 руб")
    income = income+ val
print(f"средний доход составляет {income /len(complex_list)}")

