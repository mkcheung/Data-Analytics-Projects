import pandas as pd
import numpy as np
from openpyxl import Workbook
import matplotlib.pyplot as plt

users = pd.read_csv('users_fixed.csv', index_col='user_id')
# print(users.head(25))
# print(users.tail(10))
# print(users.shape)
# print(users.columns)
# print(users.index)
# print(users.info())
# print(users.describe())
# print(users.describe(include='all'))
# print(users['occupation'].describe())
# print(users['age'].value_counts())
print(f"Number of Occupations: {users['occupation'].nunique()}")
print(f"Mean Age of Users: {round(users['age'].mean())}")