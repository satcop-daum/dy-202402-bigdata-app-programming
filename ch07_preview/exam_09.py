import folium
import pandas as pd
from folium.plugins import HeatMap

from ch07_preview.ch07_function import save_csv, print_line

def get_station_data():
    data = pd.read_csv('./data/seoul-metro-2021.logs.csv')
    return data
#end-def

def get_station_code():
    station_data = pd.read_csv('./data/seoul-metro-station-info.csv')

    # 필요한 행만 추리기
    station_data = station_data[['station.code', 'geo.latitude', 'geo.longitude']]

    # 색인 변경하기 (스테이션 코드로)
    station_data = station_data.set_index('station.code')

    return station_data
#end-def

data_station = get_station_data()
print_line()
print(data_station.info())

print_line()
print(data_station['timestamp'])

data_morning = data_station[pd.to_datetime(data_station.timestamp).dt.hour < 9]
print_line()
print(data_morning)

data_evening = data_station[pd.to_datetime(data_station.timestamp).dt.hour >= 17]
print_line()
print(data_evening)

data_morning_sum = data_morning.groupby('station_code').sum()
data_evening_sum = data_evening.groupby('station_code').sum()

data_station_info = get_station_code()

data_morning_join = data_morning_sum.join(data_station_info)
data_evening_join = data_morning_sum.join(data_station_info)


columns_in = ['geo.latitude', 'geo.longitude', 'people_in']
columns_out = ['geo.latitude', 'geo.longitude', 'people_out']

def get_map():
    location = [37.55, 126.98]
    zoom_start = 12
    map = folium.Map(location=location, zoom_start=zoom_start)
    return map
#end-def

# 출근 시간 승차 인원
map_morning_in = get_map()
HeatMap(data = data_morning_join[columns_in]).add_to(map_morning_in)
# map_morning_in.show_in_browser()

# 출근 시간 하차 인원
morning_seoul_out = get_map()
HeatMap(data = data_morning_join[columns_out]).add_to(morning_seoul_out)
# morning_seoul_out.show_in_browser()

# 퇴근 시간 승차 인원
map_evening_in = get_map()
HeatMap(data = data_evening_join[columns_in]).add_to(map_evening_in)
# map_evening_in.show_in_browser()

# 퇴근 시간 하차 인원
map_evening_out = get_map()
HeatMap(data = data_evening_join[columns_out]).add_to(map_evening_out)
map_evening_out.show_in_browser()

