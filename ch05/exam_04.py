import pandas as pd
import matplotlib.pyplot as plt

from ch05.exam_02_common import get_covid_data as get_covid


korea_index_df = get_covid('South Korea')
print('=' * 50)
print(korea_index_df.head())


usa_index_df = get_covid('United States')
print('=' * 50)
print(usa_index_df.head())


korea_population = korea_index_df['population']['2020-01-20']
usa_population = usa_index_df['population']['2020-01-20']

print('=' * 50)
print(f'대한민국 인구수: {korea_population:,} / 미국 인구수: {usa_population:,}')

polulation_rate = usa_population / korea_population

print('=' * 50)
print(f'인구비율: {polulation_rate}')


korea_total_cases_series = korea_index_df['total_cases']
usa_total_cases_series = usa_index_df['total_cases']
data_index = korea_index_df.index

df = pd.DataFrame(
    {
            'KOR': korea_total_cases_series * polulation_rate,
            'USA': usa_total_cases_series
        },
    index=data_index)
df['2022-01-01':'2023-12-31'].plot.line(rot = 45)

plt.show()

# print(df['2022-01-01':].head())









