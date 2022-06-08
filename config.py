import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "𝑾𝑶𝑹𝑳𝑫 𝑴𝑼𝑺𝑰𝑪 💗ˣ")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Gr_World_Music")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Ch_World_Music")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1491415522 1419419100 2112059230").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg")
