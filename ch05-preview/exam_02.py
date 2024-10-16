import matplotlib.pyplot as plt
import pandas as pd

# 데이터프레임 생성
df = pd.DataFrame({
    'pig': [20, 18, 489, 675, 1776],
    'horse': [4, 25, 281, 600, 1900]
}, index=[1990, 1997, 2003, 2009, 2014])

# 라인 플롯 생성
lines = df.plot.line()

print(lines)

# 차트를 화면에 출력
plt.show()
