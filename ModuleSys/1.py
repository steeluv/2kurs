"""
Напишите скрипт который выводит надпись "Привет мир" если не было передано никаких аргументов.
Если 1 из аргументов "--name" то следующий аргумент должен быть имя. В таком случае выведите надпись "Привет {Имя}"
Пример ввода: python file.py kakoitoArgument --name Oleg(Скрипт должен напечатать привет Oleg)
"""

import sys

if len(sys.argv) == 1:
    print('Привет мир!!!!')
elif "--name" in sys.argv:
    name_in = sys.argv.index('name') + 1
    if name_in < len(sys.argv):
        name1 = sys.argv[name_in]
        print(f"Привет {name1}")
    else:
        print('Введи имяяя')
else:
    print('давай сначала')