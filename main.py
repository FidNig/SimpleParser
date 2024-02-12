from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from image_parser import fetch_and_save_images
import requests
import shutil
import time
import os

# Assuming you've updated the ChromeDriver
chromedriver_path = "D:\\ChromeDriver\\chromedriver.exe" # Ensure this path is correct and matches the updated ChromeDriver location

# No change needed in the URL and images_dir setup

# Настройка WebDriver
service = Service(executable_path=chromedriver_path)
options = Options()
options.add_argument("--disable-gpu")  # Отключить использование GPU
options.add_argument('--headless')  # Запуск в фоновом режиме
driver = webdriver.Chrome(service=service, options=options)


# URL веб-страницы для парсинга
url = "https://www.metta.ru/catalog/samurai_home_and_office/samurai_l1_1k_ts_985972/"

# Создание директории для сохранения изображений
images_dir = "downloaded_images"
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

try:
    # Открытие страницы
    driver.get(url)

    # Ожидание для полной загрузки страницы
    driver.implicitly_wait(10)

    # Здесь вам нужно заменить 'By.CLASS_NAME, "full-name-value_svg"' на правильный селектор кнопки.
    # Например, если у кнопки есть уникальный класс, id, или вы можете использовать XPath.
    # Использование WebDriverWait и expected_conditions для ожидания элемента
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "full-name-value_svg"))
    )
    button.click()

    # После нажатия кнопки, дождитесь нужных изменений на странице
    time.sleep(10)  # Пример ожидания, возможно, потребуется адаптировать

    # Теперь можно продолжить с парсингом страницы
    page_source = driver.page_source

    driver.quit()

finally:
    # Закрытие браузера
    driver.quit()

# Использование BeautifulSoup для парсинга полученного HTML
soup = BeautifulSoup(page_source, 'html.parser')

# Поиск всех элементов с классом 'manual__description_item_stroke_title'
titles = soup.find_all('div', class_='manual__description_item_stroke_title')

# Поиск всех элементов с классом 'manual__description_item_stroke_desc'
descriptions = soup.find_all('div', class_='manual__description_item_stroke_desc')

# Проверка, найдены ли элементы и их количество совпадает
if titles and descriptions and len(titles) == len(descriptions):
    # Вывод заголовков таблицы
    print(f"{'Title'.ljust(50)} | {'Description'}")
    print('-' * 100)  # Разделительная линия для визуального разделения заголовка и тела таблицы

    # Перебор и вывод элементов
    for title, desc in zip(titles, descriptions):
        print(f"{title.text.ljust(50)} | {desc.text}")
else:
    print("Элементы не найдены или их количество не совпадает.")

fetch_and_save_images()