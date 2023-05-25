import pandas as pd 

products = pd.read_excel('C:\Python_1y_15_22\lessons\semester II\lesson2\Product for cake (1).xlsx')
print(products)

data = pd.read_excel('C:\Python_1y_15_22\lessons\semester II\lesson2\Product for cake (1).xlsx', usecols=['Name products', 'Price']) 
print(data)


df = pd.read_excel('C:\Python_1y_15_22\lessons\semester II\lesson2\Product for cake (1).xlsx')
total_mass = df['Mass(g)'].sum()
print('Сума стовпчика Mass(g) дорівнює', total_mass, 'грам')



total_price = df['Price'].sum()
print('Суму яку затрачено на приготування торта дорівнює', total_price, 'грн')

