import time
import logging
from decouple import config
from telethon import TelegramClient

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
TOKEN = config("TOKEN", default=None)

GogoAnime = TelegramClient('bot', APP_ID, API_HASH).start(bot_token=TOKEN)
