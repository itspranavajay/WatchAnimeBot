import os
import time
import logging
from telethon import TelegramClient, events

StartTime = time.time()
logging.basicConfig(level=logging.INFO)

API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN

GogoAnime = TelegramClient('bot', API_ID, API_HASH).start(bot_token=TOKEN)
