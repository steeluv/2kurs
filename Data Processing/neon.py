from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import lxml
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options)
driver.get("https://store.steampowered.com/")
search = driver.find_element(by = "id", value = "store_nav_search_term")
search.send_keys("Стратегии")
search.send_keys(Keys.ENTER)
sleep(1)
# button = driver.find_element(by='xpath', value="/html/body/div[1]/div[7]/div[6]/form/div[1]/div/div[1]/div[3]/div/div[3]/a[1]")
# button.click()
for i in range(10):
    sleep(0.5)
    driver.execute_script("window.scrollBy(0, 1070)")
page = driver.page_source
print(page)
soup = BeautifulSoup(page, "lxml")
conttainer = soup.find("div",id="search_resultsRows")
list_of_games = conttainer.find_all("div",class_="responsive_search_name_combined")
result = []
for game in list_of_games:
    name = game.find("span", class_="title").text
    result.append(name)
print("Вот список игр собрали",len(result))
print("Вот список игр, которые мы собрали",result)
