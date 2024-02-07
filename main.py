from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Указывайте ваш путь к ChromeDriver
chromedriver_path = "D:\ChromeDriver\chromedriver.exe"

# URL веб-страницы для парсинга
url = "https://www.metta.ru/catalog/samurai_home_and_office/samurai_l1_1k_ts_985972/"

# Настройка WebDriver
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

try:
    # Открытие страницы
    driver.get(url)

    # Ожидание для полной загрузки страницы
    time.sleep(10)  # Ожидаем, чтобы убедиться, что страница и динамические элементы полностью загружены

    # Получение исходного кода страницы
    page_source = driver.page_source
finally:
    # Закрытие браузера
    driver.quit()

# Использование BeautifulSoup для парсинга полученного HTML
soup = BeautifulSoup(page_source, 'html.parser')

# Поиск всех элементов с классом 'modal-content manual'
modal_contents = soup.find_all('div', class_='characteristics-detail-value')

# Проверка, найдены ли элементы
if modal_contents:
    for content in modal_contents:
        print(content.text)
else:
    print("Элементы с классом 'modal-content manual' не найдены.")
