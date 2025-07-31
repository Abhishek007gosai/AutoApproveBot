import os
from typing import List

API_ID = os.environ.get("API_ID", "29245477")
API_HASH = os.environ.get("API_HASH", "0abc83883262245c90ca337b7a0375c4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "7654385403"))
PICS = (os.environ.get("PICS", "https://files.catbox.moe/gyklg0.jpg")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002456565415"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "True"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "cluster0")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "True"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002456565415").split())) # Add Multiple channel ids
