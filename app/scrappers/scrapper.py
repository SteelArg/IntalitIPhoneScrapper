import requests
from bs4 import BeautifulSoup

from app.utils.logger import get_logger


default_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br"
}


class Scrapper:
    soup: BeautifulSoup

    def __init__(self, product_url, headers=default_headers):
        self.url = product_url
        self.headers = headers
        self.response = None
        self.store = None
        self.name = None
        self.price = None
        self.logger = None

    def scrape(self):
        self.logger = get_logger(f"{self.store}-scrape")
        self.load()

    def load(self):
        try:
            self.response = requests.get(self.url, headers=self.headers)

            if not self.response.status_code == 200:
                return

            self.soup = BeautifulSoup(self.response.text, "html.parser")
            self.logger.info(self.response.text)

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Bad request: {e}")

    def is_scrape_valid(self):
        return self.response.status_code == 200 and self.name is not None and self.price is not None

    def display(self):
        print(f"{self.name} from store {self.store} with price {self.price}")
