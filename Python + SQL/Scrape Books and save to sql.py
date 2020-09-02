import sqlite3

import requests
from bs4 import BeautifulSoup


def scraping(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    all_books = []
    books = soup.find_all("article")
    for book in books:
        new_book = (get_title(book), get_price(book), get_rating(book))
        all_books.append(new_book)
    create_db(all_books)


def create_db(data):
    conn = sqlite3.connect("books_data.db")
    c = conn.cursor()
    c.execute("CREATE TABLE books (title TEXT, price REAL, rating INT);")
    c.executemany('INSERT INTO books VALUES(?,?,?);', data)
    conn.commit()
    conn.close()


def get_title(book):
    return book.find("h3").find("a")["title"]


def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return price.replace("Â£", "")


def get_rating(book):
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    rating = book.select(".star-rating")[0]
    word = rating.get_attribute_list("class")[1]
    return ratings[word]


# start here
scraping("http://books.toscrape.com/")
