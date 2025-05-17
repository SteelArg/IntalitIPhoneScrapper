import os
import time
import unittest

from app.database import Database

from app.model.product import Product


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db_path = "test_db.db"
        self.db = Database(self.db_path)

    def tearDown(self):
        if os.path.exists(self.db_path):
            if self.db is not None:
                self.db.close_connection()
            os.remove(self.db_path)

    def test_insert_product(self):
        self.db.insert_product(Product("product-1", 100.0, "comfy"))
        product1 = self.db.get_product("comfy", "product-1")
        print(product1.to_json())

        self.assertEqual(product1.store, "comfy")
        self.assertEqual(product1.name, "product-1")
        self.assertEqual(product1.price, 100.0)

    def test_get_newest(self):
        time_product = Product("time-product", 200.0, "comfy")
        self.db.insert_product(time_product)

        time.sleep(2)

        time_product.price = 230.0
        time_product.set_current_date()

        self.db.insert_product(time_product)

        time_product = self.db.get_product("comfy", "time-product")
        self.assertEqual(time_product.price, 230.0)

    def test_errors(self):
        with self.assertRaises(ValueError):
            self.db.insert_product(Product("product", 10.0, "fasdgf"))

        with self.assertRaises(ValueError):
            self.db.insert_product(Product("product", -20.0, "comfy"))

        self.assertEqual(self.db.get_product("comfy", "unexisting"), None)

    def test_get_store(self):
        p1_old = Product("product-1", 200.0, "moyo")

        self.db.insert_product(p1_old)
        time.sleep(2)

        p1_new = Product("product-1", 234.0, "moyo")
        self.db.insert_product(p1_new)
        self.db.insert_product(Product("product-2", 501.0, "moyo"))

        catalog = self.db.get_all_products("moyo")

        print(p1_old.date)
        print(p1_new.date)
        print(catalog.products[0].date)

        self.assertEqual(catalog.products.__len__(), 2)
        self.assertEqual(catalog.products[1].name, "product-2")
        self.assertEqual(catalog.products[0].price, 234.0)
