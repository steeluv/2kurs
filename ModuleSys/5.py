"""
Напишите скрипт который в качестве параметра из командной строки принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""
import sys

if len(sys.argv) < 2:
    print("Укажите имя файла.")
else:
    file_name = sys.argv[1]
    try:
        with open(file_name, 'r') as file:
            commands = file.readlines()
        for command in commands:
            exec(command)
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
    except Exception as i:
        print(f"Произошла ошибка при выполнении команд: {i}")