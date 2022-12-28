from aiogram.types import Message, ChatType
from aiogram.dispatcher.filters import ChatTypeFilter


async def test_groups_msg(m: Message) -> None:
    await m.reply("Hello!")


def setup_test_groups_msg(dp) -> None:
    """ Setup groups test message handler. The bot will be answer 'hello!' on the every msg in the group. """
    dp.register_message_handler(test_groups_msg, ChatTypeFilter([ChatType.GROUP, ChatType.SUPERGROUP]))
