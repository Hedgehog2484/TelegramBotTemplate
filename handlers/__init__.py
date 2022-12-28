from handlers.admin import setup_admin
from handlers.groups import setup_groups
from handlers.private import setup_private


def setup_handlers(dp) -> None:
    setup_admin(dp)
    setup_groups(dp)
    setup_private(dp)
