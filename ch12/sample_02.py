import pandas as pd
import prophet
from prophet import Prophet

from ch10.exam_function import print_line, save_csv

file_path = './data/survey_results_public.csv'
raw_data = pd.read_csv(file_path)


print_line()
print(raw_data)

column_name = 'DevType'
value_list = ['Data scientist or machine learning specialist', 'Data or business analyst']

base_data = raw_data[raw_data[column_name].isin(value_list)]

print_line()
print(base_data)


lang_column_name = 'LanguageHaveWorkedWith'

lang_data = base_data[lang_column_name]

print_line()
print(lang_data)















































