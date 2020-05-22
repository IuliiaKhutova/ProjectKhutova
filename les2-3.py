# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
seasons_list = ("зима", "весна", "лето", "осень")
seasons_dict = {9:"осень",10:"осень",11:"осень",12:"зима",1:"зима", 2:"зима",3:"весна",4:"весна",5:"весна",6:"лето",7:"лето", 8:"лето"}
while True:
    month = input('Введите целое число от 1 до 12\n')
    if month.isdigit():
        if int(month) >=1 and int(month) <=12:
            month = int(month)
            break
for i,y in enumerate(seasons_list):
    my_month = i*3+1
    if abs(my_month-month) <=1:
        break
    else:
        i = 0
print(seasons_list[i])

for key_dict, val_dict in seasons_dict.items():
    if month == key_dict:
        break
print(seasons_dict[key_dict])

