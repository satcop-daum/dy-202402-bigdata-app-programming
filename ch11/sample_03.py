import matplotlib.pyplot as plt
import pandas as pd
import requests
#Installing Beautiful Soup
#pip install beautifulsoup4

from bs4 import BeautifulSoup
from ch10.exam_function import save_html, print_line, save_csv
from ch10.exam_function import save_html, print_line, save_csv
from prophet import Prophet

#file_path = './csv/data_1.csv' #카카오데이터
file_path = './csv/data_2.csv' #현대차
all_data = pd.read_csv(file_path)

print_line()
print(all_data)

header_columns = {'날짜': 'ds'}
all_data.rename(columns=header_columns, inplace=True)

print_line()
print(all_data)


all_data['y'] = all_data['고가'] - ((all_data['고가'] - all_data['저가']) / 2)

print_line()
print(all_data)

_fit_data = all_data[['ds', 'y']]

fit_data = _fit_data[_fit_data['ds'] >= '2020-01-01']

print_line()
print(fit_data)


#프로핏 모델 객체 만들기
model = Prophet()

#학습하기!!!
model.fit(fit_data)

#예측데이터 준비!!!!!!!!
future = model.make_future_dataframe(periods=365)
print_line()
print(future)

#예측수행!!!!!!!!!
forecast = model.predict(future)

print_line()
print(forecast)


fig1 = model.plot(forecast)
plt.show()
# fig1.show()

fig2 = model.plot_components(forecast)
#fig2.show()
plt.show()









