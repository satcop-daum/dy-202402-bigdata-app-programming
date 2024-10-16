import os
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

def save_csv(df):
    base_path = './csv'
    if not os.path.exists(base_path):
        os.mkdir(base_path)

    cur_datetime = datetime.now()
    cur_date_format = cur_datetime.strftime('%Y%m%d_%H%M%S')

    csv_file_path = f'./csv/data_{cur_date_format}.csv'
    df.to_csv(csv_file_path, index=False)
#end-def

def save_text(file_path, text_contents):
    with open(file_path, 'w') as file:
        file.write(text_contents)
#end-def

def print_line():
    cur_datetime = datetime.now()
    cur_date_format = cur_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print(cur_date_format)
    print(f'=====[{cur_date_format}]{"=" * 50}')
#end-def

def df_info(df):
    # 데이터프레임의 인덱스 정보 출력
    print(f"<class 'pandas.core.frame.DataFrame'>")
    print(f"Index: {df.index}")

    # 컬럼 정보 헤더
    print(f"Data columns (total {df.shape[1]} columns):")

    # 각 컬럼에 대한 정보 출력
    col_info = []
    for i, col in enumerate(df.columns):
        dtype = df[col].dtype  # 데이터 타입
        non_null_count = df[col].count()  # 결측치가 아닌 값의 개수
        total_count = len(df[col])  # 전체 행의 개수
        null_count = total_count - non_null_count  # 결측치의 개수
        col_info.append(f"{i}\t{col}\t{non_null_count} non-null\t{dtype}")

    for info in col_info:
        print(info)

    # 메모리 사용량 출력
    memory_usage = df.memory_usage(deep=True).sum()  # 메모리 사용량
    print(f"dtypes: {df.dtypes.nunique()} types")
    print(f"memory usage: {memory_usage / 1024:.2f} KB")
#end-def


