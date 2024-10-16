import matplotlib.pyplot as plt
import pandas as pd

file_path = '../ch04/data/owid-covid-data.csv'
raw_df = pd.read_csv(file_path)

selected_columns = ['iso_code', 'location', 'date', 'total_cases', 'population']
selected_df = raw_df[selected_columns]

# South Korea
south_korea_df = selected_df[selected_df.location == 'South Korea']

print('=' * 50)
print(south_korea_df.head())

south_korea_index_df = south_korea_df.set_index('date')

print('=' * 50)
print(south_korea_index_df.head())





kor_total_cases = south_korea_index_df['total_cases']
print('=' * 50)
print(kor_total_cases)


usa_index_df = selected_df[selected_df.location == 'United States'].set_index('date')
usa_total_cases = usa_index_df['total_cases']

print('=' * 50)
print(usa_total_cases)

print('=' * 50)
print(south_korea_index_df.index)



final_df = pd.DataFrame({
    'KOR': kor_total_cases,
    'USA': usa_total_cases
}, index=south_korea_index_df.index)

print('=' * 50)
print(final_df.head())


final_df.plot.line()
plt.show()


final_df['2022-01-01':].plot.line()
plt.show()
