import time

from app.configuration import stores
from app.utils.json_serializer import JsonSerializable


# Get current date and time as a string
def get_current_date():
    return str(time.strftime("%Y-%m-%d-%H-%M-%S"))


# Format a product name removing "bad" symbols
def format_product_name(old_name: str):
    bad_symbols = [" ", "/", "(", ")"]
    new_name = old_name
    for symbol in bad_symbols:
        new_name = new_name.replace(symbol, "-")
    return new_name


class Product(JsonSerializable):
    name: str
    price: float
    store: str
    link: str
    date: str

    def __init__(self, name, price, store, link, date=None):
        self.name = name
        self.price = price
        self.store = store
        self.link = link
        self.date = date

        self.validate()

    def validate(self):
        self.name = format_product_name(self.name)
        self.price = float(self.price)

        if self.store not in stores:
            raise ValueError(f"Store {self.store} does not exist")
        if self.price <= 0:
            raise ValueError(f"Price must be higher than 0 ({self.price})")

        if self.date is None:
            self.set_current_date()

    def set_current_date(self):
        self.date = get_current_date()
