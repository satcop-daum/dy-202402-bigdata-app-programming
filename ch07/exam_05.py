

import os
import pandas as pd
from folium import folium
from folium.plugins import HeatMap

from ch06.exam_function import print_line

def get_station_info():
    file_path = './data/seoul-metro-station-info.csv'
    raw_data = pd.read_csv(file_path)

    columns_info = ['station.code', 'geo.latitude', 'geo.longitude']
    data_columns = raw_data[columns_info]

    data_columns_index = data_columns.set_index('station.code')

    return data_columns_index
#end-def

def get_station_log():
    file_path_log = './data/seoul-metro-2021.logs.csv'
    raw_log_data = pd.read_csv(file_path_log)

    columns_log = ['station_code', 'people_in', 'people_out']

    data_columns = raw_log_data[columns_log]

    data_columns_sum = data_columns.groupby('station_code').sum()

    return data_columns_sum
#end-def

data_info = get_station_info()
data_log = get_station_log()

print_line()
print(data_info.head())

print_line()
print(data_log.head())


data_join = data_log.join(data_info)

print_line()
print(data_join.info())

print_line()
print(data_join.head())

station_in_columns = ['geo.latitude', 'geo.longitude', 'people_in']
station_out_columns = ['geo.latitude', 'geo.longitude', 'people_out']

data_station_in = data_join[station_in_columns] 
data_station_out = data_join[station_out_columns]

station_map = folium.Map(location=(37.55, 126.98), zoom_start=15)

# HeatMap(data=data_station_in).add_to(station_map)
HeatMap(data=data_station_out).add_to(station_map)

station_map.show_in_browser()












