import sqlite3

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bewakoof.com/men-clothing").text
soup = BeautifulSoup(response, "html.parser")
conn = sqlite3.connect("bewakoof2.db")
c = conn.cursor()
# c.execute("CREATE TABLE bewakoof2 (product_name TEXT, product_price TEXT);")  # run only 1 time for create the table
for data in soup.select(".productCardDetail"):
    product_title = data.find("h3").get_text()
    product_price = data.select(".discountedPriceText")[0].find("b").get_text()
    if product_title:
        data = (product_title, product_price)
        c.execute("INSERT INTO bewakoof2 VALUES(?, ?)", data)

conn.commit()
conn.close()
