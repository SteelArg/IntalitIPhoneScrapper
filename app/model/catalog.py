from app.configuration import stores
from app.utils.json_serializer import JSONSerializer


class Catalog(JSONSerializer):
    def __init__(self, store, products):
        self.store = store
        self.products = products

        self.validate()

    def validate(self):
        if self.store not in stores:
            raise ValueError(f"Store {self.store} does not exist")

    def __dict__(self):
        store_dict = {
            "store": self.store,
            "products": [product.to_json() for product in self.products]
        }
        return store_dict
