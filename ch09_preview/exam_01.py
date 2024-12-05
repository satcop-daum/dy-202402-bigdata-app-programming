import os
from datetime import datetime

import pandas as pd
import requests
from io import StringIO

def save_text_file(content):

    current_datetime = datetime.now()
    current_datetime_str =  current_datetime.strftime("%Y%m%d_%H%M%S")

    file_path = f'./html/html_${current_datetime_str}.html'

    base_path = './html'
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    with open(file_path, 'w') as file:
        file.write(content)
#end-def



headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://finance.naver.com/item/sise_day.naver?code=005930&page=2'

page = requests.get(url, headers=headers)

#print(page.text)
#save_text_file(page.text)

# pages = pd.read_html(page.text)
pages = pd.read_html(StringIO(page.text))

print(type(pages))

print(len(pages))


print(pages[0])

print(pages[1])
