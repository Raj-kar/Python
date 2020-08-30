import scrapy


class BookScripy(scrapy.Spider):
    name = "Ganna"
    start_urls = ["https://gaana.com/", "https://gaana.com/browse/albums"]

    def parse(self, response):
        for song in response.css(".arwtork_label"):
            yield {
                'song name': song.css(".album-name::text").extract_first()
            }


# scrapy runspider -o gaana_data.csv Ganna.py
