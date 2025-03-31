from app.scrappers.scrapper import Scrapper

ctrs_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }


class CtrsScrapper(Scrapper):
    def __init__(self, product_url):
        super().__init__(product_url)
        self.store = "ctrs"
        self.headers = ctrs_headers

    def scrape(self):
        super().scrape()

        price_element = self.soup.find("div", class_="Price_price__KKCnw")
        if price_element:
            self.price = price_element.get("data-price", 0)

        title_meta = self.soup.find("meta", {"property": "og:title"})
        if title_meta:
            self.name = title_meta.get("content", "Назва не знайдена")
