import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.flipkart.com/air-conditioners/pr?sid=j9e,abm,c54&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.technology%255B%255D%3DInverter&p[]=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Inverter%20AC"
current = 0
next_page = 2

while True:
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")

    divs = soup.select("._1-2Iqu")
    if not divs:
        break

    with open("Acs.csv", "a", newline="") as file:
        csv_writer = writer(file)
        if not current:
            csv_writer.writerow(["Mobile Name", "Price"])

        for div in divs:
            mobile_name = div.select("._3wU53n")[0].get_text()
            mobile_price = div.select("._1vC4OE")[0].get_text()[1:]
            # print(f"{mobile_name} --> {mobile_price}")
            csv_writer.writerow([mobile_name, mobile_price])

        a_tags = soup.select("._2Xp0TH")

        for tag in a_tags:
            if not current:
                pass
            else:
                url = f"https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.technology%255B%255D%3DInverter&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_TVs+%26+Appliances_0_Inverter+AC&page={next_page}"
                # print(url)
                print(f"😈 Scarping Done {next_page}😈")
                next_page += 1
                break
            current += 1
