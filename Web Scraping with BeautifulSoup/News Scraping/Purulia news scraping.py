import requests
from bs4 import BeautifulSoup

url = "https://www.anandabazar.com/district/purulia-birbhum-bankura/archive"
page_no = 2
while True:

    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")

    articles = soup.find_all("article")
    next_pages = soup.select(".pagination")

    for article in articles:
        heading = article.find("h3")
        # date = article.select(".date-arc")[0].get_text()
        news_title = heading.findChild().get_text()
        print(news_title)
        # print(date)

    if page_no < 51:
        url = f"https://www.anandabazar.com/district/purulia-birbhum-bankura/archive?page={page_no}&slab=0&tnp=50"
        # print(url)
        page_no += 1
    else:
        break