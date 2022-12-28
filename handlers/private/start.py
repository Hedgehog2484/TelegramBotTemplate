from aiogram.types import Message, ChatType
from aiogram.dispatcher.filters import ChatTypeFilter

from keyboards.reply import ExampleReplyMarkup


async def start_msg(m: Message) -> None:
    await m.answer("Hello! I am bot!", reply_markup=ExampleReplyMarkup().get())


def setup_start(dp) -> None:
    dp.register_message_handler(start_msg, ChatTypeFilter(ChatType.PRIVATE), commands=["start"])
