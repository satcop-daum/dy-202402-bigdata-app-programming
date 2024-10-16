import matplotlib.pyplot as plt
import pandas as pd
from six import print_

from exam_02_function import get_raw_data, save_csv_file, print_line, get_column_data, save_text_file

revised_data = get_column_data()

data_language = revised_data['LanguageHaveWorkedWith']

print_line()
print(data_language)


data_language_split = data_language.str.split(';')

print_line()
print(data_language_split)

data_language_split_exploded = data_language_split.explode()


print_line()
print(data_language_split_exploded)

#프로그래밍별 응답 수 확인하기
data_language_split_exploded_size = data_language_split_exploded.groupby(data_language_split_exploded).size()

print_line()
print(data_language_split_exploded_size)


#상위 10개 프로그래밍 언어를 파이 그래프로 그리기
data_language_split_exploded_size.nlargest(10).plot.pie(figsize=(10, 10))
plt.show()


#백분율 표기하기
data_language_split_exploded_size.nlargest(10).plot.pie(figsize=(10, 10)
                                                        , autopct='%1.2f%%')
plt.show()

