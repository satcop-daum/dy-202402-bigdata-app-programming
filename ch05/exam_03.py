import pandas as pd
import matplotlib.pyplot as plt

from ch05.exam_02_common import get_covid_data as get_covid


korea_index_df = get_covid('South Korea')
print('=' * 50)
print(korea_index_df.head())


usa_index_df = get_covid('United States')
print('=' * 50)
print(usa_index_df.head())


korea_total_cases_series = korea_index_df['total_cases']
usa_total_cases_series = usa_index_df['total_cases']
data_index = korea_index_df.index

print('=' * 50)
print(data_index)

df = pd.DataFrame(
    {
            'KOR': korea_total_cases_series,
            'USA': usa_total_cases_series
        },
    index=data_index)
df.plot.line(rot = 45)

plt.show()
