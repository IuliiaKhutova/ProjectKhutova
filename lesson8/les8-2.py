# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.
#
class MyException(Exception):
    def __init__(self, text):
        self.text = text

def division(a, b):
    try:
        if b==0:
            raise MyException("деление на 0 не поддерживается")
        else:
            return a / b
    except MyException as error:
        return error


print(division(6,3))
print(division(6,0))
