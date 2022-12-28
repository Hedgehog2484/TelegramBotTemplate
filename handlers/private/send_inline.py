from aiogram.types import Message, ChatType, CallbackQuery
from aiogram.dispatcher.filters import ChatTypeFilter

from keyboards.inline import ExampleMarkup
from keyboards.reply import ExampleReplyMarkup


async def send_inline(m: Message) -> None:
    await m.answer("Press the btn", reply_markup=ExampleMarkup().get())


async def answer_inline_btn(c: CallbackQuery, callback_data: dict) -> None:
    await c.answer()  # You must have this line necessarily.
    await c.message.answer(f"You pressed {callback_data.get('number')} button")


def setup_inline(dp) -> None:
    dp.register_message_handler(send_inline, ChatTypeFilter(ChatType.PRIVATE), text=[ExampleReplyMarkup.test_btn_text])
    dp.register_callback_query_handler(answer_inline_btn, ExampleMarkup.callback_data.filter())
