import matplotlib.pyplot as plt
import pandas as pd
from six import print_

from exam_02_function import get_raw_data, save_csv_file, print_line, get_column_data, save_text_file

revised_data = get_column_data()

#25~34세 개발자들이 사용한 프로그래밍 언어 데이터를 추출하기
data_lang_age = revised_data[revised_data.Age == '25-34 years old']['LanguageHaveWorkedWith'].str.split(';').explode()

print_line()
print(data_lang_age)

data1 = revised_data[revised_data.Age == '25-34 years old']

print_line()
print(data1)

data2 = data1['LanguageHaveWorkedWith']

print_line()
print(data2)

data3 = data2.str.split(';')

print_line()
print(data3)

data4 = data3.explode()

print_line()
print(data4)

data5 = data4.groupby(data4).size()

print_line()
print(data5)

data6 = data5.nlargest(10)

print_line()
print(data6)

data6.plot.pie(figsize=(10, 10), autopct='%1.1f%%')
plt.show()



