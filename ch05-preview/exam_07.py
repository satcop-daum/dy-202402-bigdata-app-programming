import matplotlib.pyplot as plt
import pandas as pd

from exam_06_common import get_index_df

south_korea_index_df = get_index_df('South Korea')
usa_index_df = get_index_df('United States')

south_korea_population = south_korea_index_df['population']['2022-01-01']
usa_population = usa_index_df['population']['2022-01-01']


print(f'대한민국인구: {south_korea_population:,} / 미국인구: {usa_population:,}')

# population_rate = round(usa_population / south_korea_population, 2)
population_rate = usa_population / south_korea_population

print(f'{population_rate:.2f}')


kor_total_cases = south_korea_index_df['total_cases']
usa_total_cases = usa_index_df['total_cases']

print(type(kor_total_cases))

final_df = pd.DataFrame({
    'KOR': kor_total_cases,
    'USA': usa_total_cases
}, index=south_korea_index_df.index)
final_df['2022-01-01':].plot.line()
plt.show()

final_df2 = pd.DataFrame({
    'KOR': kor_total_cases * population_rate,
    'USA': usa_total_cases
}, index=south_korea_index_df.index)
final_df2['2022-01-01':].plot.line()
plt.show()












