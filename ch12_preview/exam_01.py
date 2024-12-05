import os
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import requests
from io import StringIO

from wordcloud import WordCloud

from ch11_preview.ch11_function import save_csv, print_line


raw_data = pd.read_csv('./data/survey_results_public.csv')

print_line()
print(raw_data.info())

print_line()
print(raw_data.head())
#save_csv(raw_data[:10])


print_line()
print(raw_data['DevType'])


dev_type = raw_data['DevType'].str.split(';')

print_line()
print(dev_type)


#결손치제거
dev_type.dropna(inplace=True)

print_line()
print(dev_type)


#리스트항목을각행으로나누기
exploded_dev_type = dev_type.explode()

print_line()
print(exploded_dev_type)


#유일한값확인하기

print_line()
print(exploded_dev_type.unique())


#데이터분석가데이터만추출
data_analyst_data = raw_data[raw_data['DevType'].isin(['Data scientist or machine learning specialist', 'Data or business analyst'])]


print_line()
print(data_analyst_data)
#save_csv(data_analyst_data)

#프로그램언어데이터추출
languages = data_analyst_data['LanguageHaveWorkedWith']

print_line()
print(languages)

#데이터문자열변환후구분자로구분
languages = languages.str.split(';')
print_line()
print(languages)

#리스트를항목으로나누기
languages_exploded = languages.explode()
print_line()
print(languages_exploded)


size_by_languages = languages_exploded.groupby(languages_exploded).size()

print_line()
print(size_by_languages)

#데이터빈도역순으로정렬
size_by_languages.sort_values(ascending=False, inplace=True)

print_line()
print('#데이터빈도역순으로정렬')
print(size_by_languages)
print(type(size_by_languages))


#시각화를위해데이터프레임으로만듬

frame = {'language': size_by_languages.index, 'count': size_by_languages.values}

size_by_languages_df = pd.DataFrame(frame)

print_line()
print(size_by_languages_df.head())

save_csv(size_by_languages_df)




wordcloud = WordCloud(background_color='white').generate_from_frequencies(size_by_languages.to_dict())

plt.rcParams['figure.figsize'] = (10, 10)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()



