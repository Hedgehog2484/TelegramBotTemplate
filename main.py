import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.executor import start_polling
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils import setup_logger
from filters import setup_filters
from handlers import setup_handlers
from middlewares import setup_middlewares
from load_config import TOKEN, DATABASE_PATH
from services import ConnectionsFactory, DatabaseController


async def on_startup(dp: Dispatcher):
    """ Setup all bot services and save some data to the bot before start. """
    setup_logger()
    setup_filters(dp)
    setup_handlers(dp)
    setup_middlewares(dp)

    db = DatabaseController(await ConnectionsFactory(DATABASE_PATH).create())
    await db.create_db()
    await db.commit()
    bot = dp.bot
    bot["db"] = db

    logging.info("Bot started.")


async def on_shutdown(dp: Dispatcher):
    """ Stoping all bot services, that need it. """
    await dp.bot["db"].disconnect()


def main():
    bot = Bot(TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())
    start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
