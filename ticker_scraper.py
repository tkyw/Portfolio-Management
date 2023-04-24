import pandas as pd 
from string import ascii_uppercase
import requests 
from bs4 import BeautifulSoup as bs 

def get_ticker(alphabet):
    link = "https://www.malaysiastock.biz/Listed-Companies.aspx?type=A&value={}".format(alphabet)
    res = requests.get(link)
    soup = bs(res.content, 'lxml')
    table = soup.select_one("#MainContent_tStock")
    return pd.read_html(table.prettify())[0]

if  __name__ == '__main__':
    alphabets = list(ascii_uppercase)
    # for i, data in enumerate(get_ticker(alphabet)):
    #     print(i,'\n', data)
    #     print("------------------------\n")
    df = None
    for alphabet in alphabets:
        if df is not None:
            df = pd.concat([df, get_ticker(alphabet)])
        else:
            df = get_ticker(alphabet)
    df = df.reset_index(drop=True)
    df.to_excel("ticker.xlsx")