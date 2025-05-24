# IntalitIPhoneScrapper

This app consists of 3 components:
- **Scrapper**
- **Web API**
- **Telegram bot**


## Web API

Uses Flask REST API. Run `run_flask.py` to start a Flask server.

Starts a **Web Server** with **API** and a **Database**

### API Tests

Run `test_database.py` to test the datatbase.


## Telegram bot

Run `run_telebot.py`

Launches a **Telegram Bot** that allows users to interact with a **Web API**.

Set the bot token in a "TELEBOT_TOKEN" environmental variable.


## Scrapper

Run `run_scrapper.py` to start a script that **scrapes** all the links in a `config/scrape_links.txt` every day and sends the data to the **Web API**.

### Scrapper Tests

Run `test_unified_naming.py` to test the unified naming.

---

# Config

This project contains `config.json` with project settings.
There are some fields that point to certain files in `config` folder.

You can edit the config files at your own risk.

Make an environmental variable "WEB_API_URL" that contains a URL pointing to the **Web API**.
