from handlers.admin.check_users import setup_check_users


def setup_admin(dp) -> None:
    setup_check_users(dp)
