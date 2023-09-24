"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки. И создаем папку по указанному пути.
"""
import sys
import os

if len(sys.argv) < 3:
    print("Добавьте аргументы")
else:
    data = sys.argv[1]
    folder_name = sys.argv[2]

    folder_path = os.path.join(data, folder_name)

    try:
        os.makedirs(folder_path)
        print(f"Папка {folder_name} создана по пути {data}")
    except FileExistsError:
        print(f"Папка {folder_name} существует по пути {data}")
    except Exception as i:
        print(f"Произошла ошибка при создании папки: {i}")