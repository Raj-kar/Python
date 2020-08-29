import scrapy


class PaytmScrapy(scrapy.Spider):
    name = "PaytmElectronics"
    start_urls = [
        'https://paytmmall.com/Grooming-Appliances-Bestsellers-llpid-205950?discoverability=online&use_mw=1&src=store&from=storefront',
        'https://paytmmall.com/mobiles-glpid-6224?use_mw=1&src=store&from=storefront',
        'https://paytmmall.com/best-selling-lap-tops-llpid-233881?discoverability=online&use_mw=1&src=store&from=storefront',
        'https://paytmmall.com/Headphones-Headsets-new-llpid-201381?discoverability=online&use_mw=1&src=store&from=storefront',
        'https://paytmmall.com/For-Extra-Storage-Upto-50-off-llpid-187836?discoverability=online&use_mw=1&src=store&from=storefront']

    def parse(self, response, **kwargs):
        for div in response.css("._3WhJ"):
            yield {
                'title': div.css(".UGUy::text").extract_first(),
                'price': div.css("span::text").extract_first()
            }
            next = response.css("._2TzX > a::attr(href)").extract_first()
            if next:
                yield response.follow(next, self.parse)

# Spider with Scrapy>scrapy runspider -o paytm_data.csv paytm_mall_Scrape.py
