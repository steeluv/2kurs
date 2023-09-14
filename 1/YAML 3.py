"""
Сохраните информацию из character.json в yaml файл(Имя файла - ваша фамилия)
"""
import json
import yaml
with open('character.json') as jsonfile:
    jsonfile = json.load(jsonfile)
with open("steeluv", "w") as yamlfile: