import sqlite3

import requests
from bs4 import BeautifulSoup

count = 0


def get_title(item):
    title = item.find("h2").find("span").get_text()
    if title == "Need help?":
        pass
    else:
        return title


def get_price(item):
    return item.select(".a-price-whole")[0].get_text()


def get_ratings(item):
    price = item.select(".a-icon-alt")[0].get_text()
    return float(price[:3])


def scrap(url):
    # print(url)
    response = requests.get(url).text

    soup = BeautifulSoup(response, "html.parser")

    components = soup.select(".s-result-item")

    all_items = []
    for item in components:
        try:
            data = (get_title(item), get_price(item), get_ratings(item))
            all_items.append(data)
        except Exception as e:
            pass
    print(f"😈 Scarping Done 😈")
    # print(all_items)  # for test
    create_db(all_items)


def create_db(data):
    conn = sqlite3.connect("amazon_data.db")
    c = conn.cursor()
    # c.execute("CREATE TABLE amazon (title TEXT, price REAL, rating INT);")
    c.executemany('INSERT INTO amazon VALUES(?,?,?);', data)
    conn.commit()
    conn.close()


scrap(
    'https://www.amazon.in/s?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031&page=2&qid=1598861453&ref=lp_1389401031_pg_2')
