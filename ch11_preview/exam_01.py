import os
from datetime import datetime

import pandas as pd
import requests
from io import StringIO

from ch11_preview.ch11_function import save_csv, print_line

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://finance.naver.com/item/sise_day.naver?code=005930&page='

all_tables = pd.DataFrame()

for page_number in range(1, 712 + 1):

    req_url = url + str(page_number)

    print(f'{page_number} => {req_url}')

    page = requests.get(req_url, headers=headers)

    table = pd.read_html(StringIO(page.text))[0]

    print(f'ALL {len(all_tables.index)} => {len(table.index)} ADDED')

    all_tables = pd.concat([all_tables, table])

all_tables.dropna(inplace=True)

save_csv(all_tables)


