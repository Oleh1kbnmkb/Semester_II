import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.select_one('.wikitable')
# print(table)
header = table.find('tr')
print(header)
cols = []
for i in header:
    col_title = i.text
    cols.append(col_title)

# print(cols)
cols = [item.strip() for item in cols]
col_name = [item for item in cols if item != '']
print(cols)
print(col_name)

new_table = pd.DataFrame(columns=col_name)
rows = table.find_all('tr')
# print(rows)
for row in rows[1:]:
    cel = row.find_all('td')
    table_row = [item.text for item in cel]
    l = len(new_table)
    new_table.loc[l] = table_row
    # print(table_row)



with pd.ExcelWriter('data_types.xlsx') as writer:
    new_table.to_excel(writer, index=False)