from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import lxml
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options)
driver.get("https://www.aviasales.ru/")
search = driver.find_element(by = "xpath", value = "/html/body/div[7]/div[2]/div/div/div/div[2]/form/span/div[1]")
search.clear()
search.send_keys("Сочи")
search.send_keys(Keys.ENTER)
sleep(10)
search1 = driver.find_element(by = "xpath", value = "/html/body/div[7]/div[2]/div/div/div/div[2]/form/span/div[2]")
search1.send_keys("Минск")
search1.send_keys(Keys.ENTER)
button = driver.find_element(by='xpath', value="/html/body/div[7]/div[2]/div/div/div/div[2]/form/div[1]/div/button[1]")
button.click()
sleep(10)
button_16 = driver.find_element(by='xpath', value="/html/body/div[12]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[3]/div[4]")
button_16.click()
sleep(4)
button_no = driver.find_element(by='xpath', value="/html/body/div[12]/div/div/div/div/div[2]/div/div[3]")
button_no.click()
sleep(4)
button_tickets = driver.find_element(by='xpath', value="/html/body/div[7]/div[2]/div/div/div/div[2]/form/button")
button_tickets.click()
sleep(4)
# button = driver.find_element(by='xpath', value="/html/body/div[1]/div[7]/div[6]/form/div[1]/div/div[1]/div[3]/div/div[3]/a[1]")
# button.click()
for i in range(30):
    sleep(0.5)
    driver.execute_script("window.scrollBy(0, 1070)")
page = driver.page_source
print(page)
soup = BeautifulSoup(page, "lxml")
container = soup.find("div",class_="app__content")
list_of_tickets = container.find_all("section",class_="product-list__direct-schedule")
result = []
for ticket in list_of_tickets:
    name = ticket.find("div", class_="s__VWGMQkNvXAk6vfgXhnEX s__ShYzKW_6zESUNc6duu4d s__Z_M86eYiGhMPCOMX0AOT s__bv9SLJMgrhfHSZh5XYxL").text
    price = ticket.find("span", class_="s__wRhMOEwg2Ub7G1CotYcY")
    result.append(name,"-",price)
print("Вот список билетов, которые мы собрали",result)