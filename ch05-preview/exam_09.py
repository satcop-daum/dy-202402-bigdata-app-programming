import matplotlib.pyplot as plt
import pandas as pd

from exam_06_common import get_index_df

file_path = '../ch04/data/hawaii-covid-data.csv'
raw_hawaii_df = pd.read_csv(file_path)

print(raw_hawaii_df.head())

print('=' * 50)
for index, row in raw_hawaii_df.iterrows():
    print(f"Row {index}:")
    print(row)
    print()  # 줄바꿈

print('=' * 50)
print(raw_hawaii_df.info())


filtered_hawaii_df = raw_hawaii_df[['submission_date', 'tot_cases']]

print('=' * 50)
print(filtered_hawaii_df.head())


sorted_hawaii_df = filtered_hawaii_df.sort_values(by='submission_date')
print('=' * 50)
print(filtered_hawaii_df.head())


sorted_hawaii_df['date'] = pd.to_datetime(filtered_hawaii_df['submission_date'])

print('=' * 50)
print(sorted_hawaii_df.head())


sorted_hawaii_df.sort_values(by='date', inplace=True)

print('=' * 50)
print(sorted_hawaii_df.head())

sorted_hawaii_df.set_index('date', inplace=True)

print('=' * 50)
print(sorted_hawaii_df.head())

hawaii_total_cases = sorted_hawaii_df['tot_cases']

print('=' * 50)
print(hawaii_total_cases)
print(type(hawaii_total_cases))













