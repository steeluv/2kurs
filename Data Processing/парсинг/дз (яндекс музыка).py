"""
Соберите данные с чартов яндекс музыки https://music.yandex.ru/chart
Внимательно изучитe источник, посvотрите как именно на сайт приходит информация.
{
место в чарте: (исполнитель,трек)
}
"""
import requests
from bs4 import BeautifulSoup
import json
import requests

cookies = {
    '_yasc': '6vFEY6BaqRu+KG14A0RbeRQIoIbspY0EWUMbbbAlzKy0yWfnw1b0IgQE/iawoTl5lQ+RlO4=',
    'i': 'BDf4Wc4XRtXGj2Nq5y8EhIp3PVoBVr9t7WDviko73OEvkzdhe5W1mfg7BIjCg9QsnqyTg9jmJS01V501tQuiOZ4b/SU=',
    'yandexuid': '9587072601697809724',
    'yuidss': '9587072601697809724',
    'ymex': '2013169727.yrts.1697809727',
    'yashr': '8280769581697809729',
    'device_id': 'bc750db43420eee8e693eb2b7b43645c522faee42',
    'active-browser-timestamp': '1697809728516',
    'gdpr': '0',
    '_ym_visorc': 'b',
    '_ym_uid': '1697809727980003890',
    '_ym_d': '1697809730',
    'is_gdpr': '0',
    'is_gdpr_b': 'CNC3LBCQ1QE=',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://music.yandex.ru/chart',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Origin': 'https://music.yandex.ru',
    'Connection': 'keep-alive',
    # 'Cookie': '_yasc=6vFEY6BaqRu+KG14A0RbeRQIoIbspY0EWUMbbbAlzKy0yWfnw1b0IgQE/iawoTl5lQ+RlO4=; i=BDf4Wc4XRtXGj2Nq5y8EhIp3PVoBVr9t7WDviko73OEvkzdhe5W1mfg7BIjCg9QsnqyTg9jmJS01V501tQuiOZ4b/SU=; yandexuid=9587072601697809724; yuidss=9587072601697809724; ymex=2013169727.yrts.1697809727; yashr=8280769581697809729; device_id=bc750db43420eee8e693eb2b7b43645c522faee42; active-browser-timestamp=1697809728516; gdpr=0; _ym_visorc=b; _ym_uid=1697809727980003890; _ym_d=1697809730; is_gdpr=0; is_gdpr_b=CNC3LBCQ1QE=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = '/reqid=1697809724773372-2563584621638726851/path=690.2096.361/slots=production/vars=143=28.56.2048,287=10995,-project=MusicWeb,-page=index,-env=production,-version=3.761.0,1042=Mozilla^%^2F5.0^%^20(Windows^%^20NT^%^2010.0^%^3B^%^20Win64^%^3B^%^20x64^%^3B^%^20rv^%^3A109.0)^%^20Gecko^%^2F20100101^%^20Firefox^%^2F118.0,d=music.yandex.ru-svg^!3^!2372;yandex.ru-^!2^!2321;,t=40524,-cdn=unknown/cts=1697809764560/*'

response = requests.post('https://yandex.ru/clck/click', cookies=cookies, headers=headers, data=data)
with open("page.html", "w", encoding="utf-8") as f:
    f.write(response.text)
with open("page.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file.read(), "lxml")
    print(soup.prettify())
    container = soup.find("div", class_="page-main__line page-main__line_chart")
    top = container.find("div", class_="d-track__chart-number typo deco-typo")
    songs = container.find("div", class_="d-track__name")
    singer = container.find("div", class_="d-track__meta")

print(f"Место в чарте:{top}{singer}{songs}")



