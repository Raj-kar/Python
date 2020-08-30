import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.myntra.com/men-tshirts")

print(response)
# soup = BeautifulSoup(response, "html.parser")
#
# for shirts in soup.select(".results-base"):
#     print(shirts)