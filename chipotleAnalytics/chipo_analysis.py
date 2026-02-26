import pandas as pd
import numpy as np
from openpyxl import Workbook
import matplotlib.pyplot as plt

chipo = pd.read_csv('chipotle_fixed.csv')

# first 10 entries
# first_ten_entries = chipo.head(10)
# chipo_shape = chipo.shape # 4622 rows
# chipo_info = chipo.info()
# print('FIRST TEN OBSERVATIONS:')
# print(first_ten_entries)
# print('Overall Structure:')
# print(chipo_shape)
# print('Chipo Dataset Structure:')
# print(chipo_info)
# print('Names of Dataset Columns:')
# print(chipo.columns)
# print('Dataset Index:')
# print(chipo.index)
# # Which was the most-ordered item?
item_quantity_ordered = chipo.groupby(['item_name'])['quantity'].sum().sort_values(ascending = False)
# print(item_quantity_ordered)
print(f'Most Purchased Item: Chicken Bowl - {item_quantity_ordered.index[0]}')

choice_desc_tallied = chipo['choice_description'].value_counts().index[0]
# Most common choice description
print(f'Most Purchased Item - Choice Description: {choice_desc_tallied}')
# How many items ordered total? 
print(f"Items ordered in total: {chipo['quantity'].sum()}")
# chipo['item_price'] = chipo['item_price'].astype(str).str.replace(r'[$,]', '', regex=True).astype(float)
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(str(x).replace('$', '').strip()) if pd.notna(x) else None )
chipo['total_purchased'] = chipo['item_price'] * chipo['quantity']
# print(chipo['item_price'].dtype)
# chipo['price'] = chipo['price'].
print(f"Total Revenue: ${chipo['total_purchased'].sum()}")
print(f"Number of Orders: {chipo.sort_values(['order_id'], ascending=False).iloc[0]['order_id']}")
print(f"Number Of Unique Items Sold: {chipo['item_name'].nunique()}")