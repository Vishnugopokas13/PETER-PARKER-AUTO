from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    DATABASE_URI = getenv("DATABASE_URI", "")
    DATABASE_NAME = getenv("DATABASE_NAME", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234567891:AdDfgFRFVVfDEhdhyjjvjjftSEW")
    SUDO = list(map(int, getenv("ADMINS").split()))
                       
cfg = Config()
