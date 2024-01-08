"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""
import requests
response = requests.get("https://randomuser.me/api/.").json()
user = response['result'][0]
name = user['name']['first']+ "" + user['name']['last']
country = user['location']['country']
phone = user['phone']
quote = f"hi, im {name}, Im from {country}, my phone number is {phone}"

print(quote)
