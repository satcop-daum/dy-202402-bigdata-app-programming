import os
from datetime import datetime

import pandas as pd
import requests
from io import StringIO
from bs4 import BeautifulSoup


from ch10_preview.ch10_function import save_csv, print_line

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://finance.naver.com/item/sise_day.naver?code=005930&page='

all_tables = pd.DataFrame()

req_url = url

page = requests.get(req_url, headers=headers)

html = page.text


# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

a_list = soup.find_all('a', href=True)

print_line()
print(a_list)

for a in a_list:
    print(a)
    print(a.text)



links = [a['href'] for a in soup.find_all('a', href=True)]

link = links[-1]

print(link)

last_number = link.split('page=')[-1]

page_value = last_number

print(page_value)





