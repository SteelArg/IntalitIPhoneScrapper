import time

import requests
import schedule
from app.utils.logger import get_logger

from app.web_scrapper import scrape_product_link
from app.database import Database
from app.configuration import get_db_path, scrape_links, web_api_url

db = Database(get_db_path())

logger = get_logger("scheduler", True)


def scrape_links_job():
    logger.info("Scrape links started")
    for link in scrape_links:
        product = scrape_product_link(link)
        if product is None:
            logger.error(f"Failed to scrape link: {link}")
            continue

        post_request = requests.post(f"{web_api_url}/data/product/{product['store']}", data=product)
        logger.info(f"Post Request to API: {post_request.status_code}")
    logger.info("Scrape links finished")


def main_loop():
    scrape_links_job()
    schedule.every().day.do(scrape_links_job)
    while True:
        schedule.run_pending()
        time.sleep(60)
