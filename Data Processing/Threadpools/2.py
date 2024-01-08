"""
Создайте функцию которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""

import queue
import threading

def number(num):
    numbers = []
    for i in range(1, num + 1):
        if num % i == 0:
            numbers.append(i)
    print(f" Делители от {num}: {numbers}")
def worker(q):
    while True:
        num = q.get()
        if num is None:
            break
        number(num)
        q.task_done()
def main():
    nums = [10,20,30,40,50]
    q = queue.Queue()
    for num in nums:
        q.put(num)
    num_workers = 5
    workers = []

    for _ in range(num_workers):
        t = threading.Thread(target=worker, args=(q,))
        t.start()
        workers.append(t)
    q.join()

    for _ in range(num_workers):
        q.put(None)
    for t in workers:
        t.join()
if __name__ == "__main__":
    main()


