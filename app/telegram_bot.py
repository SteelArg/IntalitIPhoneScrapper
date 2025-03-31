import telebot
import requests

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.configuration import stores, telegram_bot_token, web_api_url

bot = telebot.TeleBot(telegram_bot_token)


def get_all_products(store: str):
    api_request = f"{web_api_url}/data/store/{store}"
    response = requests.get(api_request)
    data = eval(response.text)
    print(data)
    return data


@bot.message_handler(commands=['start'])
def handle_start(message):
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
    store_name = call.data.split("=")[1]
    products_text = ""
    products_data = get_all_products(store_name)

    for product in products_data:
        products_text += f"\n{product['name']} {str(product['price'])} грн; последн. счит. {str(product['date'])}"
    if products_text == "":
        products_text = "\nПока что нету :("

    bot.send_message(call.message.chat.id, f"Все продукты в магазине {store_name}:{products_text}")


def run_telegram_bot():
    bot.polling(non_stop=True)
