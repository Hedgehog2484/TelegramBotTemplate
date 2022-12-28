from handlers.private.start import setup_start
from handlers.private.send_inline import setup_inline


def setup_private(dp) -> None:
    setup_start(dp)
    setup_inline(dp)
