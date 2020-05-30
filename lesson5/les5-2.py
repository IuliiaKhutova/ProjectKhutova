# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
import os
file_path = os.path.join(os.path.dirname(__file__), 'file5-2')

with open(file_path,"r", encoding='utf-8') as my_file:
    count=0
    for line in my_file:
        line_list = line.split()
        print(f'количество слов в строке {count+1}: {len(line_list)}')
        count = count + 1
print(f'количество строк в файле: {count}')


