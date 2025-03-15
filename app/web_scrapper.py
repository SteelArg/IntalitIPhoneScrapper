from scrappers.rozetka import RozetkaScrapper
from scrappers.comfy import ComfyScrapper
from scrappers.moyo import MoyoScrapper
from scrappers.foxtrot import FoxtrotScrapper
from scrappers.ctrs import CtrsScrapper

from utils.unified_naming import get_unified_name_as_str


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

    if scrapper.price == 0:
        return None

    scrapper.name = get_unified_name_as_str(scrapper.name)

    product = {
        "name": scrapper.name,
        "price": scrapper.price,
        "store": scrapper.store
    }

    return product
