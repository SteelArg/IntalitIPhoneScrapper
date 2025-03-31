from app.scrappers.rozetka import RozetkaScrapper
from app.scrappers.comfy import ComfyScrapper
from app.scrappers.moyo import MoyoScrapper
from app.scrappers.foxtrot import FoxtrotScrapper
from app.scrappers.ctrs import CtrsScrapper

from app.utils.unified_naming import get_unified_name_as_str


def scrape_product_link(link: str):
    scrapper = None
    if "rozetka" in link:
        scrapper = RozetkaScrapper(link)
    if "comfy" in link:
        scrapper = ComfyScrapper(link)
    if "ctrs" in link:
        scrapper = CtrsScrapper(link)
    if "foxtrot" in link:
        scrapper = FoxtrotScrapper(link)
    if "moyo" in link:
        scrapper = MoyoScrapper(link)

    if scrapper is None:
        return None

    scrapper.scrape()

    if not scrapper.is_scrape_valid():
        return None

    scrapper.name = get_unified_name_as_str(scrapper.name)

    product = {
        "name": scrapper.name,
        "price": float(scrapper.price),
        "store": scrapper.store
    }

    return product
