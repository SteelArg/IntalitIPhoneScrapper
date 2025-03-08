import time
import schedule

from web_scrapper import scrape_product_link
from database import Database

with open("scrape_links.txt", "r", encoding="utf-8") as file:
    links = file.read().split("\n")

db = Database("products.db")


def scrape_links_job():
    for link in links:
        product = scrape_product_link(link)
        if product is None:
            print(f"Failed to scrape link: {link}")
            continue
        db.insert_product(product["store"], product["name"], product["price"])
    print("Scraped links")


def main_loop():
    scrape_links_job()
    schedule.every().day.do(scrape_links_job)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main_loop()
