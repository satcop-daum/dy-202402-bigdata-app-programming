import os
from datetime import datetime

import pandas as pd
import requests
from io import StringIO

from matplotlib import pyplot as plt
from wordcloud import WordCloud

from ch11_preview.ch11_function import save_csv, print_line


raw_data = pd.read_csv('./csv/data_languages.csv')

print_line()
print(raw_data.head())


print_line()
print(type(raw_data))


series_language_count = raw_data.set_index("language")["count"]

print_line()
print(series_language_count)
print(type(series_language_count))


wordcloud = WordCloud(background_color='white').generate_from_frequencies(series_language_count.to_dict())

plt.rcParams['figure.figsize'] = (10, 10)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()



