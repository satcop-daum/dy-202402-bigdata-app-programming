import folium
import pandas as pd
from folium.plugins import HeatMap

from ch07_preview.ch07_function import save_csv, print_line


def get_station_sum():
    data = pd.read_csv('./data/seoul-metro-2021.logs.csv')
    columns = ['station_code', 'people_in', 'people_out']
    data_columns = data[columns]
    station_sum = data_columns.groupby('station_code').sum()
    return station_sum
#end-def

def get_station_code():
    station_data = pd.read_csv('./data/seoul-metro-station-info.csv')

    # 필요한 행만 추리기
    station_data = station_data[['station.code', 'geo.latitude', 'geo.longitude']]

    # 색인 변경하기 (스테이션 코드로)
    station_data = station_data.set_index('station.code')

    return station_data
#end-def

station_sum = get_station_sum()
station_code = get_station_code()
data_station_join = station_sum.join(station_code)

print_line()
print(data_station_join)


seoul_map = folium.Map(location= [37.55, 126.98], zoom_start=12)

# columns_in = ['geo.latitude', 'geo.longitude', 'people_in']
# HeatMap(data=data_station_join[columns_in]).add_to(seoul_map)


columns_out = ['geo.latitude', 'geo.longitude', 'people_out']
HeatMap(data=data_station_join[columns_out]).add_to(seoul_map)



seoul_map.show_in_browser()











