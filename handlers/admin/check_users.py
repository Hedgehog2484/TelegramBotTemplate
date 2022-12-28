from aiogram.types import Message, ChatType
from aiogram.dispatcher.filters import ChatTypeFilter


async def check_users_count(m: Message) -> None:
    users = await m.bot["db"].get_all_users()
    await m.answer(f"Users in database: {len(users)}")


def setup_check_users(dp) -> None:
    # The bot will be send the number of users in the database if admin sends '/users' command.
    dp.register_message_handler(check_users_count, commands=["users"], is_admin=True)
