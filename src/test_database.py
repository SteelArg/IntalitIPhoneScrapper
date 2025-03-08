import time
import unittest

from database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database("test_db.db")

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
