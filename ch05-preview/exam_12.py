import matplotlib.pyplot as plt
import pandas as pd


from exam_11_common import get_hawaii_series
from exam_06_common import get_index_df


hawaii_total_cases = get_hawaii_series()
print(hawaii_total_cases)
print(type(hawaii_total_cases))

south_korea_index_df = get_index_df('South Korea')
kor_total_cases = south_korea_index_df['total_cases']

south_korea_population = south_korea_index_df['population']['2022-01-01']
hawaii_population = 1_433_336

hawaii_population_rate = hawaii_population / south_korea_population


print(str(kor_total_cases.index.dtype))
print(str(hawaii_total_cases.index.dtype))

kor_total_cases.index = kor_total_cases.index.astype('string')
hawaii_total_cases.index = hawaii_total_cases.index.astype('string')


print(str(kor_total_cases.index.dtype))
print(str(hawaii_total_cases.index.dtype))


final_df = pd.DataFrame({
    'KOR': kor_total_cases * hawaii_population_rate,
    'HAWAII': hawaii_total_cases
}, index=hawaii_total_cases.index)
print(final_df)


final_df['2022-01-01':].plot.line(rot=45)
plt.show()