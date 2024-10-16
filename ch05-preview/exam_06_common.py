import matplotlib.pyplot as plt
import pandas as pd


def get_index_df(country):
    file_path = '../ch04/book_data/owid-covid-data.csv'
    raw_df = pd.read_csv(file_path)

    selected_columns = ['iso_code', 'location', 'date', 'total_cases', 'population']
    selected_df = raw_df[selected_columns]

    # South Korea
    south_korea_df = selected_df[selected_df.location == country]
    south_korea_index_df = south_korea_df.set_index('date')

    return south_korea_index_df
#end def
