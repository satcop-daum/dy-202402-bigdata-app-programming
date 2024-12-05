
import os
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime


def save_html(contents):
    base_path = './html'
    if not os.path.exists(base_path):
        os.mkdir(base_path)

    cur_datetime = datetime.now()
    cur_date_format = cur_datetime.strftime('%Y%m%d_%H%M%S')

    file_path = f'./html/html_{cur_date_format}.html'

    with open(file_path, 'w') as file:
        file.write(contents)
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



def print_line():
    cur_datetime = datetime.now()
    cur_date_format = cur_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print(cur_date_format)
    print(f'=====[{cur_date_format}]{"=" * 50}')
#end-def

