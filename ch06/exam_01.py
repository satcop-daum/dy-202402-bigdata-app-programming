
import pandas as pd
import matplotlib.pyplot as plt

from ch06.exam_function import get_raw_data, print_line, df_info

raw_data = get_raw_data()
#print(raw_data.info())

df_info(raw_data)

print_line()
print(type(raw_data))




