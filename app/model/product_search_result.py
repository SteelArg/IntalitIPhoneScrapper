from typing import List

from app.utils.json_serializer import JsonSerializable
from app.model.product import Product


class ProductSearchResult(JsonSerializable):
    search_keywords: List[str]
    products: List[Product]

    def __init__(self, search_keywords, products):
        self.search_keywords = search_keywords
        self.products = products

        self.validate()

    def validate(self):
        for product in self.products:
            product.validate()
