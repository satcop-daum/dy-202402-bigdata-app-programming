import pandas as pd
import matplotlib.pyplot as plt

from ch05.exam_02_common import get_covid_data as get_covid

raw_hawaii_df = pd.read_csv('./book_data/hawaii-covid-data.csv')

print('=' * 50)
print(raw_hawaii_df.head())

print('=' * 50)
print(raw_hawaii_df.info())

columns = ['submission_date', 'tot_cases']
filtered_hawaii_df = raw_hawaii_df[columns]

print('=' * 50)
print(filtered_hawaii_df.head())

# 데이터 정렬
sorted_hawaii_df = filtered_hawaii_df.sort_values(by='submission_date')

print('=' * 50)
print(sorted_hawaii_df.head())

sorted_hawaii_df['date'] = pd.to_datetime(sorted_hawaii_df['submission_date'])

print('=' * 50)
print(sorted_hawaii_df.info())

sorted_hawaii_df.sort_values(by='date', inplace=True)
sorted_hawaii_df.set_index('date', inplace=True)
# data_index = sorted_hawaii_df.index

print('=' * 50)
print(sorted_hawaii_df.head())

hawaii_total_cases_series = sorted_hawaii_df['tot_cases']

korea_index_df = get_covid('South Korea')
korea_total_cases_series = korea_index_df['total_cases']

print('=' * 50)
print(korea_total_cases_series)
print('=' * 50)
print(hawaii_total_cases_series)
print('=' * 50)
print(sorted_hawaii_df.info())

korea_population = korea_index_df['population']['2022-01-01']
hawaii_population = 1_440_196

print('=' * 50)
print(f'대한민국 인구수: {korea_population:,} / 하와이 인구수: {hawaii_population:,}')

population_rate = korea_population / hawaii_population
print(f'인구 비율: {population_rate}')

korea_total_cases_series.index = korea_total_cases_series.index.astype('string')
hawaii_total_cases_series.index = hawaii_total_cases_series.index.astype('string')
data_index = korea_total_cases_series.index

print('=' * 50)
print(korea_total_cases_series.index.dtype)
print(hawaii_total_cases_series.index.dtype)

final_df = pd.DataFrame(
    {
            'KOR': korea_total_cases_series,
            'HAWAII': hawaii_total_cases_series * population_rate
        },
    index=data_index)
final_df['2021-01-01':].plot.line(rot = 45)

plt.show()
