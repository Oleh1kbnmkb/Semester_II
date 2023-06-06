import requests
from bs4 import BeautifulSoup



response = requests.get('http://yermilovcentre.org/medias/')
soup = BeautifulSoup(response.content, 'html.parser')



for element in soup.select('.col-6.mx-0.no-gutters.row.mt-0.mt-n2 > a'):
  a = f"{element.text} - {element.get('href')}\n"
  print(a.strip())
