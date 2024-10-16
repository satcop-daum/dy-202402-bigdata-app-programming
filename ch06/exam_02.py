
import pandas as pd
import matplotlib.pyplot as plt

from ch06.exam_function import get_raw_data, print_line, df_info

raw_data = get_raw_data()


print(raw_data.head())


'''
15	Country	71771 non-null	object
19	LanguageHaveWorkedWith	70975 non-null	object
49	Age	70946 non-null	object
'''
columns = ['Age', 'Country', 'LanguageHaveWorkedWith']
base_data = raw_data[columns]


print_line()
print(base_data.head())



