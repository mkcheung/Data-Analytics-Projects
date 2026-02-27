import pandas as pd
import numpy as np
from openpyxl import Workbook
import matplotlib.pyplot as plt

chipo = pd.read_csv('chipotle_fixed.csv')
# print(chipo)
# print(chipo.info())
items_and_payments = chipo[['item_name','quantity', 'choice_description', 'item_price']]
items_and_payments['item_price'] = items_and_payments['item_price'].apply(lambda x: float(str(x).strip().replace('$', '')) if pd.notna(x) else None )
items_and_payments['product_price'] = items_and_payments['item_price'] / items_and_payments['quantity'] 
items_and_payments = items_and_payments.drop_duplicates(subset='item_name', keep='first')
items_and_prices = items_and_payments[['item_name', 'choice_description', 'product_price']]
print('ITEMS AND PRICES:')
print(items_and_prices)

flag_items_over_ten_dollars = items_and_prices['product_price']>10.0
print(items_and_prices[flag_items_over_ten_dollars]['item_name'])
print(f"Number of Items costing more than $10: {items_and_prices[flag_items_over_ten_dollars]['item_name'].size}")

print("Purchases Sorted by Item:")
print(chipo.sort_values(['item_name'], ascending=[True]))
most_expensive_item_purchased = items_and_prices['product_price'] == items_and_prices['product_price'].max()
print(f"Quantity of Most Expensive Item Purchased: {items_and_payments[most_expensive_item_purchased]['quantity'].sum()}")

flag_veggie_bowl_purchases = items_and_prices['item_name'] == 'Veggie Salad Bowl'
print(f"Number of times a Veggie Salad Bowl was ordered: {len(items_and_payments[flag_veggie_bowl_purchases])}")

flag_ordered_soft_drink = (chipo['item_name'] == '6 Pack Soft Drink') & (chipo['quantity'] > 1)
# print(flag_ordered_soft_drink)
print(f"Number of times someone ordered more than one canned soda: {len(chipo[flag_ordered_soft_drink])}")

