from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome('C:\LearnPython\chromedriver.exe')
driver.get("https://www.fxclub.org/markets/crypto/bitcoin/")

try:
    bitcoin_el = EC.visibility_of_element_located((By.CLASS_NAME, "fx-live-quotes-status fx-live-quotes"))
    WebDriverWait(driver, 15).until(bitcoin_el)
except TimeoutException:
    pass

html = driver.page_source
driver.close()

soup = BeautifulSoup(html, "html.parser")

bitcoin = soup.find("div", class_="fx-live-quotes-status fx-live-quotes").find_all('span')[1]
course_str = bitcoin.text.replace(',', '')
course = float(course_str)
print(course)
