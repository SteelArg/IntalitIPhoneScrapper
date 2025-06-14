import requests

from app.model.catalog import Catalog
from app.model.product_search_result import ProductSearchResult

from app.configuration import web_api_url


def get_catalog(store: str):
    api_request = f"{web_api_url}/data/store/{store}"
    response = requests.get(api_request)

    data = eval(response.text)
    print(data)

    catalog = Catalog.from_json(response.text)
    return catalog


def get_search_result(keywords):
    api_request = f"{web_api_url}/data/search"
    response = requests.get(api_request, data={"keywords": str(keywords)})

    data = eval(response.text)
    print(data)

    search_result = ProductSearchResult.from_json(data)
    return search_result
