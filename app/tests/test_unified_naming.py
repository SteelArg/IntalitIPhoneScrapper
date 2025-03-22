import unittest

from app.utils.unified_naming import get_unified_name, get_unified_name_as_str, UnifiedNamingException


class TestUnifiedNaming(unittest.TestCase):
    def test_iphone_str(self):
        readable_name = "Мобільний телефон Apple iPhone 16 Pro 128GB Black Titanium (MYND3SX/A)"
        expected_db_name = "phone-apple-iphone-default-pro-16"
        self.assertEqual(get_unified_name_as_str(readable_name), expected_db_name)

    def test_not_enough_info_str(self):
        readable_name = "Мобільний телефон Apple"
        with self.assertRaises(UnifiedNamingException):
            get_unified_name_as_str(readable_name)

    def test_iphone_dict(self):
        readable_name = "Мобільний телефон Apple iPhone 16 Pro 128GB Black Titanium (MYND3SX/A)"
        expected_dict = {
            "Type": "phone",
            "Company": "apple",
            "Product": "iphone",
            "Line": "default",
            "Series": "pro",
            "Number": "16"
        }
        self.assertEqual(get_unified_name(readable_name), expected_dict)

    def test_not_enough_info_dict(self):
        readable_name = "Мобільний телефон Apple"
        expected_dict = {
            "Company": "apple",
            "Line": "default",
            "Series": "default",
            "Number": "0"
        }
        self.assertEqual(get_unified_name(readable_name), expected_dict)

    def test_not_enough_info_dict_2(self):
        readable_name = "Мобільний телефон Apple Galaxy 234"
        expected_dict = {
            "Company": "apple",
            "Type": "phone",
            "Product": "galaxy",
            "Line": "default",
            "Series": "default",
            "Number": "234"
        }
        self.assertEqual(get_unified_name(readable_name), expected_dict)
