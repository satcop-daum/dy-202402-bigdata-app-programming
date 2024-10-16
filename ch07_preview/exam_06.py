
import pandas as pd
from ch07_preview.ch07_function import save_csv, print_line

station_data = pd.read_csv('./data/seoul-metro-station-info.csv')
print_line()
print(station_data)


print_line()
print(station_data.info())


# 필요한 행만 추리기
station_data = station_data[['station.code', 'geo.latitude', 'geo.longitude']]

print_line()
print(station_data)

# 색인 변경하기 (스테이션 코드로)
station_data = station_data.set_index('station.code')

# 데이터 확인하기
print_line()
print(station_data)



