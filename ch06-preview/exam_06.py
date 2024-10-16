import matplotlib.pyplot as plt
import pandas as pd
from exam_02_function import get_raw_data, save_csv_file, print_line, get_column_data, save_text_file

revised_data = get_column_data()
data_age_size = revised_data.groupby(['Age']).size()

print_line()
print(data_age_size)


age_index = data_age_size.index

print_line()
print(age_index)

#text_contents = ''
#for x in age_index:
#    text_contents += "'" + x + "'," + '\n'
#save_text_file('./age_index.txt', text_contents)

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
data_age_size_reindex = data_age_size.reindex(index = re_index)

print_line()
print(data_age_size_reindex)


#수평 막대그래프
data_age_size_reindex.plot.barh()
plt.show()

