"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""

import queue
import threading

student_queue = queue.Queue()
def add_students():
    while True:
        surname = input("Введите фамилию студента / либо 'off' для завершения: ")
        if surname == 'off':
            break
        student_queue.put(surname)
def remove_students():
    while not student_queue.empty():
        surname = student_queue.get()
        print("Студент с фамилией:",surname,"отчислен")

add_thread = threading.Thread(target=add_students)
add_thread.start()
add_thread.join()

remove_thread = threading.Thread(target=remove_students)
remove_thread.start()
remove_thread.join()
