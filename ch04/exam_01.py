
import pandas as pd

file_path = './data/owid-covid-data.csv'
raw_df = pd.read_csv(file_path)

# print(type(file_path))
# print(type(df))
print(raw_df)

# pd.show_versions()
print('=' * 50)
print(raw_df.info())

print('=' * 50)
print(raw_df.head())

selected_columns = ['iso_code', 'location', 'date', 'total_cases', 'population']

selected_df = raw_df[selected_columns]

print('=' * 50)
print(selected_df.head())


locations = selected_df['location']
print('=' * 50)
print(locations)

print('=' * 50)
#print(locations.unique())
locations_unique = locations.unique()
print(type(locations_unique))

print('=' * 50)
for location in locations_unique:
    print(location)

# South Korea
south_korea_df = selected_df[selected_df.location == 'South Korea']

print('=' * 50)
print(south_korea_df.head())

south_korea_index_df = south_korea_df.set_index('date')

print('=' * 50)
print(south_korea_index_df.head())

# United States
# usa_df = selected_df[selected_df.location == 'United States']
# usa_index_df = usa_df.set_index('date')
usa_index_df = selected_df[selected_df.location == 'United States'].set_index('date')

print('=' * 50)
print(usa_index_df.head())

print('=' * 50)
for index, row in south_korea_index_df.iterrows():
    print(row)





















