"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""

import multiprocessing

def even_numbers(start, end):
    sum = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            sum += i
    return sum
def odd_numbers(start, end):
    sum = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            sum += i
    return sum
if __name__ == '__main__':
    start = 1
    end = 1000000
p1 = multiprocessing.Process(target=even_numbers, args=(start, end))
p2 = multiprocessing.Process(target=odd_numbers, args=(start, end))
p1.start()
p2.start()
p1.join()
p2.join()

