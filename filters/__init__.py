from filters.is_admin import AdminFilter


def setup_filters(dp) -> None:
    dp.filters_factory.bind(AdminFilter)
