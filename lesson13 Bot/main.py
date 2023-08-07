import sqlite3


def create_table(name, password):
  connection = sqlite3.connect('currency.db')
  cursor = connection.cursor()
  cursor.execute("""CREATE TABLE IF NOT EXISTS {name} (
      id INTEGER PRIMARY KEY,
      name VARCHAR NOT NULL,
      symbol VARCHAR NOT NULL,
      price FLOAT NOT NULL
  )""")
  connection.commit()
  connection.close()


# import sqlite3
# import requests
# from bs4 import BeautifulSoup as bs


# def create_table():
#     connection = sqlite3.connect('database.db')
#     cursor = connection.cursor()
#     cursor.execute("""CREATE TABLE IF NOT EXISTS cur
#                       (id INTEGER PRIMARY KEY, name VARCHAR NOT NULL, symbol VARCHAR NOT NULL, price FLOAT NOT NULL);""")
#     connection.commit()
#     connection.close()
# def add_data(name, symbol, price):
#     connection = sqlite3.connect('database.db')
#     cursor = connection.cursor()
#     cursor.execute("""INSERT INTO cur (name, symbol, price) VALUES (?, ?, ?);""", (name, symbol, price))
#     connection.commit()
#     connection.close()
# def get_data():
#     connection = sqlite3.connect('database.db')
#     cursor = connection.cursor()
#     cursor.execute("""SELECT * FROM cur;""")
#     data = cursor.fetchall()
#     connection.close()
#     return data
# URL_TEMPLATE = "https://privatbank.ua/ru/rates-archive"
# r = requests.get(URL_TEMPLATE)

# soup = bs(r.text, "html.parser")
# cur = soup.find_all('div', class_='purchase')
# curr = []
# for a in cur:
#     curr.append(float(a.span.text))

# add_data('euro', 'e', curr[0])
# add_data('dollar', '$', curr[1])
# add_data('pln', 'p', curr[2])
# print(get_data())
