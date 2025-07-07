import os
from typing import List

API_ID = os.environ.get("API_ID", "29245477")
API_HASH = os.environ.get("API_HASH", "0abc83883262245c90ca337b7a0375c4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7845096754:AAGp_ydOCzsjrC89b3LOWHzuWG4gKTdK2uI")
ADMIN = int(os.environ.get("ADMIN", "7654385403"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002456565415"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "False").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "mongodb+srv://Kafka:Au3OoWzCDYJKeuHU@cluster0.lz2m8iy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "cluster0")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-100******** -100*********").split())) # Add Multiple channel ids
