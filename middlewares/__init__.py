from loader import dp
from .throttling import ThrottlingMiddleware
from .language import ACLMiddleware
from loader import I18N_DOMAIN


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(ACLMiddleware(domain=I18N_DOMAIN))
