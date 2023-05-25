
# import pandas as pd
from googletrans import Translator




# for trans in a:
#     print(f'{trans.origin} -> {trans.text}')

# print(a.text)



# file = open('lessons\semester II\lesson3\info.txt', 'w')
# file.write('Hello World!\n')
# file.write('My name is Oleh.\n')
# file.write('I am 14.\n')

# file = open('lessons\semester II\lesson3\info.txt', 'r')
# text = file.read()
# print('Origin text:\n', text)

translator = Translator()

# to_translate = translator.translate(text, dest='uk')
# print('Translate text:\n', to_translate.text)


# data = pd.read_excel('lessons\semester II\lesson3\Електронна таблиця без назви.xlsx')
# print(data)



# to_translate = translator.translate(text=data, src='en', dest='uk')
# print(to_translate.text)

# products = ['Water', 'Milk', 'Melon', 'Apples']
# price = [15, 50, 200, 60]
# data = pd.DataFrame(list(zip(products, price)), columns=['Products', 'Price'])
# data.to_excel('lessons\semester II\lesson3\groceries.xlsx', index=None)

# with pd.ExcelWriter('lessons\semester II\lesson3\groceries.xlsx') as writer:
#     data.to_excel(writer, sheet_name='groceries1', index=None)
#     data.to_excel(writer, sheet_name='groceries2', index=None)




