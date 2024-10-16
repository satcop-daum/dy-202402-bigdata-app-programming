import matplotlib.pyplot as plt
import pandas as pd

from exam_02_function import get_raw_data, save_csv_file, print_line


raw_data = get_raw_data()
#일부 데이터 확인하기
print('=' * 50)
print(raw_data.head())


#필요한 열만 추출하기
'''
Age: 나이
Country: 국가 정보
LanguageHaveWorkedWith: 다룰 줄 아는 프로그래밍 언어
LearnCode: 프로그래밍을 배운 방법
'''

columns = ['Age', 'Country', 'LanguageHaveWorkedWith', 'LearnCode']
revised_data = raw_data[columns]

print('=' * 50)
print(revised_data.head())

# csv 파일로 저장
save_csv_file(revised_data)


#특정 열 데이터 조회하기
revised_data_age = revised_data['Age']
print('=' * 50)
print(revised_data_age)


#유일 데이터 확인하기
revised_data_age_dup = revised_data_age.drop_duplicates()

print('=' * 50)
print(revised_data_age_dup)


#데이터 그룹화 객체 만들기 - groupby() 메서드
revised_data_group = revised_data.groupby(['Age'])

print_line()
#print(type(revised_data_group))
print(revised_data_group.size())









