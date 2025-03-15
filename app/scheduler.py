import time
import schedule

from web_scrapper import scrape_product_link
from database import Database
from app.config import get_db_path, scrape_links

db = Database(get_db_path())


def scrape_links_job():
    for link in scrape_links:
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
