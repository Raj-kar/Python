import scrapy


class MyntraScripy(scrapy.Spider):
    name = "Myntra"
    start_urls = ["https://www.myntra.com/men-tshirts"]

    def parse(self, response, **kwargs):
        for shirt in response.css(".results-base"):
            yield {
                'shirt': shirt
            }

# scrapy runspider -o gaana_data.csv Ganna.py
