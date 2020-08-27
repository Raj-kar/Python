from random import randint

import requests
from bs4 import BeautifulSoup

def split_name(name):
    name = name.replace(".", " ")
    name = name.replace(" ", "-")
    name = name.replace("'", "")
    return name.replace("--", "-")


while True:
    random_page = randint(1, 10)

    url = f"http://quotes.toscrape.com/page/{random_page}/"

    quote_list = []
    author_list = []

    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")

    spans = soup.select(".quote")

    for span in spans:
        quote = span.select(".text")[0].get_text()
        author = span.select(".author")[0].get_text()
        quote_list.append(quote)
        author_list.append(author)

    random_no = randint(1, len(quote_list) - 1)
    quote = quote_list[random_no]
    author = author_list[random_no]

    print(" Here's a quote :\n")
    print(quote)

    _author = split_name(author)
    url = f"http://quotes.toscrape.com/author/{_author}/"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")

    author_birth_place = soup.select(".author-born-location")[0].get_text()
    author_bron_date = soup.select(".author-born-date")[0].get_text()

    chance = 4

    while chance > 0:
        user_ans = input(f"\n Who said this? Guessing remaining: {chance}. ")
        if user_ans == author:
            print(" you guess correctly ! Congratulations !")
            break
        else:
            if chance == 4:
                print(f" Here is a hint: The author was bron in {author_bron_date} in {author_birth_place} ")
            elif chance == 3:
                print(f" Here is a hint: The author's first name starts with {author[0]}")
            elif chance == 2:
                print(f" Here is a hint: The author's last name starts with {author.split(' ')[-1][0]}")
            elif chance == 1:
                print(f" Sorry, you've run out of guess, the correct answer is {author}")
        chance -= 1
    play_again = input("\n Would you like to play again (y/n)?").lower()
    if play_again[0] == "n":
        print(" Ok ! See you nex time !")
        break
    print(" Great Here we again ....")