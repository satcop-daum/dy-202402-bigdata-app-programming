import matplotlib.pyplot as plt
import pandas as pd

from exam_02_function import get_raw_data

raw_data = get_raw_data()
print('=' * 50)
print(raw_data.info())

print('=' * 50)
print(raw_data.head())
selected_columns = ['Age', 'Country', 'LanguageHaveWorkedWith', 'LearnCode']

revised_data = raw_data[selected_columns]

print('=' * 50)
print(revised_data.head())

#연령대 정보 확인하기
print('=' * 50)
print( revised_data['Age'] )


#중복값 삭제하기
revised_data_dup = revised_data['Age'].drop_duplicates()
print('=' * 50)
print(revised_data_dup.head())


# 모든 열의 정보를 출력하도록 설정
# pd.set_option('display.max_info_columns', None)

# 예를 들어, 최대 1000개의 열을 표시하도록 설정
# pd.set_option('display.max_info_columns', 1000)
print('=' * 50)
print(revised_data_dup.info())

print('=' * 50)
for index, value in revised_data_dup.items():
    print(index, value)


revised_data_group = revised_data.groupby(['Age']).size()

print('=' * 50)
print(revised_data_group)


size_by_country = revised_data.groupby(['Country']).size()


print('=' * 50)
print(size_by_country)





















