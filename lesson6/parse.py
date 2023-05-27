import requests
from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/')
print(response.content)
soup = BeautifulSoup(response.content, "html.parser")


for post in soup.select('.quote'):
    print(post.text.strip())

