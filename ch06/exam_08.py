
import pandas as pd
import matplotlib.pyplot as plt

from ch06.exam_function import get_raw_data, get_base_data, print_line, df_info, save_csv, save_text

base_data = get_base_data()

################################################################################
data1 = base_data[base_data.Age == '25-34 years old']
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

data5 = data4.groupby(data4)
print_line()
print(data5)

data6 = data5.size()
print_line()
print(data6)

data7 = data6.nlargest(10)
print_line()
print(data7)

#data7.plot.pie(figsize=(10, 10), autopct='%1.2f%%')
#plt.show()
################################################################################

data_11 = base_data[base_data.Age == '25-34 years old']['LanguageHaveWorkedWith'].str.split(';').explode()
data_12 = data_11.groupby(data_11).size().nlargest(10)

data_12.plot.pie(figsize=(10, 10), autopct='%1.2f%%')
plt.show()
































