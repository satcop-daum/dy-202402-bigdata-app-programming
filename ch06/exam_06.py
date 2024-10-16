
import pandas as pd
import matplotlib.pyplot as plt

from ch06.exam_function import get_raw_data, get_base_data, print_line, df_info, save_csv, save_text

base_data = get_base_data()
data_country_size = base_data.groupby(['Country']).size()

print_line()
print(data_country_size)


#data_country_size.plot.pie(figsize=(10, 10))
#plt.show()

data_country_size_top20 = data_country_size.nlargest(20)

data_country_size_top20.plot.pie(figsize=(10, 10))
plt.show()






