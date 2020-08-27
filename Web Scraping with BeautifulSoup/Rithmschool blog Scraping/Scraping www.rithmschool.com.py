from csv import writer

import requests
from bs4 import BeautifulSoup

url = "https://www.rithmschool.com/blog"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")

articles = soup.find_all("article")

with open("page_data.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["heading", "link", "date"])
    for article in articles:
        heading = article.find("a").get_text()
        url = article.find("a")["href"]
        date = article.find("time")["datetime"].split(" ")[0]
        csv_writer.writerow([heading, url, date])

print("😈 Scarping Done 😈")