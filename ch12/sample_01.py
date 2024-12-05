import pandas as pd
import prophet
from prophet import Prophet

from ch10.exam_function import print_line, save_csv

file_path = './data/survey_results_public.csv'
raw_data = pd.read_csv(file_path)


print_line()
print(raw_data)


print_line()
print(raw_data.info())

column_name = 'DevType'

print_line()
print(raw_data[column_name])

dev_type_data = raw_data[column_name].str.split(';')

print_line()
print(dev_type_data)

dev_type_data.dropna(inplace=True)

print_line()
print(dev_type_data)

#dev_type_data의 리스트항목을 목록 문자열로 처리
dev_data = dev_type_data.explode()

print_line()
print(dev_data)


#dev_data에서 중복된 항목을 제거
dev_unique_data = dev_data.unique()

print_line()
print(dev_unique_data)

'Data scientist or machine learning specialist'
'Data or business analyst'












































