"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""

dict_scv = [['math', 'Igor Borisovicth', 9],
               ['TCP/IP', 'Golovin', 10000],
               ['new predmeti', 'all', 7],
               ['proggaa', 'Babchenok Oleg Yurievich ', 8]]

import csv

with open('steeluv.csv', 'w') as f:
    writer = csv.writer(f)
    for i in dict_scv:
        writer.writerow(i)