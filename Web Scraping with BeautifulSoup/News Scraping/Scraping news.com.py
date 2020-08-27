from bs4 import BeautifulSoup
import requests
from termcolor import cprint, colored
from random import choice
import pyfiglet

url = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"

response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")

ava_colors = ("red", "blue", "green", "yellow", "blue", "magenta", "cyan")
google_news = pyfiglet.figlet_format("GOOGLE  NEWS")
cprint(colored(google_news, choice(ava_colors)))

headings = soup.find_all("h3")
for heading in headings:
    print(heading.get_text())