# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import datetime

class Date:
    @classmethod
    def digit_method(cls,date:str):
        my_date = str(date).split("-")
        print(my_date)
        date = int(my_date[0])
        month = int(my_date[1])
        year = int(my_date[2])
        return date,month,year

    @staticmethod
    def validate(day,month,year):
        if 1 <= year  and 1<=month <=12 and 1<=day <=31:
            return True
        else:
            return False

if __name__ =="__main__":

    day,month,year = Date.digit_method("12-13-1990")
    print(day,month,year)
    print(Date.validate(day,month,year))

