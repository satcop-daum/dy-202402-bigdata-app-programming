import pandas as pd
import requests
from matplotlib import pyplot as plt

from ch10.exam_function import save_html, print_line, save_csv


data_columns = {
    '날짜': 'date',
    '종가': 'end_price',
    '시가': 'start_price',
    '고가': 'max_price',
    '저가': 'min_price'
}

file_path = './csv/data_sample.csv'
raw_data = pd.read_csv(file_path)

all_data = raw_data.rename(columns=data_columns)

all_data.drop(['전일비', '거래량', 'start_price', 'max_price', 'min_price'], axis=1, inplace=True)

print_line()
print(all_data)


all_data['date_month'] = all_data['date'].str[:7]


print_line()
print(all_data)


all_data.set_index('date', inplace=True)
all_data.sort_index(inplace=True)


all_data.boxplot(column=['end_price'], by=['date_month'])
plt.show()






