import pandas as pd
import requests


from ch09.exam_function import save_html, print_line, save_csv

url = "https://finance.naver.com/item/sise_day.naver?code=005930&page="

header_info = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0


all_data = pd.DataFrame()


for page in range(1, 712 + 1):
    req_url = f'{url}{page}'
    print(req_url)

    response = requests.get(req_url, headers=header_info)
    
    print_line()
    # print(response.text)
    # save_html(response.text)
    
    data = pd.read_html(response.text)
    
    print_line()
    print(type(data))
    
    print_line()
    print(len(data))

    #data[0] = data[0].dropna()
    data[0].dropna(inplace=True)

    all_data = pd.concat([all_data, data[0]])
        
    # print_line()
    # print(data[0])


print_line()
print(all_data)

save_csv(all_data)









