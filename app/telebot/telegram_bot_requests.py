import requests

from app.model.catalog import Catalog

from app.configuration import web_api_url


def get_catalog(store: str):
    api_request = f"{web_api_url}/data/store/{store}"
    response = requests.get(api_request)

    data = eval(response.text)
    print(data)

    catalog = Catalog.from_json(response.text)
    return catalog
