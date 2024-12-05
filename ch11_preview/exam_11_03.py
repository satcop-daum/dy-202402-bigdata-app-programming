from matplotlib import pyplot as plt
from prophet import Prophet

import pandas as pd
import plotly.io as pio

from ch11_preview.ch11_function import save_csv, print_line

# 렌더러를 브라우저로 설정
pio.renderers.default = "browser"


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
print(df)

# 2021년 1월 1일 이후 데이터만 준비
df2 = df[df['ds'] > '2021-01-01']
print_line()
print(df2)


# 2차 예측을 위한 프로핏 객체 만들기
m2 = Prophet()


# 데이터 끝 부분 확인하기
print_line()
print(df2.tail())


# 데이터 학습하기
m2.fit(df2)



# 예측 데이터프레임 만들기
future2 = m2.make_future_dataframe(periods=1000)

print_line()
print(future2)


# 예측하기
forecast2 = m2.predict(future2)
print_line()
print(forecast2)


# 예측 결과 끝부분 확인하기
print(forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# 시각화하기
fig3 = m2.plot(forecast2)
plt.show()



# 2차 예측 컴포넌트 확인하기
fig4 = m2.plot_components(forecast2)
plt.show()



# plot 모듈 탑재
from prophet.plot import plot_plotly, plot_components_plotly



# 대화형 예측 그래프 그리기
# pip install plotly
fig5 = plot_plotly(m2, forecast2)
fig5.show()


# HTML 파일로 저장
# fig5.write_html("forecast.html")

# 브라우저로 열기
# import webbrowser
# webbrowser.open("forecast.html")



# 대화형 예측 컴포넌트 그리기
fig6 = plot_components_plotly(m2, forecast2)
fig6.show()


