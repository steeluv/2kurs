"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""
import multiprocessing

def squere(filename):
    length = int(input("Введите значение длины комнаты: "))
    height = int(input("Введите значение высоты комнаты: "))
    room = (length * height * 4) + "м^2"
    with open(filename, 'r+') as f:
        f.write(filename)

squere(filename)




def expenses(filename):
    result_filename = int(filename) / 5
    return result_filename

