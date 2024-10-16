
import pandas as pd
import matplotlib.pyplot as plt

from ch06.exam_function import get_raw_data, get_base_data, print_line, df_info, save_csv, save_text


base_data = get_base_data()

data_age_size = base_data.groupby(['Age']).size()

data_age_size_index = data_age_size.index

print_line()
print(data_age_size_index)
print(type(data_age_size_index))

"""
    text_contents = ''
    for x in data_age_size_index:
        text_contents += "'" + x + "'," + '\n'
    save_text('./index.txt', text_contents)
"""

re_index = [
    'Prefer not to say',
    '65 years or older',
    '55-64 years old',
    '45-54 years old',
    '35-44 years old',
    '25-34 years old',
    '18-24 years old',
    'Under 18 years old'
]
data_age_size_reindex = data_age_size.reindex(re_index)
print_line()
print(data_age_size_reindex)

data_age_size_reindex.plot.barh()
plt.show()





