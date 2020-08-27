from csv import writer

import requests
from bs4 import BeautifulSoup

url = "https://digigrocery.in/shop/"

count = 0
page = 2
while True:
    try:
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")

        products = soup.select(".woo-entry-inner")
        next_pages = soup.select(".page-numbers")

        if not next_pages:
            break

        with open("grocery.csv", "a", newline="") as file:
            csv_writer = writer(file)
            if not count:
                csv_writer.writerow(["s_no", "Item name", "Max-Price"])
            for product in products:
                # print(product.find("img")["alt"])
                item_name = product.select(".title")[0].findChild()
                item_name = item_name.get_text()
                spans = product.select(".woocommerce-Price-amount")
                if spans:
                    for span in spans:
                        price = span.get_text()[1:]
                csv_writer.writerow([count + 1, item_name, price])
                count += 1
            print(f"😈 Scarping Done 😈")

        for next_page in next_pages:
            next_ = next_page.attrs
            try:
                url = f"{next_['href'][:-2]}{page}/"
                page += 1
                break
            except Exception as e:
                pass
    except Exception as e:
        print("Network not connected !")
        print(e)
        break
