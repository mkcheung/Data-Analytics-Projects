import pandas as pd
import numpy as np
from openpyxl import Workbook
import matplotlib.pyplot as plt

euro12 = pd.read_csv('team_stats_clean_numeric.csv')
print(euro12['Goals'])
print(f'How many teams participate in the Euro 2012? - {euro12.shape[0]}')
print(f"How many columns are in the dataset? - {euro12.shape[1]}")

discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False))

print(f"Average number of Yellow Cards per Team: {euro12['Yellow Cards'].mean()}")

print("Teams having scored more than six goals:")
print(euro12[euro12['Goals']>6])

print("Teams that start with G:")
print(euro12[euro12['Team'].str.startswith("G", na=False)])

print("First Seven Columns:")
pd.set_option('display.max_columns', 7)
print(euro12.iloc[:, 0:7])

print('Shooting Accuracy from England, England, Italy and Russia')
print(euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']])
