from src.scrappers.scrapper import Scrapper
import json

foxtrot_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br"
    }


class FoxtrotScrapper(Scrapper):
    def __init__(self, product_url):
        super().__init__(product_url)
        self.store = "foxtrot"
        self.headers = foxtrot_headers

    def scrape(self):
        super().load()

        script = self.soup.find("script", {"type": "application/ld+json"})
        if script:
            data = json.loads(script.string)
            if "hasVariant" in data:
                variant = data["hasVariant"][0]
                self.name = variant.get("name", "Не вказано")
                self.price = variant.get("offers", {}).get("price", 0)
            else:
                self.name = "Не вказано"
                self.price = 0
        else:
            self.name = "Не вказано"
            self.price = 0
