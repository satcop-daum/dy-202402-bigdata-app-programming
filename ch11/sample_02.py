import pandas as pd
import requests
#Installing Beautiful Soup

#pip install beautifulsoup4

from bs4 import BeautifulSoup

from ch10.exam_function import save_html, print_line, save_csv


def get_http_text():
    url = "https://finance.naver.com/item/sise_day.naver?code=035720"
    header_info = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=header_info)

    return response.text
#end-def

#입력받은 주식코드의 시세데이터의 마지막페이지 번호를 리턴
def get_last_page_number_by_stock_code(code):
    url = "https://finance.naver.com/item/sise_day.naver?code=" + code
    header_info = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=header_info)
    response_text = response.text

    soup = BeautifulSoup(response_text, 'html.parser')
    atag_list = soup.find_all('a', href=True)
    last_atag = atag_list[-1]
    page_number = last_atag['href'].split('page=')[-1]

    return int(page_number)
#end-def

#code1 = '035720'
#code1_pagenumber = get_last_page_number_by_stock_code(code1)
#print(code1, code1_pagenumber)

#code2 = '000660'
#code2_pagenumber = get_last_page_number_by_stock_code(code2)
#print(code2, code2_pagenumber)


def get_stock_sise(code):

    code_pagenumber = get_last_page_number_by_stock_code(code)

    url = f'https://finance.naver.com/item/sise_day.naver?code={code}&page='
    header_info = {
        'User-Agent': 'Mozilla/5.0 '
    }

    all_data = pd.DataFrame()

    for page in range(1, code_pagenumber + 1):
        print(f'{url}{page}')
        response = requests.get(f'{url}{page}', headers=header_info)

        data = pd.read_html(response.text)
        data[0].dropna(inplace=True)
        all_data = pd.concat([all_data, data[0]])

    save_csv(all_data)

#end-def

#get_stock_sise('000660')
get_stock_sise('005380')




















