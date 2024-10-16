import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

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


def get_raw_data():
    file_name = './data/stack-overflow-2024/survey_results_public.csv'
    #file_name = './data/stack-overflow-2022/survey_results_public.csv'

    raw_data = pd.read_csv(file_name)
    return raw_data
#end-def

def get_column_data():
    raw_data = get_raw_data()
    columns = ['Age', 'Country', 'LanguageHaveWorkedWith', 'LearnCode']
    revised_data = raw_data[columns]
    return revised_data
#end-def

def save_csv_file(df):

    current_datetime = datetime.now()
    current_datetime_str =  current_datetime.strftime("%Y%m%d_%H%M%S")

    csv_file_path = f'./csv/data_${current_datetime_str}.csv'

    base_path = './csv'
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    df.to_csv(csv_file_path, index=False)
#end-def

def save_text_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
#end-def

def print_line():
    current_datetime = datetime.now()
    current_datetime_str = current_datetime.strftime("%Y%m%d_%H:%M:%S.%f")[:-3]

    print(f'{'=' * 50} >>>> {current_datetime_str}')
#end-def

























