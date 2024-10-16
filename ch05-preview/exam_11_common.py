import matplotlib.pyplot as plt
import pandas as pd

def get_hawaii_series():

    file_path = '../ch04/book_data/hawaii-covid-data.csv'
    raw_hawaii_df = pd.read_csv(file_path)

    filtered_hawaii_df = raw_hawaii_df[['submission_date', 'tot_cases']]

    sorted_hawaii_df = filtered_hawaii_df.sort_values(by='submission_date')
    sorted_hawaii_df['date'] = pd.to_datetime(filtered_hawaii_df['submission_date'])

    sorted_hawaii_df.sort_values(by='date', inplace=True)
    sorted_hawaii_df.set_index('date', inplace=True)

    hawaii_total_cases = sorted_hawaii_df['tot_cases']

    return hawaii_total_cases

#end-def
