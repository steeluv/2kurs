"""
Создайте функцию которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию которая создает txt файл  по пути из очереди.
Запустите все в разных потоках.
"""
import queue
import os
from threading import Thread

def names_r(path_file, queue):
    with open(path_file, "r") as f:
        names = f.readlines()
        for name in names:
            name = name.strip()
            path_file = os.path.join('/steeluv', name + ".txt")
            queue.put(path_file)

def new_file(path_file):
    with open(path_file, "w") as f:
        f.write("vsem privetiki pistoletiki")

q = queue.Queue
th1 = Thread(target=names_r, args=("Names.txt", q))
th2 = Thread(target=new_file, args=(q.get()))
th1.start()
th2.start()
th1.join()
th2.join()
print('aa')