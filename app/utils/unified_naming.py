from difflib import SequenceMatcher
import logging

from app.configuration import load_product_names

# Unified product name:
# Type-Company-Product-Series-Number

# Additional:
# Color-Memory

keywords = ["Type", "Company", "Product", "Line", "Series"]

logging.basicConfig(level=logging.INFO, filename="unified_naming.log", filemode="w")


class UnifiedNamingException(Exception):
    pass


class ProductNamesReader:
    def __init__(self):
        self.data = load_product_names()

    def get_values_for(self, keyword: str):
        values = self.data[keyword]
        clean_values = []
        for value in values:
            clean_values.append(value.split(">")[0])
        return clean_values

    def fill_empty_data(self, product_data: dict):
        new_data = {}
        for key in keywords:
            if key not in product_data.keys():
                continue
            for value in self.data[key]:
                if value.split(">").__len__() < 2:
                    continue
                if product_data[key] == value.split(">")[0]:
                    for derived_value in value.split(">")[1].split(";"):
                        new_data[derived_value.split("=")[0]] = derived_value.split("=")[1]

        for key in keywords:
            if key not in new_data.keys():
                continue
            if key in product_data.keys():
                if product_data[key] != new_data[key]:
                    logging.warning(f"Conflicting info: Original - {product_data[key]}; Filled - {new_data[key]}")
                continue
            product_data[key] = new_data[key]
            logging.info(f"Filled {key} with {new_data[key]}")

        if "Series" not in product_data.keys():
            product_data["Series"] = self.get_values_for("Series")[0]
        if "Line" not in product_data.keys():
            product_data["Line"] = self.get_values_for("Line")[0]

        return product_data


reader = ProductNamesReader()


def get_unified_name_as_str(full_name):
    data = get_unified_name(full_name)
    try:
        format_name = f"{data['Type']}-{data['Company']}-{data['Product']}-{data['Line']}-{data['Series']}-{data['Number']}"
    except KeyError:
        logging.error(f"Failed to create formatted string.\nRequest: {full_name}\nData: {data}")
        raise UnifiedNamingException(f"Not enough info to create a formatted string for '{full_name}': {data}")
    return format_name


def get_unified_name(full_name: str):
    full_name = full_name.lower()
    data = {"Number": "0"}
    for word in full_name.split(" "):
        word_value = eval_word(word)
        if word_value[2] is True:
            data[word_value[0]] = word_value[1]

    data = reader.fill_empty_data(data)
    return data


def eval_word(word: str):
    word_only_letters = ''.join(x for x in word if x.isalpha())
    word_only_numbers = ''.join(x for x in word if x.isdecimal())

    data = [None, None, 0]
    for key in keywords:
        for value in reader.get_values_for(key):
            similarity: float = similar(word_only_letters, value)
            if similarity > data[2]:
                data = [key, value, similarity]

    data[2] = data[2] > 0.7

    if word_only_letters.__len__() < 2 and word_only_numbers.__len__() > 0:
        data = ["Number", word_only_numbers, True]

    logging.info(f"Evaluated {word} as: {data}")

    return data


def similar(a, b):
    if a == b:
        return 1.0
    return SequenceMatcher(None, a, b).ratio()
