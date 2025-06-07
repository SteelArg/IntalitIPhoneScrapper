from app.scrappers.scrapper import Scrapper
import json

foxtrot_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8"
    }


class FoxtrotScrapper(Scrapper):
    def __init__(self, product_url):
        super().__init__(product_url)
        self.store = "foxtrot"
        self.headers = foxtrot_headers

    def scrape(self):
        super().scrape()

        script_tag = self.soup.find("script", {"type": "application/ld+json"})
        if script_tag:
            data = json.loads(script_tag.string)

            variant = data

            self.name = variant.get("name", None)
            self.price = variant.get("offers", {}).get("price", 0)
