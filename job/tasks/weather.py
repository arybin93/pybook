import requests
from bs4 import BeautifulSoup
import datetime
import time

print("Start parse")

i = 0
while i < 5:
    URL = "https://yandex.ru/pogoda/nizhny-novgorod?lat=56.312531799999995&lon=44.0702779&from=home"

    r = requests.get(URL)

    soup = BeautifulSoup(r.text, "html.parser")

    bc_span = soup.find("div", class_='temp fact__temp').find("span", class_="temp__value")

    date = datetime.datetime.now()
    date_str = date.strftime("%Y-%m-%d %H:%M")

    with open("weather.txt", "a+", encoding="utf-8") as f:
        f.write(bc_span.text + " , " + date_str + "\n")

    print(bc_span.text)
    time.sleep(5)
    i += 1

print("end parse")