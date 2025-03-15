import telebot
import requests

from configuration import stores, get_telegram_bot_token, web_api_url

bot = telebot.TeleBot(get_telegram_bot_token())

# Url pointing to your Web API
url = web_api_url


def get_all_products(store: str):
    api_request = f"{url}/data/store/{store}"
    response = requests.get(api_request)
    data = eval(response.text)
    return data


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row(*stores)
    bot.send_message(message.chat.id, "Выберите магазин", reply_markup=keyboard)


@bot.message_handler(commands=['start', 'help'])
def handle_command(message):
    if message.text == '/start':
        bot.reply_to(message, "Хай")
    elif message.text == '/help':
        bot.reply_to(message, "Тебе ничто не поможет")


@bot.message_handler()
def handle_message(message: telebot.types.Message):
    store_name = message.text.lower()
    if store_name in stores:
        products_text = ""
        products_data = get_all_products(store_name)
        for product in products_data:
            products_text += f"\n{product['name']} {str(product['price'])} грн; последн. счит. {str(product['date'])}"
        if products_text == "":
            products_text = "\nПока что нету :("
        bot.send_message(message.chat.id, f"Все продукты в магазине {message.text}:{products_text}")
    else:
        bot.reply_to(message, f"Не понимаю {message.text}")


def run_telegram_bot():
    bot.polling(non_stop=True)


if __name__ == "__main__":
    run_telegram_bot()
