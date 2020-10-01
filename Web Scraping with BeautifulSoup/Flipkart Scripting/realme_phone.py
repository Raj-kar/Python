import requests
from bs4 import BeautifulSoup
import pandas as pd

def realme(next_page):
    url = f'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme&page={next_page}'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    return soup

def extract(soup):
    divs = soup.find_all('div', class_ = '_1-2Iqu')
    
    for items in divs:
        title = items.find('div', class_ = '_3wU53n').text
        price = items.find('div', class_ = '_1vC4OE').text.replace('₹','')
        
        mobile = {
            'Mobile Name': title,
            'Price': price,
        }

        realme_list.append(mobile)

    return

realme_list = []

for i in range(1,6):
    print(f'Getting Page {i}!!')
    c = realme(i)
    extract(c)

df = pd.DataFrame(realme_list)
df.to_csv('realme_phones.csv')
