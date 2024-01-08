"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""
import requests
def random():
    for i in range(2):
        randcat = requests.get('https://cataas.com/cat')
        with open(f"cat{i}.jpg", "wb") as f:
            f.write(randcat.content)
random()
def orig():
    images = ["https://cataas.com/cat/:tag", "https://cataas.com/cat"]
    for i, image_url in enumerate(images):
        randcat = requests.get(f"{image_url}")
        with open(f"cat{i}.jpg", "wb") as f:
            f.write(randcat.content)
orig()


