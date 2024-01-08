import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep
import json

cookies = {
    'PHPSESSID': '641p1mij5f7kddgjfvav9rmg65',
    '51a55dae53577255b792d39bfe1d40ac': '1',
    '_ga_BB3QC8QLF4': 'GS1.1.1698057430.1.0.1698057430.0.0.0',
    '_ga': 'GA1.1.1635168952.1698057430',
    '_ym_uid': '1698057431933829630',
    '_ym_d': '1698057431',
    '_ym_isad': '2',
}

headers = {
    'authority': 'zaka-zaka.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=641p1mij5f7kddgjfvav9rmg65; 51a55dae53577255b792d39bfe1d40ac=1; _ga_BB3QC8QLF4=GS1.1.1698057430.1.0.1698057430.0.0.0; _ga=GA1.1.1635168952.1698057430; _ym_uid=1698057431933829630; _ym_d=1698057431; _ym_isad=2',
    'referer': 'https://jazz.sber.ru/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.967 YaBrowser/23.9.1.967 Yowser/2.5 Safari/537.36',
}
result = {}
for i in range(1,15):
    print("Собираю данные со старницы: " + str(i))
    sleep(0.7)
    response = requests.get('https://zaka-zaka.com/game/new/page' + str(i), cookies=cookies, headers=headers)
    with open("page.html", "w",encoding="utf-8") as f:
        f.write(response.text)
    with open("page.html", "r",encoding="utf-8") as file:

        soup = BeautifulSoup(file.read(), "lxml")
        container = soup.find("div",class_ ="tab-items list2")
        cards = container.find_all("a",class_="game-block")
        for card in cards:
            name = card.find("div",class_="game-block-name").text
            price = card.find("div",class_="game-block-price").text
            print(name)
            print(price)
            result[name] = (price)
print(result)

with open("zakazaka.json","w") as f:
    json.dump(result, f, indent=4,ensure_ascii = False)
