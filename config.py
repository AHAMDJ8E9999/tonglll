from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "3500"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/5d9d0c0b7d9cb483f9867.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/7cf0196f135b978d6fbd3.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/VIVIVIVVIV2")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/VIVIVIVVIV2")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))


FAILED = "https://telegra.ph/file/4a02e2542052091c5f1c7.jpg"
