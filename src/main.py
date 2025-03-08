from database import Database

from web_scrapper import scrape_product_link

with open("scrape_links.txt", "r", encoding="utf-8") as file:
    links = file.read().split("\n")

db = Database("products.db")


def main():
    for link in links:
        product = scrape_product_link(link)
        if product is None:
            print(f"Failed to scrape link: {link}")
            continue
        db.insert_product(product["store"], product["name"], product["price"])


if __name__ == "__main__":
    main()
