

import os
import pandas as pd

from ch06.exam_function import print_line

file_path = './data/seoul-metro-station-info.csv'
raw_data = pd.read_csv(file_path)

print_line()
print(raw_data.info())

print_line()
print(raw_data.head())

station_columns = ['station.code', 'geo.latitude', 'geo.longitude']


data_station = raw_data[station_columns]

print_line()
print(data_station.info())

print_line()
print(data_station.head())

data_station_index = data_station.set_index('station.code')

print_line()
print(data_station_index.info())

print_line()
print(data_station_index.head())

