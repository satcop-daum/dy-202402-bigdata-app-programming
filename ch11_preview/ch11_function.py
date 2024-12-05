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

def print_line():
    cur_datetime = datetime.now()
    cur_date_format = cur_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print(cur_date_format)
    print(f'=====[{cur_date_format}]{"=" * 50}')
#end-def

def save_csv(df):
    base_path = './csv'
    if not os.path.exists(base_path):
        os.mkdir(base_path)

    cur_datetime = datetime.now()
    cur_date_format = cur_datetime.strftime('%Y%m%d_%H%M%S')

    csv_file_path = f'./csv/data_{cur_date_format}.csv'
    df.to_csv(csv_file_path, index=False)
#end-def

