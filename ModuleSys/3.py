"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
"""
import sys
if len(sys.argv) < 3:
    print("Добавьте аргументы")
else:
    file1 = sys.argv[1]
    file_name = sys.argv[2]
    with open(file_name, 'w') as file:
        file.write(file1)
    print(file_name)
