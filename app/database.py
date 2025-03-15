import sqlite3
import time

from app.config import stores


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


# Raise error for bad parameters
def check_parameters(store: str, price=1.0):
    if store not in stores:
        raise ValueError(f"Store {store} does not exist")
    if price <= 0:
        raise ValueError(f"Price must be higher than 0 ({price})")


class Database:
    def __init__(self, filename):
        self.con = sqlite3.connect(filename, check_same_thread=False)
        self.cur = self.con.cursor()
        self.create_tables()

    def create_tables(self):
        for store in stores:
            self.create_table_for_store(store)
        self.con.commit()

    def create_table_for_store(self, store):
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {store} (name text, price real, date text)")

    def insert_product(self, store, name, price: float):
        check_parameters(store, price)

        name = format_product_name(name)
        date = get_current_date()

        self.cur.execute(f"INSERT INTO {store} VALUES ('{name}', {price}, '{date}')")
        self.con.commit()

        return name

    def update_product(self, store, name, price):
        check_parameters(store, price)

        date = get_current_date()
        self.cur.execute(f"UPDATE {store} SET date='{date}', price='{price}' WHERE name='{name}'")
        self.con.commit()

    def get_product(self, store, name):
        check_parameters(store)

        self.cur.execute(f"SELECT * FROM {store} WHERE name='{name}' ORDER BY date DESC")
        fetch = self.cur.fetchall()
        if fetch.__len__() == 0:
            return None
        else:
            data = {
                "name": name,
                "store": store,
                "price": float(fetch[0][1]),
                "date": fetch[0][2]
            }
            return data

    def get_all_products(self, store):
        check_parameters(store)

        self.cur.execute(f"SELECT * FROM {store}")
        fetch = self.cur.fetchall()
        return fetch

    def delete_product(self, store, name):
        check_parameters(store)

        self.cur.execute(f"DELETE FROM {store} WHERE name='{name}'")
        self.con.commit()
