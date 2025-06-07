import os
from dotenv import load_dotenv

abs_path = os.getcwd()
config_path = os.path.join(abs_path, "config")
logs_path = os.path.join(abs_path, "logs")

if not os.path.exists(logs_path):
    os.mkdir(logs_path)

dotenv_path = os.path.join(abs_path, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

product_names = {}
scrape_links = []

with open(os.path.join(abs_path, "config.json"), "r", encoding='utf-8') as file:
    config_data = eval(file.read())

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

web_api_url = os.environ.get("WEB_API_URL")
telegram_bot_token = os.environ.get("TELEBOT_TOKEN")
admin_password = os.environ.get("ADMIN_PASSWORD")

if admin_password is None:
    raise ValueError("Set the Admin password in the environmental variables!")


def get_db_path():
    return f"{abs_path}\\{config_data['db']}"


def get_log_path_for(filename):
    return os.path.join(logs_path, f"{filename}.log")
