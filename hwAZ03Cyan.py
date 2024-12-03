from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv
import matplotlib.pyplot as plt
import numpy as np
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
# URL страницы
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
driver.get(url)
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")
#for price in prices:
#    print(price.text)
def clean_price(price):
    # Удаляем "₽/мес." и преобразуем в число
    return int(price.replace(' ₽/мес.', '').replace(' ', ''))
pr = []
for price in prices:
    price_text = clean_price(price.text)
    #price_text = price.text.replace('₽', '').replace(' ', '')  # Убираем символы валюты и пробелы
    if price_text.is_integer():  # Проверяем, что цена состоит только из цифр
       pr.append(int(price_text))

    # Вычисляем среднюю цену
if pr:
    average_price = sum(pr) / len(pr)
    print(f'Средняя цена: {average_price:.2f} ₽')
else:
    print('Цены не найдены.')

# Построение гистограммы
plt.hist(pr, bins=20, edgecolor='black')
plt.title('Гистограмма цен')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.grid(axis='y', alpha=0.75)
plt.axvline(average_price, color='red', linestyle='dashed', linewidth=1, label='Средняя цена')
plt.legend()
plt.show()

# Закрытие драйвера
driver.quit()




