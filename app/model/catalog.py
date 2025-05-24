from typing import List

from app.configuration import stores
from app.utils.json_serializer import JsonSerializable
from app.model.product import Product


class Catalog(JsonSerializable):
    store: str
    products: List[Product]

    def __init__(self, store, products):
        self.store = store
        self.products = products

        self.validate()

    def validate(self):
        if self.store not in stores:
            raise ValueError(f"Store {self.store} does not exist")
