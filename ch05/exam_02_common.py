import pandas as pd

# 전달된 location의 값을 통해서 data.csv 파일에서 관련 데이터만 리턴
def get_covid_data(location):

   file_path = '../ch05/book_data/owid-covid-data.csv'
   raw_df = pd.read_csv(file_path)

   selected_columns = ['iso_code', 'location', 'date', 'total_cases', 'population']

   selected_df = raw_df[selected_columns]

   # South Korea
   south_korea_df = selected_df[selected_df.location == location]

   south_korea_index_df = south_korea_df.set_index('date')

   return south_korea_index_df

#end-def