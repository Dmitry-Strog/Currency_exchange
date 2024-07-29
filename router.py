from controller.handler_currencies import CurrenciesHandler
from controller.handler_currency import CurrencyHandler

routers = {
    "/currency": CurrenciesHandler,
    "/currency/": CurrencyHandler,
}
