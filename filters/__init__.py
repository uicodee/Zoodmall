from .filters import is_user

from loader import dp
# from .is_admin import AdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(is_user)
