import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from exam_02_function import df_info as info

file_name = './data/stack-overflow-2024/survey_results_public.csv'
file_name = './data/stack-overflow-2022/survey_results_public.csv'

raw_data = pd.read_csv(file_name)
print('=' * 50)
print(raw_data.info())

print('=' * 50)
print('데이터 프레임 데이터 타입 확인')
print(raw_data.dtypes)

print('=' * 50)
info(raw_data)

