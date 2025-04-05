import telebot
import requests

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from app.configuration import stores, telegram_bot_token, web_api_url
import app.telebot.telegram_bot_prettify as prettify

bot = telebot.TeleBot(telegram_bot_token)


def get_all_products(store: str):
    api_request = f"{web_api_url}/data/store/{store}"
    response = requests.get(api_request)
    data = eval(response.text)
    print(data)
    return data


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет!", reply_markup=ReplyKeyboardRemove())

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="Просмотреть все товары", callback_data="read_from_store"))

    bot.send_message(message.chat.id, "Что вы хотите?", reply_markup=markup)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "Тебе ничто не поможет")


@bot.callback_query_handler(func=lambda call: call.data == "read_from_store")
def read_from_store(call):
    markup = telebot.types.InlineKeyboardMarkup()
    store_buttons = []
    for store in stores:
        store_buttons.append(InlineKeyboardButton(text=store, callback_data=f"read_from_store={store}"))
    markup.row(*store_buttons)

    bot.send_message(call.message.chat.id, "Выберите магазин", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith("read_from_store="))
def read_from_store(call):
    store = call.data.split("=")[1]
    products_data = get_all_products(store)

    products_text = ""
    store_name = prettify.get_store(store)

    for product in products_data:
        products_text += "\n" + prettify.get_product_text(product)
    if products_text == "":
        products_text = "\nПока что нету :("

    bot.send_message(call.message.chat.id, f"Все продукты в магазине {store_name}:{products_text}")


def run_telegram_bot():
    bot.polling(non_stop=True)
