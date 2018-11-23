import requests
from bs4 import BeautifulSoup

import time

URL = 'https://yandex.ru/pogoda/nizhny-novgorod?from=serp_title'

print('Start parsing')

for i in range(10):
    r = requests.get(URL)

    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')

    div = soup.find('div', class_='temp fact__temp')
    span = div.find('span', class_='temp__value')
    temp = span.text

    f = open('temp.txt', 'a+', encoding='utf-8')
    f.write(temp + '\n')
    f.close()

    time.sleep(5)

# arybin93@gmail.com

print('End parsing')