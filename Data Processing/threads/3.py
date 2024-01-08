"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""

import time
from threading import Thread

def beautybomb():
    while True:

        code = int("030506")
        your_code = int(input("Введите код:\n "))
        if code == your_code:
            print("Бомба реанимированна")
        else:
            print("Вы взорвались((((((")

bobm = Thread(target=beautybomb)
bobm.start()
time.sleep(3)
print('ВВОДИТЕ БЫСТРЕЕЕЕЕ!!!!!')


