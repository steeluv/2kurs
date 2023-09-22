"""
Сохраните информацию из character.json в yaml файл(Имя файла - ваша фамилия)
"""
import json
import yaml

with open('character.json') as json_file:
    json_reader = json.load(json_file)

with open("enikeeva", "w") as yaml_file:
    yaml.dump(json_reader, yaml_file)
