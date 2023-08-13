import requests
import psycopg2
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}



connection = psycopg2.connect(
    host='ep-empty-sea-524845.eu-central-1.aws.neon.tech',
    port='5432',
    database='neondb',
    user='op663246',
    password='5ELlvIaWx3JK'
)
cursor = connection.cursor()






response = requests.get('https://comfy.ua/ua/cherkasy/smartfon/brand__apple/', headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser")

container = soup.select_one("div.products-catalog")













def database(item):
    try:
        connection = psycopg2.connect(
            host='ep-empty-sea-524845.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='op663246',
            password='5ELlvIaWx3JK'
        )
        
        cursor = connection.cursor()
        
        query = "INSERT INTO devices(name, code, old_price, current_price, reviews) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (item['name'], item['code'], item['old_price'], item['current_price'], item['reviews']))

        
        connection.commit()
        
        
        cursor.close()
        connection.close()
        
    except Exception as e:
        print('Виникла помилка при вході в систему:', e)





for product in container.select(".products-list-item"):
    item = {
        "name": product.select_one("a.products-list-item__name").text,
        "code": product.select_one("a.products-list-item__code.dsk").text.strip().replace('Код:', '').replace(".", "").replace(' ', ''),
        "old_price": product.select_one('div.products-list-item__actions-price-old').text[:20].replace('\n', '').replace('₴', '').replace(' ', '').strip(),
        "current_price": product.select_one("div.products-list-item__actions-price-current").text.replace('\n', '').replace('₴', '').replace(' ', '').strip(),
        "reviews": product.select_one("a.products-list-item__reviews.icon-comfy").text.strip()
    }
    
    database(item)
    print(item)