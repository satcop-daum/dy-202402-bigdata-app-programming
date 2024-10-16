
import pandas as pd
import matplotlib.pyplot as plt

from ch06.exam_function import get_raw_data, get_base_data, print_line, df_info, save_csv


base_data = get_base_data()


data_age_size = base_data.groupby(['Age']).size()

print_line()
print(data_age_size)
print(type(data_age_size))

data_country_size = base_data.groupby(['Country']).size()

print_line()
print(data_country_size)


# 그래프 그려봅시다.!!!!

data_age_size.plot.line(rot=-45)
plt.show()

data_age_size.plot.bar()
plt.show()

data_age_size.plot.barh()
plt.show()

