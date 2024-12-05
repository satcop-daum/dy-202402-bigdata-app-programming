import os
from datetime import datetime
from random import sample

import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt
from ch09_preview.ch09_function import save_csv, print_line


url = '../ch09_preview/csv/data_20241106_011840.csv'
sample_table = pd.read_csv(url)

print_line()
print(sample_table)

print_line()

table_columns = {'날짜': 'date',
           '종가': 'end_price',
           '시가': 'start_price',
           '고가': 'highest_price',
           '저가': 'lowest_price'
           }

sample_table.rename(columns=table_columns, inplace=True)

print_line()
print(sample_table)

sample_table.drop(['전일비', '거래량'], axis=1, inplace=True)

print_line()
print(sample_table)


sample_table['date_value'] = pd.to_datetime(sample_table['date'])
print_line()
print(sample_table)

sample_table = sample_table[sample_table['date_value'] >= '2024-10-01']






sample_table['midian_price'] = sample_table['highest_price'] - ((sample_table['highest_price'] - sample_table['lowest_price']) / 2)

print_line()
print(sample_table)

sample_table['month'] = sample_table['date'].str[0:7]

print_line()
print(sample_table)

sample_table.set_index('date', inplace=True)
sample_table.sort_index(inplace=True)

print_line()
print(sample_table)


sample_table.plot.line()
plt.show()


sample_table[:15].plot.line()
plt.show()


sample_table.boxplot(column=['midian_price'], by=['month'])
plt.show()
