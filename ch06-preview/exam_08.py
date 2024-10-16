import matplotlib.pyplot as plt
import pandas as pd
from exam_02_function import get_raw_data, save_csv_file, print_line, get_column_data, save_text_file

revised_data = get_column_data()
data_country_size = revised_data.groupby(['Country']).size()


data_country_size_20 = data_country_size.nlargest(20)

print_line()
print(data_country_size_20)


data_country_size_20.plot.pie(figsize=(10, 10))
plt.show()

