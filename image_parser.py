# PDF_parser.py

import requests
from bs4 import BeautifulSoup

def fetch_and_save_images():
    url = 'https://www.metta.ru/catalog/samurai_home_and_office/samurai_l1_1k_ts_985972/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img', {'itemprop': 'image', 'class': 'product-slide-image'})

    if img_tags:
        for idx, img_tag in enumerate(img_tags, start=1):
            img_src = img_tag['src']
            if not img_src.startswith(('http:', 'https:')):
                img_src = f'https://www.metta.ru{img_src}'
            img_response = requests.get(img_src)
            if img_response.status_code == 200:
                with open(f'image_{idx}.jpg', 'wb') as f:
                    f.write(img_response.content)
                print(f"Изображение {idx} успешно сохранено.")
            else:
                print(f"Не удалось скачать изображение {idx}.")
    else:
        print("Не удалось найти изображения на странице.")
