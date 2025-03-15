# IntalitIPhoneScrapper
This app consists of 3 components:
- **Scrapper**
- **Web API**
- **Telegram bot**

## Web API
Uses Flask REST API. Run `api.py` to start a Flask server.

Starts a **Web Server** with **API** and a **Database**

## Telegram bot

Add the secret file `telegram_bot_token.txt` containing your Telegram Bot Token. Run 

Launches a **Telegram Bot** that allows users to interact with a **Web API**.

## Scrapper

Run `scheduler.py` to start a script that **scrapes** all the links in a `scrape_links.txt` and writes the data to a **Database**.

### Scrapper Test

You can run `main.py` to scrape all the link just once.

# Config

This project contains `config.json` with project settings.
There are some fields that point to certain files in `config` folder.

You can edit the config files at your own risk.
