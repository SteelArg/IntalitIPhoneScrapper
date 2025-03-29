from app.scrappers.scrapper import Scrapper


class MoyoScrapper(Scrapper):
    def __init__(self, product_url):
        super().__init__(product_url)
        self.store = "moyo"

    def scrape(self):
        super().scrape()

        title_tag = self.soup.find("meta", {"property": "og:title"})
        if title_tag:
            self.name = title_tag["content"]

        price_tag = self.soup.find("meta", {"itemprop": "price"})
        if price_tag:
            self.price = price_tag["content"]
        else:
            self.price = 0
