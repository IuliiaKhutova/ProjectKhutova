# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def numbers_sum(*args):
    result = 0
    for el in args:
        try:
            el = float(el)
            result = result + float(el)
        except ValueError:
            print("Ошибка! Строка не будет добавлена в результат! вводите ТОЛЬКО числа!!!!")
    return result

result_sum = 0
while True:
    numbers = input("введите числа через пробел\n").split()
    if "q" in numbers:
        numbers = numbers[:(numbers.index("q"))]
        result_sum = result_sum + numbers_sum(*numbers)
        break
    else:
        result_sum = result_sum + numbers_sum(*numbers)
print(result_sum)
