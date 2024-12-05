import pandas as pd
import requests

from ch09.exam_function import print_line, save_csv

url = "https://www.dongyang.ac.kr/dmu_23259/1806/subview.do"

url = "https://www.dongyang.ac.kr/dongyang/130/subview.do"

response = requests.get(url)

print(response.text)

data = pd.read_html(response.text)

print_line()
print(len(data))


print_line()
print(data[0])

save_csv(data[0])








