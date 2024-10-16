import matplotlib.pyplot as plt
import pandas as pd
from exam_02_function import get_raw_data, save_csv_file, print_line, get_column_data, save_text_file

revised_data = get_column_data()
#일부 데이터 확인하기
print_line()
print(revised_data.head())

#국가별 응답 숫자 확인하기
data_country_size = revised_data.groupby(['Country']).size()

print_line()
print(data_country_size)


data_country_size.plot.pie()
plt.show()

data_country_size.plot.pie(figsize=(10, 10))
plt.show()
