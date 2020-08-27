import requests
from bs4 import BeautifulSoup
from csv import writer

page = 2
c = 0
s_no = 1
url = "https://www.rithmschool.com/blog/"
while True:
    try:
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")

        articles = soup.find_all("article")
        spans = soup.select(".page")
        if not spans:
            break

        with open("page_all_data.csv", "a") as file:
            csv_writer = writer(file)
            if not c:
                csv_writer.writerow(["no","heading", "link", "date"])
            for article in articles:
                heading = article.find("a").get_text()
                url = article.find("a")["href"]
                date = article.find("time")["datetime"].split(" ")[0]
                csv_writer.writerow([s_no, heading, url, date])
                s_no += 1
            print(f"😈 Scarping Done 😈")

            for span in spans:
                if c:
                    a_tag = span.find("a")
                    url = f"https://www.rithmschool.com/blog/?page={page}"
                    print(url)
                    break
                c += 1
            page += 1
    except Exception as e:
        print("Network not connected !")
        print(e)
        break
