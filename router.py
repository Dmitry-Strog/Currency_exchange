from controller.handler_currencies import CurrenciesHandler
from controller.handler_currency import CurrencyHandler

routers = {
    "/currencies": CurrenciesHandler,
    "/currency/": CurrencyHandler,
}
