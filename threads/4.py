"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""
import threading
import os
import time
def replace_ids(filemane):
    with open(filemane, "r") as f:
        text = f.read()
    text = text.replace('ids', 'id')
    with open(filemane, 'w') as f:
        f.write(text)

stat_time = time.time()
path_folder = 'files/'
files = os.listdir(path_folder)
threads = []

for file in files:
    path_folder = os.path.join(path_folder, file)
    t = threading.Thread(target=replace_ids, args=(path_folder))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
end = time.time()
print(stat_time - end)
