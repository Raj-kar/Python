from csv import writer

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

    with open("data2.csv", "a", newline='') as file:
        csv_writer = writer(file)
        global count
        if not count:
            csv_writer.writerow(["Title", "Price", "Ratings"])
            count += 1
        for item in components:
            try:
                csv_writer.writerow([get_title(item), get_title(item), get_ratings(item)])
            except Exception as e:
                pass
        print(f"😈 Scarping Done 😈")


for i in range(2, 50):  # highest 400 page available ! [can automate this using page crawl]
    scrap(
        f'https://www.amazon.in/s?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031&page=2&qid=1598861453&ref=lp_1389401031_pg_{i}')
