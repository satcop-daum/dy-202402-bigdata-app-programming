
import pandas as pd
import matplotlib.pyplot as plt

from ch06.exam_function import get_raw_data, get_base_data, print_line, df_info, save_csv


base_data = get_base_data()
save_csv(base_data[:20])


print_line()
print(base_data.head())

data_age = base_data['Age']
save_csv(data_age)

print_line()
print(data_age)

data_age_dup = data_age.drop_duplicates()

print_line()
print(data_age_dup)
print(type(data_age_dup))

data_age_group = base_data.groupby(['Age'])
print_line()
print(data_age_group)

data_age_group_size = data_age_group.size()
print_line()
print(data_age_group_size)
print(type(data_age_group_size))

save_csv(data_age_group_size)








