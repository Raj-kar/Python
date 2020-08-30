import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.snapdeal.com/products/mobiles-mobile-phones/filters/Form_s~Smartphones?sort=plrty").text
soup = BeautifulSoup(response, "html.parser")

for data in soup.select(".dp-widget-link"):
    product_title = data.select(".product-title ")
    product_price = data.select(".product-price")
    if product_title:
        print(product_title[0].get_text())
        print(product_price[0].get_text())