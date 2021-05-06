import os
import time
import logging
from telethon import TelegramClient, events

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("TOKEN", None)

GogoAnime = TelegramClient('GogoAnime', APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
