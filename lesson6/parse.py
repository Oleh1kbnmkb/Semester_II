import requests
from bs4 import BeautifulSoup

# response = requests.get('http://quotes.toscrape.com/')
# print(response.content)
# soup = BeautifulSoup(response.content, "html.parser")


# for post in soup.select('.quote'):
#     print(post.text.strip())



# response = requests.get('http://start.karazin.ua/page/dopushcheni#reiting')
# soup = BeautifulSoup(response.content, 'html.parser')


# with open('info.txt', 'w', encoding='utf - 8') as file:
#     for row in soup.select('.right-nav.table-cell.ic-evaluation > .item > a'):
#         a = f"{row.text} - {row.get('href')}\n"
#         file.write(a)


# response = requests.get('http://books.toscrape.com/')
# soup = BeautifulSoup(response.content, 'html.parser')


# with open('lessons_semester II\lesson6\info.txt', 'w') as file:
#     for row in soup.select('.product_pod > h3 > a'):
#         a = f"{row.text} - {row.get('href')}\n"
#         file.write(a)




response = requests.get('https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D1%96%D0%B2_%D1%81%D1%82%D0%B0%D0%BD%D1%83_HTTP')
soup = BeautifulSoup(response.content, 'html.parser')

for row in soup.select('.toclevel-1 > a'):
    a = f'{row.text.strip()}\n'
    print(a)