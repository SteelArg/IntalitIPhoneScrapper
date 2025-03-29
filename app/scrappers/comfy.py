from app.scrappers.scrapper import Scrapper
import json


comfy_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }


class ComfyScrapper(Scrapper):
    def __init__(self, product_url):
        super().__init__(product_url)
        self.store = "comfy"
        self.headers = comfy_headers

    def scrape(self):
        super().scrape()

        script_tag = self.soup.find("script", type="application/ld+json")
        if script_tag:
            json_data = json.loads(script_tag.string)
            self.price = json_data.get("offers", {}).get("price", 0)
            self.name = json_data.get("name", "Назва не знайдена")
        else:
            self.name = "Не знайдена"
            self.price = 0
