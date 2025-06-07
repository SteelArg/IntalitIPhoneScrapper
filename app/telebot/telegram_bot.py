import telebot

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from app.configuration import stores, telegram_bot_token
import app.telebot.telegram_bot_requests as requests
import app.telebot.telegram_bot_prettify as prettify
import app.telebot.telegram_bot_phrases as phrases

bot = telebot.TeleBot(telegram_bot_token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, phrases.text_start, reply_markup=ReplyKeyboardRemove())

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=phrases.option_main_read, callback_data="read_from_store_select"))

    bot.send_message(message.chat.id, phrases.text_menu, reply_markup=markup)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, phrases.text_user_help)


@bot.callback_query_handler(func=lambda call: call.data == "read_from_store_select")
def read_from_store_select(call):
    markup = telebot.types.InlineKeyboardMarkup()
    store_buttons = []
    for store in stores:
        button = InlineKeyboardButton(text=prettify.prettify_store_name(store), callback_data=f"read_from_store={store}")
        store_buttons.append(button)
    markup.row(*store_buttons)

    bot.send_message(call.message.chat.id, phrases.text_read_menu, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith("read_from_store="))
def read_from_store(call):
    store = call.data.split("=")[1]
    catalog = requests.get_catalog(store)

    products_text = ""
    store_name = prettify.prettify_store_name(catalog.store)

    for product in catalog.products:
        products_text += "\n" + prettify.get_product_text(product)
    if products_text == "":
        products_text = f"\n{phrases.text_read_no_products}"

    bot.send_message(call.message.chat.id,
                     f"{phrases.text_read_store} {store_name} ({len(catalog.products)}):{products_text}",
                     parse_mode='Markdown')


def run_telegram_bot():
    bot.polling(non_stop=True)
