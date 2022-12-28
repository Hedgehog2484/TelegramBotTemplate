import json


with open("config.json", mode="r", encoding="utf-8") as cfg:
    data = json.loads(cfg.read())

    TOKEN = data.get("bot_token")
    DATABASE_PATH = data.get("database_filepath")
    ADMINS = data.get("admins_id")
