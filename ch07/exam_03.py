

import os
import pandas as pd

from ch06.exam_function import print_line

file_path = './data/seoul-metro-station-info.csv'
raw_data = pd.read_csv(file_path)

print(raw_data.head())
print(raw_data.info())

file_path_log = './data/seoul-metro-2021.logs.csv'
raw_log_data = pd.read_csv(file_path_log)

print(raw_log_data.head())


columns = ['station_code', 'people_in', 'people_out']

data_metro = raw_log_data[columns]

print_line()
print(data_metro.head())


data_metro_sum = data_metro.groupby('station_code').sum()

print_line()
print(data_metro_sum.info())

print_line()
print(data_metro_sum.head())


