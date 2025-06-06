from app.scrappers.scrapper import Scrapper
import re


class RozetkaScrapper(Scrapper):
    def __init__(self, product_url):
        super().__init__(product_url)
        self.store = "rozetka"

    def scrape(self):
        super().scrape()

        title_tag = self.soup.find("h1", class_="title__font")
        if title_tag:
            self.name = title_tag.text

        price_tag = self.soup.find("p", class_="product-price__big text-2xl bold leading-none product-price__big-color-red")
        #product-price__big product-price__big-color-red
        if price_tag:
            self.price = float(''.join(re.findall(r'\d', price_tag.text.strip())))