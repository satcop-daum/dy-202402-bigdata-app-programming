from matplotlib import pyplot as plt
from prophet import Prophet

import pandas as pd

from ch11_preview.ch11_function import save_csv, print_line




url = './csv/data_1.csv'
data_table = pd.read_csv(url)

print_line()
print(data_table)

header_columns = {'날짜': 'ds'}
data_table.rename(columns=header_columns, inplace=True)

print_line()
print(data_table)


data_table['y'] = data_table['고가'] - ((data_table['고가'] - data_table['저가']) / 2)

print_line()
print(data_table)

print_line()
df = data_table[['ds', 'y']]
df.info()


# 프로핏 모델 객체 만들기
m = Prophet()

# 데이터프레임 학습하기
m.fit(df)

# 예측 데이터프레임 준비하기
future = m.make_future_dataframe(periods=1000)
print_line()
print(future.tail())


#예측하기
forecast = m.predict(future)

print_line()
print(forecast.tail())

print_line()
# 예측 결과 끝부분 확인하기
forecast_columns = ['ds', 'yhat', 'yhat_lower', 'yhat_upper']
print(forecast[forecast_columns])

# 예측 결과 시각화하기
fig1 = m.plot(forecast)
fig1.show()


fig2 = m.plot_components(forecast)
fig2.show()



