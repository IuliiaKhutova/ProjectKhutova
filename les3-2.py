# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

values_list = []
keys_list = []
template = {
    "имя пользователя": ("имя", str),
    "фамилия пользователя": ("фамилия", str),
    "город рождения": ("город, где родился", str),
    "город проживания": ("город, где живешь", str),
    "email": ("эл почта", int),
    "телефон": ("тел", str),
}
for key, val in template.items():
    value = input(f'{val[0]}\n')
    try:
        val[1](value)
    except:
        ValueError
        continue
    values_list.append(value)
    keys_list.append(key)
personal_data = dict(zip(keys_list,values_list))

def my_func(**kwargs):
    string =""
    for key, val in kwargs.items():
        x= key+" : "+val +" "
        x= str(x)
        string =  string + x
    result = print(string)
    return result
my_func(**personal_data)

