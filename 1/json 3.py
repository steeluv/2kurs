"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: [
{
name:***
time:***
cities:***
}
]
"""
import json

task = ["oleg",24,["Belarus","Russia"],(24,1),["Moscow","Vladikavkaz",'Krasnodar',"Rostov","Nalchik"]]

data = {'name': task[0],
        'age': task[1],
        'countries:': [{'name': task[2],
                        'time': task[3],
                        'cities': task[4]}]}

with open('steeluv1.json', 'w') as new_file:

    json.dump(data, new_file, indent=4)