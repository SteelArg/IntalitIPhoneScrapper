import os
import time
import unittest

from app.database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        db_path = "test_db.db"
        if os.path.exists(db_path):
            os.remove(db_path)

        self.db = Database(db_path)

    def test_insert_product(self):
        self.db.insert_product("comfy", "product-1", 100.0)
        product1_data = self.db.get_product("comfy", "product-1")
        self.assertEqual(product1_data["store"], "comfy")
        self.assertEqual(product1_data["name"], "product-1")
        self.assertEqual(product1_data["price"], 100.0)

    def test_get_newest(self):
        self.db.insert_product("comfy", "time-product", 200.0)
        time.sleep(2)
        self.db.insert_product("comfy", "time-product", 230.0)

        time_product = self.db.get_product("comfy", "time-product")
        self.assertEqual(time_product["price"], 230.0)

    def test_errors(self):
        with self.assertRaises(ValueError):
            self.db.insert_product("fasdgf", "product", 10.0)

        with self.assertRaises(ValueError):
            self.db.insert_product("comfy", "product", -20.0)

        self.assertEqual(self.db.get_product("comfy", "unexisting"), None)

    def test_get_store(self):
        self.db.insert_product("moyo", "product-1", 200.0)
        time.sleep(1)
        self.db.insert_product("moyo", "product-1", 234.0)
        self.db.insert_product("moyo", "product-2", 501.0)

        all_products = self.db.get_all_products("moyo")

        self.assertEqual(all_products.__len__(), 2)
        self.assertEqual(all_products[1]["name"], "product-2")
        self.assertEqual(all_products[0]["price"], 234.0)
