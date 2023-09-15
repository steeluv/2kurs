"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""
import csv
dict = {}

with open('Task1.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for i in reader:
        dict[(i[0], i[1])] = {i[2] : i[3]}
    print(dict)