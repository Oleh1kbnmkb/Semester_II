from bs4 import BeautifulSoup

with open('C:/Python_1y_15_22/lessons_semester II/lesson5/indexed.html') as file:
    soup = BeautifulSoup(file, 'html.parser')
    
for data in soup.select('.hobby, .passion'):
    print(data.text)

for data in soup.select('.future, .plans'):
    print(data.text)