
import pandas as pd
import matplotlib.pyplot as plt

from ch06.exam_function import get_raw_data, get_base_data, print_line, df_info, save_csv, save_text

base_data = get_base_data()

data_lang = base_data['LanguageHaveWorkedWith']

print_line()
print(data_lang)
#save_csv(data_lang)

data_lang_split = data_lang.str.split(';')
print_line()
print(data_lang_split)
save_csv(data_lang_split)

lang_data_exploded = data_lang_split.explode()
print_line()
print(lang_data_exploded)
save_csv(lang_data_exploded)

lang_data_size = lang_data_exploded.groupby(lang_data_exploded).size()
print_line()
print(lang_data_size)

lang_data_size_top10 = lang_data_size.nlargest(10)
print_line()
print(lang_data_size_top10)

lang_data_size_top10.plot.pie(figsize=(10, 10), autopct='%1.2f%%')
plt.show()














