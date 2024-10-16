
import pandas as pd
from ch07_preview.ch07_function import save_csv, print_line

data = pd.read_csv('./data/seoul-metro-2021.logs.csv')
print_line()
print(data)


columns = ['station_code', 'people_in', 'people_out']

data_columns = data[columns]
print_line()
print(data_columns)


station_sum = data_columns.groupby('station_code').sum()
print_line()
print(station_sum.info())


print_line()
save_csv(station_sum)
print(station_sum)
