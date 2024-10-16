
import pandas as pd

data = pd.read_csv('./data/seoul-metro-2021.logs.csv')
print(data)


station_data = pd.read_csv('./data/seoul-metro-station-info.csv')
print(station_data)


print(data.info())
