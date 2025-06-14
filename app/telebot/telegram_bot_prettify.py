import app.telebot.telegram_bot_phrases as phrases

phone_emoji = "📱"

store_prettifies = {
    "moyo": "MOYO",
    "ctrs": "CTRS"
}

name_prettifies = {
    "iphone": "IPhone",
    "pro": "Pro"
}


def get_search_result_text(search_result, search_keywords):
    search_text = f"{phrases.text_search_result} {'; '.join(search_keywords)}:"

    products_text = ""
    for product in search_result.products:
        products_text += "\n" + get_product_text(product)

    if search_result.products.__len__() == 0:
        products_text = phrases.text_search_result_none

    return f"{search_text}\n{products_text}"


def get_product_text(product):
    name = prettify_product_name(product.name, product.link)
    price = prettify_product_price(product.price)
    date = prettify_product_date(product.date)

    text = f"{name} - {price};   {date}"

    return text


def prettify_store_name(store: str):
    if store_prettifies.__contains__(store):
        return store_prettifies[store]

    prettified_store = store[0].upper()
    prettified_store += store[1:]

    return prettified_store


def prettify_product_name(product_name, link=None):
    words = product_name.split("-")

    text = ""
    if "phone" in words:
        text += phone_emoji + " "

    prettified_words = []
    for word in words:
        if word.isdecimal():
            prettified_words.append(word)
            continue
        if name_prettifies.__contains__(word):
            prettified_words.append(name_prettifies[word])

    text += " ".join(prettified_words)

    if text == "":
        for word in words:
            text += word[0].upper() + word[1:] + " "
        text = text[0:-1]

    if link is not None:
        return f"[{text}]({link})"
    else:
        return text


def prettify_product_price(product_price):
    return f"{str(product_price)} {phrases.abbreviation_currency}"


def prettify_product_date(product_date):
    date_numbers = product_date.split("-")

    date = f"{date_numbers[2]}.{date_numbers[1]}.{date_numbers[0]}"
    time = f"{date_numbers[3]}:{date_numbers[4]}:{date_numbers[5]}"

    prettified_date = f"{date} {time}"

    return f"{phrases.abbreviation_last_read} {prettified_date}"
