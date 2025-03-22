import os

file_dir = os.path.dirname(os.path.abspath(__file__))
abs_path = file_dir

if not os.path.isfile(os.path.join(abs_path, "config.json")):
    abs_path = os.path.join(abs_path, os.pardir)

config_path = os.path.join(abs_path, "config")

telebot_token = ""
product_names = {}
scrape_links = []

with open(os.path.join(abs_path, "config.json"), "r", encoding='utf-8') as file:
    config_data = eval(file.read())

try:
    with open(os.path.join(config_path, config_data['telegram_token']), "r", encoding='utf-8') as file:
        telebot_token = file.read()
except FileNotFoundError:
    pass

try:
    with open(os.path.join(config_path, config_data['product_names']), "r", encoding='utf-8') as file:
        product_names = eval(file.read())
except FileNotFoundError:
    pass

try:
    with open(os.path.join(config_path, config_data['scrape_links']), "r", encoding='utf-8') as file:
        scrape_links = file.read().split("\n")
except FileNotFoundError:
    pass

stores = config_data["stores"]

logs_dir = f"{abs_path}\\logs"

web_api_url = config_data["web_api_url"]


def get_db_path():
    return f"{abs_path}\\{config_data['db']}"


def get_telegram_bot_token():
    return telebot_token


def load_product_names():
    return product_names


def get_scrape_links():
    return scrape_links


def get_stores():
    return stores


def get_logs_dir():
    return logs_dir
