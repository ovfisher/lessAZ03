from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
# URL страницы
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
# Открытие страницы
driver.get(url)
# Ждем ... загрузилась
time.sleep(5)
prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")
#price_elements = driver.find_elements(By.XPATH, '//span[@data-mark="price"]')
#prices = [price.text for price in price_elements]
#prices = driver.find_elements(By.XPATH, '//div[@data-name="PriceInfo"]//span[@data-mark="MainPrice"]/span')

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()