import matplotlib.pyplot as plt
import pandas as pd
from exam_02_function import get_raw_data, save_csv_file, print_line, get_column_data

revised_data = get_column_data()
data_age_size = revised_data.groupby(['Age']).size()

print_line()
print(data_age_size)

data_age_size.plot.line(rot=45)
plt.show()

#수직 막대그래프
data_age_size.plot.bar(rot=-45)
plt.show()


#수평 막대그래프
data_age_size.plot.barh()
plt.show()


