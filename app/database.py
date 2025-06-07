import sqlite3

from app.configuration import stores

from app.model.product import Product
from app.model.catalog import Catalog


def validate_store(store):
    if store not in stores:
        raise ValueError(f"Store {store} does not exist")


class Database:
    def __init__(self, filename):
        self.con = sqlite3.connect(filename, check_same_thread=False)
        self.cur = self.con.cursor()
        self.create_tables()

    def close_connection(self):
        self.con.close()

    def create_tables(self):
        for store in stores:
            self.create_table_for_store(store)
        self.con.commit()

    def create_table_for_store(self, store):
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {store} (name text, price real, link text, date text)")

    def insert_product(self, product: Product):
        self.cur.execute(f"INSERT INTO {product.store} VALUES ('{product.name}', {str(product.price)}, '{product.link}', '{product.date}')")
        self.con.commit()

    def update_product(self, product: Product):
        self.cur.execute(f"UPDATE {product.store} SET date='{product.date}', price='{product.price}' WHERE name='{product.name}'")
        self.con.commit()

    def get_product(self, store, name):
        validate_store(store)

        self.cur.execute(f"SELECT * FROM {store} WHERE name='{name}' ORDER BY date DESC")
        fetch = self.cur.fetchall()
        if fetch.__len__() == 0:
            return None
        else:
            product = Product(name, float(fetch[0][1]), store, fetch[0][2], fetch[0][3])
            return product

    def get_all_products(self, store):
        validate_store(store)

        product_names = [name[0] for name in self.cur.execute(f"SELECT name FROM {store}")]
        product_names = list(dict.fromkeys(product_names))

        all_products = []

        for product_name in product_names:
            all_products.append(self.get_product(store, product_name))

        catalog = Catalog(store, all_products)

        return catalog

    def delete_product(self, store, name):
        validate_store(store)

        self.cur.execute(f"DELETE FROM {store} WHERE name='{name}'")
        self.con.commit()
